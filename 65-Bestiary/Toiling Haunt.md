---
type: creature
adventure: "SP-BST-01"
section: bestiary
publish_order: 600
publish: true
status: drafted
creature: "Toiling Haunt"
cr: "none"
cr_num: -1
xp: 0
size: Medium
creature_type: undead
alignment: unaligned
environment: [ruins, village, urban]
origin: harvested
base_block: "none (haunt; no statblock)"
source_adventures: ["SP-HAL-02"]
tags: [bestiary, haunt, 2014-5e]
art_plate: todo        # todo | generated | approved | placed
portrait: todo
token: todo
---

# Toiling Haunt

*A woman in a cook's apron kneels by the cask and scrubs it. She has been scrubbing it for fifty years. "Getting the sweet out," she says.*

> [!art]+ Plate
> ![[99-Assets/SP-BST-01/plates/Toiling Haunt.png|360]]

> [!example]+ Toiling Haunt (haunt, no CR)
> *Medium undead (haunt), unaligned*
> A toiling haunt is not a creature that can be fought. It is a piece of unfinished work that has outlasted its worker.
>
> **Detection** *Detect evil and good* registers it as undead. *Detect magic* shows a faint necromantic aura on the object it works at.
> **Immunities** all damage and conditions. It can't be turned, dispelled, or banished.
> **Manifestation** It repeats one task, with one line of speech, at one place. It ignores the living unless they interrupt the work.
> **Interruption** A creature that physically stops the work (by taking the brush or standing in the way) feels a deep chill and must succeed on a DC 10 Wisdom saving throw or be frightened of the haunt until the end of its next turn. The haunt then resumes.
> **Resolution** The haunt ends when the wrong that bound it is set right. The haunt's one line is always a clue to what that wrong was.
> **Award** Treat laying a haunt to rest as a story milestone, or award XP as for a CR 1 creature (200 XP).

## Lore
A toiling haunt forms when someone dies in the middle of a task that *matters*, usually because they were hiding something or trying to undo it. A cook who knew the wine was poisoned scrubs the cask forever. A clerk who forged a will keeps copying it out. A gravedigger who buried someone alive keeps digging the same grave. The haunt is not malevolent. It is stuck, and its work is evidence.

## Ecology
- **Environment:** kitchens, counting-houses, workshops, graveyards — the place where the work was done.
- **Encountered as:** alone. A house with one toiling haunt often has others, because the same secret binds them all.
- **Signs:** a tool that is always warm, a stain that comes back no matter how often it is cleaned, and servants who won't enter one room after dark.

## Running a Haunt
1. **Show the task** in one sentence of read-aloud.
2. **Give the line.** The haunt speaks it every time the party approaches, without variation.
3. **Make the line a clue.** "Getting the sweet out" means the wine was sweetened with something it shouldn't have been.
4. **Let it rest** when the truth is exposed or the wrongdoer is destroyed. Give it a final beat when it ends: the scrubbing stops, the haunt looks up, and it is gone.

## Named Example
**The Cook's Ghost** ([[SP-HAL-02-The-Hollow-Lantern]]). She scrubs the poisoned cask in the cellar and says only *"Getting the sweet out."* She stops when [[Lord Edric Vane]] is destroyed or Lady Ysolde is exposed.

## Adventure Hooks
1. A newly bought manor has a scullery maid who polishes the same silver spoon all night. The spoon is engraved with a family crest the previous owners never had.
2. A miller's ghost turns a grindstone that has nothing on it. Under the stone is the miller's partner, who has been missing for twenty years.
3. A PC inherits a shop whose dead owner is still balancing the books. One column never adds up.

## Spoils
None from the haunt itself. The thing it was working on is the reward: the evidence, the hidden coin, or the confession.

## Design Notes
**Harvested from** "The Cook's Ghost (haunt, no stat block)" in [[SP-HAL-02 — Bestiary]]. The Interruption save and the XP award are optional additions for DMs who want a haunt to carry a little mechanical weight. The SP-HAL-02 haunt works as written without them.

## Appears In
- [[SP-HAL-02-The-Hollow-Lantern]]: the cellar, Scene 04.

## Art Prompt
```
The translucent ghost of an older woman in a cook's cap and stained apron, drawn in faint broken lines, kneeling beside a wine cask and scrubbing it with a brush, her face patient and empty, full figure centered with the head and shoulders in the upper middle of the frame and clear space on every side, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 3:4 --v 8.1 --style raw --stylize 75 --seed 26500 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark
```

**Color portrait** (screen only: this is the FGU portrait and the token-maker source). Save it as `portraits/Toiling Haunt — Portrait.png`.
```
The translucent pale blue ghost of an older woman in a cook's cap and stained apron, scrubbing with a brush, her face patient and empty, head and shoulders portrait in three-quarter view, the head in the upper middle of the frame with clear space around it, stylized fantasy tabletop RPG creature portrait, crisp painted digital game art, clean confident linework with painterly cel-like shading, vivid but controlled color, soft rim light, strong readable silhouette, on a soft light cream and warm pale grey background with a gentle vignette --ar 3:4 --v 8.1 --stylize 150 --seed 26500 --no text, letters, signature, watermark, frame, border, dark background, black background
```

## FGU Import

Paste this block into Fantasy Grounds Unity: **NPCs → Import Text**, mode **2022 – Monsters of the Multiverse** (the 2014-style layout). If a field comes in blank, check the NPC's Notes tab, which shows where parsing stopped. *Written by hand: the haunt has no statblock, so `70-Company/Tools/fgu_import.py` skips this note and won't overwrite this section. Its AC, hit points and ability scores are placeholders the parser needs; the haunt can't actually be harmed. Challenge 0 keeps it out of encounter difficulty; grant the optional 200 XP from the party sheet when the haunt is laid to rest.*

> [!art]- FGU Portrait & Token
> ![[99-Assets/SP-BST-01/portraits/Toiling Haunt — Portrait.png|300]] ![[99-Assets/SP-BST-01/tokens/Toiling Haunt — Token.png|140]]

```text
Toiling Haunt
Medium undead, unaligned
Armor Class 10
Hit Points 1 (1d8 - 3)
Speed 0 ft.
STR DEX CON INT WIS CHA
1 (-5) 10 (+0) 4 (-3) 10 (+0) 10 (+0) 10 (+0)
Damage Immunities acid, bludgeoning, cold, fire, force, lightning, necrotic, piercing, poison, psychic, radiant, slashing, thunder
Condition Immunities blinded, charmed, deafened, exhaustion, frightened, grappled, incapacitated, invisible, paralyzed, petrified, poisoned, prone, restrained, stunned, unconscious
Senses passive Perception 10
Languages understands the languages it knew in life but speaks only its one line
Challenge 0 (0 XP) Proficiency Bonus +2
Haunt. The toiling haunt is not a creature that can be fought. It is immune to all damage and conditions, and it can't be turned, dispelled, or banished. Detect evil and good registers it as undead, and detect magic shows a faint necromantic aura on the object it works at.
Manifestation. The haunt repeats one task, with one line of speech, at one place. It ignores the living unless they interrupt the work. Its one line is always a clue to the wrong that bound it.
Resolution. The haunt ends when the wrong that bound it is set right. Treat laying it to rest as a story milestone, or award XP as for a CR 1 creature (200 XP).
Reactions
Interruption. When a creature physically stops the haunt's work (by taking its tool or standing in the way), that creature feels a deep chill and must succeed on a DC 10 Wisdom saving throw or be frightened of the haunt until the end of its next turn. The haunt then resumes its task.
```
