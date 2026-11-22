---
type: npc
status: alive
canon: false
faction: Schwartzenbruin border patrol
location: Schwartzenbruin
aliases: []
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
tags: [schwartzenbruin, patrol, sp-pbs-00]
---

# Sergeant Ruwen Hask

> The lake-gate patrol sergeant at Schwartzenbruin, who meets every boat with a lantern and three questions.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
![[SP-GQ00 Portrait - Ruwen Hask.png|300]]
A patrol coat, a lantern, and a clerk at his elbow with a ledger on a stand.

## Personality & Mannerisms
Courteous and patient; he writes everything down and compares it with the next answer.

## Goals & Secrets
- **Wants:** every answer recorded.
- **Knows:** what every boat carried in, as told to him.
- **Reacts:** asks "Business. Lodging. Company." of each passenger; records an undeclared horse in his ledger. Changes nothing in this adventure.

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
Not fought; **commoner** (MM p. 345) if needed.

## Appearances
- [[SP-GA00-Nobodys-Colors]] — Scene 4 (Transition, the lake-gate)
- [[SP-GQ00 — Prologue — The Crossing]]: Scene 1 (the lake-gate; his ledger logs Fesch)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. *SP-GA03's dock sergeant at the same lake-gate is unnamed; he can be Hask, if that ruling goes this way.*

## Continuity
None.
