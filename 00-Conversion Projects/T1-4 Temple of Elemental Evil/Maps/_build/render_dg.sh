#!/bin/bash
# render_dg.sh "FILE BASE" : FGU PNGs at 100 px per grid square (FGU_MUL=2 for 10-ft squares, 4 for 5-ft), print 300 dpi 7.5 in.
# Renders sequentially (5-ft FGU images are ~7300 px wide; parallel renders run out of memory).
B="$1"; cd out/maps
W=$(python3 -c "import re;s=open('$B - GM.svg').read(1000);print(int(float(re.search(r'width=\"([0-9.]+)\"',s).group(1))*${FGU_MUL:-2}))")
for v in GM Player "Player (No Grid)"; do rsvg-convert -w $W "$B - $v.svg" -o "$B - $v (FGU 100px).png" || exit 1; done
rsvg-convert -w 2250 "$B - Print.svg" -o "$B - Print (300dpi, 7.5in).png"
