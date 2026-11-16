# Map 5 · Church of St. Cuthbert (PDF p. 134, left column). Three floors; floor lines are drawn into the art.
SRC = 'maps/raw/pg-004.jpg'
BOX = (12, 95, 480, 835)
PX, OX, PY, OY = 25.0, 0.0, 25.0, 0.0
GRIDDED = False; DRAW_GRID = False; SCALE_BAR = False
SCALE_FT = 10
SCALE_TEXT = '1 square = 10 feet'
TITLE = 'Map 5 · Church of St. Cuthbert'
SUB = 'T1 The Village of Hommlet · Sidebar Press conversion of TSR 1985'
FILE = 'T1 Map 5 - Church of St Cuthbert'
NOTE = ''
SPECK = 3; LABEL_SIZE = 40
_n = {'11': (121, 137), '13': (59, 199), '12': (159, 197), '15': (206, 193), '14': (137, 292), '5': (124, 409), '3': (101, 467),
      '2': (204, 468), '1': (254, 465), '4': (134, 511), '8': (123, 662), '9': (201, 695), '10': (243, 696), '7': (94, 722), '6': (141, 793)}
LABELS = {k: ((x - BOX[0]) / PX, (y - BOX[1]) / PY) for k, (x, y) in _n.items()}
LABEL_MASKS = [(x - BOX[0] - 7 * len(k) - 2, y - BOX[1] - 12, x - BOX[0] + 7 * len(k) + 2, y - BOX[1] + 12) for k, (x, y) in _n.items()]
def _b(x, y): return (x - BOX[0], y - BOX[1])
_caps = [(*_b(312, 193), *_b(470, 217)), (*_b(312, 436), *_b(470, 462)), (*_b(313, 693), *_b(476, 723))]
ERASE = list(_caps)   # captions sit just right of the walls (walls end at x 311)
TEXTS = [('UPPER FLOOR', *_b(386, 212), 18), ('MAIN FLOOR', *_b(380, 456), 18), ('LOWER FLOOR', *_b(392, 715), 18)]
GM_ONLY_MASKS = []
GLYPH_MASKS = 'hybrid'
