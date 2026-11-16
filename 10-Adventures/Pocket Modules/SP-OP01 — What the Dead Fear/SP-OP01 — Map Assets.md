---
type: map-assets
adventure: "SP-OP01"
section: internal
publish_order: 0
publish: false
tags: [maps, battlemaps, vtt, production]
---

# SP-OP01 — Map Assets

Back to [[SP-OP01-What-the-Dead-Fear]] · Board: [[SP-OP01 — Board]]

Three battlemaps: the Saint's Ossuary (Scene 03), Merrow's Rest above ground (`map-graveyard.png`, E1) and the catacombs C1–C4 (`map-catacombs.png`, E2, E3 and W1–W3). The FGU build links them automatically. Layout references for CharGen are in `99-Assets/SP-OP01/_ref/`, drawn at 100 px per square with the grid origin top-left. Catacombs C1–C4 are narrated, not mapped; an optional printed DM key of the catacombs is listed below. Files go in `99-Assets/SP-OP01/`.

## Standards
- **Grid:** 1 square = 5 ft. True top-down (not isometric).
- **Exports:** **Player** (grid only), **DM** (grid + DM marks), **DM Overlay** (marks alone on transparency, same size).
- **Resolution:** 100 px/square for Fantasy Grounds; Roll20 copies at 70 px/square.
- **Format:** PNG, never JPG.
- **Tokens** live on the VTT, not baked into the map.
- **File names:** `SP-OP01 — The Saint's Ossuary — Player.png`, `— DM.png`, `— DM Overlay.png`.

## Status
| Map | Scene | Size (squares) | 100 px/sq | MJ base | Player | DM |
|---|---|---|---|---|---|---|
| The Saint's Ossuary | [[Scene 03 — What the Dead Fear]] | 16 × 18.4 (whole image) | 1600 × 1840 | CharGen ✅ | ✅ `map-saints-ossuary.png` (2026-11-16) | use the ink DM map |
| Merrow's Rest above ground: graveyard + roofless chapel (E1, early-unmasking fight) | [[Scene 01 — The Grateful Mortician]] | 32 × 21.3 at **72 px/sq** | 2304 × 1536 | CharGen ✅ | ✅ `map-graveyard.png` (2026-11-16) | use the graveyard DM map |
| The catacombs, C1–C4 (E2, E3, W1–W3, barred-doors fight) | [[Scene 02 — The Catacombs]] | 24 × 34 | 2400 × 3400 | CharGen ✅ | ✅ `map-catacombs.png` (2026-11-16) | use the ink site key |
| Saint's Ossuary — ink DM map (print) | [[Scene 03 — What the Dead Fear]] | 5-ft. grid | — | — | — | ✅ `map-saints-ossuary-dm.png` (2026-11-16) |
| Merrow's Rest graveyard — ink DM map (print) | [[Scene 01 — The Grateful Mortician]] | 5-ft. grid, matches the VTT map (32 × 21) | — | — | — | ✅ `map-graveyard-dm.png` (2026-11-16) |
| Merrow's Rest — ink site key (print) | [[Scene 02 — The Catacombs]] | 10-ft. grid | — | — | — | ✅ `map-merrows-rest-key.png` (2026-11-16) |

## The Saint's Ossuary: layout brief
Long axis north–south. Playable floor 40 × 60 ft. (8 × 12 squares) inside walls; the outer 2 squares on each side hold walls, shelves and alcoves.

| Feature | Placement | Rule (Scene 03) |
|---|---|---|
| **Iron doors** (double, 10 ft. wide) | Center of the south wall | Barred from inside after the trap; lifting the bar is an action, Athletics DC 15 |
| **Black water** | Whole floor, ankle-deep, glossy black | Dash, Disengage or shoved: DC 12 Dex save or prone |
| **Sarcophagi** (8) | Two rows of four, 10 ft. in from each long wall, 10 ft. apart; lids stood on end beside them, facing the doors (a "shield wall") | Half cover; full cover for Small behind a lid |
| **Bone shelves** | Floor-to-ceiling along both long walls, in 10-ft. sections (numbered 1–4 west, 5–8 east on the DM copy; 10-ft. sections broken by the alcoves) | Topple: 15-ft. line, DC 14 Dex, 3d10 bludgeoning, difficult terrain |
| **Drain channel** | 5 ft. wide, full length of the east wall, between the east sarcophagus row and the shelves; a grate at each end | 5 ft. deep; grappled prey is underwater |
| **Bone chute** | 5-ft. round shaft in the ceiling over the center of the vault, 25 ft. up; show as a dark circle with a dashed ring | Ossian's entrance and escape |
| **Chute alcove** | Ledge inside the chute, 20 ft. up (DM copy only) | Pallbearers wait here; the treasure ledge |
| **Altar and urn** | North end, raised one step, centered | The urn: 1d4 + 2 handfuls of ash |
| **Burial crawls** | 2-ft. openings low in the shelves: two on the west wall, one on the east, one behind the altar | Ghouls squeeze in as an action; nothing Large fits |
| **Deep alcoves** | Four 5 × 10 ft. alcoves cut into the long walls between shelf sections | Line-of-sight breaks; Ossian drags prey here |

**DM marks (DM copy):** larder undead start behind the north sarcophagi (H = Harrow, G1–G4); Ossian's drop point under the chute (O); pallbearers P1–P2 in the chute alcove; shelf section letters; slick-water reminder in the DM panel; the party's entry at the doors.

**Lighting:** none of its own. One guttering votive on the altar. Leave the floor readable: the black water should read as glossy dark stone with ripples, not as a void.

## Midjourney base prompt (VTT, color, screen only) — not needed, the CharGen render is done
**Don't render.** `map-saints-ossuary.png` already exists (CharGen); kept for reference only.
VTT battlemaps stay in their own style (Art Style Guide, out of scope for ink).

`top-down battlemap of an underground stone ossuary vault, rectangular hall with walls of stacked skulls and bones on floor-to-ceiling shelves, two rows of four open stone sarcophagi with their heavy lids standing on end, ankle-deep glossy black water covering the floor with faint ripples, a narrow drain channel with iron grates along the right wall, a raised stone altar with a single funerary urn and a guttering candle at the top, a round dark shaft in the ceiling seen as a black circle in the center, heavy iron double doors at the bottom edge, small dark crawl openings low in the bone walls, grim gothic catacomb, orthographic top-down view, flat even lighting, no perspective, no characters --ar 3:4 --v 8.1 --stylize 100 --no isometric, perspective, people, text, grid`

## Ink DM maps (done 2026-11-16)
Drawn as vector ink (pure black on white, hatched rock, keyed legend) rather than Midjourney, so the keys are exact. Sources: `99-Assets/SP-OP01/` PNGs; the SVG generator scripts live with the cloud session only. Orientation matches across both maps: the ossuary's altar is north, its iron doors south, and C4 wraps round to enter from the south. Crawls: two west stubs, one to C3 behind the altar, one to C3 from the east wall's south end. The Art Brief § 3 MJ prompt is now optional.

## VTT map notes (CharGen render, 2026-11-16)
- Made in CharGen from the layout reference in `99-Assets/SP-OP01/_ref/`. Grid: **100 px per square, origin top-left**; it lines up with no offset.
- Differences from the DM map: the lids stand on the **east** side of each sarcophagus, not the south (still half cover); the crawl behind the altar isn't drawn (three crawls shown); the alcoves have no bone shelves. None changes a rule.

## Catacombs render notes (CharGen, 2026-11-16)
- Came back 2400 × 3408; cropped 8 px of bare rock off the bottom to 2400 × 3400. Grid: 100 px per square, origin top-left, no offset.
- Differences: the skulls in C1 face outward, not into the wall (narrate the turned skulls); the last 2 × 2 squares of the C4 corridor are drawn as iron-plated floor under the barred doors. Neither changes a rule.

## Graveyard render notes (CharGen, 2026-11-16)
- CharGen returned a **landscape** 2304 × 1536 image, not the portrait layout, so the reference scale doesn't apply. **Grid: 72 px per square, origin top-left** (it lines up with the nave flagstones): 32 × 21.3 squares.
- At that grid: the nave is about 10 × 10 squares, the pews are 3 squares long with a 2-square aisle, and each grave plot is about 1 × 1.5 squares.
- Differences: six pews a side, not seven; the bone chute is an open hole in the apse floor, visible to players (added to the Scene 01 clue table, 2026-11-16); a gap in the top yard wall reads as a second way in. Eight open graves, as written.
