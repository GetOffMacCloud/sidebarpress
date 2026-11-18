"""SP-GA01 The False Arrow -> Fantasy Grounds module. Run: python3 module.py [--install]
Uses the shared builder in 70-Company/Tools/fgu-module-builder (see the fgu-module-build skill)."""
import os,sys,re,glob,shutil
HERE=os.path.dirname(os.path.abspath(__file__)); ADV=os.path.dirname(os.path.dirname(HERE)); VAULT=ADV
while not os.path.isdir(os.path.join(VAULT,'70-Company')): VAULT=os.path.dirname(VAULT)  # works at any folder depth (In Development/, Completed/)
sys.path.insert(0,os.path.join(VAULT,'70-Company','Tools','fgu-module-builder'))
from fgmod import Mod, conv, body, sections
FG=os.environ.get('FG_DIR',os.path.expanduser('~/mnt/Fantasy Grounds'))
# ---- edition settings (a renamed edition changes only this block) ----
CODE='SP-GA01'; NAME='SP-GA01 The False Arrow'; DISPLAY='SP-GA01 — The False Arrow'
SRC=ADV; IMAGES=os.path.join(ADV,'images'); EXCLUDE_IMAGES=(); TEXT_MAP={}
FRAME='Greyhawk University'; PEOPLE='Chakyik'
# -----------------------------------------------------------------------
m=Mod(NAME,DISPLAY,'Sidebar Press','Sidebar Press',FG,os.path.expanduser('~/work/fgu/'+CODE),text_map=TEXT_MAP)
m.images(IMAGES,exclude=EXCLUDE_IMAGES,keep_original=('battlemap-duel-ring',))
P=lambda pat: glob.glob(os.path.join(SRC,pat))[0]
MAIN=P(CODE+'*-The-False-Arrow.md'); BEST=P('*Bestiary.md'); FAV=P('*The Favor Tracker.md'); SC=sorted(glob.glob(os.path.join(SRC,'Scenes','*Scene 0*.md')))
HAND=[P("*Handout — Brennin's Parley Letter.md"),P("*Handout — Halya's Sealed Instruction.md"),P("*Handout — Kezrin's Papers.md")]
strip=lambda s: re.sub(r'Back to \[\[[^\]]*\]\]','',s)
M=sections(body(MAIN)); pick=lambda *n: '\n'.join('## %s\n%s'%(x,M[x]) for x in n if x in M)
scene=lambda n: re.sub(r'^# .*\n','',body(SC[n]),count=1)
title=lambda n: re.sub(r'^.*?(Scene 0\d —)',r'\1',os.path.basename(SC[n])[:-3])
# ---- NPCs (SRD copies, renamed) ----
m.npc_srd('winterwolf','Winter Wolf','winterwolf',dress='It speaks Common first, reasonably: "One mule, and you pass." It is lying. It opens with Cold Breath on the mules if the party bargains.')
m.npc_srd('wolf','Wolf','wolf')
m.npc_srd('saber_toothedtiger','Saber-Toothed Tiger','sabertoothedtiger',dress='Winter-mad and starving; ribs showing. It fights to the death and goes for whoever looks smallest. 5-6 PCs: its mate comes out of the den on round 2.')
m.npc_srd('thug',"Kezrin's Man (Thug)",'kezrinsman',dress="Each carries one flask of lamp-oil (that's how the tent burns). They knock PCs out rather than kill, and flee the moment real resistance or Naran's riders appear. A captured thug names Kezrin on Intimidation DC 13.")
SCOUT="%s riders are mounted on steppe ponies (riding horse). The beaters in Scene 04 shoot from the ravine rim and never descend; one has trader's Common."%PEOPLE
m.npc_srd('scout','Batzorig (Scout)','batzorig',dress=SCOUT); m.npc_srd('scout','%s Beater (Scout)'%PEOPLE,'beater',dress=SCOUT)
m.npc_srd('berserker',"Temur's Champion (Berserker)",'temurschampion',dress='Duel rules: first to three hits, non-lethal (a hit that would drop a combatant to 0 leaves them at 1 and counts as a hit). Sarnai stops it. The champion always fights Reckless; the crowd expects it.')
m.npc_srd('spy','Master Kezrin (Spy)','kezrin',picture='npc-kezrin',dress='Kezrin never fights if he can run. In the council chase, his Cunning Action Dash is why the chase is three rounds, not one.')
m.npc_srd('warhorse','The Black Stallion (Warhorse)','blackstallion',dress="Seventeen hands, scarred muzzle, rope-burns ringing the neck. He won't carry a rider he doesn't respect. The player names him.")
m.npc_srd('ridinghorse','Steppe Pony (Riding Horse)','steppepony')
# ---- NPCs (homebrew) ----
MIN=('Minion','If the minion takes any damage, it drops to 0 hit points. If it succeeds on a saving throw against an effect that would deal half damage on a success, it takes no damage instead.')
m.npc('ochir','Ochir the Cut-Rein','Medium','humanoid (human)','neutral evil',15,'(studded leather)',52,'(8d8 + 16)','30 ft.',[12,16,14,11,12,14],'2',450,'passive Perception 13','Baklunish, Common, Ekbiri dialect',
  traits=[('Tent-City Born',"Ochir has advantage on Dexterity (Stealth) checks made in the Chakyik camp. Riders who don't know his face take him for one of their own.")],
  actions=[('Multiattack','Ochir makes two Scimitar attacks or two Horn Bow attacks.'),('Scimitar','Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage.'),('Horn Bow','Ranged Weapon Attack: +5 to hit, range 150/600 ft., one target. Hit: 7 (1d8 + 3) piercing damage.')],
  bonus=[("Cut-Rein's Order (Recharge 5-6)",'One ally within 30 ft. that can hear Ochir uses its reaction to move up to half its speed and make one weapon attack.')],
  skills='Animal Handling +3, Intimidation +4, Perception +3, Stealth +5',saves='Dex +5',token_from='batzorig',
  text="A Chakyik rider cast out of the horde, now Kezrin's man in the tent-city. The grinning-skull brand of Iuz is inside his left forearm (Religion DC 12). He shoots from the tent-line and spends his Order on whoever holds the ravine evidence. He knocks PCs out rather than kill them, and runs when Naran's riders arrive. Captured, he says nothing.")
for key,name,where in (('steppewolfminion','Steppe Wolf (Skirmisher Minion)','Scene 01, running with the winter wolf'),('ravinewolfminion','Ravine Wolf (Skirmisher Minion)',"Scene 04, starving wolves drawn by the tiger's kills")):
    m.npc(key,name,'Medium','beast','unaligned',13,'(natural armor)',1,'(minion)','50 ft.',[12,15,12,3,12,6],'3',175,'passive Perception 11','-',
      traits=[MIN,('Keen Hearing and Smell','The wolf has advantage on Wisdom (Perception) checks that rely on hearing or smell.'),('Pack Tactics (Skirmisher)',"The wolf has advantage on an attack roll against a creature if at least one of its allies is within 5 feet of the creature and the ally isn't incapacitated.")],
      actions=[('Bite','Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 piercing damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone.')],
      token_from='wolf',text='Optional minion pack (%s). Skirmisher Minion template, APL 3. Every four count as one creature for the encounter multiplier.'%where)
m.npc('kezrinsmanminion',"Kezrin's Man (Brute Minion)",'Medium','humanoid (human)','neutral evil',12,'(leather armor)',1,'(minion)','30 ft.',[15,11,14,10,10,11],'3',175,'passive Perception 10','Common',
  traits=[MIN,('Death-Blow (Brute)','When the minion drops to 0 hit points from a melee attack, it can make one attack against the attacker before it dies.')],
  actions=[('Club','Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 bludgeoning damage.')],token_from='kezrinsman',
  text="Optional minion pack (Scene 05). Brute Minion template, APL 3. They pull their blows (7 damage, not the template's 14): Kezrin wants the party scared off, not dead.")
# ---- encounters ----
m.battle('E1a','01 Steppe Predators (4 PCs)',[('winterwolf',1)]); m.battle('E1b','01 Steppe Predators (5-6 PCs)',[('winterwolf',1),('wolf',2)])
m.battle('E4a','04 The Saber-Tooth (4 PCs)',[('sabertoothedtiger',1)],'battlemap-ravine'); m.battle('E4b','04 The Saber-Tooth (5-6 PCs)',[('sabertoothedtiger',2)],'battlemap-ravine')
m.battle('E5a','05 The Night Visit (4 PCs)',[('ochir',1),('kezrinsman',2)],'battlemap-guest-camp'); m.battle('E5b','05 The Night Visit (5-6 PCs)',[('ochir',1),('kezrinsman',3)],'battlemap-guest-camp')
m.battle('E7a',"07 Champion's Duel",[('temurschampion',1)],'battlemap-duel-ring')
m.battle('M1','Optional - 01 Steppe Wolf minion pack',[('steppewolfminion',4)]); m.battle('M4','Optional - 04 Ravine Wolf minion pack',[('ravinewolfminion',4)],'battlemap-ravine')
m.battle('M5',"Optional - 05 Kezrin's Man minion pack",[('kezrinsmanminion',4)],'battlemap-guest-camp')
# ---- items ----
m.item('tigerclawtoken','Tiger-Claw Token','Wondrous Item',"<p><i>Wondrous item, uncommon (no attunement)</i></p><p>A large tiger claw on a braided leather cord, scrimshawed with tiny tiger-stripe marks. Ilkhan Cligir wears it on his wrist until he gives it away.</p><p><b>The Tiger's Mark.</b> While worn, the wearer has advantage on Charisma checks made to interact with Baklunish nomads.</p><p><b>At the Council.</b> The Round 1 Persuasion DC drops from 14 to 12.</p><p><b>Safe Passage.</b> Chakyik riders let the wearer and companions pass through their camps unharmed. The token loses this property if its holder breaks faith with the Chakyik.</p>",rarity='Uncommon',picture='item-tigers-mark')
m.item('hornbow','Horn Bow','Weapon','<p>A Chakyik composite bow of horn, sinew and wood. Use longbow statistics (1d8 piercing, range 150/600, heavy, two-handed). The horde lends horn bows for the Trial of the Bow; no proficiency is needed for the trial.</p>',subtype='Martial Ranged Weapons',damage='1d8 piercing',properties='Ammunition (range 150/600), heavy, two-handed',weight=2)
m.item('falsewolfarrows','The False Wolf Arrows','Adventuring Gear',"<p>Grey goose fletching, Wolf-style at a glance. Wolf Nomads bind fletching with sinew in a crisscross; these are glued, and the grey is paint over brown feather. With them: a black-steel arrowhead and, eventually, Tsolmon's arrow from Temur's sash. Climax evidence, not loot.</p>",picture='item-false-arrow')
# ---- reference manual ----
I1,A1,A2,A3,AP='Introduction','Act 1 — The Road','Act 2 — The Trials','Act 3 — The Council','Appendices'
COLOR=[k for k in M if k.endswith('Color')]+[k for k in M if k.startswith('Setting')]
m.page(I1,'Cover','<p><b>APL 3 (level 3) · 4–6 characters · one 3½-hour session</b></p><p>Part 1 of <i>The Plains of Blood and Steel</i>. A Sidebar Press adventure for the %s campaign frame.</p>'%FRAME,images=['Cover'])
m.page(I1,'Credits & How to Run','<p><b>The False Arrow</b> · %s · Sidebar Press. Premise after "Nomad\'s Land" by John Lent. Creature statblocks marked SRD are from the 5E SRD 5.1 (CC-BY-4.0).</p>'%CODE+conv(pick('Date','Campaign Frame','Design Frame','Hook','PC Objectives','Subplots (keyed to PCs; assign at the table)','Act Structure')))
m.page(I1,'Background',conv(pick(*COLOR,'What the Locals Know',"What's Really Happening",'Climax at a Glance')),images=['regional-map'])
m.page(I1,'Cast & Locations',conv(pick('Key NPCs','Key Locations')),images=['npc-cligir','npc-temur','npc-sarnai','npc-kezrin','npc-brennin','npc-halya','npc-naran'],links=[m.N('kezrin'),m.N('ochir'),m.N('batzorig'),m.N('temurschampion')])
m.page(I1,'Encounter Summary',conv(pick('Encounters')),links=[m.B(c) for c in m.BAT])
m.page(I1,'The Favor Tracker',conv(strip(body(FAV)).split('## At a Virtual Table')[0]))
m.page(A1,title(0),conv(scene(0)),images=['scene-ritterstadt','scene-job-board'])
m.page(A1,title(1),conv(scene(1)),images=['scene-hospice','scene-camp-panorama'],links=[m.B('E1a'),m.B('E1b'),m.B('M1'),m.N('winterwolf'),m.N('wolf')])
m.page(A1,title(2),conv(scene(2)),images=['scene-pavilion','map-winter-camp'],links=[m.N('batzorig')])
m.page(A2,title(3),conv(scene(3)),images=['scene-black-stallion'],links=[m.N('blackstallion')])
m.page(A2,title(4),conv(scene(4)),images=['scene-fog-ravine'],links=[m.B('E4a'),m.B('E4b'),m.B('M4'),m.N('sabertoothedtiger'),m.N('beater'),m.I('battlemap-ravine'),m.IT('hornbow'),m.IT('falsewolfarrows')])
m.page(A2,title(5),conv(scene(5)),images=['scene-night-attack'],links=[m.B('E5a'),m.B('E5b'),m.B('M5'),m.N('ochir'),m.N('kezrinsman'),m.N('kezrin'),m.I('battlemap-guest-camp')])
m.page(A2,title(6),conv(scene(6)),images=['scene-sarnais-fire'])
m.page(A3,title(7),conv(scene(7)),images=['scene-war-council'],links=[m.B('E7a'),m.N('temurschampion'),m.N('kezrin'),m.I('battlemap-duel-ring'),m.IT('tigerclawtoken')])
m.page(A3,'Rewards & Continuity',conv(pick('Treasure & Rewards','Continuity')),images=['item-tigers-mark'],links=[m.IT('tigerclawtoken'),m.N('blackstallion'),m.N('steppepony')])
m.page(AP,'Bestiary',conv(strip(body(BEST))),links=[m.N(k) for k in m.NPC])
for h,img in zip(HAND,(None,None,'item-kezrin-papers')):
    m.page(AP,re.sub(r'^.*?Handout — ','Handout — ',os.path.basename(h)[:-3]),conv(strip(body(h))),images=[img] if img else [])
m.page(AP,'Maps','<p>Painted battlemaps for Encounters 4, 5 and 7. The grid is not set: calibrate it in Fantasy Grounds (5-ft. squares) before play.</p>',images=['battlemap-ravine','battlemap-guest-camp','battlemap-duel-ring'],
  links=[m.I(k) for k in ('battlemap-ravine','battlemap-guest-camp','battlemap-duel-ring','map-winter-camp','regional-map') if k in m.IMG])
# ---- build ----
OUT=os.path.join(ADV,'FGU Kit',NAME+'.mod')
m.build(os.path.expanduser('~/work/fgu/%s.mod'%CODE),cover_image='Cover')
shutil.copyfile(os.path.expanduser('~/work/fgu/%s.mod'%CODE),OUT)
if '--install' in sys.argv: shutil.copyfile(OUT,os.path.join(FG,'modules',NAME+'.mod')); print('installed to FG modules')
