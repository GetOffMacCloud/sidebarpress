---
type: art-brief
adventure: "SP-PBS-02"
midjourney_version: "8.1"
seed: 5760
prompt_count: 34
tags: [midjourney, art, prompt-pack, SP-PBS-02]
---

# SP-PBS-02 — Midjourney Prompt Pack (v8.1)

Back to [[SP-PBS-02-The-Bones-of-the-Dreadverge]] · Maps: [[SP-PBS-02 — Map Assets]]

There are 34 prompts in 8 groups. Every prompt ends with `--v 8.1`. Since 24 July 2026, **V8.2 is Midjourney's default**, so a prompt without the flag silently renders in V8.2.

## How This Pack Works

### 1. Style spine (in every prompt)
> `oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish`

- **Aquamarine** is Celene's canon color (see [[The-Common-Year-Calendar]]). It is the only cool accent in the palette.
- The **green fire** at the Three Sisters is the only saturated color. Keep it out of every image except the climax.

### 2. Consistency workflow in V8.1
| Tool | Status in V8.1 | Use it for |
|---|---|---|
| `--sref` + `--sw` | Works, very stable | **Style lock.** Render prompt **A1** first, pick the best image, then paste its URL into every later prompt as `--sref <URL> --sw 300`. |
| `--seed 5760` | Works | Composition stability between rerolls (5760 nods to 576 CY). |
| Anchor phrases | Plain text | **Character lock.** Paste each character's anchor phrase verbatim, word for word, every time. |
| `--cref` / `--cw` | **Not supported** (V6 only) | Do not use. |
| `--oref` / `--ow` | Accepted, **but renders through V7** | Last resort only, when a face must match exactly. Expect a V7 look. |

**Workflow:** render A1 → choose the style anchor → replace `[SREF]` in every prompt with `--sref <A1 URL> --sw 300` → render the character portraits (Group C) → use those portraits as visual references when judging later scenes, keeping the anchor phrases unchanged.

### 3. Standard parameter tail
`--s 250 --seed 5760 --no text, letters, watermark, signature, frame, modern clothing --v 8.1`
Aspect ratios: full page `17:22` (Homebrewery letter) · half page `3:2` · portrait `4:5` · VTT scene `16:9` · token/stamp `1:1`.

### 4. Content guardrails
No gore. Undead are **clean bone and sinew**, never rotting flesh. Captives are seen at a distance or from behind. **Tam is only ever shown from behind or in silhouette.**

---

## Anchor Phrases (paste verbatim)

| Key | Anchor phrase |
|---|---|
| **ASHLOCK** | `a spare soft-spoken man in his fifties, close-cropped grey hair, clean-shaven hollow cheeks, plain undyed grey wool mendicant's robe, ash-grey fingertips` |
| **ASHLOCK-NIGHT** | ASHLOCK + `wearing a crown of dark weathered antler bone, a sickle at his belt` |
| **ODILA** | `a broad-shouldered woman in her late forties, iron-grey braid, ink-stained right forefinger, brown wool dress and apron, silver cloak-pin` |
| **PELL** | `a lanky unshaven young man of nineteen, sandy hair, raw green-tinged chafe mark around his left wrist` |
| **HILD** | `a weathered narrow woman in a grey shawl holding a shepherd's crook taller than she is` |
| **YSOLDE** | `a sunburned woman in her thirties, braid threaded with small tin rings, hammer in her belt` |
| **KETHRA** | `the ancient remains of a bronze-skinned Flan chieftain in rotted leather and amber beads, lying on a stone bier` |
| **HOUND** | `a skeletal wolfhound of yellowed bone strung with black sinew and old leather, green-bronze collar ring cut with a triple spiral` |
| **STAG** | `an enormous skeletal white stag, chalk-pale bones bound with black sinew, antler tines capped in green bronze` |
| **TORC** | `a thick green-bronze torc cut with a triple spiral` |
| **SISTERS** | `a long turf barrow mound crowned by three tall weathered standing stones carved with triple spirals` |

---

## A · Cover & Key Art (3)

- [ ] **A1 — Cover / STYLE ANCHOR** (render first, full page)
```
an enormous skeletal white stag, chalk-pale bones bound with black sinew, antler tines capped in green bronze, standing on a long turf barrow mound crowned by three tall weathered standing stones carved with triple spirals, night heath under a small aquamarine moon, low green ritual fire between the stones, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 17:22 --s 250 --seed 5760 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **A2 — Alternate cover: the pack crossing the heath**
```
a pack of skeletal wolfhounds of yellowed bone strung with black sinew and green-bronze collar rings, loping in single file across black peat heath toward three distant standing stones, low aquamarine moon, wide lonely moorland, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 17:22 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **A3 — Back cover / title band** (wide, leave negative space for type)
```
three tall weathered standing stones on a turf barrow under a vast dusk sky over the Clatspur mountains, empty space in the upper sky, distant hamlet smoke, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```

## B · Locations (7)

- [ ] **B1 — Waycombe at dusk** (Scene 1, half page)
```
a highland hamlet of eleven turf-roofed stone houses and a mill, every shutter closed, a drystone sheep-pound against the wind, ash circles on dark doors, copper dusk light, black heather beyond and mountain ridges, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **B2 — The reeve's kitchen** (Scene 2)
```
a crowded farmhouse kitchen lit by a hearth, a notched tally-stick hanging by the fire, villagers on two benches with untouched bowls, a small girl under the table holding a carved wooden stag, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **B3 — The Dreadverge and the Weeping Beck** (Scene 3)
```
a fast brown moorland stream crossed by flat ford-stones at night, black peat heath and heather on both banks, faint clawed prints lined up at the far water's edge, aquamarine moonlight on the water, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **B4 — The cut-trenches** (Scene 3 set piece)
```
a field of straight peat trenches cut ten feet deep into black earth, stacked turves along the lips like rows of loaves, black water in the trench bottoms, a gnawed turf-spade driven upright into a stack, night, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **B5 — The cutters' camp** (Scene 4)
```
three turf huts around a dead fire, peat-spades leaning in a neat row, sheep and cattle skulls stripped white arranged in a ring all facing the center, a grey robe hanging on a stake in the middle, night, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **B6 — The Three Sisters** (Scene 5 establishing shot, full page)
```
a long turf barrow mound crowned by three tall weathered standing stones carved with triple spirals, the south face cut away to reveal a black stone doorway into the earth, a low green ritual fire between the stones, night heath, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 17:22 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **B7 — The barrow chamber** (Scene 5 interior)
```
the ancient remains of a bronze-skinned Flan chieftain in rotted leather and amber beads, lying on a stone bier in a small round turf-and-stone burial chamber, bronze spear-blades and a boar-tusk helm beside her, a bare hollow at her breast, single shaft of torchlight, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```

## C · Character Portraits (7) · `4:5`

- [ ] **C1 — Brother Ashlock (day)**
```
a spare soft-spoken man in his fifties, close-cropped grey hair, clean-shaven hollow cheeks, plain undyed grey wool mendicant's robe, ash-grey fingertips, kneeling to bless a cottage door with a circle of ash, gentle expression, half-length portrait, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 4:5 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **C2 — Brother Ashlock (night, crowned)**
```
a spare soft-spoken man in his fifties, close-cropped grey hair, clean-shaven hollow cheeks, plain undyed grey wool mendicant's robe, ash-grey fingertips, wearing a crown of dark weathered antler bone, a sickle at his belt, lit from below by a green ritual fire, calm eyes, half-length portrait, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 4:5 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **C3 — Odila Marsh**
```
a broad-shouldered woman in her late forties, iron-grey braid, ink-stained right forefinger, brown wool dress and apron, silver cloak-pin, holding a notched tally-stick by a hearth, guarded expression, half-length portrait, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 4:5 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **C4 — Pell Marsh**
```
a lanky unshaven young man of nineteen, sandy hair, raw green-tinged chafe mark around his left wrist, sitting hunched on a woodpile at dusk, rubbing his wrist, half-length portrait, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 4:5 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **C5 — Hild Brennan**
```
a weathered narrow woman in a grey shawl holding a shepherd's crook taller than she is, standing at a drystone wall watching the dark heath, a longbow hung on the door behind her, half-length portrait, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 4:5 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **C6 — Ysolde the Tinker**
```
a sunburned woman in her thirties, braid threaded with small tin rings, hammer in her belt, leaning on a red-and-yellow painted tinker's cart hung with pans, shrewd half-smile, half-length portrait, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 4:5 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **C7 — Kethra, the Hound-Mother** (bier portrait, top-down)
```
the ancient remains of a bronze-skinned Flan chieftain in rotted leather and amber beads, lying on a stone bier, seen from directly above, the mark of a crown on her brow, hands folded over a bare breast, dignified not grotesque, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 4:5 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, modern clothing, gore --v 8.1
```

## D · Bestiary (6) · `1:1` (bestiary boxes and FG portraits)

- [ ] **D1 — Bone Hound**
```
a skeletal wolfhound of yellowed bone strung with black sinew and old leather, green-bronze collar ring cut with a triple spiral, mid-lope on black heather, empty eye sockets, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 1:1 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, gore, flesh --v 8.1
```
- [ ] **D2 — Bone Boar**
```
a skeletal wild boar of yellowed bone strung with black sinew, green-bronze bands on its tusks, charging along a peat trench causeway, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 1:1 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, gore, flesh --v 8.1
```
- [ ] **D3 — Bone Elk**
```
a skeletal elk of yellowed bone strung with black sinew, green-bronze bands on its antlers, leaping a black peat trench at night, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 1:1 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, gore, flesh --v 8.1
```
- [ ] **D4 — The Barrow Stag**
```
an enormous skeletal white stag, chalk-pale bones bound with black sinew, antler tines capped in green bronze, head lowered to charge, standing beside a black barrow doorway, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 1:1 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, gore, flesh --v 8.1
```
- [ ] **D5 — Risen peat-cutter (zombie)**
```
a shambling dead peat-cutter, peat-black to the elbows, still gripping a turf-spade, a thumbprint of grey ash on his brow, grey face, ragged work clothes, night, unsettling but not gory, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 1:1 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, gore --v 8.1
```
- [ ] **D6 — Corran the foreman (ghoul)**
```
a gaunt hunched ghoul who was once a peat-crew foreman, ash smeared from brow to mouth, long black nails, crouched in a turf hut doorway, eyes catching the light, unsettling but not gory, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 1:1 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, gore --v 8.1
```

## E · Items & Props (4) · `1:1`, `--raw` for clean product-style renders

- [ ] **E1 — Torc of the Hound-Mother**
```
a thick green-bronze torc cut with a triple spiral, resting on folded undyed wool, frost forming around it, still life, oil painting on gessoed board, muted palette of peat brown, bone white and green bronze, visible brushwork, aged varnish --ar 1:1 --raw [SREF] --s 200 --seed 5760 --no text, letters, watermark, signature, frame --v 8.1
```
- [ ] **E2 — Antler Crown of Kethra**
```
a crown of dark weathered antler bone with branching tines, lying on a stone bier beside amber beads, still life, oil painting on gessoed board, muted palette of peat brown, bone white and green bronze, visible brushwork, aged varnish --ar 1:1 --raw [SREF] --s 200 --seed 5760 --no text, letters, watermark, signature, frame --v 8.1
```
- [ ] **E3 — The ash circle**
```
a hand-sized circle of grey ash smeared on an old dark wooden cottage door, iron latch, close-up, oil painting on gessoed board, muted palette of peat brown, heather black and bone white, visible brushwork, aged varnish --ar 1:1 --raw [SREF] --s 200 --seed 5760 --no text, letters, watermark, signature, frame --v 8.1
```
- [ ] **E4 — Bone whistle and sickle** (Ashlock's camp)
```
a whistle carved from a stag's antler tine beside a worn iron sickle and a small jet scythe pendant on a grey wool bedroll, still life by dying firelight, oil painting on gessoed board, muted palette of peat brown, bone white and green bronze, visible brushwork, aged varnish --ar 1:1 --raw [SREF] --s 200 --seed 5760 --no text, letters, watermark, signature, frame --v 8.1
```

## F · Scene Moments (5) · `3:2` page art / `16:9` VTT

- [ ] **F1 — Over the pound wall** (Scene 1)
```
skeletal wolfhounds of yellowed bone with green-bronze collar rings leaping silently over a drystone sheep-pound wall at copper dusk, sheep scattering, a painted tinker's cart nearby, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, gore --v 8.1
```
- [ ] **F2 — The rite at the stones** (Scene 5, VTT splash)
```
a spare man in a plain grey robe wearing a crown of dark antler bone chanting over a low green fire between three tall standing stones, distant bound figures against the stones, skeletal hounds circling the mound below, aquamarine moon, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 16:9 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, gore --v 8.1
```
- [ ] **F3 — The torc returned** (Scene 5 payoff)
```
a hand laying a thick green-bronze torc into the hollow at the throat of ancient remains on a stone bier, the torc beginning to glow faintly warm, dark burial chamber, intimate close view, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, gore --v 8.1
```
- [ ] **F4 — The boy at the barrow mouth** (silhouette only)
```
a small child seen from behind in silhouette, standing very still at a black stone doorway cut into a turf mound, green firelight behind him, three standing stones above, quiet and eerie, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, gore, face --v 8.1
```
- [ ] **F5 — Dawn at Waycombe** (denouement)
```
a highland hamlet at grey dawn, smoke standing straight up from every chimney, a woman at a drystone sheep-pound counting sheep, weary figures walking down from the heath, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, soft grey dawn light, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame --v 8.1
```

## G · VTT Stamps (2) · Inkarnate custom stamps
These use the vtt-build cut-out formula, adapted for v8.1. Remove the background to a transparent PNG before uploading.

- [ ] **G1 — Standing stone + turf stack**
```
top-down orthographic view of a weathered standing stone carved with a triple spiral and a stack of cut peat turves, folk-horror battlemap prop, isolated on plain flat white background, no cast shadow, even lighting, highly detailed --ar 1:1 --raw --s 200 --seed 5760 --v 8.1
```
- [ ] **G2 — Green ritual fire** (black background so the glow survives the cut-out)
```
top-down orthographic view of a small low ritual fire burning eerie green on a ring of stones, folk-horror battlemap prop, isolated on plain flat black background, no cast shadow, highly detailed --ar 1:1 --raw --s 200 --seed 5760 --v 8.1
```

---

## Placement Map (where each image goes)

| Image | Homebrewery / print | Fantasy Grounds |
|---|---|---|
| A1 / A2 | Cover (pick one) | Module splash |
| A3 | Back cover / title band | — |
| B1, B2 | Act 1 opener | Story entries Scenes 1–2 |
| B3, B4 | Act 2 opener | Story entry Scene 3 |
| B5 | Scene 4 | Story entry Scene 4 |
| B6, B7 | Act 3 opener | Story entry Scene 5 |
| C1–C7 | NPC sidebars | NPC portraits |
| D1–D6 | Bestiary statblock boxes | Creature portraits / tokens |
| E1–E4 | Item sidebars; E3 handout corner | Item records |
| F1–F5 | Half-page scene art | Player handout images (share F1, F5) |
| G1, G2 | — | Inkarnate stamps for map rebuilds |

## Export Notes
- Save finals to `99-Assets/SP-PBS-02/art/` with the prompt ID in the filename (e.g. `SP-PBS-02 - C2 Ashlock night.png`).
- For print, upscale and target 300 dpi at final size: full page 8.5×11 in = 2550×3300 px. Convert to CMYK in layout. That fixes the RGB/96-dpi print issues found in earlier audits.
- Record the chosen A1 URL here once it is picked: `STYLE ANCHOR URL: ______________________`
