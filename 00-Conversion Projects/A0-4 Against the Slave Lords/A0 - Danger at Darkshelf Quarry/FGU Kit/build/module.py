"""A0 Danger at Darkshelf Quarry (5e conversion) -> Fantasy Grounds Unity module.
Reads the vault notes in this adventure folder (site keys, Bestiary, NPCs, Items), the Cause Fear spell note,
and the cleaned scan maps in Maps/A0. Uses the shared builder in 70-Company/Tools/fgu-module-builder.
Run:  FG_DIR="$HOME/mnt/Fantasy Grounds" FG_WORK="$HOME/fgwork" python3 module.py [--test|--install]"""
import os,sys,re,glob,shutil,html,json,zipfile
import xml.etree.ElementTree as ET
HERE=os.path.dirname(os.path.abspath(__file__)); ADV=os.path.dirname(os.path.dirname(HERE)); PROJ=os.path.dirname(ADV); VAULT=PROJ
while not os.path.isdir(os.path.join(VAULT,'70-Company')): VAULT=os.path.dirname(VAULT)
sys.path.insert(0,os.path.join(VAULT,'70-Company','Tools','fgu-module-builder'))
import fgmod,fgconv,fgtext
from fgmod import Mod,_S,_FT,ids
FG=os.environ.get('FG_DIR',os.path.expanduser('~/mnt/Fantasy Grounds'))
NAME='A0 - Danger at Darkshelf Quarry'; DISPLAY='A0 Danger at Darkshelf Quarry (5E)'
WORK=os.path.join(os.path.expanduser(os.environ.get('FG_WORK','~/fgwork')),'A0'); os.makedirs(WORK,exist_ok=True)
MAPDIR=os.path.join(PROJ,'Maps','A0')
m=Mod(NAME,DISPLAY,'Sidebar Press Conversions','Sidebar Press',FG,WORK)
slug=lambda x: re.sub(r'[^a-z0-9]','',x.lower())
def body(p):
    t=open(p).read()
    return t.split('\n---',1)[1].split('\n',1)[1] if t.startswith('---') else t
# ---------------------------------------------------------------- wikilinks: vault notes -> module records/pages
def prep(t):
    t=re.sub(r'\[\[A0 - 5e Conversion Ledger\]\]','the Sidebar Press conversion ledger',t)
    t=re.sub(r'\[\[A0 - Bestiary \(5e\)#([^\]|]+)(\|[^\]]*)?\]\]',lambda x:'[[%s%s]]'%(x.group(1),x.group(2) or ''),t)
    t=re.sub(r'\[\[A0 - Bestiary \(5e\)\]\]','[[Bestiary]]',t)
    t=re.sub(r'\[\[A0-0\d [^\]#|]*#([^\]|]+)(\|[^\]]*)?\]\]',lambda x:'[[%s%s]]'%(x.group(1),x.group(2) or ''),t)
    t=re.sub(r'\[\[A0-0\d ([^\]|]+)(\|[^\]]*)?\]\]',lambda x:'[[%s%s]]'%(x.group(1),x.group(2) or ''),t)
    return t
ITEMNOTES=sorted(glob.glob(os.path.join(ADV,'Items','*.md')))
fgconv.NAMES={os.path.basename(p)[:-3]:re.sub(r' \(A0\)$','',os.path.basename(p)[:-3]).replace('’',"'") for p in ITEMNOTES}
fgconv.NAMES.update({'The Guardhouse':'Guardhouse (General Notes)','The Quarry':'Quarry (General Notes)','The Caverns':'Quarry: Cavern Level','Introduction':'Running A0 in 5e'})
C=lambda t: fgconv.conv(prep(t))
# ---------------------------------------------------------------- maps
src=os.path.join(WORK,'src'); os.makedirs(src,exist_ok=True)
for f in os.listdir(src): os.remove(os.path.join(src,f))
MAPS={}
for f in sorted(os.listdir(MAPDIR)):
    mm=re.match(r'A0 Map (\d) - (.*) - (GM|Player)\.png$',f)
    if not mm: continue
    k='map-a0-%s-%s'%(mm.group(1),re.sub(r'[^a-z0-9]+','-',mm.group(2).lower()).strip('-'))+('-player' if mm.group(3)=='Player' else '')
    shutil.copy(os.path.join(MAPDIR,f),os.path.join(src,k+'.png')); MAPS[k]=(mm.group(1),mm.group(2),mm.group(3))
m.images(src)
from PIL import Image
SIZE={k:Image.open(os.path.join(src,k+'.png')).size for k in MAPS}
for k,(n,title,ver) in MAPS.items():
    rec=m._cat('image').find(m.IMG[k][0]); rec.find('name').text='Map A0-%s — %s%s'%(n,title,' (Player)' if ver=='Player' else '')
    if n!='1':
        im=rec.find('image')
        for tg,v in (('grid','on'),('gridsize','50,50'),('gridoffset','0,0')):
            e=ET.Element(tg); e.text=v; im.insert(0,e)
MK={n:k for k,(n,_,v) in MAPS.items() if v=='GM'}; MP={n:k for k,(n,_,v) in MAPS.items() if v=='Player'}
# ---------------------------------------------------------------- spells (Cause Fear) before NPCs
sp=os.path.join(VAULT,'57-Spells','Converted','Cause Fear.md'); bt=body(sp).split('## Notes for the DM')[0]
bt=re.sub(r'^\s*# [^\n]*\n','',bt,count=1); f={k:v.strip() for k,v in re.findall(r'^- \*\*([A-Za-z ]+):\*\* (.*)$',bt,re.M)}
rules=re.sub(r'^- \*\*(Casting Time|Range|Components|Duration|Classes):\*\*.*\n','',bt,flags=re.M); rules=re.sub(r'^\*1st-level[^\n]*\*\n','',rules.lstrip(),count=1)
m.spell('causefear','Cause Fear',1,'Necromancy',False,f['Casting Time'],f['Range'],f['Components'],f['Duration'],'Cleric, Warlock, Wizard',
        C(rules)+'<p><i>Sidebar Press conversion of the 1e cleric spell (Greybeard, 2026-11-25).</i></p>')
CF_DESC='Level: 1\nCasting Time: 1 action\nComponents: V\nDuration: Concentration, up to 1 minute\nRange: 60 feet\nOne creature makes a Wisdom save or is frightened of you and must move away from you on its turns; it repeats the save at the end of each turn. See the Cause Fear spell record.\n'
fgtext.HOMEBREW=lambda nm: ('spell.causefear','Cause Fear',CF_DESC) if nm.lower()=='cause fear' else None
_srdx=ET.fromstring(zipfile.ZipFile(os.path.join(FG,'modules','DD5E SRD Data.mod')).read('client.xml'))
_srdsp={(e.findtext('name') or '').lower():e for e in next(x for x in _srdx.iter() if x.tag=='spelldata').iter() if e.find('name') is not None and e.find('level') is not None}
def spell_lookup(nm):
    if nm.lower()=='cause fear': return (1,CF_DESC)
    if nm.lower()=='friends': return (0,'Level: Cantrip\nCasting Time: 1 action\nComponents: S, M (a small amount of makeup)\nDuration: Concentration, up to 1 minute\nRange: Self\nAdvantage on Charisma checks directed at one creature that isn\'t hostile toward you. When the spell ends, the creature realizes it was influenced and becomes hostile. (PHB)\n')
    e=_srdsp[nm.lower()]; d=re.sub(r'\s*\n\s*','\n',re.sub(r'<[^>]+>','\n',ET.tostring(e.find('description'),encoding='unicode'))).strip()
    return (int(e.findtext('level')),'Level: %s\nCasting Time: %s\nComponents: %s\nDuration: %s\nRange: %s\n%s\n'%(e.findtext('level'),e.findtext('castingtime'),e.findtext('components'),e.findtext('duration'),e.findtext('range'),html.unescape(d)))
# ---------------------------------------------------------------- NPCs
BEST=os.path.join(ADV,'A0 - Bestiary (5e).md'); bst=open(BEST).read()
NOTES={os.path.basename(p)[:-3]:p for p in glob.glob(os.path.join(ADV,'NPCs','*.md'))}
def lore(name):
    sec=re.search(r'^### %s\n(.*?)(?=^### |\Z)'%re.escape(name),bst,re.S|re.M)
    if not sec: return ''
    t=re.sub(r'```text.*?```','',sec.group(1),flags=re.S)
    return C(t)
for blk in fgtext.blocks_md(bst):
    d=fgtext.parse(blk); k=slug(d['name'])
    fgtext.add(m,k,d,'<h>%s</h>%s<p><i>A0 Danger at Darkshelf Quarry, 5e conversion (Sidebar Press).</i></p>'%(html.escape(d['name']),lore(d['name'])))
for k in ('glyrthiel','clericoftheeye'): m.npc_spells(k,spell_lookup)
def mm(srd,name,key,dress): m.npc_srd(srd,name,key,dress=dress,keep_srd_text=False)
mm('worg','Worg','worg','Goblin worg-riders saddle a worg in 2 rounds.')
mm('ridinghorse','Riding Horse','ridinghorse','The quarry patrols\' light warhorses.')
mm('commoner','Commoner','commoner','Slaves who fight from fear use a club (1d4) or a pitchfork or stave (as a quarterstaff, 1d6). The free quarry workers carry picks (1d6) and fight only in self-defense.')
mm('bugbear','Bugbear','bugbear','The checkpoint guards of areas 51-53 thrust their spears (javelin line) through the bars.')
mm('bugbear','Snikscab','snikscab','Bugbear taskmaster (areas 20-21). Carries the keys to every manacle in the guardhouse. Hostage rule at 15 hp or fewer if Nubgrod is dead.')
mm('bugbear','Nubgrod','nubgrod','Bugbear taskmaster (areas 20-21), Snikscab\'s partner.')
mm('zombie','Zombie','zombie','Ordered to attack any living thing in area 60; they tolerate the ghouls.')
mm('ghoul','Ghoul','ghoul','They attack any living thing except the clerics of the Eye.')
mm('boar','Boar','boar','Random encounter (forest and river).')
mm('blackbear','Black Bear','blackbear','Random encounter (forest and river).')
mm('wolf','Wolf','wolf','Random encounter: 2-5 (2-3 for 4 PCs).')
mm('panther','Panther','panther','Random encounter (forest and river).')
assert not fgtext.MISSES,fgtext.MISSES
# ---------------------------------------------------------------- items (from each note's FGU Import block)
NUM={'Weight':'weight','AC Base':'ac','Bonus':'bonus'}; STR={'Non-Identified Name':'nonid_name','Damage':'damage','Properties':'properties','Cost':'cost'}
GMI=[]
for p in ITEMNOTES:
    raw=open(p).read(); blk=re.search(r'## FGU Import.*?```text\n(.*?)```',raw,re.S).group(1)
    f={}
    for l in blk.split('\n'):
        mm_=re.match(r'^([A-Za-z \-]+):\s?(.*)$',l)
        if mm_: f[mm_.group(1).strip()]=mm_.group(2).strip()
    kw={}
    for a,b in NUM.items():
        if f.get(a):
            try: kw[b]=float(f[a]) if '.' in f[a] else int(f[a])
            except ValueError: pass
    for a,b in STR.items():
        if f.get(a): kw[b]=f[a]
    sec=fgconv.sections(body(p)); key=slug(f['Name'])
    desc='<h>%s</h>%s%s'%(html.escape(f['Name']),C(sec.get('Properties','')),('<p><b>History. </b></p>'+C(sec['History'])) if sec.get('History') else '')
    m.item(key,f['Name'],f.get('Type',''),desc,subtype=f.get('Subtype',''),rarity=f.get('Rarity',''),**kw)
    GMI.append((key,f.get('DM Only','')))
# ---------------------------------------------------------------- encounters (4 PCs / 6 PCs)
G2,G3,G4,Q5,Q6,C7=MK['2'],MK['3'],MK['4'],MK['5'],MK['6'],MK['7']
ENC=[ # (area, name, {4:[...],6:[...]} or [...] for both, map)
('1','Entry: parapet guards, day',{4:[('guard',1)],6:[('guard',2)]},G2),('1','Entry: parapet goblins, night',{4:[('goblin',3)],6:[('goblin',4)]},G2),
('5','Conference ambush',{4:[('glyrthiel',1),('guard',3)],6:[('glyrthiel',1),('guard',4)]},G3),
('6','Barracks',{4:[('guard',4)],6:[('guard',6)]},G3),('10','Armory: the sergeant',[('sergeantoftheguard',1)],G3),
('12','Kitchen',{4:[('zodznog',1),('commoner',3)],6:[('zodznog',1),('commoner',4)]},G3),
('17','North guardposts, day',{4:[('guard',1)],6:[('guard',2)]},G2),('17','North guardposts, night',{4:[('goblin',3)],6:[('goblin',4)]},G2),
('18','Glyrthiel',[('glyrthiel',1)],G2),('19','Brubgrok',[('brubgrok',1)],G2),('20','The taskmasters',[('snikscab',1),('nubgrod',1)],G2),
('22','South guardpost, day',{4:[('guard',1)],6:[('guard',2)]},G2),('22','South guardpost, night',{4:[('goblin',3)],6:[('goblin',4)]},G2),
('24','Stable',{4:[('uzgrod',1),('commoner',4)],6:[('uzgrod',1),('commoner',6)]},G4),
('27','Smithy',{4:[('wartslag',1),('goblin',1)],6:[('wartslag',1),('goblin',2)]},G4),
('28','Stair guardpost',{4:[('goblin',1),('worg',1)],6:[('goblin',2),('worg',1)]},G4),
('30','Goblin den, night',{4:[('goblin',5)],6:[('goblin',8)]},G4),('30','Goblin den, day',{4:[('goblin',3)],6:[('goblin',4)]},G4),
('31','Goblin barracks, day',{4:[('goblin',5)],6:[('goblin',8)]},G4),('31','Goblin barracks, night',{4:[('goblin',3)],6:[('goblin',4)]},G4),
('32','Worg den',[('worg',2)],G4),
('34','Main gallery, day',{4:[('guard',1)],6:[('guard',2)]},Q5),('34','Main gallery, night',{4:[('goblin',3)],6:[('goblin',4)]},Q5),
('36','Off-duty guards, day (goblins)',{4:[('goblin',3)],6:[('goblin',4)]},Q5),('36','Off-duty guards, night',{4:[('guard',1)],6:[('guard',2)]},Q5),
('39','Digging team, night',{4:[('goblin',3)],6:[('goblin',5)]},Q5),
('41','Lower tunnel diggers',{4:[('goblin',3)],6:[('goblin',5)]},Q6),
('42','Elemental Temple',[('clericoftheeye',1),('youngmudtiger',2)],Q6),('42','Temple alarm: reinforcements',{4:[('clericoftheeye',1),('goblin',4)],6:[('clericoftheeye',1),('goblin',6)]},Q6),
('43','Temple guardpost',{4:[('goblin',4)],6:[('goblin',6)]},Q6),
('46','Goblin barracks, day',{4:[('goblin',7)],6:[('goblin',10)]},Q6),('46','Goblin barracks, night',{4:[('goblin',3)],6:[('goblin',4)]},Q6),
('47','Old diggings',{4:[('goblin',3)],6:[('goblin',4)]},Q6),('51','Checkpoint bugbears (51-52)',[('bugbear',2)],Q6),
('55','Water weird',[('waterweird',1)],C7),('56','Beach mudtigers',[('mudtiger',2)],C7),
('58','Troglodytes (58-59)',{4:[('troglodyte',2)],6:[('troglodyte',3)]},C7),('60','Zombies',{4:[('zombie',3)],6:[('zombie',4)]},C7),
('62','Ghouls',[('ghoul',2)],C7),('63','Mudtiger nursery',[('troglodyte',1),('youngmudtiger',1)],C7),
('64','Breeding pool',[('greatmudtiger',1),('troglodyte',2),('clericoftheeye',1)],C7),('66','Killer frogs',{4:[('killerfrog',5)],6:[('killerfrog',8)]},C7),
('R','Random: wild boar',[('boar',1)],None),('R','Random: black bear',[('blackbear',1)],None),('R','Random: wolves',{4:[('wolf',2)],6:[('wolf',4)]},None),
('R','Random: panther',[('panther',1)],None),('R','Random: huge spider',[('hugespider',1)],None),('R','Random: mudtiger (river)',[('mudtiger',1)],None),
('R','Random: ghouls',{4:[('ghoul',1)],6:[('ghoul',2)]},None),('R','Random: patrol of guards',{4:[('guard',2),('ridinghorse',2)],6:[('guard',4),('ridinghorse',4)]},None),
('R','Random: worg-riders',{4:[('goblin',1),('worg',1)],6:[('goblin',2),('worg',2)]},None),
]
ENCBY={}; n=0
for area,nm,cr,mp in ENC:
    n+=1; base='E%02d'%n
    if isinstance(cr,dict):
        for band,sfx in ((4,'a'),(6,'b')):
            m.battle(base+sfx,'%s%s (%d PCs)'%(('' if area=='R' else 'Area %s: '%area),nm,band),cr[band],mp); ENCBY.setdefault(area,[]).append(base+sfx)
    else:
        m.battle(base,'%s%s'%(('' if area=='R' else 'Area %s: '%area),nm),cr,mp); ENCBY.setdefault(area,[]).append(base)
# ---------------------------------------------------------------- reference manual
def split_h2(t):
    parts=re.split(r'(?m)^## (.+)$',t); return parts[0],[(parts[i].strip(),parts[i+1]) for i in range(1,len(parts),2)]
PAGEOF={}
def npclinks(txt):
    out=[]
    for k in m.NPC:
        nm=m.npcname(k)
        if re.search(r'\[\[(?:A0 - Bestiary \(5e\)#)?%s(?:\||\]\])'%re.escape(nm),txt) and m.N(k) not in out: out.append(m.N(k))
    return out
def itemlinks(txt): return [m.IT(slug(fgconv.NAMES[os.path.basename(p)[:-3]])) for p in ITEMNOTES if '[['+os.path.basename(p)[:-3] in txt]
def area_pages(sec,t,levelmap):
    pre,h2=split_h2(t)
    for j,(title,txt) in enumerate(h2):
        parts=re.split(r'(?m)^### (\d+\. .+)$',txt)
        lead=((pre.strip()+'\n\n') if j==0 and pre.strip() else '')+parts[0].strip()
        imgs=[]
        for lv,(gm,pl) in levelmap.items():
            if title==lv: imgs=[gm,pl]
        links=[m.I(i) for i in imgs]+npclinks(lead)+itemlinks(lead)
        m.page(sec,title,C('## '+title+'\n\n'+lead) if lead else '<h>%s</h>'%html.escape(title),images=imgs,links=links,place={i:'$end' for i in imgs})
        for i in range(1,len(parts),2):
            at=parts[i].strip(); body_=parts[i+1]; num=at.split('.')[0]
            links=[m.B(c) for c in ENCBY.get(num,[])]
            ln=[]
            for a_,nm_,cr_,_ in [x for x in ENC if x[0]==num]:
                for k,_c in (cr_[6] if isinstance(cr_,dict) else cr_):
                    if m.N(k) not in ln: ln.append(m.N(k))
            for x in npclinks(body_):
                if x not in ln: ln.append(x)
            links+=ln+itemlinks(body_)+([m.SP('causefear')] if 'cause fear' in body_.lower() else [])
            m.page(sec,at,C('## '+at+'\n'+body_),links=links); PAGEOF[num]='reference.refmanualdata.'+ids(len(m.pages))
# Introduction
intro=body(os.path.join(ADV,'A0-00 Introduction.md')); pre,h2=split_h2(re.sub(r'^\s*# [^\n]*\n','',intro,count=1))
ALLMAPS=[MK[x] for x in sorted(MK)]+[MP[x] for x in sorted(MP)]
m.page('Introduction','Using This Module',C(pre)+C('''This book holds the whole adventure: the introduction and background, then one page per keyed area in Part 1 (the Guardhouse), Part 2 (the Quarry) and Part 3 (the Caverns), the conclusion, and appendices for the bestiary, the people of the quarry and the magic items. Each area page ends with its encounters (a **4 PCs** and a **6 PCs** version where the numbers change) and creatures.

The GM maps carry a pin on every area number; double-click a pin to open the area's page. Share the **(Player)** maps, which have the area numbers, the captions that give away connections, and the secret doors painted out. The level maps use a 5-ft grid set to 50 px; the quarry overview is not to scale. These are cleaned scans of the 2013 maps; traced Sidebar Press maps will replace them in a later edition.

**Credits.** *A0 Danger at Darkshelf Quarry* by Skip Williams, from *Against the Slave Lords* (Wizards of the Coast, 2013). Cartography by Mike Schley. 5e conversion by Sidebar Press for private and ARPG table use only; not for sale or distribution. Creature statistics marked SRD: System Reference Document 5.1 (CC-BY-4.0).'''),links=[m.I(k) for k in ALLMAPS])
for title,txt in h2:
    if title in ('Credits',): continue
    imgs=[MK['1']] if title=='Maps' else []
    links=npclinks(txt)+itemlinks(txt)+([m.SP('causefear')] if 'Cause Fear' in txt else [])
    if title=='Maps': links=[m.I(k) for k in ALLMAPS]
    if title=='Darkshelf and Environs': links+=[m.B(c) for c in ENCBY['R']]
    m.page('Introduction',title,C('## '+title+'\n'+txt),images=imgs,links=links,place={i:'$end' for i in imgs})
tb='<table><tr><td><b>Code</b></td><td><b>Encounter</b></td><td><b>XP</b></td></tr>'+''.join('<tr><td>%s</td><td>%s</td><td>%d</td></tr>'%(c,html.escape(m.BATN[c]),int(m._cat('battle').find(m.BAT[c].split('.')[1]).findtext('exp'))) for c in m.BAT)+'</table>'
m.page('Introduction','Encounters','<h>Encounters</h><p>Every encounter in the module, with its total (unadjusted) XP. Area encounters have a 4-PC and a 6-PC version where the numbers change; random encounters are listed last.</p>'+tb,links=[m.B(c) for c in m.BAT])
tb='<table><tr><td><b>Item</b></td><td><b>Where</b></td></tr>'+''.join('<tr><td>%s</td><td>%s</td></tr>'%(html.escape(m.ITEMN[k]),html.escape(g)) for k,g in GMI)+'</table>'
m.page('Introduction','Magic Items and Treasure — GM Notes',tb,links=[m.IT(k) for k,_ in GMI])
LV={'Guardhouse: Main Level':(MK['3'],MP['3']),'Guardhouse: Upper Level':(MK['2'],MP['2']),'Guardhouse: Lower Level':(MK['4'],MP['4']),
    'Quarry: Main Level':(MK['5'],MP['5']),'Quarry: Lower Level':(MK['6'],MP['6']),'Quarry: Cavern Level':(MK['7'],MP['7'])}
for sec,f in (('Part 1: The Guardhouse','A0-01 The Guardhouse.md'),('Part 2: The Quarry','A0-02 The Quarry.md'),('Part 3: The Caverns','A0-03 The Caverns.md')):
    t=re.sub(r'^\s*# [^\n]*\n','',body(os.path.join(ADV,f)),count=1)
    area_pages(sec,t,LV)
con=re.sub(r'^\s*# [^\n]*\n','',body(os.path.join(ADV,'A0-04 Concluding the Adventure.md')),count=1)
pre,h2=split_h2(con)
m.page('Conclusion','Concluding the Adventure',C('## Concluding the Adventure\n'+pre),links=npclinks(pre))
for title,txt in h2: m.page('Conclusion',title,C('## '+title+'\n'+txt),links=npclinks(txt))
# Appendices: bestiary, people, items
bi=re.sub(r'```text.*?```','',bst,flags=re.S); bi=re.sub(r'^---.*?\n---\n','',bi,flags=re.S); bi=re.sub(r'^\s*# [^\n]*\n','',bi,count=1)
bpre,bh2=split_h2(bi)
m.page('Appendix: Bestiary','Bestiary',C(bpre)+C('## Quick index\n'+dict(bh2)['Quick index']),links=[m.N(k) for k in m.NPC])
m.page('Appendix: Bestiary','Monster Manual Creatures',C(dict(bh2)['MM creatures']),links=[m.N(k) for k in ('worg','ridinghorse','commoner','bugbear','snikscab','nubgrod','zombie','ghoul','boar','blackbear','wolf','panther')])
mt=dict(bh2)['Custom statblocks']; mud=re.search(r'\*\*Mudtiger fingerlings\*\*.*?(?=^### )',mt,re.S|re.M).group(0)
m.page('Appendix: Bestiary','Mudtigers','<h>Mudtigers</h>'+C(mud),links=[m.N('youngmudtiger'),m.N('mudtiger'),m.N('greatmudtiger')])
for nm_,p in sorted(NOTES.items()):
    t=re.sub(r'^\s*# [^\n]*\n','',body(p),count=1); t=t.split('## Canon Notes')[0]+'## Continuity'+t.split('## Continuity')[1] if '## Continuity' in t else t
    ln=[]
    sb=re.search(r'#([^\]]+)\]\]',fgconv.sections(body(p)).get('Stat Block','') )
    if sb:
        k=slug(sb.group(1)); k={'bugbear':slug(nm_) if nm_ in ('Snikscab','Nubgrod') else 'bugbear'}.get(k,k)
        if k in m.NPC: ln.append(m.N(k))
    ln+=itemlinks(t)
    m.page('Appendix: People of the Quarry',nm_,C('## '+nm_+'\n'+t),links=ln)
m.page('Appendix: Magic Items','Magic Items','<h>Magic Items</h><p>Click a name to open the item record, which you can drag to a character sheet.</p>'+''.join('<p><b>%s.</b> %s</p>'%(html.escape(m.ITEMN[k]),html.escape(g)) for k,g in GMI),links=[m.IT(k) for k,_ in GMI]+[m.SP('causefear')])
# ---------------------------------------------------------------- map pins -> area pages (FG image coordinates: origin at centre, y up)
PINS=json.load(open(os.path.join(HERE,'pins.json')))
for title,lab in PINS.items():
    n=title.split(' ')[0].split('-')[1]; k=MK[n]; W,H=SIZE[k]
    im=m._cat('image').find(m.IMG[k][0]).find('image'); ly=im.find('layers'); lid=10
    for area,pts in sorted(lab.items(),key=lambda kv:int(kv[0])):
        if area not in PAGEOF: print('no page for pin',area); continue
        for (x,y) in pts:
            lid+=1; L=_S(ly,'layer'); _S(L,'name',None,'Area %s'%area); _S(L,'id',None,lid); _S(L,'parentid',None,-1); _S(L,'type',None,'shortcut')
            sc=_S(L,'shortcut'); _S(sc,'class',None,'referencemanualpage'); _S(sc,'record',None,PAGEOF[area])
            _S(L,'matrix',None,'1,0,0,0,0,1,0,0,0,0,1,0,%d,%d,0,1'%(x-W//2,H//2-y))
# ---------------------------------------------------------------- build
m.LINT=[r'A0-0\d',r'Bestiary \(5e\)',r'\(A0\)',r'Conversion Ledger']
out=os.path.join(WORK,NAME+'.mod')
m.build(out,cover_image=MK['1'])
if '--test' in sys.argv: sys.exit(0)
KIT=os.path.join(ADV,'FGU Kit'); os.makedirs(KIT,exist_ok=True); shutil.copyfile(out,os.path.join(KIT,NAME+'.mod'))
if '--install' in sys.argv: shutil.copyfile(out,os.path.join(FG,'modules',NAME+'.mod')); print('installed to FG modules')
