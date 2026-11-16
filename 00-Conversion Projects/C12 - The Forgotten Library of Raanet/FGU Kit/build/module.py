"""C12 The Forgotten Library of Raanet (5e conversion) -> FGU module.
Story entries come from the working campaign's db.xml (they carry the in-FG fixes); NPCs from the
FG NPC Import text; items from the FG Item Import text; maps from FGU Kit/Maps with story pins.
Run:  FG_DIR="$HOME/mnt/Fantasy Grounds" FG_WORK="$HOME/fgwork/c12" python3 module.py [--test|--install]"""
import os,sys,re,html,copy,shutil,json
K=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))          # FGU Kit
V=os.path.expanduser('~/mnt/Sidebar Press Vault')
sys.path.insert(0,os.path.join(V,'70-Company/Tools/fgu-module-builder'))
import fgmod,fgtext
from fgmod import _S,_FT,_WR,ids
import xml.etree.ElementTree as ET
NAME='C12 - The Forgotten Library of Raanet'; DISPLAY='C12 The Forgotten Library of Raanet (5E)'
FG=os.environ['FG_DIR']; WORK=os.environ['FG_WORK']; os.makedirs(WORK,exist_ok=True)
CAMPAIGN=os.path.join(FG,'campaigns/C12 - The Forgotten Library of Raane/db.xml')
m=fgmod.Mod(NAME,DISPLAY,'Sidebar Press Conversions','Sidebar Press',FG,WORK)
slug=lambda x: re.sub(r'[^a-z0-9]','',x.lower())[:40]
# ---------- maps
src=os.path.join(WORK,'src'); shutil.rmtree(src,ignore_errors=True); os.makedirs(src)
MAPS={'map-m1-temple-incandescent':('C12 Map - M1 Temple Incandescent (5ft grid).png',48),
      'map-m1-temple-incandescent-player':('C12 Map - M1 Temple Incandescent (5ft grid, Player).png',48),
      'map-m2-burning-athenium':('C12 Map - M2 Burning Athenium (5ft grid).png',60),
      'map-m2-burning-athenium-player':('C12 Map - M2 Burning Athenium (5ft grid, Player).png',60)}
for k,(f,_) in MAPS.items(): shutil.copy(os.path.join(K,'Maps',f),os.path.join(src,k+'.png'))
m.images(src)
from PIL import Image
SIZE={k:Image.open(os.path.join(src,k+'.png')).size for k in MAPS}
for k,(f,g) in MAPS.items():
    im=m._cat('image').find(m.IMG[k][0]).find('image')
    for t,v in (('grid','on'),('gridsize','%d,%d'%(g,g)),('gridoffset','0,0')):
        e=ET.Element(t); e.text=v; im.insert(0,e)
    if k.endswith('player'): m._cat('image').find(m.IMG[k][0]).find('name').text+=' (Player)'
# ---------- NPCs (all 55 from the import text) + SRD salamander / efreeti
t=open(os.path.join(K,'C12 - FG NPC Import.txt')).read()
NK={}
for x in re.split(r'^(?:#{8} .* #{8}|#### .*####)\s*$',t,flags=re.M):
    if re.search(r'^Armor Class',x,re.M) and re.search(r'^Challenge',x,re.M):
        d=fgtext.parse(x.strip()); k=slug(d['name'])
        while k in m.NPC: k+='x'
        fgtext.add(m,k,d,'<h>%s</h><p><i>C12 The Forgotten Library of Raanet, 5e conversion (Sidebar Press).</i></p>'%html.escape(d['name']))
        NK[d['name']]=k
m.npc_srd('salamander','Salamander','salamander')
m.npc_srd('efreeti','Efreeti (Wandering)','efreeti')
def n(prefix): return next(v for k,v in NK.items() if k.startswith(prefix))
# ---------- story entries from the campaign
camp=ET.parse(CAMPAIGN).getroot(); ST={}
story=m._cat('encounter')
for e in camp.find('encounter'):
    e2=copy.deepcopy(e); story.append(e2)
    mm=re.match(r'^A(\d+)([a-z]?)\.',e.findtext('name') or '')
    if mm: ST[str(int(mm.group(1)))+mm.group(2)]=('encounter.'+e.tag,e2)
# ---------- encounters (ledger §6, party 6 x L6)
M1='map-m1-temple-incandescent'; M2='map-m2-burning-athenium'
ENC=[('A3','Keeper-of-the-Hearth',[(n('Keeper'),1)],M1,'3'),
 ('A4','Caryatid Column (west alcove)',[(n('Caryatid'),1)],M1,'4'),
 ('A5','Caryatid Column (east alcove)',[(n('Caryatid'),1)],M1,'5'),
 ('A9','Wraiths of the Oubliette',[(n('Wraith of'),2)],M1,'9'),
 ('A10','Magmen (Brothers\' Suites)',[(n('Magman'),5)],M1,'10'),
 ('A11','Magmen (Sisters\' Suites)',[(n('Magman'),4)],M1,'11'),
 ('A12','Air Elemental of the Retreat',[(n('Air Elemental'),1)],M1,'12'),
 ('A13','Harginn Grues',[(n('Harginn'),4)],M1,'13'),
 ('A15','Ranzaar',[(n('Ranzaar'),1)],M1,'15'),
 ('A16','Fire Bat Colony',[(n('Fire Bat'),12)],M1,'16'),
 ('A19','Phantom Stalkers',[(n('Phantom'),3)],M1,'19'),
 ('A21a','Ixthasus (alone)',[(n('Ixthasus'),1)],M1,'21'),
 ('A21b','Ixthasus and the alarm (+2 salamanders)',[(n('Ixthasus'),1),('salamander',2)],M1,'21'),
 ('A22a','The Conflagration (4 salamanders)',[('salamander',4)],M1,'22'),
 ('A22b','The Conflagration after the alarm (2 salamanders)',[('salamander',2)],M1,'22'),
 ('A23','Magmen (Incinerator)',[(n('Magman'),5)],M1,'23'),
 ('A25','Stone Guardian',[(n('Stone Guardian'),1)],M1,'25'),
 ('A28','Magmen (Playing with Fire)',[(n('Magman'),4)],M1,'28'),
 ('A30','Wights of the Cornucopia',[(n('Wight'),5)],M1,'30'),
 ('A32','The Fallen Champions',[(n('Naskin'),1),(n('Yrsi'),1)],M1,'32'),
 ('A33','Yox',[(n('Yox'),1)],M1,'33'),
 ('A35','Avraasha, the First Servant',[(n('Avraasha'),1)],M2,'35'),
 ('W1','Wandering Efreeti',[('efreeti',1)],None,None)]
for code,name,cr,mp,area in ENC: m.battle(code,name,cr,mp)
# links at the foot of each story entry: its encounters and creatures
for code,name,cr,mp,area in ENC:
    if not area or area not in ST: continue
    tx=ST[area][1].find('text'); ll=tx.find('linklist')
    if ll is None:
        p=ET.SubElement(tx,'p'); b=ET.SubElement(p,'b'); b.text='Encounters and creatures'; ll=ET.SubElement(tx,'linklist')
    a=ET.SubElement(ll,'link',{'class':'battle','recordname':m.BAT[code]}); a.text='Encounter: %s %s'%(code,name)
    for k,c in cr:
        if not any(x.get('recordname')==m.NPC[k] for x in ll):
            a=ET.SubElement(ll,'link',{'class':'npc','recordname':m.NPC[k]}); a.text='NPC: '+m.npcname(k)
# ---------- items (FG Item Import list format)
GM=[]
NUM={'Weight':'weight','AC Base':'ac','Bonus':'bonus'}
STR={'Non-Identified Name':'nonid_name','Damage':'damage','Properties':'properties','Cost':'cost'}
for blk in re.split(r'\n\s*\n',open(os.path.join(K,'C12 - FG Item Import.txt')).read().strip()):
    f={}
    for l in blk.split('\n'):
        mm=re.match(r'^([A-Za-z \-]+):\s?(.*)$',l)
        if mm: f[mm.group(1).strip()]=mm.group(2).strip()
    if 'Name' not in f: continue
    kw={}
    for a,b in NUM.items():
        if f.get(a):
            try: kw[b]=float(f[a]) if '.' in f[a] else int(f[a])
            except ValueError: pass
    for a,b in STR.items():
        if f.get(a): kw[b]=f[a]
    desc=''.join('<p>%s</p>'%html.escape(x) for x in f.get('Description','').split('\\n') if x)
    key=slug(f['Name'])
    while key in m.ITEM: key+='x'
    m.item(key,f['Name'],f.get('Type',''),desc or '<p></p>',subtype=f.get('Subtype',''),rarity=f.get('Rarity',''),**kw)
    if f.get('DM Only'): GM.append((key,f['DM Only']))
# ---------- map pins: story entries on the DM maps (alcoves 25a-25j point at Area 25)
P1=json.load(open(os.path.join(os.path.dirname(__file__),'pins_m1.json')))
P2={'35':[1560,1181],'34b':[1560,140],'35b':[1700,1181],'35c':[1840,1181]}
def pins(imgkey,P):
    W,H=SIZE[imgkey]; im=m._cat('image').find(m.IMG[imgkey][0]).find('image'); ly=im.find('layers'); lid=10
    for lab,(x,y) in sorted(P.items(),key=lambda kv:(int(re.match(r'\d+',kv[0]).group()),kv[0])):
        area=lab if lab in ST else re.match(r'\d+',lab).group()
        if area not in ST: print('no story for pin',lab); continue
        rec,e=ST[area]; lid+=1; L=_S(ly,'layer')
        _S(L,'name',None,('Area %s — '%lab)+(e.findtext('name') or '')); _S(L,'id',None,lid); _S(L,'parentid',None,-1); _S(L,'type',None,'shortcut')
        sc=_S(L,'shortcut'); _S(sc,'class',None,'encounter'); _S(sc,'record',None,rec)
        _S(L,'matrix',None,'1,0,0,0,0,1,0,0,0,0,1,0,%d,%d,0,1'%(x-W//2,y-H//2))
pins(M1,P1); pins(M2,P2)
# ---------- reference pages
L=lambda c,r,t:'<link class="%s" recordname="%s">%s</link>'%(c,r,html.escape(t))
intro=('<p>A 1e-to-5e conversion of <i>C12 The Forgotten Library of Raanet</i>, built for a party of six 6th-level characters '
 '(the encounter list shows the ledger\'s difficulty at that size).</p>'
 '<p><b>How the module is organised.</b> The <b>Story</b> list holds the read-aloud and keyed text for every area (A01–A35). '
 'The DM maps carry a pin on every area number, and the alcoves 25a–25j pin to Area 25; double-click a pin to open its entry. '
 'Share the <b>(Player)</b> maps, which have the numbers, secret doors and treasure marks painted out. Both maps use a 5-ft grid.</p>'
 '<p>Every story entry ends with links to its encounters and creatures. The full roster of 55 statblocks, including the summonable creatures for the Summoning Sigil and the <i>Monster Summoning</i> scrolls, is also in the <b>Sidebar Press Bestiary</b> module.</p>')
m.page('Introduction','Using This Module',intro,links=[m.I(M1),m.I(M1+'-player'),m.I(M2),m.I(M2+'-player')])
tb='<table><tr><td><b>Code</b></td><td><b>Encounter</b></td><td><b>XP</b></td></tr>'+''.join('<tr><td>%s</td><td>%s</td><td>%s</td></tr>'%(c,html.escape(nm),sum(m.XP[k]*q for k,q in cr)) for c,nm,cr,_,_ in ENC)+'</table>'
m.page('Introduction','Encounters',tb,links=[m.B(c) for c,*_ in ENC])
tb='<table><tr><td><b>Item</b></td><td><b>GM note</b></td></tr>'+''.join('<tr><td>%s</td><td>%s</td></tr>'%(html.escape(m.ITEMN[k]),html.escape(g)) for k,g in GM)+'</table>'
m.page('Introduction','Treasure — GM Notes',tb,links=[m.IT(k) for k,_ in GM])
out=os.path.join(K,NAME+('.test' if '--test' in sys.argv else '')+'.mod')
m.build(out,cover_image=M1)
if '--install' in sys.argv: shutil.copy(out,os.path.join(FG,'modules',NAME+'.mod')); print('installed')
