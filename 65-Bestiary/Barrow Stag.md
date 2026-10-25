---
type: creature
adventure: "SP-BST-01"
section: bestiary
publish_order: 120
publish: true
status: drafted
creature: "Barrow Stag"
cr: "1"
cr_num: 1
xp: 200
size: Large
creature_type: undead
alignment: unaligned
environment: [forest, hill, grassland, ruins, graveyard]
origin: harvested
base_block: "custom (Bone Beast Template)"
source_adventures: ["SP-PBS-02"]
tags: [bestiary, statblock, 2014-5e, bone-beast]
art_plate: todo        # todo | generated | approved | placed
portrait: todo
token: todo
---

# Barrow Stag

*A white stag of bare chalk-pale bone steps onto the barrow mound. Its tines are capped in green bronze. Behind it, the hounds go still.*

> [!art]+ Plate
> ![[99-Assets/SP-BST-01/plates/Barrow Stag.png|360]]

> [!example]+ Barrow Stag (CR 1, 200 XP)
> *Large undead, unaligned*
> **Armor Class** 13 (natural armor) · **Hit Points** 45 (6d10 + 12) · **Speed** 50 ft.
>
> | STR | DEX | CON | INT | WIS | CHA |
> |---|---|---|---|---|---|
> | 16 (+3) | 12 (+1) | 15 (+2) | 2 (−4) | 10 (+0) | 3 (−4) |
>
> **Damage Vulnerabilities** bludgeoning · **Damage Immunities** poison · **Condition Immunities** exhaustion, frightened, poisoned
> **Senses** darkvision 60 ft., passive Perception 10 · **Languages** — · **Challenge** 1 (200 XP)
>
> ***Trampling Charge.*** If the stag moves at least 20 feet straight toward a creature and then hits it with an Antlers attack on the same turn, the target takes an extra 7 (2d6) piercing damage and must succeed on a DC 13 Strength saving throw or be knocked prone.
>
> ***First of the Pack.*** While the stag stands, bone beasts within 30 feet of it can't be frightened or turned.
>
> ***Pack-Bound; Binding Law.*** See [[Bone Beast Template]].
>
> **Actions**
> ***Antlers.*** *Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 10 (2d6 + 3) piercing damage.

## Lore
Every bone pack has a first beast, the maker's own mount or totem animal, buried at the heart of the barrow. In the old stories it is almost always a white stag. As long as the stag stands, the pack doesn't break. Holy symbols that send hounds scattering do nothing while the stag lowers its head.

## Ecology
- **Environment:** barrow-fields, old forests, and moorland.
- **Encountered as:** alone at the head of a pack of [[Bone Hound|bone hounds]], [[Bone Boar|boars]], and [[Bone Elk|elk]]. Each pack has only one.
- **Signs:** a white stag seen at dusk that leaves no tracks, and hounds that stop and turn as one.

## Tactics
The stag charges the party's cleric or anyone brandishing a holy symbol. It knows what turning does to its pack. It fights in the middle of the pack so that First of the Pack covers as many beasts as possible.

**Running it:** First of the Pack gives Turn Undead a clear target order. Telegraph it: hounds that flinch from the holy symbol steady themselves when the stag lowers its head.

## Named Example
**Kethra's white stag** ([[SP-PBS-02-The-Bones-of-the-Dreadverge]]). It is [[Kethra-the-Hound-Mother|the Hound-Mother's]] own mount. Its tines are capped in Flan grave-bronze cut with the triple spiral.

## Adventure Hooks
1. Hunters have chased a white stag for three nights. On the fourth, it turned, and only one hunter came back.
2. A bard's ballad says the white stag will lead a worthy rider to the barrow-king's treasure. It leads riders to the barrow-king, at least.
3. Destroying the stag is the only way to break a pack that is ravaging the valley. It never leaves the pack's center.

## Spoils
The bronze tine-caps (four, worth 10 gp each) are etched with the maker's sigil. Together, they act as a key or a map to the maker's tomb (DM's choice).

## Design Notes
**Custom**, built under the [[Bone Beast Template]].

**CR verification (DMG p. 274):** *Defensive:* 45 hp is in the CR 1/4 band (36–49), and AC 13 is as expected, so defensive CR is **1/4**. The poison immunity doesn't change effective hit points meaningfully, and the DMG doesn't adjust for the bludgeoning vulnerability. *Offensive:* modeled over three rounds (17 on the charge round, then 10 and 10), it deals about 12 damage per round, which is the CR 1 band (9–14). +5 to hit is two above the expected +3, so offensive CR is **2**. *Average:* (1/4 + 2) ÷ 2 ≈ 1.1, which gives **CR 1**. It hits like a CR 2 creature and goes down to a warhammer, which is the intent. *(Revised 2026-10-17 in SP-PBS-02: a bonus-action hooves attack was removed because it pushed damage to the CR 2 band.)*

## Appears In
- [[SP-PBS-02-The-Bones-of-the-Dreadverge]]: Encounter 7, at the head of Kethra's pack. Statblocks are in [[SP-PBS-02 — Bestiary]].

## Art Prompt
```
A great stag made entirely of pale bare bone, every bone left plain white, its antler tines capped in dark stippled bronze etched with triple spirals, empty eye sockets calm, standing proud on a small grassy mound, full figure centered with the head and shoulders in the upper middle of the frame and clear space on every side, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 3:4 --v 8.1 --style raw --stylize 75 --seed 26500 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark
```

**Color portrait** (screen only: this is the FGU portrait and the token-maker source). Save it as `portraits/Barrow Stag — Portrait.png`.
```
A great stag made of chalk-white bone, its antler tines capped in verdigris-green bronze etched with triple spirals, calm empty eye sockets, head and shoulders portrait in three-quarter view, the head in the upper middle of the frame with clear space around it, stylized fantasy tabletop RPG creature portrait, crisp painted digital game art, clean confident linework with painterly cel-like shading, vivid but controlled color, soft rim light, strong readable silhouette, on a soft light dusty blue-grey background with a gentle vignette --ar 3:4 --v 8.1 --stylize 150 --seed 26500 --no text, letters, signature, watermark, frame, border, dark background, black background
```

## FGU Import

Paste each block into Fantasy Grounds Unity: **NPCs → Import Text**, mode **2022 – Monsters of the Multiverse** (the 2014-style layout). Spells link only if a module containing them is open in the campaign. If a field comes in blank, check the NPC's Notes tab, which shows where parsing stopped. *Generated by `70-Company/Tools/fgu_import.py`; re-run it after any statblock change rather than editing by hand.*

> [!art]- FGU Portrait & Token
> ![[99-Assets/SP-BST-01/portraits/Barrow Stag — Portrait.png|300]] ![[99-Assets/SP-BST-01/tokens/Barrow Stag — Token.png|140]]

```text
Barrow Stag
Large undead, unaligned
Armor Class 13 (natural armor)
Hit Points 45 (6d10 + 12)
Speed 50 ft.
STR DEX CON INT WIS CHA
16 (+3) 12 (+1) 15 (+2) 2 (-4) 10 (+0) 3 (-4)
Damage Vulnerabilities bludgeoning
Damage Immunities poison
Condition Immunities exhaustion, frightened, poisoned
Senses darkvision 60 ft., passive Perception 10
Languages -
Challenge 1 (200 XP) Proficiency Bonus +2
Trampling Charge. If the stag moves at least 20 feet straight toward a creature and then hits it with an Antlers attack on the same turn, the target takes an extra 7 (2d6) piercing damage and must succeed on a DC 13 Strength saving throw or be knocked prone.
First of the Pack. While the stag stands, bone beasts within 30 feet of it can't be frightened or turned.
Pack-Bound. The beast obeys whoever wears or carries its pack's binding relic. With no one holding the relic, it hunts the relic, guards its maker's tomb, and drags carrion home.
Binding Law. The pack was made under one law its beasts can't break (DM's choice, e.g. never attack a creature standing in running water).
Actions
Antlers. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) piercing damage.
```
