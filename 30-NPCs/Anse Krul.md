---
type: npc
status: alive
canon: false
faction: Hired by Sivert Vuurzward
location: Lake Quag
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
tags: [lake-quag, farrier, saboteur, sp-pbs-00]
---

# Anse Krul

> A farrier who lames horses for money and calls it a trade.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Thin, scarred farrier's hands with a burn across one palm. Was aboard the Kortheim Maid before the party.

## Personality & Mannerisms
Describes cruelty as craftsmanship. Runs before he fights.

## Goals & Secrets
- **Wants:** his forty marks.
- **Knows:** that Vuurzward's man paid him 20 marks at Osterschlauss and gave him the boat and the day ten days back; not who told them.
- **Reacts:** needs three uninterrupted rounds in the stall. Cornered, he talks; captured, he names Vuurzward without much pressing.

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
**Spy** (MM p. 349) with changes; see [[SP-GA00 — Bestiary]].

## Appearances
- [[SP-GA00-Nobodys-Colors]] — Scene 4; Scene 6 at APL 3–4 if he escaped

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. Clan Vuurzward is Living Greyhawk material; see [[Perrenland-Mercenary-Companies]].

## Continuity
None.
