---
type: npc
status: alive
canon: false
faction: Ritterstadt — townsfolk
location: Ritterstadt — Alder Row
aliases: [Old Hebe, Hebe Strasser]
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
tags: [ritterstadt, midwife, flan, gazetteer]
---

# Old Hebe Strasser

> Midwife and layer-out of the dead. She has delivered half the children in Ritterstadt and washed most of its dead, and remembers which were which.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Eighty, bent, Flan-dark, in a widow's shawl, smelling of lavender and lye.

## Personality & Mannerisms
Blunt, funny, unafraid of anyone. Calls the Ritter "Edmund's boy" to his face.

> *"I brought you in, I'll lay you out. Everything in between is your own affair."*

## Goals & Secrets
- **Wants:** an apprentice before she dies, and to be buried in the old way.
- **Knows:** the Peat-cutters' Row shrine-tender songs, and that her own grandmother was one.
- **Secret:** she laid out the two watchmen killed on 18 Planting and saw what was in the wounds. She told the Vater and no one else.

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
**Commoner** (MM p. 345); Medicine +5.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-03

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
