# Map 6 · Guard Tower (PDF p. 134). Composite: the tower's six levels (right column) above the cellar (bottom left).
# Composite coords: tower page (x, y) -> (x - 480, y - 120); cellar page (x, y) -> (x - 70, y + 225).
SRC = 'maps/raw/map6_composite.png'
BOX = (0, 0, 560, 1487)
PX, OX, PY, OY = 25.0, 0.0, 25.0, 0.0
GRIDDED = False; DRAW_GRID = False; SCALE_BAR = False
SCALE_FT = 10
SCALE_TEXT = '1 square = 10 feet'
TITLE = 'Map 6 · Guard Tower'
SUB = 'T1 The Village of Hommlet · Sidebar Press conversion of TSR 1985'
FILE = 'T1 Map 6 - Guard Tower'
NOTE = 'A = light catapults (parapet)'
SPECK = 3; LABEL_SIZE = 40
def _t(x, y): return (x - 480, y - 120)
def _c(x, y): return (x - 70, y + 225)
_n = {'10': _t(681, 350), '9': _t(670, 495), '8': _t(668, 523), '7': _t(636, 508), '6': _t(681, 723), '4': _t(643, 752),
      '5': _t(685, 753), '1': _t(681, 968), '2': _t(675, 1182), '3': _c(246, 1160), 'A': _t(758, 495), 'A ': _t(749, 559)}
LABELS = {k: (x / PX, y / PY) for k, (x, y) in _n.items()}
LABEL_MASKS = [(x - 8 * len(k.strip()) - 3, y - 16, x + 8 * len(k.strip()) + 3, y + 14) for k, (x, y) in _n.items() ]
_cap = {'TURRET ROOF': (_t(865, 194), _t(1015, 214)), 'TURRET': (_t(863, 341), _t(945, 361)), 'PARAPET LEVEL': (_t(863, 502), _t(1031, 521)),
        'UPPER HALL': (_t(863, 741), _t(992, 761)), 'MAIN HALL': (_t(868, 991), _t(979, 1011)), 'LOWER LEVEL': (_t(870, 1159), _t(1017, 1182)),
        'CELLAR': (_c(371, 1132), _c(450, 1149))}
LABEL_MASKS += [(a[0] - 6, a[1] - 18, b[0] + 8, b[1] + 8) for (a, b) in _cap.values()]
ERASE_CAPS = True
TEXTS = [(t, a[0], b[1] - 2, 18, 'start') for t, (a, b) in _cap.items()]
GM_ONLY_MASKS = []
GLYPH_MASKS = 'hybrid'
ERASE = [(*_t(743, 549), *_t(756, 569)), (*_t(631, 500), *_t(641, 515))]   # lower 'A' and the '7' (glyphs touching art)
ERASE = ERASE + [(a[0] - 6, a[1] - 18, b[0] + 8, b[1] + 8) for (a, b) in _cap.values()]
