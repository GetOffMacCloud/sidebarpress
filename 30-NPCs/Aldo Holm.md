---
type: npc
status: alive
canon: false
faction: Candlecrown
location: '[[Candlecrown]]'
aliases: []
species: Human
heritage: ''
gender: Male
age: Elder
alignment: ''
occupation: Retired miner's son; village memory
class: None (NPC)
subclass: ''
prestige_class: ''
level: ''
adventure_role: informant
disposition: friendly
party_trust: '0'
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
tags: [candlecrown, the-tors, sp-gs02]
---

# Aldo Holm

> Ninety-one, the oldest soul on the crown, whose grandfather sealed the mine head and who remembers why the miners stopped going down. [Fortubo]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Tiny, bald, wrapped in a bearskin by the fire. **Memorable:** a miner's brass tally-tag on a cord round his neck, his grandfather's.

## Personality & Mannerisms
Sharp in the morning, wandering by evening. Loves an audience. **Quirk:** taps out old mine signals on the arm of his chair.

## Goals & Secrets
- **Wants:** someone to listen to the whole story before he dies.
- **Knows:** his grandfather sealed the shaft (C9) after "a hunter crawled in from the cliffs with a piece of blue ice and died of the cold in it" (M3; Facts 2 and 5). The miners bricked the coal-store doorway and nailed the chapel shut. "Grandad said the chapel had the words in it, and the words were the dangerous part."
- **Fears:** forgetting it before he tells it.
- **How to reveal it:** visit in the morning, sit, and let him talk.

## Role & Context
Head of the Holm household (5): Aldo; his daughter Bettany; her husband Rolf (gate-watch); two grandchildren.

## Conversation Guide
| Topic | Freely discussed? | Notes / sample line |
|---|---|---|
| The old mine | In the morning | "Grandad sealed it. A hunter crawled in with a piece of blue ice and died of the cold in it." |
| The chapel | If pressed | "The words were the dangerous part." |

## Services
| Service | Cost / notes |
|---|---|
|  |  |

## Quest Hooks
| Hook | Leads to | Trigger |
|---|---|---|
|  |  |  |

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
**Commoner** (MM p. 345), 2 hit points.

## Appearances
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — [[Scene 03 — The Second Day]] (an extra route to Facts 2 and 5, if visited); [[Candlecrown]] (household 12).

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
If he dies before Needfest 7, the village buries him with his grandfather's tally-tag; the party is asked to carry him.
