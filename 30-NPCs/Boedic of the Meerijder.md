---
type: npc
status: alive
canon: false
faction: Clan Meerijder
location: The Erlen Bridge
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
tags: [meerijder, drover, erlen-bridge, sp-pbs-00]
---

# Boedic of the Meerijder

> A Meerijder drover holding a lawful writ he wishes he'd never been handed.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Older than his crew, red-and-black on his sleeves, a folded paper in his hand.

## Personality & Mannerisms
Polite, sorry about it, and immovable. Apologizes while not moving. Curious what strangers are doing in a family matter.

## Goals & Secrets
- **Wants:** to obey the writ and go home to his cows.
- **Knows:** the writ says hold the wagons and the Junker until the Ratsherr comes, and says nothing about the party; Otwin's boy paid him six marks.
- **Reacts:** stands aside for clan kinship, the jurisdiction argument, or twelve marks. Fights defensively and calls it off at two drovers down.

## Role & Context

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
**Bandit captain** (MM p. 344) with changes; see [[SP-GA00 — Bestiary]].

## Appearances
- [[SP-GA00-Nobodys-Colors]] — Scene 2

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. Clan Meerijder is Living Greyhawk material.

## Continuity
None.
