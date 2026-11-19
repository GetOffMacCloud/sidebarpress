# ---- SP-GS01 extra loot items and treasure parcels (exec'd by module.py after module_npcs.py) ----
for key,name,typ,rar,xml in (
  ('hearthfeather',"Old Gobbler's Hearth Feather",'Wondrous Item','Common',
   "<p>A huge slate-grey feather from above Widow Bree's hearth (Scene 02, H2). Once, a creature holding it has advantage on the Wisdom saving throw against the Gluttonwretch's Aura of Endless Hunger.</p>"),
  ('lastfeather',"Old Gobbler's Last Feather",'Wondrous Item','Common',
   "<p>Given by the calmed Offering-Heap (Scene 04). Laid on the feast table, it counts as a seventh Offering slot that only Jaroo can fill: if he places it, the rite needs one fewer household Offering.</p>"),
  ('slate','Smokehouse Delivery Slate','Adventuring Gear','',
   '<p>Found at S2 in the Smokehouse (Scene 05). A delivery list: forty barrels "to the green, Brewfest noon."</p>'),
  ('ledger',"The Traders' Cipher Ledger",'Adventuring Gear','',
   "<p>Under Rannos and Gremag's counter (Scene 02, H3); DC 17 Intelligence (Investigation) to find it unnoticed. Written in Temple cipher: the proof that the traders supply the Rotting Table. See the Cipher Ledger handout.</p>"),
  ('scroll','Spell Scroll (Cloudkill)','Scroll','Rare',
   '<p>From the Deacon\'s hoard (Ending B). A <i>spell scroll</i> of <i>cloudkill</i> (5th level; save DC 17, attack +9).</p>'),
  ('wishbonehalf','Larger Half of the Wishbone','Wondrous Item','Legendary',
   '<p>If the Wishbone of Old Gobbler was snapped (Ending B), whoever keeps the larger half gains a single <i>wish</i>, limited to duplicating a spell of 7th level or lower. The bone then crumbles.</p>')):
    m.item(key,name,typ,'<h>%s</h>'%html.escape(name)+xml,rarity=rar)
def parcel(key,name,items,coins=()):
    r=_S(m._cat('treasureparcels'),key); _S(r,'name','string',name); cl=_S(r,'coinlist')
    for j,(amt,cur) in enumerate(coins,1): c=_S(cl,ids(j)); _S(c,'amount','number',amt); _S(c,'description','string',cur)
    il=_S(r,'itemlist')
    for j,k in enumerate(items,1):
        src=m._cat('item').find(k); e=copy.deepcopy(src); e.tag=ids(j); _S(e,'count','number',1); il.append(e)
    m.PARCEL[key]='treasureparcels.'+key; m.PARCELN[key]=name
m.PARCEL={}; m.PARCELN={}
parcel('p02bree',"02 Widow Bree's Cottage (H2)",['hearthfeather'])
parcel('p02traders',"02 The Traders' Establishment (H3)",['ledger'])
parcel('p04grove',"04 The Grove: the calmed Offering-Heap",['lastfeather'])
parcel('p05smokehouse','05 The Smokehouse (S2, S5, S6)',['slate','wishbone','cipherbook'])
parcel('p07endinga','07 Ending A: The First Fruits',['feather'])
parcel('p07endingb','07 Ending B: The Wishbone',['cipherbook','scroll','wishbonehalf'])
PL=lambda k: ('treasureparcel',m.PARCEL[k],'Parcel: '+m.PARCELN[k])
