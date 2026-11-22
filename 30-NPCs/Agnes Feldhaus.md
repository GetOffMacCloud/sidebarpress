---
type: npc
status: alive
canon: false
faction: Greyhawk University — Ritterstadt Field Station
location: Schwartzenbruin — the University Post-House
aliases: [Feldhaus, Factor Feldhaus]
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
tags: [shadow-on-the-quag, greyhawk-university, schwartzenbruin, functionary]
---

# Agnes Feldhaus

> The University's factor in Schwartzenbruin: she receives the City's post for the Ritterstadt Field Station and sends it north on whatever ship is going.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
![[SP-GQ00 Portrait - Agnes Feldhaus.png|300]]
Grey-haired, sixty, spectacles on a ribbon, ink and sealing-wax on her fingers.

## Personality & Mannerisms
Brisk, kind to students, too loud on the waterfront.
> *"That one goes into Professor Vogelsang's hand and no other."*

## Goals & Secrets
- *Deity:* {Zilchus}
- **Wants:** the post delivered and no questions. **Knows:** the Chancellor's letter came up the Velverdyva with the river post; she has no idea what's in it. **Reacts:** helpful → flustered if anything goes wrong → writes to the Registrar.

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
**Commoner** (MM p. 345).

## Appearances
- [[SP-GQ00 — Prologue — The Crossing]]: Scene 1

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
She can send the party's letters to Schwartzenbruin in GQ3. Named per the functionaries rule (2026-10-23).
