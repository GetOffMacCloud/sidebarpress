---
type: npc
status: alive
canon: false
faction: Greyhawk University — Department of Natural Sciences
location: Ritterstadt
aliases: [Grasmeyer, Professor Grasmeyer]
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
tags: [ritterstadt, greyhawk-university, department-head, natural-sciences, gazetteer]
source_canon: A Tourist In Greyhawk — 02 — Department of Natural Sciences (placeholder head)
---

# Professor Berthold Grasmeyer

> ![[Ritterstadt grasmeyer.jpg|300]]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Fifties, round, muddy to the knee, a vasculum on a strap and a notebook swollen with pressed leaves.

## Personality & Mannerisms
Delighted by everything, horrified by nothing, and slow to notice danger until it has a Latin name.

> *"Everything in the Mires is adapting to the cold. Including the things that were already dead."*

## Goals & Secrets
- **Wants:** a full natural history of the Sepia Uplands, published under his name in the City of Greyhawk.
- **Pays:** credits for live specimens, double for anything nobody has catalogued.
- **Secret:** his bog-adder has not shed its skin since the Bloom began. He is afraid to find out why.

## Role & Context
> [!art]+ Portrait

> Head of the Department of Natural Sciences. A field naturalist who keeps a live bog-adder in his rooms and believes the Mires are teaching everything in them to live with the cold.

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
**Druid** (MM p. 346), minus the faith; plus the bog-adder.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-08, RG-09

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
A **placeholder department head** in the campaign vault's `02 — Department of Natural Sciences`. Anything beyond that note is Gazetteer elaboration; a full campaign note overrides this one.

## Continuity

## His Department
**Major:** Natural Philosophy · **Minors:** Zoology & Beastmastery · Astronomy & Weatherlore. His lecturer: [[Lecturer Ilvadriel]] (Zoology & Beastmastery).
