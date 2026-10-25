---
type: scene-index
adventure: SP-BST-01
section: internal
publish_order: 0
publish: false
longform:
  format: scenes
  title: "The Fell Harvest"
  workflow: Default Workflow
  sceneFolder: /
  scenes:
    - 01 — Introduction
    - 02 — Reading an Entry
    - Aetherwrack
    - Antlerwrack
    - Barrow Stag
    - Bell-Strung Corpse
    - Bell-Wight
    - Blight Wolf
    - Bloodfiend
    - Bone Beast Template
    - Bone Boar
    - Bone Elk
    - Bone Hound
    - Bone-Tally Chanter
    - Church Grim
    - Coffin-born
    - Coursehound
    - Demonic Spider
    - Drowned Guest
    - Echo
    - Fiendish Ogre
    - Gash-Marked Houndmaster
    - Gash-Marked Raider
    - Giant Hyena Witherling
    - Gnoll Warshaman
    - Goblin Battle-Drummer
    - Harvest Lord
    - Hawk Guardian
    - Hellborne
    - Hush-Moth Swarm
    - Iron-Marked Wolf
    - Jaguar Guardian
    - Kikimora
    - Kobold Blistercoil
    - Kobold Bulwark-Bearer
    - Kobold Dragonfang
    - Kobold Pot-Slinger
    - Kobold Pyrotechnic
    - Ledger Hag
    - Lesser Erinyes
    - Lieutenant of the Dark Prodigy
    - Marrow Hunter
    - Maulbone
    - Mnemophage
    - Nuckelavee
    - Pale Chimera
    - Root Guardian
    - Rot-Wargen
    - Stone Guardian
    - Straw Double
    - Threshold Lord
    - Tithe-Reaper
    - Toiling Haunt
    - Toll-Troll
    - Tunnel Scarhound
    - Viper Guardian
    - Wicker Colossus
    - Wolpertinger
    - 03 — Rogues' Gallery
    - Braknor Skullrend
    - Dorukai Thunderclub
    - Drevnar Soulreaver
    - The Endless Howl
    - Eylandra Stormchant
    - Glazryth, the Pale Terror
    - Gluttonwretch
    - Gorzak the Flaymaster
    - Grakh Unscarred
    - The Marrowmother
    - Mortenia's Echo, the Silent Sister
    - The Ninefold Voice
    - Saiyora's Echo, the Iron Sister
    - Sister Amarantha Wick, The Bell-Keeper
    - Sorrowbay, the Chained Sire
    - Sylvarith, the Venomous Wyrm
    - Tharazul, the Desert Storm
    - Velka's Echo, the Veiled Sister
    - Vespera Pixiecoil, the Prism-Coiled
    - Vyrathax, the Crimson Tyrant
    - Zarathryx, Champion of the Queen
    - Zhulkar Boneweaver
    - Zykryss, the Shadowed Doom
    - 90 — Creatures by Challenge
    - 91 — Creatures by Environment
  ignoredFiles:
    - 00 — Bestiary Index
---
# Bestiary Index — The Fell Harvest

Product: [[SP-BST-01-The-Fell-Harvest]] · Board: [[SP-BST-01 — Board]] · Template: [[90-Templates/Creature]]

> [!info] This note is the **build manifest** and the **Longform project index** for SP-BST-01. Every creature is one note in `65-Bestiary`, filed alphabetically by `publish_order` (gaps of 10). The bestiary is **setting-agnostic** and uses **2014 5e** rules, with MM page numbers from the 2014 *Monster Manual*. Adventures link here instead of copying statblocks. To add a creature, create it from [[90-Templates/Creature]], give it a free alphabetical slot, and add it to `longform: scenes:` above.

## Build Manifest

```dataview
TABLE WITHOUT ID
  file.link AS "File",
  section AS "Section",
  publish_order AS "Order",
  default(status, "—") AS "Status",
  choice(publish, "✅", "—") AS "Ships"
FROM "65-Bestiary" OR "10-Adventures/SP-BST-01 — The Fell Harvest"
WHERE adventure = "SP-BST-01" AND publish_order > 0
SORT publish_order ASC
```

## Creatures by Challenge

```dataview
TABLE WITHOUT ID
  file.link AS "Creature",
  cr AS "CR",
  xp AS "XP",
  size + " " + creature_type AS "Type",
  join(environment, ", ") AS "Environment",
  origin AS "Origin"
FROM "65-Bestiary"
WHERE type = "creature"
SORT cr_num ASC, creature ASC
```

## By Origin

```dataview
TABLE WITHOUT ID
  origin AS "Origin",
  length(rows) AS "Count",
  rows.file.link AS "Creatures"
FROM "65-Bestiary"
WHERE type = "creature"
GROUP BY origin
```

## Harvested From Adventures

```dataview
TABLE WITHOUT ID
  file.link AS "Creature",
  base_block AS "Base block",
  join(source_adventures, ", ") AS "Source"
FROM "65-Bestiary"
WHERE type = "creature" AND origin = "harvested"
SORT creature ASC
```

## Art Style Spine

**House style:** classic black-and-white pen-and-ink (see [[Art-Style-Guide]]). Every creature plate is a spot illustration: one creature on bare white, with a small solid black cast shadow. Each note's Art Prompt already ends with the PLATE spine:

> *classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm*

- **Tail:** `--ar 3:4 --v 8.1 --style raw --stylize 75 --seed 26500 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark`. Add `--sref` from our first approved plate once it's locked.
- **Print:** convert to 1-bit black and white at 600 dpi before placing.
- Production tracking lives in [[SP-BST-01 — Art Brief]].

## Entry Checklist (every creature)
- [ ] One-line read-aloud (≤25 words)
- [ ] Full 2014 statblock in a `[!example]+` callout; MM base cited where there is one
- [ ] Lore, Ecology, Tactics, three Adventure Hooks, and Spoils
- [ ] CR verification against DMG p. 274 written out in Design Notes
- [ ] Setting-agnostic: no Greyhawk proper names outside Named Example and Appears In
- [ ] Art prompt with the style spine and `--v 8.1`
- [ ] FGU Import section generated with `70-Company/Tools/fgu_import.py` (re-run after any statblock change)
- [ ] `status` moved through outline → drafted → edited → final
