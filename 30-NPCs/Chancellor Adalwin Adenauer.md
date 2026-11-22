---
type: npc
status: alive
canon: false
faction: Greyhawk University — Board of Regents
location: City of Greyhawk
aliases: [the Chancellor, Chancellor Adenauer, Adalwin Adenauer]
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
tags: [greyhawk-university, chancellor, city-of-greyhawk, regents, ritterstadt]
---

# Chancellor Adalwin Adenauer

> ![[Ritterstadt chancellor-adenauer.jpg|300]]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Seventyish, long-faced, iron-grey, in the plain black gown of the University with the Chancellor's chain worn under it rather than over. Painted standing, one hand on a closed book.

## Personality & Mannerisms
Careful, courteous, and slow to decide; once decided, immovable. Writes in short sentences. Answers every letter from Ritterstadt personally, a month late, and never in anger.

> *"The station exists to learn. I have never confused that with the station existing to keep what it learns."*

## Goals & Secrets
- **Wants:** the station solvent, its students alive, and the University's name on the north.
- **Believes:** that the Fiend's Embrace belongs in the City of Greyhawk, where it can be studied and guarded by people who are not also a palisade.
- **Secret:** he holds the Founders' Compact and Commissioner Dray's drafted commission, and has not given the word. He is waiting for Varek Doss to tell him whether moving the Embrace is survivable. If Doss says yes, the second seal is used within the season.
- **Does not know:** that Vogelsang reports to Dray directly, or that the Pale Ledger reads his correspondence in fair copy.

## Role & Context
> [!art]+ Portrait

> Chancellor of Greyhawk University, seated in the City of Greyhawk. He has never seen Ritterstadt and has read every Field Report it has sent. His portrait faces the Station House door.

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
Noncombatant. **Noble** (MM p. 348) with Intelligence 18 and expertise in History and Insight, if it ever matters.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-06, RG-08, RG-09
- By letter only, in any Ritterstadt adventure that touches the Regents

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew (Sidebar Press). Named by Greybeard for the Ritterstadt Gazetteer.

## Continuity
Record the first time a party reads one of his letters, and the first time he reads one of theirs.
