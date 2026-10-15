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

There are 30 prompts in 7 groups. Every prompt ends with `--v 8.1`. V8.2 is Midjourney's default, so a prompt without the flag silently renders in V8.2.

## How This Pack Works

### 1. Style spine (in every prompt except maps and stamps)
> `oil painting on gessoed board, old-master chiaroscuro, muted winter palette of snow white, felt brown, slate grey and smoke blue, low violet dusk light, visible brushwork, aged varnish`

- **Tiger orange and old-blood red** (banners, the saber-tooth robe) are the only warm saturated colors. Keep them to the Chakyik.
- **Black steel** is the only "wrong" material: dark, oily, faintly iridescent. It marks Iuz's hand in every image it appears in.

### 2. Consistency workflow in V8.1
| Tool | Status in V8.1 | Use it for |
|---|---|---|
| `--sref` + `--sw` | Works, very stable | **Style lock.** Render **A1** first, then add `--sref <A1 URL> --sw 300` to every later prompt in place of `[SREF]`. |
| `--seed 1576` | Works | Composition stability between rerolls (Fireseek 576 CY). |
| Anchor phrases | Plain text | **Character lock.** Paste verbatim, every time. |
| `--cref` / `--cw` | **Not supported** (V6 only) | Do not use. |
| `--oref` / `--ow` | Renders through V7 | Last resort only. |

### 3. Standard parameter tail
`--s 250 --seed 1576 --no text, letters, watermark, signature, frame, modern clothing --v 8.1`
Aspect ratios: full page `17:22` · half page `3:2` · portrait `4:5` · VTT scene `16:9` · token/stamp `1:1` · maps `3:2`.

### 4. Content guardrails
No gore. The patrol's dead are shown at a distance, frost-covered, faces turned away. The injured boy is never shown.

---

## Anchor Phrases (paste verbatim)

| Key | Anchor phrase |
|---|---|
| **CLIGIR** | `a small elderly Baklunish steppe khan, seventyish, weathered face, eyes like chipped flint, white-streaked beard, saber-tooth tiger fur robe of state` |
| **TEMUR** | `a powerfully built Baklunish nomad khan of thirty, single warrior braid, tiger-tail standard knotted at his belt, a broken grey-fletched arrow tucked in his sash` |
| **SARNAI** | `an ancient Baklunish shaman woman, one milky blind eye, bone and feather fetishes in grey hair, juniper smoke curling around her` |
| **KEZRIN** | `a smooth Ekbiri merchant in his forties, oiled beard, too-clean hands, rich southern coat, ingratiating smile that does not reach his eyes` |
| **BRENNIN** | `a kindly Oeridian priest in his sixties, plain grey robes with a cudgel emblem, worry-worn gentle face` |
| **HALYA** | `a sharp woman priest in her thirties, dark hair pulled back, plain travelling robes, watchful eyes` |
| **BATZORIG** | `a broad young Baklunish rider on a shaggy steppe pony, tiger-tail standard tied at his saddle, horn bow` |
| **STALLION** | `a furious black steppe stallion with a scarred muzzle and old rope-burn scars around its neck` |
| **YECHA** | `a squat earth-and-timber walled hill town ringed by hundreds of felt yurts between seven low hills` |

---

## A · Cover & Key Art (2)

- [ ] **A1 — Cover / STYLE ANCHOR** (render first, full page)
```
two grey goose-fletched arrows lying side by side on red felt before a low throne draped in a saber-tooth tiger fur robe, one arrow's paint flaking to show brown feather beneath, firelight, tiger skulls on tent poles in shadow behind, oil painting on gessoed board, old-master chiaroscuro, muted winter palette of snow white, felt brown, slate grey and smoke blue, low violet dusk light, visible brushwork, aged varnish --ar 17:22 --s 250 --seed 1576 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **A2 — Alternate cover: riders out of the low sun**
```
six Baklunish horse archers on shaggy steppe ponies spread in a crescent across a snowfield, bows half-drawn, riding out of a low winter sun, tiger-tail standards, breath steaming, oil painting on gessoed board, old-master chiaroscuro, muted winter palette of snow white, felt brown, slate grey and smoke blue, low violet dusk light, visible brushwork, aged varnish --ar 17:22 [SREF] --s 250 --seed 1576 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```

## B · Locations (8)

- [ ] **B1 — Ritterstadt and Greyhawk University** (Scene 0, half page)
```
a fantasy university town on the northern shore of a vast grey lake, a jumble of stone halls, towers, chapels and dormitories with smoke rising from every chimney, snow-dusted roofs, painted arms of an open book with crossed cudgel and quill over a gatehouse arch, overcast winter morning, oil painting on gessoed board, old-master chiaroscuro, muted winter palette of snow white, felt brown, slate grey and smoke blue, low violet dusk light, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 1576 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **B2 — The hospice in the pass** (Scene 1)
```
a squat stone mountain hospice in a high snowy pass, frost on the lintels, a chapel bell wrapped in sacking, mules steaming in the yard, a cudgel chalked above the gate, dawn, oil painting on gessoed board, old-master chiaroscuro, muted winter palette of snow white, felt brown, slate grey and smoke blue, low violet dusk light, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 1576 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **B3 — First sight of Yecha** (Scene 1, VTT splash)
```
a squat earth-and-timber walled hill town ringed by hundreds of felt yurts between seven low hills, smoke rising straight up in still air, tiger banners, a great striped hide pavilion beside the walls with tiger skulls on poles, mountains behind, cold clear dusk, epic scale, oil painting on gessoed board, old-master chiaroscuro, muted winter palette of snow white, felt brown, slate grey and smoke blue, low violet dusk light, visible brushwork, aged varnish --ar 16:9 [SREF] --s 250 --seed 1576 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **B4 — The great pavilion** (Scene 2, full page)
```
interior of a vast nomad pavilion of striped hides, tiger skins on the floor, tiger skulls ringing the central poles, glowing braziers, a low throne draped in a saber-tooth tiger fur robe, armed steppe warriors lining the walls, smoky firelight, oil painting on gessoed board, old-master chiaroscuro, muted winter palette of snow white, felt brown, slate grey and smoke blue, low violet dusk light, visible brushwork, aged varnish --ar 17:22 [SREF] --s 250 --seed 1576 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **B5 — The horse lines** (Scene 3)
```
a furious black steppe stallion with a scarred muzzle and old rope-burn scars around its neck, alone at a picket along a frozen creek at grey dawn, a hundred shaggy ponies steaming behind, a blurred crowd of nomads with tea bowls, oil painting on gessoed board, old-master chiaroscuro, muted winter palette of snow white, felt brown, slate grey and smoke blue, low violet dusk light, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 1576 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **B6 — The ravine** (Scene 4)
```
a narrow snow-choked ravine in winter foothills, steep shale sides, a frozen stream, a dark cleft of a den at the far end, two nomad horsemen waiting on the rim above, cold blue shadows, oil painting on gessoed board, old-master chiaroscuro, muted winter palette of snow white, felt brown, slate grey and smoke blue, low violet dusk light, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 1576 --no text, letters, watermark, signature, frame, modern clothing, gore --v 8.1
```
- [ ] **B7 — Sarnai's fire** (Scene 6)
```
an ancient Baklunish shaman woman, one milky blind eye, bone and feather fetishes in grey hair, juniper smoke curling around her, feeding a small juniper fire one twig at a time before a felt tent, violet-black sky with early stars, snow steppe beyond, oil painting on gessoed board, old-master chiaroscuro, muted winter palette of snow white, felt brown, slate grey and smoke blue, low violet dusk light, visible brushwork, aged varnish --ar 3:2 [SREF] --s 250 --seed 1576 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **B8 — The war council** (Scene 7, full page)
```
a packed nomad war council inside a huge hide pavilion, dozens of warriors in furs banging spear-butts on the ground, tiger banners overhead, a young khan holding a broken arrow high, an old khan on a low throne in a saber-tooth robe, firelight, oil painting on gessoed board, old-master chiaroscuro, muted winter palette of snow white, felt brown, slate grey and smoke blue, low violet dusk light, visible brushwork, aged varnish --ar 17:22 [SREF] --s 250 --seed 1576 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```

## C · Character Portraits (7) · `4:5`

- [ ] **C1 — Ilkhan Cligir**
```
a small elderly Baklunish steppe khan, seventyish, weathered face, eyes like chipped flint, white-streaked beard, saber-tooth tiger fur robe of state, seated very still on a low throne, half-length portrait, oil painting on gessoed board, old-master chiaroscuro, muted winter palette of snow white, felt brown, slate grey and smoke blue, low violet dusk light, visible brushwork, aged varnish --ar 4:5 [SREF] --s 250 --seed 1576 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **C2 — Khan Temur**
```
a powerfully built Baklunish nomad khan of thirty, single warrior braid, tiger-tail standard knotted at his belt, a broken grey-fletched arrow tucked in his sash, black-steel sword hilt, defiant grieving expression, half-length portrait, oil painting on gessoed board, old-master chiaroscuro, muted winter palette of snow white, felt brown, slate grey and smoke blue, low violet dusk light, visible brushwork, aged varnish --ar 4:5 [SREF] --s 250 --seed 1576 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **C3 — Mother Sarnai**
```
an ancient Baklunish shaman woman, one milky blind eye, bone and feather fetishes in grey hair, juniper smoke curling around her, quiet knowing expression, half-length portrait, oil painting on gessoed board, old-master chiaroscuro, muted winter palette of snow white, felt brown, slate grey and smoke blue, low violet dusk light, visible brushwork, aged varnish --ar 4:5 [SREF] --s 250 --seed 1576 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **C4 — Master Kezrin**
```
a smooth Ekbiri merchant in his forties, oiled beard, too-clean hands, rich southern coat, ingratiating smile that does not reach his eyes, pouring wine by a brazier inside a felt tent, half-length portrait, oil painting on gessoed board, old-master chiaroscuro, muted winter palette of snow white, felt brown, slate grey and smoke blue, low violet dusk light, visible brushwork, aged varnish --ar 4:5 [SREF] --s 250 --seed 1576 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **C5 — Father Brennin**
```
a kindly Oeridian priest in his sixties, plain grey robes with a cudgel emblem, worry-worn gentle face, holding a sealed letter in both hands at a snowy gate, half-length portrait, oil painting on gessoed board, old-master chiaroscuro, muted winter palette of snow white, felt brown, slate grey and smoke blue, low violet dusk light, visible brushwork, aged varnish --ar 4:5 [SREF] --s 250 --seed 1576 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **C6 — Sister Halya**
```
a sharp woman priest in her thirties, dark hair pulled back, plain travelling robes, watchful eyes, standing in a stable doorway holding a plain-sealed letter, half-length portrait, oil painting on gessoed board, old-master chiaroscuro, muted winter palette of snow white, felt brown, slate grey and smoke blue, low violet dusk light, visible brushwork, aged varnish --ar 4:5 [SREF] --s 250 --seed 1576 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```
- [ ] **C7 — Batzorig**
```
a broad young Baklunish rider on a shaggy steppe pony, tiger-tail standard tied at his saddle, horn bow, a hide bundle of weapons hanging from his saddle, hard unsmiling mouth, half-length portrait, oil painting on gessoed board, old-master chiaroscuro, muted winter palette of snow white, felt brown, slate grey and smoke blue, low violet dusk light, visible brushwork, aged varnish --ar 4:5 [SREF] --s 250 --seed 1576 --no text, letters, watermark, signature, frame, modern clothing --v 8.1
```

## D · Bestiary (3) · `1:1`

- [ ] **D1 — Winter wolf**
```
a huge white-furred winter wolf on a snowfield, frost breath, pale cunning eyes, circling wide, oil painting on gessoed board, old-master chiaroscuro, muted winter palette of snow white, felt brown, slate grey and smoke blue, low violet dusk light, visible brushwork, aged varnish --ar 1:1 [SREF] --s 250 --seed 1576 --no text, letters, watermark, signature, frame, gore --v 8.1
```
- [ ] **D2 — Saber-toothed tiger**
```
a starving saber-toothed tiger emerging from a dark rock cleft in a snowy ravine, ribs showing, long fangs, ambush crouch, oil painting on gessoed board, old-master chiaroscuro, muted winter palette of snow white, felt brown, slate grey and smoke blue, low violet dusk light, visible brushwork, aged varnish --ar 1:1 [SREF] --s 250 --seed 1576 --no text, letters, watermark, signature, frame, gore --v 8.1
```
- [ ] **D3 — The black stallion (reward)**
```
a furious black steppe stallion with a scarred muzzle and old rope-burn scars around its neck, standing calm beside a single rider, breath steaming, oil painting on gessoed board, old-master chiaroscuro, muted winter palette of snow white, felt brown, slate grey and smoke blue, low violet dusk light, visible brushwork, aged varnish --ar 1:1 [SREF] --s 250 --seed 1576 --no text, letters, watermark, signature, frame --v 8.1
```

## E · Items & Props (5) · `1:1`, `--raw`

- [ ] **E1 — The false arrow**
```
a grey goose-fletched arrow lying in snow, the grey paint flaking to show brown feather beneath, glue where sinew binding should be, a dark oily black-steel arrowhead, still life, oil painting on gessoed board, muted winter palette of snow white, slate grey and smoke blue, visible brushwork, aged varnish --ar 1:1 --raw [SREF] --s 200 --seed 1576 --no text, letters, watermark, signature, frame --v 8.1
```
- [ ] **E2 — Tiger-claw token**
```
a large tiger claw pendant on a braided leather cord, scrimshawed with tiny tiger-stripe marks, worn horn and bone, resting on dark felt, still life, oil painting on gessoed board, muted winter palette, visible brushwork, aged varnish --ar 1:1 --raw [SREF] --s 200 --seed 1576 --no text, letters, watermark, signature, frame --v 8.1
```
- [ ] **E3 — Kezrin's papers**
```
a folded oilskin packet of documents, a letter sealed with black wax pressed with a grinning skull, a ledger page of figures, lying on dark felt by a brazier, still life, oil painting on gessoed board, muted winter palette, visible brushwork, aged varnish --ar 1:1 --raw [SREF] --s 200 --seed 1576 --no text, letters, watermark, signature, frame --v 8.1
```
- [ ] **E4 — Halya's sealed letter**
```
a plain folded letter sealed with unmarked wax, no ribbon, held in a gloved hand in a dim stable doorway, snow outside, still life, oil painting on gessoed board, muted winter palette, visible brushwork, aged varnish --ar 1:1 --raw [SREF] --s 200 --seed 1576 --no text, letters, watermark, signature, frame --v 8.1
```
- [ ] **E5 — Brennin's parley letter**
```
a folded letter sealed with grey wax pressed with a cudgel and tied with a grey ribbon, beside a small cask of brandy on a snowy mule pack, still life, oil painting on gessoed board, muted winter palette, visible brushwork, aged varnish --ar 1:1 --raw [SREF] --s 200 --seed 1576 --no text, letters, watermark, signature, frame --v 8.1
```

## F · Maps (2) · `3:2`, parchment style — **no `[SREF]`**
*Midjourney mangles text: generate unlabeled and add labels yourself.*

- [ ] **F1 — Regional map: the Chakyik steppe** (labels to add: Yecha, Yatil Mountains, Burneal Forest, Dramidj Ocean, Fler river, Ekbir, Perrenland, Wolf Nomad lands, the hospice pass)
```
fantasy regional map viewed top-down, windswept steppe north of a great mountain range, walled town marker at the mountain base, dark forest far west, ocean to the north, wide river east, caravan roads and mountain passes, NO TEXT, NO LABELS, NO WORDS, aged parchment, hand-drawn ink and watercolor --ar 3:2 --s 150 --seed 1576 --v 8.1
```
- [ ] **F2 — Locale map: Yecha** (labels to add: old town walls, great pavilion, horse lines, guest tents, Sarnai's tent, Temur's war camp)
```
fantasy settlement map viewed top-down, a small earth-and-timber walled old town on the highest of seven low hills, hundreds of round yurts around it, a large striped pavilion beside the walls, horse lines along a frozen creek, a torchlit war camp to one side, guest tents, a lone tent set apart, NO TEXT, NO LABELS, NO WORDS, aged parchment, hand-drawn ink and watercolor --ar 3:2 --s 150 --seed 1576 --v 8.1
```

## G · VTT Stamps (3) · Inkarnate custom stamps
Remove the background to a transparent PNG before uploading.

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
| B3, B4 | Scene 2 | Story entries Scenes 1–2; share B3 |
| B5, B6 | Act 2 opener / Scene 4 | Story entries Scenes 3–4 |
| B7 | Scene 6 | Story entry Scene 6 |
| B8 | Act 3 opener | Story entry Scene 7 |
| C1–C7 | NPC sidebars | NPC portraits |
| D1–D3 | Bestiary boxes | Creature portraits / tokens |
| E1–E5 | Item sidebars; E4/E5 handout headers; E3 Handout 3 | Item records / handout images |
| F1, F2 | Inside cover / Scene 2 | Player maps (share both) |
| G1–G3 | — | Inkarnate stamps for map rebuilds |

## Export Notes
- Save finals to `99-Assets/SP-PBS-01/art/` with the prompt ID in the filename (e.g. `SP-PBS-01 - C2 Temur.png`).
- Print: upscale to 300 dpi at final size (full page 8.5×11 in = 2550×3300 px); convert to CMYK in layout.
- Homebrewery: host on Imgur, GitHub raw, or Homebrewery's own upload — **never Discord CDN links** (they expire within a day).
- Record the chosen A1 URL here: `STYLE ANCHOR URL: ______________________`
