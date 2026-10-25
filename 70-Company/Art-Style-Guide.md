---
type: style-guide
section: internal
publish: false
tags: [art, midjourney, house-style]
---

# Sidebar Press — Art Style Guide (house look, from 2026-10-24)

**Ruling (Greybeard, 2026-10-24):** every Midjourney prompt for a Sidebar Press **print** product uses the classic black-and-white ink look of late-1970s and early-1980s fantasy role-playing rulebooks and modules. Our books are home-produced, and full-color art is out of budget. Black line art prints sharp on any printer, costs no more than text, and is the look we want anyway.

Reference samples Greybeard supplied are in `99-Assets/_Style-Reference/`. They're for internal study only. Don't use them as `--sref` or publish them: they're other people's copyrighted art. Lock our own `--sref` from our first approved render instead.

---

## What defines the look
**Medium.** Black India ink on white paper, drawn with pen and brush. No grey wash, no color, no gradients. Every value is pure black or pure white, and midtones come from hatching, stippling, and pattern.

**Mode A: spot creature illustration** (the monster-manual entry)
- One creature on **bare white**, with no background.
- A small **blot of solid black cast shadow** on the ground beneath it.
- A **bold hand-inked contour**, with interior form built from crosshatching on the shadow side and stippling.
- **Texture drawn as pattern:** scales as little loops or cells, fur as short strokes, hide as stipple, and armor as ruled lines.
- Some figures are mostly **solid black silhouette**, with white detail lines drawn into them.
- **Hand-drawn charm.** Character and attitude matter more than anatomical precision; a slightly naive line is right. Creatures usually stand in three-quarter view, facing the reader.

**Mode B: full-page scene** (the module or chapter illustration)
- **Heavy shadow** with large masses of solid black.
- **White lines scratched into the black**, as on scratchboard, in the darkest areas.
- Dense **contour hatching** and crosshatching, with every surface textured: rock, mail, cloth, web.
- **Torchlight** casting hard-edged shadows.
- The monster dominates. Small adventurers stand in the foreground, often seen from behind, looking up at it for scale.
- Often a ruled rectangular border.

**Never:** color, grey wash, airbrush gradients, painterly brushwork, photorealism, 3D rendering, glossy digital polish, lens effects, text, or signatures.

**Don't name artists in prompts.** Describe the technique instead. It's fairer to the artists, and it gives Midjourney a steadier style to follow than a name does.

---

## Spines (paste verbatim)
Each prompt is **subject + composition + spine + parameter tail**.

**PLATE — creature spot illustration** (bestiary entries, NPC and monster spots, items). Use with `--ar 3:4`, or `1:1` for small spots.
> `classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm`

**SCENE — full-page or half-page illustration** (splashes, covers, chapter openers, locations, scene moments). Use with `--ar 2:3`, `17:22`, `3:2`, or `1:3`.
> `classic 1970s fantasy role-playing game module illustration, black ink on white paper, heavy chiaroscuro with large masses of solid black, dense crosshatching and contour hatching, scratchboard-style white line work in the darkest areas, every surface richly textured by hand, hard torchlit shadows, high contrast black and white line art`

**PORTRAIT — character head and shoulders** (NPC portraits). Use with `--ar 4:5`.
> `classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art`

**MAP — printed map** (module maps, not VTT). Use with `--ar 3:2`.
> `classic 1970s fantasy role-playing game module map, hand-inked black line cartography on white paper, hatched hills and mountains, stippled marsh, tree symbols, ruled grid, clean labels left blank, high contrast black and white line art`

**Parameter tail** (every print prompt):
`--v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark`
Add the product's `--seed`, and its `--sref` once locked. `--style raw` and the low `--stylize` keep Midjourney from smoothing the hand-drawn line into digital gloss.

---

## Writing the subject
- **Color words become ink values or patterns.** "Crimson cloak" becomes "dark cloak"; "green fire" becomes "pale flickering fire"; "a red clan band" becomes "a band of bold black-and-white chevrons". Color names that identify a kind of creature (a *red* dragon, a *white* dragon) can stay. Midjourney reads them as species names, and the spine keeps the image black and white.
- **A color contrast becomes a black-and-white contrast.** If a design depends on color (a grey family among bright clans, one glowing thing in a dark scene), translate it: **plain unhatched white** against **busy pattern**, a **solid black mass** against a **white figure**, or the one **white-lined light source** in a black scene.
- **Scenes need scale.** Put a few small adventurers in the foreground, ideally seen from behind.
- **Spots need a ground.** End the subject with the creature standing, so the cast-shadow blot has something to sit on.

## Print production
1. Render, then upscale (2×).
2. Convert to pure **1-bit black and white** at **600 dpi** with a threshold of about 50%. That removes any grey Midjourney sneaks in and makes the lines crisp on a home printer. (In Photoshop or GIMP: Image → Mode → Bitmap, or Threshold. In Affinity: Adjustments → Threshold.)
3. Clean up stray specks. Leave the white **white**, not transparent, unless the image is a token.
4. Sizes at 600 dpi: a column-width plate (8 cm) is 1,890 px wide, and a full page (17 cm) is 4,015 px wide.
5. FGU portraits and tokens work fine in black and white. Your token maker can add a colored ring if you want one on screen.

## Out of scope (screen-only art)
**VTT battlemap props and Inkarnate custom stamps** stay in their own style. They're never printed, color costs nothing on screen, and black-and-white props would look wrong on a color battlemap. **Covers** are black and white by default. An option worth considering is a monochrome cover: black ink printed on colored cardstock, the classic single-color module cover.
