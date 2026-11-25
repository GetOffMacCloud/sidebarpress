"""A1 Slave Pits of the Undercity (5e conversion) -> Fantasy Grounds Unity module.
Reads the vault notes in this adventure folder (site keys, Bestiary, NPCs, Items, Pregens), the Cause Fear spell note,
and the cleaned scan maps in Maps/A1. Uses the shared builder in 70-Company/Tools/fgu-module-builder; pregens.py
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
NAME='A1 - Slave Pits of the Undercity'; DISPLAY='A1 Slave Pits of the Undercity (5E)'
WORK=os.path.join(os.path.expanduser(os.environ.get('FG_WORK','~/fgwork')),'A1'); os.makedirs(WORK,exist_ok=True)
MAPDIR=os.path.join(PROJ,'Maps','A1')
m=Mod(NAME,DISPLAY,'Sidebar Press Conversions','Sidebar Press',FG,WORK)
slug=lambda x: re.sub(r'[^a-z0-9]','',x.lower())
def body(p):
    t=open(p).read()
    return t.split('\n---',1)[1].split('\n',1)[1] if t.startswith('---') else t
# ---------------------------------------------------------------- wikilinks: vault notes -> module records/pages
def prep(t):
    t=re.sub(r'\[\[A1 - 5e Conversion Ledger\]\]( §\d+)?','the Sidebar Press conversion ledger',t)
    t=re.sub(r'\[\[A1 - Bestiary \(5e\)#([^\]|]+)(\|[^\]]*)?\]\]',lambda x:'[[%s%s]]'%(x.group(1),x.group(2) or ''),t)
    t=re.sub(r'\[\[A1 - Bestiary \(5e\)\]\]','[[Bestiary]]',t)
    t=re.sub(r'\[\[A1-0\d [^\]#|]*#([^\]|]+)(\|[^\]]*)?\]\]',lambda x:'[[%s%s]]'%(x.group(1),x.group(2) or ''),t)
    t=re.sub(r'\[\[A1-0\d ([^\]|]+)(\|[^\]]*)?\]\]',lambda x:'[[%s%s]]'%(x.group(1),x.group(2) or ''),t)
    return t
ITEMNOTES=sorted(glob.glob(os.path.join(ADV,'Items','*.md')))
PREGEN=sorted(glob.glob(os.path.join(ADV,'Pregens','*.md')))
fgconv.NAMES={os.path.basename(p)[:-3]:re.sub(r' \(A1\)$','',os.path.basename(p)[:-3]).replace('’',"'") for p in ITEMNOTES}
fgconv.NAMES.update({'The Temple':'Key to the Temple Level','The Sewers':'Key to the Sewer Level','Introduction':'Running A1 in 5e','Convention Mode':'The Tournament','Ogre':'"Ogre"'})
C=lambda t: fgconv.conv(prep(t))
# ---------------------------------------------------------------- maps
src=os.path.join(WORK,'src'); os.makedirs(src,exist_ok=True)
for f in os.listdir(src): os.remove(os.path.join(src,f))
MAPS={}
for f in sorted(os.listdir(MAPDIR)):
    mm=re.match(r'A1 Map (\d) - (.*) - (GM|Player)\.png$',f)
    if not mm: continue
    k='map-a1-%s-%s'%(mm.group(1),re.sub(r'[^a-z0-9]+','-',mm.group(2).lower()).strip('-'))+('-player' if mm.group(3)=='Player' else '')
    shutil.copy(os.path.join(MAPDIR,f),os.path.join(src,k+'.png')); MAPS[k]=(mm.group(1),mm.group(2),mm.group(3))
m.images(src)
from PIL import Image
SIZE={k:Image.open(os.path.join(src,k+'.png')).size for k in MAPS}
for k,(n,title,ver) in MAPS.items():
    rec=m._cat('image').find(m.IMG[k][0]); rec.find('name').text='Map A1-%s — %s%s'%(n,title,' (Player)' if ver=='Player' else '')
    if n in ('1','2'):
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
BEST=os.path.join(ADV,'A1 - Bestiary (5e).md'); bst=open(BEST).read()
NOTES={os.path.basename(p)[:-3]:p for p in glob.glob(os.path.join(ADV,'NPCs','*.md'))}
def lore(name):
    sec=re.search(r'^### %s\n(.*?)(?=^### |^## |\Z)'%re.escape(name),bst,re.S|re.M)
    if not sec: return ''
    return C(re.sub(r'```text.*?```','',sec.group(1),flags=re.S))
LORE=dict(re.findall(r'^\*\*(Aspis|Giant sundew)\.\*\* (.*)$',bst,re.M))
for blk in fgtext.blocks_md(bst):
    d=fgtext.parse(blk); k=slug(d['name']); extra=''
    if d['name'].startswith('Aspis'): extra=C('**Aspis.** '+LORE['Aspis'])
    if d['name']=='Giant Sundew': extra=C('**Giant sundew.** '+LORE['Giant sundew'])
    fgtext.add(m,k,d,'<h>%s</h>%s%s<p><i>A1 Slave Pits of the Undercity, 5e conversion (Sidebar Press).</i></p>'%(html.escape(d['name']),lore(d['name']),extra))
for k in ('slaverpriest','highpriestess','slavermage','orcwitchdoctor'): m.npc_spells(k,spell_lookup)
def mm(srd,name,key,dress): m.npc_srd(srd,name,key,dress=dress,keep_srd_text=False)
MMDRESS={}
for nm_,txt in re.findall(r'^### ([^\n]+)\n(\*\*.*?)(?=^### |^## )',bst.split('## MM creatures')[1].split('## Custom statblocks')[0]+'## ',re.S|re.M):
    txt=re.sub(r'\[\[([^\]|]*?)(?: \(A1\))?\]\]',r'\1',txt)
    MMDRESS[nm_]=re.sub(r'\[\[[^\]|]*\|([^\]]*)\]\]',r'\1',re.sub(r'^\*\*[^*]+\*\* \([^)]*\)\.?\s*','',txt.strip())).replace('*','').strip() or 'As the Monster Manual.'
SRDK={'Orc':'orc','Ogre':'ogre','Ghoul':'ghoul','Ghast':'ghast','Zombie':'zombie','Skeleton':'skeleton','Wight':'wight','Basilisk':'basilisk','Harpy':'harpy','Stirge':'stirge',
      'Doppelganger':'doppelganger','Troll':'troll','Gray Ooze':'grayooze','Giant Rat':'giantrat','Crocodile':'crocodile','Veteran':'veteran','Commoner':'commoner'}
for nm_,k in SRDK.items(): mm(k,nm_,k,MMDRESS.get(nm_,'As the Monster Manual.'))
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
# ---------------------------------------------------------------- encounters (4 PCs / 6 PCs)
T1,S2,TT,TS=MK['1'],MK['2'],MK['3'],MK['4']
D=lambda a,b:{4:a,6:b}
ENC=[ # (area, name, {4:[...],6:[...]} or [...] for both, map)
('T3','Ghouls on the ledge',D([('ghoul',5),('ghast',1)],[('ghoul',8),('ghast',2)]),T1),
('T5a','Giant sundew',[('giantsundew',1)],T1),
('T6','Stable hands',D([('halforcslaver',3),('doppelganger',1)],[('halforcslaver',4),('doppelganger',1)]),T1),
('T7','Halberd orcs',D([('orc',4)],[('orc',6)]),T1),
('T8','Guardian trees',[('guardiantree',3)],T1),('T8','Cemetery ghouls',D([('ghoul',2)],[('ghoul',4)]),T1),
('T9','Wight',[('wight',1)],T1),
('T10','Basilisks',D([('basilisk',1)],[('basilisk',2)]),T1),
('T12','False slavers, wave 1',D([('halforcslaver',4),('slaverpriest',1)],[('halforcslaver',6),('slaverpriest',1)]),T1),
('T12','False slavers, wave 2',D([('halforcslaver',7),('cutthroat',1),('orc',2)],[('halforcslaver',11),('cutthroat',2),('orc',3)]),T1),
('T14','Harpies',D([('harpy',3)],[('harpy',4)]),T1),
('T16','Courtyard: flame cart crew',D([('orc',4),('halforcslaver',3)],[('orc',6),('halforcslaver',4)]),T1),
('T16','Outer winch: the gatekeeper',[('halforcgatekeeper',1)],T1),
('T16','Inner winch',[('halforcslaver',1),('doppelganger',1)],T1),
('T18','Temple chamber, round 1',D([('highpriestess',1),('templeguard',2),('templeassassin',1)],[('highpriestess',1),('templeguard',3),('templeassassin',1)]),T1),
('T18','Temple chamber, round 2: the troll',[('troll',1)],T1),
('T19','Stirges',D([('stirge',7)],[('stirge',10)]),T1),
('S2','Aspis larvae',D([('aspislarva',3)],[('aspislarva',5)]),S2),
('S3','Egg chamber drones',D([('aspisdrone',2)],[('aspisdrone',3)]),S2),
('S4','Gray ooze',[('grayooze',1)],S2),
('S5','Aspis chamber',D([('aspisdrone',3),('giantworkerant',3)],[('aspisdrone',4),('giantworkerant',5)]),S2),
('S6','Breeding chamber',D([('aspiscow',1),('aspisdrone',4)],[('aspiscow',1),('aspisdrone',6)]),S2),
('S8','Ant chamber',D([('giantworkerant',5),('giantsoldierant',1)],[('giantworkerant',7),('giantsoldierant',2)]),S2),
('S8','The queen\'s chamber',D([('giantantqueen',1),('giantsoldierant',7),('giantworkerant',7)],[('giantantqueen',1),('giantsoldierant',10),('giantworkerant',10)]),S2),
('S12','Orc and ogre outpost',D([('ogre',2),('orc',12)],[('ogre',3),('orc',18)]),S2),
('S14','Orc guard post',D([('orc',4)],[('orc',6)]),S2),
('S15','Main chamber',D([('orc',16)],[('orc',24)]),S2),
('S15','Chief\'s den',D([('orcchieftain',1),('orcbodyguard',5),('ogre',1)],[('orcchieftain',1),('orcbodyguard',8),('ogre',2)]),S2),
('S16','Wall guards (S16a)',D([('orc',5)],[('orc',8)]),S2),
('S16','Witch-doctor\'s ledges (S16b)',D([('orcwitchdoctor',1),('orc',4)],[('orcwitchdoctor',1),('orc',6)]),S2),
('S18a','Slave pit drones',D([('aspisdrone',1)],[('aspisdrone',2)]),S2),
('S18a','Trap-door drone (S18b)',[('aspisdrone',1)],S2),
('S19a','Caravan organizers',D([('slavermage',1),('veteran',1),('commoner',1),('orc',3)],[('slavermage',1),('veteran',1),('commoner',1),('orc',5)]),S2),
('S19a','The doppelganger slave',[('doppelganger',1)],S2),
('S19a','Overseer drone (S19c)',[('aspisdrone',1)],S2),
('S21','Slave Lord\'s den',D([('denmaster',1),('giantweaselblooddrinker',3),('orc',7)],[('denmaster',1),('giantweaselblooddrinker',5),('orc',10)]),S2),
('R','Wall: ghouls',D([('ghoul',2)],[('ghoul',3)]),None),('R','Wall: zombies',D([('zombie',4)],[('zombie',6)]),None),
('R','Wall: skeletons',D([('skeleton',4)],[('skeleton',6)]),None),('R','Wall: harpies',[('harpy',2)],None),
('R','Ruins: orc campfire',D([('orc',7)],[('orc',10)]),None),('R','Ruins: orc patrol with gatekeeper',D([('halforcgatekeeper',1),('orc',4)],[('halforcgatekeeper',1),('orc',7)]),None),
('R','Sewers: giant rats',D([('giantrat',6)],[('giantrat',9)]),None),('R','Sewers: crocodiles',D([('crocodile',2)],[('crocodile',3)]),None),
('R','Sewers: aspis drones',D([('aspisdrone',1)],[('aspisdrone',2)]),None),('R','Sewers: blood-drinker weasels',D([('giantweaselblooddrinker',2)],[('giantweaselblooddrinker',3)]),None),
]
for _,_,cr,_ in ENC:
    for k,_ in (cr[6]+cr[4] if isinstance(cr,dict) else cr): assert k in m.NPC,k
ENCBY={}; n=0
for area,nm,cr,mp in ENC:
    n+=1; base='E%02d'%n
    if isinstance(cr,dict):
        for band,sfx in ((4,'a'),(6,'b')):
            m.battle(base+sfx,'%s%s (%d PCs)'%(('' if area=='R' else '%s: '%area),nm,band),cr[band],mp); ENCBY.setdefault(area,[]).append(base+sfx)
    else:
        m.battle(base,'%s%s'%(('' if area=='R' else '%s: '%area),nm),cr,mp); ENCBY.setdefault(area,[]).append(base)
# ---------------------------------------------------------------- reference manual
def split_h2(t):
    parts=re.split(r'(?m)^## (.+)$',t); return parts[0],[(parts[i].strip(),parts[i+1]) for i in range(1,len(parts),2)]
PAGEOF={}
def npclinks(txt):
    out=[]
    for k in m.NPC:
        nm=m.npcname(k)
        if re.search(r'\[\[(?:A1 - Bestiary \(5e\)#)?%s(?:\||\]\])'%re.escape(nm),txt) and m.N(k) not in out: out.append(m.N(k))
    return out
def itemlinks(txt): return [m.IT(NOTEKEY[os.path.basename(p)[:-3]]) for p in ITEMNOTES if '[['+os.path.basename(p)[:-3] in txt]
def area_pages(sec,t,levelmap):
    pre,h2=split_h2(t)
    for j,(title,txt) in enumerate(h2):
        parts=re.split(r'(?m)^### ([TS]\d+[a-z]?\. .+)$',txt)
        lead=((pre.strip()+'\n\n') if j==0 and pre.strip() else '')+parts[0].strip()
        imgs=list(levelmap.get(title,()))
        if lead or imgs:
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
            base=re.match(r'[TS]\d+',num).group(0); PAGEOF.setdefault(base,PAGEOF[num])
# Introduction
intro=body(os.path.join(ADV,'A1-00 Introduction.md')); pre,h2=split_h2(re.sub(r'^\s*# [^\n]*\n','',intro,count=1))
ALLMAPS=[MK[x] for x in sorted(MK)]+[MP[x] for x in sorted(MP)]
m.page('Introduction','Using This Module',C(pre)+C('''This book holds the whole adventure: the introduction and background, then one page per keyed area in Part 1 (the Temple, areas T1-T19) and Part 2 (the Undercity, areas S1-S21), the tournament rules (Convention Mode), and appendices for the bestiary, the people of the slave pits, the nine pregenerated characters and the magic items. Each area page ends with its encounters (a **4 PCs** and a **6 PCs** version where the numbers change) and creatures. The biggest fights are split into waves.

The GM maps carry a pin on every area label; double-click a pin to open the area's page. Share the **(Player)** maps, which have the area labels and the trap and secret-door marks painted out. Both maps use a 10-ft grid set to 50 px. The two tournament maps (Map A1-3 and A1-4) are for Convention Mode and have no grid. These are cleaned scans of the 2013 maps; traced Sidebar Press maps will replace them in a later edition.

The nine tournament characters are in the Library as **Pregenerated Characters**: 5th-level 5e builds, the same party for A1-A4.

**Credits.** *A1 Slave Pits of the Undercity* by David Cook (TSR 1980), from *Against the Slave Lords* (Wizards of the Coast, 2013). 5e conversion by Sidebar Press for private and ARPG table use only; not for sale or distribution. Creature statistics marked SRD: System Reference Document 5.1 (CC-BY-4.0).'''),links=[m.I(k) for k in ALLMAPS])
for title,txt in h2:
    if title in ('Credits',): continue
    imgs=[]; links=npclinks(txt)+itemlinks(txt)+([m.SP('causefear')] if 'Cause Fear' in txt else [])
    if title=='Maps': links=[m.I(k) for k in ALLMAPS]
    if title in ('Wall Encounters',): links+=[m.B(c) for c in ENCBY['R'] if 'Wall' in m.BATN[c]]
    if title in ('Ruin Encounters',): links+=[m.B(c) for c in ENCBY['R'] if 'Ruins' in m.BATN[c]]
    m.page('Introduction',title,C('## '+title+'\n'+txt),images=imgs,links=links)
tb='<table><tr><td><b>Code</b></td><td><b>Encounter</b></td><td><b>XP</b></td></tr>'+''.join('<tr><td>%s</td><td>%s</td><td>%d</td></tr>'%(c,html.escape(m.BATN[c]),int(m._cat('battle').find(m.BAT[c].split('.')[1]).findtext('exp'))) for c in m.BAT)+'</table>'
m.page('Introduction','Encounters','<h>Encounters</h><p>Every encounter in the module, with its total (unadjusted) XP. Area encounters have a 4-PC and a 6-PC version where the numbers change; random encounters are listed last.</p>'+tb,links=[m.B(c) for c in m.BAT])
tb='<table><tr><td><b>Item</b></td><td><b>Where</b></td></tr>'+''.join('<tr><td>%s</td><td>%s</td></tr>'%(html.escape(m.ITEMN[k]),html.escape(g)) for k,g in GMI)+'</table>'
m.page('Introduction','Magic Items and Treasure — GM Notes',tb,links=[m.IT(k) for k,_ in GMI])
for sec,f,lv in (('Part 1: The Temple','A1-01 The Temple.md',{'Key to the Temple Level':(MK['1'],MP['1'])}),
                 ('Part 2: The Undercity','A1-02 The Sewers.md',{'Key to the Sewer Level':(MK['2'],MP['2'])})):
    t=re.sub(r'^\s*# [^\n]*\n','',body(os.path.join(ADV,f)),count=1)
    area_pages(sec,t,lv)
# Convention Mode
cm=re.sub(r'^\s*# [^\n]*\n','',body(os.path.join(ADV,'A1-03 Convention Mode.md')),count=1); pre,h2=split_h2(cm)
for j,(title,txt) in enumerate(h2):
    lead=(pre.strip()+'\n\n' if j==0 else '')+txt
    imgs=[TT,TS] if title=='Starting Points' else []
    m.page('Convention Mode',title,C('## '+title+'\n'+lead),images=imgs,links=[m.I(i) for i in imgs]+npclinks(lead),place={i:'$end' for i in imgs})
# Appendices: bestiary, people, pregens, items
bi=re.sub(r'```text.*?```','',bst,flags=re.S); bi=re.sub(r'^---.*?\n---\n','',bi,flags=re.S); bi=re.sub(r'^\s*# [^\n]*\n','',bi,count=1)
bpre,bh2=split_h2(bi); BH=dict(bh2)
m.page('Appendix: Bestiary','Bestiary',C(bpre)+C('## Quick index\n'+BH['Quick index']),links=[m.N(k) for k in m.NPC])
m.page('Appendix: Bestiary','Monster Manual Creatures',C(BH['MM creatures']),links=[m.N(k) for k in SRDK.values()])
m.page('Appendix: Bestiary','Aspis and Giant Sundew',C('## Lore\n'+BH['Lore']),links=[m.N(k) for k in ('aspisdrone','aspislarva','aspiscow','giantsundew')])
for nm_,p in sorted(NOTES.items()):
    t=re.sub(r'^\s*# [^\n]*\n','',body(p),count=1); t=re.sub(r'(?s)## Canon Notes.*?(?=## Continuity|\Z)','',t)
    ln=[]
    sb=re.search(r'#([^\]]+)\]\]',fgconv.sections(body(p)).get('Stat Block',''))
    if sb and slug(sb.group(1)) in m.NPC: ln.append(m.N(slug(sb.group(1))))
    ln+=[x for x in npclinks(t) if x not in ln]+itemlinks(t)
    m.page('Appendix: People of the Slave Pits',nm_,C('## '+nm_+'\n'+t),links=ln)
for p in sorted(PREGEN,key=lambda p:[x['name'].strip('"') for x in pregens.P].index(os.path.basename(p)[:-3])):
    t=re.sub(r'^\s*# [^\n]*\n','',body(p),count=1); t=re.sub(r'\n\*1e original:[^\n]*\n','\n',t)
    nm_=fgconv.NAMES.get(os.path.basename(p)[:-3],os.path.basename(p)[:-3])
    m.page('Appendix: Pregenerated Characters',nm_,C('## '+nm_+'\n'+t))
m.page('Appendix: Magic Items','Magic Items','<h>Magic Items</h><p>Click a name to open the item record, which you can drag to a character sheet.</p>'+''.join('<p><b>%s.</b> %s</p>'%(html.escape(m.ITEMN[k]),html.escape(g)) for k,g in GMI),links=[m.IT(k) for k,_ in GMI]+[m.SP('causefear')])
# ---------------------------------------------------------------- map pins -> area pages (FG image coordinates: origin at centre, y up)
PINS=json.load(open(os.path.join(HERE,'pins.json')))
for title,lab in PINS.items():
    n=title.split(' ')[2]; k=MK[n]; W,H=SIZE[k]; pre_='T' if n=='1' else 'S'
    im=m._cat('image').find(m.IMG[k][0]).find('image'); ly=im.find('layers'); lid=10
    for label,x,y,area in sorted(lab,key=lambda r:(int(re.match(r'[TS](\d+)',r[3]).group(1)),r[0])):
        code=pre_+re.sub(r'[A-Z]$',lambda q:q.group(0).lower(),label) if re.match(r'\d',label) else area
        rec=PAGEOF.get(code) or PAGEOF.get(area)
        if not rec: print('no page for pin',label,area); continue
        lid+=1; L=_S(ly,'layer'); _S(L,'name',None,'%s%s'%(pre_,label if re.match(r'\d',label) else '8'+label)); _S(L,'id',None,lid); _S(L,'parentid',None,-1); _S(L,'type',None,'shortcut')
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
        return e
    fgmod._S=S
    try: _build_lib(out_path,cover_image)
    finally: fgmod._S=orig
# ---------------------------------------------------------------- build
m.LINT=[r'A1-0\d',r'Bestiary \(5e\)',r'\(A1\)',r'Conversion Ledger']
out=os.path.join(WORK,NAME+'.mod')
build_with_pregens(out,cover_image=MK['1'])
if '--test' in sys.argv: sys.exit(0)
KIT=os.path.join(ADV,'FGU Kit'); os.makedirs(KIT,exist_ok=True); shutil.copyfile(out,os.path.join(KIT,NAME+'.mod'))
if '--install' in sys.argv: shutil.copyfile(out,os.path.join(FG,'modules',NAME+'.mod')); print('installed to FG modules')
