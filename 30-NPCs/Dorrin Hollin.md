---
type: npc
status: alive
canon: false
faction: The Quag Bargemen (halfling ferry)
location: Ritterstadt — the Landing
aliases: [Dorrin, the Ferryman]
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
tags: [ritterstadt, halfling, ferryman, landing, founders, gazetteer]
---

# Dorrin Hollin

> Halfling ferryman at the Landing, and nephew of the Founder Tam Hollin, the guide lost in the Mires in 569. He runs the one halfling boat among the Rhennee barges.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Thirties, sun-browned, barefoot in every season, his uncle's brass compass on a thong around his neck.

## Personality & Mannerisms
Easy-going, loyal, a good storyteller who never tells the same story twice. Takes the late crossings nobody else will.

> *"Uncle Tam always said the Mire has three paths: in, out, and the one that keeps you."*

## Goals & Secrets
- **Wants:** to find out what happened to his uncle, and to recover Tam's third map — the one marking a dry path to Cold Stone Keep.
- **Allied with:** [[Baba Yeska Marovna]], who has never once charged him a toll.
- **Secret:** his uncle's compass doesn't point north near the Hush. It points at the Wachturm.

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
**Commoner** (MM p. 345) with halfling traits; boat handling expertise.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-01, RG-03 · [[Faction — The Quag Bargemen]]

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
