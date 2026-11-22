---
type: npc
status: alive
canon: false
faction: Greyhawk University — Department of Antiquities
location: Ritterstadt
aliases: [Fennimore Tock, Lecturer Tock]
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
tags: [ritterstadt, greyhawk-university, lecturer, epigraphy, gnome, ur-flan, gazetteer]
---

# Lecturer Fennimore Tock

> Lecturer in Epigraphy & Iconography, Department of Antiquities. A gnome, and the one person at the station who can read some Ur-Flan.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Wispy white hair, a jeweller's loupe on a chain, chalk on every sleeve, a rubbing-roll under one arm.

## Personality & Mannerisms
Fussy, delighted, easily frightened. Talks to inscriptions under his breath.

> *"Letters first. Pictures lie; letters only mislead."*

## Goals & Secrets
- **Wants:** a full reading of the clay tablet from the Wachturm.
- **Secret:** he has translated one line and told no one, because it frightened him: *"the one who knew first is not asleep; it is counting."*

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
Noncombatant. **Commoner** (MM p. 345), Intelligence 17, expertise in History.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-09, RG-10
- [[SP-GQ01-The-Gaolers-Link]]: reads the six sigils; the Rubbing of the Six; Scenes 07, 08

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
