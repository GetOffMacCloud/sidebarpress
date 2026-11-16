# Map 10 · Tower Ruins (PDF p. 136, bottom). Plan of the broken tower (area A on Map 11); the floor grid is
# printed only inside the tower, 1 square = 5 ft. Grid removed inside the floor by maps/cfg/map10_prep.py.
import numpy as _np
SRC = 'maps/raw/map10_clean.png'
BOX = (0, 0, 730, 555)
PX, OX, PY, OY = 25.07, 15.25, 25.235, 21.765
GRIDDED = False; DRAW_GRID = True
SCALE_FT = 5
TITLE = 'Map 10 · Tower Ruins'
SUB = 'T2-4 The Temple of Elemental Evil · Sidebar Press conversion of TSR 1985'
FILE = 'T2-4 Map 10 - Tower Ruins'
NOTE = 'Dotted lines: secret escape tunnel (GM)'
CX, CY = 448.8, 294.6
GRID_CLIP = (CX, CY, 161)
_lab = {'1': (425, 355), '2': (480, 240), '3': (568, 240), '4': (651, 97)}
LABEL_LIST = [(k, x, y, 16, 0) for k, (x, y) in _lab.items()]
LABEL_MASKS = [(x - 9, y - 12, x + 9, y + 12) for (x, y) in _lab.values()]
ERASE = [(0, 0, 220, 62)]                                   # printed title
GM_ONLY_MASKS = [(514, 148, 546, 180)]                      # S and the dotted trapdoor square
SPECK = 3
def _at(b, r, off):
    # point on line y = b - x (shifted perpendicular by off) at radius r from the tower centre
    best = None
    for x in _np.arange(520, 740, 0.25):
        y = b - x
        rr = _np.hypot(x - CX, y - CY)
        if best is None or abs(rr - r) < best[0]: best = (abs(rr - r), x, y)
    _, x, y = best
    return (x + off / _np.sqrt(2), y + off / _np.sqrt(2))
PLAYER_FLOORPOLYS = []
for _b in (680.4, 708.1):
    p0, p1 = _at(_b, 218, -5), _at(_b, 218, 5)
    t0 = (p0[0] + 140, p0[1] - 140); t1 = (p1[0] + 140, p1[1] - 140)
    PLAYER_FLOORPOLYS.append([p0, p1, t1, t0])
PLAYER_FILLPOLYS = [[_at(680.4, 160, -6), _at(680.4, 217, -6), _at(708.1, 217, 6), _at(708.1, 160, 6)]]
