---
type: npc
status: alive
canon: false
faction: Candlecrown
location: '[[The Candlecrown Gate]]'
aliases: []
species: Human
heritage: ''
gender: Male
age: Adult
alignment: ''
occupation: Gate-warden
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
parents: []
partner: []
children: ['[[Tansy Kettle]]']
siblings: []
allies: []
enemies: []
deceased_date: ''
tags: [candlecrown, gate-warden, sp-gs02]
---

# Dob Kettle

> Candlecrown's gate-warden, a widower with a lantern on a pole, who hums his dead wife's verse on watch. [Fortubo]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Fifty, lean, with a drooping moustache white with frost. A spear he uses mostly as a walking stick. **Memorable:** a lantern on a ten-foot pole that he waves at everything.

## Personality & Mannerisms
Dry, watchful, kind. Keeps count of things: tyrgs, lanterns, strangers. **Quirk:** talks to the gate.

## Goals & Secrets
- **Wants:** his daughter safe and his gate shut. *Fears:* the cold man Tansy talks about, and his own memory of seeing him on the cliff.
- **Knows:** the Stair and the tyrgs (he counts 16 and the alpha); that he saw "a man standing on the cliff" two nights before the party came (Aurel).
- **Reacts:** waves the party up the Stair; holds the gate in every wave; loses his voice in Scene 04 (by default) and writes on a slate after that. Defers to the party at the gate in Scene 08.

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
**Guard** (MM p. 347).

## Appearances
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — Scenes 01 (the Stair-head), 02 (C1), 04 (his voice taken), 06, 08, 09, 10.

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
Hrimvald spoke to him in his dead wife's voice. If his voice comes home, he sings her verse on watch again.
