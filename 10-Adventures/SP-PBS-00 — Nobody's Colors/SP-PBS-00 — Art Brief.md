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

> [!warning] Production file. Never paste into the brew.

Ported from the A Tourist In Greyhawk draft's `0008 - Midjourney Prompts`. The seed is kept so any renders already made still match.

**Module seed:** `--seed 20008` — reuse it on every prompt so faces, palette and light stay consistent across the module.
**Version:** `--v 8.1` throughout.

> [!note] The `vtt-build` skill's stamp formula still says `--v 7`. The standing instruction is `--v 8.1`, used throughout here.

---

## Style anchor

Paste this into every prompt. It is what makes the module look like one book.

> *fourteenth-century Alpine, slate grey and cream plaster, undyed grey wool and oxblood-and-black clan bands, muted ochre and moss palette, overcast northern light, oil on panel, restrained and unromantic*

**The visual thesis: grey.** The Halbritters may wear only undyed cloth by dress-law. Every clan in the module has color; this family has none. Keep them grey in every frame they appear in, and keep the clan pavilions saturated around them. That contrast *is* the adventure.

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

---

## 1 — Front cover

```
A grey mare standing alone in a lantern-lit stable row at night, forty stalls receding into darkness behind her, a young man in undyed grey wool standing at her shoulder with his hand flat on her neck, racing silks in dead green folded over the stall rail beside them, fourteenth-century Alpine, slate grey and cream plaster, muted ochre and moss palette, warm lantern light against cold blue dark, oil on panel, restrained and unromantic, no text --ar 2:3 --v 8.1 --style raw --seed 20008
```

Second option, wider and colder — the arrival rather than the secret:

```
A lake harbor at dawn in the fourteenth-century Alps, a fat single-masted cog tied at a stone quay, a covered wagon at the head of the gangway, mountains grey behind, flat grey-green water filling the horizon, three travelers in worn road clothes standing apart from one another, overcast northern light, oil on panel, muted palette, no text --ar 2:3 --v 8.1 --style raw --seed 20008
```

---

## 2 — Column art, 8 × 24 cm

Tall and narrow. **Compose for the shape** — never render wide and scale down.

**Chapter opener — the doorpost:**
```
Extreme vertical composition, a weathered timber doorpost seen straight on, bare and scrubbed pale by rain, no painted clan band on it, neighboring doorposts visible at the edges carrying bold red-over-black and blue-over-white painted bands, slate and cream plaster wall, overcast light, fourteenth-century Alpine, oil on panel, muted palette --ar 1:3 --v 8.1 --style raw --seed 20008
```

**Appendix opener — the silks:**
```
Extreme vertical composition, a set of racing silks in faded dead green hanging alone on a peg against a plaster wall, dust on the shoulders, a wax seal and folded paper on a shelf beneath, single shaft of cold daylight, fourteenth-century Alpine, oil on panel, muted ochre and moss palette, melancholy --ar 1:3 --v 8.1 --style raw --seed 20008
```

---

## 3 — Scene art

**Aerden (Scene 0):**
```
A small Alpine market town of grey slate and cream plaster below meadow and mountains, every doorpost painted with a colored band at shoulder height, milk carts in the square before dawn, straw archery targets on the green, no walls and no castle, fourteenth century, overcast northern light, oil on panel --ar 16:6 --v 8.1 --style raw --seed 20008
```

**The Erlen bridge (Scene 2):**
```
A narrow stone toll bridge over a slow river, fifty cattle strung along the road behind it, drovers in red and black standing across the span, a covered wagon halted, a small toll house at the near end, morning, fourteenth-century Alpine, overcast light, oil on panel, muted palette, tense but bloodless --ar 16:6 --v 8.1 --style raw --seed 20008
```

**The Rhennee (Scene 4):**
```
Three long low barges with lantern-light strung along their awnings, gliding alongside a single-masted lake cog at dusk, forty feet of black water between them, a woman standing at the barge rail looking across, grey fog on the far horizon, fourteenth-century, oil on panel, cold blue dusk against warm lantern gold --ar 16:6 --v 8.1 --style raw --seed 20008
```

**The Duffkyyn Flats (Scene 5):**
```
A great race meeting outside a fourteenth-century Alpine walled town, striped clan pavilions in red-black, blue-white and dark green, cook-fires, a sale ring, crowds, a long green racecourse beyond, a stone town with a clock tower behind, overcast bright, oil on panel, busy and saturated --ar 16:6 --v 8.1 --style raw --seed 20008
```

**The stable rows (Scene 6):**
```
A long timber stable gallery at night, forty stalls under one roof, a narrow central aisle, a hanging lantern every twenty feet, horses shifting in the dark, one lantern lifted off its hook far down the row, straw and shadow, fourteenth-century, oil on panel, warm light and deep dark, threatening --ar 16:6 --v 8.1 --style raw --seed 20008
```

**Post time (Scene 7):**
```
A young woman in faded green racing silks being legged up onto a grey mare in a stable row, a young man in grey wool standing beside them with empty hands, an old man watching from the end of the row, twenty minutes before a race, fourteenth-century Alpine, overcast daylight, oil on panel, quiet and charged --ar 4:3 --v 8.1 --style raw --seed 20008
```

---

## 4 — NPC portraits

All at `--ar 3:4`. Append to each:
`fourteenth-century Alpine, oil on panel portrait, muted palette, overcast light, plain background, unsmiling, no armor --v 8.1 --style raw --seed 20008`

| NPC | Prompt body |
|---|---|
| **Corwin Halbritter** | A nineteen-year-old man in undyed grey wool, well-made but plain clothes, dark hair, an expression caught between bravado and fear, hands that have done a little work but not much |
| **Adalinde Halbritter** | A woman of twenty-four in a grey riding coat, hair tied back hard, weather on her face, holding a bucket, looking directly at the viewer without expression, entirely unimpressed |
| **Otwin Halbritter** | A grey-faced man in his sixties seated with a ledger open on his knees, gout-swollen hands, undyed grey wool, tired and exact, not unkind |
| **Hessel Amtmann** | A soldier in his forties in a plain grey house-guard's jerkin with no clan band on the sleeve, looking slightly away from the viewer, guilty and trying not to be |
| **Sivert Vuurzward** | A prosperous man of fifty in very dark green wool with a fur collar, holding his hat in both hands, courteous and entirely untroubled, the calmest man in the room |
| **Anse Krul** | A thin, plain farrier in his thirties in working leather, a hoof knife in his hand held like a craftsman's tool, no menace at all in his face, which is worse |
| **Boedic of the Meerijder** | A weathered drover in his fifties in red and black, holding a folded paper he would rather not be holding, apologetic, immovable |
| **Alric Roodberg** | A precise clerk of sixty in blue and white with a heavy register under one arm, spectacles, a man who loves a rulebook |
| **Marda Vosk** | A lake captain in her forties in oiled wool, short grey hair, weighing you up and pricing you, faint amusement |
| **Grete Haslau** | An innkeeper in her fifties, widow's dress, a foreign soldier's coin on a cord at her throat, chalk in one hand, refusing to be thanked |

---

## 5 — Handout: the notice

Not a Midjourney job — this wants clean type on a texture. If you generate the paper:

```
A sheet of good fourteenth-century laid paper pinned to a dark timber post, blank, a plain red wax seal at the lower right with no device or crest impressed in it, lantern light from the left, slightly cockled, photographed straight on --ar 3:4 --v 8.1 --style raw --seed 20008
```

**The seal must be blank.** That is the whole joke: a family with no clan has no device to press. Set the notice text over it afterward.

---

## 6 — Custom map stamps, if needed

Per the house formula, with the version corrected:

```
top-down orthographic view of [subject], [details], fourteenth-century Alpine battlemap prop, isolated on plain flat white background, no cast shadow, even lighting, highly detailed --ar 1:1 --v 8.1 --stylize 200 --seed 20008
```

Likely needs: a deck stall with canvas roof · a pitchfork rack and water butt · stone bridge sections · a drover's cart · hanging stable lanterns.

Use a **black** background instead of white for anything meant to glow, so luminosity survives the cutout. Remove the background to transparent PNG before upload or you paste a white box.

---

## Shot list

- [ ] Front cover
- [ ] Column art ×2 — chapter opener, appendix opener
- [ ] Scene art ×6
- [ ] NPC portraits ×10 *(minimum: Corwin, Adalinde, Otwin, Vuurzward — the four who carry the story)*
- [ ] Notice handout paper
- [ ] Custom stamps, as the maps require
- [ ] All images rehosted off Discord and sized in `cm`
