---
type: npc
status: alive
canon: false
faction: Candlecrown
location: '[[The Fallow Kiln]]'
aliases: []
species: Human
heritage: ''
gender: Female
age: Adult
alignment: ''
occupation: Feast cook
class: None (NPC)
subclass: ''
prestige_class: ''
level: ''
adventure_role: color
disposition: friendly
party_trust: ''
items: []
connected_quests: []
connected_groups: []
parents: []
partner: ['[[Hob Fallow]]']
children: []
siblings: []
allies: []
enemies: []
deceased_date: ''
tags: [candlecrown, cook, sp-gs02]
---

# Marra Fallow

> Hob's wife, and the cook who feeds Candlecrown's Needfest. [Telchur]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Tall, thin, flour to the elbows. **Memorable:** a wooden spoon she points like a sword.

## Personality & Mannerisms
Brisk, kind, unimpressed by heroes who don't eat. **Quirk:** counts heads at every meal.

## Goals & Secrets
- **Wants:** everyone fed. *Fears:* running out of goose.
- **Knows:** that Corin "went down for help" (the elder's lie; rumor 9); her grandmother's belief that the seventh verse keeps the winter off (rumor 7, false).
- **Reacts:** feeds the party whether they like it or not; notices first when someone is missing from a meal.

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
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — Scenes 02, 03, 09, 12.

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
Her Needfest porridge is the last taste of the adventure.
