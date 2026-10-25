---
type: art-brief
adventure: "SP-PBS-02"
section: internal
publish_order: 0
publish: false
midjourney_version: "8.1"
seed: 5760
prompt_count: 34
tags: [midjourney, art, prompt-pack, SP-PBS-02]
---

# SP-PBS-02 — Midjourney Prompt Pack (v8.1)

Back to [[SP-PBS-02-The-Bones-of-the-Dreadverge]] · Maps: [[SP-PBS-02 — Map Assets]]

Converted to the house black-and-white ink style, 2026-10-24 (see [[Art-Style-Guide]]).

There are 34 prompts in 8 groups. Every print prompt uses the house black-and-white pen-and-ink look; F2 (a 16:9 VTT splash) and the G stamps are screen-only and keep their original style. Every prompt ends with `--v 8.1`. Since 24 July 2026, **V8.2 is Midjourney's default**, so a prompt without the flag silently renders in V8.2.

## How This Pack Works

### 1. Style spines (black-and-white ink; in every print prompt)
Every print prompt is **subject + spine + parameter tail**. The spines below are pasted verbatim from [[Art-Style-Guide]] and already sit in each prompt. No color and no grey wash: every value is pure black or pure white, and midtones come from hatching, stippling and pattern.

- **SCENE**: covers (A), locations (B), scene moments (F). `--ar 17:22` or `3:2`.
> `classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art`
- **PORTRAIT**: character portraits (C). `--ar 4:5`.
> `classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art`
- **PLATE**: bestiary (D) and items & props (E), all at `--ar 1:1`.
> `classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm`

**Color notes, translated to ink:**
- **Celene's moonlight.** Aquamarine is Celene's canon color (see [[The-Common-Year-Calendar]]). In ink it becomes `cold white moonlight in long white-line rays across the solid black`, scratched into the black of night scenes (A2, B3, B4, B5). It is still the only cool accent in the pack.
- **The ritual fire** at the Three Sisters was the only saturated color. It becomes `a low ritual fire drawn as the single brilliant white-lined light in an otherwise solid-black scene`. Keep it out of every image except the climax (A1, B6, F4, and C2 as the light from below). Climax images carry no moon, so the fire is the only light in them.
- The old palette translates as: green bronze → `dark stippled bronze`; yellowed bone → `weathered, finely hatched bone`; the Barrow Stag's chalk-pale bones stay plain unhatched white so it stands apart from the hounds; peat and heather → solid black; bone white → bare white paper. Tamsin's red-and-yellow cart becomes bold black-and-white chevrons.

### 2. Consistency workflow in V8.1
| Tool | Status in V8.1 | Use it for |
|---|---|---|
| `--sref` + `--sw` | Works, very stable | **Style lock.** Render prompt **A1** first, pick the best image, then paste its URL into every later prompt as `--sref <URL> --sw 300`. |
| `--seed 5760` | Works | Composition stability between rerolls (5760 nods to 576 CY). |
| Anchor phrases | Plain text | **Character lock.** Paste each character's anchor phrase verbatim, word for word, every time. |
| `--cref` / `--cw` | **Not supported** (V6 only) | Do not use. |
| `--oref` / `--ow` | Accepted, **but renders through V7** | Last resort only, when a face must match exactly. Expect a V7 look. |

**Workflow:** render A1 → choose the style anchor (our own render only: never use the samples in `99-Assets/_Style-Reference/` as `--sref`, they're other people's copyrighted art) → replace `[SREF]` in every prompt with `--sref <A1 URL> --sw 300` → render the character portraits (Group C) → use those portraits as visual references when judging later scenes, keeping the anchor phrases unchanged.

### 3. Standard parameter tail
`[SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1`
This is the [[Art-Style-Guide]] tail plus the pack's seed, `[SREF]`, and the pack's own `--no` extras (`frame`, `modern clothing`, and `gore`, `flesh` or `face` where a prompt needs them). `--style raw --stylize 75` replaces the old `--s 250` / `--raw` and keeps Midjourney from smoothing the hand-drawn line into digital gloss. `--v 8.1` stays last. A1 takes no `[SREF]` (it *is* the anchor).
Aspect ratios: full page `17:22` (Homebrewery letter) · half page `3:2` · portrait `4:5` · bestiary and props `1:1` · VTT scene `16:9` and token/stamp `1:1` (screen-only, original style).

### 4. Content guardrails
No gore. Undead are **clean bone and sinew**, never rotting flesh. Captives are seen at a distance or from behind. **Tam is only ever shown from behind or in silhouette.**

---

## Anchor Phrases (paste verbatim)

| Key | Anchor phrase |
|---|---|
| **ASHLOCK** | `a spare soft-spoken man in his fifties, close-cropped grey hair, clean-shaven hollow cheeks, plain undyed pale wool mendicant's robe, ash-smudged fingertips` |
| **ASHLOCK-NIGHT** | ASHLOCK + `wearing a crown of dark weathered antler bone, a sickle at his belt` |
| **ODILA** | `a broad-shouldered woman in her late forties, iron-grey braid, ink-stained right forefinger, dark hatched wool dress and plain white apron, silver cloak-pin` |
| **KESTER** | `a lanky unshaven young man of nineteen, fair hair, raw dark-stippled chafe mark around his left wrist` |
| **HILD** | `a weathered narrow woman in a pale shawl holding a shepherd's crook taller than she is` |
| **TAMSIN** | `a sunburned woman in her thirties, braid threaded with small tin rings, hammer in her belt` |
| **KETHRA** | `the ancient remains of a dark-skinned Flan chieftain in rotted leather and amber beads, lying on a stone bier` |
| **HOUND** | `a skeletal wolfhound of weathered, finely hatched bone strung with black sinew and old leather, dark stippled bronze collar ring cut with a triple spiral` |
| **STAG** | `an enormous skeletal white stag, chalk-pale bones left plain unhatched white, bound with black sinew, antler tines capped in dark stippled bronze` |
| **TORC** | `a thick dark stippled bronze torc cut with a triple spiral` |
| **SISTERS** | `a long turf barrow mound crowned by three tall weathered standing stones carved with triple spirals` |
| **MOONLIGHT** | `cold white moonlight in long white-line rays across the solid black` (Celene's light, was aquamarine; night scenes only, never in a climax image) |
| **RITUAL-FIRE** | `a low ritual fire drawn as the single brilliant white-lined light in an otherwise solid-black scene` (was the green fire; climax images only: A1, B6, F4, and as the light from below in C2) |

---

## A · Cover & Key Art (3)

- [ ] **A1 — Cover / STYLE ANCHOR** (render first, full page)
```
an enormous skeletal white stag, chalk-pale bones left plain unhatched white, bound with black sinew, antler tines capped in dark stippled bronze, standing on a long turf barrow mound crowned by three tall weathered standing stones carved with triple spirals, moonless night heath, a low ritual fire drawn as the single brilliant white-lined light in an otherwise solid-black scene, burning between the stones, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 17:22 --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **A2 — Alternate cover: the pack crossing the heath**
```
a pack of skeletal wolfhounds of weathered, finely hatched bone strung with black sinew and dark stippled bronze collar rings, loping in single file across solid black peat heath toward three distant standing stones, a low small white moon, cold white moonlight in long white-line rays across the solid black, wide lonely moorland, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 17:22 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **A3 — Back cover / title band** (wide, leave negative space for type)
```
three tall weathered standing stones on a turf barrow under a vast dusk sky over the Clatspur mountains, empty plain white space in the upper sky, distant hamlet smoke, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```

## B · Locations (7)

- [ ] **B1 — Waycombe at dusk** (Scene 1, half page)
```
a highland hamlet of eleven turf-roofed stone houses and a mill, every shutter closed, a drystone sheep-pound against the wind, pale ash circles on solid black doors, low hard dusk light, black heather beyond and mountain ridges, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **B2 — The reeve's kitchen** (Scene 2)
```
a crowded farmhouse kitchen lit by a hearth, a notched tally-stick hanging by the fire, villagers on two benches with untouched bowls, a small girl under the table holding a carved wooden stag, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **B3 — The Dreadverge and the Weeping Beck** (Scene 3)
```
a fast dark moorland stream crossed by flat ford-stones at night, black peat heath and heather on both banks, faint clawed prints lined up at the far water's edge, cold white moonlight in long white-line rays across the solid black, glinting white on the water, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **B4 — The cut-trenches** (Scene 3 set piece)
```
a field of straight peat trenches cut ten feet deep into black earth, stacked turves along the lips like rows of loaves, black water in the trench bottoms, a gnawed turf-spade driven upright into a stack, night, cold white moonlight in long white-line rays across the solid black, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **B5 — The cutters' camp** (Scene 4)
```
three turf huts around a dead fire, peat-spades leaning in a neat row, sheep and cattle skulls stripped white arranged in a ring all facing the center, a pale mendicant's robe hanging on a stake in the middle, night, cold white moonlight in long white-line rays across the solid black, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **B6 — The Three Sisters** (Scene 5 establishing shot, full page)
```
a long turf barrow mound crowned by three tall weathered standing stones carved with triple spirals, the south face cut away to reveal a solid black stone doorway into the earth, a low ritual fire drawn as the single brilliant white-lined light in an otherwise solid-black scene, burning between the stones, night heath, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 17:22 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **B7 — The barrow chamber** (Scene 5 interior)
```
the ancient remains of a dark-skinned Flan chieftain in rotted leather and amber beads, lying on a stone bier in a small round turf-and-stone burial chamber, bronze spear-blades and a boar-tusk helm beside her, a bare hollow at her breast, single shaft of torchlight, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```

## C · Character Portraits (7) · `4:5`

- [ ] **C1 — Brother Ashlock (day)**
```
a spare soft-spoken man in his fifties, close-cropped grey hair, clean-shaven hollow cheeks, plain undyed pale wool mendicant's robe, ash-smudged fingertips, kneeling to bless a cottage door with a circle of ash, gentle expression, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **C2 — Brother Ashlock (night, crowned)**
```
a spare soft-spoken man in his fifties, close-cropped grey hair, clean-shaven hollow cheeks, plain undyed pale wool mendicant's robe, ash-smudged fingertips, wearing a crown of dark weathered antler bone, a sickle at his belt, lit from below by the ritual fire, his face picked out in brilliant white lines against solid black shadow, calm eyes, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **C3 — Odila Marsh**
```
a broad-shouldered woman in her late forties, iron-grey braid, ink-stained right forefinger, dark hatched wool dress and plain white apron, silver cloak-pin, holding a notched tally-stick by a hearth, guarded expression, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **C4 — Kester Marsh**
```
a lanky unshaven young man of nineteen, fair hair, raw dark-stippled chafe mark around his left wrist, sitting hunched on a woodpile at dusk, rubbing his wrist, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **C5 — Hild Brennan**
```
a weathered narrow woman in a pale shawl holding a shepherd's crook taller than she is, standing at a drystone wall watching the dark heath, a longbow hung on the door behind her, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **C6 — Tamsin the Tinker**
```
a sunburned woman in her thirties, braid threaded with small tin rings, hammer in her belt, leaning on a tinker's cart painted in bold black-and-white chevrons and bands, hung with pans, shrewd half-smile, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **C7 — Kethra, the Hound-Mother** (bier portrait, top-down)
```
the ancient remains of a dark-skinned Flan chieftain in rotted leather and amber beads, lying on a stone bier, seen from directly above, the mark of a crown on her brow, hands folded over a bare breast, dignified not grotesque, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing, gore --v 8.1
```

## D · Bestiary (6) · `1:1` (bestiary boxes and FG portraits)

- [ ] **D1 — Bone Hound**
```
a skeletal wolfhound of weathered, finely hatched bone strung with black sinew and old leather, dark stippled bronze collar ring cut with a triple spiral, empty eye sockets, mid-lope over a tuft of black heather, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 1:1 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, gore, flesh --v 8.1
```
- [ ] **D2 — Bone Boar**
```
a skeletal wild boar of weathered, finely hatched bone strung with black sinew, dark stippled bronze bands on its tusks, charging along a peat trench causeway, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 1:1 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, gore, flesh --v 8.1
```
- [ ] **D3 — Bone Elk**
```
a skeletal elk of weathered, finely hatched bone strung with black sinew, dark stippled bronze bands on its antlers, leaping a narrow black peat trench, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 1:1 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, gore, flesh --v 8.1
```
- [ ] **D4 — The Barrow Stag**
```
an enormous skeletal white stag, chalk-pale bones left plain unhatched white, bound with black sinew, antler tines capped in dark stippled bronze, head lowered to charge, standing beside a solid black barrow doorway, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 1:1 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, gore, flesh --v 8.1
```
- [ ] **D5 — Risen peat-cutter (zombie)**
```
a shambling dead peat-cutter, peat-black to the elbows, still gripping a turf-spade, a thumbprint of pale ash on his brow, pallid stippled face, ragged work clothes, unsettling but not gory, standing on cut turf, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 1:1 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, gore --v 8.1
```
- [ ] **D6 — Corran the foreman (ghoul)**
```
a gaunt hunched ghoul who was once a peat-crew foreman, ash smeared from brow to mouth, long black nails, eyes catching the light, unsettling but not gory, crouched in a turf hut doorway, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 1:1 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, gore --v 8.1
```

## E · Items & Props (4) · `1:1`, PLATE spine

- [ ] **E1 — Torc of the Hound-Mother**
```
a thick dark stippled bronze torc cut with a triple spiral, resting on folded undyed wool, frost forming around it in fine white lines, still life, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 1:1 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame --v 8.1
```
- [ ] **E2 — Antler Crown of Kethra**
```
a crown of dark weathered antler bone with branching tines, lying on a stone bier beside amber beads, still life, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 1:1 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame --v 8.1
```
- [ ] **E3 — The ash circle**
```
a hand-sized circle of pale stippled ash smeared on an old solid black wooden cottage door, iron latch, close-up, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 1:1 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame --v 8.1
```
- [ ] **E4 — Bone whistle and sickle** (Ashlock's camp)
```
a whistle carved from a stag's antler tine beside a worn iron sickle and a small solid black jet scythe pendant on a pale wool bedroll, still life by dying firelight, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 1:1 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame --v 8.1
```

## F · Scene Moments (5) · `3:2` page art (SCENE spine) / `16:9` VTT (screen-only)

- [ ] **F1 — Over the pound wall** (Scene 1)
```
skeletal wolfhounds of weathered, finely hatched bone with dark stippled bronze collar rings leaping silently over a drystone sheep-pound wall at low hard dusk, sheep scattering, a tinker's cart painted in bold black-and-white chevrons nearby, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, gore --v 8.1
```
- [ ] **F2 — The rite at the stones** (Scene 5, VTT splash)
  *Screen-only 16:9 VTT splash: deliberately left in its original painted style (not converted). Don't print it as-is, and don't feed it the black-and-white A1 as `--sref` (it would turn it black and white); render it without `[SREF]` or with a painted reference of its own.*
```
a spare man in a plain grey robe wearing a crown of dark antler bone chanting over a low green fire between three tall standing stones, distant bound figures against the stones, skeletal hounds circling the mound below, aquamarine moon, oil painting on gessoed board, folk-horror old-master chiaroscuro, muted palette of peat brown, heather black, bone white and green bronze, cold aquamarine moonlight, visible brushwork, aged varnish --ar 16:9 [SREF] --s 250 --seed 5760 --no text, letters, watermark, signature, frame, gore --v 8.1
```
- [ ] **F3 — The torc returned** (Scene 5 payoff)
```
a hand laying a thick dark stippled bronze torc into the hollow at the throat of ancient remains on a stone bier, the torc beginning to glow faintly in fine white radiating lines, dark burial chamber, intimate close view, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, gore --v 8.1
```
- [ ] **F4 — The boy at the barrow mouth** (silhouette only)
```
a small child seen from behind in silhouette, standing very still at a solid black stone doorway cut into a turf mound, backlit by a low ritual fire drawn as the single brilliant white-lined light in an otherwise solid-black scene, three standing stones above, quiet and eerie, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, gore, face --v 8.1
```
- [ ] **F5 — Dawn at Waycombe** (denouement)
```
a highland hamlet at pale dawn, smoke standing straight up from every chimney, a woman at a drystone sheep-pound counting sheep, weary figures walking down from the heath, soft pale dawn light, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --style raw --stylize 75 --seed 5760 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame --v 8.1
```

## G · VTT Stamps (2) · Inkarnate custom stamps
Screen-only: these stay in their own style and are **not** converted to black and white (see [[Art-Style-Guide]], Out of scope). These use the vtt-build cut-out formula, adapted for v8.1. Remove the background to a transparent PNG before uploading.

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
| F1–F5 | Half-page scene art: F1, F3–F5 (F2 is a screen-only VTT splash in the old painted style; not for print as-is) | Player handout images (share F1, F5) |
| G1, G2 | — | Inkarnate stamps for map rebuilds (screen-only, original style) |

Every print image is black-and-white ink and goes through the 1-bit print step below before layout. FGU portraits and tokens use the same black-and-white finals.

## Export Notes
- Save finals to `99-Assets/SP-PBS-02/art/` with the prompt ID in the filename (e.g. `SP-PBS-02 - C2 Ashlock night.png`).
- Print (see [[Art-Style-Guide]], Print production): render, upscale 2×, then convert to pure **1-bit black and white at 600 dpi** with a threshold of about 50% (Photoshop/GIMP: Image → Mode → Bitmap, or Threshold; Affinity: Adjustments → Threshold). Clean up stray specks and leave the white white, not transparent. Sizes at 600 dpi: a column-width plate (8 cm) is 1,890 px wide; a full page (17 cm) is 4,015 px wide. No CMYK step: 1-bit art prints as pure black, which also retires the RGB/96-dpi print issues found in earlier audits.
- Screen-only art (F2, G1–G2) skips the 1-bit step and stays in color.
- Record the chosen A1 URL here once it is picked: `STYLE ANCHOR URL: ______________________`
