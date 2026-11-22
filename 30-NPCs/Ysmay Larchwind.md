---
type: npc
status: alive
canon: false
faction: The Larch kin-band
location: Ritterstadt — the Larch camp; the Hush
aliases: [Ysmay]
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
tags: [ritterstadt, elf, sylvan, ranger, hush, training, gazetteer]
---

# Ysmay Larchwind

> Ranger of the Larch kin-band. She runs the elves' watch on the Hush and teaches archery and woodcraft at the camp for a price in grain.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Young by elf reckoning, lean, larch-green cloak, a longbow she never strings inside the palisade.

## Personality & Mannerisms
Quiet, watchful, and fiercely protective of [[Caelith of the Larch]]. Tests students by making them stand still in the trees for an hour.

> *"The Hush is not empty. It is listening. Be worth listening to, or be quiet."*

## Goals & Secrets
- **Teaches:** archery and woodcraft at the Larch camp (paid in grain).
- **Knows:** where the Hush is thickest — and the kin-band has not told the University.
- **Secret:** she has seen the same pale figure at the Hush's edge three nights running. She thinks it's one of the two watchmen who died on 18 Planting.

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
**Scout** (MM p. 349) with elf traits; longbow +6.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-03, RG-04

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
