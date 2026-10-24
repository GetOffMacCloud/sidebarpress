---
type: scene-index
adventure: "SP-BST-01"
section: internal
publish_order: 0
publish: false
longform:
  format: scenes
  title: "Sidebar Press Bestiary"
  workflow: Default Workflow
  sceneFolder: /
  scenes:
    - 01 — Introduction
    - 02 — Reading an Entry
    - Barrow Stag
    - Bell-Wight
    - Bone Beast Template
    - Bone Boar
    - Bone Elk
    - Bone Hound
    - Church Grim
    - Drowned Guest
    - Echo
    - Harvest Lord
    - Hush-Moth Swarm
    - Kikimora
    - Ledger Hag
    - Nuckelavee
    - Straw Double
    - Threshold Lord
    - Tithe-Reaper
    - Toiling Haunt
    - Toll-Troll
    - Wicker Colossus
    - Wolpertinger
    - 90 — Creatures by Challenge
    - 91 — Creatures by Environment
  ignoredFiles:
    - 00 — Bestiary Index
---
# Bestiary Index — Sidebar Press Bestiary

Product: [[SP-BST-01-Sidebar-Press-Bestiary]] · Board: [[SP-BST-01 — Board]] · Template: [[90-Templates/Creature]]

> [!info] This note is the **build manifest** and the **Longform project index** for SP-BST-01. Every creature is one note in `65-Bestiary`, filed alphabetically by `publish_order` (gaps of 10). The bestiary is **setting-agnostic** and uses **2014 5e** rules, with MM page numbers from the 2014 *Monster Manual*. Adventures link here instead of copying statblocks. To add a creature, create it from [[90-Templates/Creature]], give it a free alphabetical slot, and add it to `longform: scenes:` above.

## Build Manifest

```dataview
TABLE WITHOUT ID
  file.link AS "File",
  section AS "Section",
  publish_order AS "Order",
  default(status, "—") AS "Status",
  choice(publish, "✅", "—") AS "Ships"
FROM "65-Bestiary" OR "10-Adventures/SP-BST-01 — Sidebar Press Bestiary"
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

Paste this into every creature prompt so the plates read as one book:

> *naturalist field-guide plate, a single creature studied in full on a plain warm parchment ground, oil on board, muted umber, bone, moss and slate palette, soft overcast light, eerie and restrained, folk-horror mood, no text*

- **Size:** `--ar 3:4` for a creature plate (half column, 900 × 1200). Use `--ar 1:3` only for a full-column chapter opener.
- **Seed:** `--seed 26500` for the whole book. Add `--sref` from the first approved plate once it exists.
- **Avoid:** heroic posing, glowing magic, gore, busy backgrounds, and modern faces.

## Entry Checklist (every creature)
- [ ] One-line read-aloud (≤25 words)
- [ ] Full 2014 statblock in a `[!example]+` callout; MM base cited where there is one
- [ ] Lore, Ecology, Tactics, three Adventure Hooks, and Spoils
- [ ] CR verification against DMG p. 274 written out in Design Notes
- [ ] Setting-agnostic: no Greyhawk proper names outside Named Example and Appears In
- [ ] Art prompt with the style spine and `--v 8.1`
- [ ] `status` moved through outline → drafted → edited → final
