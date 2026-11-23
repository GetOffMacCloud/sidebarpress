"""SP-GS02 The Long Night at Candlecrown -> Fantasy Grounds module. Run: python3 module.py [--test | --install]
Uses the shared builder in 70-Company/Tools/fgu-module-builder (see the fgu-module-build skill).
Art: COLOR files only. Ink / -print files are for the print book and never go into the module.
Never put the seventh verse in the module (it isn't in the vault either)."""
import os,sys,re,glob,shutil,html,copy
HERE=os.path.dirname(os.path.abspath(__file__)); ADV=os.path.dirname(os.path.dirname(HERE)); VAULT=ADV
while not os.path.isdir(os.path.join(VAULT,'70-Company')): VAULT=os.path.dirname(VAULT)
sys.path.insert(0,os.path.join(VAULT,'70-Company','Tools','fgu-module-builder'))
from fgmod import Mod, conv, body, sections, _S, _FT, ids
import fgconv, zipfile, xml.etree.ElementTree as ET
FG=os.environ.get('FG_DIR',os.path.expanduser('~/mnt/Fantasy Grounds'))
# ---- edition settings ----
CODE='SP-GS02'; NAME='SP-GS02 The Long Night at Candlecrown'; DISPLAY='SP-GS02 — The Long Night at Candlecrown'
SRC=ADV; ASSETS=os.path.join(VAULT,'99-Assets',CODE); TEXT_MAP={}
fgconv.STRIP=[CODE+' — ']
fgconv.NAMES={CODE+'-The-Long-Night-at-Candlecrown':'this adventure','00 — Scene Index':'Run Sheet & Trackers',CODE+' — Front Matter':'Running the Adventure',
              'Immoth':'Hrimvald the Gatherer','Tyrg':'Tyrg','The-Tors':'The Tors','League-of-the-Yeomanry':'The Yeomanry','Passage-of-Slerotin':'The Passage of Slerotin',
              'C12 - 5e Conversion Ledger':'The Forgotten Library of Raanet (C12)','Module-Codes':'Module Codes','Plot-Threads':'Plot Threads','Timeline':'Timeline',
              'SP-GS01-The-Gluttonwretch-of-Hommlet':'The Gluttonwretch of Hommlet (GS1)','Skirmisher Minion':'Skirmisher Minion','Enforcer Minion':'Enforcer Minion','04 — Minions':'Minion rules'}
FIX=[(r'\s*\((?:<i>)?verify[^)]*\)',''),(r'00 — Scene Index','Run Sheet &amp; Trackers'),(r'\bthe Scene Index\b','Run Sheet &amp; Trackers'),(r"DM's Notes",'Running the Adventure'),(r'Back to [^<]*?·[^<]*',''),
     (r'\s*<b>Source of truth[^<]*</b>[^.<]*\.',''),(r'\(FGU import text in each bestiary note\)',''),(r'\s*Their notes are the source of truth, with FGU import text; copy any statblock change from there\.',' Every statblock is in this module\'s NPC list.')]
WORK=os.path.expanduser(os.environ.get('FG_WORK','~/work/fgu')+'/'+CODE); FLAT=WORK+'-src'; os.makedirs(FLAT,exist_ok=True)
A=lambda *p: os.path.join(ASSETS,*p)
ART={'cover':A('SP-GS02 - 01 Cover-color.png'),
     'scene-candle-stair':A('SP-GS02 - 02 The Candle Stair-color.png'),'scene-workshop':A('SP-GS02 - 03 The Workshop at Needfest-color.png'),
     'scene-chapel':A("SP-GS02 - 04 The Apprentice's Chapel-color.png"),'scene-gate':A('SP-GS02 - 05 The Knock at the Gate-color.png'),
     'scene-long-night':A('SP-GS02 - 06 The Long Night-color.png'),'scene-seventh-verse':A('SP-GS02 - 07 The Seventh Verse-color.png'),
     'npc-brannoc':A('portraits','SP-GS02 - 11 Brannoc Tull-color.png'),'npc-sedge':A('portraits','SP-GS02 - 12 Old Mother Sedge-color.png'),
     'npc-wenna':A('portraits','SP-GS02 - 13 Wenna Tull-color.png'),'npc-corin':A('portraits','SP-GS02 - 14 Corin the Shepherd-color.png'),
     'npc-pell-ash':A('portraits','SP-GS02 - 15 Pell and Ash-color.png'),'npc-dob-tansy':A('portraits','SP-GS02 - 16 Dob Kettle and Tansy-color.png'),
     'npc-aurel':A('portraits','SP-GS02 - 17 Aurel Vasch-color.png'),
     'handout-corins-drawings':A('handouts',"SP-GS02 - H1 Corin's Drawings-color.png"),'handout-carving':A('handouts',"SP-GS02 - H2 The Apprentice's Carving-color.png"),
     'handout-carol-lantern':A('handouts','SP-GS02 - H3 The Carol Lantern-color.png'),'handout-letter':A('handouts',"SP-GS02 - H4 Aunt Sedge's Letter-color.png"),
     'handout-carol':A('handouts','SP-GS02 - H5 The Long Night Carol-color.png'),'handout-miners-map':A('handouts',"SP-GS02 - H6 The Miners' Map-color.png"),
     'map-m1-candle-stair':A('SP-GS02 - M1 The Candle Stair.png'),'map-m2-candlecrown':A('SP-GS02 - M2 Candlecrown.png'),
     'map-m2-hall-workshop':A('SP-GS02 - M2 Hall and Workshop (inset).png'),'map-m3-old-workings':A('SP-GS02 - M3 The Old Workings.png'),
     'map-m4-ice-library':A('SP-GS02 - M4 The Ice Library.png'),'map-t1-candlecrown':A('SP-GS02 - T1 Candlecrown Town-color.png'),
     'map-r1-region':A('SP-GS02 - R1 Candlecrown Region (draft, color).png')}
PRETTY={'cover':'Cover','scene-candle-stair':'Scene Art — The Candle Stair','scene-workshop':'Scene Art — The Workshop at Needfest','scene-chapel':'Scene Art — The Carved Chapel',
        'scene-gate':'Scene Art — The Knock at the Gate','scene-long-night':'Scene Art — The Long Night','scene-seventh-verse':'Scene Art — The Seventh Verse',
        'npc-brannoc':'NPC — Brannoc Tull','npc-sedge':'NPC — Old Mother Sedge','npc-wenna':'NPC — Wenna Tull','npc-corin':'NPC — Corin the Shepherd',
        'npc-pell-ash':'NPC — Pell and Ash','npc-dob-tansy':'NPC — Dob and Tansy Kettle','npc-aurel':'NPC — Aurel Vasch',
        'handout-corins-drawings':"Handout — Corin's Drawings",'handout-carving':"Handout — The Apprentice's Carving",'handout-carol-lantern':'Handout — The Carol Lantern',
        'handout-letter':"Handout — Aunt Sedge's Letter",'handout-carol':'Handout — The Long Night Carol (border)','handout-miners-map':"Handout — The Miners' Map",
        'map-m1-candle-stair':'Map M1 — The Candle Stair (17 × 30 squares)','map-m2-candlecrown':'Map M2 — Candlecrown (80 × 80 squares)',
        'map-m2-hall-workshop':'Map M2 — The Hall and Workshop (30 × 20 squares)','map-m3-old-workings':'Map M3 — The Old Workings (60 × 50 squares)',
        'map-m4-ice-library':'Map M4 — The Ice Library (50 × 40 squares)','map-t1-candlecrown':'Map T1 — Candlecrown (town overview)','map-r1-region':'Map R1 — Candlecrown and Environs (draft)'}
for k,f in ART.items():
    assert os.path.exists(f),'missing art: '+f
    dst=os.path.join(FLAT,k+'.png')
    if not os.path.exists(dst) or os.path.getmtime(f)>os.path.getmtime(dst): shutil.copyfile(f,dst)
m=Mod(NAME,DISPLAY,'Sidebar Press','Sidebar Press',FG,WORK,text_map=TEXT_MAP)
_pretty=m.pretty; m.pretty=lambda n: PRETTY.get(n) or _pretty(n)
m.images(FLAT)
P=lambda pat: glob.glob(os.path.join(SRC,pat))[0]
SC=lambda n: P('Scenes/Scene %02d —*.md'%n)
def NOTEP(name):
    hits=[p for p in glob.glob(os.path.join(VAULT,'**',name+'.md'),recursive=True) if '_to_delete' not in p and '/.obsidian/' not in p and 'Claude outputs' not in p and '/90-Templates/' not in p]
    return hits[0] if hits else None
MAIN=P(CODE+'-The-Long-Night*.md'); FM=P('*Front Matter.md'); BEST=P('*Bestiary.md'); IDX=P('Scenes/00 — Scene Index.md')
LL=P('*The Lantern Line.md'); OW=P('*The Old Workings.md')
def tidy(t):
    """Drop vault-only furniture: Meta Bind quick-edit callouts, art callouts, code blocks, empty template tables and empty sections."""
    out=[]; skip=False; fence=False
    for l in t.split('\n'):
        if l.startswith('```'): fence=not fence; continue
        if fence: continue
        if re.match(r'> \[!(abstract|art)\]|> \[!info\]- FGU',l): skip=True; continue
        if skip and l.startswith('>'): continue
        skip=False
        if re.match(r'^\|(\s*\|)+\s*$',l) or 'INPUT[' in l or 'BUTTON[' in l: continue
        out.append(l)
    t='\n'.join(out)
    t=re.sub(r'(?m)^(\|[^\n]*\|)\n(\|[\s:\-|]+\|)\n(?!\|)',r'',t)  # header + separator with no rows
    parts=re.split(r'(?m)^(#{2,3} .*)$',t); keep=[parts[0]]
    for i in range(1,len(parts),2):
        if parts[i+1].strip(): keep+= [parts[i],parts[i+1]]
    return ''.join(keep)
def C(t):
    x=conv(tidy(t))
    for a,b in FIX: x=re.sub(a,b,x)
    return x
def fullnote(p):
    t=re.sub(r'^\s*# .*\n','',body(p),count=1)
    return re.sub(r'^\s*(?:Back to |\[\[)[^\n]*(?:Index|Back to|·)[^\n]*\n','',t,count=1)
pick=lambda S,*n: '\n'.join('## %s\n%s'%(x,S[x]) for x in n if x in S)
M=sections(body(MAIN)); F=sections(body(FM)); X=sections(body(IDX))
exec(open(os.path.join(HERE,'module_npcs.py')).read())
exec(open(os.path.join(HERE,'module_pages.py')).read())
m.LINT=[r'SP-GS02-The',r'SP-GS02 — (?!The Long Night at Candlecrown)',r'FGU import',r'Quick edit',r'Meta Bind',r'dataview']
OUT=os.path.join(ADV,'FGU Kit',NAME+'.mod'); os.makedirs(os.path.dirname(OUT),exist_ok=True)
m.build(WORK+'.mod',cover_image='cover')
if '--test' in sys.argv: sys.exit(0)
shutil.copyfile(WORK+'.mod',OUT); print('wrote',OUT)
if '--install' in sys.argv: shutil.copyfile(OUT,os.path.join(FG,'modules',NAME+'.mod')); print('installed to FG modules')
