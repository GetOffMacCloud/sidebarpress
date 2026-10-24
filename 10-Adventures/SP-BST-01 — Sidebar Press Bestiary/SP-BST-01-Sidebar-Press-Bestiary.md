---
type: adventure
adventure: "SP-BST-01"
section: overview
publish_order: 5
publish: true
title: "Sidebar Press Bestiary"
status: draft # draft | playtesting | editing | published
levels: "1-10"
setting: Setting-agnostic
created: 2026-10-24
product_type: bestiary
tags: [bestiary, monsters, 2014-5e, homebrew]
---

# Sidebar Press Bestiary *(working title)*

**A setting-agnostic bestiary for 2014 5e: twenty-one creatures and one template, CR 0–20**

> Country horrors and threshold things: bargains that came due, households with standards, bridges that charge for crossing, and bells that ring for the wrong reasons. Every creature has a full statblock, lore, tactics, hooks, and spoils. Most of them can be outwitted as well as outfought.

## Series Code
`SP-BST-NN` is the bestiary line, kept apart from `SP-PBS` (Greyhawk) and `SP-HAL` (Halloween). `01` is this book. Codes are never reused.

## How This Product Is Built
- **Source of truth:** one note per creature in `65-Bestiary/`, made from [[90-Templates/Creature]]. Adventures link to these notes rather than copying statblocks.
- **Manifest and Longform index:** [[65-Bestiary/00 — Bestiary Index]]. The `longform: scenes:` list there must name every shipping note, in order.
- **Board:** [[SP-BST-01 — Board]].
- **Appendices** ([[90 — Creatures by Challenge]], [[91 — Creatures by Environment]]) are static tables generated from frontmatter, so they compile for print. Regenerate them after any CR or environment change.

## Contents
| Origin | Creatures |
|---|---|
| Harvested from SP-HAL-01 to 04 and SP-PBS-02 | [[Barrow Stag]], [[Bone Beast Template]], [[Bone Boar]], [[Bone Elk]], [[Bone Hound]], [[Drowned Guest]], [[Echo]], [[Harvest Lord]], [[Straw Double]], [[Threshold Lord]], [[Tithe-Reaper]], [[Toiling Haunt]], [[Wicker Colossus]] |
| New | [[Bell-Wight]], [[Hush-Moth Swarm]] |
| Remix | [[Ledger Hag]] (green hag), [[Toll-Troll]] (troll) |
| Contributed | [[Gluttonwretch|The Gluttonwretch]] (GrimmGrixis, retuned from CR 14 to CR 20) |
| Folklore | [[Church Grim]] (English), [[Kikimora]] (Slavic), [[Nuckelavee]] (Orcadian), [[Wolpertinger]] (Bavarian) |

## Decisions
- 2026-10-24: Setting-agnostic; 2014 5e; full entries; Obsidian notes plus this product folder. Named villains are entered as a generic type with the named individual as an example (Tithe-Reaper → Josiah Thorne; Threshold Lord → the Gentleman in Grey; Harvest Lord → Thornbury).
- 2026-10-24: Contributed creatures carry `origin: contributed` and a `credit:` field, credited under the title. The Gluttonwretch (GrimmGrixis) was retuned to CR 20 at Greybeard's direction; the working is in its Design Notes.
- 2026-10-24: Art uses one style spine for the whole book (see the Bestiary Index), with `--ar 3:4 --v 8.1 --style raw --seed 26500`.

## Open
- [ ] GrimmGrixis to review the Gluttonwretch's drafted lore, hooks, spoils, and the CR 20 retune.
- [ ] Confirm the contributor credit and terms for the Gluttonwretch before release.
- [ ] Choose the title, then rename this folder, this note, and the Longform `title`.
- [ ] Apply the Tithe-Reaper errata to SP-HAL-03 (Dex 18, 97 hp, Life Drain DC 14) and to the SP-HAL-04 wraith row (99 hp → 97). See the [[Tithe-Reaper]] Design Notes.
- [ ] Decide whether the adventure bestiaries should link to the 65-Bestiary entries.
