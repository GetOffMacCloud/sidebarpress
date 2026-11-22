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
occupation: Master painter
class: None (NPC)
subclass: ''
prestige_class: ''
level: ''
adventure_role: color
disposition: friendly
party_trust: '0'
items: []
connected_quests: []
connected_groups: []
parents: []
partner: []
children: [Jory Pike]
siblings: []
allies: ['[[Brannoc Tull]]']
enemies: []
deceased_date: ''
tags: [candlecrown, the-tors, sp-gs02, painter]
---

# Ivo Pike

> Candlecrown's oldest painter, who painted the six panes of the Carol Lantern fifty years ago and still keeps the blank seventh frame in his attic. [Fortubo]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Seventy-four, stooped, with paint in the creases of his knuckles that no soap reaches. **Memorable:** a magnifying lens on a ribbon round his neck that he peers through at everything, faces included.

## Personality & Mannerisms
Precise, gentle, deaf to anything he doesn't want to hear. **Quirk:** names colors instead of things ("pass me the winter-blue" means the cup).

## Goals & Secrets
- **Wants:** his grandsons [[Pell and Ash]] to take over the brushes, and the Carol Lantern's panes repainted before he dies.
- **Knows:** the Carol Lantern was made with six panes "because there's no seventh to paint"; the blank seventh frame is in his attic. His grandfather was told never to paint it.
- **Fears:** that the boys will go down the old mine again.
- **How to reveal it:** ask him about the lantern; he'll show the frame to anyone who admires his panes.

## Role & Context
Head of the Pike household (6): Ivo; his son Jory and daughter-in-law Mab, painters; grandsons Pell and Ash, 19; granddaughter Wren, 12.

## Conversation Guide
| Topic | Freely discussed? | Notes / sample line |
|---|---|---|
| The Carol Lantern | Yes | "Six panes. There's no seventh to paint." |
| The seventh frame | If asked kindly | "My grandfather made me swear. I never asked why." |

## Services
| Service | Cost / notes |
|---|---|
| Portrait of a party member, painted tin | 5 gp; a week |

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
**Commoner** (MM p. 345).

## Appearances
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — [[Candlecrown]] (household 4); the blank seventh frame can serve as the written-verse lure in [[Scene 09 — The Short Day]].

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
If the seventh frame is painted with the verse, Hrimvald wants it more than Wenna's paper.
