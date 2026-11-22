---
type: npc
status: dead
canon: false
faction: House Vane
location: Marrow Hall — The Flooded Cellar
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
tags: [hallows-eve-quartet, sp-hal-02, wight, groom]
---

# Lord Edric Vane

> The groom. Cruel, wealthy, drowned in the cellar trying to close the sluice his bride opened; a wight who hates her more than he hates the living.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
A groom's coat gone black with lake water, a chain still wrapped round one wrist from the sluice wheel. Grey-faced, eyes like coins. Stands in water to the chest as if it were a carpet.

## Personality & Mannerisms
Cold, possessive, precise. Opens with a bargain if the party opens with words. Says *she* and never *my wife.*

## Goals & Secrets
- **Wants:** revenge on Ysolde; then the hall, and the living gone from it.
- **Knows:** she smiled at him over the cup; the wheel was already open when he reached it; she "sang once" the night she died (the Wail, telegraphed).
- **Bargain:** help him reach the tower and he fights beside the party. He means it. The second half (the hall is his after) is a problem he'll press only if nobody argues.
- **Insight DC 14** confirms the first half is true.

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
**Wight** (MM 300), CR 3, with two **drowned guests** (zombie variant, [[SP-OS02 — Bestiary]]). Immune to Ysolde's Wail; will stand in front of a PC if allied.

## Appearances
- [[SP-OS02-The-Hollow-Lantern]] — Scenes 04, 05

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
If allied and Ysolde falls, he claims the hall: a dangling hook. If destroyed, his *cloak of the manta ray* is in the silt and the cook's ghost stops scrubbing.
