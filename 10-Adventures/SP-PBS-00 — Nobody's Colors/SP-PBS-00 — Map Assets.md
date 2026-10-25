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
| Map | Scene | Size (squares) | 100 px/sq | MJ base | Player | DM |
|---|---|---|---|---|---|---|
| The Erlen Bridge | [[Scene 02 — The Erlen Bridge]] | 40 × 24 | 4000 × 2400 | ✅ | ⬜ | ⬜ |
| The *Kortheim Maid* | [[Scene 04 — Two Nights on the Quag]] | 20 × 12 | 2000 × 1200 | ✅ | ⬜ | ⬜ |
| The Stable Rows | [[Scene 06 — The Stable Rows]] | 40 × 14 | 4000 × 1400 | ✅ | ⬜ | ⬜ |

Midjourney bases (2026-10-25) are in `99-Assets/SP-PBS-00/` as `SP-PBS-00 — [Map] — MJ base.png`; prompts in [[SP-PBS-00 — Art Brief]] § 7. Next step for each: grid, cleanup and the DM Only layer in Inkarnate, then the two exports.

## 1 — The Erlen Bridge
**40 × 24 squares · 200 × 120 ft · 4000 × 2400 px**
- A stone toll bridge **3 squares wide** across a **4-square river** in the middle third of the map; the road runs the long axis.
- Waist-high stone walls on both sides of the span (half cover; a shove over is 1d6 falling and a wet drover).
- **Toll house** at the near end, 4 × 4, half cover; [[Old Hartwin]] inside.
- **Cattle** strung along the eastern half of the road.
- **Drover camp** off the verge: a fire, two carts, bedrolls.
- **DM Only:** Boedic and the drovers in a line across the span; mastiff starts at the carts (APL 3–4); the cattle squares marked as difficult terrain *only when spooked*; the note "loud noise = DC 11 Dexterity save or prone; difficult terrain 2 rounds."
- **Custom stamps likely:** bridge sections, a drover's cart.
- **As rendered (MJ base):** the river runs north–south through the middle and the road east–west across the bridge. The toll house is at the west end; cattle graze in the northwest; the drover camp (fire, two covered carts) is northeast of the bridge. Matches the spec. **Cleanup:** the toll house is still drawn slightly angled; flatten its roof or replace it with a top-down stamp.

## 2 — The *Kortheim Maid*
**20 × 12 squares · 100 × 60 ft · 2000 × 1200 px**
- A lake cog **12 squares stem to stern, 4 in the beam**, centered, with water all round.
- Single mast amidships; hatch cover aft; tiller at the stern (left on the render).
- **The deck stall** at the **bow** (right on the render), against the starboard rail, 2 × 2, canvas roof. This is the whole point of the map. *(Changed 2026-10-25 to match the render.)*
- **The lantern** hangs from the stay just aft of the stall: the only light on deck.
- Coiled rope, sacks and casks along both rails; passengers bed down aft.
- **DM Only:** Krul's start in the stall; deckhand starts by the mast (APL 2–4); the lantern's light radius; the note "Dash, shove or reaction = Acrobatics DC 10 or prone; over the rail = Athletics DC 12."
- **Lighting matters more than terrain.** Krul shutters the lantern to a slit before he starts (dim light within 10 ft, darkness beyond). Unshuttering it is an action (a bonus action for a PC adjacent to it) and lights 20 ft, which ends his advantage in the dark. With dynamic lighting, set the lantern as the only source and start it shuttered.
- **Cleanup:** the mast is drawn lying along the deck; paint it back to a single post seen from above, and darken the water, which reads a little like stone.
- **Custom stamps likely:** a canvas-roofed deck stall.

## 3 — The Stable Rows
**40 × 14 squares · 200 × 70 ft · 4000 × 1400 px**
- A long gallery under one roof running the full 40 squares.
- **Stalls 2 × 2, about fifteen a side as rendered** (horses in the north row, the south row mostly empty), opening onto a **3-square central aisle** (a wagon wide). *(Changed 2026-10-25 from twenty a side to match the render.)*
- **Five hanging lanterns** down the aisle, about 8 squares apart, each marked: light sources and weapons both. Lantern-poles at every third stall.
- **Pitchfork rack, water trough and buckets** at the near post; a lantern-pole at every third stall.
- **Maus's stall:** the fourteenth on the left, about two-thirds down, past the Roodberg strings.
- **DM Only:** bravo starts at the far end; Krul (if free) by the far door; lantern light radii; Spook die triggers keyed to features (lanterns, stall doors, the trough).
- **Grid note:** 40 × 14 letterboxes badly on a shared screen. Consider two 20 × 14 halves, split at the middle lantern.
- **Cleanup:** the lanterns are drawn about 2 squares across; shrink them, or treat each drawn lantern as its 10-ft light pool. Paint out the pipes along the curved end walls (they read as steampunk), and square off the rounded ends if they read as a ship's hull.
- **Custom stamps likely:** a pitchfork rack and water butt, hanging stable lanterns.

## Custom Stamp Formula
From [[SP-PBS-00 — Art Brief]] (module seed and `--v 8.1`):
```
top-down orthographic view of [subject], [details], fourteenth-century Alpine battlemap prop, isolated on plain flat white background, no cast shadow, even lighting, highly detailed --ar 1:1 --v 8.1 --stylize 200 --seed 20008
```
Use a **black** background for anything that glows (lanterns), so the light survives the cutout. Remove the background to a transparent PNG before uploading as a Custom Stamp.

## FGU Notes
The A Tourist In Greyhawk draft (`0008 - Nobody's Colours/FGU Kit/`) lists NPC records, the Sabotage Clock and Spook die trackers, and the Maus condition marker as built in FGU. Its tracker PNGs are not in that folder yet. When they are, copy them to `99-Assets/SP-PBS-00/`.
