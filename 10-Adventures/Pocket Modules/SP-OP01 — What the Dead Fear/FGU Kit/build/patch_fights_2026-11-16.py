import os,sys,glob,re
V=sys.argv[1]; A=os.path.join(V,'10-Adventures','Pocket Modules','SP-OP01 — What the Dead Fear')
def rd(p): return open(p).read()
def wr(p,s): os.makedirs(os.path.dirname(p),exist_ok=True); open(p,'w').write(s)
def edit(p,pairs):
    s=rd(p)
    for a,b in pairs:
        if a not in s: print('MISSING',os.path.basename(p),':',a[:60]); continue
        s=s.replace(a,b,1)
    wr(p,s)
# 1. rename everywhere
files=glob.glob(os.path.join(A,'**','*.md'),recursive=True)+[os.path.join(A,'FGU Kit','build','module.py')]
files+=[os.path.join(V,'30-NPCs','Brother Ossian.md'),os.path.join(V,'40-Locations',"Merrow's Rest.md"),os.path.join(V,'50-Items','The Urn of Saint Merrow.md')]
files+=glob.glob(os.path.join(V,'65-Bestiary','SP-OP01','*.md'))
for p in files:
    s=rd(p); t=s
    for a,b in (('an avolakia','a drunaghul'),('An avolakia','A drunaghul'),('Avolakias','Drunaghuls'),('avolakias','drunaghuls'),('Avolakia','Drunaghul'),('avolakia','drunaghul')): t=t.replace(a,b)
    if t!=s: wr(p,t); print('renamed',os.path.basename(p))
# 2. canon notes
M=os.path.join(A,'SP-OP01-What-the-Dead-Fear.md'); s=rd(M)
s=s[:s.index('## Canon Notes')]+'''## Canon Notes
The drunaghul is an original Sidebar Press creature (named 2026-11-16). Its roots are real-world folklore: the Arabian ghul (graveyards, shapeshifting, taking the form of the last person eaten; possibly from the Akkadian gallu), the Avestan Druj Nasu ("the lie that is corpse"; dogs drive it off), the Philippine aswang and bal-bal (corpse thieves at wakes, the long tongue), and the Norse Níðhöggr on Náströnd (the worm that sucks corpses). Setting-agnostic; safe for sold editions.
'''
# 3. new sections in the main note
add_hooks='''
> **Drop it in.** Merrow's Rest belongs to no setting. Put it wherever a road needs a place to bury its dead: a crossroads chapel on a pilgrim or trade road, the mortuary chapel of a remote abbey, the paupers' field outside a city wall, a cemetery on an old battlefield, or the chapel of a mining town, where the crawls meet the old workings. Saint Merrow can be any patron of the dead in your setting, and the urn's ash works the same either way.

## Rumors (d6)
| d6 | Rumor | True? |
|---|---|---|
| 1 | "Brother Ossian hasn't slept since spring. His candle's always lit." | True |
| 2 | "Grave robbers stole the saint's urn, and that's why the dead walk." | False: it's Ossian's story |
| 3 | "Tam the cooper was buried in spring. His widow swears he knocked on her door." | True |
| 4 | "There's something under the chapel older than the chapel." | True: the crawls |
| 5 | "Ossian pays in old coin. Some say it's grave money." | True |
| 6 | "The yard dog bit Brother Ossian once. Next morning the dog was fine, and the brother hadn't a mark on him." | True |

## Merrow's Rest
Full write-up (history of the place, the building and its denizens): [[Merrow's Rest]].

## Brother Ossian
Full write-up (the man, the thing wearing him, manner, wants, lines): [[Brother Ossian]].
'''
i=s.index('## Adventure Outline'); s=s[:i]+add_hooks.lstrip('\n')+'\n'+s[i:]
s=s.replace('a *cloak of protection*, a *periapt of wound closure*, and 2 *potions of greater healing*.','a *cloak of protection*, a *periapt of wound closure*, 2 *potions of greater healing*, and a *spell scroll of* [[Gravecure|gravecure]].')
add_end='''
## Running It at Other Levels
| | APL 5 (levels 4–6) | APL 9 (levels 8–10) |
|---|---|---|
| **Ossian** | 115 hp, AC 15, 1 legendary action. Drop *dominate person* and open with *hold person*. Bite necrotic 3d6. | 190 hp, AC 17, 3 legendary actions. Bite necrotic 5d6. Feed heals 20 (35 for Harrow). |
| **Graveyard** | One fewer ogre zombie | Two more ogre zombies |
| **Bone Gallery** | One fewer crawler | Two more crawlers |
| **The Kitchen** | 2 mouthers + 4 cured hands | One more mouther |
| **Pallbearers** | None | One more |
| **Wandering Husks** | Use the 4-PC numbers, one creature fewer | Use the 6-PC numbers |

Recheck each fight against the DMG thresholds for your party; these are starting points.

## Stream Twists (d6)
For streamed games: once per scene, let chat vote on or roll one of these.

| d6 | Twist |
|---|---|
| 1 | **Lights out.** Every candle and torch gutters out at once. Darkness for 1 minute. |
| 2 | **The register writes itself.** A new line appears in the neat hand: a PC's name, and *taken below for rest*. |
| 3 | **Pell follows.** Pell Brisk has trailed the party down, looking for his mother. Now he's in danger. |
| 4 | **A ghoul knows you.** A larder ghoul whispers a PC's secret. Ossian's telepathy leaks into the things he eats. |
| 5 | **The bells ring.** Roll on the Wandering Husks table right now. |
| 6 | **Mercy.** Harrow appears early, once, and warns a PC: "When the doors close, go for the hole in the ceiling." |

## Sequel Seed: The Face on the Road
Even if Ossian dies, Harrow knows one more thing: "He came up the crawls. He said the others are still down there, waiting for the yards to fill." The walled-off crawls under the ossuary lead deeper. If Ossian escaped, a new chapel two roads over has a new keeper who is very grateful for help.

## Handouts
- [[SP-OP01 — Handout — The Notice]] (the hook)
- [[SP-OP01 — Handout — The Burial Register]] (Scene 01)
- [[SP-OP01 — Handout — The Larder Ledger]] (Scene 02, C2)

## Spell
- [[Gravecure]] (3rd-level necromancy)
'''
i=s.index('## Key NPCs'); s=s[:i]+add_end.lstrip('\n')+'\n'+s[i:]
wr(M,s)
# 4. FGU import: gravecure; NPC canon note; NPC write-up
N=os.path.join(V,'30-NPCs','Brother Ossian.md'); s=rd(N)
s=s.replace('1/day each: animate dead, dominate person','1/day each: animate dead, gravecure, dominate person')
s=re.sub(r'## Canon Notes\n.*?\n\n','## Canon Notes\nAn original Sidebar Press creature: the drunaghul (named 2026-11-16). See the adventure\'s Canon Notes for its folklore roots.\n\n',s,flags=re.S)
s=s.replace('## Appearance','## The Man\nThe real Brother Ossian kept Merrow\'s Rest for forty years: a stubborn, patient man with arthritic hands. He is the first entry in the larder ledger: *Ossian, brother. Tough.* A drunaghul came up the crawls eight months ago, ate him, and took his face. It runs Merrow\'s Rest better than he did, and everyone says how well he looks.\n\n## Appearance',1)
s=s.replace('- Toasts "the brave and the quiet dead."','- Toasts "the brave and the quiet dead."\n- Lines: "Thank you. Thank you for coming." "They\'d hidden so well."')
s=s.replace('- **Wants:** his larder back out of the crawls, and the party for dessert.','- **Wants:** his larder back out of the crawls, the urn carried out of his ossuary (he can\'t bear to touch it), and the party for afters.')
s=s.replace('the urn','the urn',1)
wr(N,s)
# 5. location history
L=os.path.join(V,'40-Locations',"Merrow's Rest.md"); s=rd(L)
hist='''## History
*Setting-agnostic: the only history here is the place's own.*
- **The founding.** About a hundred years ago, a gravedigger named Merrow buried the road's dead for nothing, and buried them well. When she died, the people she had served raised a chapel over her grave and kept her ashes in a plain grey urn. The locals call her Saint Merrow, patron of the quiet dead (swap in any patron of the dead in your setting).
- **The catacombs.** A plague winter filled the yard twice over, so the brothers dug down. Below the chapel they broke into burial crawls older than anything they had built: two-foot tunnels running down into the deep earth. They walled off the deepest, raised the Saint's Ossuary around the rest, and carried the urn below to keep watch. They cut a bone drop from the apse to the ossuary to lower old remains, and no one has used it since the plague.
- **The last forty years.** Brother Ossian kept Merrow's Rest with only Sexton Harrow, who dug the graves. They were quiet years: a funeral a month, the register in Ossian's cramped, shaking hand, and Harrow's dog asleep under the yews.
- **Eight months ago.** Something came up the old crawls. The register's handwriting changed that spring to a neat, steady hand, and there have been more burials than deaths ever since.
'''
s=re.sub(r'## History\n.*?\n(?=## )',hist+'\n',s,flags=re.S)
s=s.replace("- [[Sexton Harrow]] and the larder ghouls (the Widow Brisk, the Collier twins, Old Tam)",
 "- [[Sexton Harrow]], now a wight, who keeps his memory and his shame\n- The larder: the Widow Brisk, Tam the cooper, and Wil and Ned Collier, all buried this spring and all ghouls now\n- Ossian's things: husks raised from old graves, ossuary crawlers that clean up after him, gibbering mouthers he couldn't digest\n- Pell Brisk, the widow's son, who lives a mile up the road and won't come past the lychgate\n- The chapel cat and Harrow's dog, who know exactly what Ossian is")
s=s.replace('- **Nave and vestry.** The burial register is in the vestry. The bone chute opens behind the altar.','- **Nave and vestry.** The burial register is in the vestry. The bone drop (the bone chute) opens in the apse floor beside the trapdoor.')
wr(L,s)
# 6. spell note
wr(os.path.join(A,'Spells','Gravecure.md'),'''---
type: spell
adventure: "SP-OP01"
section: appendix-mechanics
publish: true
title: "Gravecure"
level: 3
school: "necromancy"
ritual: false
tags: [spell, homebrew, sp-op01, necromancy]
---

# Gravecure

*3rd-level necromancy*

- **Casting Time:** 1 action
- **Range:** 60 feet
- **Components:** V, S, M (a pinch of grave salt)
- **Duration:** Concentration, up to 1 minute
- **Classes:** cleric, warlock, wizard *(Sidebar Press homebrew, OP1)*

You speak the old curing words over the dead. Each undead of your choice in a 20-foot-radius sphere centered on a point you can see within range must succeed on a Wisdom saving throw or be cured for the duration. A cured undead is incapacitated, its speed is 0, and it can't take reactions. It repeats the saving throw at the end of each of its turns and whenever it takes damage, ending the effect on itself on a success. An undead of CR 6 or higher has advantage on the saving throw.

***At Higher Levels.*** When you cast this spell using a spell slot of 4th level or higher, the radius increases by 10 feet for each slot level above 3rd.

## Notes for the DM
Ossian casts it once a day to turn armed ghouls back into food, since a cured undead is incapacitated and he can Feed on it. A spell scroll of *gravecure* waits on the chute ledge. Comparable to a 3rd-level crowd-control spell, but it only touches undead.
''')
# 7. handouts
H=[('The Notice','1','the hook','''RESTLESS DEAD AT MERROW'S REST

The quiet dead are quiet no longer. Brave souls are sought to clear the catacombs beneath the chapel and recover the sacred Urn of Saint Merrow, carried below by the unquiet.

600 gold, half paid in advance.

Ask for Brother Ossian at the lychgate.

With gratitude,
Br. O.'''),
('The Burial Register','2','Scene 01 (the vestry)','''*The old entries are in a cramped, shaking hand. Every entry since spring is in a neat, steady one.*

Agnes Brisk, widow, 71 years. Fever. Taken below for rest.
Tam, cooper, 58 years. Fell from his roof. Taken below for rest.
Wil and Ned Collier, brothers, 24 years. Taken by the mine. Taken below for rest.
A traveler, name unknown. Found on the road. Taken below for rest.
Harrow, sexton, 63 years. Taken below for rest.'''),
('The Larder Ledger','3','Scene 02 (C2, the Embalming Room)','''*In the same neat hand as the register.*

Ossian, brother. Tough. Stock for the broth.
Harrow, sexton. Raised first. Clever. Watch him.
Brisk, widow. Raised Planting 2nd. Tender by Harvest.
Tam, cooper. Raised Planting 9th. Lean; salt longer.
Collier twins. Raised Planting 20th. Hang apart; they whisper.
Guests expected. Something warm for afters.''')]
for t,n,where,body in H:
    wr(os.path.join(A,'SP-OP01 — Handout — %s.md'%t),'''---
type: handout
adventure: "SP-OP01"
section: appendix-handouts
publish: true
title: "Handout %s: %s"
tags: [handout, sp-op01]
---

# Handout %s: %s

*Give to players at: %s. Build in Canva: real text over a parchment or ledger background; export PNG for FGU, PDF for print.*

```text
%s
```
'''%(n,t,n,t,where,body))
# 8. handout cues in scenes
edit(os.path.join(A,'Scenes','Scene 01 — The Grateful Mortician.md'),[('| In the burial register, every burial since spring is marked "taken below for rest."','| In the burial register ([[SP-OP01 — Handout — The Burial Register|Handout 2]]), every burial since spring is marked "taken below for rest."')])
edit(os.path.join(A,'Scenes','Scene 02 — The Catacombs.md'),[('A ledger in a neat hand reads:','A ledger in a neat hand ([[SP-OP01 — Handout — The Larder Ledger|Handout 3]]) reads:')])
print('done')
