---
type: npc
status: alive
canon: false
faction: Waycombe
location: Waycombe
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
tags: [waycombe, reeve, perrenland, SP-GA02]
---

# Odila Marsh

> Reeve (elected warden) of [[Waycombe]] in the Canton of Clatspurgen. She keeps the books, she opened the barrow to pay the levy, and she will not say her missing son's name twice.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
She is in her late forties and broad-shouldered, with ink on her right forefinger and a silver cloak-pin she touches when she is lying. Her apron has a tally-knife in its pocket.

## Personality & Mannerisms
She is brisk and arithmetical, and she thinks in notches. She answers questions with numbers: *"Thirty-one sheep. Six cattle. Three people."* She feeds guests before she bargains with them.

> *"Forty marks a year we owe the canton. It was turf. It was only turf."*

## Goals & Secrets
- **Wants:** her son Tam back, and the levy to the cantonal council of Clatspurgen paid.
- **Secret:** she leased the turf on the Three Sisters' slope to a Traft peat crew against the old folks' warnings. She tells herself the cutters ran off with the advance.
- **Does not know:** her elder son [[Kester-Marsh|Kester]] took the torc.

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
Commoner (MM p. 345). She will not fight unless Tam is in reach.

## Appearances
- [[SP-GA02-The-Bones-of-the-Dreadverge]] — patron and quest-giver (Scenes 1, 2, and the denouement)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. "Reeve" is Sidebar Press house usage for an elected hamlet warden, not a canon Perrender office.

## Continuity
Her levy report to the canton, and whether the PCs covered for her, can return as a favor or a grudge. If the PCs ignore Waycombe, she sells the hamlet's flocks to pay the levy and leaves for Traft by winter.
