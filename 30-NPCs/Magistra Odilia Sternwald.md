---
type: npc
status: alive
canon: false
faction: Greyhawk University — Department of Arcane Studies
location: Ritterstadt
aliases: [Sternwald, Magistra Sternwald]
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
tags: [ritterstadt, greyhawk-university, department-head, arcane, gazetteer]
source_canon: A Tourist In Greyhawk — 01 — Department of Arcane Studies (placeholder head)
---

# Magistra Odilia Sternwald

> ![[Ritterstadt sternwald.jpg|300]]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Sixty, tall and spare, iron-grey hair pinned flat, a wizard's grey robe with the University arms embroidered small at the collar.

## Personality & Mannerisms
Lectures standing, never sits in another's presence, and will not repeat a question she considers careless.

> *"Magic is a tool. The Rain was a tool. Sit down."*

## Goals & Secrets
- **Wants:** the Bloom crystals classified as Arcane Studies property, and a laboratory nobody else can book.
- **Feuds with:** Vogelsang (over relics) and everyone (over lab space).
- **Secret:** she believes the Bloom is a working, not a weather, and has begun to suspect whose.

## Role & Context
> [!art]+ Portrait

> Head of the Department of Arcane Studies. Severe, exacting, and distrustful of sorcerers on principle. Wants every Bloom crystal in the station under her lock.

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
**Mage** (MM p. 347).

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-08, RG-09

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
A **placeholder department head** in the campaign vault's `01 — Department of Arcane Studies`. Anything beyond that note is Gazetteer elaboration; a full campaign note overrides this one.

## Continuity

## Her Department
**Major:** Arcane Research · **Minors:** Thaumaturgic Analysis · Divination & Omenry. Her lecturer: [[Lecturer Perenna Dolz]] (Divination & Omenry).
