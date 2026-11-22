---
type: npc
status: alive
canon: false
faction: Kezrin's men (agent of Iuz)
location: Yecha
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
tags: [chakyik, exile, iuz, villain-minion, SP-GA01]
---

# Ochir the Cut-Rein

> A Chakyik exile who leads Kezrin's men in the tent-city and wears Iuz's brand under his sleeve.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Lean and weathered, with a felt coat worn inside-out to hide its clan stitching. Inside his left forearm: a grinning-skull brand.

## Personality & Mannerisms
Quiet, patient and contemptuous. He calls the riders of the horde "brothers" in a way that isn't a compliment.

## Goals & Secrets
- **Wants:** to see the horde that cut his rein bleed itself out against the Wolves.
- **Knows:** Kezrin's plan in outline, the six Wolf-dressed riders, and that the payments come "from the north."
- **Reacts:** leads the Scene 5 night attack. Knocks PCs out rather than killing them, and runs when Naran's riders arrive. Captured, he says nothing; one of his thugs talks instead.

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
Homebrew, CR 2: see [[SP-GA01 — Bestiary]] (Ochir the Cut-Rein), with FGU import text.

## Appearances
- [[SP-GA01-The-False-Arrow]] — Scene 5 (the night attack)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
If he escapes, he is a natural face for Kezrin's network in Part 2.
