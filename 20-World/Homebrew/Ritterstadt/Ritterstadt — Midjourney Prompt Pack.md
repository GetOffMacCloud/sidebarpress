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

There are 24 prompts in 6 groups. Every prompt ends with `--v 8.1`. V8.2 is Midjourney's default, so a prompt without the flag silently renders in V8.2.

## How This Pack Works

### 1. Style spine (in every prompt except maps and stamps)
> `oil painting on gessoed board, old-master chiaroscuro, muted frontier palette of peat brown, palisade grey, lake slate and smoke blue, warm lamplight against cold dusk, visible brushwork, aged varnish`

- **Warm lamplight** is the town's colour: every window, the Wachturm lamp, the Fiend's Rest door. The cold is everything outside it.
- **Black ice and Bloom crystals** are the only "wrong" colour: a faint violet-blue sheen. Use it only where the Bloom is present.
- Shares a palette family with [[SP-PBS-01 — Midjourney Prompt Pack]] so the town and the steppe adventure sit together in print.

### 2. Consistency workflow
- Render **A1** first. Add `--sref <A1 URL> --sw 300` to every later prompt in place of `[SREF]`.
- `--seed 565` (the founding year) for composition stability.
- Paste the anchor phrases below verbatim.
- `--cref` is not supported in V8.1; `--oref` renders through V7 (last resort only).

### 3. Standard parameter tail
`--s 250 --seed 565 --no text, letters, watermark, signature, frame, modern clothing --v 8.1`
Aspect ratios: full page `17:22` · half page `3:2` · portrait `4:5` · VTT scene `16:9` · stamp `1:1` · maps `3:2`.

---

## Anchor Phrases (paste verbatim)

| Key | Anchor phrase |
|---|---|
| **RITTERSTADT** | `a small frontier palisade town on a rise above a grey lake shore, timber and turf roofs, a stone watchtower on the highest point, peat-smoke from every chimney` |
| **WACHTURM** | `a squat old stone watchtower on an older foundation, a lamp burning in its top window` |
| **WARDEN** | `a stooped Oeridian scholar of fifty-eight in a grey gown worn thin at the elbows, a brass seal on a chain` |
| **KARET** | `a sharp-eyed tavern-keeper in a leather apron with a ledger in its pocket, standing by a crowded notice board` |
| **YESKA** | `a small elderly Rhennee bargewoman in layered skirts and head-scarf, a knotted cord tally at her waist, short clay pipe` |
| **CAELITH** | `a weathered sylvan elf forester in larch-bark greens and a much-mended cloak, carrying bow-staves, no bow` |
| **HOGAR** | `a grim exiled dwarf smith with a soot-black beard at a roaring forge` |
| **CHANCELLOR** | `a long-faced iron-grey scholar of seventy in a plain black university gown, a chain of office worn under it, one hand on a closed book` |

---

## A · Cover & Key Art (2)

- [ ] **A1 — Cover / STYLE ANCHOR** (render first, full page)
```
a small frontier palisade town on a rise above a grey lake shore, timber and turf roofs, a stone watchtower on the highest point, peat-smoke from every chimney, warm lamplit windows at dusk, a mended section of palisade with pale new stakes, students with packs coming home through the gate, oil painting on gessoed board, old-master chiaroscuro, muted frontier palette of peat brown, palisade grey, lake slate and smoke blue, warm lamplight against cold dusk, visible brushwork, aged varnish --ar 17:22 --s 250 --seed 565 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **A2 — Back cover / title band**
```
a squat old stone watchtower on an older foundation, a lamp burning in its top window, above a palisade at dusk, wide empty sky for text, marsh and uplands beyond, oil painting on gessoed board, old-master chiaroscuro, muted frontier palette of peat brown, palisade grey, lake slate and smoke blue, warm lamplight against cold dusk, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 565 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```

## B · Buildings (10) · `3:2`

- [ ] **B1 — The Fiend's Rest and the Job Board**
```
interior of a crowded frontier tavern at night, a wall-sized notice board thick with pinned papers and wax seals, students and trappers reading it by lamplight, a tavern-keeper in a leather apron watching from behind the bar, oil painting on gessoed board, old-master chiaroscuro, muted frontier palette of peat brown, palisade grey, lake slate and smoke blue, warm lamplight against cold dusk, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 565 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **B2 — The Station House**
```
a two-storey timber hall with a painted coat of arms of an open book over a crossed cudgel and quill above its door, beside an older stone hall, inside a frontier palisade, lamplit windows, a student hurrying in with a satchel, oil painting on gessoed board, old-master chiaroscuro, muted frontier palette of peat brown, palisade grey, lake slate and smoke blue, warm lamplight against cold dusk, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 565 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **B3 — The Archive**
```
a small stone building with a slate roof and narrow good-glass windows, inside: map presses, reading desks, and an iron grille padlocked across the back stacks, a silver-haired elf archivist at a desk, cold daylight, oil painting on gessoed board, old-master chiaroscuro, muted frontier palette of peat brown, palisade grey, lake slate and smoke blue, warm lamplight against cold dusk, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 565 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **B4 — The Long Dormitory**
```
interior of a long low timber dormitory with bunks in two bays, maps pinned over beds, students gathered around a central hearth at night, boots by the door, oil painting on gessoed board, old-master chiaroscuro, muted frontier palette of peat brown, palisade grey, lake slate and smoke blue, warm lamplight against cold dusk, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 565 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **B5 — Forge Row and the University Forge**
```
a row of stone-footed turf-roofed dwarf houses inside a timber palisade, a large forge with two hearths and a water-driven trip-hammer glowing at dusk, dwarves at work, black forge-water in the gutter, oil painting on gessoed board, old-master chiaroscuro, muted frontier palette of peat brown, palisade grey, lake slate and smoke blue, warm lamplight against cold dusk, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 565 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **B6 — The Assay House**
```
interior of a stone assay house, crucibles and brass scales on a long bench, a locked cabinet of faintly violet-blue crystals, a red-bearded dwarf woman in an acid-burned apron weighing ore, oil painting on gessoed board, old-master chiaroscuro, muted frontier palette of peat brown, palisade grey, lake slate and smoke blue, warm lamplight against cold dusk, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 565 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **B7 — The Drill Yard**
```
a packed-earth drill yard behind a guardhouse, a hacked wooden pell, a whitewashed shield-wall line, a towering grey-skinned goliath sergeant drilling students with shields, cold morning, oil painting on gessoed board, old-master chiaroscuro, muted frontier palette of peat brown, palisade grey, lake slate and smoke blue, warm lamplight against cold dusk, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 565 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **B8 — The Landing**
```
a timber quay on a grey lake below a palisade town, four painted Rhennee barges hauled up on rollers for winter, a smokehouse, nets drying on poles, a small elderly Rhennee bargewoman in layered skirts and head-scarf with a short clay pipe on the quay, oil painting on gessoed board, old-master chiaroscuro, muted frontier palette of peat brown, palisade grey, lake slate and smoke blue, warm lamplight against cold dusk, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 565 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **B9 — Market Hill on a fair day**
```
a muddy slope inside a palisade crowded with trestle stalls and awnings on a fair day, one stone-built stall with an indigo awning, round gnome doors set into the hillside, a priest preaching from a barrel, oil painting on gessoed board, old-master chiaroscuro, muted frontier palette of peat brown, palisade grey, lake slate and smoke blue, warm lamplight against cold dusk, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 565 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **B10 — The Larch Camp**
```
bark-and-felt elf shelters half-hidden at the edge of a larch forest outside a palisade gate, a rack of curing bow-staves, a smokeless fire, a weathered sylvan elf forester in larch-bark greens looking out toward a silent misty hollow, oil painting on gessoed board, old-master chiaroscuro, muted frontier palette of peat brown, palisade grey, lake slate and smoke blue, warm lamplight against cold dusk, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 565 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```

## C · Portraits (8) · `4:5`

- [ ] **C1 — Chancellor Adalwin Adenauer** (the Station House portrait)
```
a long-faced iron-grey scholar of seventy in a plain black university gown, a chain of office worn under it, one hand on a closed book, formal standing portrait in an ornate frame-style composition, oil painting on gessoed board, old-master chiaroscuro, muted frontier palette, visible brushwork, aged varnish --ar 4:5 [SREF] --s 250 --seed 565 --no text, letters, watermark, signature, modern clothing --v 8.1
```
- [ ] **C2 — Rektor Albrecht Weissmantel**
```
a stooped Oeridian scholar of fifty-eight in a grey gown worn thin at the elbows, a brass seal on a chain, reading a letter at a cold desk by one candle, half-length portrait, oil painting on gessoed board, old-master chiaroscuro, muted frontier palette of peat brown, palisade grey, lake slate and smoke blue, warm lamplight against cold dusk, visible brushwork, aged varnish --ar 4:5 [SREF] --s 250 --seed 565 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **C3 — Karet, Keeper of the Board**
```
a sharp-eyed tavern-keeper in a leather apron with a ledger in its pocket, standing by a crowded notice board, a wax stamp in one hand, half-length portrait, oil painting on gessoed board, old-master chiaroscuro, muted frontier palette of peat brown, palisade grey, lake slate and smoke blue, warm lamplight against cold dusk, visible brushwork, aged varnish --ar 4:5 [SREF] --s 250 --seed 565 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **C4 — Baba Yeska Marovna**
```
a small elderly Rhennee bargewoman in layered skirts and head-scarf, a knotted cord tally at her waist, short clay pipe, shrewd eyes, by a lakeside stove, half-length portrait, oil painting on gessoed board, old-master chiaroscuro, muted frontier palette of peat brown, palisade grey, lake slate and smoke blue, warm lamplight against cold dusk, visible brushwork, aged varnish --ar 4:5 [SREF] --s 250 --seed 565 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **C5 — Caelith of the Larch**
```
a weathered sylvan elf forester in larch-bark greens and a much-mended cloak, carrying bow-staves, no bow, standing at a forest edge, half-length portrait, oil painting on gessoed board, old-master chiaroscuro, muted frontier palette of peat brown, palisade grey, lake slate and smoke blue, warm lamplight against cold dusk, visible brushwork, aged varnish --ar 4:5 [SREF] --s 250 --seed 565 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **C6 — Hesta Varnholm**
```
a pale fair-haired Suel woman in her thirties in a plain grey dress with a copyist's leather cuff and ink-stained fingers, copying a document at a window, a polite unreadable smile, half-length portrait, oil painting on gessoed board, old-master chiaroscuro, muted frontier palette of peat brown, palisade grey, lake slate and smoke blue, warm lamplight against cold dusk, visible brushwork, aged varnish --ar 4:5 [SREF] --s 250 --seed 565 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **C7 — Dominie Anselm Roth**
```
a broad-faced Perrender priest in his late forties with a close-cropped beard, a dark green coat with many small buttons, holding a staff he does not need, genial expression, half-length portrait, oil painting on gessoed board, old-master chiaroscuro, muted frontier palette of peat brown, palisade grey, lake slate and smoke blue, warm lamplight against cold dusk, visible brushwork, aged varnish --ar 4:5 [SREF] --s 250 --seed 565 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **C8 — Commissioner Lucan Dray**
```
a lean city official in his fifties in fine tailoring under an unweathered travelling cloak, holding a flat leather case, courteous cold smile, half-length portrait, oil painting on gessoed board, old-master chiaroscuro, muted frontier palette of peat brown, palisade grey, lake slate and smoke blue, warm lamplight against cold dusk, visible brushwork, aged varnish --ar 4:5 [SREF] --s 250 --seed 565 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```

## D · Props (2) · `1:1`, `--raw`

- [ ] **D1 — The commission seal and a Job Board posting**
```
a brass commission seal and a stick of red wax beside a sealed parchment notice pinned to rough timber, still life, oil painting on gessoed board, muted frontier palette, visible brushwork, aged varnish --ar 1:1 --raw [SREF] --s 200 --seed 565 --no text, letters, watermark, signature, frame --v 8.1
```
- [ ] **D2 — A Bloom crystal**
```
a small jagged crystal with a faint violet-blue inner light resting on a dwarf assayer's brass scale, frost forming around it, still life, oil painting on gessoed board, muted frontier palette, visible brushwork, aged varnish --ar 1:1 --raw [SREF] --s 200 --seed 565 --no text, letters, watermark, signature, frame --v 8.1
```

## E · Map (1) · `3:2`, parchment style — **no `[SREF]`**
*Midjourney mangles text: generate unlabeled and add labels yourself (Wachturm, Station House, Archive, Ritter's Hall, St. Erika's, the Fiend's Rest, the Grey Wolf, Market Hill, the Burrows, Forge Row, the Long Dormitory, the Drill Yard, the eastern gate breach, the Landing, the Larch camp, the farmsteads).*

- [ ] **E1 — Town map**
```
fantasy town map viewed top-down, a small palisade town on a rise above a lake shore, a stone watchtower on the highest point, a market slope, a row of houses inside the eastern wall, a quay with barges below, farm fields to the south, forest edge to the east, NO TEXT, NO LABELS, NO WORDS, aged parchment, hand-drawn ink and watercolor --ar 3:2 --s 150 --seed 565 --v 8.1
```

## F · VTT Stamp (1) · Inkarnate
- [ ] **F1 — Palisade section with new stakes**
```
top-down orthographic view of a section of timber palisade wall with a repaired gap of pale new stakes and rope lashings, battlemap prop, isolated on plain flat white background, no cast shadow, even lighting, highly detailed --ar 1:1 --raw --s 200 --seed 565 --v 8.1
```

## Export Notes
- Save finals to `99-Assets/Ritterstadt/art/` with the prompt ID in the filename (e.g. `Ritterstadt - B1 Fiends Rest.png`).
- Print: 300 dpi at final size; convert to CMYK in layout.
- Record the chosen A1 URL here: `STYLE ANCHOR URL: ______________________`
