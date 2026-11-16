"""Map 9 Nulb: build maps/raw/map9_clean.png (grid removed, frame and printed river name removed)."""
import subprocess, cv2, numpy as np
subprocess.run(['python3', 'scripts/raw_degrid.py', 'maps/raw/pg-006.jpg', '21,69,1074,699', '28.59,2.5,28.81,2.75',
                'maps/raw/map9_clean.png', '175', '1.8', '4', '2', '9', '3'], check=True)
c = cv2.imread('maps/raw/map9_clean.png', 0)
c[:9, :] = 255; c[-9:, :] = 255; c[:, :9] = 255; c[:, -9:] = 255
ink = (c < 128).astype(np.uint8)
m = np.zeros_like(ink); cv2.fillPoly(m, [np.array([(10, 560), (45, 565), (85, 410), (55, 400)], np.int32)], 1)
n, l, st, _ = cv2.connectedComponentsWithStats(ink, 8)
for i in range(1, n):
    x, y, w, h, a = st[i]; comp = l == i
    if (comp & (m == 1)).sum() > 0.6 * a and max(w, h) < 70: c[comp] = 255
cv2.imwrite('maps/raw/map9_clean.png', c)
