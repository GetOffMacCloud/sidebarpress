---
type: npc
status: alive
canon: false
faction: Waycombe
location: Waycombe
aliases: [Kester]
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
tags: [waycombe, perrenland, SP-GA02]
---

# Kester Marsh

> Odila's elder son, 19. He stole the Hound-Mother's torc to pay a dice-debt and woke what took his little brother.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
He is lanky and unshaven, with a raw, green-tinged chafe ring on his left wrist that he rubs without noticing.

## Personality & Mannerisms
He will not come indoors and sits on the woodpile. He is quick to confess to anyone who offers him an out, and terrified of his mother. He meant to go south with a free company this spring.

> *"I wore it under my sleeve two days. It was cold the whole time. It never once got warm. Then I sold it, and then they came for Tam."*

## Goals & Secrets
- **Wants:** Tam home, and his mother never to know.
- **Secret:** he entered the opened barrow alone, took the [[Torc-of-the-Hound-Mother|torc]] from Kethra, and sold it to [[Tamsin-the-Tinker|Tamsin]] for 12 kleinmarks (sp).
- **Debt:** he owes a dice-runner in Schwartzenbruin, run up while waiting to sign with a mercenary company. See [[Kester Marsh's Debt]].

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
Commoner (MM p. 345).

## Appearances
- [[SP-GA02-The-Bones-of-the-Dreadverge]] — Scene 2 (confession), denouement

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. Renamed (formerly "Pell") to keep the series' names distinct.

## Continuity
Whether he confesses to Odila is a story choice the PCs own. His debt is a dangling hook. If ignored, the debt's collector comes to Waycombe in the spring.
