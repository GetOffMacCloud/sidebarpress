---
type: npc
status: alive
canon: false
faction: Greyhawk University — Department of Exploration & Cartography
location: Ritterstadt
aliases: [Hamlin Dreel, Lecturer Dreel]
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
tags: [ritterstadt, greyhawk-university, lecturer, subterranean, gazetteer]
---

# Lecturer Hamlin Dreel

> Lecturer in Subterranean Studies, Department of Exploration & Cartography. A Perrender who lost two fingers to a Clatspur deep and will tell you exactly how.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Forties, wiry, pale from too long underground, his left hand three-fingered, a miner's lamp hooked to his belt even indoors.

## Personality & Mannerisms
Cheerful about catastrophe. Teaches by story. Tests every student by blindfolding them in the Archive cellar.

> *"Up is where the air moves. Down is where it doesn't. Remember which you want."*

## Goals & Secrets
- **Wants:** a survey of whatever lies under the Wachturm.
- **Secret:** he has heard Hanz Korngut mention "the Kammer" and has been looking for it.

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
**Scout** (MM p. 349), darkvision from a goggles-trinket; climbing kit.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-09

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
