---
type: art-brief
adventure: "SP-OP01"
section: internal
publish_order: 0
publish: false
tags: [art, midjourney, production]
---

# SP-OP01 — Art Brief

Back to [[SP-OP01-What-the-Dead-Fear]] · Maps: [[SP-OP01 — Map Assets]]

**Style (set 2026-11-16): engraving.** Greybeard picked the look of the first trap render: a detailed black-and-white wood engraving in the manner of Gustave Doré, fine engraved hatching on every surface. It replaces the old 1970s pen-and-ink spine *for this module*, kept lighter (silver-grey midtones, torch and candle highlights) and with the monster at true scale (Large, about ten feet). Style reference: `99-Assets/SP-OP01/_ref/style-ref-engraving.png`. Upload it to Midjourney and add `--sref <its URL>` to prompts 1, 2, 4 and 5 for a matched set. Seed `--seed 26601`.

Each prompt below is complete; copy the whole block. **Tail (for reference):** `--v 8.1 --style raw --stylize 75 --seed 26601 --no color, grey wash, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, monogram`

## 1. PLATE — Brother Ossian, true form (stat-block page)
**Save as:** `99-Assets/SP-OP01/plate-ossian.png`
```text
a worm-like aberration about ten feet long with a thick glistening segmented body, six long jointed limbs ending in hooked claws, a vertical lamprey mouth ringed with teeth, wet skin catching the light, rearing up and leaning forward, full body, standing on a bare stone floor, small cast shadow beneath it, plain white background, isolated creature plate for a bestiary page, detailed black and white wood engraving, nineteenth-century gothic book illustration in the manner of Gustave Doré, fine parallel engraved lines and crosshatching, every surface rendered in engraved line texture, silver-grey midtones, lit by torchlight and candles, bright highlights, plenty of light areas, high contrast black and white --ar 3:4 --v 8.1 --style raw --stylize 75 --seed 26601 --no color, grey wash, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, monogram, background scenery, solid black background
```

## 2. SCENE — The trap (spread header, 3:2 or 1:3)
**Save as:** `99-Assets/SP-OP01/scene-the-trap.png`
```text
inside a stone ossuary vault, a horse-sized worm-like monster about ten feet long hanging head-first from a round hole in the vaulted ceiling, half its body still inside the shaft, six clawed limbs reaching down, lamprey mouth open, the monster in the middle distance and no bigger than the coffins below it, gaunt ghouls cowering behind stone coffin lids stood on end, three adventurers in the foreground seen from behind, one holding a torch, ankle-deep water on the floor reflecting the torch, walls of stacked skulls, detailed black and white wood engraving, nineteenth-century gothic book illustration in the manner of Gustave Doré, fine parallel engraved lines and crosshatching, every surface rendered in engraved line texture, silver-grey midtones, lit by torchlight and candles, bright highlights, plenty of light areas, high contrast black and white --ar 3:2 --v 8.1 --style raw --stylize 75 --seed 26601 --no color, grey wash, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, monogram, giant, kaiju, colossal, deep water, wading, night sky
```

## 3. MAP — Merrow's Rest DM key (print) — DONE in ink, skip
**Don't render.** `map-merrows-rest-key.png` already exists as the exact ink key; a render saved under that name would replace it. Kept for reference only.
```text
small dungeon key map of a chapel above and catacombs below, a stair down to a gallery, a side room, a room of wall niches, a pair of doors, and a long rectangular vault with two rows of coffins and an altar, classic 1970s fantasy role-playing game module map, hand-inked black line cartography on white paper, hatched hills and mountains, stippled marsh, tree symbols, ruled grid, clean labels left blank, high contrast black and white line art --ar 3:2 --v 8.1 --style raw --stylize 75 --seed 26601 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark
```

## 4. PORTRAIT — Brother Ossian, human guise
**Save as:** `99-Assets/SP-OP01/portrait-ossian-guise.png`
```text
a hunched elderly monk in dark wool robes with a kind gentle smile and wide unblinking eyes, skin with a faint wet sheen, long fingers bent slightly backward around a goblet, candlelit, head and shoulders portrait, plain white background, detailed black and white wood engraving, nineteenth-century gothic book illustration in the manner of Gustave Doré, fine parallel engraved lines and crosshatching, every surface rendered in engraved line texture, silver-grey midtones, lit by torchlight and candles, bright highlights, plenty of light areas, high contrast black and white --ar 4:5 --v 8.1 --style raw --stylize 75 --seed 26601 --no color, grey wash, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, monogram, background scenery
```

## 5. PORTRAIT — Sexton Harrow
**Save as:** `99-Assets/SP-OP01/portrait-sexton-harrow.png`
```text
a big stooped undead gravedigger in a stained leather apron, grey sunken face with pale eyes and a sorrowful expression, holding a shovel, head and shoulders portrait, plain white background, detailed black and white wood engraving, nineteenth-century gothic book illustration in the manner of Gustave Doré, fine parallel engraved lines and crosshatching, every surface rendered in engraved line texture, silver-grey midtones, lit by torchlight and candles, bright highlights, plenty of light areas, high contrast black and white --ar 4:5 --v 8.1 --style raw --stylize 75 --seed 26601 --no color, grey wash, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, monogram, background scenery
```

## 6. Color portrait (FGU portrait and token source, screen only)
**Save as:** `99-Assets/SP-OP01/portrait-ossian-color.png`
```text
a towering worm-like aberration with glistening pale pink-grey segmented flesh, a vertical lamprey mouth ringed with teeth, two of its six clawed limbs raised, head and shoulders portrait in three-quarter view, the head in the upper middle of the frame with clear space around it, stylized fantasy tabletop RPG creature portrait, crisp painted digital game art, clean confident linework with painterly cel-like shading, vivid but controlled color, soft rim light, strong readable silhouette, on a soft light cream and warm pale grey background with a gentle vignette --ar 3:4 --v 8.1 --stylize 150 --seed 26500 --no text, letters, signature, watermark, frame, border, dark background, black background
```

**Token:** crop the head from this render into a square and save it as `99-Assets/SP-OP01/token-ossian.png`.

## File names (99-Assets/SP-OP01/, no SP-OP01 prefix)
`plate-ossian.png`, `scene-the-trap.png`, `map-merrows-rest-key.png`, `portrait-ossian-guise.png`, `portrait-sexton-harrow.png`, `portrait-ossian-color.png`, `token-ossian.png`, `map-saints-ossuary.png`. The FGU build picks up any of these automatically on the next run.
