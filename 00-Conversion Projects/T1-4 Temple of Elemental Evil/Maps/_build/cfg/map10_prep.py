"""Map 10 Tower Ruins: grid removed inside the tower floor only (the grid is printed only there)."""
import subprocess, cv2, numpy as np
B = (270, 745, 1000, 1300); CX, CY, RF = 448.8, 294.6, 160
subprocess.run(['python3', 'scripts/raw_degrid.py', 'maps/raw/pg-006.jpg', ','.join(map(str, B)), '25.07,15.25,25.235,21.765',
                '/tmp/m10_dg.png', '175', '1.8', '4', '2', '9', '3'], check=True)
dg = cv2.imread('/tmp/m10_dg.png', 0)
I = cv2.imread('maps/raw/pg-006.jpg', 0)[B[1]:B[3], B[0]:B[2]]
H, W = I.shape; yy, xx = np.mgrid[0:H, 0:W]
fl = np.hypot(xx - CX, yy - CY) < 214
_ent = np.zeros((H, W), np.uint8); cv2.fillPoly(_ent, [np.array([(288, 360), (345, 360), (360, 470), (290, 470)], np.int32)], 1)
fl |= _ent.astype(bool)
raw = np.where(I < 175, 0, 255).astype(np.uint8)
out = np.where(fl, dg, raw)
PX, OX, PY, OY = 25.07, 15.25, 25.235, 21.765
dvx = np.abs(((xx - OX) / PX - np.round((xx - OX) / PX)) * PX); dvy = np.abs(((yy - OY) / PY - np.round((yy - OY) / PY)) * PY)
band = (dvx <= 2.5) | (dvy <= 2.5)
ink = ((out < 128) & fl).astype(np.uint8)
n, l, st, _ = cv2.connectedComponentsWithStats(ink, 8)
for i in range(1, n):
    x, y, w, h, a = st[i]
    if a <= 30 and max(w, h) <= 12:
        comp = l == i
        if band[comp].mean() > 0.8: out[comp] = 255
# spurs off the wall ring and partitions: thin 1-3 px stubs on a band, opened away
ink = (out < 128).astype(np.uint8)
op = cv2.morphologyEx(ink, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
sp = (ink & (1 - op) & band & fl).astype(np.uint8)
n, l, st, _ = cv2.connectedComponentsWithStats(sp, 8)
for i in range(1, n):
    if st[i, 4] <= 14 and max(st[i, 2], st[i, 3]) <= 9: out[l == i] = 255
cv2.imwrite('maps/raw/map10_clean.png', out)
