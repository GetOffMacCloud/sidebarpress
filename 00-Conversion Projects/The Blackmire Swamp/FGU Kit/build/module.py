"""SP-CV01 The Blackmire Swamp — Fantasy Grounds Unity (5E) module build.
Source: The Blackmire Swamp Adventure Book.docx (EndYourStreamTV). Developed for FG by GetOffMacCloud.
Run:  python3 module.py [--install]"""
import os,sys,re,html,shutil,zipfile,io,glob
HERE=os.path.dirname(os.path.abspath(__file__))
# ---------- edition settings
CODE='SP-CV01'; NAME='SP-CV01 The Blackmire Swamp'; DISPLAY='The Blackmire Swamp'
SRC=os.path.normpath(os.path.join(HERE,'..','..')); DOCX=os.path.join(SRC,'The Blackmire Swamp Adventure Book.docx')
TOOLS=[os.environ.get('FGMOD_TOOLS',''),os.path.join(SRC,'..','..','70-Company','Tools','fgu-module-builder'),os.path.expanduser('~/mnt/fgu-module-builder')]
FGDIRS=[os.environ.get('FG_DIR',''),os.path.expanduser('~/SmiteWorks/Fantasy Grounds'),os.path.expanduser('~/mnt/Fantasy Grounds')]
sys.path.insert(0,next(p for p in TOOLS if p and os.path.exists(os.path.join(p,'fgmod.py'))))
FG=next(p for p in FGDIRS if p and os.path.exists(os.path.join(p,'modules')))
from fgmod import Mod
from docxfg import book,find_table,plain
# source file -> module image name (labeled location art doubles as GM encounter maps)
IMAGES={'blackmire adventure map.png':'map-blackmire-region','grimwater_docks_labeled.png':'map-grimwater-docks',
 'the_drift_labeled.png':'map-the-drift','mossfall_outpost_labeled.png':'map-mossfall-outpost',
 'fort_drowned_spear_labeled.png':'map-fort-drowned-spear','the_rooted_archive_labeled.png':'map-the-rooted-archive',
 'the_rootmaw_labyrinth_labeled.png':'map-the-rootmaw-labyrinth','crocodile_throne_pool_labeled.png':'map-crocodile-throne-pool',
 'the_sunken_war_church_labeled.png':'map-the-sunken-war-church','the_sunken_druid_grove_labeled.png':'map-the-sunken-druid-grove',
 'NPCs.png':'npc-key-npcs','Old_Marrow_Finch.png':'npc-old-marrow-finch','Sister_Vell.png':'npc-sister-vell',
 'Captain_Rusk_Ironstake.png':'npc-captain-rusk-ironstake','Silt.png':'npc-silt','Aster_Vale.png':'npc-aster-vale',
 'Living_wood_focus.png':'item-living-wood-focus','sigiled_crocodile_tooth.png':'item-sigiled-crocodile-tooth',
 'vial_of_blackmire_essence.png':'item-vial-of-blackmire-essence','Tide_Thread_Rope.png':'item-tide-thread-rope',
 'Mudrunner_Reedcloak.png':'item-mudrunner-reedcloak','Throne_Scale_Shield.png':'item-throne-scale-shield',
 'Ironstake_Hunters_Net.png':'item-ironstake-hunters-net','Resom_Sealed_Field_Journal.png':'item-resin-sealed-field-journal'}
DOCX_MEDIA={'word/media/image2.png':'map-region-schematic','word/media/image3.png':'map-grove-schematic'}
EXCLUDE_NOTE='blackmire_v1/v2/v3.png are earlier drafts of the regional map and are left out.'
SPLIT_H3={'Fort Drowned Spear','The Rooted Archive','Blackmire Magic Items'}

def stage_images():
    d=os.path.join(HERE,'source-images'); os.makedirs(d,exist_ok=True)
    for f,n in IMAGES.items():
        o=os.path.join(d,n+'.png')
        if not os.path.exists(o): shutil.copyfile(os.path.join(SRC,f),o)
    import frame_canva
    o=os.path.join(d,'cover-blackmire.jpg')
    if not os.path.exists(o): shutil.copyfile(os.path.join(frame_canva.ASSETS,'cover','SP-CV01 — Cover.jpg'),o)
    z=zipfile.ZipFile(DOCX)
    for f,n in DOCX_MEDIA.items():
        o=os.path.join(d,n+'.png')
        if not os.path.exists(o): open(o,'wb').write(z.read(f))
    return d

m=Mod(NAME,DISPLAY,'Sidebar Press','Sidebar Press',FG,HERE)
IMG_NAMES={'cover-blackmire':'Cover — The Blackmire Swamp','npc-key-npcs':'NPC — Key NPCs of Blackmire',
 'item-ironstake-hunters-net':'Item — Ironstake Hunter’s Net','item-vial-of-blackmire-essence':'Item — Vial of Blackmire Essence',
 'item-living-wood-focus':'Item — Living-Wood Focus','item-resin-sealed-field-journal':'Item — Resin-Sealed Field Journal',
 'item-throne-scale-shield':'Item — Throne-Scale Shield','item-tide-thread-rope':'Item — Tide-Thread Rope',
 'map-the-rootmaw-labyrinth':'Map — The Rootmaw Labyrinth','map-grove-schematic':'Map — Sunken Druid Grove Schematic',
 'map-region-schematic':'Map — Blackmire Regions Schematic','map-blackmire-region':'Map — Blackmire Swamp'}
m.pretty=lambda n:IMG_NAMES.get(n,Mod.pretty(n))
m.images(stage_images(),keep_original={"map-region-schematic","map-grove-schematic"})
front,CH,STAT=book(DOCX,split_h3=SPLIT_H3,skip_h2={'Contents'})

# ---------- homebrew creatures (parsed from Appendix A)
SECT={'TRAITS':'traits','ACTIONS':'actions','BONUS ACTIONS':'bonus','REACTIONS':'reactions','LEGENDARY ACTIONS':'legendary','LAIR ACTIONS':'lair'}
FIX={'thornheart':{'Damage Resistances':'lightning','Damage Immunities':'poison','Condition Immunities':'charmed and frightened while in swamp terrain, poisoned'}}
def creature(key,title,picture=None):
    S=STAT[title]; f={}; secs={v:[] for v in SECT.values()}; cur=None
    head=S['lines'][0]; size,rest=head.split(' ',1); typ,align=rest.rsplit(', ',1)
    for l in S['lines'][1:]:
        if l in SECT: cur=SECT[l]; continue
        n,_,d=l.partition('. ')
        if cur is None: f[n]=d.strip()
        else:
            n=n.replace('–','-')
            if n=='Legendary Action Use': n='Options'
            secs[cur].append((n,d.strip()))
    f.update(FIX.get(key,{}))
    ac=re.match(r'(\d+)\s*(.*)',f['Armor Class']); hp=re.match(r'(\d+)\s*(.*)',f['Hit Points'])
    cr=re.match(r'([\d/]+)\s*\(([\d,]+) XP\)',f['Challenge'])
    dash=lambda k:'' if f.get(k,'—') in ('—','-') else f[k]
    m.npc(key,title,size,typ,align,int(ac.group(1)),ac.group(2),int(hp.group(1)),hp.group(2),f['Speed'],S['abil'],
          cr.group(1),int(cr.group(2).replace(',','')),f['Senses'],dash('Languages'),traits=secs['traits'],actions=secs['actions'],
          bonus=secs['bonus'],reactions=secs['reactions'],skills=dash('Skills'),saves=dash('Saving Throws'),immunities=dash('Damage Immunities'),picture=picture)
    e=m._cat('npc').find(key)
    for tag,k in (('damageresistances','Damage Resistances'),('damagevulnerabilities','Damage Vulnerabilities'),('conditionimmunities','Condition Immunities')):
        if dash(k): ET.SubElement(e,tag,{'type':'string'}).text=f[k]
    for tag,items in (('legendaryactions',secs['legendary']),('lairactions',secs['lair'])):
        if items:
            L=ET.SubElement(e,tag)
            for i,(n,d) in enumerate(items,1):
                it=ET.SubElement(L,'id-%05d'%i); ET.SubElement(it,'desc',{'type':'string'}).text=d; ET.SubElement(it,'name',{'type':'string'}).text=n
    e.remove(e.find('text'))
    t=ET.fromstring('<text type="formattedtext"><p><b>Tactics.</b> %s</p><p><i>From The Blackmire Swamp by EndYourStreamTV (Appendix A).</i></p></text>'%html.escape(S['tactics']))
    e.append(t)
import xml.etree.ElementTree as ET
CREATURES=[('juvenilecrocodile','Juvenile Crocodile'),('huntingcrocodile','Hunting Crocodile'),('alphacrocodile','Alpha Crocodile'),
 ('swamptyrant','Swamp Tyrant Crocodile'),('thornheart','The Thorn-Heart Archdruid Crocodile'),('drownedsentry','Drowned Sentry'),
 ('rootboundsentinel','Rootbound Sentinel'),('mireechospirit','Mire-Echo Spirit')]
TOKDIR=os.path.join(SRC,'FGU Kit','tokens'); TOKFILES=[]
def set_token(key):
    from PIL import Image
    import frame_canva; src=frame_canva.path(key); dst=os.path.join(HERE,'images','token-'+key+'.webp')
    Image.open(src).save(dst,'WEBP',quality=86,method=4); TOKFILES.append(dst)
    e=m._cat('npc').find(key); ref='tokens/%s@%s'%(os.path.basename(dst),NAME)
    for t in ('token','token3Dflat'):
        if e.find(t) is not None: e.remove(e.find(t))
    ET.SubElement(e,'token',{'type':'token'}).text=ref; m.TOK[key]=ref
def strip_srd_art(key):
    e=m._cat('npc').find(key)
    for t in ('token','token3Dflat'):
        if e.find(t) is not None: e.remove(e.find(t))
    p=e.find('picture')
    if p is not None and '@SP-CV' not in (p.text or ''): e.remove(p)
    m.TOK[key]=''
for k,t in CREATURES: creature(k,t); set_token(k)

# ---------- story NPCs: SRD stand-in statblocks, dressed from the Quest Givers table
def qg_rows():
    from docxfg import blocks
    for b in blocks(DOCX):
        if b[0]=='tbl' and b[2] and [plain(' '.join(c)) for c in b[2][0]]==['NPC','Portrayal','Open Desire','Secret or Complication']:
            return {plain(' '.join(r[0])):[plain(' '.join(c)) for c in r] for r in b[2][1:]}
QG=qg_rows()
STORY=[('oldmarrowfinch','Old Marrow Finch','scout','Swamp guide, Grimwater Docks','npc-old-marrow-finch'),
 ('sistervell','Sister Vell','druid','Druid emissary, Circle of the Submerged Root','npc-sister-vell'),
 ('captainrusk','Captain Rusk Ironstake','veteran','Iron Stakes commander','npc-captain-rusk-ironstake'),
 ('silt','Silt','spy','Mudrunner and informant','npc-silt'),
 ('astervale','Aster Vale','mage','Veiled Syndicate scholar posing as an apothecary','npc-aster-vale')]
for key,name,srd,role,pic in STORY:
    r=QG[name]
    m.npc_srd(srd,name,key,picture=pic)
    e=m._cat('npc').find(key); e.remove(e.find('text'))
    e.append(ET.fromstring('<text type="formattedtext"><h>%s</h><p><i>%s</i></p><p><b>Portrayal.</b> %s</p><p><b>Open Desire.</b> %s</p><p><b>Secret or Complication.</b> %s</p><p><i>Statblock: suggested 5E SRD 5.1 %s (CC-BY-4.0); the book gives none for this character.</i></p></text>'%tuple(html.escape(x) for x in (name,role,r[1],r[2],r[3],srd.title()))))
    strip_srd_art(key); set_token(key)
# SRD creatures named in the travel tables
for srd,name,key,dress in (('giantrat','Giant Rat','giantrat','Reedmarch pack thieves; test unattended packs and retreat into reeds.'),
 ('stirge','Stirge','stirge','Hang beneath dead trees over dry crossings; attack after vibration or loud noise.'),
 ('swarmofpoisonoussnakes','Swamp Snake Nest','swampsnakes','A nest of swamp snakes uncovered by a shifting wall in the Broken Fen.'),
 ('bandit','Route-Tax Bandit','bandit','Bandits wearing stolen Iron Stakes badges; their boat carries Veiled glassware.'),
 ('guard','Iron Stakes Militia','ironstakesmilitia','Iron Stakes militia; Captain Rusk can send two at Iron Stakes +2.'),
 ('druid','Circle Druid','circledruid','Members of the Circle of the Submerged Root, e.g. Veiled prisoners in the Black Core.')):
    m.npc_srd(srd,name,key,dress=dress); strip_srd_art(key)

# ---------- encounters (baseline four characters; bands per the book's scaling notes)
J,H,A='juvenilecrocodile','huntingcrocodile','alphacrocodile'
ENC=[('E1a','Wreck of the Reedwake (4 PCs)',[(J,3)],None),('E1b','Wreck of the Reedwake (5 PCs)',[(J,4)],None),
 ('E1c','Wreck of the Reedwake (6 PCs)',[(J,5)],None),
 ('E2','Drowned Barracks',[('drownedsentry',2)],'map-fort-drowned-spear'),
 ('E3a','Flooded Courtyard (4 PCs)',[(H,2)],'map-fort-drowned-spear'),('E3b','Flooded Courtyard (5 PCs)',[(H,2),(J,1)],'map-fort-drowned-spear'),
 ('E3c','Flooded Courtyard (6 PCs)',[(H,3)],'map-fort-drowned-spear'),('E3d','Flooded Courtyard (gentler)',[(H,1),(J,2)],'map-fort-drowned-spear'),
 ('E4','The Root Vault Alpha',[(A,1)],'map-the-rooted-archive'),
 ('E5','The Swamp Tyrant',[('swamptyrant',1)],'map-crocodile-throne-pool'),
 ('E6a','The Kneeling Dead',[('drownedsentry',4)],'map-the-sunken-war-church'),('E6b','The Kneeling Dead (rite performed)',[('drownedsentry',2)],'map-the-sunken-war-church'),
 ('E7','The Thorn-Heart (Sunken Druid Grove)',[('thornheart',1)],'map-grove-schematic'),
 ('R1','Reedmarch: Giant Rats',[('giantrat',4)],None),('R2','Reedmarch: Stirges',[('stirge',2)],None),('R3','Reedmarch: Following Juvenile',[(J,1)],None),
 ('R4','Broken Fen: Hunting Pack',[(H,3)],None),('R5','Broken Fen: Swamp Snakes',[('swampsnakes',1)],None),('R6','Broken Fen: Route-Tax Bandits',[('bandit',4)],None),
 ('R7','Broken Fen: Bell-Line Sentry',[('drownedsentry',1)],None),('R8','Deepwater Reach: Alpha Beneath the Barge',[(A,1)],None),
 ('R9','Black Core: Rootbound Sentinel',[('rootboundsentinel',1)],None),('R10','Black Core: Mire-Echo Spirit',[('mireechospirit',1)],None)]
for c,n,cr,mp in ENC: m.battle(c,n,cr,mp)

# ---------- items (descriptions from Appendix C)
PG={n:x for k,t,tg,pg in CH for n,x in pg}
def itemdesc(n):
    x=PG[n]; first=re.match(r'<p>(.*?)</p>',x); return first.group(1),x[first.end():]
ITEMS=[('livingwoodfocus','Living-Wood Focus','Wondrous Item',{}),('sigiledtooth','Sigiled Crocodile Tooth','Wondrous Item',{}),
 ('blackmireessence','Vial of Blackmire Essence','Potion',{}),('tidethreadrope','Tide-Thread Rope','Wondrous Item',{}),
 ('mudrunnerreedcloak','Mudrunner Reedcloak','Wondrous Item',{}),('thronescaleshield','Throne-Scale Shield','Armor',{'subtype':'Shield','ac':2}),
 ('ironstakenet','Ironstake Hunter’s Net','Weapon',{'subtype':'Martial Ranged Weapons'}),('resinjournal','Resin-Sealed Field Journal','Wondrous Item',{})]
PIC={'Ironstake Hunter’s Net':'item-ironstake-hunters-net'}
for key,name,typ,extra in ITEMS:
    line,body=itemdesc(name); rar=re.search(r'\b(common|uncommon|rare|very rare|legendary)\b',line).group(1).title()
    att='requires attunement' in line
    pic=PIC.get(name,'item-'+re.sub(r'[^a-z]+','-',name.lower()).strip('-'))
    sub=extra.pop('subtype','')
    m.item(key,name,typ,'<p><i>%s</i></p>%s<p><i>From The Blackmire Swamp by EndYourStreamTV.</i></p>'%(line,body),subtype=sub,rarity=rar,picture=pic,**extra)
    if att: m._cat('item').find(key).append(ET.fromstring('<attunement type="number">1</attunement>'))
for b in __import__('docxfg').blocks(DOCX):
    if b[0]=='tbl' and b[2] and plain(' '.join(b[2][0][0]))=='Shard':
        for r in b[2][1:]:
            n,eff,sign=[' '.join(c) for c in r]; key=re.sub(r'[^a-z]','',plain(n).lower())
            m.item(key,plain(n),'Wondrous Item','<p><i>Anchor shard, single use. Created by extracting an anchor in Chapter 4.</i></p><p><b>One-Time Effect.</b> %s</p><p><b>Lingering Sign.</b> %s</p><p>Unless an ending states otherwise, the shard can be used once and then becomes inert.</p>'%(eff,sign),rarity='Rare')

# ---------- reference manual
N,B,I,IT=m.N,m.B,m.I,m.IT
PAGE_IMG={'The Four Regions':['map-blackmire-region','map-region-schematic'],'Grimwater Docks':['map-grimwater-docks'],
 'The Drift':['map-the-drift'],'Mossfall Outpost':['map-mossfall-outpost'],'Quest Givers and Recurring NPCs':['npc-key-npcs'],
 'Opening: Fog Over Grimwater':['map-grimwater-docks'],'Fort Drowned Spear':['map-fort-drowned-spear'],
 'Arrival at the Drift':['map-the-drift'],'The Rooted Archive':['map-the-rooted-archive'],
 'Site A: The Rootmaw Labyrinth':['map-the-rootmaw-labyrinth'],'Site B: The Crocodile Throne Pool':['map-crocodile-throne-pool'],
 'Site C: The Sunken War Church':['map-the-sunken-war-church'],'Encounter Summary':['map-the-sunken-druid-grove','map-grove-schematic'],
 'Handout: Player Primer':['map-blackmire-region']}
for key,name,typ,_ in ITEMS: PAGE_IMG[name]=[PIC.get(name,'item-'+re.sub(r'[^a-z]+','-',name.lower()).strip('-'))]
STORYN=[k for k,*_ in STORY]
PAGE_LINKS={
 'Quest Givers and Recurring NPCs':[N(k) for k in STORYN],'Factions of Blackmire':[N('captainrusk'),N('sistervell'),N('silt'),N('astervale'),N('ironstakesmilitia'),N('circledruid')],
 'Faction Boons':[N('captainrusk'),N('sistervell'),N('silt'),N('astervale'),IT('mudrunnerreedcloak'),N('ironstakesmilitia')],
 'Crocodile Escalation Guide':[N(k) for k,_ in CREATURES[:5]],
 'Opening: Fog Over Grimwater':[N('captainrusk'),N('oldmarrowfinch'),N('sistervell'),N('silt'),I('map-grimwater-docks')],
 'The Missing Reedwake':[N('captainrusk'),N('oldmarrowfinch'),N('sistervell'),N('silt')],
 'Travel Segment: The Old Safe Route':[N('giantrat'),N(J)],
 'Encounter: Wreck of the Reedwake':[B('E1a'),B('E1b'),B('E1c'),N(J)],'Clues at the Wreck':[IT('sigiledtooth')],
 'Choosing an Expedition Sponsor':[N('captainrusk'),N('sistervell'),N('silt'),N('astervale')],
 'Travel Through the Broken Fen':[N(H)],'Fort Drowned Spear':[I('map-fort-drowned-spear'),B('E2'),B('E3a')],
 '2. Drowned Barracks':[B('E2'),N('drownedsentry'),I('map-fort-drowned-spear')],
 '4. Flooded Courtyard':[B('E3a'),B('E3b'),B('E3c'),B('E3d'),N(H),N(J),I('map-fort-drowned-spear')],
 '5. Anchor Vault':[N('astervale'),N('sistervell')],
 'Arrival at the Drift':[N('captainrusk'),N('sistervell'),N('silt'),N('astervale'),I('map-the-drift')],
 'Journey to the Archive':[N(A)],'The Rooted Archive':[I('map-the-rooted-archive'),B('E4')],
 '6. The Root Vault':[B('E4'),N(A),IT('sigiledtooth'),I('map-the-rooted-archive')],
 'Site A: The Rootmaw Labyrinth':[N('rootboundsentinel'),IT('rootshard'),I('map-the-rootmaw-labyrinth')],
 'Site B: The Crocodile Throne Pool':[B('E5'),N('swamptyrant'),IT('tideshard'),IT('sigiledtooth'),I('map-crocodile-throne-pool')],
 'Site C: The Sunken War Church':[B('E6a'),B('E6b'),N('drownedsentry'),IT('memoryshard'),I('map-the-sunken-war-church')],
 'Resolving an Anchor':[IT('rootshard'),IT('tideshard'),IT('memoryshard')],
 'Encounter Summary':[B('E7'),N('thornheart'),I('map-grove-schematic'),I('map-the-sunken-druid-grove')],
 'Approaching the Grove':[B('E7'),N('thornheart')],'Phase Tracker':[N('thornheart')],'Lair Actions in the Grove':[N('thornheart')],
 'Adjusting Difficulty':[B('E7'),N('thornheart')],
 'The Dropped Bag':[IT('livingwoodfocus'),IT('sigiledtooth'),IT('blackmireessence')],
 'Rewards and Recognition':[IT('thronescaleshield'),N('captainrusk'),N('sistervell')],
 'Reedmarch Encounters (d8)':[B('R1'),B('R2'),B('R3'),N('ironstakesmilitia')],
 'Broken Fen Encounters (d8)':[B('R4'),B('R5'),B('R6'),B('R7')],'Deepwater Reach Encounters (d8)':[B('R8')],
 'Black Core Encounters (d8)':[B('R9'),B('R10'),N('circledruid'),N('swamptyrant')],
 'Anchor Shards':[IT('rootshard'),IT('tideshard'),IT('memoryshard')],
 'Faction Rewards':[IT(k) for k,*_ in ITEMS]+[IT('rootshard'),IT('tideshard'),IT('memoryshard')],
 'Handout: Player Primer':[I('map-blackmire-region')]}
for k,t in CREATURES: PAGE_LINKS[t]=[N(k)]
for key,name,*_ in ITEMS: PAGE_LINKS[name]=[IT(key)]

CREDITS=('<h>The Blackmire Swamp: The Curse of the Druids</h><p><i>A fifth-edition fantasy adventure for characters of levels 1 through 5.</i></p>'
 '<p><b>Written by</b> EndYourStreamTV (original concept and adventure design)</p>'
 '<p><b>Developed for Fantasy Grounds by</b> GetOffMacCloud</p><p><b>Published by</b> Sidebar Press</p>'
 '<p><b>In this module.</b> The complete adventure book as a reference manual, %d NPC records (8 Blackmire creatures with full statblocks, 5 story NPCs with suggested SRD statblocks, 6 SRD creatures from the travel tables), %d encounters (E = adventure, R = random-table), %d items, and location art and maps.</p>'
 '<p><b>Encounter codes.</b> Encounters assume four characters; lettered variants follow the book\'s scaling notes for five or six characters. The Thorn-Heart\'s hit-point adjustments for other party sizes are on the Adjusting Difficulty page.</p>'
 '<p><b>Art.</b> Cover and token art created with Canva for Sidebar Press; location, NPC and item art from the original book.</p>'
 '<p><i>Portions of this module use material from the System Reference Document 5.1 ("SRD 5.1") by Wizards of the Coast LLC, available at https://dnd.wizards.com/resources/systems-reference-document. The SRD 5.1 is licensed under the Creative Commons Attribution 4.0 International License (CC-BY-4.0).</i></p>')
def cleanup(x): return x.replace('<b><b>','<b>').replace('</b></b>','</b>')
def section(kick,title):
    mm=re.match(r'CHAPTER (\d+)',kick); ma=re.match(r'APPENDIX ([A-Z])',kick)
    return 'Chapter %s: %s'%(mm.group(1),title) if mm else 'Appendix %s: %s'%(ma.group(1),title) if ma else title
m.page('Credits','Credits',CREDITS%(len(m.NPC)+0,len(m.BAT),len(m.ITEM)),images=['cover-blackmire'])
PREFIX={'Fort Drowned Spear':'Fort Drowned Spear','The Rooted Archive':'Rooted Archive'}
for kick,title,tag,pages in CH:
    sec=section(kick,title); parent=None
    for i,(n,x) in enumerate(pages):
        x=cleanup(x)
        if i==0 and tag: x='<p><i>%s</i></p>'%html.escape(tag)+x
        if n in PREFIX: parent=PREFIX[n]
        elif not re.match(r'\d+\. ',n): parent=None
        disp='%s: %s'%(parent,n) if parent and re.match(r'\d+\. ',n) else n
        m.page(sec,disp,x,images=PAGE_IMG.get(n,[]),links=PAGE_LINKS.get(n,[]))
missing=[k for k in list(PAGE_IMG)+list(PAGE_LINKS) if k not in PG]
assert not missing,'unmatched page names: %s'%missing
out=os.path.join(SRC,'FGU Kit',NAME+'.mod')
m.build(out,cover_image='cover-blackmire')
with zipfile.ZipFile(out,'a',zipfile.ZIP_DEFLATED) as z:
    for f in TOKFILES: z.write(f,'tokens/'+os.path.basename(f))
print('added %d tokens'%len(TOKFILES))
if '--install' in sys.argv:
    shutil.copyfile(out,os.path.join(FG,'modules',NAME+'.mod')); print('installed to',os.path.join(FG,'modules'))
