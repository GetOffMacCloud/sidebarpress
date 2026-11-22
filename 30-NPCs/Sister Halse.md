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
title: Sister Halse
cr: '2'
xp: 450
base_block: cult fanatic (MM); *ash tally* and *reaper's tithe* added
edition: '2014'
---

# Sister Halse

> ![[SP-GA05 portrait-sister-halse.jpg|300]]

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

*Homebrew variant of the cult fanatic (MM p. 345): Wisdom 15; *ash tally* and *reaper's tithe* added. 2014 rules.*
- **Loyalty:** Ansgar first, the Sickle second. [Nerull]
- **Fears:** Losing count. An unfinished tally is the one thing that rattles her.

- **Appearance:** Small and sharp-faced, with ink-stained fingers and a satchel of notes.
- **Wants:** To be the one who rings the thirteenth toll.
- **Knows:** The ritual's rules (her notes are Handout 3), the list of barrows, which houses drank.
- **Escalation:** Doubles back at Notice 3 to poison the wardens' water. Drops her notes at the relay. On the Tor, *hold person* on whoever reaches the frame; takes the clapper if Ansgar flees and rings for as long as his concentration lasts. Fights to the end.
- **In this adventure:** Tallykeeper of the procession. Fought in [[SP-GA05 — E4 — Thirteen Tolls|E4]].

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
> [!example]- Sister Halse (CR 2, 450 XP)
> ## Sister Halse
> *Medium humanoid (human), neutral evil*
> ___
> - **Armor Class** 13 (leather armor)
> - **Hit Points** 33 (6d8 + 6)
> - **Speed** 30 ft.
> ___
> | STR | DEX | CON | INT | WIS | CHA |
> |:---:|:---:|:---:|:---:|:---:|:---:|
> | 11 (+0) | 14 (+2) | 12 (+1) | 10 (+0) | 15 (+2) | 14 (+2) |
> ___
> - **Skills** Deception +4, Persuasion +4, Religion +2
> - **Senses** passive Perception 12
> - **Languages** Common, Flan
> - **Challenge** 2 (450 XP)  **Proficiency Bonus** +2
> ___
> ***Dark Devotion.*** Halse has advantage on saving throws against being charmed or frightened.
>
> ***The Count.*** Halse counts everything aloud: tolls, steps, the dead. While she is conscious, the party always knows the current toll count.
>
> ***Spellcasting.*** Halse is a 4th-level spellcaster. Her spellcasting ability is Wisdom (spell save DC 12, +4 to hit with spell attacks). She has the following cleric spells prepared:
> >
> > Cantrips (at will): *light*, *sacred flame*, *thaumaturgy*
> 1st level (4 slots): *ash tally* (ritual), *command*, *inflict wounds*, *shield of faith*
> 2nd level (3 slots): *hold person*, *reaper's tithe* (ritual), *spiritual weapon*
>
> ### Actions
> ***Multiattack.*** Halse makes two melee attacks.
>
> ***Dagger.*** *Melee or Ranged Weapon Attack:* +4 to hit, reach 5 ft. or range 20/60 ft., one creature. *Hit:* 4 (1d4 + 2) piercing damage.

## Appearances
- [[SP-GA05-The-Pilgrims-of-the-Hollow-Bell]]: Scenes 2, 4 (her notes) and 6. Keeps [[The Grey Sickle's List]] if she survives.

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity

## FGU Import
Paste into **NPCs → Import Text** (mode "2022 – Monsters of the Multiverse"; the block is 2014 content).

> [!art]- FGU Portrait & Token
> ![[SP-GA05 portrait-sister-halse.jpg|300]]

```text
Sister Halse
Medium humanoid (human), neutral evil
Armor Class 13 (leather armor)
Hit Points 33 (6d8 + 6)
Speed 30 ft.
STR DEX CON INT WIS CHA
11 (+0) 14 (+2) 12 (+1) 10 (+0) 15 (+2) 14 (+2)
Skills Deception +4, Persuasion +4, Religion +2
Senses passive Perception 12
Languages Common, Flan
Challenge 2 (450 XP)
Proficiency Bonus +2
Dark Devotion. Halse has advantage on saving throws against being charmed or frightened.
The Count. Halse counts everything aloud: tolls, steps, the dead. While she is conscious, the party always knows the current toll count.
Spellcasting. Halse is a 4th-level spellcaster. Her spellcasting ability is Wisdom (spell save DC 12, +4 to hit with spell attacks). She has the following cleric spells prepared:

Cantrips (at will): light, sacred flame, thaumaturgy
1st level (4 slots): ash tally (ritual), command, inflict wounds, shield of faith
2nd level (3 slots): hold person, reaper's tithe (ritual), spiritual weapon
Actions
Multiattack. Halse makes two melee attacks.
Dagger. Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one creature. Hit: 4 (1d4 + 2) piercing damage.
```
