---
type: npc
status: draft
canon: false
faction: ''
location: ''
aliases: []
species: ''
heritage: ''
gender: ''
age: ''
alignment: ''
occupation: ''
class: ''
subclass: ''
prestige_class: ''
level: ''
adventure_role: ''
disposition: ''
party_trust: ''
items: []
connected_quests: []
connected_groups: []
parents: []
partner: []
children: []
siblings: []
allies: []
enemies: []
deceased_date: ''
tags: [npc, homebrew, sp-pbs-05, undead]
adventure: SP-GA05
section: appendix-bestiary
publish: true
title: Cathal Red-Torc
cr: '3'
xp: 700
base_block: wight (MM); Barrow-King traits added
edition: '2014'
---

# Cathal Red-Torc

> ![[SP-GA05 portrait-cathal-red-torc.jpg|300]]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance

## Personality & Mannerisms

## Goals & Secrets

## Role & Context
> [!art]+ Portrait

*Homebrew variant of the wight (MM); Barrow-King traits added. 2014 rules.*

- **Appearance:** Tall, dead, in a corroded mail shirt; a twisted torc of red gold at his throat; copper rings on every finger.
- **Wants:** To sleep, and to know who woke him.
- **Knows:** The Flan names of every barrow under the Tor; that the bell was rung once, for him.
- **Reaction:** Parleys with anyone who honors the Flan dead (Religion or Persuasion DC 15; advantage with the lambskin, a Yati PC, or a faith that keeps the rest of the dead). Kills whoever holds the bone clapper.
- **In this adventure:** Rises on toll 13 in [[SP-GA05 — E4 — Thirteen Tolls|E4]] (Ending D). Not in the base XP budget.

## Conversation Guide
| Topic | Freely discussed? | Notes / sample line |
|---|:---:|---|
| | | |

## Services
| Service | Cost / notes |
|---|---|
| | |

## Quest Hooks
| Hook | Leads to | Trigger |
|---|---|---|
| | | |

## Relationships
```dataview
TABLE WITHOUT ID parents AS "Parents", partner AS "Partner", children AS "Children", siblings AS "Siblings", allies AS "Allies", enemies AS "Enemies"
WHERE file.path = this.file.path
```

## Inventory
```dataview
LIST FROM "50-Items" WHERE contains(this.items, file.link)
```

## Stat Block
> [!example]- Cathal Red-Torc (CR 3, 700 XP)
> ## Cathal Red-Torc
> *Medium undead, neutral evil*
> ___
> - **Armor Class** 14 (studded leather)
> - **Hit Points** 45 (6d8 + 18)
> - **Speed** 30 ft.
> ___
> | STR | DEX | CON | INT | WIS | CHA |
> |:---:|:---:|:---:|:---:|:---:|:---:|
> | 15 (+2) | 14 (+2) | 16 (+3) | 10 (+0) | 13 (+1) | 15 (+2) |
> ___
> - **Skills** Perception +3, Stealth +4
> - **Damage Resistances** necrotic; bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered
> - **Damage Immunities** poison
> - **Condition Immunities** exhaustion, poisoned
> - **Senses** darkvision 60 ft., passive Perception 13
> - **Languages** Old Flan
> - **Challenge** 3 (700 XP)  **Proficiency Bonus** +2
> ___
> ***Sunlight Sensitivity.*** While in sunlight, Cathal has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight.
>
> ***Hatred of the Waker.*** Cathal has advantage on attack rolls against the creature holding the bone clapper.
>
> ***Rest Unearned.*** If the Sun-Bell is consecrated or Cathal is laid to rest by parley, he drops to 0 hit points and does not rise again.
>
> ### Actions
> ***Multiattack.*** Cathal makes two longsword attacks or two longbow attacks. He can use his Life Drain in place of one longsword attack.
>
> ***Life Drain.*** *Melee Weapon Attack:* +4 to hit, reach 5 ft., one creature. *Hit:* 5 (1d6 + 2) necrotic damage. The target must succeed on a DC 13 Constitution saving throw or its hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0. A humanoid slain by this attack rises 24 hours later as a zombie under Cathal's control, unless the humanoid is restored to life or its body is destroyed. Cathal can have no more than twelve zombies under his control at one time.
>
> ***Longsword.*** *Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* 6 (1d8 + 2) slashing damage, or 7 (1d10 + 2) slashing damage if used with two hands.
>
> ***Longbow.*** *Ranged Weapon Attack:* +4 to hit, range 150/600 ft., one target. *Hit:* 6 (1d8 + 2) piercing damage.

## Appearances
- [[SP-GA05-The-Pilgrims-of-the-Hollow-Bell]]: Scene 6, toll 13 only. Leaves the [[Red Torc of Cathal]] if laid to rest.

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity

## FGU Import
Paste into **NPCs → Import Text** (mode "2022 – Monsters of the Multiverse"; the block is 2014 content).

> [!art]- FGU Portrait & Token
> ![[SP-GA05 portrait-cathal-red-torc.jpg|300]]

```text
Cathal Red-Torc
Medium undead, neutral evil
Armor Class 14 (studded leather)
Hit Points 45 (6d8 + 18)
Speed 30 ft.
STR DEX CON INT WIS CHA
15 (+2) 14 (+2) 16 (+3) 10 (+0) 13 (+1) 15 (+2)
Skills Perception +3, Stealth +4
Damage Resistances necrotic; bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered
Damage Immunities poison
Condition Immunities exhaustion, poisoned
Senses darkvision 60 ft., passive Perception 13
Languages Old Flan
Challenge 3 (700 XP)
Proficiency Bonus +2
Sunlight Sensitivity. While in sunlight, Cathal has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight.
Hatred of the Waker. Cathal has advantage on attack rolls against the creature holding the bone clapper.
Rest Unearned. If the Sun-Bell is consecrated or Cathal is laid to rest by parley, he drops to 0 hit points and does not rise again.
Actions
Multiattack. Cathal makes two longsword attacks or two longbow attacks. He can use his Life Drain in place of one longsword attack.
Life Drain. Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 5 (1d6 + 2) necrotic damage. The target must succeed on a DC 13 Constitution saving throw or its hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0. A humanoid slain by this attack rises 24 hours later as a zombie under Cathal's control, unless the humanoid is restored to life or its body is destroyed. Cathal can have no more than twelve zombies under his control at one time.
Longsword. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) slashing damage, or 7 (1d10 + 2) slashing damage if used with two hands.
Longbow. Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage.
```
