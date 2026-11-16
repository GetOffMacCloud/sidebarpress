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
GM_ONLY_MASKS = [(498, 110, 523, 135)]   # secret door S + hidden stairway glyph (area 7)
SECRETS = [(509, 123)]
GM_MARKS = []
PROTECT = [(176, 96, 472, 412)]
STAIRS = [(304, 136, 313, 160, 'h')]
STAIRS = [(304, 136, 313, 160, 'h'), (417, 260, 434, 282, 'v')]           # 13 down to the dungeon; 8 up
POLYSTAIRS = [((330, 210), (378, 260), (353, 284), (305, 235), 11)]          # 5 littered steps up to the hall
LINES = [
    [(428, 133), (455, 133), (455, 158), (502, 158)],                       # 7 Black Chamber, south and west walls
    [(378, 260), (392, 260), (392, 335)],                                    # 9/10 north and east walls
    [(355, 284), (355, 386)],                                                # 9/10 and 12 west wall
    [(355, 310), (392, 310)], [(355, 335), (392, 335)],                       # 9|10, 10|12
    [(417, 282), (417, 335)], [(417, 282), (458, 282)], [(417, 335), (458, 335)],   # 11
]
DOORS = [(441, 133, 'h', 'rect'),                                            # 7 heavy door (barred)
         (392, 298, 'v', 'rect'), (392, 322, 'v', 'rect'), (417, 322, 'v', 'rect'),
         (355, 297, 'v', 'tick'), (355, 322, 'v', 'tick'), (355, 347, 'v', 'tick'), (355, 373, 'v', 'tick')]
# --- cleanup pass (2026-11-16): parapets redrawn, rooms 13-17 drawn explicitly ---
PARAPETS = [(180, 135, 189, 362),      # west wall
            (197, 111, 404, 121),      # north wall
            (407, 58, 524, 67),        # NE tower (7) north
            (516, 67, 526, 150),       # NE tower (7) east
            (469, 175, 479, 385),      # east wall
            (293, 396, 447, 405)]      # south wall
LINES += [
    [(254, 136), (254, 235)],                          # 16|17 and 15|17
    [(254, 172), (330, 172)],                          # 16 south / 13 south
    [(303, 136), (303, 172)], [(330, 148), (330, 172)],  # 13 west and east
    [(254, 198), (330, 198), (330, 212)],              # 15/14 north, down to the stair head
    [(279, 198), (279, 235)],                          # 15|14
    [(200, 235), (305, 235)],                          # 17/15/14 south
]
DOORS += [(254, 182, 'v', 'rect'), (266, 172, 'h', 'rect'), (266, 198, 'h', 'rect'), (292, 198, 'h', 'rect'),
          (242, 235, 'h', 'tick'), (268, 235, 'h', 'tick'), (292, 235, 'h', 'tick')]
ERASE = [(328, 512, 340, 542)]
FILLS = [(502, 106, 517, 138)]   # east wall of area 7 behind the secret door
DRAW_GM_INK = False   # the S is re-set by SECRETS; the traced glyph is only masked out
GRID_DIV = 2          # 5-ft squares (interior)
