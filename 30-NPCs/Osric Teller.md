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
age: Adult
alignment: ''
occupation: Tally-keeper and storehouse warden
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
children: []
siblings: []
allies: ['[[Brannoc Tull]]']
enemies: []
deceased_date: ''
tags: [candlecrown, the-tors, sp-gs02]
---

# Osric Teller

> Candlecrown's tally-keeper, who keeps the storehouse, the gift ledger and a ring of keys he can't all account for. [Fortubo]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Fifty, thin, ink-stained, spectacles on a cord. **Memorable:** a ring of a dozen iron keys on his belt that jangles when he walks; he can name all but one.

## Personality & Mannerisms
Fussy, anxious, scrupulously honest. **Quirk:** writes down everything anyone tells him, then reads it back to them.

## Goals & Secrets
- **Wants:** the gift wagons down the Stair by Needfest 7, ledger balanced.
- **Knows:** every household's stores; that Ardo Pennick of Loftwick paid in advance (hook 1); the twelfth key fits "a door down below" nobody has opened in his lifetime (the chapel, M5).
- **Fears:** an unbalanced ledger more than tyrgs.

## Role & Context
Head of the Teller household (5): Osric; his wife Hanne; his mother; two children. He keeps [[The Teller Storehouse]].

## Conversation Guide
| Topic | Freely discussed? | Notes / sample line |
|---|---|---|
| The gift wagons | Yes | "Paid in advance. Every lantern accounted for." |
| The twelfth key | If asked | "It came with the job. It fits nothing up here." |

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
**Commoner** (MM p. 345).

## Appearances
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — [[Candlecrown]] (household 11); the gift ledger (hook 1) and the chapel key.

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
If the wagons go down late, he writes to Ardo Pennick himself, and the letter names the party.
