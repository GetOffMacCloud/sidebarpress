---
title: C12 - FG Map Count
module: C12 The Forgotten Library of Raanet (5e conversion)
tags: [c12, fgu, maps]
---

# C12 – Fantasy Grounds Map Count

The module ships **two maps** (PDF pp. 59–60). Both are black-and-white schematics at **1 square = 10 ft**. The other image-only pages (pp. 36, 38, 41) are appendix title pages. There is no stair map, pit map or wilderness map.

## Summary

| # | FG image record | Source | Footprint (10-ft sq) | Real size | Status |
|---|---|---|---|---|---|
| M1 | Temple Incandescent (DM) | p. 59 | ~44 × 53 | ~440 × 530 ft | **Required** |
| M1P | Temple Incandescent (Player) | p. 59, cleaned | ~44 × 53 | same | **Required** |
| M2 | The Burning Athenium | p. 60 | ~23 × 29 | ~230 × 290 ft | **Required** |
| M3 | The Oubliette, tactical (Area 9) | inset of M1 | 3 × 3 (6 × 6 at 5 ft) | 30 × 30 ft + 40-ft pit | Optional |
| — | The Slender Stairway (Area 1) | not mapped | — | — | No map. Narrative only |

**Total: 3 required image records, 1 optional.** There are 2 playable surfaces: the Temple level and the Athenium.

## Why the Temple needs two versions

The p. 59 map prints DM-only symbols on the map itself:

- **S**: secret doors at 8/9 (×2), 24→29 corridor, 25e
- **$**: markers at 25c, 25g, 25j and the 27 corridor

A FGU image shows everything a mask reveals, so revealing a room would also reveal its secret door. Build **M1** (keyed, all symbols) for the DM. Build **M1P** with the S and $ marks painted out (secret doors drawn as plain wall) and share that one. M2 has no secrets, so one version is enough.

## Map pins (story links)

| Map | Pins | Notes |
|---|---|---|
| M1 | 34 area pins (1–34) + 10 alcove pins (25a–25j) = **44** | Area 34 also holds the Summoning Sigil pedestal note |
| M2 | **1** (Area 35) | Add a second pin at the corridor mouth for the "Chapter Two" read-aloud |

## Grid and scale

The source grid is 10 ft. FG 5E automation (reach, range, AoE templates) assumes 5 ft squares, so there are two ways to run it:

1. **Rebuild at 5 ft (recommended).** Redraw or upscale so each 10-ft square becomes 2×2 cells.
   - M1 becomes ~88 × 106 cells. At **50 px/cell** that is ~4400 × 5300 px, which keeps it under FGU's practical 8192 px limit. At 70 px/cell it would be ~6160 × 7420 px, which is heavy but possible.
   - M2 becomes ~46 × 58 cells. At 70 px/cell that is ~3220 × 4060 px. At 100 px/cell it is ~4600 × 5800 px.
2. **Use the source as-is.** Set the FG grid to the printed squares:
   - M1 is ~39.1 px per square in the 300-dpi extract.
   - M2 is ~48.9 px per square in the 300-dpi extract.
   - Treat each square as 10 ft. Reach and AoE automation will be off by half, so rule those by eye.

Tactical pinch points that suffer at a 10-ft grid:

- **Area 9 (Oubliette).** The 10-ft shelf around a 10-ft pit is a single square ring. The wraiths force the fight to the pit edge, so the pit edge is where the fight happens. This is the reason for optional M3.
- **Area 3 (Welcome Hearth).** A 50-ft circle.
- **Areas 12, 15, 17, 22, 26, 29 and 34.** All are 30-ft circles.
- **Area 24.** The Dex-save corridor trap. Narrow corridors are 1 square wide.

## Content not drawn on either map

- **The corridor from Area 34 to Area 35.** The "newly-born corridor" opens in 34's south wall when the Sigil fires. Either add a short corridor strip to the top of M2, or use a hard scene cut.
- **Area 35's dais and coal bed.** These are described in the text but not drawn (the map shows only an open rectangle). Mark the raised dais and the sunken burning bed in the redraw. The heat aura and terrain in the conversion ledger key off them.
- **The Slender Stairway (Area 1).** It sits off-map above the 1 marker. No battle is expected there.

## Files

- `FGU Kit/Maps/C12 Source Map - M1 Temple Incandescent (10ft grid).png`: 300-dpi extract, 2074 × 2688 px
- `FGU Kit/Maps/C12 Source Map - M2 Burning Athenium (10ft grid).png`: 300-dpi extract, 2074 × 2688 px

Use these as tracing references or as a stopgap FG image. They are not cleaned player versions.
