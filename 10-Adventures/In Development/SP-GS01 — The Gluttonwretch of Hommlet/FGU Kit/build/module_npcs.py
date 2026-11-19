# ---- SP-GS01 NPCs, spells, encounters and items (exec'd by module.py) ----
HEAD={'Actions':'actions','Bonus Actions':'bonusactions','Reactions':'reactions','Legendary Actions':'legendaryactions','Lair Actions':'lairactions'}
ITEMRX=re.compile(r"^([A-Z][^.]{1,60}?)\. (.+)$")
def fgu_block(p):
    return re.search(r'## FGU Import.*?```text\n(.*?)```',open(p).read(),re.S).group(1).strip().split('\n')
def addlist(e,tag,items):
    L=e.find(tag)
    if L is None: L=_S(e,tag)
    n=len(L)
    for nm,d in items: n+=1; it=_S(L,ids(n)); _S(it,'desc','string',d); _S(it,'name','string',nm)
def homebrew(key,p,picture=None,extra_traits=()):
    L=fgu_block(p); name=L[0]; sz,rest=L[1].split(' ',1); typ,align=rest.rsplit(', ',1)
    ac,actext=re.match(r'Armor Class (\d+)\s*\(?([^)]*)\)?',L[2]).groups(); hp,hd=re.match(r'Hit Points (\d+)\s*(.*)',L[3]).groups()
    speed=L[4][6:]; ab=[int(x) for x in re.findall(r'(\d+) \(',L[6])]
    f={}; i=7
    while not L[i].startswith('Challenge'):
        for lab in ('Saving Throws','Skills','Damage Vulnerabilities','Damage Resistances','Damage Immunities','Condition Immunities','Senses','Languages'):
            if L[i].startswith(lab+' '): f[lab]=L[i][len(lab)+1:]
        i+=1
    cr,xp=re.match(r'Challenge (\S+) \(([\d,]+) XP\)',L[i]).groups(); i+=1
    sec={'traits':[]}; cur=None; tgt=sec['traits']; intro={}
    for l in L[i:]:
        if l.strip() in HEAD: tgt=sec.setdefault(HEAD[l.strip()],[]); cur=None; continue
        mm=ITEMRX.match(l)
        if mm: cur=[mm.group(1),mm.group(2)]; tgt.append(cur)
        elif l.strip():
            if cur: cur[1]+='\n'+l
            else: intro[id(tgt)]=l
    traits=[tuple(t) for t in sec['traits']]+list(extra_traits)
    m.npc(key,name,sz,typ,align,int(ac),'('+actext+')' if actext else '',int(hp),hd.strip(),speed,ab,cr,int(xp.replace(',','')),f.get('Senses',''),f.get('Languages',''),
          traits=traits,actions=[tuple(a) for a in sec.get('actions',[])],bonus=[tuple(a) for a in sec.get('bonusactions',[])],reactions=[tuple(a) for a in sec.get('reactions',[])],
          skills=f.get('Skills',''),saves=f.get('Saving Throws',''),immunities=f.get('Damage Immunities',''),text='',picture=picture)
    e=m._cat('npc').find(key)
    for lab,tag in (('Damage Resistances','damageresistances'),('Damage Vulnerabilities','damagevulnerabilities'),('Condition Immunities','conditionimmunities')):
        if lab in f: _S(e,tag,'string',f[lab])
    for tag in ('legendaryactions','lairactions'):
        if sec.get(tag): addlist(e,tag,[tuple(a) for a in sec[tag]])
    if picture: _S(e,'token','token',m.imgpath(picture)); m.TOK[key]=m.imgpath(picture)
    return e
def notes(key,xml):  # replace the NPC's Notes tab text
    e=m._cat('npc').find(key); t=e.find('text')
    if t is not None: e.remove(t)
    _FT(e,'text',xml)
def retext(key,subs):  # rename words through every name/desc of an SRD copy
    for x in m._cat('npc').find(key).iter():
        if x.tag in ('name','desc') and x.text:
            for a,b in subs: x.text=x.text.replace(a,b)
def act(key,lst,old,name=None,desc=None):
    for it in m._cat('npc').find(key).find(lst):
        if it.findtext('name')==old:
            if name: it.find('name').text=name
            if desc: it.find('desc').text=desc
            return
    raise AssertionError('%s: no %s %s'%(key,lst,old))
def srd(src,name,key,dress,picture=None,**kw):
    m.npc_srd(src,name,key,dress=dress,picture=picture,keep_srd_text=False,**kw)
    e=m._cat('npc').find(key); old=e.find('token')
    if old is not None: e.remove(old)
    if picture: _S(e,'token','token',m.imgpath(picture)); m.TOK[key]=m.imgpath(picture)
    else: m.TOK[key]=''
    return e
def clone(src,key,name):
    e=copy.deepcopy(m._cat('npc').find(src)); e.tag=key; e.find('name').text=name; m._cat('npc').append(e); m._reg(key,e); return e
BT=sections(body(BEST))
def para(sec,label):  # one ***Label.*** paragraph or bullet from the SP-GS01 Bestiary, as plain text
    mm=re.search(r'\*\*\*%s\.\*\*\*\s*(.*)'%re.escape(label),BT[sec]); return fgconv.plain(mm.group(1))
# --- the Gluttonwretch (phase 1) with the SP-GS01 riders ---
homebrew('gluttonwretch',NOTEP('Gluttonwretch'),picture='npc-gluttonwretch',
         extra_traits=[('Bound by the Wishbone (SP-GS01)',para('The Gluttonwretch','Bound by the Wishbone')),('First Fruits (SP-GS01)',para('The Gluttonwretch','First Fruits'))])
notes('gluttonwretch','<h>The Gluttonwretch</h><p><i>Old Gobbler, the Old Faith\'s sacred turkey, starved by Hommlet and raised by a priest of Zuggtmoy. It speaks one sentence in Sylvan: "You did not feed me."</i></p>'
      '<p><b>Lair actions</b> (feast only): see Scene 07. <b>Phase 2:</b> at 0 hit points, unless 3 or more Offerings were made or the Wishbone was snapped, drop <b>The Gluttonwretch, Second Helpings</b> into the tracker at this initiative (no extra XP).</p>'
      '<p><i>Monster by GrimmGrixis (Writers Guild), Fell Harvest retune. Sidebar Press homebrew.</i></p>')
# --- phase 2 ---
GW=m._cat('npc').find('gluttonwretch')
sh=[('Overstuffed',para('The Gluttonwretch, Second Helpings','Overstuffed')),
    ('Aura of Endless Hunger','Any creature that starts its turn within 30 feet of the Gluttonwretch must succeed on a DC 19 Wisdom saving throw or use its action to eat the nearest edible substance and take 10 (3d6) necrotic damage, ignoring resistance and immunity. Immunity earned in phase 1 no longer protects anyone.'),
    ('Aura of the Corrupted Spirit','Any creature within 5 feet of the Gluttonwretch that hits it with a melee attack takes 7 (2d6) piercing damage.'),
    ('Legendary Resistance','It keeps whatever uses it had left from phase 1.'),
    ('Burst Seams',para('The Gluttonwretch, Second Helpings','Burst Seams'))]
sa=[('Multiattack','The Gluttonwretch makes one Gluttony\'s Peck attack and one Razorberry Shard attack.'),
    ('Gluttony\'s Peck','Melee Weapon Attack: +13 to hit, reach 15 ft., one target. Hit: 23 (3d10 + 7) slashing damage plus 14 (4d6) necrotic damage. If the target is a creature, it must succeed on a DC 18 Constitution saving throw or its hit point maximum is reduced by an amount equal to the necrotic damage taken.'),
    ('Razorberry Shard','Ranged Weapon Attack: +13 to hit, range 90 ft., one target. Hit: 35 (10d6) piercing damage, and a 5-foot radius around the target becomes difficult terrain.'),
    ('Gobble of Gluttony (Recharge 5-6)','Each creature within 60 feet of it must make a DC 19 Constitution saving throw. On a failed save, ghostly spirits drag the creature up to 30 feet toward the Gluttonwretch, and it is stunned until the end of its next turn. On a successful save, the creature is deafened until the end of its next turn and isn\'t moved.')]
m.npc('secondhelpings','The Gluttonwretch, Second Helpings','Huge','undead','chaotic evil',15,'(natural armor)',138,'(12d12 + 60)','20 ft., fly 30 ft. (hover)',[24,8,20,10,16,19],'20',0,
      'darkvision 120 ft., passive Perception 19','Sylvan',traits=sh,actions=sa,skills='Intimidation +10, Perception +9',saves='Con +11, Wis +9, Cha +10',immunities='necrotic, poison',picture='npc-second-helpings')
e2=m._cat('npc').find('secondhelpings')
for tag in ('damagevulnerabilities','damageresistances','conditionimmunities'): _S(e2,tag,'string',GW.findtext(tag))
addlist(e2,'legendaryactions',[(x.findtext('name'),x.findtext('desc')) for x in GW.find('legendaryactions')])
_S(e2,'token','token',m.imgpath('npc-second-helpings')); m.TOK['secondhelpings']=m.imgpath('npc-second-helpings')
notes('secondhelpings','<h>The Gluttonwretch, Second Helpings</h><p>Phase 2 of the same creature: bloated, slower and hungrier. Drop it into the combat tracker at the first record\'s initiative. <b>No extra XP</b> (same creature). Legendary actions reset to 3 at the start of phase 2; Offerings made in phase 1 still reduce them. Run it only if you are ahead of the clock.</p><p><i>Sidebar Press homebrew.</i></p>')
# --- the Offering-Heap ---
homebrew('offeringheap',NOTEP('Offering-Heap'),picture='npc-offering-heap').find('name').text='The Offering-Heap'
notes('offeringheap','<h>The Offering-Heap</h><p><i>Forty years of rotted offerings behind Jaroo\'s grove, pulled upright by grief and the Temple\'s rot. It is not evil. It is a sad, enormous dog that has been hit.</i></p><p>Never attacks first; meant to be calmed or fed (Scene 04). Fire stops its Composting.</p><p><i>Sidebar Press homebrew.</i></p>')
# --- SRD reskins ---
srd('mummy','Gorger (Hollow Guest)','gorger',"A villager or traveler the Wretch has gorged. Speaks only in apologies: use the barks in the Comedy Kit. Dreadful Glare feeds the Wretch's Feast on Fear.",
    picture='npc-hollow-guests',overrides={'alignment':'neutral evil'})
retext('gorger',[('Rotting Fist','Gorging Fist'),('rotting fist','gorging fist'),('mummy rot','gorging rot'),('Mummy Rot','Gorging Rot'),('The mummy','The Gorger'),('the mummy','the Gorger'),('mummy','Gorger')])
clone('gorger','hobtanner','Hob Tanner (Gorger)')
srd('wight','Flinger (Hollow Guest)','flinger','A gorged villager who throws bones and razorberry shards. At its best at dusk and night. A humanoid it kills rises as a villager zombie 24 hours later, or at the end of the feast round.',
    picture='npc-hollow-guests')
retext('flinger',[('longbow','flung bone'),('Longbow','Flung Bone'),('The wight','The Flinger'),('the wight','the Flinger')])
srd('mage','Deacon Mungo Brindlewick','brindlewick',"The round, cheerful priest of Zuggtmoy who raised Old Gobbler. Holds the Wishbone if he has it, casts from the crowd, and uses misty step or greater invisibility to keep the bone away from anyone trying to pull it. Rot-swapped spells: stinking cloud, blight and cloudkill replace fireball, ice storm and cone of cold.",
    picture='npc-brindlewick',overrides={'alignment':'neutral evil','type':'humanoid (human)','languages':'Common, Sylvan'})
retext('brindlewick',[('The mage','Brindlewick'),('the mage','Brindlewick'),('fireball','stinking cloud'),('ice storm','blight'),('cone of cold','cloudkill')])
addlist(m._cat('npc').find('brindlewick'),'bonusactions',[('Grace Before Meat','Brindlewick says grace. Until the start of his next turn, the Gluttonwretch has advantage on its next attack roll.')])
srd('gladiator','Brother of the Rotting Table','brother','A gourmand in a stained bib. Whenever a Brother fails a saving throw, he bursts into the wrong verse of the Brewfest hymn; another Brother corrects him.',
    overrides={'alignment':'neutral evil','type':'humanoid (human)'})
retext('brother',[('The gladiator','The Brother'),('the gladiator','the Brother')])
act('brother','actions','Spear','Cleaver','Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage, or 13 (2d8 + 4) slashing damage if used with two hands.')
addlist(m._cat('npc').find('brother'),'traits',[('Wrong Verse','Whenever the Brother fails a saving throw, he bursts into the wrong verse of the Brewfest hymn. Purely comic.')])
srd('earthelemental','Earth Elemental (Smokehouse Foundation)','earthelemental','The Smokehouse\'s old foundation stones, bound by the Temple before 569. They step out of the cellar walls when the site goes to Alert.')
srd('assassin','Gremag','gremag','The younger trader, a 7th-level assassin under the counter. Uses the Traders\' Establishment (T1 Map 4).',overrides={'alignment':'chaotic evil','ac':16,'actext':'(chain shirt +1)','senses':'passive Perception 11','languages':"Common, Thieves' Cant"})
g=m._cat('npc').find('gremag'); g.find('abilities/wisdom/score').text='7'; g.find('abilities/wisdom/bonus').text='-2'
retext('gremag',[('The assassin','Gremag'),('the assassin','Gremag'),('two shortsword attacks','two Dagger of Venom attacks')])
act('gremag','actions','Shortsword','Dagger of Venom','Melee or Ranged Weapon Attack: +8 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 7 (1d4 + 5) piercing damage, and the target must make a DC 15 Constitution saving throw, taking 24 (7d6) poison damage on a failed save, or half as much damage on a successful one.')
addlist(g,'actions',[('Venom (3 doses)','Gremag coats the dagger. The next creature it hits also makes a DC 15 Constitution saving throw or takes 11 (2d10) more poison damage and is poisoned for 1 minute.'),
                     ('Dust of Disappearance (3 pinches)','Gremag throws a pinch into the air: he and every creature and object within 10 feet become invisible for 2d4 minutes.')])
m.npc('rannos','Rannos Davl','Medium','humanoid (human)','chaotic evil',18,'(studded leather +1, ring of protection)',58,'(9d8 + 18)','30 ft.',[8,18,15,14,9,7],'4',1100,
      'passive Perception 12',"Common, Thieves' Cant",skills='Deception +4, Insight +2, Perception +2, Sleight of Hand +8, Stealth +8',saves='Dex +7, Int +5 (+1 to all from the ring)',
      traits=[('Undetectable','He wears an amulet of proof against detection and location: divination magic can\'t target him or see him through scrying sensors.'),
              ('Cunning Action','On each of his turns he can Dash, Disengage or Hide as a bonus action.'),
              ('Evasion','When an effect allows a Dexterity saving throw for half damage, he takes no damage on a success and half on a failure.'),
              ('Sneak Attack (1/Turn)','He deals an extra 14 (4d6) damage when he hits with advantage, or when an ally is within 5 feet of the target and he doesn\'t have disadvantage.')],
      actions=[('Multiattack','Rannos makes two melee attacks.'),('Dagger +1','Melee or Ranged Weapon Attack: +7 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 7 (1d4 + 5) piercing damage.'),
               ('Shortsword +1 (under the counter)','Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 8 (1d6 + 5) piercing damage.')],
      text='The older trader: slow, fat, clumsy and placid to all appearances. The Dexterity is real. From the Sidebar Press T1 conversion.')
# --- Brindlewick's rot spells from the SRD Data module ---
_srdx=ET.fromstring(zipfile.ZipFile(os.path.join(FG,'modules','DD5E SRD Data.mod')).read('client.xml'))
_srdsp={(e.findtext('name') or '').lower():e for e in next(x for x in _srdx.iter() if x.tag=='spelldata').iter() if e.find('name') is not None and e.find('level') is not None}
def spelldesc(nm):
    e=_srdsp[nm.lower()]; d=re.sub(r'\s*\n\s*','\n',re.sub(r'<[^>]+>','\n',ET.tostring(e.find('description'),encoding='unicode'))).strip()
    return 'Level: %s\nCasting Time: %s\nComponents: %s\nDuration: %s\nRange: %s\n%s\n'%(e.findtext('level'),e.findtext('castingtime'),e.findtext('components'),e.findtext('duration'),e.findtext('range'),html.unescape(d))
for it in m._cat('npc').find('brindlewick').find('spells'):
    nm=it.findtext('name')
    for old,new in (('Fireball','Stinking Cloud'),('Ice Storm','Blight'),('Cone Of Cold','Cloudkill'),('Cone of Cold','Cloudkill')):
        if nm.startswith(old+' - '): it.find('name').text=new+nm[len(old):]; it.find('desc').text=spelldesc(new)
# ---- round tokens (combat tracker / map) ----
for k,t in (('gluttonwretch','token-gluttonwretch'),('secondhelpings','token-second-helpings'),('offeringheap','token-offering-heap'),('gorger','token-gorger'),
            ('hobtanner','token-gorger'),('flinger','token-flinger'),('brindlewick','token-brindlewick'),
            ('brother','token-brother'),('earthelemental','token-earth-elemental'),('rannos','token-rannos'),('gremag','token-gremag')):
    e=m._cat('npc').find(k); old=e.find('token')
    if old is not None: e.remove(old)
    _S(e,'token','token',m.imgpath(t)); m.TOK[k]=m.imgpath(t)
for k,pic in (('brother','npc-brother'),('earthelemental','npc-earth-elemental'),('rannos','npc-rannos'),('gremag','npc-gremag')):
    e=m._cat('npc').find(k); old=e.find('picture')
    if old is not None: e.remove(old)
    _S(e,'picture','token',m.imgpath(pic))
# ---- encounters (7 PCs at level 12) ----
m.battle('E1','04 The Offering-Heap',[('offeringheap',1)],'map-m3-jaroos-grove')
m.battle('E2','05 The Smokehouse (Alert)',[('brindlewick',1),('brother',2),('earthelemental',2)],'map-m2b-smokehouse-cellar')
m.battle('E3','06 The Hunt (one round, then the chase)',[('gluttonwretch',1),('gorger',1),('flinger',1)],'map-m4-emridy-meadows')
m.battle('E4a','07 The Feast - best case',[('gluttonwretch',1),('hobtanner',1)],'map-m1-feast-green')
m.battle('E4b','07 The Feast - Brindlewick still loose',[('gluttonwretch',1),('hobtanner',1),('brindlewick',1)],'map-m1-feast-green')
m.battle('E4c',"07 The Feast - the barrels' Flinger",[('gluttonwretch',1),('hobtanner',1),('flinger',1)],'map-m1-feast-green')
m.battle('E4d','07 The Feast - worst case',[('gluttonwretch',1),('hobtanner',1),('flinger',1),('brindlewick',1)],'map-m1-feast-green')
m.battle('X4','07 Second Helpings (phase 2; no extra XP)',[('secondhelpings',1)],'map-m1-feast-green')
m._cat('battle').find(m.BAT['X4'].split('.')[1]).find('exp').text='0'
m.battle('M4','07 Uncured Gorgers (Ma Dunwold and Tam Thistlewood)',[('gorger',2)],'map-m1-feast-green')
m.battle('T2','02 The Traders (if it comes to blades)',[('rannos',1),('gremag',1)],'map-t1-traders-establishment')
# ---- token positions on each encounter's map (pixels from the map's top-left; FGU stores them from the centre, y UP) ----
from PIL import Image as _Im
def _size(k): return _Im.open(os.path.join(m.img,m.IMG[k][1])).size
def place(code,pos):
    b=m._cat('battle').find(m.BAT[code].split('.')[1]); mk=b.find('maplink').findtext('recordname'); key=[k for k,v in m.IMG.items() if 'image.'+v[0]==mk][0]
    W,H=_size(key); used={}
    for it in b.find('npclist'):
        n=it.find('link').findtext('recordname').split('.')[1]; pts=pos[n][used.get(n,0):used.get(n,0)+int(it.findtext('count'))]; used[n]=used.get(n,0)+len(pts)
        assert len(pts)==int(it.findtext('count')),'%s: need %s positions for %s'%(code,it.findtext('count'),n)
        ml=_S(it,'maplink')
        for j,(x,y) in enumerate(pts,1):
            e=_S(ml,ids(j)); r=_S(e,'imageref','windowreference'); _S(r,'class',None,'imagewindow'); _S(r,'recordname',None,mk+'.image')
            _S(e,'imagex','number',int(x-W/2)); _S(e,'imagey','number',int(H/2-y))
FEAST={'gluttonwretch':[(1450,350)],'hobtanner':[(550,1150)],'flinger':[(2650,1150)],'brindlewick':[(1350,1850)]}
place('E1',{'offeringheap':[(1650,450)]})
place('E2',{'brindlewick':[(1250,450)],'brother':[(1150,650),(1350,650)],'earthelemental':[(700,800),(1800,700)]})
place('E3',{'gluttonwretch':[(1750,1050)],'gorger':[(1050,1550)],'flinger':[(2550,1250)]})
for c in ('E4a','E4b','E4c','E4d'): place(c,FEAST)
place('X4',{'secondhelpings':[(1450,650)]})
place('M4',{'gorger':[(650,750),(2250,750)]})
place('T2',{'rannos':[(710,2090)],'gremag':[(1118,1920)]})
# ---- items ----
def itemtext(p):
    t=fullnote(p); t=re.split(r'\n## (?:Found In|Continuity)',t)[0]
    return C(t)
for key,name in (('feather','Feather of the First Fruits'),('wishbone','The Wishbone of Old Gobbler'),('cipherbook',"Brindlewick's Cipher Book")):
    p=NOTEP(name); rar=(re.search(r'^rarity: *"?([^"\n]*)',open(p).read(),re.M) or [None,''])[1].title()
    m.item(key,name,'Wondrous Item','<h>%s</h>'%html.escape(name)+itemtext(p),rarity=rar)
