---
type: npc
status: alive
canon: false
faction: Greyhawk University — Department of Antiquities; the Regents' Commission
location: Ritterstadt
aliases: [Vogelsang, Professor Vogelsang]
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
tags: [ritterstadt, greyhawk-university, department-head, antiquities, regents, gazetteer]
source_canon: A Tourist In Greyhawk — 04 — Department of Antiquities (placeholder head)
---

# Professor Casimir Vogelsang

> ![[Ritterstadt vogelsang.jpg|300]]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
![[SP-GQ01 Portrait - Casimir Vogelsang.png|300]]

Forties, handsome and knows it, City-of-Greyhawk tailoring under a field coat, gloves he removes only to touch a relic.

## Personality & Mannerisms
Charming in public, cutting in faculty meetings. Praises every find and asks who else has seen it.

> *"Provenance is the only morality a relic has."*

## Goals & Secrets
- **Wants:** the Wardenship, and a find great enough to carry his name to the Regents.
- **Feuds with:** [[Professor Wilhelmina Brandt]] and [[Magistra Odilia Sternwald]].
- **Secret:** he is the Regents' Commission's man on the faculty and reports to [[Commissioner Lucan Dray]] directly. He is not corrupt. He believes the Fiend's Embrace belongs in the City of Greyhawk and that the station's job is to find things worth sending.

## Role & Context
> [!art]+ Portrait

> Head of the Department of Antiquities. Ambitious, polished, and the Regents' favourite. Feuds with Professor Brandt and Magistra Sternwald, and expects the Wardenship.

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
**Noble** (MM p. 348), Intelligence 16, expertise in History.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-06, RG-08, RG-09 · [[Faction — The Regents' Commission]]
- [[SP-GA01-The-False-Arrow]] — Scene 0 (Field Station frame); a student who took his Antiquities lectures recognises the fletching (Scene 4)
- [[SP-GQ01-The-Gaolers-Link]]: keeper of record for the Gaoler's Link; Scenes 03, 05, 07, 08
- [[SP-GQ00 — Prologue — The Crossing]]: Scene 7 (receives the Chancellor's letter)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
A **placeholder department head** in the campaign vault's `04 — Department of Antiquities`. Anything beyond that note is Gazetteer elaboration; a full campaign note overrides this one.

## Continuity

## His Department
**Major:** Archaeology · **Minors:** Epigraphy & Iconography · Appraisal & Provenance. His lecturer: [[Lecturer Fennimore Tock]] (Epigraphy & Iconography). Appraisal practicals are held at [[The Assay House]].
