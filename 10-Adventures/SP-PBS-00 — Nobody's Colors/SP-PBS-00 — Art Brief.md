---
type: art-brief
adventure: "SP-PBS-00"
section: internal
publish_order: 0
publish: false
tags: [art, midjourney, production]
---

# SP-PBS-00 — Art Brief

Back to [[SP-PBS-00-Nobodys-Colors]] · Maps: [[SP-PBS-00 — Map Assets]]

Converted to the house black-and-white ink style, 2026-10-24 (see [[Art-Style-Guide]]). The guide holds the house look, the spines, the parameter tail and the print-production steps (1-bit at 600 dpi).

> [!warning] Production file. Never paste into the brew.

Ported from the A Tourist In Greyhawk draft's `0008 - Midjourney Prompts`. The seed is kept for composition continuity; any renders made before the ink conversion are in the old color style and need re-rendering.

**Module seed:** `--seed 20008` — reuse it on every prompt so faces, composition and light stay consistent across the module.
**Version:** `--v 8.1` throughout.

> [!note] The `vtt-build` skill's stamp formula still says `--v 7`. The standing instruction is `--v 8.1`, used throughout here.

---

## Style anchor

Paste this into every prompt. It is what makes the module look like one book.

> *fourteenth-century Alpine, dark slate roofs and stippled plaster walls, undyed wool drawn as plain unhatched untextured white cloth against clan bands of bold black-and-white chevrons, stripes and checks, flat overcast northern light, restrained and unromantic*

Then add the house spine for the image type from [[Art-Style-Guide]] (**SCENE** for cover, column and scene art; **PORTRAIT** for NPCs; **PLATE** for the handout) and its parameter tail with `--seed 20008`.

**House patterns (paste verbatim).** Each clan's colors become one bold black-and-white pattern; the Halbritters get none.

| House | Old color | Ink treatment |
|---|---|---|
| Halbritter | undyed grey | `undyed wool drawn as plain unhatched untextured white cloth` |
| Meerijder | red-over-black | `bold black-and-white chevrons` |
| Roodberg | blue-over-white | `bold black-and-white stripes` |
| Vuurzward | a green so dark it reads as black | `heavy black-and-white checks` |
| Ostvelt (the dead house; the rented silks) | dead green | `racing silks in a worn, broken black-and-white lozenge pattern` |

**The visual thesis: plain against pattern.** The Halbritters may wear only undyed cloth by dress-law. Every clan in the module has colors, drawn here as bold black-and-white patterned bands; this family has none. Draw them in **plain, unhatched, untextured white cloth** in every frame they appear in, the only untextured shapes in pictures where every other surface is hatched, stippled or patterned, and keep the clan bands and pavilions busy with chevrons, stripes and checks around them. That contrast *is* the adventure. Midjourney likes to hatch everything: if a render textures their clothes, vary that region or white it out in cleanup before the 1-bit conversion.

**Avoid throughout:** heroic posing, glowing magic, plate armor, dragons, high-fantasy ornament, modern faces, smiling.

---

## Sizing reference

| Use | Aspect | Render at |
|---|---|---|
| Front cover | `--ar 2:3` | 1400 × 2100 |
| Full-column art (8 × 24 cm) | `--ar 1:3` | 945 × 2835 |
| Half-column / inset | `--ar 4:3` | 1200 × 900 |
| Scene banner, full width | `--ar 16:6` | 2000 × 750 |
| NPC portrait | `--ar 3:4` | 900 × 1200 |
| Handout | `--ar 3:4` | 1200 × 1600 |

Homebrewery images use `{width:Ncm}` — **never `height`**. Host on Imgur, a GitHub raw link, or Homebrewery's own uploader. Discord CDN links carry expiry tokens and die within a day, taking the image out of the brew and every export with it.

**Print production:** every print image goes through [[Art-Style-Guide]] › Print production: upscale 2×, convert to pure **1-bit black and white at 600 dpi** (threshold about 50%), clean stray specks, keep the white white. At 600 dpi an 8 cm column is 1,890 px wide and a 17 cm full page 4,015 px; the "Render at" column above is the Midjourney render, not the print file.

---

## 1 — Front cover

```
A pale dapple-grey mare, her coat left plain white with sparse stippled dapples, standing alone in a lantern-lit stable row at night, forty stalls receding into solid black behind her, the lantern drawn as the one white-lined light source in a black scene, a young man in undyed wool drawn as plain unhatched untextured white cloth standing at her shoulder with his hand flat on her neck, racing silks in a worn, broken black-and-white lozenge pattern folded over the stall rail beside them, fourteenth-century Alpine, dark slate roofs and stippled plaster walls, restrained and unromantic, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 2:3 --seed 20008 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark
```

Second option, wider and colder — the arrival rather than the secret:

```
A lake harbor at dawn in the fourteenth-century Alps, a fat single-masted cog tied at a stone quay, a covered wagon at the head of the gangway, mountains in hatched contour lines behind, flat pale water in long ruled lines filling the horizon, three travelers in worn road clothes standing apart from one another, flat overcast northern light, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 2:3 --seed 20008 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark
```

---

## 2 — Column art, 8 × 24 cm

Tall and narrow. **Compose for the shape** — never render wide and scale down.

**Chapter opener — the doorpost:**
```
Extreme vertical composition, a weathered timber doorpost seen straight on, bare and scrubbed pale by rain, its face left plain unhatched untextured white, no painted clan band on it, neighboring doorposts visible at the edges carrying painted clan bands of bold black-and-white chevrons and bold black-and-white stripes, dark slate and stippled plaster wall, flat overcast northern light, fourteenth-century Alpine, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 1:3 --seed 20008 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark
```

**Appendix opener — the silks:**
```
Extreme vertical composition, a set of racing silks in a worn, broken black-and-white lozenge pattern hanging alone on a peg against a stippled plaster wall, dust on the shoulders, a wax seal and folded paper on a shelf beneath, a single shaft of cold daylight cut as a hard-edged white beam through solid black, fourteenth-century Alpine, melancholy, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 1:3 --seed 20008 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark
```

---

## 3 — Scene art

**Aerden (Scene 0):**
```
A small Alpine market town of dark slate roofs and stippled plaster walls below meadow and mountains, every doorpost painted at shoulder height with a clan band of bold black-and-white chevrons, stripes or checks, milk carts in the square before dawn, straw archery targets on the green, no walls and no castle, fourteenth century, flat overcast northern light, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 16:6 --seed 20008 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark
```

**The Erlen bridge (Scene 2):**
```
A narrow stone toll bridge over a slow river, fifty cattle strung along the road behind it, drovers wearing clan bands of bold black-and-white chevrons standing across the span, a covered wagon halted, a small toll house at the near end, morning, fourteenth-century Alpine, flat overcast light, tense but bloodless, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 16:6 --seed 20008 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark
```

**The Rhennee (Scene 4):**
```
Three long low barges with lanterns strung along their awnings, gliding alongside a single-masted lake cog at dusk, forty feet of solid black water between them, a woman standing at the barge rail looking across, stippled fog on the far horizon, fourteenth-century, the strung lanterns drawn as the only white-lined light in a black scene, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 16:6 --seed 20008 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark
```

**The Duffkyyn Flats (Scene 5):**
```
A great race meeting outside a fourteenth-century Alpine walled town, clan pavilions banded in bold black-and-white chevrons, stripes and checks, cook-fires, a sale ring, crowds, a long pale racecourse curving beyond, a stone town with a clock tower behind, overcast bright, busy and dense with pattern, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 16:6 --seed 20008 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark
```

**The stable rows (Scene 6):**
```
A long timber stable gallery at night, forty stalls under one roof, a narrow central aisle, a hanging lantern every twenty feet, horses shifting in solid black dark, one lantern lifted off its hook far down the row, straw and shadow, fourteenth-century, the lanterns drawn as the only white-lined light in a black scene, threatening, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 16:6 --seed 20008 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark
```

**Post time (Scene 7):**
```
A young woman in racing silks in a worn, broken black-and-white lozenge pattern being legged up onto a pale dapple-grey mare, her coat left plain white with sparse stippled dapples, in a stable row, a young man in undyed wool drawn as plain unhatched untextured white cloth standing beside them with empty hands, an old man watching from the end of the row, twenty minutes before a race, fourteenth-century Alpine, flat overcast daylight, quiet and charged, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 4:3 --seed 20008 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark
```

---

## 4 — NPC portraits

All at `--ar 3:4`. Append to each:
`fourteenth-century Alpine, unsmiling, no armor, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 3:4 --seed 20008 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark`

| NPC | Prompt body |
|---|---|
| **Corwin Halbritter** | A nineteen-year-old man in undyed wool drawn as plain unhatched untextured white cloth, well-made but plain clothes, dark hair, an expression caught between bravado and fear, hands that have done a little work but not much |
| **Adalinde Halbritter** | A woman of twenty-four in a riding coat of undyed wool drawn as plain unhatched untextured white cloth, hair tied back hard, weather on her face, holding a bucket, looking directly at the viewer without expression, entirely unimpressed |
| **Otwin Halbritter** | A drawn, pallid man in his sixties seated with a ledger open on his knees, gout-swollen hands, dressed in undyed wool drawn as plain unhatched untextured white cloth, tired and exact, not unkind |
| **Hessel Amtmann** | A soldier in his forties in a plain house-guard's jerkin of undyed wool drawn as plain unhatched untextured white cloth, with no clan band on the sleeve, looking slightly away from the viewer, guilty and trying not to be |
| **Sivert Vuurzward** | A prosperous man of fifty in near-black wool with a clan band of heavy black-and-white checks and a fur collar, holding his hat in both hands, courteous and entirely untroubled, the calmest man in the room |
| **Anse Krul** | A thin, plain farrier in his thirties in working leather, a hoof knife in his hand held like a craftsman's tool, no menace at all in his face, which is worse |
| **Boedic of the Meerijder** | A weathered drover in his fifties wearing clan bands of bold black-and-white chevrons, holding a folded paper he would rather not be holding, apologetic, immovable |
| **Alric Roodberg** | A precise clerk of sixty wearing clan bands of bold black-and-white stripes, with a heavy register under one arm, spectacles, a man who loves a rulebook |
| **Marda Vosk** | A lake captain in her forties in heavy weatherproof wool, short grizzled hair, weighing you up and pricing you, faint amusement |
| **Grete Haslau** | An innkeeper in her fifties, widow's dress, a foreign soldier's coin on a cord at her throat, chalk in one hand, refusing to be thanked |

---

## 5 — Handout: the notice

Not a Midjourney job — this wants clean type on a texture. If you generate the paper:

```
A sheet of good fourteenth-century laid paper pinned to a short section of rough timber post drawn in wood-grain lines, blank, its laid lines barely ruled, a plain solid black wax seal at the lower right with no device or crest impressed in it, lit from the left with hatched shadow along its right edge, slightly cockled, seen straight on, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 3:4 --seed 20008 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark
```

**The seal must be blank.** That is the whole joke: a family with no clan has no device to press. Set the notice text over it afterward. In 1-bit print the seal reads as a solid black blot, still blank.

---

## 6 — Custom map stamps, if needed

Per the house formula, with the version corrected. Screen-only VTT art: out of scope for the ink conversion, so this prompt stays in its own style (see [[Art-Style-Guide]] › Out of scope):

```
top-down orthographic view of [subject], [details], fourteenth-century Alpine battlemap prop, isolated on plain flat white background, no cast shadow, even lighting, highly detailed --ar 1:1 --v 8.1 --stylize 200 --seed 20008
```

Likely needs: a deck stall with canvas roof · a pitchfork rack and water butt · stone bridge sections · a drover's cart · hanging stable lanterns.

Use a **black** background instead of white for anything meant to glow, so luminosity survives the cutout. Remove the background to transparent PNG before upload or you paste a white box.

---

## 7 — Battlemaps (screen-only VTT)

Out of scope for the ink conversion, like the stamps: battlemaps are color VTT art (see [[Art-Style-Guide]] › Out of scope). Render without a grid; the grid is added at export (see [[SP-PBS-00 — Map Assets]]). Bases are saved as `99-Assets/SP-PBS-00/SP-PBS-00 — [Map] — MJ base.png`.

**What worked (2026-10-25):** the first bridge and stable renders came out as an angled view and a cutaway side view, so both were re-rolled with the hard overhead cues below. The first renders were overwritten. They would not have served as scene banners anyway, since print art is now ink (section 3).

**The Erlen Bridge** — base ✅ (re-roll)
```
directly overhead 90-degree top-down battlemap, flat orthographic view straight down, no visible walls or sides of objects, a narrow stone toll bridge seen from above as a straight paved strip with parapet tops, crossing a slow shallow river that runs across the middle of the map, the roof of a small slate toll house seen from above at the near end, dirt road the full length, cattle seen from above along the road, a drovers' camp with campfire and two carts seen from above, meadow and reeds, morning light, muted ochre and moss palette, highly detailed, no grid, no text --ar 5:3 --v 8.1 --style raw --stylize 150 --seed 20008 --no isometric, perspective, three-quarter view, side view, elevation, arch, horizon, characters, labels
```

**The *Kortheim Maid*** — base ✅ (first render; Map Assets changed to match it)
```
top-down orthographic battlemap, a fat single-masted medieval lake cog seen from directly above, centered, dark water surrounding it on all sides, plank deck with a hatch cover at the bow, mast amidships, tiller and a single hanging lantern at the stern, a small canvas-roofed horse stall against the right-hand rail amidships with straw inside, passenger bedrolls toward the bow, coiled ropes and casks, night, the stern lantern the only light source casting a warm pool on the aft deck, the rest of the deck in deep blue darkness, fourteenth-century, highly detailed, no grid, no text --ar 5:3 --v 8.1 --style raw --stylize 150 --seed 20008 --no perspective, horizon, characters, sails seen from the side, grid lines, labels
```
*Rhennee variant:* add `three long low barges with lantern-lit awnings alongside on the left, dusk`, at `--ar 16:9`.

**The Stable Rows** — base ✅ (re-roll)
```
directly overhead 90-degree top-down battlemap, flat orthographic view straight down into a long stable with the roof removed, a straw-covered central aisle running the full length, twenty small square horse stalls along each side seen from above, the backs of horses visible from above in most stalls, hanging lanterns seen from above at regular intervals casting round pools of warm orange light with dark gaps between them, a water trough, buckets and a pitchfork rack at the near end, night, highly detailed, no grid, no text --ar 20:7 --v 8.1 --style raw --stylize 150 --seed 20008 --no isometric, perspective, side view, cutaway, elevation, front view, wall, characters, people, labels
```
*If it drifts to an angle:* two `--ar 10:7` halves (the near end with the trough and pitchfork rack; the far end with a closed double door).

---

## Shot list

- [ ] Front cover
- [ ] Column art ×2 — chapter opener, appendix opener
- [ ] Scene art ×6
- [ ] NPC portraits ×10 *(minimum: Corwin, Adalinde, Otwin, Vuurzward — the four who carry the story)*
- [ ] Notice handout paper
- [x] Battlemap bases ×3 (2026-10-25)
- [ ] Custom stamps, as the maps require
- [ ] All print images converted to 1-bit at 600 dpi ([[Art-Style-Guide]] › Print production)
- [ ] All images rehosted off Discord and sized in `cm`
