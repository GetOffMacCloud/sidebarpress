---
type: npc
status: alive
canon: false
faction: Greyhawk University — Department of Arcane Studies
location: Ritterstadt
aliases: [Perenna Dolz, Lecturer Dolz]
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
tags: [ritterstadt, greyhawk-university, lecturer, divination, baklunish, gazetteer]
---

# Lecturer Perenna Dolz

> Lecturer in Divination & Omenry, Department of Arcane Studies. Ket-born Baklunish, thirty-nine. Reads the weather for the Landing and the omens for anyone who asks a better question.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
![[SP-GQ01 Portrait - Perenna Dolz.png|300]]

Dark-eyed, quick, wrapped in a Ket shawl over her University gown, a pouch of knucklebones at her belt.

## Personality & Mannerisms
Wry and impatient with vague questions. Treats divination as a craft, not a mystery.

> *"The omen says yes. The omen always says yes. Ask it a better question."*

## Goals & Secrets
- **Wants:** a real observatory on the Wachturm rise.
- **Ally:** [[Yusuf al-Rashad]], who brings her letters from Ket.
- **Secret:** her omens around the Bloom keep returning the same symbol — a closed eye — and she hasn't told Sternwald.

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
**Mage** (MM p. 347), divination spells.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-09
- [[SP-GQ01-The-Gaolers-Link]]: the fog in her scrying; reads Fesch's hand; Scenes 03, 07, 08

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
