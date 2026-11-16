import os,re,sys
V=sys.argv[1]; A=os.path.join(V,'10-Adventures','SP-OP01 — What the Dead Fear')
def edit(p,pairs):
    s=open(p).read()
    for a,b in pairs:
        if a not in s: print('MISSING in',os.path.basename(p),':',a[:60]); continue
        s=s.replace(a,b,1)
    open(p,'w').write(s)
GY=('''## Fight: The Graveyard Rising (Easy–Medium)
Ossian has staged a demonstration. As he raises his toast, the lychgate bells ring and the old graves in the yard heave open. Mindless **husks** (zombies) from decades-old burials lurch toward the chapel, with hulking **ogre zombies** in rotted burial linen behind them. Ossian grabs a lantern and "fights" beside the party, with wild swings that never land.

**Clue:** the husks walk past Ossian as if he weren't there (Perception DC 13, or automatic for anyone who watches him for a round). Afterward he's shaken and more grateful than ever: "You see? You *see* what I live with?"

| Code | PCs | Creatures | Adjusted XP | Difficulty |
|---|---|---|---|---|
| E1a | 4 | 6 zombies + 2 ogre zombies | 3,000 | Medium |
| E1b | 5 | 8 zombies + 2 ogre zombies | 3,250 | Easy |
| E1c | 6 | 10 zombies + 3 ogre zombies | 4,625 | Medium |

**Terrain:** The open graves are 6 ft. deep. A creature shoved into one takes 3 (1d6) bludgeoning damage and lands prone. Headstones give half cover.

''')
C1F=('''
> [!danger] Fight: Bone Gallery (Medium)
> **Ossuary crawlers** ([[Ossuary Crawler]]), drawn by the smell of the larder, cling to the 15-ft. ceiling among the skulls. Ossian tolerates them because they clean up. They drop on the party once the last character is inside. Their feeding tendrils paralyze (DC 13 Con), and a crawler drags a paralyzed victim 10 ft. toward the dark. The party may decide the slime trail is theirs. It isn't.
>
> | Code | PCs | Creatures | Adjusted XP | Difficulty |
> |---|---|---|---|---|
> | E2a | 4 | 4 ossuary crawlers | 3,600 | Medium |
> | E2b | 5 | 5 ossuary crawlers | 4,500 | Medium |
> | E2c | 6 | 6 ossuary crawlers | 5,400 | Medium |
''')
C2F=('''
> [!danger] Fight: The Kitchen (Easy)
> A salt pit fills the center of the room, 10 ft. square and 3 ft. deep (difficult terrain). Ossian's failures live in it: **gibbering mouthers** grown from aberrant scraps he couldn't digest. When anyone touches the hooks, the **cured hands** ([[Cured Hand]]) twitch free and scuttle, and the mouthers rise from the salt babbling in the voices of the dead. Arcana DC 13 afterward: mouthers form where aberrant flesh festers, so something in this place isn't human.
>
> | Code | PCs | Creatures | Adjusted XP | Difficulty |
> |---|---|---|---|---|
> | E3a | 4 | 2 gibbering mouthers + 6 cured hands | 2,400 | Easy |
> | E3b | 5 | 3 gibbering mouthers + 6 cured hands | 3,525 | Easy |
> | E3c | 6 | 3 gibbering mouthers + 10 cured hands | 3,625 | Easy |
''')
WH=('''## Wandering Husks
Roll a d6 whenever the party rests, dawdles for 30 minutes, or makes a racket below. On a 1–2, roll again on this table. These fights are attrition, not set pieces (trivial to Easy).

| d6 | Code | Encounter |
|---|---|---|
| 1–2 | W1 | 6 husks (zombies) shuffling along a corridor, all facing the same way: toward the ossuary |
| 3–4 | W2 | 1 ogre zombie in burial linen and 4 husks, carrying a salt barrel |
| 5 | W3 | 2 ossuary crawlers, feeding on a cured limb that fell off its hook |
| 6 | — | No fight. Ossian's voice speaks in every head at once: *"Hurry, friends. They're getting away."* |

''')
edit(os.path.join(A,'SP-OP01-What-the-Dead-Fear.md'),[
 ('estimated_hours: 3.5','estimated_hours: 4'),
 ('one 3–4 hour session**','one 4-hour session**'),
 ('Nothing in the catacombs attacks the party before the twist. If the players kill a ghoul, it dies pleading.',
  "The ghouls never attack the party. Everything that does is mindless or monstrous: Ossian's husks, his scavengers, his failures. If the players kill a ghoul, it dies pleading."),
 ('| [[Scene 01 — The Grateful Mortician]] | 45 min | The job, the advance, three or more clues that Ossian is wrong |',
  '| [[Scene 01 — The Grateful Mortician]] | 60 min | The job, the advance, three or more clues; the Graveyard Rising |'),
 ('| [[Scene 02 — The Catacombs]] | 45 min | The cured limbs, the ledger, Old Tam\'s warning, doors barred from the outside |',
  '| [[Scene 02 — The Catacombs]] | 75 min | Crawlers, the kitchen, the ledger, Old Tam\'s warning, doors barred from the outside |'),
 ('| E1a | 03 | 4 | Ossian (2 legendary actions) | 5,000 | Hard |\n| E1b | 03 | 5 | Ossian + 1 pallbearer (ogre zombie) | 8,175 | Hard (edge of Deadly) |\n| E1c | 03 | 6 | Ossian (3 legendary actions) + 2 pallbearers | 8,850 | Hard |',
  '| E1a–c | 01 | 4 / 5 / 6 | The Graveyard Rising: 6/8/10 zombies + 2/2/3 ogre zombies | 3,000 / 3,250 / 4,625 | Medium / Easy / Medium |\n| E2a–c | 02 (C1) | 4 / 5 / 6 | Bone Gallery: 4/5/6 ossuary crawlers | 3,600 / 4,500 / 5,400 | Medium |\n| E3a–c | 02 (C2) | 4 / 5 / 6 | The Kitchen: 2/3/3 gibbering mouthers + 6/6/10 cured hands | 2,400 / 3,525 / 3,625 | Easy |\n| E4a | 03 | 4 | Ossian (2 legendary actions) | 5,000 | Hard |\n| E4b | 03 | 5 | Ossian + 1 pallbearer (ogre zombie) | 8,175 | Hard (edge of Deadly) |\n| E4c | 03 | 6 | Ossian (3 legendary actions) + 2 pallbearers | 8,850 | Hard |\n| W1–3 | any | any | Wandering Husks (Scene 02 table) | 600–1,350 | trivial–Easy |'),
 ('Statblocks: [[SP-OP01 — Bestiary]].',
  'Statblocks: [[SP-OP01 — Bestiary]].\n\n**Adventuring day (4 PCs):** 3,000 + 3,600 + 2,400 + 5,000 = 14,000 XP, 70% of a 7th-level party\'s 20,000 budget. Allow one short rest after Scene 2 (and roll for Wandering Husks when they take it).'),
])
edit(os.path.join(A,'Scenes','Scene 01 — The Grateful Mortician.md'),[
 ('**Budget:** 45 minutes.','**Budget:** 60 minutes.'),
 ('## Alternates',GY+'## Alternates'),
])
edit(os.path.join(A,'Scenes','Scene 02 — The Catacombs.md'),[
 ('**Budget:** 45 minutes.','**Budget:** 75 minutes.'),
 ('**Nothing in this scene attacks the party.** Play the ghouls like frightened animals, not monsters.',
  "**The ghouls never attack the party.** Only Ossian's mindless and monstrous things do. Play the ghouls like frightened animals, not monsters."),
 ('Survival DC 13 identifies it as something big that climbs.',
  'Survival DC 13 identifies it as something big that climbs. On a 15 or higher, the trail is twice as wide as anything the party fights in here.'+C1F),
 ('someone is curing them. The ledger\'s first entry is *Ossian, brother. Tough.*',
  'someone is curing them. The ledger\'s first entry is *Ossian, brother. Tough.*'+C2F),
 ('## Clues',WH+'## Clues'),
])
edit(os.path.join(A,'SP-OP01 — Bestiary.md'),[
 ('| Pallbearers (1–2) | 2 | 450 | Ogre zombie, MM 316 | Scene 03 (5–6 PCs) |',
  '| Pallbearers (1–2) | 2 | 450 | Ogre zombie, MM 316 | Scene 03 (5–6 PCs) |\n| Husks | 1/4 | 50 | Zombie, MM 316 | Scenes 01–02 (graveyard, Wandering Husks) |\n| Ogre husks | 2 | 450 | Ogre zombie, MM 316 | Scene 01, Wandering Husks |\n| [[Ossuary Crawler]] | 2 | 450 | House creature | Scene 02 (C1), Wandering Husks |\n| Gibbering mouther | 2 | 450 | MM 157 | Scene 02 (C2) |\n| [[Cured Hand]] | 0 | 10 | House creature | Scene 02 (C2) |'),
 ('## Encounter XP check\n| Code | PCs |','## Encounter XP check\nThe graveyard (E1), crawlers (E2) and kitchen (E3) are in the scene notes with their adjusted XP. The boss fight:\n\n| Code | PCs |'),
 ('| E1a | 4 | Ossian |','| E4a | 4 | Ossian |'),('| E1b | 5 |','| E4b | 5 |'),('| E1c | 6 |','| E4c | 6 |'),
])
edit(os.path.join(A,'Scenes','00 — Scene Index.md'),[
 ("| 01 | [[Scene 01 — The Grateful Mortician]] | 45 min | 0:55 | Skip the register; describe the fingers outright | The job, the advance, three clues |",
  "| 01 | [[Scene 01 — The Grateful Mortician]] | 60 min | 1:10 | Skip the register; cut the graveyard to one ogre zombie and four husks | The job, the advance, three clues, the Graveyard Rising |"),
 ("| 02 | [[Scene 02 — The Catacombs]] | 45 min | 1:40 | C1 in one line; straight to Old Tam | The ledger, Tam's warning, the gouged doors |",
  "| 02 | [[Scene 02 — The Catacombs]] | 75 min | 2:25 | Skip the kitchen fight; no Wandering Husks rolls | Crawlers, the kitchen, the ledger, Tam's warning, the gouged doors |"),
 ("| — | *Break* | 10 min | 1:50 | — | — |","| — | *Break / short rest* | 10 min | 2:35 | — | — |"),
 ("| 03 | [[Scene 03 — What the Dead Fear]] | 60–90 min | 3:20 |","| 03 | [[Scene 03 — What the Dead Fear]] | 60–80 min | 3:55 |"),
])
edit(os.path.join(A,'SP-OP01 — Board.md'),[
 ('- [x] Encounter table with party-size bands and DMG difficulty math','- [x] Encounter table with party-size bands and DMG difficulty math (four fights + Wandering Husks, 2026-11-16)\n- [ ] Battlemaps for the graveyard, Bone Gallery and kitchen'),
])
print('done')
