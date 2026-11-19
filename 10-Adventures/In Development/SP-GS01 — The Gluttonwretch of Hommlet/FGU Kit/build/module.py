"""SP-GS01 The Gluttonwretch of Hommlet -> Fantasy Grounds module. Run: python3 module.py [--test | --install]
Uses the shared builder in 70-Company/Tools/fgu-module-builder (see the fgu-module-build skill).
Private stream edition (Greybeard's table): includes the traced T1 Hommlet maps. Do not sell this build.
Art: COLOR files only. The (ink) files are print-only and never go into the module."""
import os,sys,re,glob,shutil,html,copy
HERE=os.path.dirname(os.path.abspath(__file__)); ADV=os.path.dirname(os.path.dirname(HERE)); VAULT=ADV
while not os.path.isdir(os.path.join(VAULT,'70-Company')): VAULT=os.path.dirname(VAULT)  # works at any folder depth
sys.path.insert(0,os.path.join(VAULT,'70-Company','Tools','fgu-module-builder'))
from fgmod import Mod, conv, body, sections, _S, _FT, ids
import fgconv, zipfile, xml.etree.ElementTree as ET
FG=os.environ.get('FG_DIR',os.path.expanduser('~/mnt/Fantasy Grounds'))
# ---- edition settings ----
CODE='SP-GS01'; NAME='SP-GS01 The Gluttonwretch of Hommlet'; DISPLAY='SP-GS01 — The Gluttonwretch of Hommlet'
SRC=ADV; ASSETS=os.path.join(VAULT,'99-Assets',CODE); TEXT_MAP={}
fgconv.STRIP=[CODE+' — ']
fgconv.NAMES={CODE+'-The-Gluttonwretch-of-Hommlet':'this adventure','Gluttonwretch':'The Gluttonwretch','Offering-Heap':'The Offering-Heap',
              'The-Common-Year-Calendar':'The Common Year Calendar','Viscounty-of-Verbobonc':'The Viscounty of Verbobonc',
              '00 — Scene Index':'Run Sheet & Trackers',CODE+' — Front Matter':'Running the Adventure',
              'The-Battle-of-Emridy-Meadows':'Emridy Meadows','The-Temple-of-Elemental-Evil':"The Temple's Long Shadow"}
# Module-only wording fixes (never edit the print notes for these)
FIX=[(r'\s*\((?:<i>)?verify[^)]*\)',''),(r"DM's Notes",'Running the Adventure'),
     (r'Build it as a <b>second Fantasy Grounds NPC record</b> and drop it','The second NPC record is in this module: drop it'),
     (r'\s*Also printed as an extra form in [^.]*\.',''),(r'<b>Source of truth: [^<]*</b>[^.]*\.\s*copy any statblock change from there\.',''),
     (r'\s*<b>Source of truth: [^<]*</b> in the bestiary; copy any statblock change from there\.','')]
# ---- art: colour only, renamed to module keys ----
WORK=os.path.expanduser(os.environ.get('FG_WORK','~/work/fgu')+'/'+CODE); FLAT=WORK+'-src'; os.makedirs(FLAT,exist_ok=True)
ART={'01 Cover - The Open Door':'cover-art','02 Brewfest Eve':'scene-brewfest-eve',"03 The Elder's Cellar":'scene-the-elders-cellar',
     '04 The Offering-Heap':'npc-offering-heap','05 Chapel of the Rotting Table':'scene-chapel-of-the-rotting-table','06 The Roost on Emridy Meadows':'scene-the-roost',
     '07 The Last Toast':'scene-the-last-toast','08 The Gluttonwretch':'npc-gluttonwretch','09 Second Helpings':'npc-second-helpings','10 Hollow Guests':'npc-hollow-guests',
     '11 Deacon Mungo Brindlewick':'npc-brindlewick','12 Wat Thistlewood':'npc-wat-thistlewood','13 Widow Marta Bree':'npc-widow-bree','14 Pudding':'npc-pudding',
     '15 Brother of the Rotting Table':'npc-brother','16 Earth Elemental':'npc-earth-elemental','17 Rannos Davl':'npc-rannos','18 Gremag':'npc-gremag'}
MAPS={'M1 Feast Green':'m1-feast-green','M2a Smokehouse Ground Floor':'m2a-smokehouse-ground-floor','M2b Smokehouse Cellar':'m2b-smokehouse-cellar',
      'M3 Jaroos Grove':'m3-jaroos-grove','M4 Emridy Meadows':'m4-emridy-meadows','T1 Map 2 - Village of Hommlet':'t1-village-of-hommlet',
      'T1 Map 3 - Inn of the Welcome Wench':'t1-inn-of-the-welcome-wench',"T1 Map 4 - Traders' Establishment":'t1-traders-establishment',
      'T1 Map 5 - Church of St Cuthbert':'t1-church-of-st-cuthbert'}
PRETTY={'cover':'Cover','cover-art':'Scene Art — The Open Door','npc-brindlewick':'NPC — Deacon Mungo Brindlewick','npc-widow-bree':'NPC — Widow Marta Bree',
        'scene-the-elders-cellar':"Scene Art — The Elder's Cellar",'scene-the-roost':'Scene Art — The Roost on Emridy Meadows'}
for t,k in MAPS.items():
    lab=t.replace('Jaroos',"Jaroo's").replace(' - ',': ')
    PRETTY['map-'+k]='Map — '+lab+' (player)'; PRETTY['gm-'+k]='Map — '+lab+' (GM, keyed)'
def put(src,key):
    dst=os.path.join(FLAT,key+os.path.splitext(src)[1].lower())
    if not os.path.exists(dst) or os.path.getmtime(src)>os.path.getmtime(dst): shutil.copyfile(src,dst)
for t,k in ART.items(): put(os.path.join(ASSETS,'%s - %s (color).png'%(CODE,t)),k)
for t,k in MAPS.items():
    for f in glob.glob(os.path.join(ASSETS,'maps','%s - %s - *.png'%(CODE,t))):
        if ' - Player (No Grid) (FGU' in f: put(f,'map-'+k)
        elif ' - GM (FGU' in f: put(f,'gm-'+k)
TOKENS={'token-gluttonwretch':os.path.join(VAULT,'99-Assets','Bestiary','FGU','Tokens','Gluttonwretch — Token.png'),
        'token-offering-heap':os.path.join(VAULT,'99-Assets','Bestiary','FGU','Tokens','Offering-Heap — Token.png')}
for f in glob.glob(os.path.join(ASSETS,'tokens','%s token-*.png'%CODE)): TOKENS[os.path.basename(f)[len(CODE)+1:-4]]=f
for k,f in TOKENS.items(): put(f,k)
put(os.path.join(VAULT,'99-Assets','_Covers','Cover — The Gluttonwretch of Hommlet (color).png'),'cover')  # the colour trade-dress cover
m=Mod(NAME,DISPLAY,'Sidebar Press','Sidebar Press',FG,WORK,text_map=TEXT_MAP)
_pretty=m.pretty; m.pretty=lambda n: PRETTY.get(n) or _pretty(n)
m.images(FLAT)
for k in [k for k in m.IMG if re.match(r'(map|gm)-m\d',k)]:  # Sidebar Press battlemaps are drawn at 100 px = 5 ft.
    im=m._cat('image').find(m.IMG[k][0]).find('image'); g=ET.Element('grid'); g.text='on'; gs=ET.Element('gridsize'); gs.text='100,100'; im.insert(0,gs); im.insert(0,g)
P=lambda pat: glob.glob(os.path.join(SRC,pat))[0]
SC=lambda n: P('Scenes/Scene %02d —*.md'%n)
def NOTEP(name):
    hits=[p for p in glob.glob(os.path.join(VAULT,'**',name+'.md'),recursive=True) if '_to_delete' not in p and '/.obsidian/' not in p]
    assert hits,'note not found: '+name; return hits[0]
for h in glob.glob(os.path.join(SRC,'*Handout —*.md')):
    tt=re.search(r'^title: "(.*)"',open(h).read(),re.M)
    if tt: fgconv.NAMES[os.path.basename(h)[:-3]]=tt.group(1)
MAIN=P(CODE+'-The-Glutton*.md'); FM=P('*Front Matter.md'); BEST=P('*Bestiary.md'); IDX=P('Scenes/00 — Scene Index.md')
EMB=re.compile(r'!\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]')
def noart(t):
    out=[]; skip=False
    for l in t.split('\n'):
        if l.startswith('> [!art'): skip=True; continue
        if skip and l.startswith('>'): continue
        skip=False; out.append(l)
    return '\n'.join(out)
def C(t):
    x=conv(noart(t))
    for a,b in FIX: x=re.sub(a,b,x)
    return x
def fullnote(p):  # body without the title line and the navigation line under it
    t=re.sub(r'^\s*# .*\n','',body(p),count=1)
    return re.sub(r'^\s*(?:Back to |\[\[)[^\n]*(?:Scene Index|Back to|·)[^\n]*\n','',t,count=1)
pick=lambda S,*n: '\n'.join('## %s\n%s'%(x,S[x]) for x in n if x in S)
M=sections(body(MAIN)); F=sections(body(FM)); X=sections(body(IDX))
exec(open(os.path.join(HERE,'module_npcs.py')).read())
exec(open(os.path.join(HERE,'module_parcels.py')).read())
exec(open(os.path.join(HERE,'module_walls.py')).read())
exec(open(os.path.join(HERE,'module_loc.py')).read())
exec(open(os.path.join(HERE,'module_pages.py')).read())
# ---- build ----
m.LINT=[r'SP-GS01-The',r'SP-GS01 — (?!The Gluttonwretch of Hommlet)',r'Fantasy Grounds NPC record',r'Source of truth']
OUT=os.path.join(ADV,'FGU Kit',NAME+'.mod'); os.makedirs(os.path.dirname(OUT),exist_ok=True)
m.build(WORK+'.mod',cover_image='cover')
if '--test' in sys.argv: sys.exit(0)  # build and lint only; leave the shipped .mod alone
shutil.copyfile(WORK+'.mod',OUT)
if '--install' in sys.argv: shutil.copyfile(OUT,os.path.join(FG,'modules',NAME+'.mod')); print('installed to FG modules')
