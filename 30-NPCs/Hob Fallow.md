---
type: npc
status: alive
canon: false
faction: Candlecrown
location: '[[The Fallow Kiln]]'
aliases: []
species: Human
heritage: ''
gender: Male
age: Adult
alignment: ''
occupation: Kiln-man and glassblower
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
partner: ['[[Marra Fallow]]']
children: []
siblings: []
allies: []
enemies: []
deceased_date: ''
tags: [candlecrown, glassblower, gossip, sp-gs02]
---

# Hob Fallow

> Candlecrown's kiln-man and glassblower, and its best source of gossip. [Fortubo]

**Loyal to:** Marra and the kiln, then a good story.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Round, bald, red-faced from the kiln, with burn-spotted sleeves. **Memorable:** blows into his hands every time he stops talking.

## Personality & Mannerisms
Talkative, superstitious, generous. **Quirk:** blames Telchur for everything.

## Goals & Secrets
- **Wants:** a quiet Needfest and his bricks paid off. *Fears:* the shrine being neglected.
- **Knows:** the old silver story; that the miners stopped going down "after a man died down there"; who's sweet on whom.
- **Reacts:** tells rumors to anyone with a mug (rumors 1 and 8). If the party guards Corin on Needfest 1, Hrimvald takes Hob's voice instead; he then writes everything Corin would have drawn, and adds, "It knew my name."

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
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — Scenes 02, 03 (rumors; a possible victim).

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
Owes the elder 20 gp for kiln bricks.
