---
type: npc
status: alive
canon: false
faction: Clan Brock; the Assay House
location: Ritterstadt — the Assay House, Forge Row
aliases: [Brunna, the Assayer]
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
tags: [ritterstadt, dwarf, clan-brock, assayer, gazetteer]
---

# Brunna Deepdelve

> Assayer at the Assay House on Forge Row. A Clan Brock dwarf who tests ore, grades bog iron, and by charter logs every Bloom crystal and relic before the University sees it.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Sixty (young for a dwarf), braided red-brown beard tucked into a leather apron, acid-burned gloves, a jeweller's scale always at her elbow.

## Personality & Mannerisms
Exact, fair, and stubborn. Trusted by both the Consortium, which pays her, and the University, which needs her.

> *"The stone tells the truth. People tell me what they hope the stone says."*

## Goals & Secrets
- **Wants:** to find who took the three Bloom crystals missing from her log.
- **Suspects:** the Curio Club. (It was the Pale Ledger.)
- **Writes home:** to Brock's Aerie, which still has not acknowledged the Founder Dagmar.

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
**Commoner** (MM p. 345) with dwarf traits; expertise with alchemist's supplies and jeweler's tools.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-03, RG-04, RG-05, RG-07

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
