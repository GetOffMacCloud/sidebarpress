"""SP-GA05 The Pilgrims of the Hollow Bell -> Fantasy Grounds module. Run: python3 module.py [--install]
Uses the shared builder in 70-Company/Tools/fgu-module-builder (see the fgu-module-build skill).
Sellable master edition: no Friday-table material (Pip, Elric's squire, the FNFT insert)."""
import os,sys,re,glob,shutil,html
HERE=os.path.dirname(os.path.abspath(__file__)); ADV=os.path.dirname(os.path.dirname(HERE)); VAULT=os.path.dirname(os.path.dirname(ADV))
sys.path.insert(0,os.path.join(VAULT,'70-Company','Tools','fgu-module-builder'))
from fgmod import Mod, conv, body, sections, _S, _FT
FG=os.environ.get('FG_DIR',os.path.expanduser('~/mnt/Fantasy Grounds'))
# ---- edition settings (a renamed edition changes only this block) ----
CODE='SP-GA05'; NAME='SP-GA05 The Pilgrims of the Hollow Bell'; DISPLAY='SP-GA05 — The Pilgrims of the Hollow Bell'
SRC=ADV; ASSETS=os.path.join(VAULT,'99-Assets',CODE); TEXT_MAP={}
EXCLUDE_IMAGES=('portrait-pip-thistlebottom',)                       # Friday-table only
RENAME_IMAGES={'token-zombie-pip':'token-zombie-signaller','portrait-elrics-squire':'portrait-kalbach-letter-writer'}
DROP_SECTIONS=('Friday Night Field Trips Insert','Open Items')       # DM's Notes sections left out of the sold module
FRAME='Greyhawk University'
# -----------------------------------------------------------------------
WORK=os.path.expanduser('~/work/fgu/'+CODE); FLAT=WORK+'-src'; os.makedirs(FLAT,exist_ok=True)
def ikey(f):  # vault asset file name -> module image key
    n=os.path.splitext(f)[0]; n=n[len(CODE)+1:] if n.startswith(CODE+' ') else n
    return RENAME_IMAGES.get(n,n)
for f in glob.glob(os.path.join(ASSETS,'*','*')):
    k=ikey(os.path.basename(f)); dst=os.path.join(FLAT,k+os.path.splitext(f)[1].lower())
    if k not in EXCLUDE_IMAGES and not os.path.exists(dst): shutil.copyfile(f,dst)
m=Mod(NAME,DISPLAY,'Sidebar Press','Sidebar Press',FG,WORK,text_map=TEXT_MAP)
m.images(FLAT)
P=lambda pat: glob.glob(os.path.join(SRC,pat))[0]
NOTE=lambda folder,name: os.path.join(VAULT,folder,name+'.md')
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
def C(t): return conv(noart(t))
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
def srd(src,name,key,token,dress):
    m.npc_srd(src,name,key,dress=dress,picture=token)
    e=m._cat('npc').find(key); old=e.find('token')
    if old is not None: e.remove(old)
    _S(e,'token','token',m.imgpath(token)); m.TOK[key]=m.imgpath(token)
# ---- NPCs ----
homebrew('ansgar',NOTE('30-NPCs','Brother-Reaper Ansgar Vell'),picture='portrait-ansgar-vell',token='portrait-ansgar-vell')
homebrew('halse',NOTE('30-NPCs','Sister Halse'),picture='portrait-sister-halse',token='portrait-sister-halse')
homebrew('grukka',NOTE('30-NPCs','Grukka One-Tusk'),picture='portrait-grukka-one-tusk',token='portrait-grukka-one-tusk')
homebrew('cathal',NOTE('30-NPCs','Cathal Red-Torc'),picture='portrait-cathal-red-torc',token='portrait-cathal-red-torc')
homebrew('barrowdead',NOTE('65-Bestiary/'+CODE,'Barrow Dead'),token='token-barrow-skeleton')
homebrew('pennyrisen',NOTE('65-Bestiary/'+CODE,'Penny-Risen'),token='token-zombie-villager')
homebrew('pennyrisenlamb',NOTE('65-Bestiary/'+CODE,'Penny-Risen'),token='token-zombie-lamb')
m._cat('npc').find('pennyrisenlamb').find('name').text='Penny-Risen (Lamb)'
homebrew('pennyrisensignaller',NOTE('65-Bestiary/'+CODE,'Penny-Risen'),token='token-zombie-signaller')
m._cat('npc').find('pennyrisensignaller').find('name').text='Penny-Risen (Relay Signaller)'
homebrew('pennyrisenfox',NOTE('65-Bestiary/'+CODE,'Penny-Risen'),token='token-zombie-fox')
m._cat('npc').find('pennyrisenfox').find('name').text='Penny-Risen (Fox)'
homebrew('ghoulrider',NOTE('65-Bestiary/'+CODE,'Ghoul Rider'),token='token-ghoul-rider')
srd('acolyte','Grey Sickle Acolyte','sickleacolyte','token-grey-sickle-acolyte','Rust-red habit under undyed grey. On the Tor they ring the bell stair and cast sanctuary on Ansgar first, then sacred flame on anyone climbing. A muffle torn off the bell is an acolyte\'s action.')
srd('orc','Orc Deserter','orcdeserter','token-orc-deserter',"One of Grukka's band, out of Iuz's war in the Vesve. Paid in green Flan grave-silver and uneasy about it. Turned orcs fight with the wardens on the Tor.")
srd('ridinghorse','The Relay Horse (Riding Horse)','relayhorse','token-relay-horse',"A dead Hollen Ford rider's horse. Calmed (Animal Handling DC 10), it follows the wardens and carries one up the Tor path at full speed.")
# ---- encounters (one per party size) ----
PR,GH='pennyrisen','ghoulrider'
for c,n,cr in (('E1a','01 Kalbach Churchyard (4 PCs)',[(PR,3),('pennyrisenlamb',1)]),('E1b','01 Kalbach Churchyard (5 PCs)',[(PR,4),('pennyrisenlamb',1)]),('E1c','01 Kalbach Churchyard (6 PCs)',[(PR,4),('pennyrisenlamb',2)])): m.battle(c,n,cr,'map-kalbach')
for c,n,cr in (('E2a','02 Hollen Ford Relay (4 PCs)',[(GH,1),('pennyrisensignaller',1),(PR,1),('pennyrisenfox',1)]),('E2b','02 Hollen Ford Relay (5 PCs)',[(GH,2),('pennyrisensignaller',1),('pennyrisenfox',1)]),('E2c','02 Hollen Ford Relay (6 PCs)',[(GH,2),('pennyrisensignaller',1),(PR,2),('pennyrisenfox',1)])): m.battle(c,n,cr,'map-hollen-ford-relay')
for c,n,k in (('E3a','03 The Orc Camp (4 PCs)',2),('E3b','03 The Orc Camp (5 PCs)',4),('E3c','03 The Orc Camp (6 PCs)',5)): m.battle(c,n,[('grukka',1),('orcdeserter',k)],'map-orc-camp')
for c,n,a,b in (('E4a','04 Thirteen Tolls (4 PCs)',2,0),('E4b','04 Thirteen Tolls (5 PCs)',2,2),('E4c','04 Thirteen Tolls (6 PCs)',4,4)):
    m.battle(c,n,[('ansgar',1),('halse',1),('sickleacolyte',a)]+([('barrowdead',b)] if b else []),'map-bell-tor')
m.battle('W4','04 Wave - Barrow Dead (1 per toll)',[('barrowdead',1)],'map-bell-tor')
m.battle('X4','04 Toll 13 - Cathal Red-Torc rises',[('cathal',1)],'map-bell-tor')
# ---- items (from 50-Items notes) ----
def itemtext(p):
    t=fullnote(p); t=re.sub(r'^\*[^\n]*\*\n','',t.lstrip(),count=1)
    return C(t)
for key,name,typ,rar,pic in (('reaperspenny',"Reaper's Penny",'Wondrous Item','Common','item-reapers-penny'),('boneclapper','The Bone Clapper','Wondrous Item','Uncommon','item-bone-clapper'),
    ('sunbell','The Sun-Bell of Carn Aedh','Wondrous Item','Very Rare','item-sun-bell'),('yatilambskin','The Yati Lambskin','Wondrous Item','Uncommon','item-yati-lambskin'),('redtorc','Red Torc of Cathal','Wondrous Item','Uncommon','portrait-cathal-red-torc')):
    rl=re.search(r'^\*(Wondrous item[^\n]*)\*',fullnote(NOTE('50-Items',name)).lstrip(),re.M)
    m.item(key,name,typ,'<p><i>%s</i></p>'%html.escape(rl.group(1) if rl else '')+itemtext(NOTE('50-Items',name)),rarity=rar,picture=pic)
# ---- the Primer as a shareable story record ----
pr=_S(m._cat('encounter'),'primer'); _S(pr,'name','string',"The Field Warden's Primer (Player Handout)"); _FT(pr,'text',C(fullnote(PRIMER)))
PRIM=('encounter','encounter.primer',"Story: The Field Warden's Primer")
# ---- reference manual ----
I1,A1,A2,A3,AP='Introduction','Act 1 — The Road and Kalbach','Act 2 — Hollen Ford and the Orc Camp','Act 3 — The Bell-Tor','Appendices'
ENC=lambda n: P('Encounters/*E%d —*.md'%n)
B3=lambda e: [m.B(e+x) for x in 'abc']
m.page(I1,'Cover','<p><b>APL 3 (level 3) · 4–6 characters · one 4-hour session</b></p><p><i>Nobody\'s coming to save you.</i></p><p>A Sidebar Press adventure for the %s campaign frame.</p>'%FRAME,images=['cover'])
m.page(I1,'Credits & How to Use','<p><b>The Pilgrims of the Hollow Bell</b> · %s · Sidebar Press. Statblocks marked SRD are from the 5E SRD 5.1 (CC-BY-4.0).</p>'%CODE+C(pick(M,'Adventure Code','How to Use This Note','Design Frame')))
m.page(I1,'Opening Narration',C(pick(M,'Opening Narration')),links=[PRIM])
m.page(I1,'Background',C(pick(M,'Background','Adventure Outline')),images=['map-route-overview'])
m.page(I1,'Facts & Hooks',C(pick(M,'Facts the Players Must Learn','Hooks')),images=imgs(M.get('Hooks','')))
m.page(I1,'Running the Adventure',C(pick(D,'Running the Theme: *Nobody\'s coming to save you*','Time Budget (4 hours)','The Notice Track (Parts 1–2)',"Ansgar's Alert States",'Factions','Rumors (d6)')))
m.page(I1,'Encounter Curve & Lanes',C(pick(D,'Encounter Curve (2014 DMG)','Every Seat Has a Lane')),links=[m.B(c) for c in m.BAT])
m.page(I1,'Weather, Gods & the Land',C(pick(D,'Weather and Sky (Patchwall 23–25, 576 CY)','Learning the Gods (the Lore Ladder)','The Grieving Land')))
m.page(I1,'Cast & Locations',C(pick(M,'Key NPCs','Key Locations')),images=['portrait-ansgar-vell','portrait-sister-halse','portrait-grukka-one-tusk','portrait-cathal-red-torc','portrait-udo-pfaff','portrait-brenna','portrait-field-office-clerk'],
  links=[m.N(k) for k in ('ansgar','halse','grukka','cathal')])
def scene(sec,part,i,links=()):
    h,t=PART[part][i]; m.page(sec,h,C(t),images=imgs(t),links=links)
P1,P2,P3,P4,P5=[k for k in PART]
scene(A1,P1,0,[PRIM]); scene(A1,P1,1)
scene(A1,P2,0,B3('E1')+[m.N(PR),m.IT('reaperspenny')])
def encpage(sec,n,links):
    t=fullnote(ENC(n)); m.page(sec,os.path.basename(ENC(n))[len(CODE)+3:-3],C(t),images=imgs(t),links=links)
encpage(A1,1,B3('E1')+[m.N(PR),m.N('pennyrisenlamb'),m.I('map-kalbach'),m.IT('reaperspenny')])
scene(A2,P3,0,B3('E2')+[m.N(GH),m.N('relayhorse')]); encpage(A2,2,B3('E2')+[m.N(GH),m.N('pennyrisensignaller'),m.N('pennyrisenfox'),m.N('relayhorse'),m.I('map-hollen-ford-relay')])
scene(A2,P4,0,B3('E3')+[m.N('grukka')]); encpage(A2,3,B3('E3')+[m.N('grukka'),m.N('orcdeserter'),m.I('map-orc-camp')])
scene(A3,P5,0,B3('E4')+[m.B('W4'),m.B('X4'),m.IT('sunbell'),m.IT('boneclapper')])
encpage(A3,4,B3('E4')+[m.B('W4'),m.B('X4'),m.N('ansgar'),m.N('halse'),m.N('sickleacolyte'),m.N('barrowdead'),m.N('cathal'),m.I('map-bell-tor'),m.IT('sunbell'),m.IT('boneclapper'),m.IT('redtorc')])
m.page(A3,'Concluding the Adventure',C(pick(M,'Concluding the Adventure'))+C(pick(D,'Credits (Greyhawk University frame)')),images=imgs(M['Concluding the Adventure']),links=[m.IT('yatilambskin'),m.IT('redtorc')])
m.page(AP,'Bestiary',C(re.sub(r'^# .*\n','',body(BEST),count=1)),links=[m.N(k) for k in m.NPC])
for s in ('Ash Tally',"Reaper's Tithe",'Hollowing Toll'): m.page(AP,'Spell — '+s,C(fullnote(P('Spells/%s.md'%s))))
m.page(AP,'Magic Items','<p>The adventure\'s homebrew items are in the Items list.</p>',images=['item-reapers-penny','item-bone-clapper','item-sun-bell','item-yati-lambskin'],links=[m.IT(k) for k in m.ITEM])
for h in sorted(glob.glob(os.path.join(SRC,'*Handout —*.md')),key=lambda p: re.search(r'Handout (\d)',open(p).read()).group(1)):
    t=fullnote(h); m.page(AP,re.search(r'^title: "(.*)"',open(h).read(),re.M).group(1),C(t),images=imgs(t))
m.page(AP,"The Field Warden's Primer",C(fullnote(PRIMER)),images=imgs(fullnote(PRIMER)),links=[PRIM])
m.page(AP,'Continuing: Side Quests',''.join(C('## '+os.path.basename(q)[:-3]+'\n'+fullnote(q).split('## Theme')[0]) for q in sorted(glob.glob(os.path.join(SRC,'Side Quests','*.md')))))
MAPS=['map-route-overview','map-kalbach','map-hollen-ford-relay','map-orc-camp','map-bell-tor']
m.page(AP,'Maps','<p>Top-down ink maps for the four encounters and the route. No grid is set: calibrate it in Fantasy Grounds (5-ft. squares) before play.</p>',images=MAPS,links=[m.I(k) for k in MAPS])
# ---- build ----
OUT=os.path.join(ADV,'FGU Kit',NAME+'.mod')
m.build(WORK+'.mod',cover_image='cover'); shutil.copyfile(WORK+'.mod',OUT)
if '--install' in sys.argv: shutil.copyfile(OUT,os.path.join(FG,'modules',NAME+'.mod')); print('installed to FG modules')
