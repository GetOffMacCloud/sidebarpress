---
type: npc
status: alive
canon: false
faction: Candlecrown
location: Candlecrown
aliases: []
species: ''
heritage: ''
gender: ''
age: ''
alignment: ''
occupation: ''
class: ''
subclass: ''
prestige_class: ''
level: ''
adventure_role: ''
disposition: ''
party_trust: ''
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
tags: [candlecrown, singer, sp-gs02]
---

# Wenna Tull

> Lead singer of the Long Night Carol, the elder's daughter, and the one person in Candlecrown who wrote the seventh verse down. [Telchur]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Twenty-six, tall, red-haired, with her father's shoulders. **Memorable:** a voice that carries across the whole crown without seeming to try.

## Personality & Mannerisms
Confident in the hall, shy everywhere else. Loves the carol more than anything and is terrified of being the one who loses it. **Quirk:** taps out the beat on her thigh when she's nervous.

## Goals & Secrets
- **Wants:** to sing the seventh verse once more. *Fears:* that the verse will die with Mother Sedge.
- **Knows:** the sounds of all seven verses (not the meaning of the seventh); that she has written the seventh verse's sounds on a lantern-paper in her sewing box.
- **Reacts:** keeps rehearsing whatever the danger; loses her voice in Scene 07. Afterward, guilty, she writes *I'M SORRY* and gives up the paper to anyone kind enough to ask. Will help write the false verse (by gesture and paper).

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
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — Scenes 02, 07, 09, 11, 12. Her paper is the written verse (the lure, or a payment).

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
If her voice comes home, she leads the carol next year with all seven verses. If not, she teaches it to Tansy by writing, which Mother Sedge allows.
