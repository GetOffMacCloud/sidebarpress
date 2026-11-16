# Map 17 · Earth Elemental Node (PDF p. 143). Grey-rock dungeon: rock/floor separated by tone and the printed grid
# removed in scripts/dungeon_prep.py (maps/dgcfg/m17.py); this config renders the cleaned image.
import json as _j
_m = _j.load(open('maps/dg/m17_labels.json'))
SRC = 'maps/dg/m17_final.png'
_W, _H = _m['box'][2] - _m['box'][0], _m['box'][3] - _m['box'][1]
BOX = (0, 0, _W, _H)
PX, OX, PY, OY = _m['lattice']
GRIDDED = False; DRAW_GRID = True
TITLE = 'Map 17 · Earth Elemental Node'
SUB = 'T2-4 The Temple of Elemental Evil · Sidebar Press conversion of TSR 1985'
FILE = 'T2-4 Map 17 - Earth Elemental Node'
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
SCALE_FT = 10
GRID_DIV = 2          # 5-ft squares

TREADS_V = _m.get('treads_v', [])

TREADS_V = _m.get('treads_v', [])

SPECK = 1
