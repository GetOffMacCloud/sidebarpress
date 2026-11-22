---
type: npc
status: alive
canon: false
faction: ''
location: Vesper Hollow — The Last Toll
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
tags: [sp-hal-03, victim, innkeeper, hallows-eve-quartet]
---

# Marta Greaves

> Innkeeper of the Last Toll, loud and generous with the stew. The soul Thorne takes at the first midnight unless the party protects her.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Broad, flushed from the fire, sleeves rolled, a ladle in hand. After she's taken: the same, with grey eyes that don't track, saying "They do that" to nobody.

## Personality & Mannerisms
Warm, loud, a second bowl before the first is empty. Laughs at the crows. Toasts the harvest, old Hale, and Elsbeth, in that order, every night.

## Goals & Secrets
- **Wants:** everyone fed and nobody frightened.
- **Knows:** nothing of the loop. Half her regulars are Echoes and she hasn't noticed.
- **Secret:** none. She's the stake.

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
**Commoner** (MM 345). As an Echo, see [[SP-OS03 — Bestiary]].

## Appearances
- [[SP-OS03-The-Night-That-Doesnt-End]] — the feast; the first midnight

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. No canon source.

## Continuity
Taken at the sixth toll of Loop 1 unless under *protection from evil and good*, *magic circle*, *sanctuary*, carried out of the valley, or held in the chapel nave. Protecting her drops the Loop 2 crow count by one and shows the players the scoreboard works. If she's hollowed, her lantern is in the Hollow Choir; break it and she wakes at dawn.
