---
type: npc
status: alive
canon: false
faction: Candlecrown
location: '[[Candlecrown]]'
aliases: []
species: Human
heritage: ''
gender: Female
age: Adult
alignment: ''
occupation: Oil-renderer and cooper
class: None (NPC)
subclass: ''
prestige_class: ''
level: ''
adventure_role: ally
disposition: friendly
party_trust: '0'
items: []
connected_quests: []
connected_groups: []
parents: []
partner: [Brom Carrow]
children: []
siblings: []
allies: []
enemies: []
deceased_date: ''
tags: [candlecrown, the-tors, sp-gs02]
---

# Edda Carrow

> Keeper of Candlecrown's oil-house, who presses, barrels and counts every flask of lantern oil on the crown. [Fortubo]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Forty, solid, smelling faintly of tallow, a tally-stick behind one ear. **Memorable:** the stencil-burn of a lantern on the back of one hand, from her first barrel.

## Personality & Mannerisms
Careful, tight-fisted, fair. Counts out loud. **Quirk:** taps each flask she hands over and names its number.

## Goals & Secrets
- **Wants:** the oil used well. Forty gallons is all there is until spring.
- **Knows:** exactly how much oil, rope and pitch the village has; how to make fire pots.
- **Fears:** running dry on the Long Night.

## Role & Context
Head of the Carrow household (5): Edda; her husband Brom (gate-watch); three children. She runs [[The Carrow Oil-House]].

## Conversation Guide
| Topic | Freely discussed? | Notes / sample line |
|---|---|---|
|  |  |  |

## Services
| Service | Cost / notes |
|---|---|
| Lantern oil, flasks | 1 sp each (free on the Short Day) |
| Fire pots (Scene 09) | free |

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
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — [[Scene 09 — The Short Day]] (fire pots, the lantern line); [[Candlecrown]] (household 10).

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
If the party wastes oil, she tells Brannoc. If they use it well, she names a barrel after them.
