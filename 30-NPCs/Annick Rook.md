---
type: npc
status: alive
canon: false
faction: ''
location: Vesper Hollow — Rook's Orchard
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
tags: [sp-hal-03, ally, druid, crows, hallows-eve-quartet]
---

# Annick Rook

> The druid of the orchard above Vesper Hollow. She doesn't remember the loops, but her crows do, and they count the souls lost each night.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Wild-haired, forty-something, in an apple-picker's smock with crow feathers worked into the hem. A crow on each shoulder more often than not. Cider-stained fingers.

## Personality & Mannerisms
Curious about strangers, quick to trust animals and slow to trust people. Speaks to her crows in the middle of sentences and expects answers. Takes Prior Benedikt's sermons against her as weather.

## Goals & Secrets
- **Wants:** to know what the crows are counting, and why the count has been "one" for as long as she can remember.
- **Knows:** nothing of the loop. But if befriended (Wisdom (Animal Handling) DC 14, or a crow's feather carried through a reset), she asks the crows and they tell her *who* will be taken tonight.
- **Secret:** none. She's the one honest adult in the valley.

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
**Druid** (MM 346). Her crows are a **swarm of ravens** (MM 339) that will not fight unless she's attacked.

## Appearances
- [[SP-OS03-The-Night-That-Doesnt-End]] — the orchard; the Crows Count; dawn (her crows fly west)
- [[SP-OS04-The-Tithe-of-Thornbury]] — her crows can arrive at the Tithe Barn if the party sent word

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. No canon source.

## Continuity
She is the second soul taken in Loop 2 if unprotected. If the loop ends, her crows fly west at dawn toward Thornbury. She can be written to for help in SP-OS04.
