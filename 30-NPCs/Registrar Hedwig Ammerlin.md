---
type: npc
status: alive
canon: false
faction: Greyhawk University — Ritterstadt Field Station
location: Ritterstadt — the Station House
aliases: [the Registrar, Registrar Ammerlin, Hedwig Ammerlin]
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
tags: [ritterstadt, greyhawk-university, registrar, administration, gazetteer]
---

# Registrar Hedwig Ammerlin

> Registrar of the Academic Registry: enrollment, the credit ledgers, declarations of major, and the sealed files. The station's conscience and its bureaucracy in one.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
![[SP-GQ01 Portrait - Hedwig Ammerlin.png|300]]

Forty-four, Perrender, square-built, spectacles on a cord. A ring of keys at her belt that she never sets down, even at the Fiend's Rest.

## Personality & Mannerisms
Precise, unhurried, and unexpectedly kind to students who tell the truth. Corrects dates in other people's sentences. Keeps the seal-wax in her sleeve.

> *"It is in the ledger, or it did not happen. Would you like it to have happened?"*

## Goals & Secrets
- **Wants:** the ledgers to balance and every student's name to leave the station alive.
- **Holds:** the sealed files — AR-001, Hassenrath's second notebook, the Founders' Compact correspondence — under the Chancellor's standing instruction.
- **Secret:** she has read all of them. She has never said so, and the Archivist knows she has.

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
Noncombatant. **Commoner** (MM p. 345) with Intelligence 15 and proficiency in Investigation.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-02, RG-04, RG-08, RG-09
- [[SP-GQ01-The-Gaolers-Link]]: holds the sealed-stacks key at the Warden's dinner; Scenes 03, 05

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
Record which sealed files have been opened, by whom, and under whose order.
