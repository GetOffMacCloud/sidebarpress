---
type: npc
status: dead
canon: false
faction: ''
location: '[[Merrow''s Rest]]'
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
tags: [wight, undead, ally, SP-OP01]
---

# Sexton Harrow

> The chapel's old gravedigger, raised as a wight by the thing that killed him, who led the larder dead into hiding.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
A big, stooped man in a sexton's leather apron gone black with damp, a shovel still in his hand. Grey skin, pale eyes, a voice like a shovel in gravel.

## Personality & Mannerisms
- Speaks for the others; counts them under his breath.
- Ashamed of the hunger. Keeps his hands where you can see them.

## Goals & Secrets
- **Wants:** rest for his people, clean, by the saint's ash. He'll ask for it.
- **Secret:** he could have used the urn on all of them a week ago. He couldn't make himself do it.

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
Wight (MM 300), CR 3 (700 XP). Fights Ossian only if the party persuades him (Persuasion DC 13).

## Appearances
- [[SP-OP01-What-the-Dead-Fear]]: Scene 03 (Harrow's truth, the Larder).

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
If the party lets the dead walk free, he leads them into the hills; a month later, hunger wins.
