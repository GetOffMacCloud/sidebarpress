# Map 1 · From Hommlet to Nulb (PDF p. 130). Region map: hex art, no square grid, no GM secrets.
SRC = 'maps/raw/pg-000.jpg'
BOX = (28, 170, 1062, 1338)
PX, OX, PY, OY = 25.0, 0.0, 25.0, 0.0           # nominal (scale only)
GRIDDED = False; DRAW_GRID = False; SCALE_BAR = False
SPECK = 2
TITLE = 'Map 1 · From Hommlet to Nulb'
SUB = 'T1 The Village of Hommlet · Sidebar Press conversion of TSR 1985'
FILE = 'T1 Map 1 - Hommlet to Nulb'
SCALE_FT = 0
SCALE_TEXT = '1 hex = 10 leagues (30 miles) · Hommlet to Nulb ≈ 33 miles · Hommlet to the Moathouse ≈ 15 miles'
NOTE = 'Inset: the Verbobonc region'
# region map: no square grid and no secrets, so GM, Player and Player (No Grid) are the same image
LABELS = {}
_lab = {  # page-px boxes of the printed lettering (masked, then re-set below)
 'title': (75, 528, 627, 557), 'scale': (70, 565, 330, 582), 'verb': (36, 639, 188, 658), 'kron': (284, 713, 484, 744),
 'high': (725, 838, 868, 864), 'evil': (752, 988, 895, 1005), 'gnarley': (732, 1028, 1038, 1060), 'low': (410, 1046, 546, 1072),
 'beware': (555, 1110, 666, 1126), 'danger': (653, 1248, 718, 1264), 'hommlet': (55, 1293, 204, 1320),
 'unused': (381, 1304, 546, 1320), 'sobanwych': (926, 546, 1057, 584), 'nulb': (870, 625, 947, 652),
 'inulb': (598, 350, 686, 377), 'ihommlet': (381, 443, 507, 472)}
LABEL_MASKS = [(a - BOX[0], b - BOX[1], c - BOX[0], d - BOX[1]) for (a, b, c, d) in _lab.values()]
def _b(x, y): return (x - BOX[0], y - BOX[1])
TEXTS = [
 ('TO VERBOBONC', *_b(40, 656), 15, 'start'), ('KRON HILLS', *_b(384, 742), 28), ('HIGH ROAD', *_b(796, 862), 20),
 ('EVIL LURKS HERE', *_b(824, 1003), 12), ('GNARLEY FOREST', *_b(885, 1058), 28), ('LOW ROAD', *_b(478, 1070), 20),
 ('BEWARE EVIL', *_b(610, 1124), 12), ('DANGER', *_b(686, 1262), 12), ('HOMMLET', *_b(57, 1318), 22, 'start'),
 ('UNUSED TRACE ROAD', *_b(463, 1318), 12), ('TO', *_b(942, 562), 12), ('SOBANWYCH', *_b(928, 582), 13, 'start'),
 ('NULB', *_b(872, 650), 22, 'start'), ('NULB', *_b(601, 375), 20, 'start'), ('HOMMLET', *_b(384, 470), 20, 'start'),
]
GM_ONLY_MASKS = []
