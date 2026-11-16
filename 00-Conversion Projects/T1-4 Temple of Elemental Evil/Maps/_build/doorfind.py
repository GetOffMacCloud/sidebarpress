"""Find door rectangles in a grey-rock TSR dungeon scan. usage: doorfind.py CFG.py -> OUT_doors.json + overlay"""
import sys, json, cv2, numpy as np
C = {}; exec(open(sys.argv[1]).read(), C)
m = json.load(open(C['OUT'] + '_meta.json')); x0, y0, x1, y1 = m['box']
I = cv2.imread(C['OUT'] + '_I.png', 0); H, W = I.shape
hole = (I >= C.get('DOOR_HOLE_T', 170)).astype(np.uint8)
n, lab, st, cen = cv2.connectedComponentsWithStats(hole, 4)
cand = [i for i in range(1, n) if 3 <= st[i, 4] <= 160 and max(st[i, 2], st[i, 3]) <= C.get('DOOR_L', (7, 17))[1]]
_lz = np.zeros((H, W), np.uint8)
for it in C.get('LABELS', []):
    _w = 6 * len(it[0]) + 8; _h = 11
    if len(it) > 3 and it[3]: _w = _h = max(_w, _h)
    _lz[max(int(it[2] - _h), 0):int(it[2] + _h), max(int(it[1] - _w), 0):int(it[1] + _w)] = 1
cand = [i for i in cand if not _lz[int(cen[i][1]), int(cen[i][0])]]
dark = (I < 130).astype(np.uint8)
# group nearby small holes (a grid line may split one door interior)
used = set(); doors = []
for i in cand:
    if i in used: continue
    grp = [i]; used.add(i); ch = True
    while ch:
        ch = False
        a = min(st[j, 0] for j in grp); b = min(st[j, 1] for j in grp); c = max(st[j, 0] + st[j, 2] for j in grp); d = max(st[j, 1] + st[j, 3] for j in grp)
        for j in cand:
            if j in used: continue
            if st[j, 0] <= c + 3 and st[j, 0] + st[j, 2] >= a - 3 and st[j, 1] <= d + 3 and st[j, 1] + st[j, 3] >= b - 3:
                grp.append(j); used.add(j); ch = True
    a = min(st[j, 0] for j in grp); b = min(st[j, 1] for j in grp); c = max(st[j, 0] + st[j, 2] for j in grp); d = max(st[j, 1] + st[j, 3] for j in grp)
    w, h = c - a, d - b
    L, S_ = max(w, h), min(w, h)
    Lr, Sr, AR = C.get('DOOR_L', (7, 17)), C.get('DOOR_S', (1, 7)), C.get('DOOR_AR', 1.8)
    if not (Lr[0] <= L <= Lr[1] and Sr[0] <= S_ <= Sr[1] and L >= AR * S_): continue
    # ring darkness: outline around the interior
    A, B, Cc, D = max(a - 3, 0), max(b - 3, 0), min(c + 3, W), min(d + 3, H)
    box = dark[B:D, A:Cc].copy(); box[b - B:d - B, a - A:c - A] = 0
    ring = np.zeros_like(box); ring[:, :] = 1; ring[b - B:d - B, a - A:c - A] = 0
    # sample the 4 sides 1-3 px outside the interior
    sides = [dark[max(b - 3, 0):b, a:c], dark[d:d + 3, a:c], dark[b:d, max(a - 3, 0):a], dark[b:d, c:c + 3]]
    sc = [s.any(axis=0 if k < 2 else 1).mean() if s.size else 0 for k, s in enumerate(sides)]
    if min(sc) < 0.6: continue
    pts = (np.column_stack(np.nonzero(np.isin(lab[b:d, a:c], grp)))[:, ::-1] + [a, b]).astype(np.float32)
    (cx, cy), (rw, rh), ang = cv2.minAreaRect(pts)
    if rw < rh: rw, rh = rh, rw; ang += 90
    ang = ((ang + 90) % 180) - 90
    if C.get('DOOR_RECT_ONLY'):
        fill_ = len(pts) / max((c - a) * (d - b), 1)
        if fill_ < C.get('DOOR_FILL', 0.72): continue
        if min(abs(ang), abs(abs(ang) - 90)) > 6: continue
    if abs(ang) < 8: ang = 0.0
    elif abs(abs(ang) - 90) < 8: ang = 90.0
    o = ('h' if ang == 0 else 'v') if ang in (0.0, 90.0) else round(float(ang), 1)
    doors.append([round((a + c) / 2, 1), round((b + d) / 2, 1), o, round(float(L) + 4, 1), round(float(S_) + 4, 1)])
json.dump(doors, open(C['OUT'] + '_doors.json', 'w'))
v = cv2.cvtColor(I, cv2.COLOR_GRAY2BGR)
for k, (x, y, o, L, S_) in enumerate(doors):
    w, h = (S_, L) if o == 'v' else (L, S_)
    if not isinstance(o, str): w, h = L, L
    cv2.rectangle(v, (int(x - w / 2), int(y - h / 2)), (int(x + w / 2), int(y + h / 2)), (0, 0, 255), 1)
    cv2.putText(v, str(k), (int(x + w / 2 + 1), int(y)), cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 140, 0), 1)
cv2.imwrite(C['OUT'] + '_doors.png', v)
print(len(doors), 'doors')
