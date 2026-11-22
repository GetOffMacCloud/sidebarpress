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
tags: [npc, homebrew, sp-pbs-05, humanoid]
adventure: SP-GA05
section: appendix-bestiary
publish: true
title: Grukka One-Tusk
cr: '2'
xp: 450
base_block: orog (MM); Duelist's Word added
edition: '2014'
---

# Grukka One-Tusk

> ![[SP-GA05 portrait-grukka-one-tusk.jpg|300]]

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

*Homebrew variant of the orog (MM); Duelist's Word added. 2014 rules.*

- **Appearance:** Grey and scarred, missing his left tusk, wearing a stolen blue Furyondian cloak.
- **Wants:** To be paid, and never to see the Vesve again.
- **Fears:** The "barrow coin" curse.
- **Knows:** The Sickle's numbers and the Tor path; that Iuz's recruiters are combing the woods for deserters.
- **Escalation:** Threatens → bargains (offers the wardens grave-silver to turn back) → accepts a duel → honors the result. Turns on the Sickle if shown Halse's notes (DC 12).
- **In this adventure:** War-chief of the deserters holding the Tor path. [[SP-GA05 — E3 — The Orc Camp|E3]].

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
> [!example]- Grukka One-Tusk (CR 2, 450 XP)
> ## Grukka One-Tusk
> *Medium humanoid (orc), chaotic neutral*
> ___
> - **Armor Class** 18 (plate)
> - **Hit Points** 42 (5d8 + 20)
> - **Speed** 30 ft.
> ___
> | STR | DEX | CON | INT | WIS | CHA |
> |:---:|:---:|:---:|:---:|:---:|:---:|
> | 18 (+4) | 12 (+1) | 18 (+4) | 12 (+1) | 11 (+0) | 12 (+1) |
> ___
> - **Skills** Intimidation +5, Survival +2
> - **Senses** darkvision 60 ft., passive Perception 10
> - **Languages** Common, Orc
> - **Challenge** 2 (450 XP)  **Proficiency Bonus** +2
> ___
> ***Aggressive.*** As a bonus action, Grukka can move up to his speed toward a hostile creature that he can see.
>
> ***Duelist's Word.*** If Grukka accepts single combat, he fights only his challenger and yields at 10 hit points or fewer. His band honors the result.
>
> ### Actions
> ***Multiattack.*** Grukka makes two greataxe attacks.
>
> ***Greataxe.*** *Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 10 (1d12 + 4) slashing damage.
>
> ***Javelin.*** *Melee or Ranged Weapon Attack:* +6 to hit, reach 5 ft. or range 30/120 ft., one target. *Hit:* 7 (1d6 + 4) piercing damage.

## Appearances
- [[SP-GA05-The-Pilgrims-of-the-Hollow-Bell]]: Scene 5. Recurs in [[Grukka's Deserters]].

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity

## FGU Import
Paste into **NPCs → Import Text** (mode "2022 – Monsters of the Multiverse"; the block is 2014 content).

> [!art]- FGU Portrait & Token
> ![[SP-GA05 portrait-grukka-one-tusk.jpg|300]] ![[SP-GA05 token-orc-deserter.jpg|140]]

```text
Grukka One-Tusk
Medium humanoid (orc), chaotic neutral
Armor Class 18 (plate)
Hit Points 42 (5d8 + 20)
Speed 30 ft.
STR DEX CON INT WIS CHA
18 (+4) 12 (+1) 18 (+4) 12 (+1) 11 (+0) 12 (+1)
Skills Intimidation +5, Survival +2
Senses darkvision 60 ft., passive Perception 10
Languages Common, Orc
Challenge 2 (450 XP)
Proficiency Bonus +2
Aggressive. As a bonus action, Grukka can move up to his speed toward a hostile creature that he can see.
Duelist's Word. If Grukka accepts single combat, he fights only his challenger and yields at 10 hit points or fewer. His band honors the result.
Actions
Multiattack. Grukka makes two greataxe attacks.
Greataxe. Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 10 (1d12 + 4) slashing damage.
Javelin. Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 7 (1d6 + 4) piercing damage.
```
