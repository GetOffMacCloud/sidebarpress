---
type: npc
status: alive
canon: false
faction: Greyhawk University — Department of War Studies & Engineering
location: Ritterstadt — the Station House yard
aliases: [Dagny Holmgard, Lecturer Holmgard, the Quartermaster]
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
tags: [ritterstadt, greyhawk-university, lecturer, logistics, quartermaster, gazetteer]
---

# Lecturer Dagny Holmgard

> Lecturer in Logistics & Quartermastery, Department of War Studies & Engineering — and the Field Station's Quartermaster. Keeps the kit store and the ration ledger.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Oeridian, forties, broad, sleeves rolled, a tally-stick tucked behind one ear.

## Personality & Mannerisms
Brisk, practical, and personally offended by waste. Argues with Mauerbrecher about walls and with everyone about bog poles.

> *"Logistics is the art of being there with bread. Two bog poles a party. Not one."*

## Goals & Secrets
- **Wants:** a full winter stock before the pass closes, and no student lost to cold she could have prevented. So far, none has been.
- **Assistant:** [[Ulf Hadric]], who keeps the kit store.
- **Secret:** she skims nothing, and knows exactly who does.

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
**Veteran** (MM p. 350), retired.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-08, RG-09

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
