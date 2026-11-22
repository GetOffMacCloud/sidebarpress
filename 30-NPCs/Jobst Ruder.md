---
type: npc
status: alive
canon: false
faction: ''
location: Ritterstadt
aliases: [Jobst Ruder]
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
tags: [perrenland, lake-quag, sailor, shadow-on-the-quag, SP-GQ01]
---

# Jobst Ruder

> Master of the Graue Hecht, a Perrender lake-master in his fifties, loyal to Brandmeier and hostile to the clerk. Not tethered.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
![[SP-GQ01 Portrait - Jobst Ruder.png|300]]

Weathered and slow-spoken; whittles while he watches the shore.

## Personality & Mannerisms
> *"He's not been right since spring. I knew it."*

## Goals & Secrets
- *Deity:* [Osprem]
- **Wants:** his master back and his ship home. **Knows:** the stores are wrong for Schwartzenbruin; the clerk signs everything. **Reacts:** surly → helpful once shown F2 → refuses to sail with the clerk aboard.

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
**Veteran** (MM p. 350), if needed; he doesn't fight students.

## Appearances
- [[SP-GQ01-The-Gaolers-Link]]: Scenes 03, 06, 07
- [[SP-GQ00 — Prologue — The Crossing]]: Scenes 2–5

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
Freed of the clerk, he sails Brandmeier home, and he'll carry the party across the lake for free in SP-GQ03. Named per the functionaries rule (2026-10-23).
