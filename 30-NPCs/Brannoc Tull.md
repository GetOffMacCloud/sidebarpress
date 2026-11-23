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
occupation: Elder and master lantern-maker
class: None (NPC)
subclass: ''
prestige_class: ''
level: ''
adventure_role: patron
disposition: friendly
party_trust: ''
items: []
connected_quests: []
connected_groups: []
parents: []
partner: []
children: ['[[Wenna Tull]]']
siblings: []
allies: ['[[Garth Vossmer]]', '[[Osric Teller]]']
enemies: []
deceased_date: ''
tags: [candlecrown, the-tors, sp-gs02]
---

# Brannoc Tull

> Elder of Candlecrown and master lantern-maker, who would rather lie than cancel Needfest. [Fortubo]

**Loyal to:** the carol and Needfest, then Wenna, then Candlecrown's good name (he'll lie to protect all three).

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Sixty, broad as a door, with a grey beard singed short on one side by fifty years at the forge. Wears a leather apron to the feast. **Memorable:** burn-scarred hands that are always holding something: a lantern-hook, a mug, someone else's hand.

## Personality & Mannerisms
Warm, loud and stubborn. Makes speeches. Treats every guest as Fortubo's guest and every problem as something to keep quiet until it goes away. **Quirk:** taps any lantern he passes to check the glass.

## Goals & Secrets
- **Wants:** the carol sung and the gifts sent down, as every year since the founders. *Fears:* a panic, and the end of the village's trade if word spreads that Candlecrown is cursed.
- **Knows:** the village, the workshop, the trade, the founders' charter, the miners' map ("just an old map"); that Corin is mute (from Needfest 2).
- **Reacts:** **deny** ("Corin went down for help") → **redirect** (busies the party with the crates and the gifts) → **give in** when caught: leads them to the loft and asks their pardon. After that he's the party's strongest ally and does whatever they ask on the Short Day.

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
**Commoner** (MM p. 345), 8 hit points.

## Appearances
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — Scenes 02, 03, 07, 08, 09, 10, 12. Pays the party; gives them the Long Night Lantern.

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
If the village goes silent, he never forgives himself for hiding Corin. If it sings, he names the party's Needfest figure "the Lantern-Keepers."
