---
type: npc
status: alive
canon: false
faction: ''
location: Ritterstadt
aliases: [Jens Ober]
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
tags: [greyhawk-university, probationer, gate-rota, shadow-on-the-quag, SP-GQ01]
---

# Jens Ober

> A Probationer on the gate rota, working off his first-term bond.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
![[SP-GQ01 Portrait - Jens Ober.png|300]]

Gangly, freckled, a lantern always held too high.

## Personality & Mannerisms
> *"The Registrar never misses the Warden's dinner. Wears the stacks key on a ribbon so it won't be lost."*

## Goals & Secrets
- *Deity:* [Pelor]
- **Wants:** to finish his rota and get to the dinner's leftovers. **Knows:** the round timings; the Registrar's habits. **Reacts:** chatty → officious if he catches someone → easily bribed with food.

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
**Guard** (MM p. 347), nonlethal; or a Gate-Rota Probationer minion (Scene 05).

## Appearances
- [[SP-GQ01-The-Gaolers-Link]]: Scenes 03, 05

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
Speaks in SP-GQ01; named per the functionaries rule (2026-10-23).
