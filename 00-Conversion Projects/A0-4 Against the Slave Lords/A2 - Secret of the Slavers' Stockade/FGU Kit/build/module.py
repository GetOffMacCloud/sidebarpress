"""A2 Secret of the Slavers' Stockade (5e conversion) -> Fantasy Grounds Unity module.
Reads the vault notes in this adventure folder (site keys, Bestiary, NPCs, Items, Pregens), the Cause Fear spell note,
and the cleaned map renders in Maps/A2 (pins.json from the render script). Uses the shared builder in 70-Company/Tools/fgu-module-builder; pregens.py
builds the nine tournament characters as FG pregenerated character sheets.
Run:  FG_DIR="$HOME/mnt/Fantasy Grounds" FG_WORK="$HOME/fgwork" python3 module.py [--test|--install]"""
import os,sys,re,glob,shutil,html,json,zipfile
import xml.etree.ElementTree as ET
HERE=os.path.dirname(os.path.abspath(__file__)); ADV=os.path.dirname(os.path.dirname(HERE)); PROJ=os.path.dirname(ADV); VAULT=PROJ
while not os.path.isdir(os.path.join(VAULT,'70-Company')): VAULT=os.path.dirname(VAULT)
sys.path.insert(0,os.path.join(VAULT,'70-Company','Tools','fgu-module-builder')); sys.path.insert(0,HERE)
import fgmod,fgconv,fgtext,pregens
from fgmod import Mod,_S,_FT,_WR,ids
FG=os.environ.get('FG_DIR',os.path.expanduser('~/mnt/Fantasy Grounds'))
NAME="A2 - Secret of the Slavers' Stockade"; DISPLAY="A2 Secret of the Slavers' Stockade (5E)"
WORK=os.path.join(os.path.expanduser(os.environ.get('FG_WORK','~/fgwork')),'A2'); os.makedirs(WORK,exist_ok=True)
MAPDIR=os.path.join(PROJ,'Maps','A2')
m=Mod(NAME,DISPLAY,'Sidebar Press Conversions','Sidebar Press',FG,WORK)
slug=lambda x: re.sub(r'[^a-z0-9]','',x.lower())
def body(p):
    t=open(p).read()
    return t.split('\n---',1)[1].split('\n',1)[1] if t.startswith('---') else t
# ---------------------------------------------------------------- wikilinks: vault notes -> module records/pages
def prep(t):
    t=re.sub(r'\[\[A[012] - 5e Conversion Ledger\]\]( §\d+)?','the Sidebar Press conversion ledger',t)
    t=re.sub(r'\[\[A2 - Bestiary \(5e\)#([^\]|]+)(\|[^\]]*)?\]\]',lambda x:'[[%s%s]]'%(x.group(1),x.group(2) or ''),t)
    t=re.sub(r'\[\[A2 - Bestiary \(5e\)\]\]','[[Bestiary]]',t)
    t=re.sub(r'\[\[A2-0\d [^\]#|]*#([^\]|]+)(\|[^\]]*)?\]\]',lambda x:'[[%s%s]]'%(x.group(1),x.group(2) or ''),t)
    t=re.sub(r'\[\[A2-0\d ([^\]|]+)(\|[^\]]*)?\]\]',lambda x:'[[%s%s]]'%(x.group(1),x.group(2) or ''),t)
    return t
ITEMNOTES=sorted(glob.glob(os.path.join(ADV,'Items','*.md')))
PREGEN=sorted(glob.glob(os.path.join(PROJ,'A1 - Slave Pits of the Undercity','Pregens','*.md')))   # same nine characters as A1
fgconv.NAMES={os.path.basename(p)[:-3]:re.sub(r' \(A2\)$','',os.path.basename(p)[:-3]).replace('’',"'") for p in ITEMNOTES}
fgconv.NAMES.update({'The Hill Fort':'Key to the Hill Fort','The Dungeon':'Key to the Dungeon','Introduction':'Running A2 in 5e','Convention Mode':'The Tournament','Ogre':'"Ogre"'})
C=lambda t: fgconv.conv(prep(t))
# ---------------------------------------------------------------- maps (1 fort, 2 curtain wall and gatehouse floors, 3 F34, 4 dungeon; 5 tournament tactical maps, GM only)
src=os.path.join(WORK,'src'); os.makedirs(src,exist_ok=True)
for f in os.listdir(src): os.remove(os.path.join(src,f))
MAPS={}
for f in sorted(os.listdir(MAPDIR)):
    mm=re.match(r'A2 Map (\d) - (.*) - (GM|Player)\.png$',f)
    if not mm: continue
    k='map-a2-%s-%s'%(mm.group(1),re.sub(r'[^a-z0-9]+','-',mm.group(2).lower()).strip('-'))+('-player' if mm.group(3)=='Player' else '')
    shutil.copy(os.path.join(MAPDIR,f),os.path.join(src,k+'.png')); MAPS[k]=(mm.group(1),mm.group(2),mm.group(3))
m.images(src)
from PIL import Image
SIZE={k:Image.open(os.path.join(src,k+'.png')).size for k in MAPS}
for k,(n,title,ver) in MAPS.items():
    rec=m._cat('image').find(m.IMG[k][0]); rec.find('name').text='Map A2-%s — %s%s'%(n,title,' (Player)' if ver=='Player' else '')
    if n in ('1','2','3','4'):
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
SRDSP={(e.findtext('name') or '').lower():e for e in next(x for x in _srdx.iter() if x.tag=='spelldata').iter() if e.find('name') is not None and e.find('level') is not None}
def spell_lookup(nm):
    if nm.lower()=='cause fear': return (1,CF_DESC)
    e=SRDSP[nm.lower()]; d=re.sub(r'\s*\n\s*','\n',re.sub(r'<[^>]+>','\n',ET.tostring(e.find('description'),encoding='unicode'))).strip()
    return (int(e.findtext('level')),'Level: %s\nCasting Time: %s\nComponents: %s\nDuration: %s\nRange: %s\n%s\n'%(e.findtext('level'),e.findtext('castingtime'),e.findtext('components'),e.findtext('duration'),e.findtext('range'),html.unescape(d)))
# ---------------------------------------------------------------- NPCs
BEST=os.path.join(ADV,'A2 - Bestiary (5e).md'); bst=open(BEST).read()
NOTES={os.path.basename(p)[:-3]:p for p in glob.glob(os.path.join(ADV,'NPCs','*.md'))}
def lore(name):
    sec=re.search(r'^### %s\n(.*?)(?=^### |^## |\Z)'%re.escape(name),bst,re.S|re.M)
    if not sec: return ''
    return C(re.sub(r'```text.*?```','',sec.group(1),flags=re.S))
LORE=dict(re.findall(r'^\*\*(Boggles|Cloakers|Haunts|Phantoms|Cavelings)\*\* (.*)$',bst,re.M))
LOREFOR={'Boggle':'Boggles','Baby Boggle':'Boggles','Cloaker':'Cloakers','Haunt':'Haunts','Caveling':'Cavelings','Caveling Brute':'Cavelings','Cari':'Cavelings','Filch':'Cavelings'}
for blk in fgtext.blocks_md(bst):
    d=fgtext.parse(blk); k=slug(d['name']); extra=''
    if d['name'] in LOREFOR: lf=LOREFOR[d['name']]; extra=C('**%s** %s'%(lf,LORE[lf]))
    fgtext.add(m,k,d,'<h>%s</h>%s%s<p><i>A2 Secret of the Slavers\' Stockade, 5e conversion (Sidebar Press).</i></p>'%(html.escape(d['name']),lore(d['name']),extra))
for k in ('markessa','markessasdouble','gulyet','adhunazaryet','drowmerchant','drowguardcaptain','drowguard'): m.npc_spells(k,spell_lookup)
def mm(srd,name,key,dress): m.npc_srd(srd,name,key,dress=dress,keep_srd_text=False)
MMDRESS={}
mmsec=bst.split('## MM creatures')[1].split('## Hazards')[0]
for nm_,txt in re.findall(r'^### ([^\n]+)\n(\*\*.*?)(?=^### |\Z)',mmsec,re.S|re.M):
    txt=re.sub(r'\[\[([^\]|]*?)(?: \(A2\))?\]\]',r'\1',txt)
    t2=re.sub(r'\[\[[^\]|]*\|([^\]]*)\]\]',r'\1',re.sub(r'^\*\*[^*]+\*\* \([^)]*\)\.?\s*','',txt.strip())).replace('*','').strip()
    t2=re.sub(r'^, named ([^.]+)\.\s*',r'Named \1 in this adventure. ',t2)
    MMDRESS[nm_]=t2 or 'As the Monster Manual.'
# name -> SRD tag (key = slug(name))
SRDK={'Hobgoblin':'hobgoblin','Goblin':'goblin','Kobold':'kobold','Orc':'orc','Thug':'thug','Commoner':'commoner','Veteran':'veteran','Ankheg':'ankheg',
 'Wereboar':'wereboar','Boar':'boar','Medusa':'medusa','Madman':'berserker','Winter Wolf':'winterwolf','Werewolf':'werewolf','Owlbear':'owlbear','Minotaur':'minotaur',
 'Worg':'worg','Wolf':'wolf','Giant Spider':'giantspider','Bugbear':'bugbear','Gnoll':'gnoll','Blackthorn':'oni','Oni':'oni','Mastiff':'mastiff','Giant Rat':'giantrat',
 'Draft Horse':'drafthorse','Warhorse':'warhorse','Riding Horse':'ridinghorse','Poisonous Snake':'poisonoussnake','Badger':'badger','Brown Bear':'brownbear',
 'Jackal':'jackal','Hill Giant':'hillgiant','Ghoul':'ghoul','Griffon':'griffon','Ogre':'ogre','Elk':'elk','Wight':'wight','Giant Fire Beetle':'giantfirebeetle',
 'Giant Centipede':'giantcentipede','Giant Wolf Spider':'giantwolfspider','Giant Lizard':'giantlizard'}
for nm_,tag in SRDK.items(): mm(tag,nm_,slug(nm_),MMDRESS.get(nm_,'As the Monster Manual.'))
assert not fgtext.MISSES,fgtext.MISSES
# ---------------------------------------------------------------- items (from each note's FGU Import block)
NUM={'Weight':'weight','AC Base':'ac','Bonus':'bonus'}; STR={'Non-Identified Name':'nonid_name','Damage':'damage','Properties':'properties','Cost':'cost'}
GMI=[]; NOTEKEY={}
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
    props=sec.get('Properties','')
    props=re.sub(r'(?m)^- \*\*(Curse|Which pearls are cursed)[^\n]*\n?','',props); props=re.sub(r'(?m)^\*\*This pearl[^\n]*\n?','',props)  # the curse stays GM-only
    desc='<h>%s</h>%s'%(html.escape(f['Name']),C(props))
    m.item(key,f['Name'],f.get('Type',''),desc,subtype=f.get('Subtype',''),rarity=f.get('Rarity',''),**kw)
    GMI.append((key,f.get('DM Only',''))); NOTEKEY[os.path.basename(p)[:-3]]=key; fgconv.NAMES[os.path.basename(p)[:-3]]=f['Name']
# ---------------------------------------------------------------- encounters (6 PCs as printed; 4 PCs = 2/3 of every group of two or more)
K=lambda n:{'Gorbin':'gorbinstalworth'}.get(n,slug(n))
def four(c): return {k:(v if v==1 else max(1,round(v*2/3))) for k,v in c.items()}
F1,F2,F3,DN,TAC=MK['1'],MK['2'],MK['3'],MK['4'],MK['5']
ENC=[ # (area, name, {creature: count for 6 PCs}, map)
('F1','Walltop pairs',{'Hobgoblin':4},F2),
('F2','Jon the haunt',{'Haunt':1},F2),
('F5','The ankheg in the mud',{'Ankheg':1},F1),
('F8','Gatehouse barracks (F8b)',{'Hobgoblin':22,'Hobgoblin Sergeant':2},F2),
('F8','Gorbin and Kairn (F8c)',{'Gorbin':1,'Kairn':1},F2),
('F9','Gatehouse third floor',{'Hobgoblin':11,'Hobgoblin Sergeant':1},F2),
('F11','The wandering patrol',{'Hobgoblin':12,'Hobgoblin Sergeant':1},F1),
('F13','Garden ambush',{'Hobgoblin':12,'Carnivorous Ape':4},F1),
('F16','The madman',{'Madman':1},F1),
('F19','The mirror corridor',{'Hobgoblin':9,'Hobgoblin Sub-Chief':1},F1),
('F25','The cloaker',{'Cloaker':1},F1),
('F31','Estelrath and his cavelings',{'Veteran':1,'Cari':1,'Filch':1},F1),
('F32','Executioner',{'Executioner':1},F1),
('F33','The pit fight crowd',{'Goblin':8,'Kobold':10},F1),
('F34','The guard tower',{'Hobgoblin':20,'Hobgoblin Sergeant':2},F3),
('F35','Kitchen ambush, wave 1: axes and boars',{'Wereboar':3,'Hobgoblin':8},F1),
('F35','Kitchen ambush, wave 2: Icar',{'Icar':1},F1),
('F39','The chained medusa',{'Medusa':1},F1),
('D1','Goblin guards',{'Goblin':12,'Hobgoblin':1},DN),
('D4','Spiders over the arches',{'Giant Spider':2},DN),
('D8','Boggles',{'Boggle':2},DN),
('D12','Torture chamber',{'Goblin':16,'Bugbear':2,'Worg':3},DN),
('D18','Goblin lancers',{'Goblin Lancer':9,'Goblin Captain':1,'Worg':9},DN),
('D19','Worg females',{'Wolf':4},DN),
('D21','Watch-worgs',{'Worg':2},DN),
('D22','Laboratory, wave 1: the archers',{'Elite Goblin':13},DN),
('D22','Laboratory, wave 2: owlbears and Markessa',{'Owlbear':2,'Markessa':1},DN),
('D25','The werewolves (D25e)',{'Werewolf':3},DN),
('D25','Blackthorn (D25f)',{'Blackthorn':1},DN),
('D26','The Ear-biters',{'Goblin':12},DN),
('D28','Overseers (D28v)',{'Hobgoblin':5,'Gnoll':2},DN),
('D29','Gulyet and her wolf',{'Gulyet':1,'Winter Wolf':1},DN),
('D30','Corridor guards',{'Gnoll Guard':2},DN),
('D30','Markessa\'s double (D30a)',{"Markessa's Double":1},DN),
('D31','The bodyguard',{'Elf Bodyguard':1},DN),
('D33','The minotaur',{'Minotaur':1},DN),
('D34','The slithering tracker',{'Slithering Tracker':1},DN),
('D35','Markessa at bay',{'Markessa':1},DN),
('D38','The drow caravan',{'Drow Merchant':1,'Drow Guard Captain':1,'Drow Guard':6},DN),
('D39','Exit guards',{'Hobgoblin':7},DN),
]
for _,_,c,_ in ENC:
    for n_ in c: assert K(n_) in m.NPC,n_
ENCBY={}; n=0
for area,nm,c,mp in ENC:
    n+=1; base='E%02d'%n; c4=four(c)
    if c4!=c:
        for band,cc,sfx in ((4,c4,'a'),(6,c,'b')):
            m.battle(base+sfx,'%s: %s (%d PCs)'%(area,nm,band),[(K(k),v) for k,v in cc.items()],mp); ENCBY.setdefault(area,[]).append(base+sfx)
    else:
        m.battle(base,'%s: %s'%(area,nm),[(K(k),v) for k,v in c.items()],mp); ENCBY.setdefault(area,[]).append(base)
RANDBY={}
TAB={}; TABN={}; TABG={}
def table(key,name,group,label,rows,cols=1,notes=''):
    """rows: [(from,to,[(text,(class,rec) or None), ...])]"""
    c=m._cat('tables'); tid=ids(len(c)+1); e=_S(c,tid)
    _S(e,'dice','dice',''); _S(e,'hiderollresults','number',0)
    for i,l in enumerate(label if isinstance(label,list) else [label],1): _S(e,'labelcol%d'%i,'string',l)
    _S(e,'mod','number',0); _S(e,'name','string',name); _S(e,'output','string','encounter'); _S(e,'resultscols','number',cols); _S(e,'table_positionoffset','number',0)
    if notes: _FT(e,'notes','<p>%s</p>'%html.escape(notes))
    R=_S(e,'tablerows')
    for i,(fr,to,cells) in enumerate(rows,1):
        r=_S(R,ids(i)); _S(r,'fromrange','number',fr); res=_S(r,'results')
        for j,(txt,lk) in enumerate(cells,1):
            x=_S(res,ids(j)); _S(x,'result','string',txt); w=_S(x,'resultlink','windowreference')
            _S(w,'class',None,lk[0] if lk else ''); _S(w,'recordname',None,lk[1] if lk else '')
        _S(r,'torange','number',to if to!=fr else 0)
    TAB[key]='tables.'+tid; TABN[key]=name; TABG.setdefault(group,[]).append(key)
TL=lambda g:[('table',TAB[k],'Table: '+TABN[k]) for k in TABG.get(g,[])]
for b in (4,6):
    s_=lambda six,four: six if b==6 else four
    def N(k,six,four=None):
        ex=s_(six,four if four is not None else six)
        return ('[%sx] %s'%(ex,m.npcname(k)) if ex!='1' else m.npcname(k),('npc',m.NPC[k]))
    P='(%d PCs)'%b; X=lambda n:'%s %s'%(n,P)
    table('wild%d'%b,X('A2 Wilderness Encounters'),'wild','Creatures',[
        (1,3,[N('brownbear','1d4','1d3')]),(4,11,[N('bugbear','2d4','1d4+1')]),(12,14,[N('boar','1d8','1d6')]),(15,17,[N('jackal','3d4','2d4')]),
        (18,21,[N('hillgiant','1d3','1')]),(22,25,[N('ghoul','1d6','1d4')]),(26,33,[N('gnoll','3d4','2d4')]),(34,45,[N('goblin','5d6','3d6')]),
        (46,48,[N('griffon','1d3','1d2')]),(49,60,[N('hobgoblin','4d6','3d6')]),(61,63,[N('ridinghorse','2d6','1d6+1')]),(64,66,[N('wereboar','1d2','1')]),
        (67,69,[N('werewolf','1d3','1d2')]),(70,75,[N('ogre','1d6','1d4')]),(76,77,[N('oni','1')]),(78,89,[N('orc','3d6','2d6')]),
        (90,92,[N('elk','2d4','1d4+1')]),(93,95,[N('wight','1d3','1d2')]),(96,100,[N('wolf','2d6','1d6+1')])],
        notes='Check three times a day: a 1 on a d12 in the plains, a 1 on a d10 in the hills. Encounter distance 6d4 x 10 feet. Hill giants, griffons and ogre magi in numbers are past Deadly for 5th level: roll again or let them pass at a distance.')
    table('fort%d'%b,X('A2 Hill Fort Encounters'),'fort',['Creatures','Also'],[
        (1,1,[N('hobgoblin','3d4','2d4'),N('hobgoblinsergeant','1')]),
        (2,2,[N('adhunazaryet','1'),N('hobgoblin','2d4','1d4+1')]),
        (3,3,[N('mastiff','2d4','1d4+1')]),(4,4,[N('carnivorousape','1d3','1d2')]),
        (5,5,[N('gnoll','2d6','1d6+1'),N('gnollguard','1')]),
        (6,6,[('An escaped slave: "Lady Morwin Elissar"',('npc',m.NPC['commoner'])),('',None)])],cols=2,
        notes='Campaign play only. Check every 10 minutes in hallways, empty rooms and cleared areas (never in the haunt\'s area or the haunted west wing): an encounter on a 1 on a d6.')
    table('dun%d'%b,X('A2 Dungeon Encounters'),'dun',['Creatures','Also'],[
        (1,1,[N('giantrat','4d6','3d6'),('and a rat leader (a giant rat with 7 hp)',None)]),
        (2,2,[N('babyboggle','1'),('',None)]),
        (3,3,[N('goblin','1d10+5','1d6+3'),N('hobgoblin','1')]),
        (4,4,[N('gulyet','1'),N('goblin','3d4','2d4')]),
        (5,5,[N('wolf','1d3','1d2'),('',None)]),
        (6,6,[N('haunt','1'),('',None)])],cols=2,
        notes='Campaign play only, in corridors and empty or emptied rooms. Check every 10 minutes: an encounter on a 1 on a d6. Gulyet\'s winter wolf arrives 2 rounds after she blows her whistle.')
table('cave','A2 Cave Encounters','cave','Encounter',[
    (1,1,[('A caveling (the DM\'s creation)',('npc',m.NPC['caveling']))]),(2,2,[('Lost, or a dead end',None)]),
    (3,3,[('A cave beetle',('npc',m.NPC['giantfirebeetle']))]),(4,4,[('A pit fall (DC 12 Wisdom (Perception) to notice; 1d4 bludgeoning damage)',None)]),
    (5,5,[('Dripping water (drinkable on 1-4 on a d6)',None)]),(6,6,[('[1d4+1x] Giant Rat',('npc',m.NPC['giantrat']))]),
    (7,7,[('[1d4x] Giant Centipede',('npc',m.NPC['giantcentipede']))]),(8,8,[('A sound (it may lead to an encounter or a trap)',None)]),
    (9,9,[('Fungus (edible on 1-2 on a d6)',None)]),(10,10,[('Stone chips (usable as tools or weapons)',None)]),
    (11,11,[('[1d2x] Giant Wolf Spider',('npc',m.NPC['giantwolfspider']))]),(12,12,[('A cave lizard',('npc',m.NPC['giantlizard']))])],
    notes='In the caves beyond D28c. Check every 20 minutes of travel: an encounter on a 1 on a d10. Same for 4 or 6 PCs.')
# ---------------------------------------------------------------- reference manual
def split_h2(t):
    parts=re.split(r'(?m)^## (.+)$',t); return parts[0],[(parts[i].strip(),parts[i+1]) for i in range(1,len(parts),2)]
PAGEOF={}
def npclinks(txt):
    out=[]
    for k in m.NPC:
        nm=m.npcname(k)
        if re.search(r'\[\[(?:A2 - Bestiary \(5e\)#)?%s(?:\||\]\])'%re.escape(nm),txt) and m.N(k) not in out: out.append(m.N(k))
    return out
def itemlinks(txt): return [m.IT(NOTEKEY[os.path.basename(p)[:-3]]) for p in ITEMNOTES if '[['+os.path.basename(p)[:-3] in txt]
CF=lambda t:[m.SP('causefear')] if 'cause fear' in t.lower() else []
def area_pages(sec,t,levelmap,extra={}):
    pre,h2=split_h2(t)
    for j,(title,txt) in enumerate(h2):
        parts=re.split(r'(?m)^### ([FD]\d+[a-z]?\. .+)$',txt)
        lead=((pre.strip()+'\n\n') if j==0 and pre.strip() else '')+parts[0].strip()
        imgs=list(levelmap.get(title,()))
        if lead or imgs:
            links=[m.I(i) for i in imgs]+npclinks(lead)+itemlinks(lead)+CF(lead)+extra.get(title,[])
            m.page(sec,title,C('## '+title+'\n\n'+lead) if lead else '<h>%s</h>'%html.escape(title),images=imgs,links=links,place={i:'$end' for i in imgs})
        for i in range(1,len(parts),2):
            at=parts[i].strip(); body_=parts[i+1]; num=at.split('.')[0]
            links=[m.B(c) for c in ENCBY.get(num,[])]
            ln=[]
            for a_,nm_,c_,_ in [x for x in ENC if x[0]==num]:
                for k in c_:
                    if m.N(K(k)) not in ln: ln.append(m.N(K(k)))
            for x in npclinks(body_):
                if x not in ln: ln.append(x)
            links+=ln+itemlinks(body_)+CF(body_)+extra.get(num,[])
            m.page(sec,at,C('## '+at+'\n'+body_),links=links); PAGEOF[num]='reference.refmanualdata.'+ids(len(m.pages))
            base=re.match(r'[FD]\d+',num).group(0); PAGEOF.setdefault(base,PAGEOF[num])
# Introduction
intro=body(os.path.join(ADV,'A2-00 Introduction.md')); pre,h2=split_h2(re.sub(r'^\s*# [^\n]*\n','',intro,count=1))
ALLMAPS=[MK[x] for x in sorted(MK)]+[MP[x] for x in sorted(MP)]
m.page('Introduction','Using This Module',C(pre)+C('''This book holds the whole adventure: the introduction and background, then one page per keyed area in Part 1 (the hill fort, areas F1-F39) and Part 2 (the dungeon, areas D1-D39), the tournament rules (Convention Mode), and appendices for the bestiary, the people of the stockade, the nine pregenerated characters and the magic items. Each area page ends with its encounters (a **4 PCs** and a **6 PCs** version where the numbers change) and creatures. The kitchen ambush (F35) and Markessa's laboratory (D22) are split into waves.

The GM maps carry a pin on every area label; double-click a pin to open the area's page. Share the **(Player)** maps, which have the area labels and the secret- and concealed-door marks removed. Maps A2-1 to A2-4 use a 10-ft grid set to 50 px; Map A2-5 (the tournament tactical maps) has no grid. These are cleaned renders of the 2013 maps; traced Sidebar Press maps will replace them in a later edition.

The nine tournament characters are in the Library as **Pregenerated Characters**: 5th-level 5e builds, the same party for A1-A4. Wandering monsters are rollable **Tables** (4 PCs and 6 PCs versions).

**Credits.** *A2 Secret of the Slavers' Stockade* by Harold Johnson with Tom Moldvay (TSR 1981), from *Against the Slave Lords* (Wizards of the Coast, 2013). 5e conversion by Sidebar Press for private and ARPG table use only; not for sale or distribution. Creature statistics marked SRD: System Reference Document 5.1 (CC-BY-4.0).'''),links=[m.I(k) for k in ALLMAPS])
for title,txt in h2:
    if title in ('Credits',): continue
    links=npclinks(txt)+itemlinks(txt)+CF(txt)
    if title=='Maps': links=[m.I(k) for k in ALLMAPS]
    if title=='Overland from Highport': links+=TL('wild')
    if title=='Hill Fort Wandering Monsters': links+=TL('fort')
    m.page('Introduction',title,C('## '+title+'\n'+txt),links=links)
tb='<table><tr><td><b>Code</b></td><td><b>Encounter</b></td><td><b>XP</b></td></tr>'+''.join('<tr><td>%s</td><td>%s</td><td>%d</td></tr>'%(c,html.escape(m.BATN[c]),int(m._cat('battle').find(m.BAT[c].split('.')[1]).findtext('exp'))) for c in m.BAT)+'</table>'
m.page('Introduction','Encounters','<h>Encounters</h><p>Every encounter in the module, with its total (unadjusted) XP. Area encounters have a 4-PC and a 6-PC version where the numbers change. Wandering monsters use the rollable tables.</p>'+tb,links=[m.B(c) for c in m.BAT])
tb='<table><tr><td><b>Item</b></td><td><b>Where</b></td></tr>'+''.join('<tr><td>%s</td><td>%s</td></tr>'%(html.escape(m.ITEMN[k]),html.escape(g)) for k,g in GMI)+'</table>'
m.page('Introduction','Magic Items and Treasure — GM Notes',tb,links=[m.IT(k) for k,_ in GMI])
for sec,f,lv,ex in (('Part 1: The Hill Fort','A2-01 The Hill Fort.md',{'Key to the Hill Fort':(MK['1'],MP['1'],MK['2'],MP['2'],MK['3'],MP['3'])},{}),
                 ('Part 2: The Dungeon','A2-02 The Dungeon.md',{'Key to the Dungeon':(MK['4'],MP['4'])},{'Dungeon Wandering Monsters':TL('dun'),'D28':TL('cave')})):
    t=re.sub(r'^\s*# [^\n]*\n','',body(os.path.join(ADV,f)),count=1)
    area_pages(sec,t,lv,ex)
# Convention Mode
cm=re.sub(r'^\s*# [^\n]*\n','',body(os.path.join(ADV,'A2-03 Convention Mode.md')),count=1); pre,h2=split_h2(cm)
for j,(title,txt) in enumerate(h2):
    lead=(pre.strip()+'\n\n' if j==0 else '')+txt
    imgs=[TAC] if title=='Starting Points' else []
    m.page('Convention Mode',title,C('## '+title+'\n'+lead),images=imgs,links=[m.I(i) for i in imgs]+npclinks(lead),place={i:'$end' for i in imgs})
# Appendices: bestiary, people, pregens, items
bi=re.sub(r'```text.*?```','',bst,flags=re.S); bi=re.sub(r'^---.*?\n---\n','',bi,flags=re.S); bi=re.sub(r'^\s*# [^\n]*\n','',bi,count=1)
bpre,bh2=split_h2(bi); BH=dict(bh2)
m.page('Appendix: Bestiary','Bestiary',C(bpre)+C('## Quick index\n'+BH['Quick index']),links=[m.N(k) for k in m.NPC])
m.page('Appendix: Bestiary','Monster Manual Creatures',C(BH['MM creatures']),links=[m.N(slug(k)) for k in SRDK])
m.page('Appendix: Bestiary','Hazard: the Phantom',C(BH['Hazards']))
m.page('Appendix: Bestiary','Boggles, Cloakers, Haunts, Phantoms and Cavelings',C('## Lore\n'+BH['Lore']),links=[m.N(k) for k in ('boggle','babyboggle','cloaker','haunt','caveling','cavelingbrute')])
for nm_,p in sorted(NOTES.items()):
    t=re.sub(r'^\s*# [^\n]*\n','',body(p),count=1); t=re.sub(r'(?s)## Canon Notes.*?(?=## Continuity|\Z)','',t)
    ln=[]
    for sb in re.findall(r'#([^\]|]+)[\]|]',fgconv.sections(body(p)).get('Stat Block','')):
        if slug(sb) in m.NPC and m.N(slug(sb)) not in ln: ln.append(m.N(slug(sb)))
    ln+=[x for x in npclinks(t) if x not in ln]+itemlinks(t)
    m.page('Appendix: People of the Stockade',nm_,C('## '+nm_+'\n'+t),links=ln)
for p in sorted(PREGEN,key=lambda p:[x['name'].strip('"') for x in pregens.P].index(os.path.basename(p)[:-3])):
    t=re.sub(r'^\s*# [^\n]*\n','',body(p),count=1); t=re.sub(r'\n\*1e original:[^\n]*\n','\n',t)
    nm_=fgconv.NAMES.get(os.path.basename(p)[:-3],os.path.basename(p)[:-3])
    m.page('Appendix: Pregenerated Characters',nm_,C('## '+nm_+'\n'+t))
m.page('Appendix: Magic Items','Magic Items','<h>Magic Items</h><p>Click a name to open the item record, which you can drag to a character sheet.</p>'+''.join('<p><b>%s.</b> %s</p>'%(html.escape(m.ITEMN[k]),html.escape(g)) for k,g in GMI),links=[m.IT(k) for k,_ in GMI]+[m.SP('causefear')])
# ---------------------------------------------------------------- map pins -> area pages (FG image coordinates: origin at centre, y up)
PINS=json.load(open(os.path.join(HERE,'pins.json')))
for title,lab in PINS.items():
    n=title.split(' ')[2]; k=MK[n]; W,H=SIZE[k]
    im=m._cat('image').find(m.IMG[k][0]).find('image'); ly=im.find('layers'); lid=10
    for code in sorted(lab,key=lambda c:(c[0],int(re.match(r'[FD](\d+)',c).group(1)),c)):
        rec=PAGEOF.get(code) or PAGEOF.get(re.match(r'[FD]\d+',code).group(0))
        if not rec: print('no page for pin',title,code); continue
        for x,y in lab[code]:
            lid+=1; L=_S(ly,'layer'); _S(L,'name',None,code); _S(L,'id',None,lid); _S(L,'parentid',None,-1); _S(L,'type',None,'shortcut')
            sc=_S(L,'shortcut'); _S(sc,'class',None,'referencemanualpage'); _S(sc,'record',None,rec)
            _S(L,'matrix',None,'1,0,0,0,0,1,0,0,0,0,1,0,%d,%d,0,1'%(x-W//2,H//2-y))
# ---------------------------------------------------------------- pregenerated characters
pregens.add_fg(m.root,SRDSP)
_build_lib=m.build
def build_with_pregens(out_path,cover_image=None):
    # fgmod.build writes the library; add the Pregenerated Characters entry by patching ET.tostring's input just before it runs
    orig=fgmod._S
    def S(p,tag,typ=None,text=None):
        e=orig(p,tag,typ,text)
        if tag=='entries' and p.tag==re.sub(r'[^a-z0-9]','',NAME.lower()):
            x=orig(e,'charsheet'); _WR(x,'librarylink','pregencharselect','pregencharsheet'); orig(x,'name','string','Pregenerated Characters')
            for tg,lab in (('tables','Tables'),):
                x=orig(e,tg); _WR(x,'librarylink','reference_list','..'); orig(x,'name','string',lab); orig(x,'recordtype','string','table' if tg=='tables' else tg)
        return e
    fgmod._S=S
    try: _build_lib(out_path,cover_image)
    finally: fgmod._S=orig
# ---------------------------------------------------------------- build
m.LINT=[r'A2-0\d',r'Bestiary \(5e\)',r'\(A2\)',r'Conversion Ledger']
out=os.path.join(WORK,NAME+'.mod')
build_with_pregens(out,cover_image=MK['1'])
if '--test' in sys.argv: sys.exit(0)
KIT=os.path.join(ADV,'FGU Kit'); os.makedirs(KIT,exist_ok=True); shutil.copyfile(out,os.path.join(KIT,NAME+'.mod'))
if '--install' in sys.argv: shutil.copyfile(out,os.path.join(FG,'modules',NAME+'.mod')); print('installed to FG modules')
