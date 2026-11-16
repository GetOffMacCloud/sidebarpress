# Map 11 · The Temple (PDF p. 137). Temple grounds, 1 square = 30 ft (site scale kept, like Nulb).
# maps/cfg/map11_prep.py deskews the scan and removes the printed grid.
SRC = 'maps/raw/map11_clean.png'
BOX = (0, 0, 1035, 1245)
PX, OX, PY, OY = 28.54, 9.0, 28.82, 14.25
GRIDDED = False; DRAW_GRID = True
SCALE_FT = 30
TITLE = 'Map 11 · The Temple'
SUB = 'T2-4 The Temple of Elemental Evil · Sidebar Press conversion of TSR 1985'
FILE = 'T2-4 Map 11 - The Temple'
NOTE = 'A: Broken Tower (Map 10) · B: Building Ruins · C: Temple'
_lab = {'10': (487, 446), '9': (567.5, 462.5), '8': (489.5, 492.0), '7': (504.5, 579.5), '6': (430, 588), '5': (391.5, 667.5), '3': (504.0, 667.0), '4': (595.5, 663.0), '4a': (625, 702), '2': (499.5, 811.5), '1': (500.5, 863.0), 'C': (593.0, 865.0), '5a': (345.0, 699.0), 'A': (878.0, 84.5), 'B': (249.0, 258.0)}
LABEL_LIST = [(k, x, y, 15, 0) for k, (x, y) in _lab.items()]
LABEL_MASKS = [(int(x - 6 * len(k) - 4), int(y - 14), int(x + 6 * len(k) + 4), int(y + 15)) for k, (x, y) in _lab.items()]
GLYPH_MASKS = 'hybrid'
ERASE = [(0, 0, 16, 1245), (620, 1192, 1035, 1245), (930, 1120, 1005, 1215)]       # printed scale line and north arrow
GM_ONLY_MASKS = []
SPECK = 3
