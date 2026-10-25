---
type: art-brief
book: "Ritterstadt — Gazetteer (Book)"
midjourney_version: "8.1"
seed: 565
prompt_count: 24
tags: [midjourney, art, prompt-pack, ritterstadt, gazetteer]
---

# Ritterstadt — Midjourney Prompt Pack (v8.1)

Back to [[Ritterstadt — Gazetteer (Book)]]

Converted to the house black-and-white ink style, 2026-10-24 (see [[Art-Style-Guide]]).

There are 24 prompts in 6 groups. Every prompt carries `--v 8.1`. V8.2 is Midjourney's default, so a prompt without the flag silently renders in V8.2.

## How This Pack Works

### 1. Style spine (house spines from [[Art-Style-Guide]], by image type)
Every print prompt is **subject + composition + spine + parameter tail**, using the house black-and-white pen-and-ink spines verbatim: **SCENE** for the covers and buildings (A, B), **PORTRAIT** for portraits (C), **PLATE** at `--ar 1:1` for props (D), and **MAP** for the town map (E). The VTT stamp (F) is screen-only and stays in its own style.

- **Lamplight** is still the town's signature, drawn now as the one **white-lined light source in a black scene**: every window, the Wachturm lamp, the Fiend's Rest door. The cold outside is solid black mass and dense hatching. Paste the **LAMPLIGHT** anchor.
- **Black ice and Bloom crystals** are the only "wrong" thing in the book: a **distinctive crystalline white-line pattern** (fine radiating white lines scratched into faceted black shards) that nothing else is drawn with. Paste the **BLOOM** anchor, and use it only where the Bloom is present.
- Uses the same house spines as every Sidebar Press print product, so the town and [[SP-PBS-01 — Midjourney Prompt Pack]] sit together in print once that pack is on the house style too.

### 2. Consistency workflow
- Render **A1** first, in the ink style (an older painted A1 can't serve as the anchor). Never use the `99-Assets/_Style-Reference/` samples as `--sref`. Add `--sref <A1 URL> --sw 300` to every later prompt in place of `[SREF]`.
- `--seed 565` (the founding year) for composition stability.
- Paste the anchor phrases below verbatim.
- `--cref` is not supported in V8.1; `--oref` renders through V7 (last resort only).

### 3. Standard parameter tail
`--seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing`
This is the [[Art-Style-Guide]] tail plus this pack's seed and its own `frame, modern clothing` exclusions (C1 drops `frame` for its frame-style composition, props drop `modern clothing`, and the map takes the guide's list alone). `[SREF]` sits right after `--ar`. `--style raw` and the low `--stylize` keep the hand-drawn line from smoothing into digital gloss.
Aspect ratios: full page `17:22` · half page `3:2` · portrait `4:5` · VTT scene `16:9` · stamp `1:1` · maps `3:2`.

---

## Anchor Phrases (paste verbatim)

| Key | Anchor phrase |
|---|---|
| **RITTERSTADT** | `a small frontier palisade town on a rise above a flat pale lake shore, timber and turf roofs, a stone watchtower on the highest point, peat-smoke from every chimney` |
| **WACHTURM** | `a squat old stone watchtower on an older foundation, a lamp burning in its top window` |
| **WARDEN** | `a stooped Oeridian scholar of fifty-eight in a plain hatched gown worn thin at the elbows, a brass seal on a chain` |
| **KARET** | `a sharp-eyed tavern-keeper in a leather apron with a ledger in its pocket, standing by a crowded notice board` |
| **YESKA** | `a small elderly Rhennee bargewoman in layered skirts and head-scarf, a knotted cord tally at her waist, short clay pipe` |
| **CAELITH** | `a weathered sylvan elf forester in larch-bark-textured forester's garb and a much-mended cloak, carrying bow-staves, no bow` |
| **HOGAR** | `a grim exiled dwarf smith with a soot-black beard at a roaring forge` |
| **LAMPLIGHT** | `lamplight drawn as the one white-lined light source in a scene of solid black` |
| **BLOOM** | `the Bloom drawn as a distinctive crystalline pattern of fine radiating white lines scratched into faceted solid black shards` |
| **CHANCELLOR** | `a long-faced grizzled scholar of seventy in a plain black university gown, a chain of office worn under it, one hand on a closed book` |

---

## A · Cover & Key Art (2)

- [ ] **A1 — Cover / STYLE ANCHOR** (render first, full page)
```
a small frontier palisade town on a rise above a flat pale lake shore, timber and turf roofs, a stone watchtower on the highest point, peat-smoke from every chimney, lamplit windows at dusk, lamplight drawn as the one white-lined light source in a scene of solid black, a mended section of palisade with pale new stakes, students with packs coming home through the gate, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 17:22 --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing
```
- [ ] **A2 — Back cover / title band**
```
a squat old stone watchtower on an older foundation, a lamp burning in its top window, above a palisade at dusk, lamplight drawn as the one white-lined light source in a scene of solid black, wide empty sky for text, marsh and uplands beyond, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing
```

## B · Buildings (10) · `3:2`

- [ ] **B1 — The Fiend's Rest and the Job Board**
```
interior of a crowded frontier tavern at night, a wall-sized notice board thick with pinned papers and wax seals, students and trappers reading it by lamplight, lamplight drawn as the one white-lined light source in a scene of solid black, a tavern-keeper in a leather apron watching from behind the bar, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing
```
- [ ] **B2 — The Station House**
```
a two-storey timber hall with a painted coat of arms of an open book over a crossed cudgel and quill above its door, beside an older stone hall, inside a frontier palisade, lamplit windows, lamplight drawn as the one white-lined light source in a scene of solid black, a student hurrying in with a satchel, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing
```
- [ ] **B3 — The Archive**
```
a small stone building with a slate roof and narrow good-glass windows, inside: map presses, reading desks, and an iron grille padlocked across the back stacks, a silver-haired elf archivist at a desk, cold daylight, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing
```
- [ ] **B4 — The Long Dormitory**
```
interior of a long low timber dormitory with bunks in two bays, maps pinned over beds, students gathered around a central hearth at night, the hearth drawn as the one white-lined light source in a scene of solid black, boots by the door, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing
```
- [ ] **B5 — Forge Row and the University Forge**
```
a row of stone-footed turf-roofed dwarf houses inside a timber palisade, a large forge with two hearths and a water-driven trip-hammer glowing at dusk, the forge mouth drawn as the one white-lined light source in a scene of solid black, dwarves at work, black forge-water in the gutter, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing
```
- [ ] **B6 — The Assay House**
```
interior of a stone assay house, crucibles and brass scales on a long bench, a locked cabinet of Bloom crystals, the Bloom drawn as a distinctive crystalline pattern of fine radiating white lines scratched into faceted solid black shards, a dwarf woman with a dark hatched beard in an acid-burned apron weighing ore, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing
```
- [ ] **B7 — The Drill Yard**
```
a packed-earth drill yard behind a guardhouse, a hacked wooden pell, a whitewashed shield-wall line, a towering goliath sergeant with mottled stippled skin drilling students with shields, cold morning, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing
```
- [ ] **B8 — The Landing**
```
a timber quay on a flat pale lake below a palisade town, four Rhennee barges with hulls painted in bold black-and-white patterns hauled up on rollers for winter, a smokehouse, nets drying on poles, a small elderly Rhennee bargewoman in layered skirts and head-scarf with a short clay pipe on the quay, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing
```
- [ ] **B9 — Market Hill on a fair day**
```
a muddy slope inside a palisade crowded with trestle stalls and awnings on a fair day, one stone-built stall with a solid black awning, round gnome doors set into the hillside, a priest preaching from a barrel, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing
```
- [ ] **B10 — The Larch Camp**
```
bark-and-felt elf shelters half-hidden at the edge of a larch forest outside a palisade gate, a rack of curing bow-staves, a smokeless fire, a weathered sylvan elf forester in larch-bark-textured forester's garb looking out toward a silent hollow filled with stippled mist, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing
```

## C · Portraits (8) · `4:5`

- [ ] **C1 — Chancellor Adalwin Adenauer** (the Station House portrait)
```
a long-faced grizzled scholar of seventy in a plain black university gown, a chain of office worn under it, one hand on a closed book, formal standing portrait in an ornate frame-style composition, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, modern clothing
```
- [ ] **C2 — Rektor Albrecht Weissmantel**
```
a stooped Oeridian scholar of fifty-eight in a plain hatched gown worn thin at the elbows, a brass seal on a chain, reading a letter at a cold desk by one candle, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing
```
- [ ] **C3 — Karet, Keeper of the Board**
```
a sharp-eyed tavern-keeper in a leather apron with a ledger in its pocket, standing by a crowded notice board, a wax stamp in one hand, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing
```
- [ ] **C4 — Baba Yeska Marovna**
```
a small elderly Rhennee bargewoman in layered skirts and head-scarf, a knotted cord tally at her waist, short clay pipe, shrewd eyes, by a lakeside stove, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing
```
- [ ] **C5 — Caelith of the Larch**
```
a weathered sylvan elf forester in larch-bark-textured forester's garb and a much-mended cloak, carrying bow-staves, no bow, standing at a forest edge, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing
```
- [ ] **C6 — Hesta Varnholm**
```
a pale fair-haired Suel woman in her thirties in a plain lightly hatched dress with a copyist's leather cuff and ink-stained fingers, copying a document at a window, a polite unreadable smile, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing
```
- [ ] **C7 — Dominie Anselm Roth**
```
a broad-faced Perrender priest in his late forties with a close-cropped beard, a dark coat with many small buttons, holding a staff he does not need, genial expression, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing
```
- [ ] **C8 — Commissioner Lucan Dray**
```
a lean city official in his fifties in fine tailoring under an unweathered travelling cloak, holding a flat leather case, courteous cold smile, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing
```

## D · Props (2) · `1:1`, PLATE

- [ ] **D1 — The commission seal and a Job Board posting**
```
a brass commission seal and a stick of dark sealing wax beside a sealed parchment notice pinned to rough timber, still life, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 1:1 [SREF] --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame
```
- [ ] **D2 — A Bloom crystal**
```
a small jagged Bloom crystal with a faint inner light, the Bloom drawn as a distinctive crystalline pattern of fine radiating white lines scratched into faceted solid black shards, resting on a dwarf assayer's brass scale, stippled frost forming around it, still life, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 1:1 [SREF] --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame
```

## E · Map (1) · `3:2`, MAP spine — **no `[SREF]`**
*Midjourney mangles text: generate unlabeled and add labels yourself (Wachturm, Station House, Archive, Ritter's Hall, St. Erika's, the Fiend's Rest, the Grey Wolf, Market Hill, the Burrows, Forge Row, the Long Dormitory, the Drill Yard, the eastern gate breach, the Landing, the Larch camp, the farmsteads).*

- [ ] **E1 — Town map**
```
fantasy town map viewed top-down, a small palisade town on a rise above a lake shore, a stone watchtower on the highest point, a market slope, a row of houses inside the eastern wall, a quay with barges below, farm fields to the south, forest edge to the east, NO TEXT, NO LABELS, NO WORDS, classic 1970s fantasy role-playing game module map, hand-inked black line cartography on white paper, hatched hills and mountains, stippled marsh, tree symbols, ruled grid, clean labels left blank, high contrast black and white line art --ar 3:2 --seed 565 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark
```

## F · VTT Stamp (1) · Inkarnate
- [ ] **F1 — Palisade section with new stakes**
```
top-down orthographic view of a section of timber palisade wall with a repaired gap of pale new stakes and rope lashings, battlemap prop, isolated on plain flat white background, no cast shadow, even lighting, highly detailed --ar 1:1 --raw --s 200 --seed 565 --v 8.1
```

## Export Notes
- Save finals to `99-Assets/Ritterstadt/art/` with the prompt ID in the filename (e.g. `Ritterstadt - B1 Fiends Rest.png`).
- Print: follow [[Art-Style-Guide]] › Print production. Upscale 2×, convert to pure **1-bit black and white at 600 dpi** (threshold about 50%), clean stray specks, and keep the white white. No CMYK step: the art is pure black. At 600 dpi a column plate (8 cm) is 1,890 px wide and a full page (17 cm) is 4,015 px.
- F1 is screen-only VTT art: keep it as a transparent PNG and don't threshold it.
- Record the chosen A1 URL here: `STYLE ANCHOR URL: ______________________`
