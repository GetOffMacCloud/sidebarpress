"""SP-SQ-01 The Gaoler's Link -> Fantasy Grounds module. Run: python3 module.py [--install]
Uses the shared builder in 70-Company/Tools/fgu-module-builder (see the fgu-module-build skill).
v1 (2026-11-06): no battlemaps or scene plates yet; rebuild when the art lands in 99-Assets/SP-SQ/."""
import os,sys,re,glob,shutil
HERE=os.path.dirname(os.path.abspath(__file__)); ADV=os.path.dirname(os.path.dirname(HERE)); VAULT=os.path.dirname(os.path.dirname(ADV))
sys.path.insert(0,os.path.join(VAULT,'70-Company','Tools','fgu-module-builder'))
from fgmod import Mod, conv, body, sections
FG=os.environ.get('FG_DIR',os.path.expanduser('~/mnt/Fantasy Grounds'))
# ---- edition settings (a renamed edition changes only this block) ----
CODE='SP-SQ-01'; NAME="SP-SQ-01 The Gaoler's Link"; DISPLAY="SP-SQ-01 — The Gaoler's Link"
SRC=ADV; ASSETS=os.path.join(VAULT,'99-Assets','SP-SQ'); EXCLUDE_IMAGES=(); TEXT_MAP={}
FRAME='Greyhawk University'
# -----------------------------------------------------------------------
WORK=os.path.expanduser('~/work/fgu/'+CODE); STAGE=os.path.join(WORK,'src-images'); os.makedirs(STAGE,exist_ok=True)
def stage(src,name):
    if os.path.exists(src):
        out=os.path.join(STAGE,name+os.path.splitext(src)[1])
        if not os.path.exists(out) or os.path.getmtime(out)<os.path.getmtime(src): shutil.copyfile(src,out)
stage(os.path.join(ASSETS,'cover','SP-SQ-01-cover.png'),'Cover')
stage(os.path.join(ASSETS,'handouts',"The Gaoler's Link — Handout.png"),'item-gaolers-link')
SIG=[]
for f in sorted(glob.glob(os.path.join(ASSETS,'handouts','Sigil *.png'))):
    n='handout-'+re.sub(r'[^a-z0-9]+','-',os.path.basename(f)[:-4].lower().replace(' — ',' ')).strip('-'); stage(f,n); SIG.append(n)
for f in sorted(glob.glob(os.path.join(ASSETS,'plates','*.png'))): stage(f,'scene-'+re.sub(r'[^a-z0-9]+','-',os.path.basename(f)[:-4].lower().replace(CODE.lower(),'')).strip('-'))
for f in sorted(glob.glob(os.path.join(ASSETS,'maps','*.*'))): stage(f,'battlemap-'+re.sub(r'[^a-z0-9]+','-',os.path.basename(f).rsplit('.',1)[0].lower().replace(CODE.lower(),'')).strip('-'))
SL=lambda n: re.sub(r'[^a-z0-9]+','-',n.lower()).strip('-')
PORTN={}
for f in sorted(glob.glob(os.path.join(ASSETS,'portraits','SP-SQ-01 Portrait - *.png'))):
    n=os.path.basename(f)[:-4].split(' - ',1)[1]; stage(f,'npc-'+SL(n)); PORTN['npc-'+SL(n)]='NPC — '+n
m=Mod(NAME,DISPLAY,'Sidebar Press','Sidebar Press',FG,WORK,text_map=TEXT_MAP)
NICE={'Cover':'Cover','item-gaolers-link':"Item — The Gaoler's Link"}
for f in glob.glob(os.path.join(ASSETS,'handouts','Sigil *.png')):
    b=os.path.basename(f)[:-4]; NICE['handout-'+re.sub(r'[^a-z0-9]+','-',b.lower().replace(' — ',' ')).strip('-')]='Handout — '+b
NICE.update(PORTN)
HO={}
for f in sorted(glob.glob(os.path.join(ASSETS,'handouts','SP-SQ-01 Handout - *.png'))):
    n=os.path.basename(f)[:-4].split(' - ',1)[1]; k='ho-'+SL(n); stage(f,k); NICE[k]='Handout — '+n; HO[n]=k
m.pretty=lambda n,_p=Mod.pretty: NICE.get(n,_p(n))
m.images(STAGE,exclude=EXCLUDE_IMAGES)
TOKF={}
for f in sorted(glob.glob(os.path.join(ASSETS,'tokens','SP-SQ-01 Token - *.png'))):
    sl=SL(os.path.basename(f)[:-4].split(' - ',1)[1]); fn='token-%s.png'%sl
    shutil.copyfile(f,os.path.join(m.img,fn)); m.imgfiles.append(fn); TOKF[sl]='images/%s@%s'%(fn,NAME)
import xml.etree.ElementTree as _ET
def settok(key,sl):
    e=m._cat('npc').find(key)
    for t in ('token','picture'):
        x=e.find(t)
        if x is not None: e.remove(x)
    if sl in TOKF: x=_ET.SubElement(e,'token'); x.set('type','token'); x.text=TOKF[sl]; m.TOK[key]=TOKF[sl]
    if 'npc-'+sl in m.IMG: x=_ET.SubElement(e,'picture'); x.set('type','token'); x.text=m.imgpath('npc-'+sl)
P=lambda pat: glob.glob(os.path.join(SRC,pat))[0]
MAIN=P(CODE+'-The-Gaolers-Link.md'); BEST=P('*Bestiary.md'); JOB=P('*The Job.md'); IDX=P('Scenes/00 — Scene Index.md')
SC=sorted(glob.glob(os.path.join(SRC,'Scenes','Scene 0*.md')))
HAND=[P('*Handout — The %s.md'%x) for x in ('Deed of Pledge','Cipher Letter','Provenance Slip','Six Sigils')]
strip=lambda s: re.sub(r'Back to \[\[[^\]]*\]\]','',s)
M=sections(body(MAIN)); pick=lambda *n: '\n'.join('## %s\n%s'%(x,M[x]) for x in n if x in M)
scene=lambda n: re.sub(r'^# .*\n','',body(SC[n]),count=1)
title=lambda n: re.sub(r'^.*?(Scene 0\d —)',r'\1',os.path.basename(SC[n])[:-3])
def nocallout(t,kinds=('art',)):
    out=[];skip=False
    for l in t.split('\n'):
        if any(l.startswith('> [!%s'%k) for k in kinds): skip=True; continue
        if skip and l.startswith('>'): continue
        skip=False; out.append(l)
    return '\n'.join(out)
def itemdesc(fname,secs=('Properties','The Six Sigils','History')):
    t=nocallout(body(os.path.join(VAULT,'50-Items',fname+'.md'))); t=re.sub(r'^# .*\n','',t,count=1)
    intro=t.split('\n## ',1)[0]; S=sections(t)
    return conv(intro+'\n'+'\n'.join('### %s\n%s'%(k,S[k]) for k in secs if k in S))
# ---- NPCs (SRD copies, renamed) ----
m.npc_srd('quasit','Snick (Quasit)','snick',dress="Vesharan's familiar, usually invisible. It spies, steals and runs; it flees at the first real hit. Its claws smoke and burn on the Gaoler's Link, and it drops it. Captured, it bargains for sugar and its life.")
m.npc_srd('noble','Ottokar Brandmeier (Noble)','brandmeier',dress='Not a combatant. Tethered: a bone pin in his collar lining (DC 13 Investigation). He wakes, confused, within 30 ft. of the unboxed Link or when the pin is pulled.')
m.npc_srd('scout','Tegin (Scout)','tegin',dress="The Hecht's Wolf Nomad pilot (APL 4 only). Fights for pay and quits at half hit points. Tethered (a pin in the cap), so the pilot wakes near the Link.")
m.npc_srd('veteran','Jobst Ruder (Veteran)','ruder',dress="Master of the Graue Hecht. Won't fight students; included for completeness.")
m.npc_srd('guard','Gate Rota / Proctor (Guard)','gaterota',dress='Jens Ober, Mathias Grell, Garrok Stonebrow and Hask\'s men use this block. NONLETHAL: they grab, shout and hold. A PC who kills one ends their career (Conclusion D).')
m.npc_srd('bandit','Weil Brother (Bandit)','weil',dress='Konstanz and Rudi Weil, indebted Freshmen. Nonlethal; they surrender at the first sign of authority.')
# ---- NPCs (homebrew; statblocks from 65-Bestiary/Shadow on the Quag) ----
def addf(key,**kw):
    e=m._cat('npc').find(key)
    for k,v in kw.items():
        x=e.find(k)
        if x is None: x=__import__('xml.etree.ElementTree',fromlist=['x']).SubElement(e,k); x.set('type','string')
        x.text=v
MIN=('Minion','If the minion takes any damage, it drops to 0 hit points. If it succeeds on a saving throw against an effect that would deal half damage on a success, it takes no damage instead.')
INTERPOSE=('Interpose (Enforcer)','When another creature the minion can see within 5 feet of it is hit by an attack, the minion steps into the blow. The attack hits the minion instead.')
m.npc('vesharan','Dawud Vesharan (Tether-Mage)','Medium','humanoid (human)','neutral evil',15,'(mage armor; 12 without)',58,'(13d8)','30 ft.',[9,14,10,17,12,14],'2',450,'passive Perception 11','Common, Abyssal, Bakluni',
  traits=[('Spellcasting','The mage casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 13, +5 to hit with spell attacks):\nAt will: friends, mage hand, minor illusion\n1/day each: charm person, command, disguise self, hold person, mage armor, suggestion'),
          ("Tether's Eye",'As a bonus action, the mage perceives through the senses of its familiar, or of any creature wearing one of its bone tethers, if that creature is within 1 mile of it. This lasts until the start of its next turn, and during it the mage is blinded and deafened with regard to its own surroundings.')],
  actions=[('Multiattack','The mage makes two Splinter of Will attacks.'),('Splinter of Will','Ranged Spell Attack: +5 to hit, range 60 ft., one creature. Hit: 8 (2d4 + 3) psychic damage.'),('Dagger','Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d4 + 2) piercing damage.')],
  reactions=[("Puppet's Shield",'When a creature the mage can see targets it with an attack, the mage chooses a creature charmed by it within 5 feet of it. That creature becomes the attack\'s target instead.')],
  skills='Arcana +5, Deception +4, Insight +3',saves='Int +5, Wis +3',
  text='"Herr Fesch", Brandmeier\'s quiet clerk: Kermin Mind-Bender\'s tether-mage (Named Example of the Tether-Mage). Mage armor is cast before Scene 06 (AC 15). He never touches the Link, fights from range with command and hold person, uses Puppet\'s Shield every round he can, and keeps a crate between himself and any holy symbol. He carries a potion of water breathing; at half hit points he drinks it and dives over the rail for the reeds. He can be stopped: grapple him, guard the rail, or put a PC in the water. Captured within 30 ft. of the Link, he can be turned.')
SLEEP=dict(traits=[("Sleeper's Calm","The sleeper speaks in flat, borrowed phrases and can't be frightened."),('Tether-Bound','The sleeper is charmed by its handler, a creature that planted a bone tether on it. While charmed this way it makes no saving throws to end the effect. If its tether is removed, or if it starts its turn within 30 feet of the unboxed Gaoler\'s Link, it is incapacitated until the end of its next turn. After that, it is no longer charmed and stops fighting, confused about where it is and why.'),("Handler's Window","The sleeper's handler can perceive through its senses (see the Tether-Mage's Tether's Eye).")],
  actions=[('Multiattack','The sleeper makes two Cudgel attacks.'),('Cudgel','Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) bludgeoning damage.')])
m.npc('sleeper','Hecht Bargeman (Tethered Sleeper)','Medium','humanoid (human)','any alignment',12,'(leather armor)',32,'(5d8 + 10)','30 ft.',[13,12,14,10,8,10],'1/4',50,'passive Perception 9','Common',**SLEEP,token_from='weil',
  text='Piet Lanz and Arnold Fenn, the Hecht\'s bargemen, with cargo hooks used as cudgels. INNOCENTS: they wake and stop fighting within 30 ft. of the unboxed Link, or when the pin in the cap is pulled. Carrying the Link toward them is a tactic; tell the players once.')
addf('sleeper',conditionimmunities='frightened')
GUARD=dict(traits=[('Antimagic Susceptibility',"The guardian is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the guardian must succeed on a Constitution saving throw against the caster's spell save DC or fall unconscious for 1 minute."),('False Appearance','While the guardian remains motionless on its mount, it is indistinguishable from an ordinary mounted trophy.'),('Watchword','The guardian stops, goes still, and returns to its mount when a creature within 30 feet of it speaks its watchword aloud. Its maker sets the watchword.')],
  actions=[('Bite','Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) piercing damage. If the target is a Medium or smaller creature, it is grappled (escape DC 13). Until this grapple ends, the guardian can\'t bite another target.'),('Tail Sweep (Recharge 5-6)','Each creature within 10 feet of the guardian must make a DC 13 Dexterity saving throw. On a failure, a creature takes 7 (1d8 + 3) bludgeoning damage and is knocked prone. On a success, it takes half as much damage and isn\'t knocked prone.')],
  immunities='poison, psychic')
PIKE='The Archive Pike (A5), a stuffed lake pike on its board. Watchword: "by leave of the Registrar." It blocks the grille gate and bites the bearer of the coffer, dragging them toward its board. The fight is a Heat clock, not a killer: each round is +1 Heat. Remind the table that the watchword exists.'
for key,name,hp,hd,txt in (('archivepike','Archive Pike (Trophy Guardian)',52,'(7d10 + 14)',PIKE),('archivepike2','Archive Pike, APL 2 (Trophy Guardian)',25,'(7d10 + 14; reduced)',PIKE+' APL 2 version: 25 hp.'),('lakegar','Lake Gar (Trophy Guardian)',52,'(7d10 + 14)','APL 4 only: a matched lake gar on the next board wakes with the pike. Same watchword.')):
    m.npc(key,name,'Large','construct','unaligned',14,'(natural armor)',hp,hd,'15 ft., swim 40 ft.',[16,8,14,1,5,1],'1',200,'blindsight 60 ft. (blind beyond this radius), passive Perception 7','-',**GUARD,text=txt)
    addf(key,conditionimmunities='blinded, charmed, deafened, exhaustion, frightened, paralyzed, petrified, poisoned')
m.npc('probationer','Gate-Rota Probationer (Enforcer Minion)','Medium','humanoid (any race)','any alignment',15,'(padded jack, shield)',1,'(minion)','30 ft.',[13,12,12,10,11,10],'3',175,'passive Perception 10','Common',
  traits=[MIN],actions=[('Bog Pole','Melee Weapon Attack: +4 to hit, reach 10 ft., one target. Hit: 7 bludgeoning damage. The Probationer can choose to deal no damage and instead push the target 5 feet.')],reactions=[INTERPOSE],token_from='gaterota',
  text='Optional minion pack (Scene 05), for when the gate rota turns out in force (Alert). Enforcer Minion template, APL 3; every four count as one creature for the multiplier. Other APLs: APL 2 AC 15, +3, DC 13, 5 damage, 112 XP; APL 4 AC 16, +5, DC 14, 9 damage, 275 XP. CAUTION: they are students. They fight to hold, never to kill; a PC who kills one has ended their career.')
m.npc('bargemanminion','Hecht Bargeman (Enforcer Minion)','Medium','humanoid (human)','any alignment',15,'(leather jerkin, cargo hook)',1,'(minion)','30 ft., swim 30 ft.',[13,12,14,10,8,10],'3',175,'passive Perception 9','Common',
  traits=[MIN,('Tether-Bound','If the bargeman starts its turn within 30 feet of the unboxed Gaoler\'s Link, it is incapacitated until the end of its turn and then stops fighting.')],
  actions=[('Cargo Hook','Melee Weapon Attack: +4 to hit, reach 10 ft., one target. Hit: 7 piercing damage.')],reactions=[INTERPOSE],token_from='weil',
  text="Optional minion pack (Scenes 06-07), for when the Hecht's other bargemen pile in at Alert. Enforcer Minion template, APL 3. Other APLs: APL 2 AC 15, +3, DC 13, 5 damage, 112 XP; APL 4 AC 16, +5, DC 14, 9 damage, 275 XP. CAUTION: tethered innocents; each drops out within 30 ft. of the unboxed Link, and the party should be told.")
addf('bargemanminion',conditionimmunities='frightened')
for k,sl in (('vesharan','dawud-vesharan'),('snick','snick'),('sleeper','hecht-bargeman'),('bargemanminion','hecht-bargeman'),('tegin','tegin'),('brandmeier','ottokar-brandmeier'),('ruder','jobst-ruder'),('gaterota','mathias-grell'),('probationer','gate-rota-probationer'),('archivepike','archive-pike'),('archivepike2','archive-pike'),('lakegar','lake-gar')): settok(k,sl)
# ---- encounters (one per APL band; scenes give APL 2/3/4 rows) ----
MAP=lambda k: next((x for x in sorted(m.IMG) if x.startswith(k) and 'dm' not in x.split('-')),None)
m.battle('E5a','05 The Archive Pike (APL 2)',[('archivepike2',1)],MAP('battlemap-archive'))
m.battle('E5b','05 The Archive Pike (APL 3)',[('archivepike',1)],MAP('battlemap-archive'))
m.battle('E5c','05 The Archive Pike (APL 4)',[('archivepike',1),('lakegar',1)],MAP('battlemap-archive'))
m.battle('E5d','05 Caught by the Gate Rota (nonlethal)',[('gaterota',3)],MAP('battlemap-archive'))
m.battle('E6a','06 The Handover (APL 2)',[('vesharan',1),('sleeper',1),('snick',1)],MAP('battlemap-hecht-1'))
m.battle('E6b','06 The Handover (APL 3)',[('vesharan',1),('snick',1),('sleeper',2)],MAP('battlemap-hecht-1'))
m.battle('E6c','06 The Handover (APL 4)',[('vesharan',1),('snick',1),('sleeper',2),('tegin',1)],MAP('battlemap-hecht-1'))
m.battle('E7a','07 The Hold (APL 2-3)',[('sleeper',2)],MAP('battlemap-hecht-3'))
m.battle('E7b','07 The Hold (APL 4)',[('sleeper',2),('tegin',1)],MAP('battlemap-hecht-3'))
m.battle('M5','Optional - 05 Gate-Rota Probationer minion pack',[('probationer',4)],MAP('battlemap-archive'))
m.battle('M6','Optional - 06-07 Hecht Bargeman minion pack',[('bargemanminion',4)],MAP('battlemap-hecht-1'))
# ---- items ----
m.item('gaolerslink',"The Gaoler's Link",'Wondrous Item',itemdesc("The Gaoler's Link"),rarity='Artifact',picture='item-gaolers-link')
m.item('ashbox','The Ashbox','Wondrous Item',itemdesc('The Ashbox'),rarity='Uncommon')
m.item('bonetether','Bone Tether','Wondrous Item',itemdesc('Bone Tether'),rarity='Uncommon')
m.item('omentaper','Omen-Taper of the Blind Spot','Wondrous Item',itemdesc('Omen-Taper of the Blind Spot'),rarity='Common')
m.item('rubbingofthesix','Rubbing of the Six','Wondrous Item',itemdesc('Rubbing of the Six'),rarity='Common')
m.item('waterbreathing',"Potion of Water Breathing (Vesharan's)",'Potion','<p><i>Potion, uncommon</i></p><p>You can breathe underwater for 1 hour after drinking this potion. Its cloudy green fluid smells of the sea and has a jellyfish-like bubble floating in it.</p><p>Vesharan carries one into Scene 06 as his way out. If the party takes it first, he has no escape over the rail. (5E SRD 5.1, CC-BY-4.0.)</p>',rarity='Uncommon')
# ---- reference manual ----
I1,A1,A2,A3,A4,AP='Introduction','Act 1 — The Offer','Act 2 — Casing the Job','Act 3 — The Job','Act 4 — The Turn','Appendices'
X=sections(body(IDX)); xpick=lambda *n: '\n'.join('## %s\n%s'%(k,X[k]) for k in n if k in X)
m.page(I1,'Cover','<p><b>APL 3 (levels 2–4) · 4–6 characters · one 4-hour session</b></p><p>A heist for 3rd-level characters. Part 1 of <i>The Shadow on the Quag</i>. A Sidebar Press adventure for the %s campaign frame.</p>'%FRAME,images=['Cover'])
m.page(I1,'Credits & How to Run','<p><b>The Gaoler\'s Link</b> · %s · Sidebar Press. Creature statblocks marked SRD are from the 5E SRD 5.1 (CC-BY-4.0).</p><p><b>Battlemaps</b> (personal and stream use; Inkarnate community maps, CC BY-NC-SA 4.0): The Archive by Timo. The <i>Graue Hecht</i> (four decks): Mehujel. The Landing by Sidebar Press. Calibrate each map\'s grid in Fantasy Grounds (5-ft squares). Scene art is not in this version.</p>'%CODE+conv(pick('Date','Design Frame','Hook','PC Objectives (the plot, as goals rather than events)','Subplots (keyed to PCs; assign at the table)','Act Structure')))
m.page(I1,'Background',conv(pick('Ritterstadt Color','What the Locals Know',"What's Really Happening","Vesharan's Scheme",'Climax at a Glance')),links=[m.N('vesharan'),m.N('brandmeier'),m.IT('gaolerslink')])
m.page(I1,'Cast & Locations',conv(pick('Key NPCs','Key Locations')),images=[k for k in PORTN if k in m.IMG],links=[m.N(k) for k in ('brandmeier','vesharan','snick','ruder','tegin','sleeper','gaterota','weil')])
m.page(I1,'The Job: Edges, Heat & Alert',conv(strip(nocallout(body(JOB),('art','info'))).split('\n# ',1)[-1]),links=[m.IT('gaolerslink'),m.IT('ashbox'),m.N('snick')])
m.page(I1,'Running the Adventure',conv(xpick('Run Sheet','Spotlight Check','Standing Trackers','Clue Ledger (tick as found)','Nudge List')))
m.page(I1,'Encounter Summary',conv(pick('Encounters')),links=[m.B(c) for c in m.BAT])
LK={0:[m.N('brandmeier'),m.N('vesharan'),m.N('snick')],1:[m.N('brandmeier'),m.N('vesharan')],2:[m.N('snick'),m.N('ruder'),m.N('tegin'),m.IT('omentaper')],
    3:[m.N('archivepike'),m.IT('gaolerslink'),m.I('item-gaolers-link')],
    4:[m.B(c) for c in ('E5a','E5b','E5c','E5d','M5')]+[m.N(k) for k in ('archivepike','lakegar','gaterota','weil','probationer')]+[m.IT('gaolerslink')],
    5:[m.B(c) for c in ('E6a','E6b','E6c','M6')]+[m.N(k) for k in ('vesharan','snick','sleeper','tegin','bargemanminion')]+[m.IT(k) for k in ('ashbox','gaolerslink','bonetether','waterbreathing')],
    6:[m.B(c) for c in ('E7a','E7b','M6')]+[m.N(k) for k in ('sleeper','tegin','ruder','vesharan','brandmeier')]+[m.IT('bonetether'),m.IT('ashbox')],
    7:[m.IT('rubbingofthesix'),m.IT('omentaper'),m.N('vesharan')]}
ACT={0:A1,1:A1,2:A2,3:A2,4:A3,5:A4,6:A4,7:A4}
PL=lambda n: [k for k in m.IMG if k.startswith('scene-') and k.split('-',1)[1].startswith('s%02d'%(n+1))]
SCP={0:['ottokar-brandmeier','dawud-vesharan'],2:['perenna-dolz','jens-ober','jobst-ruder'],3:['casimir-vogelsang','hedwig-ammerlin'],4:['archive-pike','mathias-grell'],5:['dawud-vesharan','snick'],6:['jobst-ruder','tegin','hecht-bargeman'],7:['liesl-amsel']}
PL0=PL; PL=lambda n: PL0(n)+['npc-'+x for x in SCP.get(n,[]) if 'npc-'+x in m.IMG]
for n in range(len(SC)): m.page(ACT[n],title(n),conv(scene(n)),images=PL(n),links=LK.get(n,[]))
m.page(A4,'Rewards, Endings & Continuity',conv(pick('Treasure & Rewards','Denouement','Continuity')),links=[m.IT(k) for k in ('rubbingofthesix','omentaper','ashbox','waterbreathing')])
m.page(AP,'Bestiary',conv(strip(body(BEST))),links=[m.N(k) for k in m.NPC])
m.page(AP,'Magic Items',''.join('<h>%s</h>'%m.ITEMN[k]+itemdesc(f) for k,f in (('gaolerslink',"The Gaoler's Link"),('ashbox','The Ashbox'),('bonetether','Bone Tether'),('omentaper','Omen-Taper of the Blind Spot'),('rubbingofthesix','Rubbing of the Six'))),images=['item-gaolers-link'],links=[m.IT(k) for k in m.ITEM])
for h in HAND:
    hn=re.sub(r'^.*?Handout — ','',os.path.basename(h)[:-3]); six='Six Sigils' in h
    hi=[HO[x] for x in sorted(HO) if x==hn or x.startswith(hn+' (')]; hi=[k for k in hi if k in m.IMG]
    m.page(AP,'Handout — '+hn,conv(strip(nocallout(body(h),('art',)))),images=hi,links=[m.I(k) for k in hi]+([m.I(k) for k in SIG] if six else []))
MAPS=[k for k in m.IMG if k.startswith('battlemap-')]
if MAPS: m.page(AP,'Maps','<p>Battlemaps for Scenes 01 and 05–08. The Landing (Scenes 01, 06 and 08): the long left pier is where the <i>Hecht</i> ties up (place a ship token or describe her); the long-tabled building at the bottom is the Fiend\'s Rest; the cranes and cart rail are harbor dressing. The <i>Hecht</i>: deck 1 (main deck, H1) is the Handover; deck 3 (lower deck and cabins, H2 and H3) is the Hold; decks 2 and 4 are spares. The cannons are set dressing from the source map: Oerth has no working gunpowder, so cover them with tokens or describe them as cargo. Calibrate the grid in Fantasy Grounds (5-ft. squares) before play.</p>',images=MAPS,links=[m.I(k) for k in MAPS])
# ---- build ----
OUT=os.path.join(ADV,'FGU Kit',NAME+'.mod')
m.build(os.path.join(WORK,CODE+'.mod'),cover_image='Cover')
shutil.copyfile(os.path.join(WORK,CODE+'.mod'),OUT)
if '--install' in sys.argv: shutil.copyfile(OUT,os.path.join(FG,'modules',NAME+'.mod')); print('installed to FG modules')
