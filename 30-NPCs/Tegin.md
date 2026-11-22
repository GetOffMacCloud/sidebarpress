---
type: npc
status: alive
canon: false
faction: ''
location: Ritterstadt
aliases: [Tegin]
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
tags: [wolf-nomads, pilot, tethered, shadow-on-the-quag, SP-GQ01]
---

# Tegin

> A Wolf Nomad ice- and lake-pilot hired by "Fesch" for a run north. Tethered, and doesn't know it.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
![[SP-GQ01 Portrait - Tegin.png|300]]

Lean, weathered, a braided horsehair cord at his throat with a lodestone on it.

## Personality & Mannerisms
> *"I go where the money points, and the money points north."*

## Goals & Secrets
- *Deity:* [Istus]
- **Wants:** his pay and the open lake. **Knows:** the route north along the shore into Wolf Nomad water, which is hostile to Iuz; that's why a tether was needed. **Reacts:** fights only for pay; quits at half hit points; wakes within 30 ft of the unboxed Link.

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
**Scout** (MM p. 349).

## Appearances
- [[SP-GQ01-The-Gaolers-Link]]: Scenes 03, 06, 07

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
Freed of his tether, he gives the party his [[Ice-Pilot's Lodestar]] (SP-GQ05). Wolf Nomads are hostile to Iuz in 576 ([[Wolf-Nomads]]). Named per the functionaries rule (2026-10-23).
