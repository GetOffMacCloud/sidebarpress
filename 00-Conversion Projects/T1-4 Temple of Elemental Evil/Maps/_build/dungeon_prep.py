"""Prepare a TSR grey-rock dungeon map (T2-4 Maps 12-19) for inktrace.
Tones: rock ~85 grey, printed linework/grid ~15 black, floor ~245 white.
Output: a clean black/white image where rock + features are black and the printed floor grid is removed,
plus an OCR'd label list (numbers, letters, S) with boxes.

usage: python3 dungeon_prep.py PAGE.jpg OUT_PREFIX [x0,y0,x1,y1]
"""
import sys, json, cv2, numpy as np, pytesseract

C = {}
exec(open(sys.argv[1]).read(), C)
src, out = C['PAGE'], C['OUT']
PROTECT, UNPROTECT = C.get('PROTECT', []), C.get('UNPROTECT', [])
S = cv2.imread(src, 0)
if 'BOX' in C:
    x0, y0, x1, y1 = C['BOX']
else:
    d = S < 200
    rows = np.where(d.mean(1) > 0.5)[0]; cols = np.where(d.mean(0) > 0.5)[0]
    x0, y0, x1, y1 = cols.min(), rows.min(), cols.max() + 1, rows.max() + 1
I = S[y0:y1, x0:x1]
H, W = I.shape
SKEW = None
if C.get('DESKEW', True):
    _rk0 = cv2.morphologyEx((I < 200).astype(np.uint8), cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)))
    _ln0 = ((I < 165) & (_rk0 == 0)); _L0 = I > 200
    _tv0 = (_ln0 & np.roll(_L0, 2, 1) & np.roll(_L0, -2, 1)).astype(np.uint8)
    _th0 = (_ln0 & np.roll(_L0, 2, 0) & np.roll(_L0, -2, 0)).astype(np.uint8)
    def _ang(m, vert):
        segs = cv2.HoughLinesP(m * 255, 1, np.pi / 1800, 60, minLineLength=120, maxLineGap=6)
        a = []
        for x1_, y1_, x2_, y2_ in (segs.reshape(-1, 4) if segs is not None else []):
            if vert and abs(x2_ - x1_) < abs(y2_ - y1_):
                if y2_ < y1_: x1_, y1_, x2_, y2_ = x2_, y2_, x1_, y1_
                a.append((x2_ - x1_) / (y2_ - y1_))
            if not vert and abs(x2_ - x1_) > abs(y2_ - y1_):
                if x2_ < x1_: x1_, y1_, x2_, y2_ = x2_, y2_, x1_, y1_
                a.append((y2_ - y1_) / (x2_ - x1_))
        return float(np.median(a)) if a else 0.0
    sv, sh = _ang(_tv0, True), _ang(_th0, False)
    if 'SKEW' in C: sv, sh = C['SKEW']
    if abs(sv) > 0.002 or abs(sh) > 0.002:
        # source point for output (u, v): x = u + sv * (v - H/2), y = v + sh * (u - W/2)
        M = np.float32([[1, sv, -sv * H / 2], [sh, 1, -sh * W / 2]])
        I = cv2.warpAffine(I, M, (W, H), flags=cv2.INTER_LINEAR | cv2.WARP_INVERSE_MAP, borderMode=cv2.BORDER_REPLICATE)
        SKEW = (sv, sh)
    print('skew', round(sv, 4), round(sh, 4))
cv2.imwrite(out + '_I.png', I)
def fw(x, y):
    if SKEW is None: return x, y
    sv, sh = SKEW
    return x - sv * (y - H / 2), y - sh * (x - W / 2)
def fwb(b):
    a, b_, c, d = b
    p1 = fw(a, b_); p2 = fw(c, d)
    return (int(round(p1[0])), int(round(p1[1])), int(round(p2[0])), int(round(p2[1])))
if SKEW is not None and C.get('RAW_COORDS', True):
    C['LABELS'] = [(it[0], *fw(it[1], it[2]), *it[3:]) for it in C.get('LABELS', [])]
    C['SECRETS'] = [(*[int(round(v)) for v in fw(it[0], it[1])], *it[2:]) for it in C.get('SECRETS', [])]
    for k in ('ERASE', 'FLOOR', 'BLACK', 'PROTECT', 'UNPROTECT', 'WHITE'): C[k] = [fwb(b) for b in C.get(k, [])]
if True:
    C['ERASE'] = list(C.get('ERASE', [])) + list(C.get('ERASE_DESK', []))
    C['FLOOR_CIRCLES'] = [(*fw(x, y), r) for x, y, r in C.get('FLOOR_CIRCLES', [])]
    C['DOORS'] = list(C.get('DOORS', [])) + [(*[round(v, 1) for v in fw(d[0], d[1])], *d[2:]) for d in C.get('DOORS_RAW', [])]
else:
    C['DOORS'] = list(C.get('DOORS', [])) + list(C.get('DOORS_RAW', []))
PROTECT, UNPROTECT = C.get('PROTECT', []), C.get('UNPROTECT', [])

# ---- lattice fit (grid lines are the darkest thin lines) ----
_rk = cv2.morphologyEx((I < 200).astype(np.uint8), cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)))
_ln = ((I < 165) & (_rk == 0)).astype(np.uint8)
_L = (I > 200)
_tv = (_ln == 1) & np.roll(_L, 2, 1) & np.roll(_L, -2, 1)       # thin vertical line pixel: light at x+-2
_th = (_ln == 1) & np.roll(_L, 2, 0) & np.roll(_L, -2, 0)
_pv = cv2.morphologyEx(_tv.astype(np.uint8), cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (1, 12))).sum(0).astype(float)
_ph = cv2.morphologyEx(_th.astype(np.uint8), cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (12, 1))).sum(1).astype(float)
def lfit(p, lo, hi):
    best = None
    for P in np.arange(lo, hi, 0.005):
        idx0 = np.arange(0, len(p) / P + 1)
        for o in np.arange(0, P, 0.25):
            idx = np.round(o + idx0 * P).astype(int); idx = idx[idx < len(p)]
            sc = p[idx].sum() + 0.6 * (p[np.clip(idx - 1, 0, len(p) - 1)].sum() + p[np.clip(idx + 1, 0, len(p) - 1)].sum())
            if best is None or sc > best[0]: best = (sc, P, o)
    return (0, round(float(best[1]), 3), float(best[2]))
fx = lfit(_pv, *C.get('PITCH', (27.8, 29.6))); fy = lfit(_ph, *C.get('PITCH', (27.8, 29.6)))
if 'LATTICE' in C: fx, fy = (0, C['LATTICE'][0], C['LATTICE'][1]), (0, C['LATTICE'][2], C['LATTICE'][3])
PX, OX, PY, OY = fx[1], fx[2], fy[1], fy[2]

# ---- classes ----
ROCK_K = C.get('ROCK_K', 5)
rock = cv2.morphologyEx((I < 200).astype(np.uint8), cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (ROCK_K, ROCK_K)))
rock = cv2.morphologyEx(rock, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
_n0, _l0, _s0, _ = cv2.connectedComponentsWithStats(rock, 8)
_ok0 = np.zeros(_n0, bool); _ok0[1:] = _s0[1:, 4] >= C.get('ROCK_MIN', 80)
rock = _ok0[_l0].astype(np.uint8)
if C.get('ROCK_THIN', False):
    # thin grey walls (3-4 px) count as rock: grey tone (not black ink), opened 3x3, grid slits closed
    gry = ((I >= C.get('GREY_LO', 55)) & (I < 185)).astype(np.uint8)
    thin = cv2.morphologyEx(gry, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (C.get('THIN_K', 2),) * 2))
    n_, l_, s_, _ = cv2.connectedComponentsWithStats(thin, 8)
    ok_ = np.zeros(n_, bool); ok_[1:] = s_[1:, 4] >= C.get('THIN_MIN', 60)
    thin = ok_[l_].astype(np.uint8)
    rock_thick = rock.copy()
    rock = cv2.morphologyEx(rock | thin, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)))
light = ((I >= 170) & (rock == 0)).astype(np.uint8)
line = ((I < C.get('LINE_T', 165)) & (rock == 0)).astype(np.uint8)   # thin linework on the floor: grid, door outlines, glyphs
# grid removal on the floor: a black pixel on a (locally refined) grid line whose perpendicular
# neighbours at +-3 px are light (floor) is grid; in rock it simply becomes rock
grid = np.zeros_like(line); gridv = np.zeros_like(line); gridh = np.zeros_like(line)
R = 4
GW = C.get('GRID_HALF', 2)
wallm = np.zeros_like(line)
labz0 = np.zeros_like(line)
for it in C.get('LABELS', []):
    _w = sum({'I': 5, 'V': 11, ' ': 4}.get(ch, 9 if ch.islower() else 11) + 1 for ch in it[0]) / 2 + 6; _h = 12
    if len(it) > 3 and it[3]: _w, _h = _h, _w
    labz0[max(int(it[2] - _h), 0):int(it[2] + _h), max(int(it[1] - _w), 0):int(it[1] + _w)] = 1
for it in C.get('SECRETS', []): labz0[max(it[1] - 12, 0):it[1] + 12, max(it[0] - 10, 0):it[0] + 10] = 1
def _run(prof):
    # contiguous dark run (median < WALL_MEAN) through the centre offsets of the profile (-4..4)
    dk = [v < C.get('WALL_MEAN', 150) for v in prof]
    c0 = next((i for i in (4, 3, 5) if dk[i]), None)
    if c0 is None: return []
    a = c0
    while a > 0 and dk[a - 1]: a -= 1
    b = c0
    while b < 8 and dk[b + 1]: b += 1
    return list(range(a - 4, b - 3))
for k in range(int(W / PX) + 2):
    xc = OX + k * PX
    for j in range(-1, int(H / PY) + 2):
        ya, yb = int(OY + j * PY + 2), int(OY + (j + 1) * PY - 2)
        ya, yb = max(ya, 0), min(yb, H)
        if yb - ya < 4: continue
        best, bx = 0, None
        for dx in range(-R, R + 1):
            xx = int(round(xc)) + dx
            if 0 <= xx < W:
                nr = (rock[ya:yb, xx] == 0).sum()
                f = line[ya:yb, xx].sum() / nr if nr >= 3 else 0
                if f > best: best, bx = f, xx
        if bx is None or best < 0.4: continue
        rows = np.where((rock[ya:yb, bx] == 0) & (labz0[ya:yb, bx] == 0))[0] + ya
        prof = []
        for d in range(-4, 5):
            xx_ = min(max(bx + d, 0), W - 1); ok = rows[rock[rows, xx_] == 0]
            prof.append(np.median(I[ok, xx_]) if len(ok) >= 0.7 * len(rows) and len(ok) >= 3 else 255)
        ds = _run(prof)
        if len(ds) >= C.get('WALL_PX', 3):   # thin grey wall under the grid
            wallm[max(ya - 4, 0):yb + 4, max(bx + min(ds), 0):bx + max(ds) + 1] = 1; continue
        for xx in range(max(bx - GW, 0), min(bx + GW + 1, W)):
            gridv[ya - 2 if ya >= 2 else 0:yb + 2, xx] |= line[ya - 2 if ya >= 2 else 0:yb + 2, xx]
for j in range(int(H / PY) + 2):
    yc = OY + j * PY
    for k in range(-1, int(W / PX) + 2):
        xa, xb = int(OX + k * PX + 2), int(OX + (k + 1) * PX - 2)
        xa, xb = max(xa, 0), min(xb, W)
        if xb - xa < 4: continue
        best, by = 0, None
        for dy in range(-R, R + 1):
            yy = int(round(yc)) + dy
            if 0 <= yy < H:
                nr = (rock[yy, xa:xb] == 0).sum()
                f = line[yy, xa:xb].sum() / nr if nr >= 3 else 0
                if f > best: best, by = f, yy
        if by is None or best < 0.4: continue
        cols = np.where((rock[by, xa:xb] == 0) & (labz0[by, xa:xb] == 0))[0] + xa
        prof = []
        for d in range(-4, 5):
            yy_ = min(max(by + d, 0), H - 1); ok = cols[rock[yy_, cols] == 0]
            prof.append(np.median(I[yy_, ok]) if len(ok) >= 0.7 * len(cols) and len(ok) >= 3 else 255)
        ds = _run(prof)
        if len(ds) >= C.get('WALL_PX', 3):
            wallm[max(by + min(ds), 0):by + max(ds) + 1, max(xa - 4, 0):xb + 4] = 1; continue
        for yy in range(max(by - GW, 0), min(by + GW + 1, H)):
            gridh[yy, xa - 2 if xa >= 2 else 0:xb + 2] |= line[yy, xa - 2 if xa >= 2 else 0:xb + 2]
# thin grey walls printed under a grid line are wider than the grid: keep runs wider than WALL_W
dk185 = (I < C.get('WALL_T', 175)).astype(np.uint8)
WW = C.get('WALL_W', 4)
wide_v = cv2.dilate(cv2.morphologyEx(dk185, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (WW, 1))), cv2.getStructuringElement(cv2.MORPH_RECT, (WW, 1)))
wide_h = cv2.dilate(cv2.morphologyEx(dk185, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (1, WW))), cv2.getStructuringElement(cv2.MORPH_RECT, (1, WW)))
# but a wide run that is just the crossing grid line (at a lattice node) does not count
yy_n, xx_n = np.mgrid[0:H, 0:W]
near_node = ((np.abs(((xx_n - OX) / PX - np.round((xx_n - OX) / PX)) * PX) <= 4) & (np.abs(((yy_n - OY) / PY - np.round((yy_n - OY) / PY)) * PY) <= 4))
labz = np.zeros_like(line)
for it in C.get('LABELS', []):
    _w = sum({'I': 5, 'V': 11, ' ': 4}.get(ch, 9 if ch.islower() else 11) + 1 for ch in it[0]) / 2 + 8; _h = 14
    if len(it) > 3 and it[3]: _w, _h = _h, _w
    labz[max(int(it[2] - _h), 0):int(it[2] + _h), max(int(it[1] - _w), 0):int(it[1] + _w)] = 1
for it in C.get('SECRETS', []): labz[max(it[1] - 14, 0):it[1] + 14, max(it[0] - 12, 0):it[0] + 12] = 1
grid = (gridv | gridh) & (1 - wallm)
if C.get('CROSS_RESTORE', True):
    # keep band pixels where a non-grid stroke crosses the grid line (evidence 3-4 px either side, off the other band)
    ev = (line & (1 - gridv) & (1 - gridh)).astype(np.uint8)
    D_ = C.get('CROSS_D', 3)
    evh = np.zeros_like(ev); evv = np.zeros_like(ev)
    for d_ in (D_, D_ + 1):
        evh |= np.roll(ev, d_, 1) & np.roll(ev, -d_, 1)       # stroke continues left AND right of a vertical grid line
        evv |= np.roll(ev, d_, 0) & np.roll(ev, -d_, 0)
    keepx = (gridv & evh) | (gridh & evv)
    grid = (grid & (1 - keepx)).astype(np.uint8)
# strokes thicker than the grid (door outlines are ~2px too, so test perpendicular light on BOTH sides)
gv = np.zeros_like(grid); gh = np.zeros_like(grid)
gl = np.roll(light, 3, 1); gr = np.roll(light, -3, 1); gu = np.roll(light, 3, 0); gd = np.roll(light, -3, 0)
gl2 = np.roll(rock, 3, 1); gr2 = np.roll(rock, -3, 1); gu2 = np.roll(rock, 3, 0); gd2 = np.roll(rock, -3, 0)
floor_side_v = (gl | gl2) & (gr | gr2)        # vertical line: left and right are floor or rock (not more ink)
floor_side_h = (gu | gu2) & (gd | gd2)
grid = grid & (floor_side_v | floor_side_h | labz)
core = cv2.dilate((I < C.get('CORE', 60)).astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
pass  # (core test retired; walls detected per segment)
grid_raw = grid.copy()
# protect closed glyphs (doors, X-boxes, triangles): small enclosed light holes -> no grid removal nearby
hole = (I >= 150).astype(np.uint8)
n2, lab2, st2, _ = cv2.connectedComponentsWithStats(hole, 4)
prot = np.zeros_like(hole)
for i in range(1, n2):
    x, y, w, h, a = st2[i]
    if 4 <= a <= 70 and max(w, h) <= 15:
        hm = (lab2[max(y - 2, 0):y + h + 2, max(x - 2, 0):x + w + 2] == i).astype(np.uint8)
        ring = cv2.dilate(hm, np.ones((3, 3), np.uint8)) - hm
        ry, rx = np.nonzero(ring); ry = ry + max(y - 2, 0); rx = rx + max(x - 2, 0)
        onl = (np.abs(((rx - OX) / PX - np.round((rx - OX) / PX)) * PX) <= 1.6) | (np.abs(((ry - OY) / PY - np.round((ry - OY) / PY)) * PY) <= 1.6)
        nearrock = rock[ry, rx].mean() if len(ry) else 0
        if onl.mean() > 0.45: continue
        prot[lab2 == i] = 1
prot = cv2.dilate(prot, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)))
# hatching (rubble, ramps, stairs): dense texture measured OFF the lattice lines
yy_, xx_ = np.mgrid[0:H, 0:W]
dlx = np.abs(((xx_ - OX) / PX - np.round((xx_ - OX) / PX)) * PX); dly = np.abs(((yy_ - OY) / PY - np.round((yy_ - OY) / PY)) * PY)
offl = ((dlx > 3) & (dly > 3)).astype(np.float32)
num = cv2.blur(((I < 150) & (rock == 0)).astype(np.float32) * offl, (13, 13)); den = cv2.blur(offl * (rock == 0), (13, 13)) + 1e-3
dens = num / den
hatch = ((dens > 0.2) & (rock == 0) & (den > 0.25)).astype(np.uint8)
hatch = cv2.morphologyEx(hatch, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7)))
n3, lab3, st3, _ = cv2.connectedComponentsWithStats(hatch, 8)
for i in range(1, n3):
    if st3[i, 4] < 250: hatch[lab3 == i] = 0
for it in C.get('LABELS', []):
    _w = sum({'I': 5, 'V': 11, ' ': 4}.get(ch, 9 if ch.islower() else 11) + 1 for ch in it[0]) / 2 + 10; _h = 16
    if len(it) > 3 and it[3]: _w, _h = _h, _w
    hatch[max(int(it[2] - _h), 0):int(it[2] + _h), max(int(it[1] - _w), 0):int(it[1] + _w)] = 0
for it in C.get('SECRETS', []): hatch[max(it[1] - 16, 0):it[1] + 16, max(it[0] - 14, 0):it[0] + 14] = 0
for (a, b, c, d) in PROTECT: hatch[b:d, a:c] = 1
for (a, b, c, d) in UNPROTECT: hatch[b:d, a:c] = 0
hatch = cv2.dilate(hatch, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)))
cv2.imwrite(out + '_hatch.png', hatch * 255)
_hz = hatch.copy()
for (a, b, c, d) in C.get('HATCH_DEGRID', []): _hz[b:d, a:c] = 0
if not C.get('PROTECT_HOLES', True): prot[:] = 0
grid[(prot == 1) | (_hz == 1)] = 0
line = np.where(hatch == 1, (I < 170).astype(np.uint8), line)
if C.get('ROCK_THIN', False): rock = np.where(hatch == 1, rock_thick, rock).astype(np.uint8)
feat = (line & (1 - grid)).astype(np.uint8)
if C.get('DEBUG'): np.savez('/tmp/dbg.npz', grid=grid, gridv=gridv, gridh=gridh, wallm=wallm, hatch=hatch, prot=prot, line=line, light=light, rock=rock, labz=labz)
# grid intersections: a dark blob centred on a lattice node whose diagonal neighbours (+-4) are light
for k in range(int(W / PX) + 2):
    for j in range(int(H / PY) + 2):
        cx, cy = int(round(OX + k * PX)), int(round(OY + j * PY))
        a0, b0, a1, b1 = cx - 5, cy - 5, cx + 6, cy + 6
        if a0 < 4 or b0 < 4 or a1 > W - 4 or b1 > H - 4: continue
        if hatch[cy, cx] or prot[cy, cx] or wallm[cy, cx]: continue
        win = feat[b0:b1, a0:a1]
        if not win.any(): continue
        ring = np.concatenate([light[b0 - 1, a0 - 1:a1 + 1], light[b1, a0 - 1:a1 + 1], light[b0:b1, a0 - 1], light[b0:b1, a1]])
        if ring.mean() > 0.55: win[:] = 0
# drop grid stubs: tiny feature specks left on lattice lines
n, lab, st, _ = cv2.connectedComponentsWithStats(feat, 8)
keep = np.ones(n, bool); keep[0] = False
for i in range(1, n):
    x, y, w, h, a = st[i]
    if a <= C.get('STUB_MIN', 6): keep[i] = False
    elif (w <= 3 and h >= 4 and a < 3.2 * h) or (h <= 3 and w >= 4 and a < 3.2 * w):
        cx, cy = x + w / 2, y + h / 2
        on_v = abs(((cx - OX) / PX) - round((cx - OX) / PX)) * PX < 4
        on_h = abs(((cy - OY) / PY) - round((cy - OY) / PY)) * PY < 4
        if (w <= 3 and on_v) or (h <= 3 and on_h): keep[i] = False
feat = keep[lab].astype(np.uint8)
n7, lab7, st7, cen7 = cv2.connectedComponentsWithStats(feat, 8)
for i in range(1, n7):
    x, y, w, h, a = st7[i]
    if w <= 13 and h <= 13 and a <= 40:
        cx, cy = x + w / 2, y + h / 2
        if abs(((cx - OX) / PX) - round((cx - OX) / PX)) * PX <= 4 and abs(((cy - OY) / PY) - round((cy - OY) / PY)) * PY <= 4 \
           and not prot[int(cy), int(cx)] and not wallm[int(cy), int(cx)]:
            feat[lab7 == i] = 0
black = ((rock | feat) & (1 - (light & (1 - feat)))).astype(np.uint8)
# thin spurs on rock edges (grid stubs where a lattice line meets the rock): opened away near rock,
# never on doors (prot), walls or hatching
_op = cv2.morphologyEx(black, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
_near = cv2.dilate(rock, cv2.getStructuringElement(cv2.MORPH_RECT, (13, 13)))
_spur = (black & (1 - _op) & _near & (1 - cv2.dilate(prot, np.ones((5, 5), np.uint8))) & (1 - wallm) & (1 - hatch)).astype(np.uint8)
n8, lab8, st8, _ = cv2.connectedComponentsWithStats(_spur, 8)
_k = np.zeros(n8, bool); _k[1:] = st8[1:, 4] <= C.get('SPUR_MAX', 40)
black[_k[lab8]] = 0
clean = np.where(black == 1, 0, 255).astype(np.uint8)
cv2.imwrite(out + '_clean.png', clean)

# ---- labels: glyph components grouped into words, OCR per word ----
g0 = (line & (1 - grid_raw)).astype(np.uint8)
n4, lab4, st4, cen4 = cv2.connectedComponentsWithStats(g0, 8)
gl = [i for i in range(1, n4) if 7 <= st4[i, 3] <= 17 and 2 <= st4[i, 2] <= 14 and st4[i, 4] >= 12]
used = set(); words = []
for i in sorted(gl, key=lambda i: st4[i, 0]):
    if i in used: continue
    grp = [i]; used.add(i)
    while True:
        x, y, w, h = st4[grp[-1], :4]
        nxt = [j for j in gl if j not in used and -1 <= st4[j, 0] - (x + w) <= 9 and abs((st4[j, 1] + st4[j, 3]) - (y + h)) <= 4]
        if not nxt: break
        j = min(nxt, key=lambda j: st4[j, 0]); grp.append(j); used.add(j)
    xs = [st4[j, 0] for j in grp]; ys = [st4[j, 1] for j in grp]
    xe = [st4[j, 0] + st4[j, 2] for j in grp]; ye = [st4[j, 1] + st4[j, 3] for j in grp]
    words.append((min(xs), min(ys), max(xe), max(ye)))
res = []
for (a, b, c, d) in words:
    crop = I[max(b - 3, 0):d + 3, max(a - 3, 0):c + 3]
    crop = cv2.resize(crop, None, fx=5, fy=5, interpolation=cv2.INTER_CUBIC)
    crop = cv2.copyMakeBorder(np.where(crop > 140, 255, 0).astype(np.uint8), 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=255)
    t = pytesseract.image_to_string(crop, config='--psm 7 -c tessedit_char_whitelist=0123456789abcdefgABCDS').strip()
    res.append([t, int(a), int(b), int(c), int(d)])
json.dump({'box': [int(x0), int(y0), int(x1), int(y1)], 'lattice': [PX, OX, PY, OY], 'words': res}, open(out + '_meta.json', 'w'), indent=0)
dbg = cv2.cvtColor(I, cv2.COLOR_GRAY2BGR)
for k, (t, a, b, c, d) in enumerate(res):
    cv2.rectangle(dbg, (a - 1, b - 1), (c + 1, d + 1), (0, 0, 255), 1)
    cv2.putText(dbg, f'{k}:{t}', (a, d + 10), cv2.FONT_HERSHEY_PLAIN, 0.8, (0, 140, 0), 1)
cv2.imwrite(out + '_words.png', dbg)
print('box', (x0, y0, x1, y1), 'lattice', (PX, OX, PY, OY), 'words', len(res))

# ================= stage 2: curated labels + secret doors =================
if 'LABELS' in C:
    gc = g0.copy()
    n5, lab5, st5, cen5 = cv2.connectedComponentsWithStats(gc, 8)
    _dk = ((I < 165) & (rock == 0)).astype(np.uint8)
    longl = cv2.morphologyEx(_dk, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (21, 1))) | \
            cv2.morphologyEx(_dk, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (1, 21)))
    longl = (longl & (1 - grid_raw)).astype(np.uint8)          # long straight ink that is not printed grid = wall
    longl = cv2.dilate(longl, np.ones((3, 3), np.uint8))
    dkm = ((I < 120) & (rock == 0) & (wallm == 0) & (longl == 0)).astype(np.float32)
    ii = cv2.integral(dkm)
    CW = {'I': 5, 'V': 11, ' ': 4}
    def tw(t): return sum(CW.get(ch, 9 if ch.islower() else 11) + 1 for ch in t) + 1
    def fitbox(x, y, w, h, r=7):
        best = None
        for dy in range(-r, r + 1):
            for dx in range(-r, r + 1):
                a = int(round(x - w / 2 + dx)); b = int(round(y - h / 2 + dy))
                if a < 0 or b < 0 or a + w >= W or b + h >= H: continue
                v = ii[b + h, a + w] - ii[b, a + w] - ii[b + h, a] + ii[b, a]
                v -= 0.02 * (dx * dx + dy * dy)
                if best is None or v > best[0]: best = (v, a, b)
        _, a, b = best
        return (a, b, a + w, b + h)
    final = clean.copy()
    labels_out, secrets_out, miss = [], [], []
    erase = np.zeros_like(gc); serase = np.zeros_like(gc); sboxes = []
    for item in C['LABELS']:
        t, x, y = item[:3]; rot = item[3] if len(item) > 3 else 0
        n = len(t)
        w_, h_ = tw(t), C.get("LABEL_H", 17)
        if rot in (90, -90): w_, h_ = h_, w_
        elif rot: w_ = h_ = int(0.75 * w_ + 0.7 * h_)
        bb = fitbox(x, y, w_, h_)
        _pd = C.get('LABEL_PAD', 2)
        erase[max(bb[1] - _pd, 0):bb[3] + _pd, max(bb[0] - _pd, 0):bb[2] + _pd] = 1
        labels_out.append([t, (bb[0] + bb[2]) / 2, (bb[1] + bb[3]) / 2, bb[3] - bb[1] if rot == 0 else (bb[2] - bb[0] if rot in (90, -90) else C.get('LABEL_H', 17)), rot, list(bb)])
    for sec in C.get('SECRETS', []):
        x, y = sec[:2]; manual = sec[2] if len(sec) > 2 else None
        bb = fitbox(x, y, 13, 18, 8)
        sx, sy = (bb[0] + bb[2]) / 2, (bb[1] + bb[3]) / 2
        serase[bb[1] - 1:bb[3] + 1, bb[0] - 1:bb[2] + 1] = 1; sboxes.append(list(bb))
        big = -1
        # dashes either side of the S: small components within 22 px that are not the S
        dash = [i for i in range(1, n5) if 9 < np.hypot(cen5[i][0] - sx, cen5[i][1] - sy) < 22 and 3 <= st5[i, 4] <= 30
                and max(st5[i, 2], st5[i, 3]) <= 10 and not (bb[0] <= cen5[i][0] <= bb[2] and bb[1] <= cen5[i][1] <= bb[3])]
        if C.get('DASH_WALLS', False) or (manual and manual != 'n'):
            for i in dash: serase[lab5 == i] = 1
        if not C.get('DASH_WALLS', False): dv = None
        elif len(dash) >= 2:
            pts = np.array([cen5[i] for i in dash]); vx_, vy_, x_, y_ = cv2.fitLine(pts.astype(np.float32), cv2.DIST_L2, 0, 0.01, 0.01).ravel()
            dv = np.array([vx_, vy_])
        elif len(dash) == 1:
            dv = np.array(cen5[dash[0]]) - np.array([sx, sy]); dv /= np.linalg.norm(dv) + 1e-6
        else:
            dv = None
        wall = None
        if manual == 'h': dv = np.array([1.0, 0.0])
        elif manual == 'v': dv = np.array([0.0, 1.0])
        elif manual == 'n': dv = None
        elif manual: dv = None; wall = [list(manual[0]), list(manual[1])]
        if dv is not None:
            ends = []
            for sg in (1, -1):
                p = np.array([sx, sy], float)
                for t_ in np.arange(0, 34, 0.5):
                    q = p + sg * t_ * dv; qi = q.round().astype(int)
                    if not (0 <= qi[0] < W and 0 <= qi[1] < H): break
                    if rock[qi[1], qi[0]]: break
                ends.append((q + sg * 1.5 * dv).round(1).tolist())
            wall = ends
        secrets_out.append([round(sx, 1), round(sy, 1), wall])
    erase = (erase & (1 - rock) & (1 - wallm) & (1 - longl)) | (serase & (1 - rock))
    doors_out = []
    _dl = list(C.get('DOORS', [])) + list(C.get('DOORS_DESK', []))
    _nraw = len(C.get('DOORS_RAW', [])) + len(C.get('DOORS_DESK', []))
    _auto, _man = _dl[:len(_dl) - _nraw], _dl[len(_dl) - _nraw:]
    _auto = [d for d in _auto if not any(abs(d[0] - m[0]) < 12 and abs(d[1] - m[1]) < 12 for m in _man)]
    # auto-auto duplicates
    _a2 = []
    for d in _auto:
        if not any(abs(d[0] - e[0]) < 8 and abs(d[1] - e[1]) < 8 for e in _a2): _a2.append(d)
    for dd in _a2 + _man:
        x, y, o = dd[:3]
        dl, dw = (dd[3], dd[4]) if len(dd) > 4 else (C.get('DOOR_SIZE', (6.5, 16))[1], C.get('DOOR_SIZE', (6.5, 16))[0])
        L, Wd = dl + 6, dw + 6
        if o == 'v': a, b, c, d = x - Wd / 2, y - L / 2, x + Wd / 2, y + L / 2
        elif o == 'h': a, b, c, d = x - L / 2, y - Wd / 2, x + L / 2, y + Wd / 2
        else: a, b, c, d = x - L / 2, y - L / 2, x + L / 2, y + L / 2
        a, b, c, d = int(a), int(b), int(c + 1), int(d + 1)
        erase[b:d, a:c] |= ((final[b:d, a:c] == 0) & (rock[b:d, a:c] == 0) & (wallm[b:d, a:c] == 0)).astype(np.uint8)
        doors_out.append([x, y, o, 'rect', dl, dw])
    _nr, _lr, _sr, _ = cv2.connectedComponentsWithStats(rock, 8)
    for (a, b, c, d) in C.get('ERASE', []):
        erase[b:d, a:c] |= ((final[b:d, a:c] == 0) & (rock[b:d, a:c] == 0)).astype(np.uint8)
        _g = C.get('ERASE_GRID_PAD', 8)
        A_, B_, C_, D_ = max(a - _g, 0), max(b - _g, 0), min(c + _g, W), min(d + _g, H)
        erase[B_:D_, A_:C_] |= (grid_raw[B_:D_, A_:C_] & (1 - rock[B_:D_, A_:C_])).astype(np.uint8)
        for i in np.unique(_lr[b:d, a:c]):
            if i and _sr[i, 4] < C.get('ERASE_ROCK_MAX', 400): erase[b:d, a:c] |= (_lr[b:d, a:c] == i).astype(np.uint8)
    # repair straight wall lines that pass through an erased S / label box (seen on both sides)
    pre = ((final == 0) & (rock == 0)).astype(np.uint8)
    rep = np.zeros_like(pre)
    for (a, b, c, d) in [l[5] for l in labels_out] + sboxes:
        m_ = 14
        A, B, Cc, D = max(a - m_, 0), max(b - m_, 0), min(c + m_, W), min(d + m_, H)
        win = pre[B:D, A:Cc].copy(); win[max(b - B - 1, 0):d - B + 1, max(a - A - 1, 0):c - A + 1] = 0
        win = cv2.morphologyEx(win, cv2.MORPH_OPEN, np.ones((1, 1), np.uint8))
        segs = cv2.HoughLinesP(win * 255, 1, np.pi / 180, 8, minLineLength=9, maxLineGap=2)
        if segs is None: continue
        for x1_, y1_, x2_, y2_ in segs.reshape(-1, 4):
            if not (x1_ == x2_ or y1_ == y2_): continue          # axis-aligned walls only
            if x1_ == x2_:
                X = x1_ + A
                if not (a - 1 <= X <= c + 1): continue
                up = pre[max(b - 8, 0):b - 1, X].mean() if b > 2 else 0; dn = pre[d + 1:d + 8, X].mean() if d + 1 < H else 0
                if up > 0.7 and dn > 0.7:
                    th = max(1, int(round(pre[d + 3, max(X - 3, 0):X + 4].sum()))) if d + 3 < H else 2
                    cv2.line(rep, (X, b - 1), (X, d + 1), 1, 1); rep[b - 1:d + 2, max(X - th // 2, 0):X - th // 2 + th] = 1
            else:
                Y = y1_ + B
                if not (b - 1 <= Y <= d + 1): continue
                lf = pre[Y, max(a - 8, 0):a - 1].mean() if a > 2 else 0; rt = pre[Y, c + 1:c + 8].mean() if c + 1 < W else 0
                if lf > 0.7 and rt > 0.7:
                    th = max(1, int(round(pre[max(Y - 3, 0):Y + 4, c + 3].sum()))) if c + 3 < W else 2
                    rep[max(Y - th // 2, 0):Y - th // 2 + th, a - 1:c + 2] = 1
    treads = []; stair_clear = []
    def _stairs(Iv, sb):
        out_ = []
        a, b, c, d = sb[:4]; sw_ = sb[4] if len(sb) > 4 else 2.0
        sub = (Iv[b:d, a:c] < C.get('TREAD_T', 60)).astype(np.uint8)
        prof = sub.mean(1)
        rows = [r for r in range(1, len(prof) - 1) if prof[r] >= prof[r - 1] and prof[r] >= prof[r + 1] and prof[r] > 0.25]
        # merge rows closer than 3 px
        mr = []
        for r in rows:
            if mr and r - mr[-1][-1] <= 2: mr[-1].append(r)
            else: mr.append([r])
        segs = []
        for g in mr:
            r = int(round(np.mean(g))); cols = np.nonzero(sub[max(r - 1, 0):r + 2].max(0))[0]
            if len(cols) < 4: continue
            runs = np.split(cols, np.nonzero(np.diff(cols) > C.get("TREAD_GAP", 5))[0] + 1)
            mid = (c - a) / 2
            runs = [q for q in runs if q[0] <= mid + 3 and q[-1] >= mid - 3] or [max(runs, key=len)]
            cols = runs[0]
            segs.append([r + b, int(cols.min()) + a, int(cols.max()) + a + 1])
        # grid rows span the whole box: clamp to the neighbours' extent
        for k_, sg in enumerate(segs):
            if sg[1] <= a + 1 and sg[2] >= c - 1 and len(segs) > 2:
                nb = [segs[j] for j in (k_ - 1, k_ + 1) if 0 <= j < len(segs) and not (segs[j][1] <= a + 1 and segs[j][2] >= c - 1)]
                if nb: sg[1] = int(np.mean([q[1] for q in nb])); sg[2] = int(np.mean([q[2] for q in nb]))
        good = [sg for sg in segs if not (sg[1] <= a + 2 or sg[2] >= c - 2)] or segs
        ys_ = np.array([g[0] for g in good], float)
        if len(ys_) >= 3:
            dys = np.diff(np.sort([g[0] for g in segs])); dy = float(np.median(dys[dys >= 3])) if (dys >= 3).any() else 6.0
            y0_, y1_ = min(g[0] for g in segs), max(g[0] for g in segs)
            _o = np.argsort(ys_); _ys = ys_[_o]; _xa = np.array([g[1] for g in good], float)[_o]; _xb = np.array([g[2] for g in good], float)[_o]
            from scipy.ndimage import median_filter as _mf
            if len(_xa) >= 5: _xa = _mf(_xa, 3, mode='nearest'); _xb = _mf(_xb, 3, mode='nearest')
            n_ = int(round((y1_ - y0_) / dy)) + 1; dy = (y1_ - y0_) / max(n_ - 1, 1)
            for k_ in range(n_):
                yy = y0_ + k_ * dy
                out_.append([round(yy, 1), round(float(np.interp(yy, _ys, _xa)), 1), round(float(np.interp(yy, _ys, _xb)), 1), sw_])
        else:
            out_ += [[sg[0], sg[1], sg[2], sw_] for sg in segs]

        return out_
    for sb in C.get('STAIRS_H', []):
        a, b, c, d = sb[:4]
        treads += _stairs(I, sb)
        erase[b + 2:d - 2, a + 2:c - 2] = 1; stair_clear.append((a + 2, b + 2, c - 2, d - 2))
    treads_v = []
    for sb in C.get('STAIRS_V', []):
        a, b, c, d = sb[:4]
        for (y_, xa_, xb_, sw_) in _stairs(I.T, (b, a, d, c) + tuple(sb[4:])):
            treads_v.append([y_, xa_, xb_, sw_])
        erase[b + 2:d - 2, a + 2:c - 2] = 1; stair_clear.append((a + 2, b + 2, c - 2, d - 2))
    final[erase == 1] = 255
    final[rep == 1] = 0
    for (a, b, c, d) in stair_clear: final[b:d, a:c] = 255
    # second pass: any ink component on the floor lying wholly inside a widened label / S box is glyph residue
    blk = ((final == 0) & (rock == 0)).astype(np.uint8)
    n6, lab6, st6, _ = cv2.connectedComponentsWithStats(blk, 8)
    kill = np.zeros(n6, bool)
    boxes = [l[5] for l in labels_out] + [[int(x - 8), int(y - 10), int(x + 8), int(y + 10)] for x, y, w in secrets_out]
    G = C.get('GLYPH_PAD', 6)
    for (a, b, c, d) in boxes:
        a, b, c, d = a - G, b - G, c + G, d + G
        for i in np.unique(lab6[max(b, 0):d, max(a, 0):c]):
            if i == 0: continue
            x_, y_, w_, h_, ar = st6[i]
            if x_ >= a and y_ >= b and x_ + w_ <= c and y_ + h_ <= d and ar < 160: kill[i] = True
    for i in range(1, n6):
        if st6[i, 4] < C.get('FLOOR_SPECK', 6): kill[i] = True
    final[kill[lab6]] = 255
    for (a, b, c, d) in C.get('WHITE', []): final[b:d, a:c] = np.where(rock[b:d, a:c] == 1, 0, 255)
    for (a, b, c, d) in C.get('FLOOR', []): final[b:d, a:c] = 255
    for (a, b, c, d) in C.get('BLACK', []): final[b:d, a:c] = 0
    for (cx, cy, r) in C.get('FLOOR_CIRCLES', []):
        cv2.circle(final, (int(cx), int(cy)), int(r), 255, -1)
    cv2.imwrite(out + '_final.png', final)
    json.dump({'box': [int(x0), int(y0), int(x1), int(y1)], 'lattice': [PX, OX, PY, OY], 'labels': labels_out, 'secrets': secrets_out, 'doors': doors_out, 'treads': treads, 'treads_v': treads_v},
              open(out + '_labels.json', 'w'), indent=0)
    print('missed:', miss)
