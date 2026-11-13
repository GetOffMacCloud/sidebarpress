---
type: art-brief
adventure: "SP-GQ00"
section: internal
publish: false
tags: [art-brief, shadow-on-the-quag, SP-GQ00, midjourney]
---

# SP-GQ00 — Art Brief

Midjourney prompts for **GQ0** (the arc guide and the prologue, *The Crossing*). Every prompt uses the house black-and-white ink style for print ([[Art-Style-Guide]]): **subject + composition + spine + parameter tail**, with `--v 8.1`.

## How This Brief Works
- **Spines** are pasted verbatim from the [[Art-Style-Guide]]: **SCENE** for the cover and scenes, **PORTRAIT** for NPCs, **PLATE** for the creature and props.
- **Seed:** `--seed 26576`, the arc's seed (shared with GQ1's sigils), so the GQ series renders as one family.
- **Style reference:** lock `--sref` from GQ1's first approved scene once it exists, and use the same `--sref` here with `--sw 300`. Until then, render **P1 (the cover)** first and lock it. `[SREF]` marks where it goes.
- **Print density (lesson from the Ritterstadt Gazetteer, 2026-11-13):** the SCENE spine's "large masses of solid black" made night interiors come out 55–78% solid black, too heavy for B&W print. Every night scene below adds the **print-safe clause**: `open white paper in the lit areas, solid black limited to the deepest shadows`. Aim for 25–45% solid black. Check before upscaling; if a render is a black slab, rerun it rather than lightening it, because lightening line art only makes it grey.
- **Print production:** render, upscale 2×, convert to 1-bit at 600 dpi with a ~50% threshold, clean up specks ([[Art-Style-Guide#Print production]]).
- **Files** go in `99-Assets/SP-SQ/` under the subfolder listed with each prompt, named as listed. Reuse is marked where GQ1 or the Ritterstadt Gazetteer already has the art.

**Standard tail** (paste after `--ar`):
`[SREF] --seed 26576 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, modern clothing`

---

## A · Cover and Openers

**P1 — Cover / style anchor** (full page; for `99-Assets/_Covers/make_covers.py`, which crops to 2:3)
File: `cover/SP-GQ00 — Cover.png`
```
a broad-bellied single-masted lake cog with a carved pike's head on her stem post drifting toward a towering wall of fog standing on black water, three small figures at the rail seen from behind holding up lanterns, the lanterns drawn as the only white-lined light in the scene, a thin figure in black watching from the stern, open white paper in the lit areas, solid black limited to the deepest shadows, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 2:3 --seed 26576 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, modern clothing
```

**P2 — Arc guide opener** (half page)
File: `scenes/SP-GQ00 — Arc Opener.png`
```
a palisade town on a rise above a wide lake at dusk, seen from far out on the water, and across the whole sky behind it a vast cloud shaped faintly like a grinning skull drifting down from the north, a single small boat with a lantern in the foreground, open white paper in the lit areas, solid black limited to the deepest shadows, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --seed 26576 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, modern clothing
```

---

## B · The Crossing: Scenes (half page, `3:2`)

**P3 — Scene 1: The Post-House**
File: `scenes/SP-GQ00 — S1 Post-House.png`
```
interior of a cramped waterfront post office over a chandler's shop, a grey-haired woman with spectacles on a ribbon stacking oilcloth bundles and a locked black leather letter-case on a wooden counter, a thin girl in a borrowed cloak sitting on a sea-chest by an iron stove reading a pamphlet, ropes and lamps hanging from the beams, daylight through a small window, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --seed 26576 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, modern clothing
```

**P4 — Scene 2: Casting Off**
File: `scenes/SP-GQ00 — S2 Casting Off.png`
```
a broad-bellied lake cog with a carved pike's head on her stem post moored at a timber quay in a stone-built lakeside city, salt sacks stacked to the gunwales, a big broad-shouldered merchant in a fur-trimmed coat waving from the raised stern deck, a thin clerk in black beside him writing in a ledger without looking up, a weathered steersman whittling at the tiller, small students with packs climbing the gangplank seen from behind, noon light, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --seed 26576 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, modern clothing
```

**P5 — Scene 3: The First Night**
File: `scenes/SP-GQ00 — S3 First Night.png`
```
the dim berth-deck of a small cargo ship at night, sleeping figures in hammocks among salt sacks, a thin girl lying awake with her eyes wide open listening, beside her a leather pack whose strap is being lifted by an unseen hand, a trail of small wet clawed footprints on the planks leading away, one shuttered lantern drawn as the only white-lined light, open white paper in the lit areas, solid black limited to the deepest shadows, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --seed 26576 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, modern clothing
```

**P6 — Scene 4: Into the Grey**
File: `scenes/SP-GQ00 — S4 Into the Grey.png`
```
the deck of a becalmed lake cog at night drifting into a wall of fog, the sail hanging slack, a tall rawboned old woman with two long grey braids in a man's oilcloth coat standing at the bow holding a lit lamp in each raised hand, a weathered steersman gripping the tiller behind her, the fog drawn as fine stippling with no outlines, the two lamps drawn as the only white-lined light, open white paper in the lit areas, solid black limited to the deepest shadows, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --seed 26576 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, modern clothing
```

**P7 — Scene 5: The Drowned Come Aboard** (full page option: `--ar 2:3`)
File: `scenes/SP-GQ00 — S5 The Drowned.png`
```
a drowned sailor hauling himself over the rail of a ship out of thick fog, bloated and grey with a rope still knotted round his wrist and water running from his open mouth, another drowned face rising from the black water behind him, in the foreground small adventurers seen from behind thrusting lanterns and a holy symbol toward him, the lanterns drawn as the only white-lined light, open white paper in the lit areas, solid black limited to the deepest shadows, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --seed 26576 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, modern clothing
```

**P8 — Scene 4 (failure branch): The Isle in the Grey**
File: `scenes/SP-GQ00 — S4b Isle in the Grey.png`
```
a low reed-fringed island glimpsed through thick fog from the deck of a grounded ship, a timber lodge among stunted alders with a thin line of smoke rising from its chimney, a sail-sled with runners drawn up under a tarpaulin on the shore, the fog drawn as fine stippling, one lit window drawn as the only white-lined light, open white paper in the lit areas, solid black limited to the deepest shadows, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --seed 26576 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, modern clothing
```

**Scene 6: The Landing** — **reuse** the Ritterstadt Gazetteer's *The Landing* (`99-Assets/Ritterstadt/buildings/Ritterstadt the-landing.jpg`). No new prompt.

---

## C · Portraits (`4:5`)
**Reuse from GQ1** (`99-Assets/SP-SQ/portraits/`): Ottokar Brandmeier, Dawud Vesharan, Snick, Jobst Ruder, Liesl Amsel, Hecht Bargeman, Casimir Vogelsang. **Reuse from the Ritterstadt Gazetteer:** Baba Yeska (`Ritterstadt baba-yeska.jpg`). New:

**P9 — Agnes Feldhaus**
File: `portraits/SP-GQ00 Portrait - Agnes Feldhaus.png`
```
a brisk grey-haired woman of sixty with spectacles hanging on a ribbon, ink and sealing-wax on her fingers, a plain dark dress with a clerk's apron, holding a bundle of letters tied with string, kind but harried expression, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --seed 26576 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing
```

**P10 — Mother Gunde**
File: `portraits/SP-GQ00 Portrait - Mother Gunde.png`
```
a tall rawboned old riverfolk woman of sixty, bareheaded with two long grey braids, a man's oilcloth coat, a brass ring in one ear, burn scars across the backs of her hands, holding a ladle in one fist, shrewd squinting eyes and a set jaw, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --seed 26576 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing
```

**P14 — Ouderling Machteld Vreeswijk** (offstage in GQ0; for her note and GQ3)
File: `portraits/SP-GQ00 Portrait - Machteld Vreeswijk.png`
```
a small very upright old woman of seventy, white hair under a plain black elder's cap, a dark high-collared coat with a long row of small buttons all fastened, holding an ivory rod banded with iron upright before her, thin lips and steady exacting eyes, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --seed 26576 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing
```

---

## D · Plates and Props (PLATE spine)

**P11 — Fog-Drowned** (bestiary plate, `3:4`)
File: `plates/Fog-Drowned.png` (named after the creature note, per the bestiary convention)
```
a drowned sailor risen from a lake, bloated and grey, lank hair plastered to the skull, a rope knotted round one wrist and weed trailing from its belt, water running from its open mouth, reaching forward with both hands, standing on wet planks, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 3:4 [SREF] --seed 26576 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark
```

**P12 — The Chancellor's letter-case** (prop spot, `1:1`)
File: `handouts/SP-GQ00 — Letter-Case.png`
```
a locked black leather letter-case with brass hinge pins and a heavy strap fastened with a large wax seal pressed with an open book over a crossed cudgel and quill, fresh scratches around the brass latch, still life, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 1:1 [SREF] --seed 26576 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark
```

**P13 — Dorakaa silver** (prop spot, `1:1`)
File: `handouts/SP-GQ00 — Dorakaa Silver.png`
```
six thick silver coins spilling out of a rolled wool stocking, each coin stamped with a grinning human skull, one coin standing on its edge, still life, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 1:1 [SREF] --seed 26576 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark
```

---

## E · Maps
**Reuse GQ1's *Graue Hecht* deck maps** (`99-Assets/SP-SQ/maps/SP-GQ01 — Hecht 1–4 — Player.png`; credit Mehujel, Inkarnate). The prologue's ship key (H1–H5) is mapped to them. No new map prompt.

## Checklist
- [ ] P1 Cover (lock as `--sref` if GQ1 has none yet)
- [ ] P2 Arc opener
- [ ] P3 Post-House · [ ] P4 Casting Off · [ ] P5 First Night · [ ] P6 Into the Grey · [ ] P7 The Drowned · [ ] P8 Isle in the Grey
- [ ] P9 Agnes Feldhaus · [ ] P10 Mother Gunde · [ ] P14 Machteld Vreeswijk
- [ ] P11 Fog-Drowned plate · [ ] P12 Letter-case · [ ] P13 Dorakaa silver
- [ ] Density check (25–45% solid black) on every scene before upscaling
- [ ] Cover plaque: add GQ0 to `make_covers.py` (series line "Greyhawk University · The Shadow on the Quag", code GQ0, "An adventure for 1st- and 2nd-level characters")
