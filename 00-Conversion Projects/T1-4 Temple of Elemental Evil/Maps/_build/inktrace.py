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
TINT = None
if cfg.get('TINT_MASK'):
    TINT = (cv2.imread(cfg['TINT_MASK'], 0) > 127).astype(np.uint8)
    for _poly in cfg.get('TINT_POLYS', []):
        cv2.fillPoly(TINT, [np.array(_poly, np.int32)], 1)
    hard = (img < cfg.get('TINT_THRESH', 60)).astype(np.uint8)
    ink = np.where(TINT == 1, hard, ink).astype(np.uint8)
    # drop leftover screen dots inside the tint
    n_, lab_, st_, _ = cv2.connectedComponentsWithStats(ink * TINT, 8)
    small_ = np.zeros(n_, bool); small_[1:] = st_[1:, cv2.CC_STAT_AREA] < cfg.get('TINT_SPECK', 10)
    ink[small_[lab_] & (TINT == 1)] = 0
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
GRIDDED = cfg.get('GRIDDED', True)
FRAG = cfg.get('GRID_REMOVAL', 'full') == 'fragments'   # dark threshold already drops the grid; only clean fragments
_ink0 = ink.copy()
# strokes 3+ px wide are art, never grid (the printed grid is 1-2 px): find them BEFORE any removal
_thick0 = cv2.morphologyEx(ink, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
_thick0 = cv2.dilate(_thick0, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))) & ink
if GRIDDED and not FRAG: ink = clear_grid(ink) | (_thick0 if cfg.get('THICK_GUARD', False) else 0)
# refined grid removal: locate each printed grid line's true position per cell span (the scan drifts
# a few px off the fitted lattice), and clear only thin ink there; thick walls (survive a 3x3 open) stay
_thick = _thick0 if cfg.get('THICK_GUARD', False) else cv2.morphologyEx(ink, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
_raw = (img < cfg.get('THRESH', 120)).astype(np.uint8)
# ink that is not a grid-line candidate: used for the perpendicular (crossing-stroke) tests, so grid
# intersections don't protect each other
def _gridband():
    G = np.zeros_like(_raw)
    R_ = cfg.get('GRID_BAND', 3)
    for k in range(int(W / PX) + 2):
        x = int(round(OX + k * PX)); G[:, max(x - R_, 0):min(x + R_ + 1, W)] = 1
    Gv = G.copy(); G[:] = 0
    for j in range(int(H / PY) + 2):
        y = int(round(OY + j * PY)); G[max(y - R_, 0):min(y + R_ + 1, H), :] = 1
    return Gv, G
_Gv, _Gh = _gridband()
_thin = _raw & (1 - _thick)
PERP = bool(cfg.get('PERP_TEST', False))   # only clear a grid pixel if no crossing stroke touches it
AGG = bool(cfg.get('AGGRESSIVE', False))   # with THICK_GUARD: clear every thin pixel on a located grid line
_raw_nv = _raw & (1 - (_thin & _Gv))     # for horizontal-line tests: ignore thin ink on vertical grid bands
_raw_nh = _raw & (1 - (_thin & _Gh))     # for vertical-line tests: ignore thin ink on horizontal grid bands
def refine(ink):
    out = ink.copy()
    nx, ny = int(W / PX) + 2, int(H / PY) + 2
    R = cfg.get('DRIFT', 5)
    for k in range(nx):
        x = OX + k * PX
        for j in range(-1, ny):
            ya, yb = int(OY + j * PY + 3), int(OY + (j + 1) * PY - 3)
            ya, yb = max(ya, 0), min(yb, H)
            if yb - ya < 6: continue
            best, bx = 0, None
            for dx in range(-R, R + 1):
                xx = int(round(x)) + dx
                if 0 <= xx < W:
                    f = _raw[ya:yb, xx].mean()
                    if f > best: best, bx = f, xx
            if bx is not None and best >= 0.55:
                y_a, y_b = (ya - 3 if ya >= 3 else 0), yb + 3
                L = _raw_nh[y_a:y_b, max(bx - 3, 0)]; Rr = _raw_nh[y_a:y_b, min(bx + 3, W - 1)]
                for xx in range(max(bx - 1, 0), min(bx + 2, W)):
                    col = out[y_a:y_b, xx]
                    th = _thick[y_a:y_b, xx]
                    col[(th == 0) & ((((L == 0) & (Rr == 0)) | AGG) | (not PERP))] = 0
    for j in range(ny):
        y = OY + j * PY
        for k in range(-1, nx):
            xa, xb = int(OX + k * PX + 3), int(OX + (k + 1) * PX - 3)
            xa, xb = max(xa, 0), min(xb, W)
            if xb - xa < 6: continue
            best, by = 0, None
            for dy in range(-R, R + 1):
                yy = int(round(y)) + dy
                if 0 <= yy < H:
                    f = _raw[yy, xa:xb].mean()
                    if f > best: best, by = f, yy
            if by is not None and best >= 0.55:
                x_a, x_b = (xa - 3 if xa >= 3 else 0), xb + 3
                U_ = _raw_nv[max(by - 3, 0), x_a:x_b]; D_ = _raw_nv[min(by + 3, H - 1), x_a:x_b]
                for yy in range(max(by - 1, 0), min(by + 2, H)):
                    row = out[yy, x_a:x_b]
                    th = _thick[yy, x_a:x_b]
                    row[(th == 0) & ((((U_ == 0) & (D_ == 0)) | AGG) | (not PERP))] = 0
    return out
if GRIDDED and not FRAG: ink = refine(ink)
if GRIDDED and FRAG and cfg.get('FRAG_REFINE'):
    # second pass on the dark ink: clear grid-line pixels except 2-px-wide strokes (building outlines)
    _d = cv2.blur((img < 120).astype(np.float32), (11, 11))
    _p = (_d > cfg.get('FRAG_DENSE', 0.42)).astype(np.uint8)
    _p = cv2.morphologyEx(_p, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)))
    _n, _l, _st, _ = cv2.connectedComponentsWithStats(_p, 8)
    _k = np.zeros(_n, bool); _k[1:] = _st[1:, cv2.CC_STAT_AREA] >= cfg.get('AUTO_PROTECT_MIN', 220)
    _keep2 = cv2.dilate(_k[_l].astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_RECT, (cfg.get('FRAG_HALO', 9),) * 2))
    if TINT is not None: _keep2[TINT == 1] = 0
    globals()['_KEEP_ZONE'] = _keep2
    ink = np.where(_keep2 == 1, ink, refine(clear_grid(ink))).astype(np.uint8)
if GRIDDED and FRAG and TINT is not None:
    # inside tinted areas (roads) nothing coincides with the grid: run the full grid removal there only
    _zone = cv2.dilate(TINT, cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7)))
    _full = refine(clear_grid(ink))
    ink = np.where(_zone == 1, _full, ink).astype(np.uint8)
# auto-protect dense art (hatched buildings, solid streams): grid removal must not cut their outlines
if GRIDDED and not FRAG and cfg.get('AUTO_PROTECT'):
    _d = cv2.blur(_ink0.astype(np.float32), (11, 11))
    _p = (_d > cfg['AUTO_PROTECT']).astype(np.uint8)
    _p = cv2.morphologyEx(_p, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)))
    _n, _l, _st, _ = cv2.connectedComponentsWithStats(_p, 8)
    _k = np.zeros(_n, bool); _k[1:] = _st[1:, cv2.CC_STAT_AREA] >= cfg.get('AUTO_PROTECT_MIN', 220)
    _ad = cfg.get('AUTO_PROTECT_DIL', 7)
    _p = cv2.dilate(_k[_l].astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_RECT, (_ad, _ad)))
    ink = ink | (_ink0 & _p)
if cfg.get('GLYPH_MASKS') == 'hybrid':
    # hybrid: inside each label box keep only THICK ink (walls, solid fills) and repair thin lines (grid, outlines)
    # that cross the box, by re-drawing any straight line seen on BOTH sides of the box
    _thk = cv2.morphologyEx(ink, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (cfg.get('THICK_K', 4),) * 2))
    _thk = (cv2.dilate(_thk, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))) & ink).astype(np.uint8)
    _src = ink.copy()
    for (a, b, c, d) in cfg.get('LABEL_MASKS', []):
        a, b, c, d = max(a, 0), max(b, 0), min(c, W), min(d, H)
        if c <= a or d <= b: continue
        ink[b:d, a:c] = _thk[b:d, a:c]
        bw, bh = c - a, d - b; m_ = max(bw, bh)
        A, B, C, D = max(a - m_, 0), max(b - m_, 0), min(c + m_, W), min(d + m_, H)
        win = _src[B:D, A:C].copy(); win[b - B:d - B, a - A:c - A] = 0
        win = (win & (1 - _thk[B:D, A:C])).astype(np.uint8)
        segs = cv2.HoughLinesP(win * 255, 1, np.pi / 360, 10, minLineLength=max(8, m_ // 2), maxLineGap=3)
        if segs is None: continue
        for x1_, y1_, x2_, y2_ in segs.reshape(-1, 4):
            p1 = np.array([x1_ + A, y1_ + B], float); p2 = np.array([x2_ + A, y2_ + B], float)
            dv = p2 - p1; L = np.hypot(*dv)
            if L < 1: continue
            dv /= L
            # walk the infinite line across the window; collect where it is inside the box
            ts = np.arange(-2 * m_ - L, 2 * m_ + L, 0.5)
            pts = p1[None, :] + ts[:, None] * dv[None, :]
            inb = (pts[:, 0] >= a) & (pts[:, 0] < c) & (pts[:, 1] >= b) & (pts[:, 1] < d)
            if not inb.any(): continue
            t_in0, t_in1 = ts[inb].min(), ts[inb].max()
            def _hits(t0, t1):
                q = p1[None, :] + np.arange(t0, t1, 1.0)[:, None] * dv[None, :]
                q = np.round(q).astype(int); ok = (q[:, 0] >= 0) & (q[:, 0] < W) & (q[:, 1] >= 0) & (q[:, 1] < H)
                q = q[ok]
                return _src[q[:, 1], q[:, 0]].mean() if len(q) else 0
            if _hits(t_in0 - 8, t_in0 - 1) > 0.6 and _hits(t_in1 + 1, t_in1 + 8) > 0.6:
                q0 = p1 + (t_in0 - 1) * dv; q1 = p1 + (t_in1 + 1) * dv
                _tmp = np.zeros_like(ink)
                cv2.line(_tmp, (int(round(q0[0])), int(round(q0[1]))), (int(round(q1[0])), int(round(q1[1]))), 1, cfg.get('REPAIR_W', 2))
                ink[b:d, a:c] |= _tmp[b:d, a:c]
elif cfg.get('GLYPH_MASKS'):
    # erase only ink components that lie wholly inside a label box (the printed glyphs); walls that pass
    # through the box are kept intact
    _nn, _ll, _ss, _ = cv2.connectedComponentsWithStats(ink, 8)
    _kill = np.zeros(_nn, bool)
    for (a, b, c, d) in cfg.get('LABEL_MASKS', []):
        for _i in np.unique(_ll[max(b, 0):d, max(a, 0):c]):
            if _i == 0: continue
            x_, y_, w_, h_, _ = _ss[_i]
            if x_ >= a - 1 and y_ >= b - 1 and x_ + w_ <= c + 1 and y_ + h_ <= d + 1: _kill[_i] = True
    ink[_kill[_ll]] = 0
else:
    for (a, b, c, d) in cfg.get('LABEL_MASKS', []):
        ink[b:d, a:c] = 0
gm_ink = np.zeros_like(ink)
for (a, b, c, d) in cfg.get('GM_ONLY_MASKS', []):
    gm_ink[b:d, a:c] = ink[b:d, a:c]; ink[b:d, a:c] = 0
for (a, b, c, d) in cfg.get('ERASE', []) + [(p[0] - 1, p[1] - 1, p[2] + 1, p[3] + 1) for p in cfg.get('PARAPETS', [])]:
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
if GRIDDED: ink = degrid(ink)
# final pass: lone perfectly straight strokes (grid residue); forked tufts and curved contours survive
def straight_clean(m):
    n, lab, st, _ = cv2.connectedComponentsWithStats(m, 8)
    keep = np.ones(n, bool); keep[0] = False
    for i in range(1, n):
        x, y, w, h, a = st[i]
        if any(x >= p0 and y >= p1 and x + w <= p2 and y + h <= p3 for (p0, p1, p2, p3) in cfg.get('PROTECT', [])): continue
        if (w <= 3 and h >= 5) or (h <= 3 and w >= 5): keep[i] = False
        # T / L stubs at the frame edge
        elif (x <= 1 or y <= 1 or x + w >= W - 1 or y + h >= H - 1) and a < 0.35 * w * h and w < 3 * PX and h < 3 * PX: keep[i] = False
    return keep[lab].astype(np.uint8)
if GRIDDED and cfg.get('STRAIGHT_CLEAN', True): ink = straight_clean(ink)
# tangent restore: a stroke that runs ALONG a grid line is erased with the grid. Restore the erased stretch
# between two consecutive points where ONE kept stroke touches the line from the SAME side (the stroke leaves
# the line and comes back, e.g. a tree's flank), if the stretch is short and nothing crosses it.
if GRIDDED and cfg.get('TANGENT_RESTORE', 0):
    _rr = (img < cfg.get('THRESH', 120)).astype(np.uint8)
    if TINT is not None: _rr[TINT == 1] = 0
    MAXR = cfg['TANGENT_RESTORE']
    _nl, _lab = cv2.connectedComponents(ink, connectivity=8)
    def _first(v):
        nz = v[v > 0]; return int(nz[0]) if nz.size else 0
    def _scan(n_lines, origin, pitch, length, get_side, restore):
        for k in range(n_lines):
            c = int(round(origin + k * pitch))
            touches = []
            for t in range(length):
                la, lb = get_side(c, t)
                if la and not lb: touches.append((t, 'a', la))
                elif lb and not la: touches.append((t, 'b', lb))
                elif la and lb: touches.append((t, 'x', 0))
            for (t0, s0, l0), (t1, s1, l1) in zip(touches, touches[1:]):
                g = t1 - t0
                if s0 == s1 and s0 != 'x' and l0 == l1 and 2 <= g <= MAXR:
                    restore(c, t0, t1)
    def _gv(c, t):
        return (_first(_lab[t, max(c - 6, 0):max(c - 2, 0)][::-1]), _first(_lab[t, min(c + 3, W):min(c + 7, W)]))
    def _rv(c, t0, t1):
        sl = slice(max(c - 2, 0), min(c + 3, W)); ink[t0:t1 + 1, sl] |= _rr[t0:t1 + 1, sl]
    def _gh(c, t):
        return (_first(_lab[max(c - 6, 0):max(c - 2, 0), t][::-1]), _first(_lab[min(c + 3, H):min(c + 7, H), t]))
    def _rh(c, t0, t1):
        sl = slice(max(c - 2, 0), min(c + 3, H)); ink[sl, t0:t1 + 1] |= _rr[sl, t0:t1 + 1]
    _scan(int(W / PX) + 2, OX, PX, H, _gv, _rv)
    _scan(int(H / PY) + 2, OY, PY, W, _gh, _rh)
# gap repair: grid removal nicks strokes where they run along a grid line; restore raw ink that a small
# closing of the cleaned ink would fill (bridges gaps without bringing back free-standing grid lines)
if GRIDDED and cfg.get('GAP_REPAIR', 0):
    _k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (cfg['GAP_REPAIR'],) * 2)
    _cl = cv2.morphologyEx(ink, cv2.MORPH_CLOSE, _k)
    _rr = (img < cfg.get('THRESH', 120)).astype(np.uint8)
    if TINT is not None: _rr[TINT == 1] = 0
    ink = (ink | (_cl & _rr)).astype(np.uint8)
if GRIDDED and cfg.get('FINAL_CLEAN', False): ink = straight_clean(ink)
# tree rebuild: cloud-shaped outlines (trees, bushes) broken by grid removal are re-closed: close the outline,
# fill it, and redraw its ring at the original stroke weight. Only blob-like, tree-sized shapes qualify.
if GRIDDED and cfg.get('TREE_REBUILD'):
    _tr = cfg['TREE_REBUILD']
    _excl = np.zeros_like(ink)
    if TINT is not None: _excl |= cv2.dilate(TINT, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)))
    for (a_, b_, c_, d_) in cfg.get('TREE_EXCLUDE', []): _excl[b_:d_, a_:c_] = 1
    _cand = (ink & (1 - _excl)).astype(np.uint8)
    _cl = cv2.morphologyEx(_cand, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (_tr.get('close', 7),) * 2))
    _cs, _hi = cv2.findContours(_cl, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    _ring_all = np.zeros_like(ink); _gone = np.zeros_like(ink); _HULLRIM = []
    _GRIDLINES = np.zeros_like(ink)
    for _k in range(int(W / PX) + 2):
        _x = int(round(OX + _k * PX)); _GRIDLINES[:, max(_x - 3, 0):min(_x + 4, W)] = 1
    for _k in range(int(H / PY) + 2):
        _y = int(round(OY + _k * PY)); _GRIDLINES[max(_y - 3, 0):min(_y + 4, H), :] = 1
    _nt = 0
    for _c in _cs:
        x_, y_, w_, h_ = cv2.boundingRect(_c)
        if not (_tr.get('min', 12) <= max(w_, h_) <= _tr.get('max', 60)): continue
        if max(w_, h_) > 2.2 * min(w_, h_): continue
        if any(x_ <= hx <= x_ + w_ and y_ <= hy <= y_ + h_ for (hx, hy) in _tr.get('hull_at', [])):
            # named crowns whose flank lies ON a grid line: restore the raw scan ink in the hull's rim band
            _bx0, _by0, _bx1, _by1 = max(x_ - 8, 0), max(y_ - 8, 0), min(x_ + w_ + 8, W), min(y_ + h_ + 8, H)
            _pts = np.column_stack(np.where(_cand[_by0:_by1, _bx0:_bx1] > 0))[:, ::-1] + [_bx0, _by0]
            _hf = np.zeros_like(ink); cv2.fillPoly(_hf, [cv2.convexHull(_pts.astype(np.int32))], 1)
            _hf = cv2.dilate(_hf, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
            _rim = (_hf - cv2.erode(_hf, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (19, 19)))).astype(np.uint8)
            _hull_t = np.zeros_like(ink); cv2.fillPoly(_hull_t, [cv2.convexHull(_pts.astype(np.int32))], 1)
            _edge = (cv2.dilate(_hull_t, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))) - cv2.erode(_hull_t, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7)))).astype(np.uint8)
            _rawt = (img < cfg.get('THRESH', 120)).astype(np.uint8)
            # off the grid lines: restore anything in the rim; ON a grid line: only right at the crown's edge
            _ring_all |= ((_rim & _rawt & (1 - _GRIDLINES)) | (_edge & _rawt & _GRIDLINES & _rim)).astype(np.uint8)
            _gone |= (cv2.erode(_hf, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (21, 21))) & _GRIDLINES).astype(np.uint8)
            _HULLRIM.append(_rim); _nt += 1; continue
        _f = np.zeros_like(ink); cv2.drawContours(_f, [_c], -1, 1, -1)
        _area = _f.sum(); _hull = cv2.contourArea(cv2.convexHull(_c))
        _open = False
        if _hull <= 0: continue
        if _area / _hull < _tr.get('solidity', 0.80):
            # an open "C": the outline did not close. Re-close this one shape with larger kernels; the bridge
            # follows the crown's curve rather than a straight chord.
            _x0, _y0 = max(x_ - 12, 0), max(y_ - 12, 0); _x1, _y1 = min(x_ + w_ + 12, W), min(y_ + h_ + 12, H)
            _sub = _cand[_y0:_y1, _x0:_x1] * _cl[_y0:_y1, _x0:_x1]
            _ok = False
            for _ks in (13, 17, 21):
                _cc = cv2.morphologyEx(_sub, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (_ks, _ks)))
                _c2, _ = cv2.findContours(_cc, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
                if not _c2: continue
                _cm = max(_c2, key=cv2.contourArea)
                _ff = np.zeros_like(_sub); cv2.drawContours(_ff, [_cm], -1, 1, -1)
                _hh = cv2.contourArea(cv2.convexHull(_cm))
                if _hh > 0 and _ff.sum() / _hh >= _tr.get('solidity', 0.80):
                    _f = np.zeros_like(ink); _f[_y0:_y1, _x0:_x1] = _ff; _area = _f.sum(); _ok = True; break
            if not _ok:
                # named open crowns (config TREE_HULL_AT): close along the hull
                if any(x_ <= hx <= x_ + w_ and y_ <= hy <= y_ + h_ for (hx, hy) in _tr.get('hull_at', [])):
                    # the crown's flank lies ON a grid line: restore the raw scan ink in the hull's rim band
                    _hf = np.zeros_like(ink); cv2.fillPoly(_hf, [cv2.convexHull(_c)], 1)
                    _rim = (cv2.dilate(_hf, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))) - cv2.erode(_hf, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7)))).astype(np.uint8)
                    _RAWT = (img < cfg.get('THRESH', 120)).astype(np.uint8)
                    _ring_all |= (_rim & _RAWT).astype(np.uint8)
                    _gone |= (cv2.erode(_hf, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))) & _GRIDLINES).astype(np.uint8)
                    _nt += 1
                continue
            _open = True
        _bd = (_f - cv2.erode(_f, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))).astype(np.uint8)
        _cover = (_cand & _bd).sum() / max(_bd.sum(), 1)
        if _open and _cover < _tr.get('open_cover', 0.55) and not any(x_ <= hx <= x_ + w_ and y_ <= hy <= y_ + h_ for (hx, hy) in _tr.get('hull_at', [])): continue
        _fill = (_cand & _f).sum() / max(_area, 1)
        if _cover < _tr.get('cover', 0.45) or _fill > _tr.get('maxfill', 0.55): continue
        _w = _tr.get('weight', 3)
        _ring = (_f - cv2.erode(_f, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * _w - 1,) * 2))).astype(np.uint8)
        _inner = cv2.erode(_f, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * _w + 3,) * 2))
        _near = cv2.dilate(_cand * _f, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (_tr.get('near', 7),) * 2))
        _ring_all |= (_ring & (1 - _near)).astype(np.uint8)      # bridge only the gaps; intact lobes stay
        _gone |= (_inner & _GRIDLINES).astype(np.uint8)          # grid crossings left inside the crown
        _nt += 1
    ink = ((ink & (1 - _gone)) | _ring_all).astype(np.uint8)
    # restored rim ink: keep only pieces attached to the crown (drop grid stubs that left the rim)
    if _HULLRIM:
        _n2, _l2 = cv2.connectedComponents(ink, connectivity=8)
        for _rm in _HULLRIM:
            _ids, _cnt = np.unique(_l2[(_rm == 1) & (ink == 1)], return_counts=True)
            if len(_ids):
                _main = _ids[np.argmax(_cnt)]
                _drop = (_rm == 1) & (ink == 1) & (_l2 != _main)
                ink[_drop] = 0
    print('trees rebuilt:', _nt)
# dash zones: faint dashed outlines (foundations, planned works) survive by removing only LONG straight
# h/v lines (the printed grid) from the raw ink, then keeping short dash-sized pieces
for (za, zb, zc, zd) in cfg.get('DASH_ZONES', []):
    _r = (img[zb:zd, za:zc] < cfg.get('DASH_THRESH', 150)).astype(np.uint8)
    _L = cfg.get('DASH_LONG', 21)
    _lh = cv2.morphologyEx(_r, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (_L, 1)))
    _lv = cv2.morphologyEx(_r, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (1, _L)))
    _gl = cv2.dilate(_lh | _lv, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
    _d = (_r & (1 - _gl)).astype(np.uint8)
    _n, _lb, _st, _ = cv2.connectedComponentsWithStats(_d, 8)
    _kp = np.zeros(_n, bool)
    for _i in range(1, _n):
        x_, y_, w_, h_, a_ = _st[_i]
        if 6 <= a_ <= cfg.get('DASH_MAX', 80) and max(w_, h_) >= 4: _kp[_i] = True
    _dd = cv2.dilate(_kp[_lb].astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2)))
    if TINT is not None: _dd[TINT[zb:zd, za:zc] == 1] = 0
    ink[zb:zd, za:zc] |= _dd
# building footprints: the outline band keeps the raw ink (walls on grid lines survive); the interior keeps the
# grid-cleaned ink (the printed grid runs through buildings); never inside tint
if cfg.get('FOOTPRINTS'):
    _fp = np.zeros_like(ink)
    _rawf = (img < 120).astype(np.float32)
    def _samp(p0, p1, n=40):
        t = np.linspace(0.15, 0.85, n)
        xs = np.clip(np.round(p0[0] + t * (p1[0] - p0[0])).astype(int), 0, W - 1)
        ys = np.clip(np.round(p0[1] + t * (p1[1] - p0[1])).astype(int), 0, H - 1)
        return _rawf[ys, xs].mean()
    def _snap(poly, R=8):
        P = np.array(poly, np.float64); n = len(P)
        area = 0.5 * sum(P[i][0] * P[(i + 1) % n][1] - P[(i + 1) % n][0] * P[i][1] for i in range(n))
        lines = []
        for i in range(n):
            a, b = P[i], P[(i + 1) % n]; d = b - a; L = np.hypot(*d) or 1
            nrm = np.array([d[1], -d[0]]) / L
            if area < 0: nrm = -nrm                      # outward normal
            cands = []
            for t in np.arange(-R, R + 0.5, 0.5):
                on = _samp(a + nrm * t, b + nrm * t)
                if on < 0.6: continue
                outw = np.mean([_samp(a + nrm * (t + k), b + nrm * (t + k)) for k in (2.5, 4, 5.5)])
                inw = np.mean([_samp(a + nrm * (t - k), b + nrm * (t - k)) for k in (2.5, 4, 5.5)])
                cands.append((t, on, inw - outw))
            good = [c for c in cands if c[2] > 0.1]
            if good: bt = max(good, key=lambda c: c[2] - 0.02 * abs(c[0]))[0]
            elif cands: bt = min(cands, key=lambda c: abs(c[0]))[0]
            else: bt = 0.0
            lines.append((a + nrm * bt, d))
        out = []
        for i in range(n):
            (p1, d1), (p2, d2) = lines[i - 1], lines[i]
            M = np.array([d1, -d2]).T
            if abs(np.linalg.det(M)) < 1e-6: out.append(p2); continue
            tt = np.linalg.solve(M, p2 - p1); out.append(p1 + tt[0] * d1)
        return [tuple(map(float, q)) for q in out]
    SNAPPED = []
    for poly in cfg['FOOTPRINTS']:
        is_rect = len(poly) == 4 and not isinstance(poly[0], (tuple, list))
        if is_rect:
            a_, b_, c_, d_ = poly; poly = [(a_, b_), (c_, b_), (c_, d_), (a_, d_)]
        sp = _snap(poly) if (cfg.get('FP_SNAP', True) and is_rect) else poly
        SNAPPED.append(sp)
        cv2.fillPoly(_fp, [np.round(np.array(sp)).astype(np.int32)], 1)
    _out = cv2.dilate(_fp, cv2.getStructuringElement(cv2.MORPH_RECT, (2 * cfg.get('FP_OUT', 2) + 1,) * 2))
    _inn = cv2.erode(_fp, cv2.getStructuringElement(cv2.MORPH_RECT, (2 * cfg.get('FP_IN', 3) + 1,) * 2))
    _band = (_out & (1 - _inn)).astype(np.uint8)
    if TINT is not None: _band[TINT == 1] = 0
    _rawfp = (img < cfg.get('FP_THRESH', 120)).astype(np.uint8)
    ink = (ink | (_rawfp & _band)).astype(np.uint8)
    FP_MASK = _out
    for (a, b, c, d) in cfg.get('LABEL_MASKS', []) + cfg.get('ERASE', []):
        ink[b:d, a:c] = 0

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
# no-grid variant for illustrated maps whose floor grid is drawn into the art (oblique views): remove long, thin,
# straight lines found by a Hough transform; thick walls (3+ px) and furniture survive
INK_PATH_NG = None
if cfg.get('NOGRID_STRIP'):
    _ns = cfg['NOGRID_STRIP']
    _thk = cv2.morphologyEx(ink, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
    _thk = cv2.dilate(_thk, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))) & ink
    _thin = (ink & (1 - _thk)).astype(np.uint8)
    _lines = cv2.HoughLinesP(_thin * 255, 1, np.pi / 720, _ns.get('votes', 40), minLineLength=_ns.get('min_len', 50), maxLineGap=_ns.get('gap', 6))
    _lm = np.zeros_like(ink)
    _angs = _ns.get('angles')
    for x1_, y1_, x2_, y2_ in (_lines.reshape(-1, 4) if _lines is not None else []):
        _a = (np.degrees(np.arctan2(y2_ - y1_, x2_ - x1_)) + 180) % 180
        if _angs and not any(min(abs(_a - a0), 180 - abs(_a - a0)) <= _ns.get('ang_tol', 3) for a0 in _angs): continue
        cv2.line(_lm, (int(x1_), int(y1_)), (int(x2_), int(y2_)), 1, _ns.get('width', 3))
    for (a_, b_, c_, d_) in _ns.get('keep', []): _lm[b_:d_, a_:c_] = 0
    if _ns.get('dense_keep'):
        # furniture and fixtures are dense clusters of strokes: never strip lines inside them
        _dn = cv2.blur((ink & (1 - _lm)).astype(np.float32), (9, 9))
        _fk = cv2.dilate((_dn > _ns['dense_keep']).astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7)))
        _lm[_fk == 1] = 0
    _ng = (ink & (1 - (_lm & _thin))).astype(np.uint8)
    _ng = despeckle(_ng, _ns.get('speck', 6))
    INK_PATH_NG = vectorize(_ng)
TINT_PATH = vectorize(TINT) if TINT is not None else ''
GM_PATH = vectorize(gm_ink) if gm_ink.any() else ''

FLOOR, GRID, INK, PAPER = '#efe3c4', '#8a7754', '#151310', '#e6d5ae'
S = 50 / PX                                    # svg scale: 50 units per grid square

def grid_lines():
    o = []
    dv = cfg.get('GRID_DIV', 1); px, py = PX / dv, PY / dv
    x0g, y0g = OX % px, OY % py
    k = 0
    while x0g + k * px < W:
        x = (x0g + k * px) * S; o.append(f'M{x:.1f} 0V{H * S:.1f}'); k += 1
    k = 0
    while y0g + k * py < H:
        y = (y0g + k * py) * S; o.append(f'M0 {y:.1f}H{W * S:.1f}'); k += 1
    return ' '.join(o)

def _gclip():
    g = cfg.get('GRID_CLIP')
    return f'<clipPath id="gclip"><circle cx="{g[0] * S:.1f}" cy="{g[1] * S:.1f}" r="{g[2] * S:.1f}"/></clipPath>' if g else ''
def _gcl(): return ' clip-path="url(#gclip)"' if cfg.get('GRID_CLIP') else ''

def build(mode):
    gm, pr = mode in ('gm', 'print'), mode == 'print'
    Wd, Ht = W * S, H * S
    top = 90 if pr else 0; bot = 70 if pr else 0
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {-top} {Wd:.0f} {Ht + top + bot:.0f}" width="{Wd:.0f}" height="{Ht + top + bot:.0f}" font-family="Georgia, \'Times New Roman\', serif">',
         f'<title>{cfg["TITLE"]} ({mode.upper()})</title>',
         '<defs><filter id="paper" x="0" y="0" width="1" height="1"><feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="4" seed="11" result="n"/><feColorMatrix in="n" type="matrix" values="0 0 0 0 0.36  0 0 0 0 0.26  0 0 0 0 0.12  0 0 0 0.22 0" result="t"/><feComposite in="t" in2="SourceGraphic" operator="in" result="tt"/><feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="tt"/></feMerge></filter></defs>',
         f'<rect x="0" y="{-top}" width="{Wd:.0f}" height="{Ht + top + bot:.0f}" fill="{PAPER}" filter="url(#paper)"/>',
         f'<rect x="0" y="0" width="{Wd:.0f}" height="{Ht:.0f}" fill="{FLOOR}" filter="url(#paper)"/>',
         (f'<g transform="scale({S:.5f})"><path d="{TINT_PATH}" fill="{cfg.get("TINT_COLOR", "#cdb98d")}" fill-rule="evenodd"/></g>' if TINT_PATH else ''),
         (f'{_gclip()}<path d="{grid_lines()}" stroke="{GRID}" stroke-width="{1.4 if cfg.get('GRID_DIV', 1) == 1 else 1.1}" opacity="0.75" fill="none"{_gcl()}/>' if (mode != 'player_nogrid' and cfg.get('DRAW_GRID', True)) else ''),
         f'<g transform="scale({S:.5f})"><path d="{(INK_PATH_NG if (mode == "player_nogrid" and INK_PATH_NG) else INK_PATH)}" fill="{INK}" fill-rule="evenodd"/></g>']
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
    for _pp in cfg.get('FILLPOLYS', []):          # solid wall patches as polygons (box px), all versions
        o.append(f'<path d="M' + ' L'.join(f'{x * S:.1f} {y * S:.1f}' for x, y in _pp) + f'Z" fill="{INK}"/>')
    if not gm:
        for _pp in cfg.get('PLAYER_FLOORPOLYS', []):  # parchment patches on player versions (hide GM-only marks)
            o.append(f'<path d="M' + ' L'.join(f'{x * S:.1f} {y * S:.1f}' for x, y in _pp) + f'Z" fill="{FLOOR}" filter="url(#paper)"/>')
        for _pp in cfg.get('PLAYER_FILLPOLYS', []):   # solid patches on player versions only (hide GM-only openings)
            o.append(f'<path d="M' + ' L'.join(f'{x * S:.1f} {y * S:.1f}' for x, y in _pp) + f'Z" fill="{INK}"/>')
    for (a, b, c, d) in cfg.get('FILLS', []):     # solid wall patches (box px), all versions
        o.append(f'<rect x="{a * S:.1f}" y="{b * S:.1f}" width="{(c - a) * S:.1f}" height="{(d - b) * S:.1f}" fill="{INK}"/>')
    # parapets: outlined band with solid merlons every PX/3 along its length
    for (a, b, c, d) in cfg.get('PARAPETS', []):
        X0, Y0, X1, Y1 = a * S, b * S, c * S, d * S
        o.append(f'<rect x="{X0:.1f}" y="{Y0:.1f}" width="{X1-X0:.1f}" height="{Y1-Y0:.1f}" fill="{FLOOR}" stroke="{INK}" stroke-width="{1.6 * S:.1f}"/>')
        per = PX / 3 * S; m = 0.62 * per
        if (c - a) >= (d - b):
            x = X0 + (per - m) / 2
            while x + m <= X1 + 0.1:
                o.append(f'<rect x="{x:.1f}" y="{Y0 + 1.2 * S:.1f}" width="{m:.1f}" height="{Y1 - Y0 - 2.4 * S:.1f}" fill="{INK}"/>'); x += per
        else:
            y = Y0 + (per - m) / 2
            while y + m <= Y1 + 0.1:
                o.append(f'<rect x="{X0 + 1.2 * S:.1f}" y="{y:.1f}" width="{X1 - X0 - 2.4 * S:.1f}" height="{m:.1f}" fill="{INK}"/>'); y += per
    # explicit thin walls (box px polylines), doors, angled stairs: features too fine for the trace
    LW = cfg.get('LINE_W', 3.2) * S
    for pts in cfg.get('HAIRLINES', []):          # thin art lines (floor tiles) lost under a mask
        d = 'M' + ' L'.join(f'{x * S:.1f} {y * S:.1f}' for x, y in pts)
        o.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{cfg.get("HAIR_W", 2.0) * S:.1f}" stroke-linecap="round"/>')
    for pts in cfg.get('LINES', []):
        d = 'M' + ' L'.join(f'{x * S:.1f} {y * S:.1f}' for x, y in pts)
        o.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{LW:.1f}" stroke-linecap="square"/>')
    for _dd in cfg.get('DOORS', []):
        x, y, orient, kind = _dd[:4]
        _dl, _dw = (_dd[4], _dd[5]) if len(_dd) > 5 else cfg.get('DOOR_SIZE', (5.5, 15))[::-1]
        X, Y = x * S, y * S
        if kind == 'rect':
            if isinstance(orient, (int, float)):
                w, h = _dl * S, _dw * S
                o.append(f'<rect x="{X - w / 2:.1f}" y="{Y - h / 2:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{1.5 * S:.1f}" fill="{FLOOR}" stroke="{INK}" stroke-width="{2.2 * S:.1f}" transform="rotate({orient} {X:.1f} {Y:.1f})"/>')
                continue
            w, h = (_dw * S, _dl * S) if orient == 'v' else (_dl * S, _dw * S)
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
    for t in cfg.get('TEXTS', []):
        txt, x, y, size = t[:4]; txt = txt.replace('&', '&amp;'); anchor = t[4] if len(t) > 4 else 'middle'; style = t[5] if len(t) > 5 else 'bold'
        fw = 'bold' if 'bold' in style else 'normal'; fs = 'italic' if 'italic' in style else 'normal'
        _rt = f' transform="rotate({t[6]} {x * S:.1f} {y * S:.1f})"' if len(t) > 6 else ''
        o.append(f'<text x="{x * S:.1f}" y="{y * S:.1f}" font-size="{size * S:.1f}" font-weight="{fw}" font-style="{fs}" text-anchor="{anchor}" letter-spacing="{0.06 * size * S:.1f}" fill="{INK}" stroke="{FLOOR}" stroke-width="{0.28 * size * S:.1f}" stroke-linejoin="round" paint-order="stroke"{_rt}>{txt}</text>')
    for (xa, ya, xb, yb) in cfg.get('ARROWS', []):     # box px; head at (xb, yb)
        dx, dy = xb - xa, yb - ya; L = (dx * dx + dy * dy) ** 0.5; ux, uy = dx / L, dy / L; hl, hw = 9, 3.6
        o.append(f'<line x1="{xa * S:.1f}" y1="{ya * S:.1f}" x2="{(xb - ux * hl) * S:.1f}" y2="{(yb - uy * hl) * S:.1f}" stroke="{INK}" stroke-width="{1.7 * S:.1f}"/>')
        o.append(f'<path d="M{xb * S:.1f} {yb * S:.1f} L{(xb - ux * hl - uy * hw) * S:.1f} {(yb - uy * hl + ux * hw) * S:.1f} L{(xb - ux * hl + uy * hw) * S:.1f} {(yb - uy * hl - ux * hw) * S:.1f}Z" fill="{INK}"/>')
    for pts in cfg.get('DASHLINES', []):
        d = 'M' + ' L'.join(f'{x * S:.1f} {y * S:.1f}' for x, y in pts)
        o.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{2.0 * S:.1f}" stroke-dasharray="{2.2 * S:.1f} {3.2 * S:.1f}" stroke-linecap="round"/>')
    for (x, y, r) in cfg.get('DASHCIRCLES', []):
        o.append(f'<circle cx="{x * S:.1f}" cy="{y * S:.1f}" r="{r * S:.1f}" fill="none" stroke="{INK}" stroke-width="{1.8 * S:.1f}" stroke-dasharray="{2.6 * S:.1f} {2.4 * S:.1f}"/>')
    for k_, poly in enumerate(cfg.get('RUBBLE', [])):   # stippled rubble inside a polygon (box px)
        import random as _r; _r.seed(1000 + k_)
        _pm = np.zeros((H, W), np.uint8); cv2.fillPoly(_pm, [np.array(poly, np.int32)], 1)
        ys_, xs_ = np.nonzero(_pm); n_ = int(len(xs_) / cfg.get('RUBBLE_SPARSE', 14))
        cid = f'rb{k_}'; d_ = 'M' + ' L'.join(f'{x * S:.1f} {y * S:.1f}' for x, y in poly) + 'Z'
        o.append(f'<clipPath id="{cid}"><path d="{d_}"/></clipPath><g clip-path="url(#{cid})" stroke="{INK}" stroke-linecap="round">')
        for _ in range(n_):
            i_ = _r.randrange(len(xs_)); x, y = xs_[i_] + _r.random(), ys_[i_] + _r.random()
            if _r.random() < 0.45:
                o.append(f'<circle cx="{x * S:.1f}" cy="{y * S:.1f}" r="{_r.uniform(0.5, 0.9) * S:.1f}" fill="{INK}" stroke="none"/>')
            else:
                a_ = _r.uniform(0, 3.1416); L_ = _r.uniform(1.5, 3.5)
                o.append(f'<line x1="{x * S:.1f}" y1="{y * S:.1f}" x2="{(x + L_ * np.cos(a_)) * S:.1f}" y2="{(y + L_ * np.sin(a_)) * S:.1f}" stroke-width="{_r.uniform(0.7, 1.2) * S:.1f}"/>')
        o.append('</g>')
    for (x, y, dr, sz) in cfg.get('TRIS', []):      # statue triangles, apex pointing dr (r/l/u/d)
        h_ = sz / 2
        pts = {'r': [(x + h_, y), (x - h_, y - h_), (x - h_, y + h_)], 'l': [(x - h_, y), (x + h_, y - h_), (x + h_, y + h_)],
               'u': [(x, y - h_), (x - h_, y + h_), (x + h_, y + h_)], 'd': [(x, y + h_), (x - h_, y - h_), (x + h_, y - h_)]}[dr]
        d_ = 'M' + ' L'.join(f'{px * S:.1f} {py * S:.1f}' for px, py in pts) + 'Z'
        o.append(f'<path d="{d_}" fill="{FLOOR}" stroke="{INK}" stroke-width="{2.0 * S:.1f}" stroke-linejoin="round"/>')
    for (cx, cy, rx, ry, sw) in cfg.get('ELLIPSES', []):
        o.append(f'<ellipse cx="{cx * S:.1f}" cy="{cy * S:.1f}" rx="{rx * S:.1f}" ry="{ry * S:.1f}" fill="none" stroke="{INK}" stroke-width="{sw * S:.1f}"/>')
    for (x0_, x1_, y_, amp, per, sw) in cfg.get('WAVES', []):
        n_ = max(8, int((x1_ - x0_) * 3)); pts = []
        for i in range(n_ + 1):
            xx = x0_ + (x1_ - x0_) * i / n_; pts.append((xx, y_ + amp * np.sin(2 * np.pi * (xx - x0_) / per)))
        d_ = 'M' + ' L'.join(f'{px * S:.1f} {py * S:.1f}' for px, py in pts)
        o.append(f'<path d="{d_}" fill="none" stroke="{INK}" stroke-width="{sw * S:.1f}" stroke-linecap="round" stroke-linejoin="round"/>')
    for (y_, xa_, xb_, sw_) in cfg.get('TREADS', []):
        o.append(f'<line x1="{xa_ * S:.1f}" y1="{y_ * S:.1f}" x2="{xb_ * S:.1f}" y2="{y_ * S:.1f}" stroke="{INK}" stroke-width="{sw_ * S:.1f}" stroke-linecap="butt"/>')
    for (a_, b_, c_, d_, sw) in cfg.get('RECTS', []):    # outline rectangles (box px)
        o.append(f'<rect x="{a_ * S:.1f}" y="{b_ * S:.1f}" width="{(c_ - a_) * S:.1f}" height="{(d_ - b_) * S:.1f}" fill="none" stroke="{INK}" stroke-width="{sw * S:.1f}"/>')
    for (cx, cy, rx, ry, a0, a1, sw) in cfg.get('ARCS', []):   # elliptical arc, degrees (0 = +x, 90 = +y)
        n_ = 48; pts = [(cx + rx * np.cos(np.radians(a0 + (a1 - a0) * i / n_)), cy + ry * np.sin(np.radians(a0 + (a1 - a0) * i / n_))) for i in range(n_ + 1)]
        o.append('<path d="M' + ' L'.join(f'{px * S:.1f} {py * S:.1f}' for px, py in pts) + f'" fill="none" stroke="{INK}" stroke-width="{sw * S:.1f}" stroke-linecap="round"/>')
    for (y0_, y1_, x_, amp, per, sw) in cfg.get('WAVES_V', []):
        n_ = max(8, int((y1_ - y0_) * 3)); pts = []
        for i in range(n_ + 1):
            yy = y0_ + (y1_ - y0_) * i / n_; pts.append((x_ + amp * np.sin(2 * np.pi * (yy - y0_) / per), yy))
        o.append('<path d="M' + ' L'.join(f'{px * S:.1f} {py * S:.1f}' for px, py in pts) + f'" fill="none" stroke="{INK}" stroke-width="{sw * S:.1f}" stroke-linecap="round" stroke-linejoin="round"/>')
    for (x_, ya_, yb_, sw_) in cfg.get('TREADS_V', []):
        o.append(f'<line x1="{x_ * S:.1f}" y1="{ya_ * S:.1f}" x2="{x_ * S:.1f}" y2="{yb_ * S:.1f}" stroke="{INK}" stroke-width="{sw_ * S:.1f}" stroke-linecap="butt"/>')
    for (pts_, sw) in cfg.get('POLYS', []):       # closed outlined polygons, floor-filled (later ones on top)
        o.append('<path d="M' + ' L'.join(f'{px * S:.1f} {py * S:.1f}' for px, py in pts_) + f'Z" fill="{FLOOR}" stroke="{INK}" stroke-width="{sw * S:.1f}" stroke-linejoin="miter"/>')
    for (x, y) in cfg.get('DOTS', []):
        o.append(f'<circle cx="{x * S:.1f}" cy="{y * S:.1f}" r="{cfg.get("DOT_R", 4.2) * S:.1f}" fill="{INK}"/>')
    for (x, y, r) in cfg.get('STARS', []):
        pts = [(x + (r if k % 2 == 0 else r * 0.42) * np.sin(np.pi * k / 5), y - (r if k % 2 == 0 else r * 0.42) * np.cos(np.pi * k / 5)) for k in range(10)]
        o.append('<path d="M' + ' L'.join(f'{px * S:.1f} {py * S:.1f}' for px, py in pts) + f'Z" fill="{INK}"/>')
    for (p0, pc, p1, wd) in cfg.get('CHAINARCS', []):
        d_ = f'M{p0[0] * S:.1f} {p0[1] * S:.1f} Q{pc[0] * S:.1f} {pc[1] * S:.1f} {p1[0] * S:.1f} {p1[1] * S:.1f}'
        o.append(f'<path d="{d_}" fill="none" stroke="{INK}" stroke-width="{wd * S:.1f}" stroke-linecap="round"/>')
        o.append(f'<path d="{d_}" fill="none" stroke="{FLOOR}" stroke-width="{(wd - 3.2) * S:.1f}" stroke-dasharray="{3.0 * S:.1f} {2.2 * S:.1f}"/>')
    for (d_, sw) in cfg.get('PATHS', []):          # raw path in box px
        o.append(f'<g transform="scale({S:.5f})"><path d="{d_}" fill="none" stroke="{INK}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/></g>')
    for k_, poly in enumerate(cfg.get('BONES', [])):    # scattered bones and skulls inside a polygon (box px)
        import random as _r; _r.seed(2000 + k_)
        _pm = np.zeros((H, W), np.uint8); cv2.fillPoly(_pm, [np.array(poly, np.int32)], 1)
        _pm = cv2.erode(_pm, np.ones((5, 5), np.uint8))
        ys_, xs_ = np.nonzero(_pm); area_ = len(xs_)
        placed = []
        n_ = int(area_ / cfg.get('BONE_SPARSE', 55))
        tries = 0
        while len(placed) < n_ and tries < n_ * 30:
            tries += 1
            i_ = _r.randrange(area_); x, y = xs_[i_] + _r.random(), ys_[i_] + _r.random()
            skull = _r.random() < cfg.get('SKULL_P', 0.14)
            rr = 5.0 if skull else 4.0
            if any((x - px_) ** 2 + (y - py_) ** 2 < (rr + pr_ + 0.8) ** 2 for px_, py_, pr_ in placed): continue
            placed.append((x, y, rr))
            if skull:
                r_ = 3.3
                o.append(f'<g transform="translate({x * S:.1f} {y * S:.1f}) rotate({_r.uniform(-30, 30):.0f}) scale({S:.4f})">'
                         f'<path d="M-{r_} 0.4 A{r_} {r_} 0 1 1 {r_} 0.4 L{r_ * 0.7} 2.4 L-{r_ * 0.7} 2.4 Z" fill="{FLOOR}" stroke="{INK}" stroke-width="0.85"/>'
                         f'<circle cx="-1.25" cy="0.2" r="0.85" fill="{INK}"/><circle cx="1.25" cy="0.2" r="0.85" fill="{INK}"/></g>')
            else:
                L_ = _r.uniform(2.8, 4.2); a_ = _r.uniform(0, 180)
                o.append(f'<g transform="translate({x * S:.1f} {y * S:.1f}) rotate({a_:.0f}) scale({S:.4f})">'
                         f'<line x1="-{L_}" y1="0" x2="{L_}" y2="0" stroke="{INK}" stroke-width="0.9"/>'
                         f'<circle cx="-{L_}" cy="-0.55" r="0.6" fill="{INK}"/><circle cx="-{L_}" cy="0.55" r="0.6" fill="{INK}"/>'
                         f'<circle cx="{L_}" cy="-0.55" r="0.6" fill="{INK}"/><circle cx="{L_}" cy="0.55" r="0.6" fill="{INK}"/></g>')
    for (x, y) in cfg.get('XMARKS', []):
        for sg in (1, -1):
            o.append(f'<line x1="{(x - 3.5) * S:.1f}" y1="{(y - 3.5 * sg) * S:.1f}" x2="{(x + 3.5) * S:.1f}" y2="{(y + 3.5 * sg) * S:.1f}" stroke="{INK}" stroke-width="{1.6 * S:.1f}" stroke-linecap="round"/>')
    if gm and GM_PATH and cfg.get('DRAW_GM_INK', True):
        o.append(f'<g transform="scale({S:.5f})"><path d="{GM_PATH}" fill="{INK}" fill-rule="evenodd"/></g>')
    if gm:
        for t, (gx, gy) in cfg.get('LABELS', {}).items():
            x, y = (OX + gx * PX) * S, (OY + gy * PY) * S
            _ls = cfg.get('LABEL_SIZE', 24)
            o.append(f'<text x="{x:.1f}" y="{y + _ls / 3:.1f}" font-size="{_ls}" font-weight="bold" text-anchor="middle" fill="{INK}" stroke="{FLOOR}" stroke-width="{_ls / 4.5:.1f}" paint-order="stroke">{t.strip()}</text>')
        for it in cfg.get('LABEL_LIST', []):       # (text, x, y, size, rot) in box px
            t, x, y, sz = it[:4]; rot = it[4] if len(it) > 4 else 0
            fs = sz * S * cfg.get('LABEL_SCALE', 1.25); tr = f' transform="rotate({rot} {x * S:.1f} {y * S:.1f})"' if rot else ''
            ff = ' font-family="Times New Roman, serif"' if set(t) <= set('IV') else ''
            o.append(f'<text x="{x * S:.1f}" y="{y * S + fs * 0.36:.1f}" font-size="{fs:.1f}" font-weight="bold"{ff} text-anchor="middle" fill="{INK}" stroke="{FLOOR}" stroke-width="{fs / 4.5:.1f}" paint-order="stroke"{tr}>{t}</text>')
        for (bx, by) in cfg.get('SECRETS', []):     # secret doors: bold ink S, GM only (box px)
            _ss = cfg.get('SECRET_SIZE', 26)
            o.append(f'<text x="{bx * S:.1f}" y="{by * S + _ss / 3:.1f}" font-size="{_ss}" font-weight="bold" text-anchor="middle" fill="{INK}" stroke="{FLOOR}" stroke-width="{_ss / 5:.1f}" paint-order="stroke">S</text>')
        for kind, gx, gy in cfg.get('GM_MARKS', []):
            x, y = (OX + gx * PX) * S, (OY + gy * PY) * S
            o.append(f'<text x="{x:.1f}" y="{y + 7:.1f}" font-size="20" font-weight="bold" text-anchor="middle" fill="#9b2226" stroke="{FLOOR}" stroke-width="4" paint-order="stroke">{kind}</text>')
    o.append(f'<rect x="0" y="0" width="{Wd:.0f}" height="{Ht:.0f}" fill="none" stroke="{INK}" stroke-width="4"/>')
    if pr:
        o.append(f'<text x="18" y="-40" font-size="38" font-weight="bold" fill="{INK}" letter-spacing="2">{cfg["TITLE"].upper()}</text>')
        o.append(f'<text x="20" y="-12" font-size="18" fill="#5a4a32" font-style="italic">{cfg["SUB"]}</text>')
        sx, sy = 20, Ht + 40
        for i in (range(5) if cfg.get('SCALE_BAR', True) else []):
            o.append(f'<rect x="{sx + i * 50}" y="{sy}" width="50" height="10" fill="{FLOOR if i % 2 == 0 else INK}" stroke="{INK}" stroke-width="1.5"/>')
        if cfg.get('SCALE_BAR', True):
            ft = cfg['SCALE_FT']
            o.append(f'<text x="{sx}" y="{sy - 8}" font-size="16" fill="{INK}">0</text><text x="{sx + 230}" y="{sy - 8}" font-size="16" fill="{INK}">{5 * ft} ft</text>')
            _sqft = ft / cfg.get('GRID_DIV', 1); _sqft = int(_sqft) if _sqft == int(_sqft) else _sqft
            o.append(f'<text x="{sx + 270}" y="{sy + 10}" font-size="16" fill="{INK}">1 square = {_sqft} feet</text>')
        else:
            o.append(f'<text x="{sx}" y="{sy + 10}" font-size="18" fill="{INK}">{cfg.get("SCALE_TEXT", "")}</text>')
        if cfg.get('NOTE'):
            o.append(f'<text x="{Wd - 20:.0f}" y="{sy + 10}" font-size="15" text-anchor="end" fill="#5a4a32" font-style="italic">{cfg["NOTE"]}</text>')
    o.append('</svg>')
    return '\n'.join(o)

base = cfg['FILE']
ALLV = (('gm', 'GM'), ('player', 'Player'), ('player_nogrid', 'Player (No Grid)'), ('print', 'Print'))
for mode, name in [v for v in ALLV if v[0] in cfg.get('MODES', [m for m, _ in ALLV])]:
    open(f'{OUT}/{base} - {name}.svg', 'w').write(build(mode))
print('ok', W, H, len(INK_PATH))
