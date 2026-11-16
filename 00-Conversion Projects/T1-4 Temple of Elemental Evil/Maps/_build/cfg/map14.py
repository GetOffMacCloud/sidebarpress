# Map 14 · Dungeon Level 3 (PDF p. 140). Grey-rock dungeon: rock/floor separated by tone and the printed grid
# removed in scripts/dungeon_prep.py (maps/dgcfg/m14.py); this config renders the cleaned image.
import json as _j
_m = _j.load(open('maps/dg/m14_labels.json'))
SRC = 'maps/dg/m14_final.png'
_W, _H = _m['box'][2] - _m['box'][0], _m['box'][3] - _m['box'][1]
BOX = (0, 0, _W, _H)
PX, OX, PY, OY = _m['lattice']
GRIDDED = False; DRAW_GRID = True
SCALE_FT = 10
TITLE = 'Map 14 · Dungeon Level 3'
SUB = 'T2-4 The Temple of Elemental Evil · Sidebar Press conversion of TSR 1985'
FILE = 'T2-4 Map 14 - Dungeon Level 3'
NOTE = ''
SPECK = 3
THRESH = 128
LABEL_LIST = [(t, x, y, h, r) for t, x, y, h, r, bb in _m['labels']]
SECRETS = [(x, y) for x, y, w in _m['secrets']]
LINES = [w for x, y, w in _m['secrets'] if w]
LW = 3.0
SECRET_SIZE = 28
DOORS = [tuple(d) for d in _m["doors"]]

TREADS = _m.get("treads", [])
GRID_DIV = 2          # 5-ft squares

TREADS_V = _m.get('treads_v', [])
ELLIPSES = [(175.5, 202.5, 35.4, 35.4, 2.2)]
ARCS = [(79, 203, 44, 45, -90, 90, 2.6), (79, 203, 36, 38, -90, 90, 2.4), (79, 203, 28, 31, -90, 90, 2.4)]
WAVES_V = [(176, 232, 80, 2.2, 9, 1.8)]
LINES += [[(79, 150), (79, 175)], [(79, 232), (79, 258)]]
RECTS = [(495.5, 72.5, 575, 157.5, 2.2), (501.5, 80.5, 568.5, 150.5, 2.2), (507, 86.5, 563.5, 143.5, 2.2)]
PATHS = [('M120 838.5 L136 838.5', 2.6), ('M136 895 L136 913', 2.6), ('M79 60 L79 114', 2.6), ('M79 284 L79 322', 2.6), ('M151 598 L135 631', 2.2), ('M841 836 L841 826 Q842 820 848 820 L870 820 Q875 822 878 834', 2.0), ('M845.5 836 L845.5 829 Q846 826.5 849 826.5 L866 826.5 Q869 827 871 834', 1.8), ('M239 796 L261 836', 2.2), ('M323 836 L340 804', 2.2), ('M448.6 899 L505.5 865.5 L562 893.6', 2.2), ('M450 966 L505.5 1000.5 L563.6 968.6', 2.2), ('M336.7 1005.8 L336.7 983 L340 980 L390 980 L393.3 983 L393.3 1005.8', 2.0), ('M341.7 1005.8 L341.7 986.5 L343.5 985 L387.5 985 L389.2 986.5 L389.2 1005.8', 2.0), ('M489.5 61 L489.5 164.5 L583 164.5 L583 61', 2.2)]
ELLIPSES += [(535, 115, 7.5, 9, 2.0)]
LINES += [[(535, 106), (535, 124)]]
TREADS = TREADS + [[round(305 + 6.4 * k, 1), 507, 566, 2.4] for k in range(16)] + [[None, 536, 0, 0]][:0]
TRIS = [(864, 159, 'u', 22)]
ELLIPSES += [(866, 331, 14.5, 13.5, 2.2)]
RECTS += [(909, 233, 926, 255, 2.6)]
POLYS = [([(811, 235), (831, 235), (831, 255), (811, 255)], 2.0), ([(821, 231), (835, 245), (821, 259), (807, 245)], 2.4)]
ELLIPSES += [(373.3, 1010.8, 9, 8.3, 2.0)]
LABEL_LIST = [(t, (x - 7 if (t == 'c' and abs(x - 813.5) < 1) else x), y, h, r) for (t, x, y, h, r) in LABEL_LIST]
