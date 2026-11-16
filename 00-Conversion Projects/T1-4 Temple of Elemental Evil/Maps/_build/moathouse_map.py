"""Trace Map 8 (Moathouse Dungeon) from the T1-4 scan into a styled vector map.
Outputs GM / Player / Print SVGs. Coordinates: grid units (1 = 10 ft) -> SVG units (S per cell)."""
import cv2, numpy as np, sys, os
OUT = sys.argv[1] if len(sys.argv) > 1 else 'out/maps'
os.makedirs(OUT, exist_ok=True)

m = cv2.imread('maps/m8_box.png', 0)
PX, OX, PY, OY = 16.69, 13.75, 16.61, 3.5          # lattice fitted to the scan
S = 50                                              # svg units per 10-ft square
C0, R0, C1, R1 = 0, 0, 38.5, 36.0                   # visible window (grid units)

def g(x, y):  # scan px -> grid units
    return (x - OX) / PX, (y - OY) / PY

# ---------- floor mask ----------
b = (m > 110).astype(np.uint8) * 255
b = cv2.morphologyEx(b, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7)))
b = cv2.morphologyEx(b, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
b[39:70, 49:166] = 0                                # "Dungeon Level" label box
b[:7, :] = 0; b[-6:, :] = 0; b[:, -4:] = 0          # scan border strips
# cave zone (no grid, organic outline)
H, W = b.shape
yy, xx = np.mgrid[0:H, 0:W]
gx, gy = (xx - OX) / PX, (yy - OY) / PY
cave_zone = ((gx < 7.9) & (gy > 9.1)) | ((gx < 11.2) & (gy > 14.2)) | ((gx < 15) & (gy > 25.4))
b[(gx > 12.55) & (gx < 14.75) & (gy > 12.7) & (gy < 18.85)] = 0   # hidden crawlway is not floor
# hand cleanup: area 31 crypt niches (scan bars blur into spikes) and the notch south of 28
def zero(c0, c1, r0, r1): b[(gx >= c0) & (gx <= c1) & (gy >= r0) & (gy <= r1)] = 0
def fill(c0, c1, r0, r1): b[(gx >= c0) & (gx <= c1) & (gy >= r0) & (gy <= r1)] = 255
zero(14.05, 17.95, 19.6, 20.97); zero(14.05, 16.95, 23.03, 24.3); zero(21.0, 23.0, 27.03, 27.7)
# crypt niches: (center x, top y, bottom y, side the room is on)
NICHES = [(c, 20.05, 21.0, 'below') for c in (14.5, 15.5, 16.5, 17.5)] + \
         [(c, 23.0, 23.95, 'above') for c in (14.5, 15.25, 16.0, 16.75)] + \
         [(c, 18.1, 19.0, 'below') for c in (12.5, 13.5)]
zero(12.2, 13.8, 18.0, 18.98)
room = np.where(cave_zone, 0, b).astype(np.uint8)
cave = np.where(cave_zone, b, 0).astype(np.uint8)

def snap(v):
    r = round(v)
    if abs(v - r) < 0.3: return float(r)
    h = round(v * 2) / 2
    return h if abs(v - h) < 0.08 else v

def polys(mask, eps, do_snap, min_area):
    cs, hier = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    out = []
    for cn in cs:
        if cv2.contourArea(cn) < min_area: continue
        ap = cv2.approxPolyDP(cn, eps, True)[:, 0, :]
        pts = []
        for x, y in ap:
            u, v = g(x + 0.5, y + 0.5)
            if do_snap: u, v = snap(u), snap(v)
            pts.append((u, v))
        out.append(pts)
    return out

room_polys = polys(room, 1.6, True, 40)
# hand fixes: south wall of rooms 18-20 sits on line 9 (the scan's heavy wall line eats the floor)
room_polys = [[(u, 9.0) if (u < 8.5 and 8.3 < v < 9.1) else (u, v) for (u, v) in p] for p in room_polys]
cave_polys = polys(cave, 0.9, False, 25)
def _cen(p): return sum(u for u, v in p) / len(p), sum(v for u, v in p) / len(p)
cave_polys = [p for p in cave_polys if not (10.4 < _cen(p)[0] < 12.3 and 17.5 < _cen(p)[1] < 25.5)]

def path(pts):
    return 'M' + ' L'.join(f'{(u-C0)*S:.1f} {(v-R0)*S:.1f}' for u, v in pts) + ' Z'

# ---------- features (grid coords read off the scan) ----------
# walls: ((x1,y1),(x2,y2)) interior walls lost in the floor mask
walls = [((5, 5), (5, 6)), ((5, 8), (5, 9)), ((3, 7), (5, 7)), ((10, 5), (10, 7)),
         ((12, 6), (12, 7)), ((10.5, 7), (12, 7)), ((12.5, 7), (13, 7)), ((11, 9), (11, 14)), ((11, 9), (13, 9))]
# doors: (x, y, orient) orient 'v' = door in a vertical wall (center on line x), 'h' = horizontal wall
doors = [(5, 6.5, 'v'), (5, 7.5, 'v'), (12, 5.5, 'v'), (10.5, 7, 'h'), (12.5, 7, 'h'),
         (9, 9.5, 'v'), (9, 10.5, 'v'), (9, 11.5, 'v'), (9, 12.5, 'v'), (9, 13.5, 'v'),
         (31, 15.5, 'v'), (21.5, 20, 'h'), (25.5, 20, 'h'), (32.5, 28, 'h'), (32.1, 28.5, 'v')]
locked = {(5, 6.5), (5, 7.5)}
false_doors = [(33, 7.5, 'v'), (33, 9.5, 'v'), (33, 11.5, 'v'), (23.5, 20, 'h')]
secret = [(16, 6.5, 'v'), (17, 6.5, 'v'), (24.5, 9, 'h'), (14.5, 19.1, 'h')]
pillars = [(6, 7), (9, 7), (10, 9), (10, 11), (10, 13), (12, 10), (13, 4), (14, 5), (13, 6), (15, 6)]
pillar_secret = (12, 13)
stairs = [((7.15, 6.0), (7.85, 8.0), 'up', 'v'), ((17.4, 6.12), (19.6, 6.88), 'down', 'h'),
          ((25.1, 27.1), (25.9, 29.0), 'down', 'v')]
curved_stair = (16.0, 5.0)
rubble = [(5.45, 6.25), (5.75, 6.55), (5.5, 6.85), (5.8, 7.2), (5.45, 7.5), (5.75, 7.75), (5.6, 6.05)]
labels = {18: (7.0, 8.55), 19: (3.5, 8.5), 20: (3.5, 5.6), 21: (10.55, 10.5), 22: (12.0, 11.5), 23: (10.6, 5.6),
          24: (13.6, 4.6), 25: (12.0, 8.5), 26: (24.0, 7.6), '26 ': (22.0, 8.6), 27: (30.2, 2.6), 28: (30.9, 9.65),
          '28 ': (23.4, 19.55), 29: (17.4, 16.6), 30: (23.4, 30.7), 31: (13.4, 22.0), 32: (34.4, 28.75),
          33: (30.6, 19.55), 34: (29.5, 15.6), 35: (32.6, 14.6), 'A': (12.6, 30.4), 'B': (7.55, 30.6)}
guards = [(30.5, 18.5), (31.6, 19.4), (30.4, 20.5), (32.5, 20.6), (32.5, 24.5), (32.5, 27.4)]
passage = [(12.35, 13.0), (14.45, 13.0), (14.45, 19.0)]
grate = ((21.3, 7.2), (22.9, 8.8))
pool = (23.5, 30.6, 0.95, 1.05)

# ---------- style ----------
ROCK, FLOOR, GRID, INK, WATER = '#151310', '#efe3c4', '#8a7754', '#151310', '#ddd5bd'
CAVE, PAPER = '#e8d9b5', '#e6d5ae'

def P(u, v): return f'{(u-C0)*S:.1f}', f'{(v-R0)*S:.1f}'

def door_svg(x, y, o, kind='door'):
    cx, cy = (x - C0) * S, (y - R0) * S
    w, h = (0.24 * S, 0.62 * S) if o == 'v' else (0.62 * S, 0.24 * S)
    s = f'<rect x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{FLOOR}" stroke="{ROCK}" stroke-width="3"/>'
    if kind == 'false':
        s += (f'<line x1="{cx-w/2:.1f}" y1="{cy-h/2:.1f}" x2="{cx+w/2:.1f}" y2="{cy+h/2:.1f}" stroke="{ROCK}" stroke-width="3"/>')
    if kind == 'locked':
        s += f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="2.6" fill="{ROCK}"/>'
    return s

def secret_svg(x, y, o):
    cx, cy = (x - C0) * S, (y - R0) * S
    return (f'<text x="{cx:.1f}" y="{cy+7:.1f}" font-size="22" font-weight="bold" text-anchor="middle" '
            f'fill="{ROCK}" stroke="{FLOOR}" stroke-width="4" paint-order="stroke">S</text>')

def stair_svg(a, bb, d, o):
    (x0, y0), (x1, y1) = a, bb
    X0, Y0, X1, Y1 = (x0 - C0) * S, (y0 - R0) * S, (x1 - C0) * S, (y1 - R0) * S
    s = f'<rect x="{X0:.1f}" y="{Y0:.1f}" width="{X1-X0:.1f}" height="{Y1-Y0:.1f}" fill="{FLOOR}" stroke="{ROCK}" stroke-width="2"/>'
    n = 9
    for i in range(1, n):
        t = i / n
        if o == 'v':
            yv = Y0 + t * (Y1 - Y0); inset = (X1 - X0) * (0.0 if d == 'up' else 0.32 * t)
            s += f'<line x1="{X0+inset:.1f}" y1="{yv:.1f}" x2="{X1-inset:.1f}" y2="{yv:.1f}" stroke="{ROCK}" stroke-width="2"/>'
        else:
            xv = X0 + t * (X1 - X0); inset = (Y1 - Y0) * (0.0 if d == 'up' else 0.32 * t)
            s += f'<line x1="{xv:.1f}" y1="{Y0+inset:.1f}" x2="{xv:.1f}" y2="{Y1-inset:.1f}" stroke="{ROCK}" stroke-width="2"/>'
    return s

def build(mode):
    gm, pr = mode in ('gm', 'print'), mode == 'print'
    Wd, Ht = (C1 - C0) * S, (R1 - R0) * S
    pad_top = 90 if pr else 0
    pad_bot = 110 if pr else 0
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {-pad_top} {Wd:.0f} {Ht+pad_top+pad_bot:.0f}" '
         f'width="{Wd:.0f}" height="{Ht+pad_top+pad_bot:.0f}" font-family="Georgia, \'Times New Roman\', serif">',
         f'<title>T1 Map 8 — Moathouse Dungeon ({mode.upper()}) · 1 square = 10 ft</title>',
         '<defs>',
         f'<pattern id="grid" width="{S}" height="{S}" patternUnits="userSpaceOnUse"><path d="M{S} 0H0V{S}" fill="none" stroke="{GRID}" stroke-width="1.6"/></pattern>',
         f'<clipPath id="rooms"><path d="{" ".join(path(p) for p in room_polys)}" clip-rule="evenodd"/></clipPath>',
         '<filter id="paper" x="0" y="0" width="1" height="1"><feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="4" seed="11" result="n"/><feColorMatrix in="n" type="matrix" values="0 0 0 0 0.36  0 0 0 0 0.26  0 0 0 0 0.12  0 0 0 0.22 0" result="t"/><feComposite in="t" in2="SourceGraphic" operator="in" result="tt"/><feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="tt"/></feMerge></filter>',
         '</defs>',
         f'<rect x="0" y="{-pad_top}" width="{Wd:.0f}" height="{Ht+pad_top+pad_bot:.0f}" fill="{PAPER}" filter="url(#paper)"/>',
         f'<rect x="0" y="0" width="{Wd:.0f}" height="{Ht:.0f}" fill="{ROCK}"/>']
    # floors
    o.append(f'<path d="{" ".join(path(p) for p in room_polys)}" fill="{FLOOR}" fill-rule="evenodd" stroke="{INK}" stroke-width="2.5" stroke-linejoin="miter" filter="url(#paper)"/>')
    o.append(f'<rect width="{Wd:.0f}" height="{Ht:.0f}" fill="url(#grid)" clip-path="url(#rooms)"/>')
    o.append(f'<path d="{" ".join(path(p) for p in cave_polys)}" fill="{CAVE}" fill-rule="evenodd" stroke="{INK}" stroke-width="2" stroke-linejoin="round" filter="url(#paper)"/>')
    # crypt niches (drawn, not traced: too thin for the trace)
    for (c, t, bt, side) in NICHES:
        x0, x1 = (c - 0.15 - C0) * S, (c + 0.15 - C0) * S; y0, y1 = (t - R0) * S, (bt - R0) * S
        if side == 'below':
            d = f'M{x0:.1f} {y1+1:.1f} L{x0:.1f} {y0:.1f} L{x1:.1f} {y0:.1f} L{x1:.1f} {y1+1:.1f}'
            cover = (x0 + 1.3, y1 - 3, x1 - x0 - 2.6, 6)
        else:
            d = f'M{x0:.1f} {y0-1:.1f} L{x0:.1f} {y1:.1f} L{x1:.1f} {y1:.1f} L{x1:.1f} {y0-1:.1f}'
            cover = (x0 + 1.3, y0 - 3, x1 - x0 - 2.6, 6)
        o.append(f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{x1-x0:.1f}" height="{y1-y0:.1f}" fill="{FLOOR}"/>')
        o.append(f'<rect x="{cover[0]:.1f}" y="{cover[1]:.1f}" width="{cover[2]:.1f}" height="{cover[3]:.1f}" fill="{FLOOR}"/>')
        o.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="2.5"/>')
    # pool
    cx, cy, rx, ry = pool
    pts = []
    for k in range(36):
        t = k / 36 * 2 * np.pi; rr = 1 + 0.09 * np.sin(5 * t) + 0.05 * np.cos(3 * t)
        pts.append(((cx + rx * rr * np.cos(t) - C0) * S, (cy + ry * rr * np.sin(t) - R0) * S))
    d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + ' Z'
    o.append(f'<path d="{d}" fill="{WATER}" stroke="{ROCK}" stroke-width="2.5" stroke-linejoin="round"/>')
    o.append(f'<path d="{d}" fill="none" stroke="{ROCK}" stroke-width="1.2" transform="translate({(cx-C0)*S:.1f} {(cy-R0)*S:.1f}) scale(0.82) translate({-(cx-C0)*S:.1f} {-(cy-R0)*S:.1f})"/>')
    # walls
    for (a, c) in walls:
        o.append(f'<line x1="{P(*a)[0]}" y1="{P(*a)[1]}" x2="{P(*c)[0]}" y2="{P(*c)[1]}" stroke="{ROCK}" stroke-width="5" stroke-linecap="square"/>')
    # rubble
    for (u, v) in rubble:
        x, y = P(u, v)
        o.append(f'<ellipse cx="{x}" cy="{y}" rx="7" ry="5" fill="none" stroke="{ROCK}" stroke-width="2"/>')
    # pillars
    for (u, v) in pillars:
        x, y = P(u, v); o.append(f'<circle cx="{x}" cy="{y}" r="7.5" fill="{ROCK}"/>')
    x, y = P(*pillar_secret)
    o.append(f'<circle cx="{x}" cy="{y}" r="9" fill="{FLOOR}" stroke="{ROCK}" stroke-width="3"/>')
    if gm:
        o.append(f'<text x="{x}" y="{float(y)+5:.1f}" font-size="13" font-weight="bold" text-anchor="middle" fill="{ROCK}">S</text>')
    else:
        o[-1] = f'<circle cx="{x}" cy="{y}" r="7.5" fill="{ROCK}"/>'
    # stairs
    for a, c, dd, oo in stairs: o.append(stair_svg(a, c, dd, oo))
    x, y = P(*curved_stair)
    for k in range(5):
        r = 6 + k * 8
        o.append(f'<path d="M{float(x)+S:.1f} {float(y)+S-r:.1f} A{r} {r} 0 0 0 {float(x)+S-r:.1f} {float(y)+S:.1f}" fill="none" stroke="{ROCK}" stroke-width="2"/>')
    # doors
    for (u, v, oo) in doors: o.append(door_svg(u, v, oo, 'locked' if (u, v) in locked else 'door'))
    for (u, v, oo) in false_doors: o.append(door_svg(u, v, oo, 'false' if gm else 'door'))
    if gm:
        for (u, v, oo) in secret: o.append(secret_svg(u, v, oo))
        # subterranean passage (shaft and crawlway)
        d = 'M' + ' L'.join(' '.join(P(u, v)) for u, v in passage)
        o.append(f'<path d="{d}" fill="none" stroke="{FLOOR}" stroke-width="5" stroke-dasharray="2 6" stroke-linecap="round"/>')
        # grate trap
        (a, c) = grate
        o.append(f'<line x1="{P(*a)[0]}" y1="{P(*c)[1]}" x2="{P(*c)[0]}" y2="{P(*a)[1]}" stroke="#9b2226" stroke-width="4" stroke-dasharray="10 6"/>')
        tx, ty = P(22.75, 7.35)
        o.append(f'<text x="{tx}" y="{ty}" font-size="17" font-weight="bold" fill="#9b2226" text-anchor="middle">T</text>')
        for (u, v) in guards:
            x, y = P(u, v)
            o.append(f'<text x="{x}" y="{float(y)+7:.1f}" font-size="20" font-weight="bold" text-anchor="middle" fill="#9b2226">X</text>')
        for k, (u, v) in labels.items():
            x, y = P(u, v)
            o.append(f'<text x="{x}" y="{y}" font-size="23" font-weight="bold" text-anchor="middle" fill="{INK}" '
                     f'stroke="{FLOOR}" stroke-width="5" paint-order="stroke">{str(k).strip()}</text>')
    # exit
    x, y = P(35.6, 28.75)
    o.append(f'<text x="{x}" y="{y}" font-size="21" font-weight="bold" fill="{INK}">OUT →</text>')
    if pr:
        o.append(f'<text x="24" y="-38" font-size="40" font-weight="bold" fill="{INK}" letter-spacing="2">MAP 8 · THE MOATHOUSE DUNGEON</text>')
        o.append(f'<text x="26" y="-10" font-size="19" fill="#5a4a32" font-style="italic">T1 The Village of Hommlet · Sidebar Press conversion of TSR 1985</text>')
        # legend
        lx, ly = 20, Ht + 30
        items = [('door', 'Door'), ('locked', 'Locked door'), ('secret', 'Secret door'), ('false', 'False door'),
                 ('stairs', 'Stairs'), ('pillar', 'Pillar'), ('passage', 'Hidden shaft'), ('X', 'Guard post'), ('T', 'Trap')]
        for i, (k, lab) in enumerate(items):
            X = lx + (i % 5) * 360; Y = ly + (i // 5) * 40
            if k in ('door', 'locked', 'false'):
                o.append(door_svg(X / S + C0 + 0.3, Y / S + R0 + 0.2, 'h', k))
            elif k == 'secret': o.append(secret_svg(X / S + C0 + 0.3, Y / S + R0 + 0.2, 'h'))
            elif k == 'stairs': o.append(stair_svg((X / S + 0.0, Y / S - 0.05), (X / S + 0.62, Y / S + 0.45), 'down', 'h'))
            elif k == 'pillar': o.append(f'<circle cx="{X+15}" cy="{Y+10}" r="7.5" fill="{ROCK}"/>')
            elif k == 'passage': o.append(f'<line x1="{X}" y1="{Y+10}" x2="{X+32}" y2="{Y+10}" stroke="{ROCK}" stroke-width="5" stroke-dasharray="2 5" stroke-linecap="round"/>')
            else: o.append(f'<text x="{X+15}" y="{Y+18}" font-size="20" font-weight="bold" text-anchor="middle" fill="#9b2226">{k}</text>')
            o.append(f'<text x="{X+44}" y="{Y+17}" font-size="19" fill="{INK}">{lab}</text>')
        # scale bar
        sx, sy = Wd - 560, Ht + 92
        for i in range(5):
            o.append(f'<rect x="{sx+i*S}" y="{sy}" width="{S}" height="10" fill="{FLOOR if i%2==0 else ROCK}" stroke="{INK}" stroke-width="1.5"/>')
        o.append(f'<text x="{sx}" y="{sy-8}" font-size="16" fill="{INK}">0</text><text x="{sx+5*S-20}" y="{sy-8}" font-size="16" fill="{INK}">50 ft</text>')
        o.append(f'<text x="{sx+5*S+14}" y="{sy+10}" font-size="16" fill="{INK}">1 square = 10 feet</text>')
    o.append('</svg>')
    return '\n'.join(o)

for mode in ('gm', 'player', 'print'):
    name = {'gm': 'GM', 'player': 'Player', 'print': 'Print'}[mode]
    open(f'{OUT}/T1 Map 8 - Moathouse Dungeon - {name}.svg', 'w').write(build(mode))
print(len(room_polys), 'room polys;', len(cave_polys), 'cave polys')
