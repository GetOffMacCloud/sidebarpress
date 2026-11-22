---
type: npc
status: alive
canon: false
faction: The Mining Consortium (Forge Row)
location: Ritterstadt — Forge Row; the margin bogs
aliases: [Orrim, the Foreman]
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
tags: [ritterstadt, dwarf, foreman, bog-iron, peat, gazetteer]
---

# Orrim Stoneweir

> The Mining Consortium's cutting foreman on Forge Row. He runs the crews that cut peat and dig bog iron in the margin bogs, under factor [[Drunik Runevault]].

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Broad, bow-legged, mud to the thigh in every season, a cutting-spade over his shoulder like a halberd.

## Personality & Mannerisms
Loud, practical, protective of his crews. Measures distance in spade-lengths and danger in how quiet the bog gets.

> *"When the frogs stop, you stop. When the frogs start again, you run."*

## Goals & Secrets
- **Wants:** a second season's iron before the Bloom closes the bogs.
- **Has seen:** black ice in the cuttings in Planting, a month before anyone else.
- **Secret:** a Traft factor offered him twice the Clatspur price for a season's iron, delivered to a barge at night. He hasn't said no.

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
**Thug** (MM p. 350) with dwarf traits; a spade (as a battleaxe).

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-03, RG-05

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
