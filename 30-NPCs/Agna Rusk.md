---
type: npc
status: alive
canon: false
faction: Candlecrown
location: '[[Candlecrown]]'
aliases: [Widow Rusk]
species: Human
heritage: ''
gender: Female
age: Elder
alignment: ''
occupation: Straw-weaver
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
allies: []
enemies: []
deceased_date: ''
tags: [candlecrown, the-tors, sp-gs02]
---

# Agna Rusk

> The widow Rusk, who weaves the packing straw for every lantern that leaves Candlecrown, and who hears the singing wind in her one good ear. [Telchur]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Sixty-eight, round, deaf in the left ear, always turning her right side to whoever's speaking. **Memorable:** straw in her hair, her sleeves, her bread.

## Personality & Mannerisms
Cheerful, nosy, a little alarming. Repeats things to make sure she heard them. **Quirk:** reads the weather off her bad knee and is never wrong.

## Goals & Secrets
- **Wants:** company, and to be believed about the wind.
- **Knows:** she heard the carol in the wind three nights before the party came, "all seven verses, and none of us singing." Her knee says the storm won't break "until something's paid."
- **Fears:** being told she's going deaf in the other ear too.

## Role & Context
Head of the Rusk household (3): Agna and two straw apprentices from the Vossmer brood.

## Conversation Guide
| Topic | Freely discussed? | Notes / sample line |
|---|---|---|
| The wind | Yes | "All seven verses, dear. And none of us singing." |
| The weather | Yes | "My knee says it won't break till something's paid." |

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
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — [[Candlecrown]] (household 6); rumor and weather lore in [[Scene 02 — Candlecrown at Needfest]] and [[Scene 03 — The Second Day]].

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
A party that sits with her gets Mother Sedge's rumor ("listen to the wind") a night early.
