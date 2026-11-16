"""SP-OP01 What the Dead Fear -> Fantasy Grounds module. Run: python3 module.py [--test|--install]
Uses the shared builder in 70-Company/Tools/fgu-module-builder (see the fgu-module-build skill).
Modeled on SP-GA05's module.py, cut down for a Pocket Module (3 scenes, 1 homebrew NPC, 3 encounter bands)."""
import os,sys,re,glob,shutil,html,zipfile
import xml.etree.ElementTree as ET
HERE=os.path.dirname(os.path.abspath(__file__)); ADV=os.path.dirname(os.path.dirname(HERE)); VAULT=os.path.dirname(os.path.dirname(ADV))
sys.path.insert(0,os.path.join(VAULT,'70-Company','Tools','fgu-module-builder'))
from fgmod import Mod, conv, body, sections, _S, _FT, ids
import fgconv
FG=os.environ.get('FG_DIR',os.path.expanduser('~/mnt/Fantasy Grounds'))
# ---- edition settings ----
CODE='SP-OP01'; NAME='SP-OP01 What the Dead Fear'; DISPLAY='SP-OP01 — What the Dead Fear'
SRC=ADV; ASSETS=os.path.join(VAULT,'99-Assets',CODE); TEXT_MAP={}
fgconv.STRIP=[CODE+' — ']
fgconv.NAMES={CODE+'-What-the-Dead-Fear':'Concluding the Adventure','Brother Ossian':'Brother Ossian (Avolakia)'}
FIX=[(r'See <b>?Concluding the Adventure</b>?\.?',''),(r'<p>Back to [^<]*</p>',''),(r' with no notes of their own; the real .*?either\.',' (Scene 3).'),(r'are sub-sites of the one note','are its areas'),(r'The FGU Import block in Brother Ossian \(Avolakia\) \(the one source the module build reads\)','the Brother Ossian NPC record')]
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
          text='The keeper of Merrow\'s Rest is an avolakia wearing the face of the brother it ate first. Grateful, gentle, and always hungry. See the Bestiary page for the CR check and the Larder rules.',
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
def innate(e):
    tr=[x for x in e.find('traits') if x.findtext('name')=='Innate Spellcasting'][0].findtext('desc'); L=_S(e,'innatespells'); n=0
    for freq,lst in re.findall(r'^(At will|\d/day(?: each)?): (.*)$',tr,re.M):
        for sp in [x.strip() for x in lst.split(',')]:
            n+=1; it=_S(L,ids(n)); _S(it,'desc','string',srd_spell(sp)); _S(it,'name','string','%s (%s)'%(sp.title(),freq))
TOK=('token-ossian' if has('token-ossian') else None); PIC=('portrait-ossian-color' if has('portrait-ossian-color') else TOK)
innate(homebrew('ossian',NOTE('30-NPCs','Brother Ossian'),token=TOK,picture=PIC))
def srd(src,name,key,dress,**kw):
    m.npc_srd(src,name,key,dress=dress,**kw)
    e=m._cat('npc').find(key); old=e.find('token')
    if old is not None: e.remove(old)
    m.TOK[key]=''
srd('wight','Sexton Harrow (Wight)','harrow',"The chapel's old gravedigger, raised by the avolakia. His longsword is a shovel (same stats, bludgeoning damage). He speaks for the larder and won't fight Ossian unless persuaded (Persuasion DC 13). If Ossian feeds on him, Ossian regains 25 hit points.",overrides={'alignment':'neutral'},keep_srd_text=False)
srd('ghoul','Larder Ghoul','larderghoul',"The Widow Brisk, the Collier twins, Old Tam. They cower, taking the Dodge action every turn, until the party arms them (Persuasion DC 13). Their claws can paralyze Ossian. Each one Ossian feeds on heals him 15.",keep_srd_text=False)
srd('ogrezombie','Pallbearer (Ogre Zombie)','pallbearer',"Ossian's butchers, wrapped in burial linen and smelling of salt and clove. They wait in the chute alcove and drop down on round 2 (5–6 PCs only). Ossian can't feed on them.",keep_srd_text=False)
# ---- encounters (one per party size); the larder is listed as friendly, not foe ----
MAP='map-saints-ossuary' if has('map-saints-ossuary') else None
for c,n,cr in (('E1a','03 The Saint\'s Ossuary (4 PCs)',[('ossian',1)]),('E1b','03 The Saint\'s Ossuary (5 PCs)',[('ossian',1),('pallbearer',1)]),('E1c','03 The Saint\'s Ossuary (6 PCs)',[('ossian',1),('pallbearer',2)])): m.battle(c,n,cr,MAP)
m.battle('L1','03 The Larder (Harrow and four ghouls; not foes)',[('harrow',1),('larderghoul',4)],MAP)
for it in m._cat('battle').find(m.BAT['L1'].split('.')[1]).find('npclist'): it.find('faction').text='neutral'
# ---- item ----
UP=os.path.join(VAULT,'50-Items','The Urn of Saint Merrow.md')
m.item('urn','The Urn of Saint Merrow','Wondrous Item',C(fullnote(UP).split('## History')[0]),rarity='Uncommon')
# ---- reference manual ----
I1,A1,A2,A3,AP='Introduction','Act 1 — The Chapel','Act 2 — The Catacombs','Act 3 — The Ossuary','Appendices'
SC=lambda n: P('Scenes/Scene 0%d —*.md'%n)
B3=[m.B(c) for c in ('E1a','E1b','E1c')]+[m.B('L1')]
for x in (CODE+' — Bestiary',CODE+' — Map Assets',CODE+' — Art Brief',CODE+' — Board','Build-Pipeline'): fgconv.SEEN.append(x)
cover=['cover'] if has('cover') else []
m.page(I1,'Cover','<p><b>APL 7 (levels 6–8) · 4–6 characters · one 3–4 hour session</b></p><p><i>The mortician thanks you for coming. He thanks you for everything. He never once blinks.</i></p><p>OP1 · A Sidebar Press Pocket Module · November 2026. Setting-agnostic.</p>',images=cover)
HOWTO=('<h>How to Use This Module</h><p>The whole adventure, in order of play: three scenes, then the ending. The fight has ready-made combat tracker entries for 4, 5 and 6 PCs, '
 'plus a <b>Larder</b> entry (Harrow and four ghouls, set to neutral) to add alongside. Every statblock is in the NPC list; the Urn is in Items.</p>'
 '<p><b>Boxed text:</b> read it as written or paraphrase it, but keep every clue. Stats are 2014 5e.</p>')
m.page(I1,'Credits & How to Use','<p><b>What the Dead Fear</b> · %s · Sidebar Press. Statblocks marked SRD are from the 5E SRD 5.1 (CC-BY-4.0). The avolakia statblock is original to Sidebar Press.</p>'%CODE+HOWTO+C(pick(M,'Design Frame')))
m.page(I1,'Background & Hooks',C(pick(M,'Background','Hooks')))
m.page(I1,'Encounters & Cast',C(pick(M,'Encounters','Key NPCs','Key Locations')),links=B3+[m.N(k) for k in ('ossian','harrow','larderghoul','pallbearer')])
m.page(A1,'Scene 1 — The Grateful Mortician',C(fullnote(SC(1))),images=[i for i in ('portrait-ossian-guise',) if has(i)],links=[m.N('ossian')])
m.page(A2,'Scene 2 — The Catacombs',C(fullnote(SC(2))),images=[i for i in ('map-merrows-rest-key',) if has(i)],links=[m.N('larderghoul')])
s3=[i for i in ('scene-the-trap','plate-ossian','portrait-sexton-harrow','map-saints-ossuary-dm') if has(i)]
m.page(A3,'Scene 3 — What the Dead Fear',C(fullnote(SC(3))),images=s3+([MAP] if MAP else []),links=B3+[m.N('ossian'),m.N('harrow'),m.IT('urn')]+([m.I(MAP)] if MAP else []))
m.page(A3,'Concluding the Adventure',C(pick(M,'Concluding the Adventure')),links=[m.IT('urn')])
m.page(AP,'Bestiary',C(fullnote(BEST)),links=[m.N(k) for k in m.NPC])
m.page(AP,'The Urn of Saint Merrow',C(fullnote(UP).split('## Continuity')[0]),links=[m.IT('urn')])
# ---- build ----
m.LINT=[r'SP-OP01-What',r'SP-OP01 — (Bestiary|Board|Map|Art)',r'FGU Import',r'30-NPCs']
OUT=os.path.join(ADV,'FGU Kit',NAME+'.mod')
m.build(WORK+'.mod',cover_image='cover' if cover else None)
if '--test' in sys.argv: sys.exit(0)
shutil.copyfile(WORK+'.mod',OUT)
if '--install' in sys.argv: shutil.copyfile(OUT,os.path.join(FG,'modules',NAME+'.mod')); print('installed to FG modules')
