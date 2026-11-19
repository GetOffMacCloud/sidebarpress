# ---- SP-GS01 location and quest records (exec'd by module.py after module_npcs.py) ----
LOC={}; LOCN={}
def L(k): return ('location',LOC[k],'Location: '+LOCN[k])
def tc(t): return ' '.join(w.capitalize() if i==0 or w.lower() not in ('of','the','and','a') else w.lower() for i,w in enumerate(t.split()))
def keyed(text,pfx):  # split a keyed-area section into {code: (title, markdown)}
    out={}; cur=None
    for l in text.split('\n'):
        mm=re.match(r'^\*\*(%s\d)\. ([^*]+?)\.?\*\*\.?\s*(.*)$'%pfx,l)
        if mm: cur=mm.group(1); out[cur]=[tc(mm.group(2).strip()),[mm.group(3)] if mm.group(3).strip() else []]
        elif cur: out[cur][1].append(l)
    return {k:(t,'\n'.join(b).strip()) for k,(t,b) in out.items()}
def location(key,name,typ,xml,picture=None,subs=()):
    r=_S(m._cat('location'),key); _S(r,'name','string',name); _S(r,'type','string',typ); _FT(r,'text',xml or '<p />')
    if picture: _S(r,'picture','token',m.imgpath(picture))
    LOC[key]='location.'+key; LOCN[key]=name; fgconv.SEEN.clear(); return r
def sublocs(key,kids):
    r=m._cat('location').find(key); s=_S(r,'sublocations')
    for j,k in enumerate(kids,1):
        e=_S(s,ids(j)); _S(e,'name','string',LOCN[k]); w=_S(e,'shortcut','windowreference'); _S(w,'class',None,'location'); _S(w,'recordname',None,LOC[k]); _S(e,'locked','number',1)
def links(xml,lst): return xml+('<p><b>Records</b></p><linklist>%s</linklist>'%''.join('<link class="%s" recordname="%s">%s</link>'%(c,rr,html.escape(l)) for c,rr,l in lst) if lst else '')
def locnote(n): return C(fullnote(NOTEP(n)))
S2=sections(fullnote(SC(2))); S5=sections(fullnote(SC(5))); S4=sections(fullnote(SC(4))); S7=sections(fullnote(SC(7)))
H=keyed(S2['Hommlet at a Glance'],'H'); SK=keyed(S5['Keyed Areas'],'S')
HPIC={'H2':'npc-widow-bree','H3':'map-t1-traders-establishment','H5':'map-t1-church-of-st-cuthbert','H1':'scene-the-elders-cellar'}
HREC={'H3':[m.N('rannos'),m.N('gremag'),m.B('T2')],'H5':[m.N('gorger')]}
for c,(t,b) in H.items():
    location('hommlet'+c.lower(),'%s. %s'%(c,t),'Building',links(C(b),HREC.get(c,[])),picture=HPIC.get(c))
SPIC={'S5':'scene-chapel-of-the-rotting-table'}
SREC={'S5':[m.N('brindlewick'),m.N('brother'),m.B('E2'),m.IT('wishbone')],'S6':[m.N('brindlewick'),m.IT('cipherbook')],'S4':[m.N('earthelemental')]}
for c,(t,b) in SK.items():
    location('smokehouse'+c.lower(),'%s. %s'%(c,t),'Keyed Area',links(C(b),SREC.get(c,[])),picture=SPIC.get(c))
location('feastgreen','The Feast Green','Site',links(C(S7.get('Climax at a Glance','')),[m.B('E4a'),m.B('E4b'),m.B('E4c'),m.B('E4d'),m.B('X4'),m.B('M4'),m.N('gluttonwretch')]),picture='map-m1-feast-green')
location('welcomewench','Inn of the Welcome Wench','Establishment',locnote('Inn of the Welcome Wench'),picture='map-t1-inn-of-the-welcome-wench')
location('jaroosgrove',"Jaroo's Grove",'Site',links(locnote("Jaroo's Grove"),[m.N('offeringheap'),m.B('E1')]),picture='map-m3-jaroos-grove')
location('hommlet','Hommlet','Settlement',locnote('Hommlet'),picture='map-t1-village-of-hommlet')
location('smokehouse','The Smokehouse','Site',links(locnote('The Smokehouse (Hommlet)'),[m.B('E2')]),picture='map-m2a-smokehouse-ground-floor')
location('emridymeadows','Emridy Meadows','Wilderness',links(locnote('Emridy Meadows'),[m.N('gluttonwretch'),m.B('E3')]),picture='map-m4-emridy-meadows')
location('verbobonc','The Viscounty of Verbobonc','Region',locnote('Viscounty-of-Verbobonc'))
sublocs('verbobonc',['hommlet','emridymeadows'])
sublocs('hommlet',['welcomewench','feastgreen']+['hommlet'+c.lower() for c in sorted(H) if c!='H6']+['jaroosgrove','smokehouse'])
if 'H6' in H: sublocs('welcomewench',['hommleth6'])
sublocs('smokehouse',['smokehouse'+c.lower() for c in sorted(SK)])
# ---- quests: what the players know (description) and the GM's side (notes + links) ----
P_=lambda *x: ''.join('<p>%s</p>'%t for t in x)
def Q(key,name,desc,gm,lk):
    m.quest(key,name,'',P_(*desc),P_(*gm),links=lk); _S(m._cat('quest').find(key),'xp','number',0)
Q('brewfest','Brewfest Under a Full Celene',
  ["Canon Terjon has asked you to bless Hommlet's Brewfest table at tomorrow night's feast. Villagers are falling sick with a \"fever\" that makes them eat what isn't food. Find out what is happening and keep Hommlet alive through the feast."],
  ['The main quest. The Gluttonwretch (Old Gobbler, starved when Hommlet kept back its 575 offering) comes to the feast through the Open Door on Brewfest 4 at dusk. Three ways to end it: six Offerings of first fruits (the good ending), snapping the Wishbone, or carving it down. Act 2 sets the feast\'s difficulty.'],
  [L('hommlet'),L('feastgreen'),m.N('gluttonwretch'),m.B('E4a'),m.B('E4d'),m.IT('wishbone'),m.IT('feather')])
Q('firstfruits','First Fruits',
  ['Jaroo says Old Gobbler can still be laid to rest: six offerings of this year\'s first fruits, given freely by the households that owe them. Not bought, not taken, not given by you. Win six households before the feast.'],
  ['The Grove path (Scene 04). Each household won becomes one Offering at the feast; Offerings can still be won during the fight. Only one Offering per round counts. See The First Fruits and the households table in Scene 04.'],
  [L('jaroosgrove'),m.N('offeringheap'),m.B('E1'),m.IT('feather')])
Q('rottingtable','The Rotting Table',
  ["Wat Thistlewood's six pigs walked into the Gnarley singing and ended up in the old Smokehouse up the High Road, where a man in brewer's leathers says grace to a wishbone the size of a boy. Take the Wishbone from the cult."],
  ['The Smokehouse path (Scene 05). Taking Brindlewick and the Wishbone here removes him from the feast. Snapping the bone weakens the Wretch but destroys Old Gobbler\'s spirit (Jaroo\'s warning). The cipher book is the sequel hook.'],
  [L('smokehouse'),m.N('brindlewick'),m.N('brother'),m.B('E2'),m.IT('wishbone'),m.IT('cipherbook')])
Q('roost','The Roost on Emridy Meadows',
  ['Drovers have seen the thing roosting on Emridy Meadows, where Hommlet fought in 569. Canon Terjon wants it wounded before it reaches the feast.'],
  ['The Meadows path (Scene 06). One round of fighting, then a three-round chase; the party always loses it over the Smokehouse smoke. Damage dealt carries over to the feast.'],
  [L('emridymeadows'),m.N('gluttonwretch'),m.B('E3')])
Q('fever','The Brewfest Fever',
  ['People across Hommlet are gorging on bread crusts, spoons, candles and worse, and the village insists it is a seasonal fever. Help the afflicted before they go hollow.'],
  ['Everyone who ate from the 575 harvest can gorge. Lesser restoration or DC 15 Wisdom (Medicine) ends one gorging; the curse ends only when the Wretch does. Uncured Ma Dunwold and Tam Thistlewood rise as Hollow Guests at the feast. See The Gorgings.'],
  [L('hommleth5'),m.N('gorger'),m.N('hobtanner'),m.B('M4')])
Q('preserves',"The Traders' Preserves",
  ['Rannos Davl and Gremag have been very generous with "preserves" for the Brewfest table, and their crates came from somewhere north.'],
  ['The traders are the cult\'s suppliers (Scene 02, H3). Exposing them before noon on Day 2 keeps their Flinger out of the barrels at the feast. The cipher ledger is the proof.'],
  [L('hommleth3'),m.N('rannos'),m.N('gremag'),m.B('T2')])
Q('secondtable','The Second Table',
  ["Brindlewick's cipher book is mostly recipes. Mostly. One page names a \"second table\" under the Temple."],
  ['A sequel hook (Continuing the Adventure). The Rotting Table, a Zuggtmoy cell, survives the Temple\'s fall.'],
  [m.IT('cipherbook')])
