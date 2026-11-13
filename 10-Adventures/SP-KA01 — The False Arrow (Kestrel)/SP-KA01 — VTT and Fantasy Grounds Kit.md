---
type: build-guide
adventure: "SP-KA01"
section: internal
publish_order: 0
publish: false
tags: [build, vtt, fantasy-grounds, SP-KA01]
---

# SP-KA01 — VTT and Fantasy Grounds Kit

Back to [[SP-KA01-The-False-Arrow]] · Maps: [[SP-GA01 — Map Assets]] · Statblocks: [[SP-KA01 — Bestiary]]

**Status:** not built (`fg_module` is empty). Kit folder: `10-Adventures/SP-KA01 — The False Arrow (Kestrel)/FGU Kit/` (create it when the first asset is made). Ruleset: **5E (2014)**. Grid: **100 px per square** on every map.

> [!warning] Kestrel build. Build it as its own module (`SP-KA01 The False Arrow (Kestrel)`), with Kestrel names on every record. Don't use `regional-map.png` or `Cover.png` until they are redone. The NPC portraits and battlemaps carry no names and can be shared with the Greyhawk build.

## Reference Modules (Fantasy Grounds)
- Creature records: **DD MM Monster Manual** (2014), loaded in the campaign.
- Homebrew records come from the Bestiary's *FGU Import* text: **NPCs → Import Text**, mode **2022 – Monsters of the Multiverse**.

## Maps
| Map | Encounter | Grid (squares) | FGU file at 100 px/sq | Copies |
|---|---|---|---|---|
| Ravine | E4 · Scene 04 | 36 × 16 | `Ravine - Simple Layout (FGU).png` · 3600 × 1600 | Player + DM |
| Night Camp | E5 · Scene 05 | 24 × 24 | `Night-Camp - Simple Layout (FGU).png` · 2400 × 2400 | Player + DM |
| Duel Ring | E7a · Scene 07 | 20 × 20 | `Duel-Ring - Simple Layout (FGU).png` · 2000 × 2000 | one |

- Source: the SVGs in `99-Assets/SP-GA01/`. Map Assets says the 100 px/sq PNGs are kept outside the vault; copy them into `FGU Kit/` (or re-export from the SVGs) so the kit is complete.
- The painted maps in `images/` (`battlemap-ravine.png` 2048 × 1536, `battlemap-guest-camp.png` 2048 × 2048, `battlemap-duel-ring.jpg` 1680 × 2380) **are not on those grids**. Their aspect ratios don't match the Simple Layouts. If you use them, set the grid by hand in FG and record the px/sq here.
- **Copies of the painted battlemaps are in the Greyhawk edition's `FGU Kit/` (they carry no names, so the Kestrel build can use them as they are):** `battlemap-ravine.png`, `battlemap-guest-camp.png` (Night Camp) and `battlemap-duel-ring.jpg` (a JPG; the original is one).
- `regional-map.png` and `map-winter-camp.png` go in as plain images (no grid), linked from the Overview and Scene 02 story entries.

## Story Entries (in index order)
| # | Entry | From |
|---|---|---|
| 01 | Credits & How to Run | Main note: cover line, Design Frame, Hook |
| 02 | The False Arrow — Overview | Main note: What the Locals Know, What's Really Happening, Climax at a Glance |
| 03 | The Favor Tracker | [[SP-KA01 — The Favor Tracker]] (link the tracker image) |
| 04 | Scene 00 — Kestrel University | [[SP-KA01 — Scene 00 — Kestrel University]] |
| 05 | Scene 01 — The High Pass | [[SP-KA01 — Scene 01 — The High Pass]] |
| 06 | Scene 02 — The Cold Welcome | [[SP-KA01 — Scene 02 — The Cold Welcome]] |
| 07 | Scene 03 — Trial of the Horse | [[SP-KA01 — Scene 03 — Trial of the Horse]] |
| 08 | Scene 04 — Trial of the Bow | [[SP-KA01 — Scene 04 — Trial of the Bow]] |
| 09 | Scene 05 — Night in Karash | [[SP-KA01 — Scene 05 — Night in Karash]] |
| 10 | Scene 06 — Trial of the Fire | [[SP-KA01 — Scene 06 — Trial of the Fire]] |
| 11 | Scene 07 — The War Council | [[SP-KA01 — Scene 07 — The War Council]] |
| 12 | Rewards & Continuity Ledger | Main note: Treasure & Rewards, Continuity Ledger |

Inside each entry: read-aloud in FG's boxed-text style, and links to that scene's NPCs, encounter, images and handouts, so the DM works from the story entry alone.

## Encounters (7 records)
| ID | Scene | 4 PCs | 5–6 PCs |
|---|---|---|---|
| E1a / E1b | 01 Steppe Predators | 1 winter wolf | 1 winter wolf + 2 wolves |
| E4a / E4b | 04 The Saber-Tooth | 1 saber-toothed tiger | 2 saber-toothed tigers (place the mate in the den; it joins on round 2) |
| E5a / E5b | 05 The Night Visit | Ochir + 2 thugs | Ochir + 3 thugs |
| E7a | 07 Champion's Duel | 1 berserker | same |

- Optional minion packs (Steppe Wolf, Ravine Wolf, Kezrin's Man) as three extra encounters of 4, kept out of the default list.
- The duel is "first to three hits, non-lethal": track hits by hand, and have the DM stop damage at 1 hp.

## NPC Records
| Record | Source block | Portrait |
|---|---|---|
| Winter Wolf · Wolf · Saber-Toothed Tiger | MM 2014 | — |
| Kezrin's Man (thug) · Batzorig, Beater (scout) · Temur's Champion (berserker) | MM 2014, renamed copies | — |
| Master Kezrin (spy) | MM 2014, renamed | `npc-kezrin.png` |
| The Black Stallion (warhorse) · Steppe Pony (riding horse) | MM 2014 | — |
| Ochir the Cut-Rein · 3 minions | Bestiary *FGU Import* | — |
| Story-only: Brennin, Halya, Sarnai, Temur, Naran, Sorvash | Personality page, no statblock | `npc-*.png` |

## Items
- **Tiger-Claw Token**: uncommon wondrous, no attunement. Advantage on Charisma checks made to interact with Karashi nomads; Round 1 DC 14 → 12. Image `item-tigers-mark.png`.
- **The False Wolf Arrows**: story item; image `item-false-arrow.png`.
- **Horn bow**: longbow copy (1d8 piercing, 150/600) for the Bow trial.

## Handouts
| Handout | Share with | When |
|---|---|---|
| 1 — Brennin's Parley Letter | everyone | Scene 01 (Sarnai reads it in 02) |
| 2 — Halya's Sealed Instruction | **one player** (Halya's pick) | Only when the seal is broken in Karash (Scene 05) |
| 3 — Kezrin's Papers (`item-kezrin-papers.png`) | everyone | Scene 07, if recovered |

## Favor Tracker
No FGU asset: a static image can't track anything. Keep the count on the printed table card, say it aloud every time it moves, and type it into chat so the log keeps a record. Story entry 03 links the rules.

## Build & Export
- [x] Battlemaps: use the Greyhawk edition's `FGU Kit/`
- [ ] Story entries 01–12 written
- [ ] 7 encounters built and placed on their maps
- [ ] NPC records created and linked (2014 sources; Ochir and minions imported)
- [ ] Items and handouts created; handouts flagged shareable
- [ ] Module exported: name `SP-KA01 The False Arrow (Kestrel)`, author Sidebar Press, versioned; `fg_module` set in the main note
