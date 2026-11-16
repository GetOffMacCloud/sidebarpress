"""raw_degrid.py PAGE x0,y0,x1,y1 PX,OX,PY,OY OUT [T=175] [BAND=2.0] [SPECK=4]
Thin-line illustrated maps: keep raw ink, drop pixels on a grid line unless ink continues on BOTH
perpendicular sides (a stroke crossing the line). Output black-on-white PNG of the box."""
import sys, os, cv2, numpy as np
p, b, l, out = sys.argv[1:5]
T = float(sys.argv[5]) if len(sys.argv) > 5 else 175; BAND = float(sys.argv[6]) if len(sys.argv) > 6 else 2.0
SP = int(sys.argv[7]) if len(sys.argv) > 7 else 4
x0, y0, x1, y1 = map(int, b.split(',')); PX, OX, PY, OY = map(float, l.split(','))
I = cv2.imread(p, 0)[y0:y1, x0:x1]; H, W = I.shape
if os.environ.get('SKEW'):
    sv, sh = map(float, os.environ['SKEW'].split(','))
    M = np.float32([[1, sv, -sv * H / 2], [sh, 1, -sh * W / 2]])
    I = cv2.warpAffine(I, M, (W, H), flags=cv2.INTER_LINEAR | cv2.WARP_INVERSE_MAP, borderMode=cv2.BORDER_REPLICATE)
    if os.environ.get('SAVE_I'): cv2.imwrite(os.environ['SAVE_I'], I)
raw = (I < T).astype(np.uint8)
yy, xx = np.mgrid[0:H, 0:W]
dvx = np.abs(((xx - OX) / PX - np.round((xx - OX) / PX)) * PX); dvy = np.abs(((yy - OY) / PY - np.round((yy - OY) / PY)) * PY)
onv = dvx <= BAND; onh = dvy <= BAND
def side(m, axis):
    s = np.zeros_like(m, bool)
    for d in (3, 4):
        s |= np.roll(m, d, axis).astype(bool)
    a = s.copy(); s = np.zeros_like(m, bool)
    for d in (3, 4):
        s |= np.roll(m, -d, axis).astype(bool)
    return a & s
# evidence = raw ink that is itself off both grid bands
off = (raw.astype(bool) & ~onv & ~onh).astype(np.uint8)
AL = int(sys.argv[8]) if len(sys.argv) > 8 else 4
offv = cv2.dilate(off, cv2.getStructuringElement(cv2.MORPH_RECT, (1, 2 * AL + 1)))   # tolerance along a vertical grid line
offh = cv2.dilate(off, cv2.getStructuringElement(cv2.MORPH_RECT, (2 * AL + 1, 1)))
sh = side(offv, 1); sv = side(offh, 0)
TK = int(sys.argv[10]) if len(sys.argv) > 10 else 3
dk = (I < 150).astype(np.uint8)
thv = cv2.morphologyEx(dk, cv2.MORPH_OPEN, np.ones((1, TK), np.uint8)).astype(bool)   # >=3 px wide horizontally: not a 1-2 px vertical grid line
thh = cv2.morphologyEx(dk, cv2.MORPH_OPEN, np.ones((TK, 1), np.uint8)).astype(bool)
thv = cv2.dilate(thv.astype(np.uint8), np.ones((1, 3), np.uint8)).astype(bool); thh = cv2.dilate(thh.astype(np.uint8), np.ones((3, 1), np.uint8)).astype(bool)
g = (onv & ~sh & ~thv) | (onh & ~sv & ~thh)
RUN = int(os.environ.get('RUN', 0)) if 'os' in dir() else 0
if RUN:
    rv = cv2.morphologyEx(raw, cv2.MORPH_OPEN, np.ones((RUN, 1), np.uint8)).astype(bool)   # long vertical run
    rh = cv2.morphologyEx(raw, cv2.MORPH_OPEN, np.ones((1, RUN), np.uint8)).astype(bool)
    g = (g & onv & rv) | (g & onh & rh)
ink = (raw.astype(bool) & ~g).astype(np.uint8)
if os.environ.get('MINIMAL'):
    cv2.imwrite(out, np.where(ink == 1, 0, 255).astype(np.uint8)); print('ok', W, H); sys.exit(0)
# prune spurs left along grid bands: a band pixel needs ink 2-3 px off the band (either side) within +-1 along it
import os
for _ in range(int(os.environ.get('PRUNE', 2))):
    nb_v = np.zeros_like(ink, bool); nb_h = np.zeros_like(ink, bool)
    k = cv2.dilate(ink, np.ones((3, 1), np.uint8)).astype(bool)   # along-vertical tolerance
    kh = cv2.dilate(ink, np.ones((1, 3), np.uint8)).astype(bool)
    for d in (2, 3):
        nb_v |= np.roll(k, d, 1) | np.roll(k, -d, 1)
        nb_h |= np.roll(kh, d, 0) | np.roll(kh, -d, 0)
    spur = ink.astype(bool) & ((onh & ~onv & ~nb_h & ~thh) | (onv & ~onh & ~nb_v & ~thv))
    ink[spur] = 0
n, lab, st, cen = cv2.connectedComponentsWithStats(ink, 8)
ok = np.zeros(n, bool); ok[1:] = st[1:, 4] >= SP
for i in range(1, n):
    x_, y_, w_, h_, a_ = st[i]
    if w_ <= 6 and h_ <= 6 and a_ <= 20:
        cx, cy = cen[i]
        if abs(((cx - OX) / PX - round((cx - OX) / PX)) * PX) <= 3 or abs(((cy - OY) / PY - round((cy - OY) / PY)) * PY) <= 3:
            ok[i] = False
ink = ok[lab].astype(np.uint8)
# bridge gaps the removal opened across a grid line: pair skeleton endpoints on opposite sides of a band
from skimage.morphology import skeletonize
sk = skeletonize(ink.astype(bool)).astype(np.uint8)
nbr = cv2.filter2D(sk, -1, np.ones((3, 3), np.float32), borderType=cv2.BORDER_CONSTANT)
ey, ex = np.nonzero((sk == 1) & (nbr == 2))
E_ = np.column_stack([ex, ey]).astype(float)
used = set(); MAXG = float(sys.argv[9]) if len(sys.argv) > 9 else 9
lab_s = cv2.connectedComponents(ink, connectivity=8)[1]
for i in range(len(E_)):
    if i in used: continue
    d = np.hypot(*(E_ - E_[i]).T); d[i] = 1e9
    for j in np.argsort(d)[:4]:
        if j in used or d[j] > MAXG or d[j] < 2: continue
        (xa, ya), (xb, yb) = E_[i], E_[j]
        if lab_s[int(ya), int(xa)] == lab_s[int(yb), int(xb)]: continue
        mx, my = (xa + xb) / 2, (ya + yb) / 2
        nv = abs(((mx - OX) / PX - round((mx - OX) / PX)) * PX) <= 3 and abs(xa - xb) >= 2
        nh = abs(((my - OY) / PY - round((my - OY) / PY)) * PY) <= 3 and abs(ya - yb) >= 2
        crosses_v = nv and (((xa - OX) / PX - round((mx - OX) / PX)) * ((xb - OX) / PX - round((mx - OX) / PX)) < 0)
        crosses_h = nh and (((ya - OY) / PY - round((my - OY) / PY)) * ((yb - OY) / PY - round((my - OY) / PY)) < 0)
        if crosses_v or crosses_h:
            cv2.line(ink, (int(xa), int(ya)), (int(xb), int(yb)), 1, 2); used |= {i, j}; break
_cl = cv2.morphologyEx(ink, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
ink = (ink | (_cl & (onv | onh))).astype(np.uint8)
cv2.imwrite(out, np.where(ink == 1, 0, 255).astype(np.uint8))
print('ok', W, H)
