---
type: npc
status: alive
canon: false
faction: Greyhawk University — Department of Physic & Alchemy
location: Ritterstadt
aliases: [Jorund Vesk, Lecturer Vesk]
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
tags: [ritterstadt, greyhawk-university, lecturer, necrology, dwarf, wee-jas, gazetteer]
---

# Lecturer Jorund Vesk

> Lecturer in Necrology, Department of Physic & Alchemy. A Clan Brock dwarf and a true Grave-cleric of Wee Jas, which the Chapel pretends not to notice.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Stocky, grey-bearded, in black leather apron and a grave-cleric's silver skull-pin worn under his collar.

## Personality & Mannerisms
Gentle with the dying, blunt with the living. Lays out the dead for the Infirmary and won't let anyone rush it.

> *"The dead do not lie. They do, however, get up."*

## Goals & Secrets
- **Wants:** every body in Ritterstadt properly buried and properly kept down.
- **Role:** the Grey Sickle's natural enemy, whether or not either knows it yet.
- **Secret:** he writes to Brock's Aerie about the Founder Dagmar, and the Aerie writes back.

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
**Priest** (MM p. 348) with Wee Jas's grave domain; Turn Undead.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-09 · [[Faction — The Grey Sickle]]

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
