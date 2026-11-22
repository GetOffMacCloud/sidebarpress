---
type: npc
status: alive
canon: false
faction: Greyhawk University — Ritterstadt Field Station
location: Ritterstadt — the Station House
aliases: [the Warden, Rektor Weissmantel, Albrecht Weissmantel]
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
tags: [ritterstadt, greyhawk-university, warden, administration, gazetteer]
---

# Rektor Albrecht Weissmantel

> ![[Ritterstadt rektor-weissmantel.jpg|300]]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Fifty-eight, Oeridian, stooped from reading at a cold desk. A grey gown worn thin at the elbows, ink on the right cuff, a brass seal on a chain he touches when he is thinking.

## Personality & Mannerisms
Tired, exact, and fair. Reads the whole letter before he answers the first line. Loyal to the station over the Chancellor, and ashamed of knowing it.

> *"I seal commissions. I do not sign confessions. Which is this?"*

## Goals & Secrets
- **Wants:** the station solvent and its students home; the Regents kept at a month's distance.
- **Knows:** that the Regents' Commission holds a second seal he cannot refuse, and that Vogelsang expects his chair.
- **Secret:** he has hidden Hassenrath's second notebook in the Registrar's sealed files under his own name, so that only a Chancellor's order can open it.

## Role & Context
> [!art]+ Portrait

> Station Warden of Greyhawk University's Ritterstadt Field Station since 571 CY. He seals every commission on the Job Board and has drafted his resignation twice.

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
Noncombatant. **Noble** (MM p. 348), Intelligence 16, proficient in History and Insight.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-02, RG-04, RG-08, RG-09
- [[SP-GA03-The-Red-Cord]] — Scene 1 (seals the Job Board commission)
- [[SP-GQ01-The-Gaolers-Link]]: hosts the Warden's Brewfest Dinner; Scene 05

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
Record each time a party learns about the second seal, and whether he resigns.
