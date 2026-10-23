---
type: map-assets
adventure: "SP-PBS-00"
section: internal
publish_order: 0
publish: false
tags: [maps, battlemaps, vtt, production]
---

# SP-PBS-00 — Map Assets

Back to [[SP-PBS-00-Nobodys-Colors]] · Board: [[SP-PBS-00 — Board]]

One battlemap per encounter. The three sites are non-contiguous, so there is no connected map. Files go in `99-Assets/SP-PBS-00/`.

## Standards
- **Grid:** 1 square = 5 ft.
- **Two exports per map:** **Player** (DM Only layer hidden, grid on) and **DM** (everything visible). Start positions, difficult terrain and the clock notes live on the DM copy only.
- **Resolution:** **100 px/square** for Fantasy Grounds and Foundry (the draft's FGU Kit standard). Roll20 copies at 70 px/square. Print at 300 px/square only for the deck (the other two exceed Inkarnate Pro's 8K cap; print those at 200 or tile them).
- **Format:** PNG, never JPG (JPG artifacts the grid lines).
- **Inkarnate build:** pick a Battlemap style at creation; paint floors on Foreground; walls are Mask Tool cut-outs of the floor with stamps on top; all stamps on the default object layer plus one object layer named **DM Only**. Use the search box for stamps; category names shift.
- **Tokens** live on the VTT, not baked into the map.
- **File names:** `SP-PBS-00 — [Map] — Player.png`, `SP-PBS-00 — [Map] — DM.png`.

## Status
| Map | Scene | Size (squares) | 100 px/sq | Player | DM |
|---|---|---|---|---|---|
| The Erlen Bridge | [[Scene 02 — The Erlen Bridge]] | 40 × 24 | 4000 × 2400 | ⬜ | ⬜ |
| The *Kortheim Maid* | [[Scene 04 — Two Nights on the Quag]] | 20 × 12 | 2000 × 1200 | ⬜ | ⬜ |
| The Stable Rows | [[Scene 06 — The Stable Rows]] | 40 × 14 | 4000 × 1400 | ⬜ | ⬜ |

## 1 — The Erlen Bridge
**40 × 24 squares · 200 × 120 ft · 4000 × 2400 px**
- A stone toll bridge **3 squares wide** across a **4-square river** in the middle third of the map; the road runs the long axis.
- Waist-high stone walls on both sides of the span (half cover; a shove over is 1d6 falling and a wet drover).
- **Toll house** at the near end, 4 × 4, half cover; [[Old Hartwin]] inside.
- **Cattle** strung along the eastern half of the road.
- **Drover camp** off the verge: a fire, two carts, bedrolls.
- **DM Only:** Boedic and the drovers in a line across the span; mastiff starts at the carts (APL 3–4); the cattle squares marked as difficult terrain *only when spooked*; the note "loud noise = DC 11 Dexterity save or prone; difficult terrain 2 rounds."
- **Custom stamps likely:** bridge sections, a drover's cart.

## 2 — The *Kortheim Maid*
**20 × 12 squares · 100 × 60 ft · 2000 × 1200 px**
- A lake cog **12 squares stem to stern, 4 in the beam**, centered, with water all round.
- Single mast amidships; hatch cover forward; tiller and the single stern lantern aft.
- **The deck stall** against the starboard rail amidships, 2 × 2, canvas roof. This is the whole point of the map.
- Passenger bedrolls forward, crew aft.
- **DM Only:** the 20-ft light radius from the stern lantern (darkness beyond); Krul's start at the mast; deckhand starts aft (APL 2–4); the note "Dash, shove or reaction = Acrobatics DC 10 or prone; over the rail = Athletics DC 12."
- **Lighting matters more than terrain.** With dynamic lighting, make the stern lantern the only light source and give Krul vision as if adjusted to the dark; the party's disadvantage in the dark is the encounter.
- **Custom stamps likely:** a canvas-roofed deck stall.

## 3 — The Stable Rows
**40 × 14 squares · 200 × 70 ft · 4000 × 1400 px**
- A long gallery under one roof running the full 40 squares.
- **Stalls 2 × 2, twenty a side**, opening onto a **3-square central aisle** (a wagon wide).
- A **lantern every 4 squares** (20 ft), each marked: light sources and weapons both.
- **Pitchfork rack, water trough and buckets** at the near post; a lantern-pole at every third stall.
- **Maus's stall:** the fourteenth on the left, about two-thirds down, past the Roodberg strings.
- **DM Only:** bravo starts at the far end; Krul (if free) by the far door; lantern light radii; Spook die triggers keyed to features (lanterns, stall doors, the trough).
- **Grid note:** 40 × 14 letterboxes badly on a shared screen. Consider two 20 × 14 halves, split at stall 10.
- **Custom stamps likely:** a pitchfork rack and water butt, hanging stable lanterns.

## Custom Stamp Formula
From [[SP-PBS-00 — Art Brief]] (module seed and `--v 8.1`):
```
top-down orthographic view of [subject], [details], fourteenth-century Alpine battlemap prop, isolated on plain flat white background, no cast shadow, even lighting, highly detailed --ar 1:1 --v 8.1 --stylize 200 --seed 20008
```
Use a **black** background for anything that glows (lanterns), so the light survives the cutout. Remove the background to a transparent PNG before uploading as a Custom Stamp.

## FGU Notes
The A Tourist In Greyhawk draft (`0008 - Nobody's Colours/FGU Kit/`) lists NPC records, the Sabotage Clock and Spook die trackers, and the Maus condition marker as built in FGU. Its tracker PNGs are not in that folder yet. When they are, copy them to `99-Assets/SP-PBS-00/`.
