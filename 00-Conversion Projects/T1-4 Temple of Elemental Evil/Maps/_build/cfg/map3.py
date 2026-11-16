# Map 3 · Inn of the Welcome Wench (PDF p. 133, left). Oblique illustrations of three floors; the floor grid is
# drawn into the art (1 square = 10 ft), so it is kept on the GM/Player/Print versions and stripped for No Grid.
SRC = 'maps/raw/pg-003.jpg'
BOX = (12, 70, 690, 1312)
PX, OX, PY, OY = 25.0, 0.0, 25.0, 0.0
GRIDDED = False; DRAW_GRID = False; SCALE_BAR = False
SCALE_FT = 10
SCALE_TEXT = '1 square = 10 feet (oblique view)'
TITLE = 'Map 3 · Inn of the Welcome Wench'
SUB = 'T1 The Village of Hommlet · Sidebar Press conversion of TSR 1985'
FILE = 'T1 Map 3 - Inn of the Welcome Wench'
NOTE = ''
SPECK = 3
LABEL_SIZE = 40
_n = {'20': (91, 242), '19': (82, 315), '18': (137, 310), '7': (260, 276), '9': (306, 274), '11': (388, 273), '13': (434, 272),
      '15': (553, 275), '17': (190, 422), '16': (253, 420), '14': (312, 417), '12': (355, 417), '10': (413, 395), '8': (465, 419),
      '6': (571, 418), '5': (161, 677), '4': (234, 674), '1': (413, 678), '3': (534, 667), '2': (565, 783),
      '22': (90, 1100), '23': (213, 1121), '27': (420, 1095), '21': (130, 1162), '24': (210, 1201), '25': (355, 1197),
      '26': (495, 1197), '28': (600, 1237)}
def _b(x, y): return (x - BOX[0], y - BOX[1])
LABELS = {k: ((x - BOX[0]) / PX, (y - BOX[1]) / PY) for k, (x, y) in _n.items()}
LABEL_MASKS = [(x - BOX[0] - 7 * len(k) - 2, y - BOX[1] - 14, x - BOX[0] + 7 * len(k) + 2, y - BOX[1] + 14) for k, (x, y) in _n.items()]
# captions (masked, re-set) and the page furniture
LABEL_MASKS += [(484 - BOX[0], 462 - BOX[1], 632 - BOX[0], 485 - BOX[1]), (498 - BOX[0], 890 - BOX[1], 638 - BOX[0], 914 - BOX[1]),
                (553 - BOX[0], 1300 - BOX[1], 637 - BOX[0], BOX[3] - BOX[1]), (40 - BOX[0] + 12, 0, 720 - BOX[0], 62 - BOX[1] + 12)]
TEXTS = [('UPPER FLOOR', *_b(557, 480), 17), ('FIRST FLOOR', *_b(568, 909), 17), ('CELLAR', *_b(595, 1309), 17)]
# secret doors: first-floor stair panel (S) and two in the cellar; shown only to the GM
_sec = [(605, 712), (543, 1205), (554, 1098)]
GM_ONLY_MASKS = [(x - BOX[0] - 9, y - BOX[1] - 8, x - BOX[0] + 9, y - BOX[1] + 8) for (x, y) in _sec]
SECRETS = [((x - BOX[0]), (y - BOX[1])) for (x, y) in _sec]
DRAW_GM_INK = False
# floor tiles are drawn into the 1985 oblique art; stripping them damaged furniture, so No Grid keeps them
FILLPOLYS = [[(516, 1114), (524, 1114), (537, 1150), (529, 1150)]]   # cellar wall behind the 26/28 secret door
SECRET_SIZE = 36
GLYPH_MASKS = 'hybrid'
