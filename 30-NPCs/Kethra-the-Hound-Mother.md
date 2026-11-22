---
type: npc
status: dead
canon: false
faction: Flan (ancient)
location: The Three Sisters (barrow)
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
tags: [flan, undead-binding, barrow, perrenland, SP-GA02]
---

# Kethra, the Hound-Mother

> A Flan chieftain fifteen centuries dead, buried in the high Clatspurs before the Oeridian clans crossed the passes. Her hunting pack was buried with her and bound to her barrow by a green-bronze torc.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
She lies on a stone bier in rotted leather and amber beads. Her brow bears the mark where the [[Antler-Crown-of-Kethra|Antler Crown]] sat, and her breast is bare where the [[Torc-of-the-Hound-Mother|torc]] lay.

## Personality & Mannerisms
None at the table. She never speaks, moves, or appears as a ghost. Her will shows only in the pack's behavior: the **Hound-Mother's Law** (bound offerings are hers) and the pack's turn against the crown-thief when the torc returns.

## Goals & Secrets
Her binding wants the torc back. That is all. *Never give her a voice.*

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
None.

## Appearances
- [[SP-GA02-The-Bones-of-the-Dreadverge]] — Scene 5 (the bier)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew, inspired by the canon Flan tribes of the Yatil and Clatspur highlands. See [[The-Hound-Mother-of-the-Dreadverge]].

## Continuity
She is one of the "nine chiefs" in [[The Nine Chiefs of the Clatspurs]].
