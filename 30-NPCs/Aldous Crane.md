---
type: npc
status: missing
canon: false
faction: Hollow Ford
location: The mill, Hollow Ford
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
tags: [hallows-eve-quartet, sp-hal-01, miller, straw-double]
---

# Aldous Crane

> The miller of Hollow Ford, and the first villager Auntie Chaff took. The one at the bar is a Straw Double with three phrases.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Floury, stooped, a miller's smock. Smells of wet hay and river water if you stand close enough.

## Personality & Mannerisms
**The double:** repeats the same three phrases in the same cadence: *"Closed for repairs." "Be right as rain by spring." "Nothing to see up there."* Doesn't drink the ale in front of him. If asked anything outside the three phrases, says one of them anyway.
**The real Aldous:** quiet, decent, proud of his wheel, and the first to swear it has never once turned the wrong way.

## Goals & Secrets
*The double wants:* the mill left alone. It bars the mill door from the inside each night and walks the footprint path through the flour to the loft. *Secret:* Widow Haskell says "closed for repairs" in exactly his cadence, because she wrote the phrase.

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
Straw Double (standard, 9 hp); see [[SP-OS01 — Bestiary]]. The real Aldous is a **commoner** (MM 345), asleep in M4.

## Appearances
- [[SP-OS01-Straw-Men]] — Scene 00 (at the bar), Scene 04 (his cadence in Haskell's mouth), Scene 05 (wakes in M4; the mill is his).

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
If the real Aldous wakes, he rebuilds the wheel to turn the right way and never speaks of the three weeks. If the party wedged his wheel with something valuable, he keeps it on the wall above the millstone.
