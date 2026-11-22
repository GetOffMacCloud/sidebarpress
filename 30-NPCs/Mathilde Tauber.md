---
type: npc
status: alive
canon: false
faction: Ritterstadt — the Moot (Tauber household)
location: Ritterstadt — the Taubers' lane; Market Hill
aliases: [Mathilde, Frau Tauber]
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
tags: [ritterstadt, market, moot, gazetteer]
---

# Mathilde Tauber

> Wife of the Moot Speaker [[Reinholt Tauber]]. She runs the market on Market Hill, the Needfest Fair, and most of her husband's politics.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Fifties, small, sharp-eyed, a market-mistress's satchel of tallies and a voice that carries across the hill without being raised.

## Personality & Mannerisms
Organised, generous with credit, merciless with cheats. Knows every stallholder's prices and every household's debts.

> *"Two coppers a day. One silver on fair days. And whatever you owe the baker, which I also know."*

## Goals & Secrets
- **Wants:** a covered market hall before her knees give out.
- **Runs:** stall fees for the Moot (2 cp a day, 1 sp on fair days).
- **Secret:** she counts the Pale Ledger's comings and goings without knowing what she's counting, and has noticed the tailor ships more than he sews.

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
- [[Ritterstadt — Gazetteer (Book)]] — RG-03, RG-04

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
