---
type: npc
status: alive
canon: false
faction: Candlecrown
location: '[[Candlecrown]]'
aliases: [Pell Pike, Ash Pike]
species: Human
heritage: ''
gender: Male
age: Young Adult
alignment: ''
occupation: Toymakers
class: None (NPC)
subclass: ''
prestige_class: ''
level: ''
adventure_role: ally
disposition: friendly
party_trust: ''
items: []
connected_quests: []
connected_groups: []
parents: [Jory Pike, Mab Pike]
partner: []
children: []
siblings: []
allies: ['[[Ivo Pike]]']
enemies: []
deceased_date: ''
tags: [candlecrown, toymakers, twins, sp-gs02]
---

# Pell and Ash

> Candlecrown's toymaker twins, nineteen, who know the old mine from childhood games and want their Needfest gifts delivered. [Fortubo]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Identical, freckled, sawdust in their hair. Pell wears a red scarf and Ash a blue one, except when they swap to confuse people. **Memorable:** they finish each other's sentences and argue about the endings.

## Personality & Mannerisms
Cheerful, quick, brave in a careless way. Pell is the bolder; Ash is the cleverer and has the key to the coal-store hatch.

## Goals & Secrets
- **Wants:** their gifts delivered on time (they carved half of them). *Fears:* that the gifts won't go down, and that their father will learn about the key.
- **Knows:** the mine as far as M4 ("the ghost tunnels"); a door with a hammer on it they never opened (M5). Ash can find the way down blind.
- **Reacts:** guide the party as far as M4. Ash turns back at the first sign of trouble; Pell stays if asked. On the Short Day they run oil and build anything the party asks. Pell is Aurel's first choice for a thrall.

## Role & Context
The Pike twins: grandsons of [[Ivo Pike]], sons of Jory and Mab Pike (Pike household).


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
**Commoner** (MM p. 345), each.

## Appearances
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — Scenes 02, 04 (Pell finds the tyrg), 05 (guides), 09, 10, 12 (they make the party's figure and the Long Night Lantern).

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
If Pell was Aurel's thrall, he recovers in three days and remembers nothing; the twins never swap scarves again.
