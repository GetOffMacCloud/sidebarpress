"""SP-OP01 What the Dead Fear -> Fantasy Grounds module. Run: python3 module.py [--test|--install]
Uses the shared builder in 70-Company/Tools/fgu-module-builder (see the fgu-module-build skill).
Modeled on SP-GA05's module.py, cut down for a Pocket Module (3 scenes, 1 homebrew NPC, 3 encounter bands)."""
import os,sys,re,glob,shutil,html,zipfile
import xml.etree.ElementTree as ET
HERE=os.path.dirname(os.path.abspath(__file__)); ADV=os.path.dirname(os.path.dirname(HERE)); VAULT=ADV
while not os.path.isdir(os.path.join(VAULT,'70-Company')): VAULT=os.path.dirname(VAULT)  # works at any folder depth (Pocket Modules/)
sys.path.insert(0,os.path.join(VAULT,'70-Company','Tools','fgu-module-builder'))
from fgmod import Mod, conv, body, sections, _S, _FT, ids
import fgconv
FG=os.environ.get('FG_DIR',os.path.expanduser('~/mnt/Fantasy Grounds'))
# ---- edition settings ----
CODE='SP-OP01'; NAME='SP-OP01 What the Dead Fear'; DISPLAY='SP-OP01 — What the Dead Fear'
SRC=ADV; ASSETS=os.path.join(VAULT,'99-Assets',CODE); TEXT_MAP={}
fgconv.STRIP=[CODE+' — ']
fgconv.NAMES={'SP-OP01 — Handout — The Notice':'Handout 1: The Notice','SP-OP01 — Handout — The Burial Register':'Handout 2: The Burial Register','SP-OP01 — Handout — The Larder Ledger':'Handout 3: The Larder Ledger','Gravecure':'Spell: Gravecure',CODE+'-What-the-Dead-Fear':'Concluding the Adventure','Brother Ossian':'Brother Ossian (Drunaghul)',"SP-OP01 — Handout — Ossian's Sketch":"Handout 4: Ossian's Sketch",'SP-OP01 — Appendix — NPC Summary':'Appendix: NPC Summary','SP-OP01 — Appendix — Adventure Flowchart':'Appendix: Adventure Flowchart','SP-OP01 — Story Award — He Remembers Your Face':'Story Award: He Remembers Your Face',"SP-OP01 — Bonus Objective — Pell's Mother":"Bonus Objective: Pell's Mother",'SP-OP01 — Ritterstadt Rewards':'Ritterstadt Rewards'}
FIX=[(r'See <b>?Concluding the Adventure</b>?\.?',''),(r'<p>Back to [^<]*</p>',''),(r' with no notes of their own; the real .*?either\.',' (Scene 3).'),(r'are sub-sites of the one note','are its areas'),(r'The FGU Import block in Brother Ossian \(Drunaghul\) \(the one source the module build reads\)','the Brother Ossian NPC record')]
# ---------------------------
WORK=os.path.expanduser(os.environ.get('FG_WORK','~/work/fgu')+'/'+CODE); FLAT=WORK+'-src'; os.makedirs(FLAT,exist_ok=True)
def ikey(f):
    n=os.path.splitext(f)[0]
    return n[len(CODE)+1:] if n.startswith(CODE+' ') else n
for f in glob.glob(os.path.join(ASSETS,'*'))+glob.glob(os.path.join(ASSETS,'*','*')):
    if '/_ref/' not in f and os.path.isfile(f) and os.path.splitext(f)[1].lower() in ('.png','.jpg','.jpeg','.webp'):
        dst=os.path.join(FLAT,ikey(os.path.basename(f))+os.path.splitext(f)[1].lower())
        if not os.path.exists(dst) or os.path.getmtime(f)>os.path.getmtime(dst): shutil.copyfile(f,dst)
m=Mod(NAME,DISPLAY,'Sidebar Press','Sidebar Press',FG,WORK,text_map=TEXT_MAP)
m.images(FLAT)
P=lambda pat: glob.glob(os.path.join(SRC,pat))[0]
NOTE=lambda folder,name: os.path.join(VAULT,folder,name+'.md')
MAIN=P(CODE+'-What-the-Dead-Fear.md'); BEST=P('*Bestiary.md')
def C(t):
    x=conv(t)
    for a,b in FIX: x=re.sub(a,b,x)
    return x
def fullnote(p): return re.sub(r'^# .*\n','',body(p).lstrip(),count=1)
def clean(t): return re.sub(r'```mermaid.*?```','',re.sub(r'!\[\[[^\]]*\]\]\n?','',t),flags=re.S)
APX=lambda n: os.path.join(SRC,n+'.md')
TITLE=lambda f: re.search(r'^title: "(.*)"',open(f).read(),re.M).group(1)
M=sections(body(MAIN))
pick=lambda S,*n: '\n'.join('## %s\n%s'%(x,S[x]) for x in n if x in S)
has=lambda k: k in m.IMG
# ---- homebrew NPC from the ## FGU Import block (traits / Actions / Bonus Actions / Legendary Actions) ----
def fgu_block(p): return re.search(r'## FGU Import.*?```text\n(.*?)```',open(p).read(),re.S).group(1).strip().split('\n')
def homebrew(key,p,token=None,picture=None):
    L=fgu_block(p); name=L[0]; sz,rest=L[1].split(' ',1); typ,align=rest.rsplit(', ',1)
    ac,actext=re.match(r'Armor Class (\d+)\s*(.*)',L[2]).groups(); hp,hd=re.match(r'Hit Points (\d+)\s*(.*)',L[3]).groups()
    speed=L[4][6:]; ab=[int(x) for x in re.findall(r'(\d+) \(',L[6])]
    f={}; i=7
    while not L[i].startswith('Proficiency Bonus'):
        for lab in ('Saving Throws','Skills','Damage Vulnerabilities','Damage Resistances','Damage Immunities','Condition Immunities','Senses','Languages','Challenge'):
            if L[i].startswith(lab+' '): f[lab]=L[i][len(lab)+1:]
        i+=1
    cr,xp=re.match(r'(\S+) \(([\d,]+) XP\)',f['Challenge']).groups(); i+=1
    G={'traits':[],'actions':[],'bonus':[],'legendary':[]}; tgt=G['traits']; cur=None
    for l in L[i:]:
        if l in ('Actions','Bonus Actions','Legendary Actions'): tgt=G[{'Actions':'actions','Bonus Actions':'bonus','Legendary Actions':'legendary'}[l]]; cur=None; continue
        mm=re.match(r"^([A-Z][A-Za-z' ()0-9-]{1,40})\. (.*)",l)
        if mm: cur=[mm.group(1),mm.group(2)]; tgt.append(cur)
        elif l.strip() and cur: cur[1]+='\n'+l
        elif l.strip() and tgt is G['legendary']: cur=['Options',l]; tgt.append(cur)
    m.npc(key,name,sz,typ,align,int(ac),actext,int(hp),hd,speed,ab,cr,int(xp.replace(',','')),f.get('Senses',''),f.get('Languages',''),
          traits=[tuple(t) for t in G['traits']],actions=[tuple(a) for a in G['actions']],bonus=[tuple(b) for b in G['bonus']],
          skills=f.get('Skills',''),saves=f.get('Saving Throws',''),immunities=f.get('Damage Immunities',''),
          text='The keeper of Merrow\'s Rest is a drunaghul wearing the face of the brother it ate first. Grateful, gentle, and always hungry. See the Bestiary page for the CR check and the Larder rules.',
          picture=picture)
    e=m._cat('npc').find(key)
    for lab,tag in (('Damage Resistances','damageresistances'),('Damage Vulnerabilities','damagevulnerabilities'),('Condition Immunities','conditionimmunities')):
        if lab in f: _S(e,tag,'string',f[lab])
    LA=_S(e,'legendaryactions')
    for k,(n,d) in enumerate(G['legendary'],1): it=_S(LA,ids(k)); _S(it,'desc','string',d); _S(it,'name','string',n)
    if token: _S(e,'token','token',m.imgpath(token)); m.TOK[key]=m.imgpath(token)
    return e
# innate spells: SRD text from DD5E SRD Data
_srdx=ET.fromstring(zipfile.ZipFile(os.path.join(FG,'modules','DD5E SRD Data.mod')).read('client.xml'))
_srdsp={(e.findtext('name') or '').lower():e for e in next(x for x in _srdx.iter() if x.tag=='spelldata').iter() if e.find('name') is not None and e.find('level') is not None}
def srd_spell(nm):
    e=_srdsp[nm.lower()]; d=re.sub(r'\s*\n\s*','\n',re.sub(r'<[^>]+>','\n',ET.tostring(e.find('description'),encoding='unicode'))).strip()
    return 'Level: %s\nCasting Time: %s\nComponents: %s\nDuration: %s\nRange: %s\n%s\n'%(e.findtext('level'),e.findtext('castingtime'),e.findtext('components'),e.findtext('duration'),e.findtext('range'),html.unescape(d))
GV=os.path.join(SRC,'Spells','Gravecure.md'); _gv=fullnote(GV)
_gvrules=re.sub(r'^\*\d\w\w-level[^\n]*\*\n','',re.sub(r'^- \*\*(Casting Time|Range|Components|Duration|Classes):\*\*.*\n','',_gv,flags=re.M).lstrip(),count=1).split('## Notes for the DM')[0]
m.spell('gravecure','Gravecure',3,'Necromancy',False,'1 action','60 feet','V, S, M (a pinch of grave salt)','Concentration, up to 1 minute','Cleric, Warlock, Wizard',C(_gvrules)+'<p><i>Sidebar Press homebrew (OP1).</i></p>')
HB_SPELL={'gravecure':'Level: 3\nCasting Time: 1 action\nComponents: V, S, M (a pinch of grave salt)\nDuration: Concentration, up to 1 minute\nRange: 60 feet\nEach undead of your choice in a 20-foot-radius sphere must succeed on a Wisdom saving throw or be cured: incapacitated, speed 0, no reactions. It repeats the save at the end of each of its turns and when it takes damage. CR 6+ undead have advantage. See the Gravecure spell record.\n'}
def innate(e):
    tr=[x for x in e.find('traits') if x.findtext('name')=='Innate Spellcasting'][0].findtext('desc'); L=_S(e,'innatespells'); n=0
    for freq,lst in re.findall(r'^(At will|\d/day(?: each)?): (.*)$',tr,re.M):
        for sp in [x.strip() for x in lst.split(',')]:
            n+=1; it=_S(L,ids(n)); _S(it,'desc','string',HB_SPELL.get(sp.lower()) or srd_spell(sp)); _S(it,'name','string','%s (%s)'%(sp.title(),freq))
TOK=('token-ossian' if has('token-ossian') else None); PIC=('portrait-ossian-color' if has('portrait-ossian-color') else TOK)
innate(homebrew('ossian',NOTE('30-NPCs','Brother Ossian'),token=TOK,picture=PIC))
def srd(src,name,key,dress,**kw):
    m.npc_srd(src,name,key,dress=dress,**kw)
    e=m._cat('npc').find(key); old=e.find('token')
    if old is not None: e.remove(old)
    m.TOK[key]=''
srd('wight','Sexton Harrow (Wight)','harrow',"The chapel's old gravedigger, raised by the drunaghul. His longsword is a shovel (same stats, bludgeoning damage). He speaks for the larder and won't fight Ossian unless persuaded (Persuasion DC 13). If Ossian feeds on him, Ossian regains 25 hit points.",overrides={'alignment':'neutral'},keep_srd_text=False)
srd('ghoul','Larder Ghoul','larderghoul',"The Widow Brisk, the Collier twins, Old Tam. They cower, taking the Dodge action every turn, until the party arms them (Persuasion DC 13). Their claws can paralyze Ossian. Each one Ossian feeds on heals him 15.",keep_srd_text=False)
srd('ogrezombie','Pallbearer (Ogre Zombie)','pallbearer',"Ossian's butchers, wrapped in burial linen and smelling of salt and clove. They wait in the chute alcove and drop down on round 2 (5–6 PCs only). Ossian can't feed on them.",keep_srd_text=False)
def hb_plain(key,path):
    e=homebrew(key,path); e.remove(e.find('legendaryactions'))
    t=e.find('text'); t.clear(); t.set('type','formattedtext'); h=ET.SubElement(t,'h'); h.text=e.findtext('name')
    p=ET.SubElement(t,'p'); p.text=' '.join(x.strip('- ') for x in re.findall(r'^- \*\*(?:Description|In this adventure):\*\* .*$',body(path),re.M)).replace('**','').replace('*','')
    p.text=re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]',r'\1',p.text or '')
    p=ET.SubElement(t,'p'); i=ET.SubElement(p,'i'); i.text='Sidebar Press homebrew.'
hb_plain('crawler',NOTE('65-Bestiary/'+CODE,'Ossuary Crawler')); hb_plain('curedhand',NOTE('65-Bestiary/'+CODE,'Cured Hand'))
srd('zombie','Husk (Zombie)','husk',"One of Ossian's mindless puppets, raised from decades-old burials. Husks walk past Ossian as if he weren't there.",keep_srd_text=False)
srd('ogrezombie','Ogre Husk (Ogre Zombie)','ogrehusk',"A hulking husk in rotted burial linen. It rises in the graveyard and wanders the catacombs.",keep_srd_text=False)
srd('gibberingmouther','Gibbering Mouther','mouther',"Ossian's failures: aberrant scraps he couldn't digest, festering in the kitchen's salt pit. They babble in the voices of the dead.",keep_srd_text=False)
# ---- encounters (one per party size); the larder is listed as friendly, not foe ----
MAP='map-saints-ossuary' if has('map-saints-ossuary') else None
for c,n,cr in (('E4a','03 The Saint\'s Ossuary (4 PCs)',[('ossian',1)]),('E4b','03 The Saint\'s Ossuary (5 PCs)',[('ossian',1),('pallbearer',1)]),('E4c','03 The Saint\'s Ossuary (6 PCs)',[('ossian',1),('pallbearer',2)])): m.battle(c,n,cr,MAP)
m.battle('L4','03 The Larder (Harrow and four ghouls; not foes)',[('harrow',1),('larderghoul',4)],MAP)
for it in m._cat('battle').find(m.BAT['L4'].split('.')[1]).find('npclist'): it.find('faction').text='neutral'
GYM='map-graveyard' if has('map-graveyard') else None; C1M=C2M=('map-catacombs' if has('map-catacombs') else None)
for c,n,cr in (('E1a','01 The Graveyard Rising (4 PCs)',[('husk',6),('ogrehusk',2)]),('E1b','01 The Graveyard Rising (5 PCs)',[('husk',10),('ogrehusk',2)]),('E1c','01 The Graveyard Rising (6 PCs)',[('husk',10),('ogrehusk',3)])): m.battle(c,n,cr,GYM)
for c,n,k in (('E2a','02 Bone Gallery (4 PCs)',4),('E2b','02 Bone Gallery (5 PCs)',5),('E2c','02 Bone Gallery (6 PCs)',6)): m.battle(c,n,[('crawler',k)],C1M)
for c,n,cr in (('E3a','02 The Kitchen (4 PCs)',[('mouther',3),('curedhand',4)]),('E3b','02 The Kitchen (5 PCs)',[('mouther',3),('curedhand',8)]),('E3c','02 The Kitchen (6 PCs)',[('mouther',4),('curedhand',8)])): m.battle(c,n,cr,C2M)
for c,n,cr in (('W1a','Wandering: Husk procession (4 PCs)',[('ogrehusk',4),('husk',4)]),('W1b','Wandering: Husk procession (5 PCs)',[('ogrehusk',5),('husk',4)]),('W1c','Wandering: Husk procession (6 PCs)',[('ogrehusk',6),('husk',6)]),
    ('W2a','Wandering: Crawler nest (4 PCs)',[('crawler',5)]),('W2b','Wandering: Crawler nest (5 PCs)',[('crawler',7)]),('W2c','Wandering: Crawler nest (6 PCs)',[('crawler',8)]),
    ('W3a',"Wandering: Butcher's crew (4 PCs)",[('ogrehusk',2),('crawler',3)]),('W3b',"Wandering: Butcher's crew (5 PCs)",[('ogrehusk',3),('crawler',4)]),('W3c',"Wandering: Butcher's crew (6 PCs)",[('ogrehusk',4),('crawler',4)])): m.battle(c,n,cr,C1M)
# ---- item ----
UP=os.path.join(VAULT,'50-Items','The Urn of Saint Merrow.md')
m.item('urn','The Urn of Saint Merrow','Wondrous Item',C(fullnote(UP).split('## History')[0]),rarity='Uncommon')
# ---- reference manual ----
I1,A1,A2,A3,AP='Introduction','Act 1 — The Chapel','Act 2 — The Catacombs','Act 3 — The Ossuary','Appendices'
SC=lambda n: P('Scenes/Scene 0%d —*.md'%n)
B3=[m.B(c) for c in ('E4a','E4b','E4c')]+[m.B('L4')]
BX=lambda p:[m.B(p+x) for x in 'abc']
for x in (CODE+' — Bestiary',CODE+' — Map Assets',CODE+' — Art Brief',CODE+' — Board','Build-Pipeline'): fgconv.SEEN.append(x)
cover=['cover'] if has('cover') else []
m.page(I1,'Cover','<p><b>APL 7 (levels 6–8) · Tier 2 · 4–6 characters · one 4-hour session</b></p><p><i>The mortician thanks you for coming. He thanks you for everything. He never once blinks.</i></p><p>OP1 · A Sidebar Press Pocket Module · November 2026. Setting-agnostic.</p>',images=cover)
HOWTO=('<h>How to Use This Module</h><p>The whole adventure, in order of play: three scenes, then the ending. Every fight (E1–E4) has ready-made combat tracker entries for 4, 5 and 6 PCs; W1–W3 are the Wandering Husks (all Hard). The boss fight '
 'also has a <b>Larder</b> entry (Harrow and four ghouls, set to neutral) to add alongside. Every statblock is in the NPC list; the Urn is in Items.</p>'
 '<p><b>Boxed text:</b> read it as written or paraphrase it, but keep every clue. Stats are 2014 5e.</p>')
m.page(I1,'Credits & How to Use','<p><b>What the Dead Fear</b> · %s · Sidebar Press. Statblocks marked SRD are from the 5E SRD 5.1 (CC-BY-4.0). The drunaghul statblock is original to Sidebar Press.</p>'%CODE+HOWTO+C(pick(M,'Design Frame','Credits')))
m.page(I1,'Background & Hooks',C(pick(M,'Background','Hooks')))
m.page(I1,'Rumors',C(pick(M,'Rumors (d6)')))
m.page(I1,"Merrow's Rest",C(fullnote(os.path.join(VAULT,'40-Locations',"Merrow's Rest.md")).split('## Adventure Use')[0]))
m.page(I1,'Brother Ossian',C(fullnote(os.path.join(VAULT,'30-NPCs','Brother Ossian.md')).split('## Stat Block')[0]),images=[i for i in ('portrait-ossian-guise','portrait-ossian-color') if has(i)],links=[m.N('ossian')])
m.page(I1,'Encounters & Cast',C(pick(M,'Encounters','Key NPCs','Key Locations')),links=BX('E1')+BX('E2')+BX('E3')+B3+[m.B(w+x) for w in ('W1','W2','W3') for x in 'abc']+[m.N(k) for k in ('ossian','harrow','larderghoul','pallbearer','husk','ogrehusk','crawler','mouther','curedhand')])
m.page(A1,'Scene 1 — The Grateful Mortician',C(fullnote(SC(1))),images=[i for i in ('portrait-ossian-guise','map-graveyard-dm') if has(i)],place={'map-graveyard-dm':'Fight: The Graveyard Rising'},links=BX('E1')+[m.N('ossian'),m.N('husk'),m.N('ogrehusk')])
m.page(A2,'Scene 2 — The Catacombs',C(fullnote(SC(2))),images=[i for i in ('map-merrows-rest-key',) if has(i)],links=BX('E2')+BX('E3')+[m.B(w+x) for w in ('W1','W2','W3') for x in 'abc']+[m.N('larderghoul'),m.N('crawler'),m.N('mouther'),m.N('curedhand'),m.N('husk')])
s3=[i for i in ('scene-the-trap','plate-ossian','portrait-sexton-harrow','map-saints-ossuary-dm') if has(i)]
m.page(A3,'Scene 3 — What the Dead Fear',C(fullnote(SC(3))),images=s3+([MAP] if MAP else []),links=B3+[m.N('ossian'),m.N('harrow'),m.IT('urn')]+([m.I(MAP)] if MAP else []))
m.page(A3,'Concluding the Adventure',C(pick(M,'Concluding the Adventure')),links=[m.IT('urn')])
m.page(AP,'Bestiary',C(fullnote(BEST)),links=[m.N(k) for k in m.NPC])
m.page(AP,'Spell: Gravecure',C(fullnote(GV)),links=[m.SP('gravecure')])
m.page(AP,'Running It at Other Levels',C(pick(M,'Running It at Other Levels')))
m.page(AP,'Stream Twists',C(pick(M,'Stream Twists (d6)')))
m.page(AP,'Sequel Seed',C(pick(M,'Sequel Seed: The Face on the Road')))
for _t in ('The Notice','The Burial Register','The Larder Ledger'):
    _h=os.path.join(SRC,'SP-OP01 — Handout — %s.md'%_t); _hi=[i for i in ('handout-'+_t.lower().replace(' ','-').replace('the-',''),) if has(i)]
    m.page(AP,re.search(r'^title: "(.*)"',open(_h).read(),re.M).group(1),C(clean(fullnote(_h))),images=_hi,place={k:'$end' for k in _hi})
_h=APX("SP-OP01 — Handout — Ossian's Sketch"); _hi=[i for i in ('handout-ossians-sketch',) if has(i)]
m.page(AP,TITLE(_h),C(clean(fullnote(_h)).split('## Production')[0]),images=_hi,place={k:'## What It Shows' for k in _hi} if False else {})
for _n,_imgs in (('SP-OP01 — Appendix — NPC Summary',[]),('SP-OP01 — Appendix — Adventure Flowchart',['flowchart']),("SP-OP01 — Bonus Objective — Pell's Mother",[]),('SP-OP01 — Story Award — He Remembers Your Face',[]),('SP-OP01 — Ritterstadt Rewards',[])):
    _f=APX(_n); _i=[i for i in _imgs if has(i)]
    m.page(AP,TITLE(_f),C(clean(fullnote(_f))),images=_i)
m.page(AP,'The Urn of Saint Merrow',C(fullnote(UP).split('## Continuity')[0]),links=[m.IT('urn')])
# ---- build ----
m.LINT=[r'SP-OP01-What',r'SP-OP01 — (Bestiary|Board|Map|Art)',r'FGU Import',r'30-NPCs']
OUT=os.path.join(ADV,'FGU Kit',NAME+'.mod')
m.build(WORK+'.mod',cover_image='cover' if cover else None)
if '--test' in sys.argv: sys.exit(0)
shutil.copyfile(WORK+'.mod',OUT)
if '--install' in sys.argv: shutil.copyfile(OUT,os.path.join(FG,'modules',NAME+'.mod')); print('installed to FG modules')
