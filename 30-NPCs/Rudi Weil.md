---
type: npc
status: alive
canon: false
faction: ''
location: Ritterstadt
aliases: [Rudi Weil]
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
tags: [greyhawk-university, freshman, shadow-on-the-quag, SP-GQ01]
---

# Rudi Weil

> Konstanz's cousin, a Freshman with a crowbar and no plan of his own.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Heavyset, slow, loyal; carries the crowbar everywhere this week.

## Personality & Mannerisms
> *"Kon says it's easy money. Kon always says."*

## Goals & Secrets
- *Deity:* [Kord]
- **Wants:** to keep Konstanz out of trouble, and fails. **Knows:** the backup plan (the book-chute). **Reacts:** follows Konstanz; surrenders to anyone in authority.

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
**Bandit** (MM p. 343), nonlethal.

## Appearances
- [[SP-GQ01-The-Gaolers-Link]]: Scene 05 (complication); the decline path

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
Speaks in SP-GQ01; named per the functionaries rule (2026-10-23).
