#!/bin/bash
# render_dg.sh "FILE BASE" : FGU PNGs at 100 px / square (svg 50 units / square -> 2x) and print at 300 dpi 7.5 in
B="$1"; cd out/maps
W=$(python3 -c "import re;s=open('$B - GM.svg').read(1000);print(int(float(re.search(r'width=\"([0-9.]+)\"',s).group(1))*2))")
for v in GM Player "Player (No Grid)"; do rsvg-convert -w $W "$B - $v.svg" -o "$B - $v (FGU 100px).png" & done
rsvg-convert -w 2250 "$B - Print.svg" -o "$B - Print (300dpi, 7.5in).png" &
wait; ls -la "$B"* | awk '{print $5, $9, $10, $11, $12, $13, $14, $15, $16}'
