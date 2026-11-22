---
type: npc
status: alive
canon: false
faction: Greyhawk University — Ritterstadt Field Station
location: Ritterstadt — the Long Dormitory
aliases: [the Proctor, Proctor Grell, Mathias Grell]
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
tags: [ritterstadt, greyhawk-university, proctor, discipline, administration, gazetteer]
---

# Mathias Grell

> Proctor of Students. A former Traft watchman of thirty-six who keeps discipline, the gate rota, and the student organizations' charters from his room at the end of the Long Dormitory.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
![[SP-GQ01 Portrait - Mathias Grell.png|300]]

Flan, lean, short-cropped hair, a watchman's leather coat he still wears, and a whistle on a cord.

## Personality & Mannerisms
Fair, humourless, and respected. Never raises his voice; writes everything down. Knows every student's name and their worst night.

> *"I am not your mother. I am the man who decides whether your mother hears about this."*

## Goals & Secrets
- **Wants:** no student dead on his rota.
- **Runs:** the eastern-gate breach watch since 18 Planting.
- **Secret:** he suspects the Curio Club is selling Bloom crystals and hasn't proved it.

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
**Guard** (MM p. 347), Wisdom 14; a cudgel and the whistle.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-02, RG-04, RG-08, RG-09
- [[SP-GQ01-The-Gaolers-Link]]: the Proctor; the inquiry; Scenes 05, 08

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
