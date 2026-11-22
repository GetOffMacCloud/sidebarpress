---
type: npc
status: alive
canon: false
faction: Waycombe
location: Waycombe — the mill
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
tags: [waycombe, child, perrenland, SP-GA02]
---

# Rowan Gest

> Twelve, the miller Mother Gest's daughter. The mill door was ash-marked this morning, so she is next.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Flour on her sleeves, braids, and a direct stare.

## Personality & Mannerisms
Curious and unafraid of strangers. She asks questions adults don't.

## Goals & Secrets
- **Nudge:** if the table is stuck on the ash circles for 10 minutes, Rowan asks the cleric PC whether "the brother" will bless her too.
- **Reacts:** if the party waits for dawn, she is taken from the mill at midnight and becomes a fourth captive after Tam on the Rite Track.

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
Noncombatant.

## Appearances
- [[SP-GA02-The-Bones-of-the-Dreadverge]] — Scene 2 (the marked mill door; the nudge), Scene 5 (fourth captive, if the party waited)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
None.
