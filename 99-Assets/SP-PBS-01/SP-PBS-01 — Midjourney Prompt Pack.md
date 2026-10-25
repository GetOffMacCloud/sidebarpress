---
type: art-brief
adventure: "SP-PBS-01"
section: internal
publish_order: 0
publish: false
midjourney_version: "8.1"
seed: 1576
prompt_count: 30
tags: [midjourney, art, prompt-pack, SP-PBS-01]
---

# SP-PBS-01 — Midjourney Prompt Pack (v8.1)

Back to [[SP-PBS-01-The-False-Arrow]] · Maps: [[SP-PBS-01 — Map Assets]]

Converted to the house black-and-white ink style, 2026-10-24 (see [[Art-Style-Guide]]).

There are 30 prompts in 7 groups. Every print prompt uses the house black-and-white pen-and-ink look; B3 (a 16:9 VTT splash) and the G stamps are screen-only and keep their original style. Every prompt ends with `--v 8.1`. V8.2 is Midjourney's default, so a prompt without the flag silently renders in V8.2.

## How This Pack Works

### 1. Style spines (black-and-white ink; in every print prompt)
Every print prompt is **subject + spine + parameter tail**. The spines below are pasted verbatim from [[Art-Style-Guide]] and already sit in each prompt. No color and no grey wash: every value is pure black or pure white, and midtones come from hatching, stippling and pattern.

- **SCENE**: cover (A), locations (B). `--ar 17:22` or `3:2`.
> `classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art`
- **PORTRAIT**: character portraits (C). `--ar 4:5`.
> `classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art`
- **PLATE**: bestiary (D) and items & props (E), all at `--ar 1:1`.
> `classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm`
- **MAP**: printed maps (F). `--ar 3:2`, no `[SREF]`.
> `classic 1970s fantasy role-playing game module map, hand-inked black line cartography on white paper, hatched hills and mountains, stippled marsh, tree symbols, ruled grid, clean labels left blank, high contrast black and white line art`

**Color notes, translated to ink:**
- **The Chakyik pattern.** Tiger orange and old-blood red used to mark the Chakyik (banners, tiger-tail standards, the saber-tooth robe, the pavilion hides). They now become `in bold black tiger-stripe hatching`, the boldest pattern in the pack, so Chakyik gear still jumps out against plain snow, felt and stone. Keep it to the Chakyik.
- **Black steel** is still the only "wrong" material and still marks Iuz's hand in every image it appears in (C2's sword hilt, E1's arrowhead): `solid glossy black steel picked out with thin white highlight lines`. All other steel is drawn with ordinary ruled-line hatching, so the solid gloss reads as wrong.
- The old winter palette translates as: snow → bare white; felt and fur → short-stroke hatching; slate and smoke → hatched or stippled midtones; dusk light → hard shadow and masses of solid black. Grey as a surface color (the false arrow's fletching, Brennin's robes and wax) becomes pale, unhatched white; grey hair stays, since it draws as fine white-line hair.

### 2. Consistency workflow in V8.1
| Tool | Status in V8.1 | Use it for |
|---|---|---|
| `--sref` + `--sw` | Works, very stable | **Style lock.** Render **A1** first, then add `--sref <A1 URL> --sw 300` to every later prompt in place of `[SREF]`. |
| `--seed 1576` | Works | Composition stability between rerolls (Fireseek 576 CY). |
| Anchor phrases | Plain text | **Character lock.** Paste verbatim, every time. |
| `--cref` / `--cw` | **Not supported** (V6 only) | Do not use. |
| `--oref` / `--ow` | Renders through V7 | Last resort only. |

Lock `[SREF]` from our own approved A1 render. Never use the samples in `99-Assets/_Style-Reference/` as `--sref`: they're other people's copyrighted art, for internal study only.

### 3. Standard parameter tail
`[SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1`
This is the [[Art-Style-Guide]] tail plus the pack's seed, `[SREF]`, and the pack's own `--no` extras (`frame`, `modern clothing`, and `gore` where a prompt needs it). `--style raw --stylize 75` replaces the old `--s 250` / `--raw` and keeps Midjourney from smoothing the hand-drawn line into digital gloss. `--v 8.1` stays last. A1 takes no `[SREF]` (it *is* the anchor), and neither do the maps.
Aspect ratios: full page `17:22` · half page `3:2` · portrait `4:5` · bestiary and props `1:1` · maps `3:2` · VTT scene `16:9` and token/stamp `1:1` (screen-only, original style).

### 4. Content guardrails
No gore. The patrol's dead are shown at a distance, frost-covered, faces turned away. The injured boy is never shown.

---

## Anchor Phrases (paste verbatim)

| Key          | Anchor phrase                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CLIGIR**   | `a small elderly Baklunish steppe khan, seventyish, weathered face, eyes like chipped flint, white-streaked beard, saber-tooth tiger fur robe of state in bold black tiger-stripe hatching`             |
| **TEMUR**    | `a powerfully built Baklunish nomad khan of thirty, single warrior braid, tiger-tail standard in bold black tiger-stripe hatching knotted at his belt, a broken pale-fletched arrow tucked in his sash` |
| **SARNAI**   | `an ancient Baklunish shaman woman, one milky blind eye, bone and feather fetishes in grey hair, juniper smoke curling around her`                                  |
| **KEZRIN**   | `a smooth Ekbiri merchant in his forties, oiled beard, too-clean hands, rich southern coat, ingratiating smile that does not reach his eyes`                        |
| **BRENNIN**  | `a kindly Oeridian priest in his sixties, plain pale unhatched robes with a cudgel emblem, worry-worn gentle face`                                                            |
| **HALYA**    | `a sharp woman priest in her thirties, dark hair pulled back, plain travelling robes, watchful eyes`                                                                |
| **BATZORIG** | `a broad young Baklunish rider on a shaggy steppe pony, tiger-tail standard in bold black tiger-stripe hatching tied at his saddle, horn bow`                                                           |
| **STALLION** | `a furious solid black steppe stallion drawn with white detail lines, a scarred muzzle and old rope-burn scars around its neck`                                                                     |
| **YECHA**    | `a squat earth-and-timber walled hill town ringed by hundreds of felt yurts between seven low hills`                                                                |
| **CHAKYIK**  | `in bold black tiger-stripe hatching` (the Chakyik mark: banners, tiger-tail standards, the saber-tooth robe, the pavilion hides; was tiger orange and old-blood red) |
| **BLACK-STEEL** | `solid glossy black steel picked out with thin white highlight lines` (Iuz's hand only; all other steel is ordinary ruled-line hatching) |

---

## A · Cover & Key Art (2)

- [ ] **A1 — Cover / STYLE ANCHOR** (render first, full page)
```
two pale goose-fletched arrows lying side by side on solid black felt before a low throne draped in a saber-tooth tiger fur robe in bold black tiger-stripe hatching, one arrow's pale paint flaking to show dark hatched feather beneath, firelight, tiger skulls on tent poles in shadow behind, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 17:22 --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **A2 — Alternate cover: riders out of the low sun**
```
six Baklunish horse archers on shaggy steppe ponies spread in a crescent across a bare white snowfield, bows half-drawn, riding out of a low winter sun drawn as white rays, tiger-tail standards in bold black tiger-stripe hatching, breath steaming, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 17:22 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```

## B · Locations (8)

- [ ] **B1 — Ritterstadt and Greyhawk University** (Scene 0, half page)
```
a fantasy university town on the northern shore of a vast pale lake, a jumble of stone halls, towers, chapels and dormitories with smoke rising from every chimney, snow-dusted roofs, painted arms of an open book with crossed cudgel and quill over a gatehouse arch, overcast winter morning, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **B2 — The hospice in the pass** (Scene 1)
```
a squat stone mountain hospice in a high snowy pass, frost on the lintels, a chapel bell wrapped in sacking, mules steaming in the yard, a cudgel chalked above the gate, dawn, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **B3 — First sight of Yecha** (Scene 1, VTT splash)
  *Screen-only 16:9 VTT splash: deliberately left in its original painted style (not converted). Don't print it as-is, and don't feed it the black-and-white A1 as `--sref` (it would turn it black and white); render it without `[SREF]` or with a painted reference of its own.*
```
a squat earth-and-timber walled hill town ringed by hundreds of felt yurts between seven low hills, smoke rising straight up in still air, tiger banners, a great striped hide pavilion beside the walls with tiger skulls on poles, mountains behind, cold clear dusk, epic scale, oil painting on gessoed board, old-master chiaroscuro, muted winter palette of snow white, felt brown, slate grey and smoke blue, low violet dusk light, visible brushwork, aged varnish --ar 16:9 [SREF] --s 250 --seed 1576 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **B4 — The great pavilion** (Scene 2, full page)
```
interior of a vast nomad pavilion of hides in bold black tiger-stripe hatching, tiger skins on the floor, tiger skulls ringing the central poles, glowing braziers, a low throne draped in a saber-tooth tiger fur robe in bold black tiger-stripe hatching, armed steppe warriors lining the walls, smoky firelight, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 17:22 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **B5 — The horse lines** (Scene 3)
```
a furious solid black steppe stallion drawn with white detail lines, a scarred muzzle and old rope-burn scars around its neck, alone at a picket along a frozen creek at pale dawn, a hundred shaggy ponies steaming behind, a loosely sketched crowd of nomads with tea bowls, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **B6 — The ravine** (Scene 4)
```
a narrow snow-choked ravine in winter foothills, steep shale sides, a frozen stream, a solid black cleft of a den at the far end, two nomad horsemen waiting on the rim above, hard black shadows, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing, gore --v 8.1
```
- [ ] **B7 — Sarnai's fire** (Scene 6)
```
an ancient Baklunish shaman woman, one milky blind eye, bone and feather fetishes in grey hair, juniper smoke curling around her, feeding a small juniper fire one twig at a time before a felt tent, solid black night sky scratched with tiny white early stars, snow steppe beyond, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 3:2 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **B8 — The war council** (Scene 7, full page)
```
a packed nomad war council inside a huge hide pavilion, dozens of warriors in furs banging spear-butts on the ground, banners in bold black tiger-stripe hatching overhead, a young khan holding a broken arrow high, an old khan on a low throne in a saber-tooth robe in bold black tiger-stripe hatching, firelight, classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art --ar 17:22 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```

## C · Character Portraits (7) · `4:5`

- [ ] **C1 — Ilkhan Cligir**
```
a small elderly Baklunish steppe khan, seventyish, weathered face, eyes like chipped flint, white-streaked beard, saber-tooth tiger fur robe of state in bold black tiger-stripe hatching, seated very still on a low throne, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **C2 — Khan Temur**
```
a powerfully built Baklunish nomad khan of thirty, single warrior braid, tiger-tail standard in bold black tiger-stripe hatching knotted at his belt, a broken pale-fletched arrow tucked in his sash, a sword hilt of solid glossy black steel picked out with thin white highlight lines, defiant grieving expression, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **C3 — Mother Sarnai**
```
an ancient Baklunish shaman woman, one milky blind eye, bone and feather fetishes in grey hair, juniper smoke curling around her, quiet knowing expression, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **C4 — Master Kezrin**
```
a smooth Ekbiri merchant in his forties, oiled beard, too-clean hands, rich southern coat, ingratiating smile that does not reach his eyes, pouring wine by a brazier inside a felt tent, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **C5 — Father Brennin**
```
a kindly Oeridian priest in his sixties, plain pale unhatched robes with a cudgel emblem, worry-worn gentle face, holding a sealed letter in both hands at a snowy gate, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **C6 — Sister Halya**
```
a sharp woman priest in her thirties, dark hair pulled back, plain travelling robes, watchful eyes, standing in a stable doorway holding a plain-sealed letter, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```
- [ ] **C7 — Batzorig**
```
a broad young Baklunish rider on a shaggy steppe pony, tiger-tail standard in bold black tiger-stripe hatching tied at his saddle, horn bow, a hide bundle of weapons hanging from his saddle, hard unsmiling mouth, half-length portrait, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 4:5 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, modern clothing --v 8.1
```

## D · Bestiary (3) · `1:1`

- [ ] **D1 — Winter wolf**
```
a huge white-furred winter wolf, frost breath, pale cunning eyes, circling wide, standing on a patch of snow, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 1:1 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, gore --v 8.1
```
- [ ] **D2 — Saber-toothed tiger**
```
a starving saber-toothed tiger, ribs showing, long fangs, emerging from a solid black rock cleft, crouched to ambush on snowy ground, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 1:1 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame, gore --v 8.1
```
- [ ] **D3 — The black stallion (reward)**
```
a furious solid black steppe stallion drawn with white detail lines, a scarred muzzle and old rope-burn scars around its neck, breath steaming, standing calm on trampled snow beside a single rider, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 1:1 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame --v 8.1
```

## E · Items & Props (5) · `1:1`, PLATE spine

- [ ] **E1 — The false arrow**
```
a pale goose-fletched arrow lying in snow, the pale paint flaking to show dark hatched feather beneath, glue where sinew binding should be, an arrowhead of solid glossy black steel picked out with thin white highlight lines, still life, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 1:1 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame --v 8.1
```
- [ ] **E2 — Tiger-claw token**
```
a large tiger claw pendant on a braided leather cord, scrimshawed with tiny tiger-stripe marks, worn horn and bone, resting on solid black felt, still life, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 1:1 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame --v 8.1
```
- [ ] **E3 — Kezrin's papers**
```
a folded oilskin packet of documents, a letter sealed with solid black wax pressed with a grinning skull, a ledger page of figures, lying on dark felt by a brazier, still life, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 1:1 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame --v 8.1
```
- [ ] **E4 — Halya's sealed letter**
```
a plain folded letter sealed with unmarked wax, no ribbon, held in a gloved hand in a dim stable doorway, snow outside, still life, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 1:1 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame --v 8.1
```
- [ ] **E5 — Brennin's parley letter**
```
a folded letter sealed with pale wax pressed with a cudgel and tied with a pale ribbon, beside a small cask of brandy on a snowy mule pack, still life, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 1:1 [SREF] --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark, frame --v 8.1
```

## F · Maps (2) · `3:2`, MAP spine — **no `[SREF]`**
*Midjourney mangles text: generate unlabeled and add labels yourself.*

- [ ] **F1 — Regional map: the Chakyik steppe** (labels to add: Yecha, Yatil Mountains, Burneal Forest, Dramidj Ocean, Fler river, Ekbir, Perrenland, Wolf Nomad lands, the hospice pass)
```
fantasy regional map viewed top-down, windswept steppe north of a great mountain range, walled town marker at the mountain base, dark forest far west, ocean to the north, wide river east, caravan roads and mountain passes, NO TEXT, NO LABELS, NO WORDS, classic 1970s fantasy role-playing game module map, hand-inked black line cartography on white paper, hatched hills and mountains, stippled marsh, tree symbols, ruled grid, clean labels left blank, high contrast black and white line art --ar 3:2 --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark --v 8.1
```
- [ ] **F2 — Locale map: Yecha** (labels to add: old town walls, great pavilion, horse lines, guest tents, Sarnai's tent, Temur's war camp)
```
fantasy settlement map viewed top-down, a small earth-and-timber walled old town on the highest of seven low hills, hundreds of round yurts around it, a large striped pavilion beside the walls, horse lines along a frozen creek, a torchlit war camp to one side, guest tents, a lone tent set apart, NO TEXT, NO LABELS, NO WORDS, classic 1970s fantasy role-playing game module map, hand-inked black line cartography on white paper, hatched hills and mountains, stippled marsh, tree symbols, ruled grid, clean labels left blank, high contrast black and white line art --ar 3:2 --style raw --stylize 75 --seed 1576 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark --v 8.1
```

## G · VTT Stamps (3) · Inkarnate custom stamps
Screen-only: these stay in their own style and are **not** converted to black and white (see [[Art-Style-Guide]], Out of scope). Remove the background to a transparent PNG before uploading.

- [ ] **G1 — Felt yurt (top-down)**
```
top-down orthographic view of a round felt nomad yurt with a smoke hole and guy-ropes, winter battlemap prop, isolated on plain flat white background, no cast shadow, even lighting, highly detailed --ar 1:1 --raw --s 200 --seed 1576 --v 8.1
```
- [ ] **G2 — Burning yurt** (black background so the glow survives)
```
top-down orthographic view of a round felt nomad yurt burning, orange fire at the seams, battlemap prop, isolated on plain flat black background, no cast shadow, highly detailed --ar 1:1 --raw --s 200 --seed 1576 --v 8.1
```
- [ ] **G3 — Brazier and tiger skins**
```
top-down orthographic view of a glowing iron brazier on a striped tiger skin rug, battlemap prop, isolated on plain flat white background, no cast shadow, even lighting, highly detailed --ar 1:1 --raw --s 200 --seed 1576 --v 8.1
```

---

## Placement Map

| Image | Homebrewery / print | Fantasy Grounds |
|---|---|---|
| A1 / A2 | Cover (pick one) | Module splash |
| B1, B2 | Act 1 opener | Story entries Scenes 0–1 |
| B3, B4 | Scene 2: B4 (B3 is a screen-only VTT splash in the old painted style; not for print as-is) | Story entries Scenes 1–2; share B3 |
| B5, B6 | Act 2 opener / Scene 4 | Story entries Scenes 3–4 |
| B7 | Scene 6 | Story entry Scene 6 |
| B8 | Act 3 opener | Story entry Scene 7 |
| C1–C7 | NPC sidebars | NPC portraits |
| D1–D3 | Bestiary boxes | Creature portraits / tokens |
| E1–E5 | Item sidebars; E4/E5 handout headers; E3 Handout 3 | Item records / handout images |
| F1, F2 | Inside cover / Scene 2 | Player maps (share both) |
| G1–G3 | — | Inkarnate stamps for map rebuilds (screen-only, original style) |

Every print image is black-and-white ink and goes through the 1-bit print step below before layout. FGU portraits and tokens use the same black-and-white finals.

## Export Notes
- Save finals to `99-Assets/SP-PBS-01/art/` with the prompt ID in the filename (e.g. `SP-PBS-01 - C2 Temur.png`).
- Print (see [[Art-Style-Guide]], Print production): render, upscale 2×, then convert to pure **1-bit black and white at 600 dpi** with a threshold of about 50% (Photoshop/GIMP: Image → Mode → Bitmap, or Threshold; Affinity: Adjustments → Threshold). Clean up stray specks and leave the white white, not transparent. Sizes at 600 dpi: a column-width plate (8 cm) is 1,890 px wide; a full page (17 cm) is 4,015 px wide. No CMYK step: 1-bit art prints as pure black.
- Screen-only art (B3, G1–G3) skips the 1-bit step and stays in color.
- Homebrewery: host on Imgur, GitHub raw, or Homebrewery's own upload — **never Discord CDN links** (they expire within a day).
- Record the chosen A1 URL here: `STYLE ANCHOR URL: ______________________`
