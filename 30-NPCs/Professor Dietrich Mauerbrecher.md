---
type: npc
status: alive
canon: false
faction: Greyhawk University — Department of War Studies & Engineering
location: Ritterstadt
aliases: [Mauerbrecher, Professor Mauerbrecher]
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
tags: [ritterstadt, greyhawk-university, department-head, war-studies, engineering, gazetteer]
source_canon: A Tourist In Greyhawk — 06 — Department of War Studies & Engineering (placeholder head)
---

# Professor Dietrich Mauerbrecher

> ![[Ritterstadt mauerbrecher.jpg|300]]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Sixties, bull-necked, a former Perrender free-company engineer with a surveyor's chain looped on his belt and a limp from a collapsed sap.

## Personality & Mannerisms
Draws on whatever is nearest — tables, walls, students' notebooks. Argues with Holmgard about walls versus bread and loses half the time.

> *"A wall is a promise the town makes to itself."*

## Goals & Secrets
- **Wants:** the eastern gate rebuilt in stone before the next Bloom, and Dagmar of Clan Brock's original palisade plans.
- **Knows:** the plans show a fifth bastion on the Wachturm rise that was never built.
- **Secret:** his repair drawings leave the breach timber-and-rope for another season on purpose; stone would need a footing on the old foundation, and he does not want to dig there.

## Role & Context
> [!art]+ Portrait

> Head of the Department of War Studies & Engineering. He designed the eastern gate's repair and is the Ritter's unofficial engineer.

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
**Veteran** (MM p. 350), retired; Intelligence 15.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-08, RG-09

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
A **placeholder department head** in the campaign vault's `06 — Department of War Studies & Engineering`. Anything beyond that note is Gazetteer elaboration; a full campaign note overrides this one.

## Continuity

## His Department
**Major:** Military Theory · **Minors:** Fortification & Engineering · Logistics & Quartermastery. His lecturer: [[Lecturer Dagny Holmgard]] (Logistics; also Quartermaster). Practicals with [[Garrok Stonebrow]] at [[The Drill Yard]].
