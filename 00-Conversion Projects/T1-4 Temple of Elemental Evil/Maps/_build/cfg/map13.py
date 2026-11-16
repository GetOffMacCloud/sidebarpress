# Map 13 · Dungeon Level 2 (PDF p. 139). Grey-rock dungeon: rock/floor separated by tone and the printed grid
# removed in scripts/dungeon_prep.py (maps/dgcfg/m13.py); this config renders the cleaned image.
import json as _j
_m = _j.load(open('maps/dg/m13_labels.json'))
SRC = 'maps/dg/m13_final.png'
_W, _H = _m['box'][2] - _m['box'][0], _m['box'][3] - _m['box'][1]
BOX = (0, 0, _W, _H)
PX, OX, PY, OY = _m['lattice']
GRIDDED = False; DRAW_GRID = True
SCALE_FT = 10
TITLE = 'Map 13 · Dungeon Level 2'
SUB = 'T2-4 The Temple of Elemental Evil · Sidebar Press conversion of TSR 1985'
FILE = 'T2-4 Map 13 - Dungeon Level 2'
NOTE = ''
SPECK = 3
THRESH = 128
LABEL_LIST = [(t, x, y, h, r) for t, x, y, h, r, bb in _m['labels']]
SECRETS = [(x, y) for x, y, w in _m['secrets']]
LINES = [w for x, y, w in _m['secrets'] if w]
LW = 3.0
SECRET_SIZE = 28
DOORS = [tuple(d) for d in _m["doors"]]

ELLIPSES = [(247, 1168, 17, 25, 2.2)]
WAVES = [(274, 291, 247, 1.6, 7.5, 1.6), (236, 254, 1152, 1.3, 7.5, 1.5), (244, 262, 1161, 1.3, 7.5, 1.5), (234, 254, 1170, 1.3, 7.5, 1.5), (238, 256, 1180, 1.3, 7.5, 1.5),
         (242, 258, 1189, 1.3, 7.5, 1.5),
         (325, 347, 399, 1.3, 7.5, 1.5), (343, 371, 404, 1.3, 7.5, 1.5), (318, 344, 413, 1.3, 7.5, 1.5), (356, 378, 414, 1.3, 7.5, 1.5),
         (330, 352, 424, 1.3, 7.5, 1.5), (360, 380, 428, 1.3, 7.5, 1.5),
         (229, 271, 1044, 3.2, 9.5, 2.0)]
STARS = [(247, 1031, 6)]
CHAINARCS = [((300, 393), (345, 362), (390, 393), 6.5)]
TEXTS = [('C', 298, 252, 15, 'middle', 'normal'), ('C', 198, 922, 15, 'middle', 'normal'), ('C', 287, 1120, 15, 'middle', 'normal')]
LINES += [[(205, 917), (213, 917)]]
ELLIPSES += [(532.5, 801.5, 30, 30, 2.0)]
DOTS = [(762.4, 1013.4), (878.2, 1014.2), (777.4, 1039.1), (863.2, 1041.0), (791.0, 1062.0), (850.3, 1062.7), (800.9, 1089.7), (838.1, 1090.6), (851.8, 1111.6), (785.7, 1113.5), (774.5, 1140.7), (864.9, 1139.9), (762.3, 1167.0), (879.1, 1166.7)]
TREADS = _m.get('treads', [])
GRID_DIV = 2          # 5-ft squares
LABEL_LIST = [(t, (x - 3 if t == '209a' else x), y, (h - 2 if t == '209a' else h), r) for (t, x, y, h, r) in LABEL_LIST]
