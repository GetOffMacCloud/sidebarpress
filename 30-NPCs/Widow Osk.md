---
type: npc
status: alive
canon: false
faction: Reed-cutters
location: Marrowmere — The Reed Landing
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
tags: [hallows-eve-quartet, sp-hal-02, guide, folk-magic]
---

# Widow Osk

> Reed-cutter and water-reader; knows the safe path across the marsh and which wisp will talk for bread.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Small, bent, barefoot on the landing stones in any weather. A basket of bread heels on her hip. Eyes the color of the mere.

## Personality & Mannerisms
Speaks in riddles about "what the water keeps." Helpful to anyone who shows respect and brings a loaf; silent to anyone who laughs. Never looks at the hall directly.

## Goals & Secrets
- **Wants:** respect; the old custom kept; nobody drowned on her water tonight.
- **Knows:** the marsh path, the wisps' names (they were guests), and that bread set on the water calms one wisp into answering a single question honestly.
- **Can do:** read the water for a PC and tell them one true thing about their own dead (a 10-minute beat if running short).

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
**Commoner** (MM 345) with proficiency in Survival (+4) and Nature (+2). Not a druid; she has no spells, only the path.

## Appearances
- [[SP-OS02-The-Hollow-Lantern]] — Scenes 00, 02

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
The reed-cutters' tradition is the "second faith" of the Hommlet pattern. If the PCs ignore her, the marsh path is closed and the wisp's clue is lost.
