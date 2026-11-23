# ---- SP-GS02 handouts (shareable story records) and the reference manual (exec'd by module.py) ----
HO={}; HIMG={"Aunt Sedge's Letter":'handout-letter','The Long Night Carol':'handout-carol',"Corin's Drawings":'handout-corins-drawings',
             "The Miners' Map":'handout-miners-map',"The Apprentice's Carving":'handout-carving'}
for h in sorted(glob.glob(os.path.join(SRC,'*Handout —*.md'))):
    title=re.search(r'^title: "(.*)"',open(h).read(),re.M).group(1); short=title.split('— ',1)[1]; key=re.sub(r'[^a-z]','',short.lower())
    fgconv.NAMES[os.path.basename(h)[:-3]]=title
    quote='\n'.join(l for l in fullnote(h).split('\n') if l.startswith('>'))  # the player-facing text only; DM notes stay in the book
    if "Apprentice" in short: quote=quote.split('> **In the Suel')[0]   # the counter-verse's meaning is for a reader of Suloise only
    xml=C(quote) if quote.strip() else '<p><i>Show the players the picture.</i></p>'
    r=_S(m._cat('encounter'),key); _S(r,'name','string','%s (Player Handout)'%short); _FT(r,'text',xml); fgconv.SEEN.clear()
    HO[title]=(h,('encounter','encounter.'+key,'Handout: '+short),HIMG.get(short))
H=lambda t: HO['Handout — '+t][1]
I1,A1,A2,A3,A4,AP,PP='Introduction','Act 1 — The Gathering','Act 2 — The Howling','Act 3 — The Long Night','Session 4 (optional)','Appendices','People & Places'
B=lambda *c: [m.B(x) for x in c]
BB=lambda c: [m.B(c+s) for s in 'abc']
m.page(I1,'Cover','<p><b>APL 6 (levels 5–7) · 5 characters (scales to 4–6) · three sessions of 3–4 hours (optional fourth)</b></p>'
       '<p><i>Every Midwinter Night, Candlecrown sings seven verses to Telchur. This year, something has come down out of the cold to collect the seventh.</i></p>'
       '<p>A Sidebar Press Greyhawk Special. Candlecrown, the Tors, Needfest 1–5, 576 CY.</p>',images=['cover'])
HOWTO=('<h>How to Use This Module</h><p>This reference manual is the whole adventure in order of play. Read <b>Running the Adventure</b>, <b>Run Sheet &amp; Trackers</b> and <b>The Lantern Line</b> before Session 1.</p><list>'
 '<li><b>Scenes 01–13</b>, one page each, grouped by session. Each page lists its encounters, NPCs, items and maps in the <b>Records for this page</b> box at the foot.</li>'
 '<li><b>Encounters</b> come in three sizes: <b>a</b> for 4 PCs, <b>b</b> for 5 (the default) and <b>c</b> for 6, all at level 6. Minion packs add four bodies at a time.</li>'
 '<li><b>Bestiary</b>: every statblock is in the NPC list. Statblocks marked SRD are from the 5E SRD 5.1 (CC-BY-4.0).</li>'
 '<li><b>For the players:</b> five handouts in the Story list, plus their pictures in the Images list. The seventh verse is never written down, here or anywhere.</li>'
 '<li><b>Maps</b> have no grid. Set the grid by the square count in each map\'s name (for example, M1 is 17 × 30 squares).</li></list>'
 '<p><b>Boxed text:</b> read it as written or paraphrase it, but keep every clue. Stats are 2014 5e.</p>')
m.page(I1,'Credits & How to Use','<p><b>The Long Night at Candlecrown</b> · GS2 · Sidebar Press. The immoth is adapted from the 3e <i>Monster Manual II</i>; tyrgs from the 2e <i>Monstrous Compendium</i>. Statblocks marked SRD are from the 5E SRD 5.1 (CC-BY-4.0).</p>'+HOWTO+C(pick(M,'Pitch','Design Frame','PC Objectives','Act Structure')))
m.page(I1,'Background & Hooks',C(pick(F,'Introduction','Background','Adventure Outline','Hooks')),links=[H("Aunt Sedge's Letter")])
m.page(I1,'Running the Adventure',C(pick(F,'Running the Adventure')))
m.page(I1,'Run Sheet & Trackers',C('\n'.join('## %s\n%s'%(k,v) for k,v in X.items() if k.startswith(('Run Sheet','Standing','Clue Ledger','Climax')))))
m.page(I1,'The Lantern Line',C(fullnote(LL)))
m.page(I1,'Encounters',C(pick(M,'Encounters')),links=[m.B(c) for c in m.BAT])
CAST=['npc-brannoc','npc-sedge','npc-wenna','npc-corin','npc-pell-ash','npc-dob-tansy','npc-aurel']
m.page(I1,'Cast & Locations',C(pick(M,'Key NPCs','Key Locations')),images=CAST,place={k:'$end' for k in CAST},links=[m.N(k) for k in ('aurel','hrimvald','sedge','dob')])
def scene(sec,n,imgs=(),links=()):
    p=SC(n); m.page(sec,os.path.basename(p)[:-3],C(fullnote(p)),images=list(imgs),links=list(links))
MI=lambda k: m.I(k)
scene(A1,1,['scene-candle-stair'],BB('E01')+[m.B('M1'),m.N('tyrg'),m.N('tyrgminion'),MI('map-m1-candle-stair'),MI('map-r1-region')])
scene(A1,2,['scene-workshop'],[m.N('villager'),m.N('sedge'),m.N('dob'),H('The Long Night Carol'),H("The Miners' Map"),MI('map-t1-candlecrown'),MI('map-m2-candlecrown'),MI('map-m2-hall-workshop'),MI('handout-carol-lantern')])
scene(A1,3,['npc-corin'],[H("Corin's Drawings"),MI('handout-corins-drawings')])
scene(A1,4,['npc-dob-tansy'],B('E04')+[m.B('M1'),m.N('tyrg'),m.N('hrimvald'),MI('map-m2-hall-workshop')])
scene(A2,5,['scene-chapel'],BB('E05')+BB('E05x')+[m.B('M2'),m.N('guardian'),m.N('rimeshard'),m.N('aurel'),H("The Apprentice's Carving"),H("The Miners' Map"),m.IT('tailtip'),m.IT('signet'),m.IT('pendant'),m.IT('rubbing'),MI('map-m3-old-workings')])
m.page(A2,'The Old Workings (site key)',C(fullnote(OW)),images=['map-m3-old-workings'],links=BB('E05')+[m.N('guardian'),m.N('aurel'),m.N('tyrg'),m.IT('tailtip'),m.IT('signet'),m.IT('pendant'),MI('handout-carving')])
scene(A2,6,[],BB('E06')+[m.B('M1'),m.N('tyrg'),m.N('hrimvald'),MI('map-m1-candle-stair')])
scene(A2,7,['npc-wenna'],[m.IT('wennapaper'),H('The Long Night Carol')])
scene(A2,8,['scene-gate'],BB('E05x')+[m.N('aurel'),m.N('dob'),MI('map-m2-candlecrown')])
scene(A3,9,[],[m.N('gateguard'),m.N('villager'),MI('map-m2-candlecrown'),MI('map-m2-hall-workshop')])
scene(A3,10,['scene-long-night'],BB('E10a')+BB('E10b')+BB('E10c')+[m.B('M1'),m.N('tyrg'),m.N('tyrgalpha'),m.N('guardian'),m.N('gateguard'),MI('map-m1-candle-stair'),MI('map-m2-hall-workshop'),MI('map-m2-candlecrown')])
scene(A3,11,['scene-seventh-verse'],B('E11','E11x','M1')+[m.N('hrimvald'),m.N('tyrgalpha'),m.N('sedge'),m.IT('wennapaper'),m.IT('rubbing'),m.IT('heartrune'),MI('map-m2-candlecrown')])
scene(A3,12,['npc-brannoc'],[m.IT('lantern'),m.IT('heartrune'),m.IT('tailtip'),m.IT('signet'),m.IT('pendant')])
scene(A4,13,[],BB('E13')+[m.B('M2'),m.N('hrimvald'),m.N('guardian'),m.N('rimeshard'),m.IT('ringwarmth'),m.IT('wandweb'),MI('map-m4-ice-library')])
m.page(AP,'Bestiary',C(fullnote(BEST)),links=[m.N(k) for k in m.NPC])
for title,(h,ln,img) in sorted(HO.items()):
    m.page(AP,title,C(fullnote(h)),images=[img] if img else [],links=[ln]+([MI(img)] if img else []))
m.page(AP,'Magic Items & Treasure','<h>Magic Items &amp; Treasure</h><p>Click a name to open the item record, which you can drag to a character sheet.</p>'+''.join(
       '<p><b>%s</b></p><linklist><link class="item" recordname="%s">%s</link></linklist>'%(html.escape(m.ITEMN[k]),m.ITEM[k],html.escape(m.ITEMN[k])) for k in m.ITEM))
MP=[k for k in PRETTY if k.startswith('map-')]
m.page(AP,'Maps','<p>Battlemaps have no grid. In Fantasy Grounds, set the grid so the square count in each map\'s name fits the image (M1 is 17 × 30 squares, M2 80 × 80, the hall-and-workshop inset 30 × 20, M3 60 × 50, M4 50 × 40). T1 is the players\' town overview; R1 is a draft region map.</p>',links=[m.I(k) for k in MP])
# ---- People & Places: every vault note the adventure names ----
OUTSIDE=['Candlecrown','The Candlecrown Gate','The Stair-Head Winch','The Lantern Workshop','The Workshop Hall',"Mother Sedge's Shrine",'Candlecrown Green',"Corin's Fold",
         'The Mine Head (Candlecrown)','The Fallow Kiln','The Carrow Oil-House','The Teller Storehouse','The Candle Stair','The Old Workings (Candlecrown)','The Ice Library',
         'Brannoc Tull','Old Mother Sedge','Wenna Tull','Corin the Shepherd','Pell and Ash','Dob Kettle','Tansy Kettle','Hob Fallow','Marra Fallow',
         'Ivo Pike','Nell Amberson','Agna Rusk','Garth Vossmer','Edda Carrow','Osric Teller','Aldo Holm','Aurel Vasch','Hrimvald the Gatherer',
         'The Curse of Binding','Needfest','Telchur','Fortubo','The-Tors','League-of-the-Yeomanry','Melkot','Passage-of-Slerotin']
PIC={'Brannoc Tull':'npc-brannoc','Old Mother Sedge':'npc-sedge','Wenna Tull':'npc-wenna','Corin the Shepherd':'npc-corin','Pell and Ash':'npc-pell-ash',
     'Dob Kettle':'npc-dob-tansy','Tansy Kettle':'npc-dob-tansy','Aurel Vasch':'npc-aurel','Candlecrown':'map-t1-candlecrown','The Candle Stair':'scene-candle-stair'}
REC={'Aurel Vasch':[m.N('aurel')],'Hrimvald the Gatherer':[m.N('hrimvald')],'Old Mother Sedge':[m.N('sedge')],'Dob Kettle':[m.N('dob')],
     'Candlecrown':[MI('map-m2-candlecrown'),MI('map-t1-candlecrown')],'The Old Workings (Candlecrown)':[MI('map-m3-old-workings')],'The Ice Library':[MI('map-m4-ice-library')]}
for n in OUTSIDE:
    p=NOTEP(n)
    if not p: print('WARN note not found, skipped:',n); continue
    m.page(PP,fgconv.NAMES.get(n,n),C(fullnote(p)),images=[PIC[n]] if n in PIC else [],links=REC.get(n,[]))
