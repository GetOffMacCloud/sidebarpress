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
occupation: Master carver
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
partner: [Liesl Vossmer]
children: [Jakob Vossmer, Lute Vossmer]
siblings: []
allies: ['[[Brannoc Tull]]']
enemies: []
deceased_date: ''
tags: [candlecrown, the-tors, sp-gs02, carver]
---

# Garth Vossmer

> Candlecrown's master carver and father of seven, whose two eldest sons stand on the gate-watch. [Fortubo]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Forty-five, huge, gentle-handed, a beard full of wood shavings. **Memorable:** carves while he talks, and has always just finished a tiny goose he gives to the nearest child.

## Personality & Mannerisms
Slow-spoken, calm, deeply loyal to Brannoc. **Quirk:** measures everything in handspans.

## Goals & Secrets
- **Wants:** his family safe and the Needfest figures finished on time.
- **Knows:** the workshop floor; which planks are rotten over the coal store; how to build a barricade fast.
- **Fears:** losing a son on the gate.

## Role & Context
Head of the Vossmer household (9): Garth; his wife Liesl; seven children, of whom Jakob (20) and Lute (18) are on the gate-watch.

## Conversation Guide
| Topic | Freely discussed? | Notes / sample line |
|---|---|---|
|  |  |  |

## Services
| Service | Cost / notes |
|---|---|
| Carved figure to order | 1–10 gp |
| Barricade work (Scene 09) | free |

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
**Commoner** (MM p. 345); his sons are **guards** (MM p. 347).

## Appearances
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — [[Scene 09 — The Short Day]] (he leads the workshop crew: barring the coal store, the singing room); [[Candlecrown]] (household 9).

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
If a Vossmer son dies in the siege, Garth carves the party's Needfest figure himself, and leaves one figure out.
