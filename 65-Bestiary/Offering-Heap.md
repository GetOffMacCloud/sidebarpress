---
type: creature
adventure: "SP-OM01"
section: bestiary
publish_order: 525
publish: true
status: drafted
creature: "Offering-Heap"
cr: "15"
cr_num: 15
xp: 13000
size: Huge
creature_type: plant
alignment: unaligned
environment: [forest, farmland, village]
origin: new
credit: ""
base_block: "none (new; defenses follow the shambling mound, MM p. 270)"
source_adventures: ["SP-GS01"]
tags: [bestiary, statblock, 2014-5e, plant, harvest]
art_plate: todo
portrait: done
token: done
---

# Offering-Heap

*A mound of rotten pumpkins taller than a barn shifts, sighs like a cider press, and holds out a squashed gourd to you.*

> [!art]+ Plate
> ![[99-Assets/Bestiary/Print/Offering-Heap.png|360]]

> [!example]+ Offering-Heap (CR 15, 13,000 XP)
> *Huge plant, unaligned*
> **Armor Class** 16 (natural armor) · **Hit Points** 250 (20d12 + 120) · **Speed** 30 ft.
>
> | STR | DEX | CON | INT | WIS | CHA |
> |---|---|---|---|---|---|
> | 24 (+7) | 6 (−2) | 22 (+6) | 6 (−2) | 14 (+2) | 8 (−1) |
>
> **Saving Throws** Str +12, Con +11
> **Damage Vulnerabilities** fire · **Damage Resistances** bludgeoning, cold, necrotic, piercing, psychic · **Damage Immunities** lightning
> **Condition Immunities** blinded, deafened, exhaustion, prone
> **Senses** blindsight 60 ft. (blind beyond this radius), passive Perception 12 · **Languages** understands Sylvan but can't speak · **Challenge** 15 (13,000 XP)
>
> ***Grief-Bound.*** The Offering-Heap never attacks first, and it won't pursue a creature beyond the bounds of the shrine it guards.
>
> ***Composting.*** The Offering-Heap regains 20 hit points at the start of its turn if it has at least 1 hit point. If it takes fire damage, this trait doesn't function at the start of its next turn. The Offering-Heap dies only if it starts its turn with 0 hit points and doesn't regenerate.
>
> ***Lightning Absorption.*** Whenever the Offering-Heap is subjected to lightning damage, it takes no damage and regains a number of hit points equal to the lightning damage dealt.
>
> ***Burning Layers.*** Whenever the Offering-Heap takes fire damage, it sheds a burning layer. Each creature within 10 feet of it must make a DC 19 Dexterity saving throw, taking 14 (4d6) fire damage on a failed save, or half as much damage on a successful one.
>
> **Actions**
> ***Multiattack.*** The Offering-Heap makes three Slam attacks.
>
> ***Slam.*** *Melee Weapon Attack:* +12 to hit, reach 15 ft., one target. *Hit:* 29 (4d10 + 7) bludgeoning damage. If the target is a Large or smaller creature, it must succeed on a DC 20 Strength saving throw or be pushed 10 feet away from the Offering-Heap and knocked prone.
>
> ***Harvest Avalanche (Recharge 5–6).*** Part of the Offering-Heap collapses forward in a 30-foot cone. Each creature in that area must make a DC 19 Dexterity saving throw. On a failed save, a creature takes 55 (10d10) bludgeoning damage and is buried, becoming restrained (escape DC 19). On a successful save, it takes half as much damage and isn't buried.
>
> **Bonus Actions**
> ***Gift.*** The Offering-Heap presses a rotten pumpkin, a moldy sheaf or a squashed gourd into the hands of a creature within 15 feet of it. This has no effect. It means well.

## Lore
Wherever the old faiths take offerings — a druid's shrine, a harvest stone, a saint's well — the gifts pile up behind the altar once the god has had its share. Most years the heap rots quietly into the soil. But when a shrine is wronged (an offering skipped, a keeper murdered, a sacred beast left to starve), the grief of the place can pull that heap upright.

An Offering-Heap is not malicious. It is the shrine's last servant, made of everything the faithful ever gave, and it keeps guarding the altar because no one told it to stop. It understands the old tongue of the woods, it answers with gifts, and it is lonely in a way that is hard to watch.

It is also as heavy as a barn and as strong as a landslide. People who mistake its grief for menace find that out.

## Ecology
- **Environment:** old-faith groves, field shrines and offering stones in farming country, especially in autumn.
- **Encountered as:** alone. One heap to a shrine.
- **Signs:** a sweet stink of cider and rot; pumpkins and gourds left on doorsteps nearby; crows that won't settle; a trail of wet leaves leading back to the altar.

## Tactics
It never strikes first. Faced with intruders, it looms, shuffles between them and whatever it guards, and offers them gifts. Attacked, it Slams the nearest attacker and buries clusters under a Harvest Avalanche. It never chases beyond the shrine's bounds.

**Running it:** play it as a sad, enormous dog that has been hit. Reward players who talk to it.
- **Calming it:** a DC 18 Intelligence (Nature) or Wisdom (Animal Handling) check, with advantage for anyone who speaks Sylvan or is of the shrine's faith. **Feeding it** a true offering for its shrine calms it at once.
- **Fighting it:** it is vulnerable to fire, and fire stops its regeneration. A DC 15 Intelligence (Nature) check spots that it is a compost heap: "wet, but it'll burn." Lightning heals it.

## Named Example
**The heap behind Jaroo's grove** ([[SP-GS01-The-Gluttonwretch-of-Hommlet]], Hommlet, 576 CY). It is forty years of Brewfest offerings, risen when Hommlet starved the grove's sacred bird. Calmed, it hands over the bird's last feather and follows the party to the feast.

## Adventure Hooks
1. A village's well-saint has been forgotten for a generation, and the heap of old tokens behind the well has started following children home.
2. A temple's new priest has thrown the old offerings out; the midden behind the temple is now standing in the road.
3. A druid asks the party to escort a living offering-heap to a new grove before the loggers arrive.

## Spoils
Calmed, an Offering-Heap gives one true gift from the shrine's past: a relic, a lost token or a holy object. Killed, it leaves compost, and the shrine's keepers do not forgive it.

## Design Notes
**New creature** (Sidebar Press, 2026-11-18, for [[SP-GS01-The-Gluttonwretch-of-Hommlet]]). Greybeard's brief: a grieving guardian that can be talked down in under 30 minutes, but hits exceptionally hard if attacked. Defenses follow the **shambling mound** (MM p. 270): its resistances, its lightning immunity and Lightning Absorption, and its blinded, deafened and exhaustion immunities. Psychic resistance was added. The mound's fire resistance was dropped so that the Heap's fire vulnerability works.

**CR verification (DMG p. 274).** *Defensive:* 250 hit points plus 60 from three rounds of Composting = 310 effective, the CR 15–16 band; AC 16 is two below the expected 18, so **defensive CR 15**. *Offensive:* three Slams for 87 (12d10 + 21) a round, the CR 13 band (87–92); +12 to hit is four above the expected +8, so **offensive CR 15**. Harvest Avalanche, 55 (10d10) against several targets on a recharge, keeps it there. *Average:* **CR 15**.

**Scaling:** APL 11, 225 hit points (18d12 + 108); APL 13, Composting 25.

## Appears In
- [[SP-GS01-The-Gluttonwretch-of-Hommlet]] — [[Scene 04 — The Grove and the Offering-Heap]] (guardian of the grove); optional ally in [[Scene 07 — The Brewfest Feast]]

## Art Prompt
Style: black-and-white ink, per [[Art-Style-Guide]] (PLATE spine).
```
a towering creature made of rotting harvest offerings, pumpkins, gourds, corn husks and wet leaves rendered as hand-drawn patterns, a pumpkin for a head, gourd knuckles, a shaggy corn-husk mane, holding out a squashed pumpkin with both hands like a gift, standing on the ground, full figure centered with the head and shoulders in the upper middle of the frame and clear space on every side, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 3:4 --v 8.1 --style raw --stylize 75 --seed 26500 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark
```

**Color portrait** (screen only: the FGU portrait and the token-maker source). Save it as `99-Assets/Bestiary/FGU/Portraits/Offering-Heap — Portrait.png`.
```
a towering creature made of rotting orange pumpkins, mottled gourds, golden corn husks and russet leaves, a carved-looking pumpkin head with sad hollow eyes, a shaggy corn-husk mane, head and shoulders portrait in three-quarter view, the head in the upper middle of the frame with clear space around it, stylized fantasy tabletop RPG creature portrait, crisp painted digital game art, clean confident linework with painterly cel-like shading, vivid but controlled color, soft rim light, strong readable silhouette, on a soft light cream and warm pale grey background with a gentle vignette --ar 3:4 --v 8.1 --stylize 150 --seed 26500 --no text, letters, signature, watermark, frame, border, dark background, black background
```

## FGU Import

Paste each block into Fantasy Grounds Unity: **NPCs → Import Text**, mode **2022 – Monsters of the Multiverse** (the 2014-style layout). Spells link only if a module containing them is open in the campaign. If a field comes in blank, check the NPC's Notes tab, which shows where parsing stopped. *Generated by `70-Company/Tools/fgu_import.py`; re-run it after any statblock change rather than editing by hand.*

> [!art]- FGU Portrait & Token
> ![[99-Assets/Bestiary/FGU/Portraits/Offering-Heap — Portrait.png|300]] ![[99-Assets/Bestiary/FGU/Tokens/Offering-Heap — Token.png|140]]

```text
Offering-Heap
Huge plant, unaligned
Armor Class 16 (natural armor)
Hit Points 250 (20d12 + 120)
Speed 30 ft.
STR DEX CON INT WIS CHA
24 (+7) 6 (-2) 22 (+6) 6 (-2) 14 (+2) 8 (-1)
Saving Throws Str +12, Con +11
Damage Vulnerabilities fire
Damage Resistances bludgeoning, cold, necrotic, piercing, psychic
Damage Immunities lightning
Condition Immunities blinded, deafened, exhaustion, prone
Senses blindsight 60 ft. (blind beyond this radius), passive Perception 12
Languages understands Sylvan but can't speak
Challenge 15 (13,000 XP) Proficiency Bonus +5
Grief-Bound. The Offering-Heap never attacks first, and it won't pursue a creature beyond the bounds of the shrine it guards.
Composting. The Offering-Heap regains 20 hit points at the start of its turn if it has at least 1 hit point. If it takes fire damage, this trait doesn't function at the start of its next turn. The Offering-Heap dies only if it starts its turn with 0 hit points and doesn't regenerate.
Lightning Absorption. Whenever the Offering-Heap is subjected to lightning damage, it takes no damage and regains a number of hit points equal to the lightning damage dealt.
Burning Layers. Whenever the Offering-Heap takes fire damage, it sheds a burning layer. Each creature within 10 feet of it must make a DC 19 Dexterity saving throw, taking 14 (4d6) fire damage on a failed save, or half as much damage on a successful one.
Actions
Multiattack. The Offering-Heap makes three Slam attacks.
Slam. Melee Weapon Attack: +12 to hit, reach 15 ft., one target. Hit: 29 (4d10 + 7) bludgeoning damage. If the target is a Large or smaller creature, it must succeed on a DC 20 Strength saving throw or be pushed 10 feet away from the Offering-Heap and knocked prone.
Harvest Avalanche (Recharge 5-6). Part of the Offering-Heap collapses forward in a 30-foot cone. Each creature in that area must make a DC 19 Dexterity saving throw. On a failed save, a creature takes 55 (10d10) bludgeoning damage and is buried, becoming restrained (escape DC 19). On a successful save, it takes half as much damage and isn't buried.
Bonus Actions
Gift. The Offering-Heap presses a rotten pumpkin, a moldy sheaf or a squashed gourd into the hands of a creature within 15 feet of it. This has no effect. It means well.
```
