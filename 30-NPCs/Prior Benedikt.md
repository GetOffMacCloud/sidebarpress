---
type: npc
status: alive
canon: false
faction: Chapel of St. Vesper
location: Vesper Hollow — Chapel of St. Vesper
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
tags: [sp-hal-03, obstacle, priest, hallows-eve-quartet]
---

# Prior Benedikt

> Priest of St. Vesper, keeper of the crypt key, and the man who blesses the lanterns every night without knowing it's the same night. He thinks the druid on the hill is the problem.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Fifties, lean, in a grey cassock kept very clean. The crypt key on a cord at his belt, where everyone can see it. Lights every yew lantern himself.

## Personality & Mannerisms
Stiff, devout, courteous, protective of his flock. Warms to any show of piety. Preaches against "the witch on the hill" at 7 PM every loop and means it. Doesn't remember any of it.

## Goals & Secrets
- **Wants:** his people safe, which to him means the druid gone and the crypt locked.
- **Knows:** the parish record of the bell's purchase, forty years ago, "one bell, bought of T. Marrow of Marrowmere, that had rung over the drowned." He'll fetch it if asked.
- **Secret:** none. He is an innocent obstacle. The method says: talk, steal, or wait, never kill.

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
**Priest** (MM 348).

## Appearances
- [[SP-OS03-The-Night-That-Doesnt-End]] — the chapel yard; the crypt key; Midnight Mass

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. No canon source.

## Continuity
He is the third soul taken in Loop 2 if unprotected. If the party convinces him the druid isn't the threat (Persuasion DC 15), he hands over the key and becomes an ally; he opens the crypt at 11:45 for Midnight Mass regardless. If the party kills him, the village turns on them for the loop and Hale says, *"That one was innocent, you know."*
