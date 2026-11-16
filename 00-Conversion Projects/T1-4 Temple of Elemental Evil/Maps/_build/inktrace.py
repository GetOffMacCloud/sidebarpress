"""Generic ink tracer for illustrated TSR maps (white ground, black ink, printed grid).
Removes the printed grid and the printed labels, vectorizes the remaining ink, and re-renders it
on parchment with a fresh grid and re-set labels. GM / Player / Print variants.

usage: python3 inktrace.py CONFIG.py OUTDIR
CONFIG defines: SRC (image), BOX (x0,y0,x1,y1 in SRC px), PX, OX, PY, OY (grid lattice in box px),
TITLE, SUB, LABELS {text: (gx, gy)}, LABEL_MASKS [(x0,y0,x1,y1) box px], GM_ONLY_MASKS [(...)] ink that
is GM-only (e.g. secret-door S), GM_MARKS [(kind, gx, gy)], SCALE_FT (feet per square), FT_LABEL.
"""
import sys, os, cv2, numpy as np
cfg = {}
exec(open(sys.argv[1]).read(), cfg)
OUT = sys.argv[2]; os.makedirs(OUT, exist_ok=True)
U = 3                                       # supersample factor for smooth contours
src = cv2.imread(cfg['SRC'], 0)
x0, y0, x1, y1 = cfg['BOX']
img = src[y0:y1, x0:x1].astype(np.float32)
H, W = img.shape
PX, OX, PY, OY = cfg['PX'], cfg['OX'], cfg['PY'], cfg['OY']

# ---- ink mask ----
ink = (img < cfg.get('THRESH', 120)).astype(np.uint8)
# remove printed grid: pixels on a grid line whose perpendicular neighbours (±3 px) are paper
def clear_grid(ink):
    out = ink.copy()
    k = 0
    while OX + k * PX < W:
        x = int(round(OX + k * PX))
        for xx in range(max(x - 1, 0), min(x + 2, W)):
            l = ink[:, max(xx - 2, 0)]; r = ink[:, min(xx + 2, W - 1)]
            out[(ink[:, xx] == 1) & ((l == 0) | (r == 0)), xx] = 0 if False else out[(ink[:, xx] == 1) & ((l == 0) | (r == 0)), xx]
            out[(ink[:, xx] == 1) & (l == 0) & (r == 0), xx] = 0
        k += 1
    k = 0
    while OY + k * PY < H:
        y = int(round(OY + k * PY))
        for yy in range(max(y - 1, 0), min(y + 2, H)):
            u = ink[max(yy - 2, 0), :]; d = ink[min(yy + 2, H - 1), :]
            out[yy, (ink[yy, :] == 1) & (u == 0) & (d == 0)] = 0
        k += 1
    return out
ink = clear_grid(ink)
# remove straight hairlines (printed grid drifting off the fitted lattice); thick walls are untouched
_thick = cv2.morphologyEx(ink, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
_thin = ink & (1 - _thick)
_L = cfg.get('HAIRLINE', 15)
_hl = cv2.morphologyEx(_thin, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (_L, 1)))
_vl = cv2.morphologyEx(_thin, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (1, _L)))
_kill = cv2.dilate(_hl | _vl, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))) & _thin
for (a, b, c, d) in cfg.get('PROTECT', []):
    _kill[b:d, a:c] = 0
ink = ink & (1 - _kill)
for (a, b, c, d) in cfg.get('LABEL_MASKS', []):
    ink[b:d, a:c] = 0
gm_ink = np.zeros_like(ink)
for (a, b, c, d) in cfg.get('GM_ONLY_MASKS', []):
    gm_ink[b:d, a:c] = ink[b:d, a:c]; ink[b:d, a:c] = 0
for (a, b, c, d) in cfg.get('ERASE', []):
    ink[b:d, a:c] = 0
# drop isolated specks
def despeckle(m, area=3):
    n, lab, st, _ = cv2.connectedComponentsWithStats(m, 8)
    keep = np.zeros(n, bool); keep[1:] = st[1:, cv2.CC_STAT_AREA] >= area
    return keep[lab].astype(np.uint8)
ink = despeckle(ink, cfg.get('SPECK', 4)); gm_ink = despeckle(gm_ink, 2)
# drop leftover printed-grid fragments: thin components lying along a grid line
def degrid(m):
    gxs = [OX + k * PX for k in range(int(W / PX) + 2)]; gys = [OY + k * PY for k in range(int(H / PY) + 2)]
    n, lab, st, _ = cv2.connectedComponentsWithStats(m, 8)
    keep = np.ones(n, bool); keep[0] = False
    for i in range(1, n):
        x, y, w, h, a = st[i]
        cx, cy = x + w / 2, y + h / 2
        if w <= 4 and min(abs(cx - g) for g in gxs) < 3.2: keep[i] = False
        elif h <= 4 and min(abs(cy - g) for g in gys) < 3.2: keep[i] = False
        elif h <= 3 and w >= 30 and a < w * 3: keep[i] = False      # long hairline (stray grid)
        elif w <= 3 and h >= 30 and a < h * 3: keep[i] = False
    return keep[lab].astype(np.uint8)
ink = degrid(ink)

def vectorize(m):
    big = cv2.resize(m.astype(np.float32), (W * U, H * U), interpolation=cv2.INTER_CUBIC)
    big = cv2.GaussianBlur(big, (0, 0), U * 0.45)
    bm = (big > 0.5).astype(np.uint8) * 255
    cs, _ = cv2.findContours(bm, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    parts = []
    for cn in cs:
        if len(cn) < 3: continue
        ap = cv2.approxPolyDP(cn, 0.9, True)[:, 0, :]
        parts.append('M' + ' L'.join(f'{x / U:.2f} {y / U:.2f}' for x, y in ap) + 'Z')
    return ' '.join(parts)

INK_PATH = vectorize(ink)
GM_PATH = vectorize(gm_ink) if gm_ink.any() else ''

FLOOR, GRID, INK, PAPER = '#efe3c4', '#8a7754', '#151310', '#e6d5ae'
S = 50 / PX                                    # svg scale: 50 units per grid square

def grid_lines():
    o = []
    k = 0
    while OX + k * PX < W:
        x = (OX + k * PX) * S; o.append(f'M{x:.1f} 0V{H * S:.1f}'); k += 1
    k = 0
    while OY + k * PY < H:
        y = (OY + k * PY) * S; o.append(f'M0 {y:.1f}H{W * S:.1f}'); k += 1
    return ' '.join(o)

def build(mode):
    gm, pr = mode in ('gm', 'print'), mode == 'print'
    Wd, Ht = W * S, H * S
    top = 90 if pr else 0; bot = 70 if pr else 0
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {-top} {Wd:.0f} {Ht + top + bot:.0f}" width="{Wd:.0f}" height="{Ht + top + bot:.0f}" font-family="Georgia, \'Times New Roman\', serif">',
         f'<title>{cfg["TITLE"]} ({mode.upper()})</title>',
         '<defs><filter id="paper" x="0" y="0" width="1" height="1"><feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="4" seed="11" result="n"/><feColorMatrix in="n" type="matrix" values="0 0 0 0 0.36  0 0 0 0 0.26  0 0 0 0 0.12  0 0 0 0.22 0" result="t"/><feComposite in="t" in2="SourceGraphic" operator="in" result="tt"/><feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="tt"/></feMerge></filter></defs>',
         f'<rect x="0" y="{-top}" width="{Wd:.0f}" height="{Ht + top + bot:.0f}" fill="{PAPER}" filter="url(#paper)"/>',
         f'<rect x="0" y="0" width="{Wd:.0f}" height="{Ht:.0f}" fill="{FLOOR}" filter="url(#paper)"/>',
         (f'<path d="{grid_lines()}" stroke="{GRID}" stroke-width="1.4" opacity="0.75" fill="none"/>' if mode != 'player_nogrid' else ''),
         f'<g transform="scale({S:.5f})"><path d="{INK_PATH}" fill="{INK}" fill-rule="evenodd"/></g>']
    for (a, b, c, d, orient) in cfg.get('STAIRS', []):
        X0, Y0, X1, Y1 = a * S, b * S, c * S, d * S
        o.append(f'<rect x="{X0:.1f}" y="{Y0:.1f}" width="{X1-X0:.1f}" height="{Y1-Y0:.1f}" fill="{FLOOR}" stroke="{INK}" stroke-width="2.5"/>')
        n = 8
        for i in range(1, n):
            t = i / n
            if orient == 'h':
                yv = Y0 + t * (Y1 - Y0); o.append(f'<line x1="{X0:.1f}" y1="{yv:.1f}" x2="{X1:.1f}" y2="{yv:.1f}" stroke="{INK}" stroke-width="2"/>')
            else:
                xv = X0 + t * (X1 - X0); o.append(f'<line x1="{xv:.1f}" y1="{Y0:.1f}" x2="{xv:.1f}" y2="{Y1:.1f}" stroke="{INK}" stroke-width="2"/>')
    # explicit thin walls (box px polylines), doors, angled stairs: features too fine for the trace
    LW = cfg.get('LINE_W', 3.2) * S
    for pts in cfg.get('LINES', []):
        d = 'M' + ' L'.join(f'{x * S:.1f} {y * S:.1f}' for x, y in pts)
        o.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{LW:.1f}" stroke-linecap="square"/>')
    for (x, y, orient, kind) in cfg.get('DOORS', []):
        X, Y = x * S, y * S
        if kind == 'rect':
            w, h = (5.5 * S, 15 * S) if orient == 'v' else (15 * S, 5.5 * S)
            o.append(f'<rect x="{X - w / 2:.1f}" y="{Y - h / 2:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{1.5 * S:.1f}" fill="{FLOOR}" stroke="{INK}" stroke-width="{2.2 * S:.1f}"/>')
        else:   # tick pair across the wall line
            for off in (-2.2, 2.2):
                if orient == 'v':
                    o.append(f'<line x1="{X - 4 * S:.1f}" y1="{Y + off * S:.1f}" x2="{X + 4 * S:.1f}" y2="{Y + off * S:.1f}" stroke="{INK}" stroke-width="{1.8 * S:.1f}"/>')
                else:
                    o.append(f'<line x1="{X + off * S:.1f}" y1="{Y - 4 * S:.1f}" x2="{X + off * S:.1f}" y2="{Y + 4 * S:.1f}" stroke="{INK}" stroke-width="{1.8 * S:.1f}"/>')
    for (A, R, T, B, n) in cfg.get('POLYSTAIRS', []):
        # parallelogram A-R-T-B; treads run parallel to A->R, stepped across A->B
        pts = [A, R, T, B]
        d = 'M' + ' L'.join(f'{x * S:.1f} {y * S:.1f}' for x, y in pts) + 'Z'
        o.append(f'<path d="{d}" fill="{FLOOR}" stroke="{INK}" stroke-width="{2.6 * S:.1f}" stroke-linejoin="round"/>')
        for i in range(1, n):
            t = i / n
            p0 = (A[0] + t * (B[0] - A[0]), A[1] + t * (B[1] - A[1])); p1 = (R[0] + t * (T[0] - R[0]), R[1] + t * (T[1] - R[1]))
            o.append(f'<line x1="{p0[0] * S:.1f}" y1="{p0[1] * S:.1f}" x2="{p1[0] * S:.1f}" y2="{p1[1] * S:.1f}" stroke="{INK}" stroke-width="{1.4 * S:.1f}"/>')
    if gm and GM_PATH:
        o.append(f'<g transform="scale({S:.5f})"><path d="{GM_PATH}" fill="{INK}" fill-rule="evenodd"/></g>')
    if gm:
        for t, (gx, gy) in cfg['LABELS'].items():
            x, y = (OX + gx * PX) * S, (OY + gy * PY) * S
            o.append(f'<text x="{x:.1f}" y="{y + 8:.1f}" font-size="24" font-weight="bold" text-anchor="middle" fill="{INK}" stroke="{FLOOR}" stroke-width="5" paint-order="stroke">{t.strip()}</text>')
        for kind, gx, gy in cfg.get('GM_MARKS', []):
            x, y = (OX + gx * PX) * S, (OY + gy * PY) * S
            o.append(f'<text x="{x:.1f}" y="{y + 7:.1f}" font-size="20" font-weight="bold" text-anchor="middle" fill="#9b2226" stroke="{FLOOR}" stroke-width="4" paint-order="stroke">{kind}</text>')
    o.append(f'<rect x="0" y="0" width="{Wd:.0f}" height="{Ht:.0f}" fill="none" stroke="{INK}" stroke-width="4"/>')
    if pr:
        o.append(f'<text x="18" y="-40" font-size="38" font-weight="bold" fill="{INK}" letter-spacing="2">{cfg["TITLE"].upper()}</text>')
        o.append(f'<text x="20" y="-12" font-size="18" fill="#5a4a32" font-style="italic">{cfg["SUB"]}</text>')
        sx, sy = 20, Ht + 40
        for i in range(5):
            o.append(f'<rect x="{sx + i * 50}" y="{sy}" width="50" height="10" fill="{FLOOR if i % 2 == 0 else INK}" stroke="{INK}" stroke-width="1.5"/>')
        ft = cfg['SCALE_FT']
        o.append(f'<text x="{sx}" y="{sy - 8}" font-size="16" fill="{INK}">0</text><text x="{sx + 230}" y="{sy - 8}" font-size="16" fill="{INK}">{5 * ft} ft</text>')
        o.append(f'<text x="{sx + 270}" y="{sy + 10}" font-size="16" fill="{INK}">1 square = {ft} feet</text>')
        if cfg.get('NOTE'):
            o.append(f'<text x="{Wd - 20:.0f}" y="{sy + 10}" font-size="15" text-anchor="end" fill="#5a4a32" font-style="italic">{cfg["NOTE"]}</text>')
    o.append('</svg>')
    return '\n'.join(o)

base = cfg['FILE']
for mode, name in (('gm', 'GM'), ('player', 'Player'), ('player_nogrid', 'Player (No Grid)'), ('print', 'Print')):
    open(f'{OUT}/{base} - {name}.svg', 'w').write(build(mode))
print('ok', W, H, len(INK_PATH))
