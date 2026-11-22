---
type: npc
status: alive
canon: false
faction: Greyhawk University — Ritterstadt Field Station
location: Ritterstadt
aliases: [Federkiel, Professor Federkiel, Ilsabet Federkiel]
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
tags: [greyhawk-university, ritterstadt, faculty, department-head, languages, baklunish, SP-GA01]
source_canon: A Tourist In Greyhawk — 07 — Department of Letters & Cultures
---

# Professor Ilsabet Federkiel

> ![[Ritterstadt federkiel.jpg|300]]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance

## Personality & Mannerisms
Warm, digressive, delighted by conjugations. Believes most diplomatic disasters are grammar errors.

> *"You did not insult the khan. You insulted his horse. In Baklunish, this is worse."*

## Goals & Secrets

## Role & Context
> [!art]+ Portrait

> Head of the Department of Letters & Cultures at Greyhawk University's Ritterstadt Field Station. Speaks eleven languages and gossips fluently in all of them. Her lectures run long; nobody minds.

- **SP-GA01:** students from her Baklunish lectures follow the Chakyik war council without Sarnai's softening and can read Kezrin's ledger (Intelligence DC 12). **Extra-credit hook:** if Kezrin's papers reach the Historical Society, that's a documented discovery — 50 bonus credits (extra credit, on top of the quest's pay).

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
Not met in the field. If needed: **noble** (MM p. 348) with eleven languages.

## Appearances
- [[SP-GA01-The-False-Arrow]] — Scene 0
- [[Ritterstadt — Gazetteer (Book)]] — RG-08, RG-09

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Defined in the A Tourist In Greyhawk vault (`07 — Department of Letters & Cultures`), where she is an **unstatted placeholder department head**. Anything beyond that note is Sidebar Press elaboration.

## Continuity

## Her Department
- **Major:** Anthropology & Cultural Studies. **Minors:** Linguistics & Philology · Theology & Religion.
- **Student organizations:** the Polyglot Circle; the Historical Society (50 bonus credits for a documented, historically significant discovery); the Illuminators' Guild.
- **Motto:** *Everything that happened matters. The question is whether we understand it yet.*
