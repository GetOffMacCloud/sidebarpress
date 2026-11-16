SRC = 'maps/raw/p135-000.jpg'
BOX = (28, 120, 690, 662)
PX, OX, PY, OY = 24.8, 8.0, 24.9, 9.75
TITLE = 'Map 7 · Ruins of the Moathouse'
SUB = 'T1 The Village of Hommlet · Sidebar Press conversion of TSR 1985'
FILE = 'T1 Map 7 - Moathouse Ruins'
SCALE_FT = 10
NOTE = 'Crumbled wall and rubble are difficult terrain'
_box = {'16': (278, 152), '13': (322, 152), '17': (241, 222), '15': (266, 223), '14': (291, 223), '7': (465, 122),
        '6': (416, 197), '5': (317, 273), '8': (409, 273), '9': (372, 296), '10': (371, 322), '11': (440, 322),
        '12': (393, 373), '3': (241, 344), '2': (253, 418), '4': (199, 379)}
def _g(p): return ((p[0] - OX) / PX, (p[1] - OY) / PY)
LABELS = {k: _g(v) for k, v in _box.items()}
LABEL_MASKS = []
for k, (x, y) in _box.items():
    w = 4 * len(k) + 3
    LABEL_MASKS.append((x - w, y - 8, x + w, y + 8))
GM_ONLY_MASKS = [(499, 114, 508, 132)]
GM_MARKS = []
PROTECT = [(176, 96, 472, 412)]
STAIRS = [(304, 136, 313, 160, 'h')]
