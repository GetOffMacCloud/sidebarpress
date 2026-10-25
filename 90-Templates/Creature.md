---
type: creature
adventure: "SP-BST-01"
section: bestiary
publish_order: 0 # alphabetical slot, gaps of 10 (see 65-Bestiary/00 — Bestiary Index)
publish: true
status: outline # outline | drafted | edited | final
creature: "{{name}}"
cr: "" # as printed: "1/4", "3"
cr_num: 0 # decimal for sorting: 0.125, 0.25, 0.5, 1, 2…
xp: 0
size: "" # Tiny | Small | Medium | Large | Huge | Gargantuan
creature_type: "" # aberration | beast | celestial | construct | dragon | elemental | fey | fiend | giant | humanoid | monstrosity | ooze | plant | undead
alignment: ""
environment: [] # arctic, coastal, desert, forest, grassland, hill, mountain, swamp, underdark, underwater, urban, farmland, village, ruins, graveyard
origin: "" # harvested | new | remix | folklore | contributed
credit: "" # contributor name, for contributed entries
base_block: "" # e.g. "Commoner (MM p. 345)" or "none"
source_adventures: [] # e.g. ["SP-HAL-01"]
tags: [bestiary, statblock, 2014-5e]
---

# {{name}}

*One line a DM can read aloud when the creature first appears (≤25 words).*

> [!art]+ Plate
> ![[99-Assets/SP-BST-01/plates/{{name}}.png|360]]

> [!example]+ {{name}} (CR X, X XP)
> *Size type, alignment*
> **Armor Class** · **Hit Points** · **Speed**
>
> | STR | DEX | CON | INT | WIS | CHA |
> |---|---|---|---|---|---|
> | 10 (+0) | 10 (+0) | 10 (+0) | 10 (+0) | 10 (+0) | 10 (+0) |
>
> **Saving Throws** · **Skills** · **Damage Vulnerabilities** · **Damage Resistances** · **Damage Immunities** · **Condition Immunities**
> **Senses** · **Languages** · **Challenge** X (X XP)
>
> ***Trait.*** Text.
>
> **Actions**
> ***Action.*** Text.

## Lore
What it is, where it comes from, what people believe about it. Two or three paragraphs.

## Ecology
- **Environment:**
- **Encountered as:** alone / pairs / groups (number appearing by APL)
- **Signs:** what the party finds before they find it

## Tactics
How it fights, what it wants, when it flees or bargains.

## Lair / Regional Effects
Only where it fits. Delete otherwise.

## Named Example
For villain types: the individual from a Sidebar Press adventure, and what is unique to them.

## Adventure Hooks
1.
2.
3.

## Spoils
What the party can take from it, if anything.

## Design Notes
**Changes from the base block:**

**CR verification (DMG p. 274):** defensive CR, offensive CR, average.

## Appears In
- [[SP-XXX-NN-Title]] — scene, role

## Art Prompt
Style: black-and-white ink, per [[Art-Style-Guide]] (PLATE spine). Describe the creature alone with only the ground it stands on, and write colors as ink values or patterns.
```
<subject>, full figure centered with the head and shoulders in the upper middle of the frame and clear space on every side, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 3:4 --v 8.1 --style raw --stylize 75 --seed 26500 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark
```

**Color portrait** (screen only: the FGU portrait and the token-maker source). Full color, light background; see [[Art-Style-Guide#COLOR PORTRAIT — screen only (Greybeard, 2026-10-25)]].
```
<creature in full color>, head and shoulders portrait in three-quarter view, the head in the upper middle of the frame with clear space around it, stylized fantasy tabletop RPG creature portrait, crisp painted digital game art, clean confident linework with painterly cel-like shading, vivid but controlled color, soft rim light, strong readable silhouette, on a soft light cream and warm pale grey background with a gentle vignette --ar 3:4 --v 8.1 --stylize 150 --seed 26500 --no text, letters, signature, watermark, frame, border, dark background, black background
```

## FGU Import
Generated, never hand-written (the generator also adds the FGU Portrait & Token image callout): after the statblock is final, run `python3 70-Company/Tools/fgu_import.py 65-Bestiary` and this section is rebuilt with paste-ready text for FGU's NPCs → Import Text (mode: 2022 – Monsters of the Multiverse).
