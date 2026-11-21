"""SP-GA05 The Pilgrims of the Hollow Bell -> Fantasy Grounds module. Run: python3 module.py [--install]
Uses the shared builder in 70-Company/Tools/fgu-module-builder (see the fgu-module-build skill).
Sellable master edition: no Friday-table material (Pip, Elric's squire, the FNFT insert)."""
import os,sys,re,glob,shutil,html
HERE=os.path.dirname(os.path.abspath(__file__)); ADV=os.path.dirname(os.path.dirname(HERE)); VAULT=ADV
while not os.path.isdir(os.path.join(VAULT,'70-Company')): VAULT=os.path.dirname(VAULT)  # works at any folder depth (In Development/, Completed/)
sys.path.insert(0,os.path.join(VAULT,'70-Company','Tools','fgu-module-builder'))
from fgmod import Mod, conv, body, sections, _S, _FT
import fgconv, zipfile, xml.etree.ElementTree as ET
FG=os.environ.get('FG_DIR',os.path.expanduser('~/mnt/Fantasy Grounds'))
# ---- edition settings (a renamed edition changes only this block) ----
CODE='SP-GA05'; NAME='SP-GA05 The Pilgrims of the Hollow Bell'; DISPLAY='SP-GA05 — The Pilgrims of the Hollow Bell'
SRC=ADV; ASSETS=os.path.join(VAULT,'99-Assets',CODE); TEXT_MAP={}
EXCLUDE_IMAGES=('portrait-pip-thistlebottom','map-kalbach-print')                       # Friday-table only
RENAME_IMAGES={'token-zombie-pip':'token-zombie-signaller','portrait-elrics-squire':'portrait-kalbach-letter-writer','SP-PBS-05 map-orc-camp':'map-orc-camp'}
DROP_SECTIONS=('Friday Night Field Trips Insert','Open Items')       # DM's Notes sections left out of the sold module
FRAME='Greyhawk University'
# Vault note names as the module shows them (wikilinks resolve through these; CODE+' — ' is stripped from the rest)
fgconv.STRIP=[CODE+' — ']
fgconv.NAMES={CODE+" — DM's Notes":'Running the Adventure',CODE+'-The-Pilgrims-of-the-Hollow-Bell':'this adventure',
              CODE+" — Player Gazetteer — The Field Warden's Primer":"The Field Warden's Primer"}
# Module-only wording: the print book is organised in Parts, the module in Scenes; vault-only notes are dropped.
FIX=[(r'\(<b>Part 1\s*</b>\)','(<b>Scenes 1–2</b>)'),(r'\(<b>Part 2, Easy\s*</b>\)','(<b>Scene 3, Easy</b>)'),(r'\(<b>Part 3, Medium\s*</b>\)','(<b>Scene 4, Medium</b>)'),
     (r'\(<b>Part 4, Hard\s*</b>\)','(<b>Scene 5, Hard</b>)'),(r'\(<b>Part 5, Deadly\s*</b>\)','(<b>Scene 6, Deadly</b>)'),(r'Then go to <b>Part 1\s*</b>','Then go to <b>Scene 1: The Field Office</b>'),
     (r'\(Part 1\)','(Scene 2)'),(r'\(Part 4\)','(Scene 5)'),(r'Start at Part 3','Start at Scene 4'),(r'\(Parts 1–2\)','(Scenes 2–3)'),(r'Each Part takes away','Each scene takes away'),
     (r'<td><b>Part</b></td>','<td><b>Scene</b></td>'),(r'<tr><td>1</td><td>The garrison','<tr><td>1–2</td><td>The garrison'),(r'<tr><td>2</td><td>The village','<tr><td>3</td><td>The village'),
     (r'<tr><td>3</td><td>The relay','<tr><td>4</td><td>The relay'),(r'<tr><td>4</td><td>The road','<tr><td>5</td><td>The road'),(r'<tr><td>5</td><td>Time','<tr><td>6</td><td>Time'),
     (r'Part 5, the Bell-Tor crown','Scene 6, the Bell-Tor crown'),(r'(Scene \d) of this adventure',r'\1'),(r'Full encounter:','Run'),
     (r'\(house hamlet, table canon; ~1 day SE of Ritterstadt\)','(hamlet, about a day southeast of Ritterstadt)'),(r'\s*Transit on the drove roads gets no note\.',''),
     (r'; full table in Running the Adventure',''),(r'\s*Details in Running the Adventure\.',''),(r'Each has its own note in Side Quests/:','See Continuing: Side Quests:'),
     (r'the theme beat in the main note','the theme beat in Scene 4'),(r'Encounter loot is listed in each encounter note','Encounter loot is listed on each encounter page'),
     (r"DM's Notes",'Running the Adventure'),(r'this adventure: (Scene)',r'\1')]
# -----------------------------------------------------------------------
WORK=os.path.expanduser(os.environ.get('FG_WORK','~/work/fgu')+'/'+CODE); FLAT=WORK+'-src'; os.makedirs(FLAT,exist_ok=True)
def ikey(f):  # vault asset file name -> module image key
    n=os.path.splitext(f)[0]
    for pre in (CODE+' ','SP-PBS-05 '): n=n[len(pre):] if n.startswith(pre) else n  # old-code asset names
    return RENAME_IMAGES.get(n,n)
for f in glob.glob(os.path.join(ASSETS,'*','*')):
    if os.path.basename(os.path.dirname(f)).startswith('_'): continue  # _brew-hosted etc. are not module art
    k=ikey(os.path.basename(f)); dst=os.path.join(FLAT,k+os.path.splitext(f)[1].lower())
    if os.path.isfile(f) and k not in EXCLUDE_IMAGES and (not os.path.exists(dst) or os.path.getmtime(f)>os.path.getmtime(dst)): shutil.copyfile(f,dst)  # skip folders; refresh changed art
# The finished cover (title + Sidebar Press logo) is the module cover and thumbnail; the bare painting stays as 'cover-art'.
_fc=os.path.join(VAULT,'99-Assets','_Covers','Cover — '+NAME.split(' ',1)[1]+'.png')
if os.path.exists(_fc[:-4]+' (color).png'): _fc=_fc[:-4]+' (color).png'   # the module always shows the colour cover when there is one
for x in glob.glob(os.path.join(FLAT,'cover.*')):
    if x.endswith('cover.png'): os.remove(x); continue  # our own copy from a previous run
    os.replace(x,os.path.join(FLAT,'cover-art'+os.path.splitext(x)[1]))
shutil.copyfile(_fc,os.path.join(FLAT,'cover.png'))
# Colour/B&W pairs (Sidebar Press, 2026-11-20): FGU and Homebrewery use '<name>-color' when it exists, print uses '<name>-print'.
for f in glob.glob(os.path.join(FLAT,'*-print.*')): os.remove(f)
for f in glob.glob(os.path.join(FLAT,'*-color.*')):
    base=os.path.splitext(f)[0][:-len('-color')]
    if os.path.basename(base)=='cover': base=os.path.join(FLAT,'cover-art')   # colour cover painting; the titled cover is cover.png
    for g in glob.glob(base+'.*'): os.remove(g)
    os.replace(f,base+os.path.splitext(f)[1])
# Daylight copies of the night battle maps (maps/_day): extra image records only; the reference manual shows the night maps.
for f in glob.glob(os.path.join(ASSETS,'maps','_day','*-color (day).*')):
    k=ikey(os.path.basename(f).replace('-color (day)','-day')); dst=os.path.join(FLAT,k+os.path.splitext(f)[1].lower())
    if not os.path.exists(dst) or os.path.getmtime(f)>os.path.getmtime(dst): shutil.copyfile(f,dst)
# Round, transparent tokens for FGU (print art keeps its white ground). Creature tokens are converted in place;
# NPCs whose portrait doubles as their token get a separate round 'token-<name>' copy.
import fgtoken
for f in glob.glob(os.path.join(FLAT,'token-*.*')):
    if os.path.splitext(f)[1].lower() not in ('.jpg','.jpeg','.png','.webp'): continue
    out=os.path.splitext(f)[0]+'.png'; fgtoken.make(f,out)
    if f!=out: os.remove(f)
PORTRAIT_TOKENS=['ansgar-vell','sister-halse','grukka-one-tusk','cathal-red-torc']
for k in PORTRAIT_TOKENS:
    src=glob.glob(os.path.join(FLAT,'portrait-'+k+'.*'))[0]; fgtoken.make(src,os.path.join(FLAT,'token-'+k+'.png'),ringed=False)
m=Mod(NAME,DISPLAY,'Sidebar Press','Sidebar Press',FG,WORK,text_map=TEXT_MAP)
m.images(FLAT)
P=lambda pat: glob.glob(os.path.join(SRC,pat))[0]
NOTE=lambda folder,name: os.path.join(VAULT,folder,name+'.md')
for h in glob.glob(os.path.join(SRC,'*Handout —*.md')):
    tt=re.search(r'^title: "(.*)"',open(h).read(),re.M)
    if tt: fgconv.NAMES[os.path.basename(h)[:-3]]=tt.group(1)
MAIN=P(CODE+'-The-Pilgrims*.md'); DMN=P("*DM's Notes.md"); BEST=P('*Bestiary.md'); PRIMER=P('*Field Warden*.md')
# ---- helpers: images from embeds, art callouts stripped, sections ----
EMB=re.compile(r'!\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]')
def imgs(t): return [k for k in (ikey(x) for x in EMB.findall(t)) if k in m.IMG and k not in EXCLUDE_IMAGES]
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
M=sections(body(MAIN)); D=sections(body(DMN))
pick=lambda S,*n: '\n'.join('## %s\n%s'%(x,S[x]) for x in n if x in S)
def subs(t):  # split a Part section at its ### headings
    out=[]; cur=None
    for l in t.split('\n'):
        mm=re.match(r'^### (.*)',l)
        if mm: cur=[mm.group(1).strip(),[]]; out.append(cur)
        elif cur: cur[1].append(l)
    return [(a,'\n'.join(b)) for a,b in out]
PART={k:subs(v) for k,v in M.items() if k.startswith('Part ')}
def fullnote(p): return re.sub(r'^# .*\n','',body(p),count=1)
# ---- homebrew NPCs, parsed from each note's ## FGU Import block ----
def fgu_block(p):
    return re.search(r'## FGU Import.*?```text\n(.*?)```',open(p).read(),re.S).group(1).strip().split('\n')
def homebrew(key,p,token=None,picture=None):
    L=fgu_block(p); name=L[0]; st=L[1]; sz,rest=st.split(' ',1); typ,align=rest.rsplit(', ',1)
    ac,actext=re.match(r'Armor Class (\d+)\s*(.*)',L[2]).groups(); hp,hd=re.match(r'Hit Points (\d+)\s*(.*)',L[3]).groups()
    speed=L[4][6:]; ab=[int(x) for x in re.findall(r'(\d+) \(',L[6])]
    f={}; i=7
    while not L[i].startswith('Proficiency Bonus'):
        for lab in ('Saving Throws','Skills','Damage Vulnerabilities','Damage Resistances','Damage Immunities','Condition Immunities','Senses','Languages','Challenge'):
            if L[i].startswith(lab+' '): f[lab]=L[i][len(lab)+1:]
        i+=1
    cr,xp=re.match(r'(\S+) \(([\d,]+) XP\)',f['Challenge']).groups(); i+=1
    traits,actions,cur=[],[],None; tgt=traits
    for l in L[i:]:
        if l=='Actions': tgt=actions; continue
        mm=re.match(r"^([A-Z][A-Za-z' -]{1,40})\. (.*)",l)
        if mm and not l.startswith(('Cantrips','1st','2nd','3rd')): cur=[mm.group(1),mm.group(2)]; tgt.append(cur)
        elif l.strip() and cur: cur[1]+='\n'+l
    text=' '.join(x.strip('- ') for x in re.findall(r'^- \*\*(?:Description|Appearance|In this adventure|Animal variant):\*\* .*$',body(p),re.M))
    text=re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]',r'\1',text).replace('**','').replace('*','')
    m.npc(key,name,sz,typ,align,int(ac),actext,int(hp),hd,speed,ab,cr,int(xp.replace(',','')),f.get('Senses',''),f.get('Languages',''),
          traits=[tuple(t) for t in traits],actions=[tuple(a) for a in actions],skills=f.get('Skills',''),saves=f.get('Saving Throws',''),
          immunities=f.get('Damage Immunities',''),text=text,picture=picture or token)
    e=m._cat('npc').find(key)
    for lab,tag in (('Damage Resistances','damageresistances'),('Damage Vulnerabilities','damagevulnerabilities'),('Condition Immunities','conditionimmunities')):
        if lab in f: _S(e,tag,'string',f[lab])
    if token: _S(e,'token','token',m.imgpath(token)); m.TOK[key]=m.imgpath(token)
def srd(src,name,key,token,dress,**kw):
    m.npc_srd(src,name,key,dress=dress,picture=token,**kw)
    e=m._cat('npc').find(key); old=e.find('token')
    if old is not None: e.remove(old)
    _S(e,'token','token',m.imgpath(token)); m.TOK[key]=m.imgpath(token)
# ---- NPCs ----
homebrew('ansgar',NOTE('30-NPCs','Brother-Reaper Ansgar Vell'),picture='portrait-ansgar-vell',token='token-ansgar-vell')
homebrew('halse',NOTE('30-NPCs','Sister Halse'),picture='portrait-sister-halse',token='token-sister-halse')
homebrew('grukka',NOTE('30-NPCs','Grukka One-Tusk'),picture='portrait-grukka-one-tusk',token='token-grukka-one-tusk')
homebrew('cathal',NOTE('30-NPCs','Cathal Red-Torc'),picture='portrait-cathal-red-torc',token='token-cathal-red-torc')
homebrew('barrowdead',NOTE('65-Bestiary/'+CODE,'Barrow Dead'),token='token-barrow-skeleton')
homebrew('pennyrisen',NOTE('65-Bestiary/'+CODE,'Penny-Risen'),token='token-zombie-villager')

homebrew('pennyrisensignaller',NOTE('65-Bestiary/'+CODE,'Penny-Risen'),token='token-zombie-signaller')
m._cat('npc').find('pennyrisensignaller').find('name').text='Penny-Risen (Relay Signaller)'
def animal(key,label,token):  # the Bestiary's animal variant: Small, speed 30 ft., Bite instead of Slam
    homebrew(key,NOTE('65-Bestiary/'+CODE,'Penny-Risen'),token=token); e=m._cat('npc').find(key)
    e.find('name').text='Penny-Risen (%s)'%label; e.find('size').text='Small'; e.find('speed').text='30 ft.'; e.find('languages').text='-'
    a=e.find('actions')[0]; a.find('name').text='Bite'; a.find('desc').text='Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) piercing damage.'
animal('pennyrisenlamb','Lamb','token-zombie-lamb'); animal('pennyrisenfox','Fox','token-zombie-fox'); animal('pennyrisendog','Dog','token-zombie-dog')
homebrew('ghoulrider',NOTE('65-Bestiary/'+CODE,'Ghoul Rider'),token='token-ghoul-rider')
srd('acolyte','Grey Sickle Acolyte','sickleacolyte','token-grey-sickle-acolyte','Rust-red habit under undyed grey. On the Tor they ring the bell stair and cast sanctuary on Ansgar first, then sacred flame on anyone climbing. A muffle torn off the bell is an acolyte\'s action.',overrides={'alignment':'neutral evil','type':'humanoid (human)','languages':'Common, Flan'},keep_srd_text=False)
srd('orc','Orc Deserter','orcdeserter','token-orc-deserter',"One of Grukka's band, out of Iuz's war in the Vesve. Paid in green Flan grave-silver and uneasy about it. Turned orcs fight with the wardens on the Tor.")
srd('ridinghorse','The Relay Horse (Riding Horse)','relayhorse','token-relay-horse',"A dead Hollen Ford rider's horse. Calmed (Animal Handling DC 10), it follows the wardens and carries one up the Tor path at full speed.")
# ---- spells: the adventure's homebrew spells as 5E spell records ----
SPELLS={}
for sn in ('Ash Tally',"Reaper's Tithe",'Hollowing Toll'):
    sp=P('Spells/%s.md'%sn); raw=open(sp).read(); fm=raw.split('\n---',1)[0]
    g=lambda k: (re.search(r'^%s: *(.*)$'%k,fm,re.M) or [None,''])[1].strip().strip('"')
    bt=re.sub(r'^\s*# [^\n]*\n','',body(sp),count=1).split('## Notes for the DM')[0]
    f={k:v.strip() for k,v in re.findall(r'^- \*\*([A-Za-z ]+):\*\* (.*)$',bt,re.M)}
    rules=re.sub(r'^- \*\*(Casting Time|Range|Components|Duration|Classes):\*\*.*\n','',bt,flags=re.M)
    rules=re.sub(r'^\*\d\w\w-level[^\n]*\*\n','',rules.lstrip(),count=1)
    classes=re.sub(r'\s*\*\(([^)]*)\)\*','',f['Classes']); note=(re.search(r'\*\(([^)]*)\)\*',f['Classes']) or [None,''])[1]
    key=re.sub(r'[^a-z]','',sn.lower())
    f={k:fgconv.plain(v) for k,v in f.items()}
    m.spell(key,sn,int(g('level')),g('school').title(),g('ritual')=='true',f['Casting Time'],f['Range'],f['Components'],f['Duration'],classes,
            C(rules)+('<p><i>Sidebar Press. %s.</i></p>'%html.escape(note[0].upper()+note[1:]) if note else ''))
    SPELLS[sn.lower()]=(int(g('level')),'Level: %s\nCasting Time: %s\nComponents: %s\nDuration: %s\nRange: %s\n%s\nSee the %s spell record for full text.\n'%(
        g('level'),f['Casting Time'],f['Components'],f['Duration'],f['Range'],re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',html.unescape(C(rules.split('\n\n')[0])))).strip(),sn))
# NPC spell lists: SRD text and roll data from DD5E SRD Data, homebrew spells from the notes above
_srdx=ET.fromstring(zipfile.ZipFile(os.path.join(FG,'modules','DD5E SRD Data.mod')).read('client.xml'))
_srdsp={(e.findtext('name') or '').lower():e for e in next(x for x in _srdx.iter() if x.tag=='spelldata').iter() if e.find('name') is not None and e.find('level') is not None}
def spell_lookup(nm):
    if nm.lower() in SPELLS: return SPELLS[nm.lower()]
    e=_srdsp[nm.lower()]; d=re.sub(r'\s*\n\s*','\n',re.sub(r'<[^>]+>','\n',ET.tostring(e.find('description'),encoding='unicode'))).strip()
    return (int(e.findtext('level')),'Level: %s\nCasting Time: %s\nComponents: %s\nDuration: %s\nRange: %s\n%s\n'%(e.findtext('level'),e.findtext('castingtime'),e.findtext('components'),e.findtext('duration'),e.findtext('range'),html.unescape(d)))
for k in ('ansgar','halse'): m.npc_spells(k,spell_lookup)
# ---- encounters (one per party size) ----
PR,GH='pennyrisen','ghoulrider'
for c,n,cr in (('E1a','01 Kalbach Churchyard (4 PCs)',[(PR,3),('pennyrisenlamb',1)]),('E1b','01 Kalbach Churchyard (5 PCs)',[(PR,3),('pennyrisenlamb',1),('pennyrisendog',1)]),('E1c','01 Kalbach Churchyard (6 PCs)',[(PR,3),('pennyrisenlamb',2),('pennyrisendog',1)])): m.battle(c,n,cr,'map-kalbach')
for c,n,cr in (('E2a','02 Hollen Ford Relay (4 PCs)',[(GH,1),('pennyrisensignaller',1),(PR,1),('pennyrisenfox',1)]),('E2b','02 Hollen Ford Relay (5 PCs)',[(GH,2),('pennyrisensignaller',1),('pennyrisenfox',1)]),('E2c','02 Hollen Ford Relay (6 PCs)',[(GH,2),('pennyrisensignaller',1),(PR,2),('pennyrisenfox',1)])): m.battle(c,n,cr,'map-hollen-ford-relay')
for c,n,k in (('E3a','03 The Orc Camp (4 PCs)',2),('E3b','03 The Orc Camp (5 PCs)',4),('E3c','03 The Orc Camp (6 PCs)',5)): m.battle(c,n,[('grukka',1),('orcdeserter',k)],'map-orc-camp')
m.battle('R3','03 Orc Camp - Foraging Party (if the horn sounds, round 3)',[('orcdeserter',2)],'map-orc-camp')
for c,n,a,b in (('E4a','04 Thirteen Tolls (4 PCs)',2,0),('E4b','04 Thirteen Tolls (5 PCs)',2,2),('E4c','04 Thirteen Tolls (6 PCs)',4,4)):
    m.battle(c,n,[('ansgar',1),('halse',1),('sickleacolyte',a)]+([('barrowdead',b)] if b else []),'map-bell-tor')
m.battle('W4','04 Wave - Barrow Dead (1 per toll)',[('barrowdead',1)],'map-bell-tor')
m.battle('X4','04 Toll 13 - Cathal Red-Torc rises',[('cathal',1)],'map-bell-tor')
# ---- items (from 50-Items notes) ----
def itemtext(p):
    t=re.sub(r'^\s*# [^\n]*\n','',body(p),count=1); t=re.sub(r'^\*[^\n]*\*\n','',t.lstrip(),count=1)
    return C(t)
for key,name,typ,rar,pic in (('reaperspenny',"Reaper's Penny",'Wondrous Item','Common','item-reapers-penny'),('boneclapper','The Bone Clapper','Wondrous Item','Uncommon','item-bone-clapper'),
    ('sunbell','The Sun-Bell of Carn Aedh','Wondrous Item','Very Rare','item-sun-bell'),('yatilambskin','The Yati Lambskin','Wondrous Item','Uncommon','item-yati-lambskin'),('redtorc','Red Torc of Cathal','Wondrous Item','Uncommon','portrait-cathal-red-torc')):
    rl=re.search(r'^\*(Wondrous item[^\n]*)\*',fullnote(NOTE('50-Items',name)).lstrip(),re.M)
    m.item(key,name,typ,'<h>%s</h><p><i>%s</i></p>'%(html.escape(name),html.escape(rl.group(1) if rl else ''))+itemtext(NOTE('50-Items',name)),rarity=rar,picture=pic)
# ---- the Primer as a shareable story record ----
pr=_S(m._cat('encounter'),'primer'); _S(pr,'name','string',"The Field Warden's Primer (Player Handout)"); _FT(pr,'text',C(fullnote(PRIMER)))
PRIM=('encounter','encounter.primer',"Story: The Field Warden's Primer")
# ---- quests: one per side-quest note (Player Lead -> description; seed, lead credit and links -> GM notes) ----
QLINKS={"The Grey Sickle's List":lambda:[m.N('halse'),m.SP('ashtally')],'The Copper-Torc Dead':lambda:[m.N('barrowdead')],'The Grave-Silver':lambda:[],
        'Ansgar Returns':lambda:[m.N('ansgar'),m.IT('boneclapper'),m.IT('sunbell')],"Grukka's Deserters":lambda:[m.N('grukka')],'Hollen Ford Must Be Manned':lambda:[m.N('relayhorse')]}
QKEY=lambda n: re.sub(r'^the','',re.sub(r'[^a-z]','',n.lower()))
for q in sorted(glob.glob(os.path.join(SRC,'Side Quests','*.md'))):
    qn=os.path.basename(q)[:-3]; qs=sections(body(q)); lv=re.search(r'^levels: "APL ([^"]*)"',open(q).read(),re.M)
    m.quest(QKEY(qn),qn,lv.group(1).replace('–','-') if lv else '',C(qs.get('Player Lead','')),C(pick(qs,'The Seed','Lead Credit')),links=QLINKS.get(qn,lambda:[])())
# ---- reference manual ----
I1,A1,A2,A3,AP='Introduction','Act 1 — The Road and Kalbach','Act 2 — Hollen Ford and the Orc Camp','Act 3 — The Bell-Tor','Appendices'
ENC=lambda n: P('Encounters/*E%d —*.md'%n)
B3=lambda e: [m.B(e+x) for x in 'abc']
m.page(I1,'Cover','<p><b>APL 3 (level 3) · 4–6 characters · one 4-hour session</b></p><p><i>Nobody\'s coming to save you.</i></p><p>A Sidebar Press adventure for the %s campaign frame.</p>'%FRAME,images=['cover'])
HOWTO=('<h>How to Use This Module</h><p>This reference manual is the whole adventure, start to finish, in order of play. Supporting pages:</p><list>'
 '<li><b>Running the Adventure</b>, <b>Encounter Curve &amp; Lanes</b> and <b>Weather, Gods &amp; the Land</b>: the Notice track, the time budget, scaling, alert states, rumors, the Lore Ladder and the weather. <b>Read them once before running.</b></li>'
 '<li>Encounter pages, each with its map, tactics, scaling and loot: E1 to E4. Each encounter has ready-made combat tracker entries for 4, 5 and 6 PCs.</li>'
 '<li><b>Bestiary</b>: every statblock (also in the NPC list). New spells are in the Spells list; new items in the Items list.</li>'
 "<li>For the players: The Field Warden's Primer (a story entry you can share) and six handouts.</li></list>"
 '<p><b>Boxed text:</b> read it as written or paraphrase it, but keep every clue. <b>Conventions:</b> creature counts in parentheses are the scaling dial. Stats are 2014 5e. <b>ESSENTIAL CLUE</b> marks a fact the players must not miss.</p>')
for x in ("SP-GA05 — DM's Notes",'SP-GA05 — E1 — The Kalbach Churchyard','SP-GA05 — E2 — The Hollen Ford Relay','SP-GA05 — E3 — The Orc Camp','SP-GA05 — E4 — Thirteen Tolls','SP-GA05 — Bestiary'): fgconv.SEEN.append(x)
m.page(I1,'Credits & How to Use','<p><b>The Pilgrims of the Hollow Bell</b> · %s · Sidebar Press. Statblocks marked SRD are from the 5E SRD 5.1 (CC-BY-4.0).</p>'%CODE+HOWTO+C(pick(M,'Design Frame')))
m.page(I1,'Opening Narration',C(pick(M,'Opening Narration')),links=[PRIM])
m.page(I1,'Background',C(pick(M,'Background','Adventure Outline')),images=['map-route-overview'])
m.page(I1,'Facts & Hooks',C(pick(M,'Facts the Players Must Learn','Hooks')),images=imgs(M.get('Hooks','')))
m.page(I1,'Running the Adventure',C(pick(D,'Running the Theme: *Nobody\'s coming to save you*','Time Budget (4 hours)','The Notice Track (Parts 1–2)',"Ansgar's Alert States",'Factions','Rumors (d6)')))
m.page(I1,'Encounter Curve & Lanes',C(pick(D,'Encounter Curve (2014 DMG)','Every Seat Has a Lane')),links=[m.B(c) for c in m.BAT])
m.page(I1,'Weather, Gods & the Land',C(pick(D,'Weather and Sky (Patchwall 23–25, 576 CY)','Learning the Gods (the Lore Ladder)','The Grieving Land')))
m.page(I1,'Cast & Locations',C(pick(M,'Key NPCs','Key Locations')),images=['portrait-ansgar-vell','portrait-sister-halse','portrait-grukka-one-tusk','portrait-cathal-red-torc','portrait-udo-pfaff','portrait-brenna','portrait-field-office-clerk'],
  links=[m.N(k) for k in ('ansgar','halse','grukka','cathal')],place={k:'$end' for k in ('portrait-ansgar-vell','portrait-sister-halse','portrait-grukka-one-tusk','portrait-cathal-red-torc','portrait-udo-pfaff','portrait-brenna','portrait-field-office-clerk')})
def scene(sec,part,i,links=(),place=None):  # place: {image: anchor}; only placed images go on scene pages
    h,t=PART[part][i]; m.page(sec,h,C(t),images=list(place or {}),links=links,place=place)
P1,P2,P3,P4,P5=[k for k in PART]
scene(A1,P1,0,[PRIM],{'handout-4-field-office-notice':'>The Field Office smells','portrait-field-office-clerk':'Wendel Krafft','handout-1-sketch-map':'$end','map-route-overview':'$end'})
scene(A1,P1,1,(),{'scene-procession':'Ten figures'})
scene(A1,P2,0,B3('E1')+[m.N(PR),m.IT('reaperspenny')],{'scene-kalbach-dusk':'Kalbach is a dozen','portrait-udo-pfaff':'Sexton Udo Pfaff','portrait-brenna':'Brenna, a Yati','handout-5-winter-telling':'>Brenna, a Yati','item-reapers-penny':'The well.'})
def encpage(sec,n,links,place):
    t=fullnote(ENC(n)); m.page(sec,os.path.basename(ENC(n))[len(CODE)+3:-3],C(t),images=list(place),links=links,place=place)
encpage(A1,1,B3('E1')+[m.N(PR),m.N('pennyrisenlamb'),m.N('pennyrisendog'),m.I('map-kalbach'),m.IT('reaperspenny')],{'map-kalbach':'Creatures'})
scene(A2,P3,0,B3('E2')+[m.N(GH),m.N('relayhorse')],{'handout-2-relay-log':'Who is here','handout-3-halse-notes-p1':'Theme beat','handout-3-halse-notes-p2':'Theme beat','scene-hollen-ford-beacon':'Theme beat'})
encpage(A2,2,B3('E2')+[m.N(GH),m.N('pennyrisensignaller'),m.N('pennyrisenfox'),m.N('relayhorse'),m.I('map-hollen-ford-relay')],{'map-hollen-ford-relay':'Site Key'})
scene(A2,P4,0,B3('E3')+[m.N('grukka')],{'portrait-grukka-one-tusk':'Grukka One-Tusk'})
encpage(A2,3,B3('E3')+[m.B('R3'),m.N('grukka'),m.N('orcdeserter'),m.I('map-orc-camp')],{'map-orc-camp':'Site Key','portrait-grukka-one-tusk':'O3. GRUKKA'})
scene(A3,P5,0,B3('E4')+[m.B('W4'),m.B('X4'),m.IT('sunbell'),m.IT('boneclapper')],{'scene-bell-tor':"The Tor's crown",'portrait-ansgar-vell':"Ansgar's greeting",'portrait-sister-halse':"Ansgar's greeting",
  'portrait-cathal-red-torc':'Ways to stop the bell','item-sun-bell':'Ways to stop the bell','item-bone-clapper':'Ways to stop the bell'})
encpage(A3,4,B3('E4')+[m.B('W4'),m.B('X4'),m.N('ansgar'),m.N('halse'),m.N('sickleacolyte'),m.N('barrowdead'),m.N('cathal'),m.I('map-bell-tor'),m.IT('sunbell'),m.IT('boneclapper'),m.IT('redtorc'),m.SP('hollowingtoll')],
  {'map-bell-tor':'Site Key','portrait-ansgar-vell':'Tactics','portrait-sister-halse':'Tactics','portrait-cathal-red-torc':'Toll 13 —'})
_cc=M['Concluding the Adventure']; _pre,_rew=_cc.split('### Rewards Beyond Credits',1); _pre=re.sub(r'### Credits\n.*','',_pre,flags=re.S)  # one credits table: the DM's Notes version
m.page(A3,'Concluding the Adventure',C('## Concluding the Adventure\n'+_pre)+C(pick(D,'Credits (Greyhawk University frame)'))+C('### Rewards Beyond Credits'+_rew),images=['item-yati-lambskin'],
  links=[m.IT('yatilambskin'),m.IT('redtorc')],place={'item-yati-lambskin':'B — The Reaper'})
m.page(AP,'Bestiary',C(re.sub(r'^# .*\n','',body(BEST),count=1)),links=[m.N(k) for k in m.NPC])
for s in ('Ash Tally',"Reaper's Tithe",'Hollowing Toll'): m.page(AP,'Spell — '+s,C(fullnote(P('Spells/%s.md'%s))),links=[m.SP(re.sub(r'[^a-z]','',s.lower()))])
MI=[('reaperspenny','item-reapers-penny'),('boneclapper','item-bone-clapper'),('sunbell','item-sun-bell'),('yatilambskin','item-yati-lambskin'),('redtorc',None)]
def blurb(k):  # name, type line and first paragraph of the item, plus a link to the record
    d=m._cat('item').find(k).find('description'); kids=list(d); typ=ET.tostring(kids[1],encoding='unicode'); first=next(ET.tostring(x,encoding='unicode') for x in kids[2:] if x.tag=='p')
    return '<p><b>%s</b></p>%s%s<linklist><link class="item" recordname="%s">%s</link></linklist>'%(html.escape(m.ITEMN[k]),typ,first,m.ITEM[k],html.escape(m.ITEMN[k]))
m.page(AP,'Magic Items','<h>Magic Items</h><p>The adventure\'s homebrew items. Click a name to open the item record, which you can drag to a character sheet.</p>'+''.join(blurb(k) for k,_ in MI),
  images=[i for _,i in MI if i],place={i:m.ITEMN[k] for k,i in MI if i})
for h in sorted(glob.glob(os.path.join(SRC,'*Handout —*.md')),key=lambda p: re.search(r'Handout (\d)',open(p).read()).group(1)):
    t=fullnote(h); hi=imgs(t); m.page(AP,re.search(r'^title: "(.*)"',open(h).read(),re.M).group(1),C(t),images=hi,place={k:'$end' for k in hi})  # heading first, handout under it
m.page(AP,"The Field Warden's Primer",C(fullnote(PRIMER)),images=imgs(fullnote(PRIMER)),links=[PRIM])
m.page(AP,'Continuing: Side Quests',''.join(C('## '+os.path.basename(q)[:-3]+'\n'+fullnote(q).split('## Theme')[0]) for q in sorted(glob.glob(os.path.join(SRC,'Side Quests','*.md')))),links=[m.Q(k) for k in m.QUEST])
MAPS=['map-route-overview','map-kalbach','map-hollen-ford-relay','map-hollen-ford-tower','map-orc-camp','map-bell-tor']
DAYMAPS=['map-kalbach-day','map-hollen-ford-relay-day','map-orc-camp-day','map-bell-tor-day']
m.page(AP,'Maps','<p>Top-down colour maps for the route and the four encounters, the relay tower\'s interior, and a keyed GM copy of Kalbach. Kalbach is shown at dusk and the relay, orc camp, and Bell-Tor at night, as they are played; daylight versions of those four are linked below. Encounter tokens are already placed: add an encounter to the Combat Tracker and its creatures appear on the map. No grid is set: calibrate it in Fantasy Grounds (5-ft. squares) before play.</p>',images=MAPS,links=[m.I(k) for k in MAPS+DAYMAPS])
# ---- build ----
m.LINT=[r'SP-GA05-The',r'SP-GA05 — (E\d|Bestiary|Handout|Player)',r'\bParts? [1-5]\b',r'table canon']
OUT=os.path.join(ADV,'FGU Kit',NAME+'.mod')
m.build(WORK+'.mod',cover_image='cover')
import place_tokens; print('tokens placed on maps:',place_tokens.apply(WORK+'.mod'))
if '--test' in sys.argv: sys.exit(0)  # build and lint only; leave the shipped .mod alone
shutil.copyfile(WORK+'.mod',OUT)
if '--install' in sys.argv: shutil.copyfile(OUT,os.path.join(FG,'modules',NAME+'.mod')); print('installed to FG modules')
