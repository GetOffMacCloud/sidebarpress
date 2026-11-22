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
tags: [waycombe, shepherd, guide, perrenland, SP-GA02]
---

# Hild Brennan

> A Waycombe shepherd and the only witness to the pack's master. Her husband Brannoc is a captive at the Three Sisters.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
She is weathered and narrow, wrapped in a grey shawl, and carries a shepherd's crook taller than she is.

## Personality & Mannerisms
She is laconic and speaks in single lines while watching something else. She is fearless out of exhaustion, not courage. She does not believe the Iuz talk.

> *"They had him by the coat and walked him like a calf. There was a man with them. He had antlers. Not on his head like a beast's. On his head like a crown."*
> *"Iuz sends orcs. These came for sheep and walked home."*

## Goals & Secrets
- **Wants:** Brannoc back alive. Brannoc served a season as a Clatspurgen militia longbowman; his bow still hangs over their door.
- Knows the Dreadverge, the Weeping Beck's ford-stones, and that the pack will not cross running water.

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
Commoner (MM p. 345), with proficiency in Survival (+2). Her crook is a quarterstaff.

## Appearances
- [[SP-GA02-The-Bones-of-the-Dreadverge]] — Scenes 1 and 2 (witness), Scene 3 (guide), Scene 5 (if she comes)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
If the party arrives in time, she becomes a friendly contact and guide on the Dreadverge in any future adventure.
