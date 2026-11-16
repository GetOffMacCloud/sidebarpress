# Map 2 · The Village of Hommlet (PDF pp. 131-132, stitched on the shared grid line: p131 col 1081 = p132 col 33, p132 +1 px).
SRC = 'maps/raw/map2_stitched.png'
BOX = (402, 20, 2118, 1346)
PX, OX, PY, OY = 23.45, 0.75, 23.56, 1.25
SCALE_FT = 20
TITLE = 'Map 2 · The Village of Hommlet'
SUB = 'T1 The Village of Hommlet · Sidebar Press conversion of TSR 1985'
FILE = 'T1 Map 2 - Village of Hommlet'
NOTE = 'Grey bands are roads; the stream flows west to east'
TINT_MASK = 'maps/raw/map2_tint.png'; TINT_THRESH = 62; TINT_COLOR = '#cbb68a'
def _g(x, y): return ((x - OX) / PX, (y - OY) / PY)
_nums = {'1': (387, 1125), '2': (201, 1125), '3': (153, 959), '4': (458, 1077), '5': (345, 890), '6': (439, 889),
         '7': (412, 725), '8': (581, 766), '9': (500, 649), '10': (553, 621), '11': (482, 557), '12': (530, 506),
         '13': (485, 325), '14': (549, 204), '15': (363, 418), '16': (175, 440), '17': (267, 465), '18': (129, 584),
         '19': (150, 299), '20': (223, 204), '21': (690, 274), '22': (830, 412), '23': (854, 296), '24': (581, 884),
         '25': (651, 865), '26': (670, 747), '27': (760, 698), '28': (855, 792), '29': (1090, 696), '30': (1044, 792),
         '31': (1205, 864), '32': (1395, 696), '33': (1604, 788)}
LABELS = {k: _g(x, y - 6) for k, (x, y) in _nums.items()}
# place names (shown on every version): text, center x, center y
_names = [('CHURCH', 270, 133), ('HERDSMAN', 122, 322), ('TRADER', 369, 321), ('FIELDS', 575, 131), ('TEAMSTER', 636, 202),
  ('CHEESE', 722, 239), ('FARMER', 750, 311), ('FARMER', 902, 259), ('MILLER', 791, 376), ('BARN', 612, 438),
  ('CABINET MAKER', 96, 438), ('& LIMNER', 92, 464), ('POTTER', 265, 487), ('JEWELS', 382, 458), ('& MONEY', 370, 476),
  ('CHANGER', 358, 495), ('PASTURE', 65, 511), ('BREWER', 183, 536), ('TAILOR', 445, 532), ('FARMER', 604, 511),
  ('PASTURE', 716, 485), ('FARMER', 805, 531), ('WEAVER', 596, 579), ('VILLAGE', 756, 581), ('ELDER', 749, 602),
  ('VILLAGE HALL', 472, 675), ('INN', 435, 746), ('OF THE', 422, 769), ('WELCOME', 418, 792), ('WENCH', 402, 816),
  ('BLACKSMITH', 580, 746), ('CARPENTER', 891, 744), ('STONEMASON', 1078, 719), ('WHEEL &', 760, 793),
  ('WAINWRIGHT', 771, 815), ('HERDSMAN', 677, 817), ('BARN', 678, 862), ('LEATHER', 490, 910), ('WORKER', 492, 933),
  ('WOODCUTTER', 186, 936), ('FARMER', 366, 959), ('DRUID', 661, 980), ('BARN', 303, 1006), ('BARN', 490, 1006),
  ('FIELDS', 221, 1030), ('FARMER', 155, 1077), ('FARMER', 295, 1076), ('FARMER', 580, 1076), ('FIELDS', 604, 1194),
  ('TO NYR DYV', 1312, 743), ('& THE TEMPLE', 1316, 768)]
TEXTS = [(t, x, y + 4.5, 11.5) for (t, x, y) in _names]
TEXTS += [('THE VILLAGE', 998, 532, 30, 'middle', 'normal'), ('OF HOMMLET', 998, 565, 30, 'middle', 'normal')]
def _wbox(t, x, y, cw, h): w = len(t) * cw / 2 + 4; return (int(x - w), int(y - h), int(x + w), int(y + h))
LABEL_MASKS = [_wbox(k, x, y, 10.5, 10) for k, (x, y) in _nums.items()]
LABEL_MASKS += [_wbox(t, x, y, 8.8, 8) for (t, x, y) in _names]
LABEL_MASKS += [(880, 505, 1115, 580)]                       # printed title
ERASE = [(1265, 1180, 1465, 1252)]                           # printed scale bar (re-set in the frame)
GM_ONLY_MASKS = []
SPECK = 6
AUTO_PROTECT = 0
AUTO_PROTECT_DIL = 3
FP_IN = 2
FP_OUT = 2
# building footprints (box px): raw ink kept inside. Rects (x0,y0,x1,y1) or polygons.
FOOTPRINTS = [
 (232, 162, 307, 240),                                                   # 20 church
 (160, 259, 208, 290),                                                   # 19 herdsman
 [(380, 357), (447, 262), (490, 307), (424, 404)],                       # 13 trader
 [(193, 435), (227, 401), (252, 426), (217, 460)],                       # 16 cabinet maker
 [(297, 457), (327, 401), (369, 440), (326, 486)],                       # 15 jewels & money changer
 (232, 496, 271, 525), (286, 501, 307, 523),                              # 17 potter + kiln
 (138, 545, 212, 663), (116, 643, 212, 665), (180, 663, 211, 683),        # 18 brewer
 (561, 165, 595, 209), (537, 220, 595, 257),                              # 14 teamster
 [(498, 255), (520, 235), (542, 261), (519, 284)],                       # 14 shed
 (679, 290, 718, 322), (717, 290, 731, 303), (707, 251, 752, 273),        # 21 + cheese shed
 (877, 274, 923, 305), (910, 328, 945, 352),                              # 23 + shed
 (772, 377, 843, 416), (772, 415, 812, 448),                              # 22 miller
 (538, 497, 567, 547), (565, 505, 573, 519),                              # 12 farmer
 (444, 544, 473, 570),                                                   # 11 tailor
 (562, 590, 614, 641), (587, 639, 605, 647),                              # 10 weaver
 [(423, 613), (446, 591), (498, 640), (472, 665)],                       # 9 village hall
 (586, 446, 652, 492),                                                   # barn N
 (537, 683, 592, 735), (514, 732, 539, 782),                              # 8 blacksmith
 [(305, 756), (403, 658), (455, 708), (378, 782)], [(261, 754), (284, 735), (381, 826), (358, 845)],  # 7 inn
 [(307, 684), (332, 665), (345, 682), (320, 701)],                       # shed by the inn
 [(447, 872), (496, 827), (520, 849), (472, 898)],                       # 6 leather worker
 (352, 899, 402, 945),                                                   # 5 farmer
 (329, 969, 380, 1042),                                                  # barn W
 [(303, 1112), (349, 1088), (380, 1114), (338, 1149)],                   # 1 farmer
 (446, 1013, 521, 1042),                                                 # barn E
 (470, 1065, 521, 1103), (519, 1069, 528, 1083),                          # 4 farmer
 (94, 909, 122, 948), (121, 926, 151, 948),                               # 3 woodcutter
 (94, 1106, 135, 1138), (133, 1094, 178, 1126),                           # 2 farmer
 [(591, 818), (638, 780), (664, 840), (633, 870)],                       # 25 herdsman
 (656, 754, 729, 804),                                                   # 26 wheel & wainwright
 (701, 507, 753, 548), (752, 507, 776, 530), (701, 568, 727, 617), (782, 589, 798, 686), (724, 637, 798, 686),  # farmer + 27 village elder
 (794, 747, 854, 776),                                                   # 28 carpenter
 [(992, 659), (1029, 659), (1029, 686), (992, 686)], [(1028, 659), (1067, 659), (1067, 702), (1028, 702)], [(1067, 659), (1091, 659), (1091, 680), (1067, 680)],  # 29 stonemason
 (635, 921, 679, 963),                                                   # druid's hut
]
GAP_REPAIR = 0
TANGENT_RESTORE = 0
FINAL_CLEAN = True
DASH_ZONES = [(1040, 770, 1420, 1120)]
TREE_REBUILD = {'close': 9, 'min': 12, 'max': 60, 'solidity': 0.78, 'cover': 0.35, 'maxfill': 0.55, 'weight': 3, 'near': 7}
TREE_EXCLUDE = []
THICK_GUARD = True
TINT_POLYS = [[(179,547),(208,546),(211,575),(204,600),(199,624),(186,627),(186,610),(180,600),(163,599),(161,640),(166,652),(146,652),(144,600),(151,590),(179,588)]]   # brewer's yard (fine stripe screen)
AGGRESSIVE = True
LABEL_SIZE = 36
