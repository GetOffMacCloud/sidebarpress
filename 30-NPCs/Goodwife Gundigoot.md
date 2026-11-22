---
type: npc
status: alive
canon: false
faction: Hommlet
location: Inn of the Welcome Wench
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
tags: [hommlet, sp-gs01]
---

# Goodwife Gundigoot

> Ostler Gundigoot's wife and the reason the Welcome Wench's door stays open every Brewfest.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Broad, floury and quick, sleeves rolled, a ring of keys at her belt. Never seen sitting down.

## Personality & Mannerisms
Practical and warm. Explains things while doing three other things. Says the important part last.

## Goals & Secrets
- **Wants:** the Open Door kept, whatever comes through it.
- **Knows:** why the door stays open: a family he'd never met fed her husband when he walked into Hommlet with nothing after the battle.
- **Reacts:** explains the custom while wedging the door wider; during the feast fight she stands in the doorway and won't move; the Gundigoot household's first pour is hers to give.

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
- [[SP-GS01-The-Gluttonwretch-of-Hommlet]] — Scenes 01, 04 (the Gundigoot household), 07

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
T1 names Ostler Gundigoot's wife but gives her no detail; everything here is homebrew. See [[Ostler Gundigoot]].

## Continuity
Keeps the Open Door every Brewfest after Ending A.
