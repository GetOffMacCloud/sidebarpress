#!/bin/bash
# dg_build.sh m13 map13 "T2-4 Map 13 - Dungeon Level 2"
set -e
cd /home/claude/toee
python3 scripts/dungeon_prep.py maps/dgcfg/$1.py | grep -v "^box" || true
python3 scripts/doorfind.py maps/dgcfg/$1.py
python3 scripts/dungeon_prep.py maps/dgcfg/$1.py | grep -E "missed" || true
python3 scripts/inktrace.py maps/cfg/$2.py out/maps >/dev/null
for v in GM "Player (No Grid)"; do rsvg-convert -w 2000 "out/maps/$3 - $v.svg" -o "/tmp/$1-$v.png" & done; wait
python3 - "$1" <<'P'
import cv2,sys
k=sys.argv[1]
for v,t in (('GM','g'),('Player (No Grid)','p')):
    g=cv2.imread(f'/tmp/{k}-{v}.png'); h,w=g.shape[:2]
    for n,(a,b) in enumerate([(0,0),(w//2,0),(0,h//2),(w//2,h//2)]): cv2.imwrite(f'/tmp/{t}{"abcd"[n]}.png',g[b:b+h//2,a:a+w//2])
P
