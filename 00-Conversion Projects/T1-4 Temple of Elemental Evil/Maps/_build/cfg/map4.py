# Map 4 · Traders' Establishment (PDF p. 133, right of Map 3). Plan view, 1 square = 10 ft.
SRC = 'maps/raw/pg-003.jpg'
BOX = (735, 225, 1095, 745)
PX, OX, PY, OY = 44.0, 35.0, 44.5, 39.5
SCALE_FT = 10
TITLE = "Map 4 · The Traders' Establishment"
SUB = 'T1 The Village of Hommlet · Sidebar Press conversion of TSR 1985'
FILE = "T1 Map 4 - Traders' Establishment"
NOTE = ''
THICK_GUARD = True; PERP_TEST = True; AGGRESSIVE = True
LABEL_SIZE = 30
_n = {'12': (832, 386), '13': (961, 338), '11': (1048, 567), '10': (836, 623), '9': (895, 615), '8': (980, 616),
      '7': (980, 647), '6': (1060, 632), '2': (893, 688), '1': (834, 703), '3': (932, 720), '4': (1002, 699), '5': (1057, 705)}
def _g(x, y): return ((x - BOX[0] - OX) / PX, (y - BOX[1] - OY) / PY)
LABELS = {k: _g(x, y) for k, (x, y) in _n.items()}
LABEL_MASKS = [(x - BOX[0] - 6 * len(k) - 3, y - BOX[1] - 13, x - BOX[0] + 6 * len(k) + 3, y - BOX[1] + 13) for k, (x, y) in _n.items()]
GM_ONLY_MASKS = []
ERASE = [(167, 22, 173, 40), (211, 22, 217, 40), (255, 22, 261, 40)]   # grid stubs under the barnyard fence
GLYPH_MASKS = False
GRID_DIV = 2          # 5-ft squares (interior)
