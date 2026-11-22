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
tags: [candlecrown, shepherd, victim, sp-gs02]
---

# Corin the Shepherd

> Candlecrown's shepherd and the first voice Hrimvald takes; he can't read, but he can draw what he saw. [Telchur]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Forty, weathered, gentle, with a shepherd's crook and a dog called Biscuit. **Memorable:** a grey wool hood he never takes off, even indoors.

## Personality & Mannerisms
Shy, slow to trust, patient with animals and children. Mute after Needfest 1, and frightened of it. **Quirk:** when he wants to say something, he points with his crook.

## Goals & Secrets
- **Wants:** to be understood. *Fears:* that no one will believe what he saw.
- **Knows:** what took his voice, close up; that it went for him because he hums all seven verses to his sheep. He can draw it, and he knows the way it climbs (the north cliff).
- **Reacts:** hides from strangers in the wool loft until someone is gentle or brings Biscuit; then draws. Points the party at the seventh verse with charcoal.

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
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — Scenes 02 (C8, his fold), 03 (the drawings), 09, 12. Hidden by Brannoc in the wool loft.

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
If his voice comes home, the first thing he says is his dog's name.
