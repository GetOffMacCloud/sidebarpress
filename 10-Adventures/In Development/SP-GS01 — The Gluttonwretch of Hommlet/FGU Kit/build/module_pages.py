# ---- SP-GS01 handouts (shareable story records) and the reference manual (exec'd by module.py) ----
HO={}
for h in sorted(glob.glob(os.path.join(SRC,'*Handout —*.md'))):
    title=re.search(r'^title: "(.*)"',open(h).read(),re.M).group(1); key=re.sub(r'[^a-z]','',title.lower())
    player=fullnote(h).split('\n## DM Notes')[0]
    r=_S(m._cat('encounter'),key); _S(r,'name','string','%s (Player Handout)'%title); _FT(r,'text',C(player)); fgconv.SEEN.clear()
    HO[title]=(h,('encounter','encounter.'+key,'Handout: '+title))
H=lambda t: HO[t][1]
I1,A1,A2,A3,AP,PP='Introduction','Act 1 — Brewfest Eve','Act 2 — Three Paths','Act 3 — The Feast','Appendices','People & Places'
B=lambda *c: [m.B(x) for x in c]
m.page(I1,'Cover','<p><b>APL 12 (level 12) · 7 characters · one 3½-hour session (4-hour hard cap)</b></p><p><i>"You did not feed me."</i></p>'
       '<p>A Sidebar Press Greyhawk Special. Hommlet, Brewfest 3–4, 576 CY, under a full Celene.</p>'
       '<p><i>Private stream edition. The Hommlet, inn, traders\' and church maps are traced from T1 The Village of Hommlet (TSR, 1979) for personal table use only.</i></p>',images=['cover'])
HOWTO=('<h>How to Use This Module</h><p>This reference manual is the whole adventure in order of play. Read <b>Running the Adventure</b> and <b>Run Sheet &amp; Trackers</b> once before the stream.</p><list>'
 '<li><b>Scenes 01–08</b>, one page each. Each page lists its encounters, NPCs, items and maps in the <b>Records for this page</b> box at the foot.</li>'
 '<li><b>Encounters</b> are built for <b>7 PCs at 12th level</b>. The feast has four versions (best case to worst case) so you can drop in the one Act 2 earned, plus Second Helpings and the uncured Gorgers as add-ons.</li>'
 '<li><b>Bestiary</b>: every statblock is also in the NPC list. The Gluttonwretch has two records, one per phase.</li>'
 '<li><b>For the players:</b> three handouts in the Story list, ready to share.</li>'
 '<li><b>Maps</b> come in a player version (no grid; set the grid to 100 px = 5 ft.) and a keyed GM version.</li></list>'
 '<p><b>Boxed text:</b> read it as written or paraphrase it, but keep every clue. Stats are 2014 5e. Every damage figure carries its dice.</p>')
m.page(I1,'Credits & How to Use','<p><b>The Gluttonwretch of Hommlet</b> · GS1 · Sidebar Press. The Gluttonwretch by GrimmGrixis (Writers Guild). Statblocks marked SRD are from the 5E SRD 5.1 (CC-BY-4.0). Hommlet and its people are from T1 The Village of Hommlet by Gary Gygax (TSR, 1979), used here for a private table.</p>'+HOWTO+C(pick(M,'Design Frame','Act Structure')))
m.page(I1,'Background & Hooks',C(pick(F,'Introduction','Background','Adventure Outline','Hooks')),links=[H("Who's Who in Hommlet"),H("Jaroo's Letter")]+[m.Q(k) for k in m.QUEST]+[L('hommlet'),L('verbobonc')])
m.page(I1,'Running the Adventure',C(pick(F,'Running the Adventure')))
m.page(I1,'Run Sheet & Trackers',C(pick(X,'Run Sheet — three and a half hours (4-hour hard cap)','Standing Trackers','Clue Ledger (tick as found)')))
m.page(I1,'Encounters',C(pick(M,'Encounters')),links=[m.B(c) for c in m.BAT])
CAST=['npc-brindlewick','npc-wat-thistlewood','npc-widow-bree','npc-pudding','npc-gluttonwretch','npc-offering-heap']
m.page(I1,'Cast & Locations',C(pick(M,'Key NPCs','Key Locations')),images=CAST,place={k:'$end' for k in CAST},links=[m.N(k) for k in ('gluttonwretch','offeringheap','brindlewick','rannos','gremag')])
def scene(sec,n,links=(),place=None):
    p=SC(n); m.page(sec,os.path.basename(p)[:-3],C(fullnote(p)),images=list(place or {}),links=links,place=place)
G=lambda k: m.I('gm-'+k)
scene(A1,1,[L('welcomewench'),H("Who's Who in Hommlet"),H("Jaroo's Letter"),m.I('map-t1-inn-of-the-welcome-wench'),G('t1-inn-of-the-welcome-wench')],
      {'scene-brewfest-eve':'Woodsmoke and cider','map-t1-inn-of-the-welcome-wench':'1. The welcome','npc-pudding':'2. The Open Door'})
scene(A1,2,B('T2')+[L('hommlet'),m.N('rannos'),m.N('gremag'),m.N('gorger'),H('The Cipher Ledger'),m.I('map-t1-village-of-hommlet'),G('t1-village-of-hommlet'),G('t1-traders-establishment'),G('t1-church-of-st-cuthbert')],
      {'map-t1-village-of-hommlet':'Hommlet at a Glance','map-t1-church-of-st-cuthbert':'H5. CHURCH','scene-the-elders-cellar':'Steps lead down','npc-widow-bree':'>H2. WIDOW','map-t1-traders-establishment':'>H3. THE TRADERS'})
scene(A1,3,[],{'npc-wat-thistlewood':'2. Wat speaks'})
scene(A2,4,B('E1')+[L('jaroosgrove'),m.Q('firstfruits'),m.N('offeringheap'),m.I('map-m3-jaroos-grove'),G('m3-jaroos-grove')],{'map-m3-jaroos-grove':'A ring of standing stones','npc-offering-heap':'$end'})
scene(A2,5,B('E2')+[L('smokehouse'),m.Q('rottingtable'),m.N('brindlewick'),m.N('brother'),m.N('earthelemental'),m.IT('wishbone'),m.IT('cipherbook'),m.I('map-m2a-smokehouse-ground-floor'),G('m2a-smokehouse-ground-floor'),m.I('map-m2b-smokehouse-cellar'),G('m2b-smokehouse-cellar')],
      {'map-m2a-smokehouse-ground-floor':'S1. THE YARD','map-m2b-smokehouse-cellar':'S4. THE CELLAR','scene-chapel-of-the-rotting-table':'>S5. CHAPEL','npc-brindlewick':'S6. BRINDLEWICK'})
scene(A2,6,B('E3')+[L('emridymeadows'),m.Q('roost'),m.N('gluttonwretch'),m.N('gorger'),m.N('flinger'),m.I('map-m4-emridy-meadows'),G('m4-emridy-meadows')],{'map-m4-emridy-meadows':'Grass grows high','scene-the-roost':'1. The roost'})
scene(A3,7,B('E4a','E4b','E4c','E4d','X4','M4')+[L('feastgreen'),m.Q('brewfest'),m.N('gluttonwretch'),m.N('secondhelpings'),m.N('hobtanner'),m.N('flinger'),m.N('brindlewick'),m.IT('wishbone'),m.IT('feather'),m.I('map-m1-feast-green'),G('m1-feast-green')],
      {'map-m1-feast-green':'Long tables run','cover-art':'Something fills','npc-gluttonwretch':'Part C'})
scene(A3,8,[m.IT('feather')],{'scene-the-last-toast':'Nobody goes home'})
m.page(A3,'Concluding the Adventure',C(pick(F,'Concluding the Adventure')),links=[m.IT('feather'),m.IT('wishbone'),m.IT('cipherbook')])
BI=['npc-gluttonwretch','npc-second-helpings','npc-offering-heap','npc-hollow-guests','npc-brindlewick']
m.page(AP,'Bestiary',C(fullnote(BEST)),images=BI,place={'npc-gluttonwretch':'>The Gluttonwretch','npc-second-helpings':'>The Gluttonwretch, Second Helpings','npc-offering-heap':'>The Offering-Heap',
       'npc-hollow-guests':'>Hollow Guests','npc-brindlewick':'>Deacon Mungo Brindlewick'},links=[m.N(k) for k in m.NPC])
for nm in ('The First Fruits','The Gorgings','Comedy Kit'): m.page(AP,nm,C(fullnote(P('*— %s.md'%nm))))
for title,(h,ln) in sorted(HO.items()): m.page(AP,title,C(fullnote(h)),links=[ln])
m.page(AP,'Magic Items','<h>Magic Items</h><p>Click a name to open the item record, which you can drag to a character sheet.</p>'+''.join(
       '<p><b>%s</b></p><linklist><link class="item" recordname="%s">%s</link></linklist>'%(html.escape(m.ITEMN[k]),m.ITEM[k],html.escape(m.ITEMN[k])) for k in ('feather','wishbone','cipherbook')))
MP=['map-'+k for k in MAPS.values()]+['gm-'+k for k in MAPS.values()]
m.page(AP,'Maps','<p>Player maps have no grid: in Fantasy Grounds set the grid to <b>100 px = 5 ft.</b> The GM versions carry the area keys. The four T1 maps are traced from the 1979 module for private use.</p>',images=[],links=[m.I(k) for k in MP])
# ---- People & Places: every outside note the adventure links to ----
OUTSIDE=['Hommlet','Inn of the Welcome Wench',"Jaroo's Grove",'The Smokehouse (Hommlet)','Emridy Meadows','Viscounty-of-Verbobonc','The-Common-Year-Calendar',
         'Canon Terjon','Deacon Mungo Brindlewick','Goodwife Gundigoot','Ostler Gundigoot','Jaroo Ashstaff','Lissa (Hommlet)','Mytch the Miller','Pip Haddle','Pudding',
         'Rannos Davl','Gremag','The Elder of Hommlet','Wat Thistlewood','Widow Marta Bree','The Rotting Table',"The Temple's Long Shadow"]
PIC={'Deacon Mungo Brindlewick':'npc-brindlewick','Wat Thistlewood':'npc-wat-thistlewood','Widow Marta Bree':'npc-widow-bree','Pudding':'npc-pudding'}
REC={'Deacon Mungo Brindlewick':[m.N('brindlewick')],'Rannos Davl':[m.N('rannos'),m.B('T2')],'Gremag':[m.N('gremag'),m.B('T2')]}
for n in OUTSIDE:
    t=fullnote(NOTEP(n)); im=[PIC[n]] if n in PIC else []
    m.page(PP,fgconv.NAMES.get(n,n),C(t),images=im,links=REC.get(n,[]))
