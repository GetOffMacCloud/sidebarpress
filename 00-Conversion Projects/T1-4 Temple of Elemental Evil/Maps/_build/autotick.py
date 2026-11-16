"""autotick.py: extract tick-marked slope/contour lines from a grey-rock node scan.
Reads maps/dg/<k>_I.png + _meta (lattice) and writes <k>_autotick.json: [{'pts': [...], 'side': +-1}]
usage: autotick.py k zone_polys_json T"""
import sys, json, cv2, numpy as np
from skimage.morphology import skeletonize
k = sys.argv[1]; zones = json.loads(sys.argv[2]) if len(sys.argv) > 2 else None; T = float(sys.argv[3]) if len(sys.argv) > 3 else 175
I = cv2.imread(f'maps/dg/{k}_I.png', 0); H, W = I.shape
m = json.load(open(f'maps/dg/{k}_meta.json')); PX, OX, PY, OY = m['lattice']
rock = cv2.morphologyEx((I < 200).astype(np.uint8), cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9)))
rock = cv2.dilate(rock, np.ones((3, 3), np.uint8))
yy, xx = np.mgrid[0:H, 0:W]
dvx = np.abs(((xx - OX) / PX - np.round((xx - OX) / PX)) * PX); dvy = np.abs(((yy - OY) / PY - np.round((yy - OY) / PY)) * PY)
onv, onh = dvx <= 2, dvy <= 2
raw = ((I < T) & (rock == 0)).astype(np.uint8)
side_h = (np.roll(raw, 3, 1) | np.roll(raw, -3, 1) | np.roll(raw, 4, 1) | np.roll(raw, -4, 1)).astype(bool)
side_v = (np.roll(raw, 3, 0) | np.roll(raw, -3, 0) | np.roll(raw, 4, 0) | np.roll(raw, -4, 0)).astype(bool)
g = (onv & ~side_h) | (onh & ~side_v)
# inpaint the grid away in the grey image so lines stay continuous across grid crossings
gm = (cv2.dilate((onv | onh).astype(np.uint8), np.ones((3, 3), np.uint8)) & (rock == 0)).astype(np.uint8)
Ji = cv2.inpaint(I, gm, 3, cv2.INPAINT_TELEA)
ink = ((Ji < T) & (rock == 0)).astype(np.uint8)
zm = np.ones((H, W), np.uint8)
if zones:
    zm[:] = 0
    for z in zones: cv2.fillPoly(zm, [np.array(z, np.int32)], 1)
ink &= zm
for (a, b, c, d) in (json.loads(sys.argv[4]) if len(sys.argv) > 4 else []): ink[b:d, a:c] = 0
# main stroke: the line is ~2-4 px; ticks hang off it. Close, skeletonize, prune spurs.
ink_c = cv2.morphologyEx(ink, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7)))
ink_c = cv2.morphologyEx(ink_c, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)))
cv2.imwrite(f'/tmp/{k}_inkc.png', ink_c * 255)
sk = skeletonize(ink_c.astype(bool)).astype(np.uint8)
K = np.ones((3, 3), np.float32)
def nb(s): return cv2.filter2D(s, -1, K, borderType=cv2.BORDER_CONSTANT) - s
for it in range(14):          # prune ends up to 10 px (ticks are ~3-6 px)
    e = (sk == 1) & (nb(sk) <= 1)
    sk[e] = 0
# link fragments broken at grid crossings: join endpoints within LINK px whose tangents roughly agree
LINK = 14
for _round in range(3):
    n0, lab0 = cv2.connectedComponents(sk, connectivity=8)
    ey, ex = np.nonzero((sk == 1) & (nb(sk) == 1))
    E = []
    for x, y in zip(ex, ey):
        # tangent from the endpoint back along its branch (~6 px)
        win = sk[max(y - 6, 0):y + 7, max(x - 6, 0):x + 7]; wy, wx = np.nonzero(win)
        wx = wx + max(x - 6, 0); wy = wy + max(y - 6, 0)
        c = np.array([wx.mean(), wy.mean()]); t = np.array([x, y], float) - c; t /= np.linalg.norm(t) + 1e-6
        E.append((x, y, t, lab0[y, x]))
    used = set()
    for i, (x, y, t, l) in enumerate(E):
        if i in used: continue
        best = None
        for j, (x2, y2, t2, l2) in enumerate(E):
            if j == i or j in used or l2 == l: continue
            d = np.array([x2 - x, y2 - y], float); L = np.linalg.norm(d)
            if L > LINK or L < 1: continue
            dn = d / L
            if np.dot(t, dn) < 0.5 or np.dot(t2, -dn) < 0.5: continue
            sc = L - 6 * (np.dot(t, dn) + np.dot(t2, -dn))
            if best is None or sc < best[0]: best = (sc, j)
        if best:
            j = best[1]; cv2.line(sk, (int(x), int(y)), (int(E[j][0]), int(E[j][1])), 1, 1); used |= {i, j}
    sk = skeletonize(sk.astype(bool)).astype(np.uint8)
n, lab, st, _ = cv2.connectedComponentsWithStats(sk, 8)
paths = []
for i in range(1, n):
    if st[i, 4] < 40: continue
    comp = (lab == i).astype(np.uint8)
    ys, xs = np.nonzero(comp); pts = list(zip(xs.tolist(), ys.tolist())); ps = set(pts)
    def nbrs(p): return [(p[0] + dx, p[1] + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if (dx or dy) and (p[0] + dx, p[1] + dy) in ps]
    deg = {p: len(nbrs(p)) for p in pts}
    ends = [p for p in pts if deg[p] == 1]
    from collections import deque
    def bfs(src):
        dist = {src: 0}; par = {src: None}; q = deque([src])
        while q:
            c = q.popleft()
            for n_ in nbrs(c):
                if n_ not in dist: dist[n_] = dist[c] + 1; par[n_] = c; q.append(n_)
        far = max(dist, key=dist.get); return far, par
    closed_loop = len(ends) == 0
    if closed_loop:
        cut = pts[0]; ps.discard(cut)
        start = next(iter(ps))
    else:
        start = ends[0]
    u, _ = bfs(start); v, par = bfs(u)
    order = []; c = v
    while c is not None: order.append(c); c = par[c]
    if len(order) < 30: continue
    P = np.array(order, float)
    closed = closed_loop or np.hypot(*(P[0] - P[-1])) < 6
    # smooth
    w = 7; Kk = np.ones(w) / w
    mode = 'wrap' if closed else 'edge'
    Ps = np.column_stack([np.convolve(np.pad(P[:, 0], w // 2, mode=mode), Kk, 'valid'), np.convolve(np.pad(P[:, 1], w // 2, mode=mode), Kk, 'valid')])
    Ps = Ps[::3]
    if closed: Ps = np.vstack([Ps, Ps[:1]])
    # tick side: ink count 3-6 px each side
    sc = [0, 0]
    for j in range(1, len(Ps) - 1):
        d = Ps[j + 1] - Ps[j - 1]; d /= np.linalg.norm(d) + 1e-6; nrm = np.array([-d[1], d[0]])
        for s_i, sg in enumerate((1, -1)):
            for r in (3, 4, 5, 6):
                q = (Ps[j] + sg * r * nrm).round().astype(int)
                if 0 <= q[0] < W and 0 <= q[1] < H and ink[q[1], q[0]]: sc[s_i] += 1
    side = 1 if sc[0] >= sc[1] else -1
    paths.append({'pts': [[round(float(a), 1), round(float(b), 1)] for a, b in Ps], 'side': side, 'closed': bool(closed), 'score': sc})
json.dump(paths, open(f'maps/dg/{k}_autotick.json', 'w'))
v = cv2.cvtColor(I, cv2.COLOR_GRAY2BGR)
for p in paths:
    P = np.array(p['pts'], np.int32); cv2.polylines(v, [P], False, (0, 0, 255), 1)
    for j in range(2, len(P) - 2, 4):
        d = (P[j + 1] - P[j - 1]).astype(float); d /= np.linalg.norm(d) + 1e-6; nrm = np.array([-d[1], d[0]]) * p['side']
        q = (P[j] + 5 * nrm).astype(int); cv2.line(v, tuple(P[j]), tuple(q), (0, 160, 0), 1)
cv2.imwrite(f'/tmp/{k}_autotick.png', v)
print(len(paths), 'paths')
