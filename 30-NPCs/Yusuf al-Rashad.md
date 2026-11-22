---
type: npc
status: alive
canon: false
faction: Ritterstadt — merchants
location: Ritterstadt — Market Hill (the stone stall)
aliases: [Yusuf, al-Rashad]
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
tags: [ritterstadt, merchant, baklunish, ket, cloth, salt, gazetteer]
---

# Yusuf al-Rashad

> A Baklunish cloth-and-salt merchant up from Ket. His is the only stone-built stall on Market Hill, and the only reliable source of dyed cloth north of Traft.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Fifty, round, immaculate, a Ket turban in indigo, rings on every finger he does not need for counting.

## Personality & Mannerisms
Courtly, patient, and loves a long negotiation. Pours tea before naming a price.

> *"A price is a conversation. Sit. We are only at the beginning."*

## Goals & Secrets
- **Wants:** a factor's house in Ritterstadt and his family brought north from Ket.
- **Friends:** [[Lecturer Perenna Dolz]], to whom he brings letters from home.
- **Doesn't know:** that the Pale Ledger sews its calfskin ledger into the bolts he ships to Traft twice a year.

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
**Noble** (MM p. 348), merchant; two hired guards in season.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-03, RG-04, RG-05 · [[Faction — The Pale Ledger]]

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
