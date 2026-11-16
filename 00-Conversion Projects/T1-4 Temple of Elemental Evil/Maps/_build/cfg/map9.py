# Map 9 · Nulb (PDF p. 136, top). Gridded village map, 1 square = 30 ft (settlement scale kept).
SRC = 'maps/raw/map9_clean.png'   # raw_degrid.py output (grid removed)
BOX = (0, 0, 1053, 630)
GRIDDED = False; DRAW_GRID = True
PX, OX, PY, OY = 28.59, 2.5, 28.81, 2.75
SCALE_FT = 30
TITLE = 'Map 9 · Nulb'
SUB = 'T2-4 The Temple of Elemental Evil · Sidebar Press conversion of TSR 1985'
FILE = 'T2-4 Map 9 - Nulb'
NOTE = ''
def _g(x, y): return ((x - OX) / PX, (y - OY) / PY)
_nums = {'1': (190, 152), '2': (279, 329), '3': (388, 335), '4': (452, 220)}
LABELS = {k: _g(x, y) for k, (x, y) in _nums.items()}
LABEL_SIZE = 26
_names = [('TO HOMMLET', 85, 47, 14), ('TO THE TEMPLE', 109, 592, 14), ('OF ELEMENTAL EVIL', 128, 614, 14),
          ('TO SOBANWYCH  19 LEAGUES', 770, 616, 14)]
TEXTS = [(t, x, y + 5, s) for (t, x, y, s) in _names]
TEXTS += [('IMERYDS RUN', 50, 487, 13, 'middle', 'italic', -69)]
LABEL_MASKS = [(x - 9, y - 12, x + 9, y + 12) for (x, y) in _nums.values()]
LABEL_MASKS += [(15, 33, 160, 62), (20, 578, 198, 600), (20, 600, 245, 628), (595, 600, 950, 630), (575, 4, 1035, 30)]
ERASE = [(990, 590, 1020, 628)]
GM_ONLY_MASKS = []
SPECK = 6
SPECK = 4
LINE_W = 2.6
LINES = [[(393.5, 204.5), (411, 204.5)]]
