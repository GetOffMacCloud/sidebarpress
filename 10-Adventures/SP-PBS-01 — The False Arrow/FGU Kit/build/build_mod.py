import os,re,glob,json,zipfile,html,copy,sys
import xml.etree.ElementTree as ET
sys.path.insert(0,os.path.expanduser('~/work'))
from fgconv import conv, body, sections
MOD='SP-PBS-01 The False Arrow'; CAT=MOD
V=os.path.expanduser('~/mnt/Sidebar Press Vault/10-Adventures/SP-PBS-01 — The False Arrow/')
W=os.path.expanduser('~/work/mod/'); IMG=W+'images/'
SRD=ET.parse(os.path.expanduser('~/work/ref/srd/db.xml')).getroot().find('reference/npcdata')
def S(parent,tag,typ=None,text=None):
    e=ET.SubElement(parent,tag)
    if typ: e.set('type',typ)
    if text is not None: e.text=str(text)
    return e
def FT(parent,tag,xmlstr):
    e=ET.fromstring('<%s type="formattedtext">%s</%s>'%(tag,xmlstr,tag)); parent.append(e); return e
def WR(parent,tag,cls,rec):
    e=S(parent,tag,'windowreference'); S(e,'class',None,cls); S(e,'recordname',None,rec); return e
def ids(n): return 'id-%05d'%n
root=ET.Element('root',{'version':'5.1','dataversion':'20260124','release':'9|CoreRPG:7'})
imgfiles=sorted(os.listdir(IMG)); IMGID={}
imgroot=S(root,'image'); ic=S(imgroot,'category'); ic.set('name',CAT)
def layers(parent,f):
    im=S(parent,'image','image'); S(im,'color',None,'#FFFFFFFF'); ls=S(im,'layers'); l=S(ls,'layer')
    S(l,'name',None,f); S(l,'id',None,0); S(l,'parentid',None,-1); S(l,'type',None,'image'); S(l,'bitmap',None,'images/'+f)
def pretty(n):
    for a,b in (('npc-','NPC — '),('scene-','Scene Art — '),('battlemap-','Battlemap — '),('item-','Item — ')):
        if n.startswith(a): return b+n[len(a):].replace('-',' ').title()
    return n.replace('-',' ').title()
for k,f in enumerate(imgfiles,1):
    n=os.path.splitext(f)[0]; IMGID[n]=ids(k); r=S(ic,ids(k)); layers(r,f); S(r,'name','string',pretty(n))
def imgblock(blocks,order,name):
    b=S(blocks,ids(order)); S(b,'blocktype','string','image'); S(b,'caption','string',pretty(name))
    f=[x for x in imgfiles if os.path.splitext(x)[0]==name][0]; layers(b,f)
    WR(b,'imagelink','imagewindow','image.'+IMGID[name]); S(b,'order','number',order)
npcroot=S(root,'npc'); nc=S(npcroot,'category'); nc.set('name',CAT); NPC={}; TOK={}
DRESS={'winterwolf':"It speaks Common first, reasonably: \"One mule, and you pass.\" It is lying. It opens with Cold Breath on the mules if the party bargains.",
 'saber_toothedtiger':"Winter-mad and starving; ribs showing. It fights to the death and goes for whoever looks smallest. 5-6 PCs: its mate comes out of the den on round 2.",
 'thug':"Each carries one flask of lamp-oil (that's how the tent burns). They knock PCs out rather than kill, and flee the moment real resistance or Naran's riders appear. A captured thug names Kezrin on Intimidation DC 13.",
 'scout':"Chakyik riders are mounted on steppe ponies (riding horse). The beaters in Scene 04 shoot from the ravine rim and never descend; one has trader's Common.",
 'berserker':"Duel rules: first to three hits, non-lethal (a hit that would drop a combatant to 0 leaves them at 1 and counts as a hit). Sarnai stops it. The champion always fights Reckless; the crowd expects it.",
 'spy':"Kezrin never fights if he can run. In the council chase, his Cunning Action Dash is why the chase is three rounds, not one.",
 'warhorse':"Seventeen hands, scarred muzzle, rope-burns ringing the neck. He won't carry a rider he doesn't respect. The player names him."}
COPIES=[('winterwolf','Winter Wolf','winterwolf'),('wolf','Wolf','wolf'),('saber_toothedtiger','Saber-Toothed Tiger','sabertoothedtiger'),
 ('thug',"Kezrin's Man (Thug)",'kezrinsman'),('scout','Batzorig (Scout)','batzorig'),('scout','Chakyik Beater (Scout)','beater'),
 ('berserker',"Temur's Champion (Berserker)",'temurschampion'),('spy','Master Kezrin (Spy)','kezrin'),('warhorse','The Black Stallion (Warhorse)','blackstallion'),
 ('ridinghorse','Steppe Pony (Riding Horse)','steppepony')]
for src,name,key in COPIES:
    e=copy.deepcopy(SRD.find(src)); e.tag=key; e.find('name').text=name
    t=e.find('text')
    if t is None: t=S(e,'text','formattedtext')
    if src in DRESS: p=ET.SubElement(t,'p'); b=ET.SubElement(p,'b'); b.text='Sidebar Press. '; b.tail=DRESS[src]
    p=ET.SubElement(t,'p'); i=ET.SubElement(p,'i'); i.text='Statblock: 5E SRD 5.1 (CC-BY-4.0).'
    if key=='kezrin':
        if e.find('picture') is not None: e.remove(e.find('picture'))
        S(e,'picture','token','images/npc-kezrin.webp@'+MOD)
    nc.append(e); NPC[key]='npc.'+key; TOK[key]=e.findtext('token') or ''
def hb(key,name,size,typ,align,ac,actext,hp,hd,speed,ab,cr,xp,senses,langs,traits,actions,bonus=(),skills='',saves='',text='',tokfrom='thug'):
    e=S(nc,key); a=S(e,'abilities')
    for n,v in zip(['strength','dexterity','constitution','intelligence','wisdom','charisma'],ab):
        x=S(a,n); S(x,'bonus','number',(v-10)//2); S(x,'score','number',v)
    S(e,'ac','number',ac); S(e,'actext','string',actext)
    def lst(tag,items):
        L=S(e,tag)
        for k,(n,d) in enumerate(items,1): it=S(L,ids(k)); S(it,'desc','string',d); S(it,'name','string',n)
    lst('actions',actions); lst('traits',traits); lst('bonusactions',bonus)
    S(e,'alignment','string',align); S(e,'cr','string',cr); S(e,'hd','string',hd); S(e,'hp','number',hp)
    S(e,'languages','string',langs); S(e,'name','string',name); S(e,'senses','string',senses); S(e,'size','string',size)
    if skills: S(e,'skills','string',skills)
    if saves: S(e,'savingthrows','string',saves)
    S(e,'speed','string',speed); S(e,'type','string',typ); S(e,'xp','number',xp)
    FT(e,'text','<h>%s</h><p>%s</p><p><i>Sidebar Press homebrew.</i></p>'%(html.escape(name),html.escape(text)))
    tok=TOK.get(tokfrom,'')
    if tok: S(e,'token','token',tok)
    NPC[key]='npc.'+key; TOK[key]=tok
MIN=('Minion','If the minion takes any damage, it drops to 0 hit points. If it succeeds on a saving throw against an effect that would deal half damage on a success, it takes no damage instead.')
hb('ochir','Ochir the Cut-Rein','Medium','humanoid (human)','neutral evil',15,'(studded leather)',52,'(8d8 + 16)','30 ft.',[12,16,14,11,12,14],'2',450,
   'passive Perception 13','Baklunish, Common, Ekbiri dialect',
   [('Tent-City Born',"Ochir has advantage on Dexterity (Stealth) checks made in the Chakyik camp. Riders who don't know his face take him for one of their own.")],
   [('Multiattack','Ochir makes two Scimitar attacks or two Horn Bow attacks.'),('Scimitar','Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage.'),('Horn Bow','Ranged Weapon Attack: +5 to hit, range 150/600 ft., one target. Hit: 7 (1d8 + 3) piercing damage.')],
   bonus=[("Cut-Rein's Order (Recharge 5-6)",'One ally within 30 ft. that can hear Ochir uses its reaction to move up to half its speed and make one weapon attack.')],
   skills='Animal Handling +3, Intimidation +4, Perception +3, Stealth +5',saves='Dex +5',
   text="A Chakyik rider cast out of the horde, now Kezrin's man in the tent-city. The grinning-skull brand of Iuz is inside his left forearm (Religion DC 12). He shoots from the tent-line and spends his Order on whoever holds the ravine evidence. He knocks PCs out rather than kill them, and runs when Naran's riders arrive. Captured, he says nothing.",tokfrom='scout')
def wolfmin(key,name,where): hb(key,name,'Medium','beast','unaligned',13,'(natural armor)',1,'(minion)','50 ft.',[12,15,12,3,12,6],'3',175,'passive Perception 11','-',
   [MIN,('Keen Hearing and Smell','The wolf has advantage on Wisdom (Perception) checks that rely on hearing or smell.'),('Pack Tactics (Skirmisher)',"The wolf has advantage on an attack roll against a creature if at least one of its allies is within 5 feet of the creature and the ally isn't incapacitated.")],
   [('Bite','Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 piercing damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone.')],
   text='Optional minion pack (%s). Skirmisher Minion template, APL 3. Every four count as one creature for the encounter multiplier.'%where,tokfrom='wolf')
wolfmin('steppewolfminion','Steppe Wolf (Skirmisher Minion)','Scene 01, running with the winter wolf')
wolfmin('ravinewolfminion','Ravine Wolf (Skirmisher Minion)',"Scene 04, starving wolves drawn by the tiger's kills")
hb('kezrinsmanminion',"Kezrin's Man (Brute Minion)",'Medium','humanoid (human)','neutral evil',12,'(leather armor)',1,'(minion)','30 ft.',[15,11,14,10,10,11],'3',175,'passive Perception 10','Common',
   [MIN,('Death-Blow (Brute)','When the minion drops to 0 hit points from a melee attack, it can make one attack against the attacker before it dies.')],
   [('Club','Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 bludgeoning damage.')],
   text="Optional minion pack (Scene 05). Brute Minion template, APL 3. They pull their blows (7 damage, not the template's 14): Kezrin wants the party scared off, not dead.")
def npcname(key): return nc.find(key).findtext('name')
batroot=S(root,'battle'); bc=S(batroot,'category'); bc.set('name',CAT); BAT={}
XP={'winterwolf':700,'wolf':50,'sabertoothedtiger':450,'kezrinsman':100,'ochir':450,'temurschampion':450,'steppewolfminion':175,'ravinewolfminion':175,'kezrinsmanminion':175}
BATS=[('E1a','01 Steppe Predators (4 PCs)',[('winterwolf',1)],None),('E1b','01 Steppe Predators (5-6 PCs)',[('winterwolf',1),('wolf',2)],None),
 ('E4a','04 The Saber-Tooth (4 PCs)',[('sabertoothedtiger',1)],'battlemap-ravine'),('E4b','04 The Saber-Tooth (5-6 PCs)',[('sabertoothedtiger',2)],'battlemap-ravine'),
 ('E5a','05 The Night Visit (4 PCs)',[('ochir',1),('kezrinsman',2)],'battlemap-guest-camp'),('E5b','05 The Night Visit (5-6 PCs)',[('ochir',1),('kezrinsman',3)],'battlemap-guest-camp'),
 ('E7a',"07 Champion's Duel",[('temurschampion',1)],'battlemap-duel-ring'),
 ('M1','Optional - 01 Steppe Wolf minion pack',[('steppewolfminion',4)],None),('M4','Optional - 04 Ravine Wolf minion pack',[('ravinewolfminion',4)],'battlemap-ravine'),
 ('M5',"Optional - 05 Kezrin's Man minion pack",[('kezrinsmanminion',4)],'battlemap-guest-camp')]
for k,(code,name,lst,mp) in enumerate(BATS,1):
    r=S(bc,ids(k)); S(r,'exp','number',sum(XP.get(n,0)*c for n,c in lst))
    if mp: WR(r,'maplink','imagewindow','image.'+IMGID[mp])
    S(r,'name','string','%s %s'%(code,name)); L=S(r,'npclist')
    for j,(n,c) in enumerate(lst,1):
        it=S(L,ids(j)); S(it,'count','number',c); S(it,'faction','string','foe'); WR(it,'link','npc',NPC[n]); S(it,'name','string',npcname(n))
        if TOK.get(n): S(it,'token','token',TOK[n])
    BAT[code]='battle.'+ids(k)
itroot=S(root,'item'); itc=S(itroot,'category'); itc.set('name',CAT); ITEM={}
ITEMS=[('tigerclawtoken','Tiger-Claw Token','Wondrous Item','','Uncommon',"<p><i>Wondrous item, uncommon (no attunement)</i></p><p>A large tiger claw on a braided leather cord, scrimshawed with tiny tiger-stripe marks. Ilkhan Cligir wears it on his wrist until he gives it away.</p><p><b>The Tiger's Mark.</b> While worn, the wearer has advantage on Charisma checks made to interact with Baklunish nomads.</p><p><b>At the Council.</b> The Round 1 Persuasion DC drops from 14 to 12.</p><p><b>Safe Passage.</b> Chakyik riders let the wearer and companions pass through their camps unharmed. The token loses this property if its holder breaks faith with the Chakyik.</p>",'item-tigers-mark'),
 ('hornbow','Horn Bow','Weapon','Martial Ranged Weapons','','<p>A Chakyik composite bow of horn, sinew and wood. Use longbow statistics (1d8 piercing, range 150/600, heavy, two-handed). The horde lends horn bows for the Trial of the Bow; no proficiency is needed for the trial.</p>',None),
 ('falsewolfarrows','The False Wolf Arrows','Adventuring Gear','','',"<p>Grey goose fletching, Wolf-style at a glance. Wolf Nomads bind fletching with sinew in a crisscross; these are glued, and the grey is paint over brown feather. With them: a black-steel arrowhead and, eventually, Tsolmon's arrow from Temur's sash. Climax evidence, not loot.</p>",'item-false-arrow')]
for key,name,typ,sub,rar,desc,img in ITEMS:
    r=S(itc,key); S(r,'name','string',name); S(r,'type','string',typ)
    if sub: S(r,'subtype','string',sub)
    if rar: S(r,'rarity','string',rar)
    if key=='hornbow': S(r,'damage','string','1d8 piercing'); S(r,'properties','string','Ammunition (range 150/600), heavy, two-handed'); S(r,'weight','number',2)
    S(r,'isidentified','number',1); FT(r,'description',desc)
    if img: S(r,'picture','token','images/%s.webp@%s'%(img,MOD))
    ITEM[key]='item.'+key
M=sections(body(V+'SP-PBS-01-The-False-Arrow.md'))
def pick(*names): return '\n'.join('## %s\n%s'%(n,M[n]) for n in names if n in M)
SC=sorted(glob.glob(V+'Scenes/Scene 0*.md'))
def scene(n): return re.sub(r'^# .*\n','',body(SC[n]),count=1)
def links(*items):
    s='<linklist>'
    for cls,rec,label in items: s+='<link class="%s" recordname="%s">%s</link>'%(cls,rec,html.escape(label))
    return s+'</linklist>'
B=lambda c: ('battle',BAT[c],'Encounter: '+[b[1] for b in BATS if b[0]==c][0])
N=lambda k: ('npc',NPC[k],'NPC: '+npcname(k))
I=lambda k: ('imagewindow','image.'+IMGID[k],'Image: '+pretty(k))
IT=lambda k: ('item',ITEM[k],'Item: '+[i[1] for i in ITEMS if i[0]==k][0])
strip=lambda s: s.replace('Back to [[SP-PBS-01-The-False-Arrow]]','')
cover='<p><b>APL 3 (level 3) · 4–6 characters · one 3½-hour session</b></p><p>Part 1 of <i>The Plains of Blood and Steel</i>. A Sidebar Press adventure for the Greyhawk University campaign frame.</p>'
hand=lambda f: conv(strip(body(V+f)))
PAGES=[
 ('Introduction','Cover',['Cover'],None,cover),
 ('Introduction','Credits & How to Run',[],None,'<p><b>The False Arrow</b> · SP-PBS-01 · Sidebar Press. Premise after "Nomad\'s Land" by John Lent. Creature statblocks marked SRD are from the 5E SRD 5.1 (CC-BY-4.0).</p>'+conv(pick('Date','Campaign Frame','Design Frame','Hook','PC Objectives','Subplots (keyed to PCs; assign at the table)','Act Structure'))),
 ('Introduction','Background',['regional-map'],None,conv(pick('Chakyik Color','What the Locals Know',"What's Really Happening",'Climax at a Glance'))),
 ('Introduction','Cast & Locations',['npc-cligir','npc-temur','npc-sarnai','npc-kezrin','npc-brennin','npc-halya','npc-naran'],links(N('kezrin'),N('ochir'),N('batzorig'),N('temurschampion')),conv(pick('Key NPCs','Key Locations'))),
 ('Introduction','Encounter Summary',[],links(*[B(b[0]) for b in BATS]),conv(pick('Encounters'))),
 ('Introduction','The Favor Tracker',[],None,conv(strip(body(V+'SP-PBS-01 — The Favor Tracker.md')))),
 ('Act 1 — The Road','Scene 00 — Greyhawk University',['scene-ritterstadt','scene-job-board'],None,conv(scene(0))),
 ('Act 1 — The Road','Scene 01 — The High Pass',['scene-hospice','scene-camp-panorama'],links(B('E1a'),B('E1b'),B('M1'),N('winterwolf'),N('wolf')),conv(scene(1))),
 ('Act 1 — The Road','Scene 02 — The Cold Welcome',['scene-pavilion','map-winter-camp'],links(N('batzorig')),conv(scene(2))),
 ('Act 2 — The Trials','Scene 03 — Trial of the Horse',['scene-black-stallion'],links(N('blackstallion')),conv(scene(3))),
 ('Act 2 — The Trials','Scene 04 — Trial of the Bow',['scene-fog-ravine'],links(B('E4a'),B('E4b'),B('M4'),N('sabertoothedtiger'),N('beater'),I('battlemap-ravine'),IT('hornbow'),IT('falsewolfarrows')),conv(scene(4))),
 ('Act 2 — The Trials','Scene 05 — Night in Yecha',['scene-night-attack'],links(B('E5a'),B('E5b'),B('M5'),N('ochir'),N('kezrinsman'),N('kezrin'),I('battlemap-guest-camp')),conv(scene(5))),
 ('Act 2 — The Trials','Scene 06 — Trial of the Fire',['scene-sarnais-fire'],None,conv(scene(6))),
 ('Act 3 — The Council','Scene 07 — The War Council',['scene-war-council'],links(B('E7a'),N('temurschampion'),N('kezrin'),I('battlemap-duel-ring'),IT('tigerclawtoken')),conv(scene(7))),
 ('Act 3 — The Council','Rewards & Continuity',['item-tigers-mark'],links(IT('tigerclawtoken'),N('blackstallion'),N('steppepony')),conv(pick('Treasure & Rewards','Continuity'))),
 ('Appendices','Bestiary',[],links(*[N(k) for k in NPC]),conv(strip(body(V+'SP-PBS-01 — Bestiary.md')))),
 ('Appendices',"Handout 1 — Brennin's Parley Letter",[],None,hand("SP-PBS-01 — Handout — Brennin's Parley Letter.md")),
 ('Appendices',"Handout 2 — Halya's Sealed Instruction",[],None,hand("SP-PBS-01 — Handout — Halya's Sealed Instruction.md")),
 ('Appendices',"Handout 3 — Kezrin's Papers",['item-kezrin-papers'],None,hand("SP-PBS-01 — Handout — Kezrin's Papers.md")),
 ('Appendices','Maps',['battlemap-ravine','battlemap-guest-camp','battlemap-duel-ring'],links(I('battlemap-ravine'),I('battlemap-guest-camp'),I('battlemap-duel-ring'),I('map-winter-camp'),I('regional-map')),'<p>Painted battlemaps for Encounters 4, 5 and 7. The grid is not set: calibrate it in Fantasy Grounds (5-ft. squares) before play.</p>'),
]
ref=S(root,'reference'); rd=S(ref,'refmanualdata'); ri=S(ref,'refmanualindex'); chs=S(ri,'chapters')
ch=S(chs,ids(1)); S(ch,'name','string','SP-PBS-01 — The False Arrow'); S(ch,'order','number',1); subs=S(ch,'subchapters')
SUB={}; stop=set('the and a an of to in is it on for with as at by or be if that this their they them from are was but not his her he she you your one two any all can will has have who what when'.split())
for k,(sec,pname,imgs,ll,xml) in enumerate(PAGES,1):
    if sec not in SUB:
        s=S(subs,ids(len(SUB)+1)); S(s,'name','string',sec); S(s,'order','number',len(SUB)+1); SUB[sec]=[S(s,'refpages'),0]
    SUB[sec][1]+=1; rp,n=SUB[sec]
    pid=ids(k); pg=S(rd,pid); bl=S(pg,'blocks'); o=0
    for im in imgs: o+=1; imgblock(bl,o,im)
    if ll: o+=1; b=S(bl,ids(o)); S(b,'blocktype','string','singletext'); S(b,'frame','string','sidebar'); FT(b,'text','<p><b>Records for this page</b></p>'+ll); S(b,'order','number',o)
    o+=1; b=S(bl,ids(o)); S(b,'blocktype','string','singletext'); FT(b,'text',xml); S(b,'order','number',o)
    S(pg,'name','string',pname)
    words=sorted({w for w in re.findall(r"[a-z][a-z'-]{2,}",re.sub(r'<[^>]+>',' ',xml).lower()) if w not in stop})
    e=S(rp,ids(n)); S(e,'keywords','string',' '.join(words[:400])); WR(e,'listlink','story_book_page_advanced','reference.refmanualdata.'+pid); S(e,'name','string',pname); S(e,'order','number',n)
lib=S(root,'library'); le=S(lib,'spbps01thefalsearrow'); le.set('static','true')
S(le,'categoryname','string','Sidebar Press'); S(le,'name','string','spbps01thefalsearrow'); en=S(le,'entries')
x=S(en,'_story_book'); WR(x,'librarylink','reference_manual','reference.refmanualindex'); S(x,'name','string','Book - SP-PBS-01 — The False Arrow')
for tag,label in (('battle','Encounters'),('image','Images'),('item','Items'),('npc','NPCs')):
    x=S(en,tag); WR(x,'librarylink','reference_list','..'); S(x,'name','string',label); S(x,'recordtype','string',tag)
ET.indent(root,'\t')
db=b'<?xml version="1.0" encoding="utf-8"?>\n'+ET.tostring(root,encoding='utf-8')
ET.fromstring(db)
defn='<?xml version="1.0" encoding="utf-8"?>\n<root version="5.1" dataversion="20260124" release="9|CoreRPG:7">\n\t<name>%s</name>\n\t<displayname>SP-PBS-01 — The False Arrow</displayname>\n\t<category>Sidebar Press</category>\n\t<author>Sidebar Press</author>\n\t<ruleset>5E</ruleset>\n</root>\n'%MOD
from PIL import Image
im=Image.open(IMG+'Cover.webp').convert('RGB'); im.thumbnail((256,256)); im.save(W+'thumbnail.png')
out=sys.argv[1]
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
    z.writestr('definition.xml',defn); z.writestr('db.xml',db); z.write(W+'thumbnail.png','thumbnail.png')
    for f in imgfiles: z.write(IMG+f,'images/'+f)
open(W+'db.xml','wb').write(db)
print('pages',len(PAGES),'npcs',len(NPC),'battles',len(BATS),'items',len(ITEMS),'images',len(imgfiles),'db KB',len(db)//1024,'mod MB',round(os.path.getsize(out)/1048576,1))
