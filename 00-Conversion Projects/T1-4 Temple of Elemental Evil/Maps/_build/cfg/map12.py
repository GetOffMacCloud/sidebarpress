# Map 12 · Dungeon Level 1 (PDF p. 138). Grey-rock dungeon: rock/floor separated by tone and the printed grid
# removed in scripts/dungeon_prep.py (maps/dgcfg/m12.py); this config renders the cleaned image.
import json as _j
_m = _j.load(open('maps/dg/m12_labels.json'))
SRC = 'maps/dg/m12_final.png'
_W, _H = _m['box'][2] - _m['box'][0], _m['box'][3] - _m['box'][1]
BOX = (0, 0, _W, _H)
PX, OX, PY, OY = _m['lattice']
GRIDDED = False; DRAW_GRID = True
SCALE_FT = 10
TITLE = 'Map 12 · Dungeon Level 1'
SUB = 'T2-4 The Temple of Elemental Evil · Sidebar Press conversion of TSR 1985'
FILE = 'T2-4 Map 12 - Dungeon Level 1'
NOTE = ''
SPECK = 3
THRESH = 128
LABEL_LIST = [(t, x, y, h, r) for t, x, y, h, r, bb in _m['labels']]
SECRETS = [(x, y) for x, y, w in _m['secrets']]
LINES = [w for x, y, w in _m['secrets'] if w]
LW = 3.0
SECRET_SIZE = 34
POLYSTAIRS = [((494, 391), (547, 391), (547, 463), (494, 463), 11),
              ((496, 578), (551, 578), (529, 668), (516, 668), 12)]
ARROWS = [(521, 1200, 521, 1112), (270, 1203, 486, 1203), (782, 1203, 565, 1203)]
XMARKS = [(910, 1012), (926, 1029), (910, 1045)]
DASHLINES = [[(898, 1016), (898, 1042)], [(212, 157), (253, 157), (253, 179), (212, 179), (212, 157)]]
LINES += [[(765, 307), (852, 392)]]
_u = (0.699, -0.715)
for _t in (0.36, 0.64):
    _p = (765 + 87 * _t, 307 + 85 * _t); LINES.append([_p, (_p[0] + 11 * _u[0], _p[1] + 11 * _u[1])])
RUBBLE = [[(403, 790), (695, 790), (695, 830), (403, 830)]]     # 125 rubble-choked corridor
DASHCIRCLES = [(912, 631, 9)]
TEXTS = [('F', 912, 632, 11, 'middle', 'bold')]
DOORS = [tuple(d) for d in _m['doors']]
DOOR_SIZE = (6.5, 16)
TRIS = [(380, 112, 'r', 17), (411, 113, 'r', 17), (440, 116, 'd', 17), (377, 146, 'u', 17), (378, 179, 'u', 17), (611, 116, 'd', 17), (637, 112, 'l', 17), (665, 111, 'l', 17), (661, 145, 'u', 17), (661, 178, 'u', 17)]
