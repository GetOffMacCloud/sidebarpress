---
type: npc
status: alive
canon: false
faction: Greyhawk University — Ritterstadt Field Station
location: Ritterstadt
aliases: [Kartner, Magister Kartner, Roswitha Kartner]
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
tags: [greyhawk-university, ritterstadt, faculty, department-head, fieldcraft, SP-GA01]
source_canon: A Tourist In Greyhawk — 05 — Department of Exploration & Cartography
---

# Magister Roswitha Kartner

> ![[Ritterstadt kartner.jpg|300]]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance

## Personality & Mannerisms
Unhurried, exact, dry. Reads Job Board postings aloud with a hot mug in hand. Teaches field manners as survival skills.

> *"In another people's country you are a guest from the moment they see you. Put your steel down before you're asked. Let their taster drink first. Eat what they put in front of you."*

## Goals & Secrets

## Role & Context
> [!art]+ Portrait

> Head of the Department of Exploration & Cartography at Greyhawk University's Ritterstadt Field Station. Never lost, never hurried. It is said she once corrected a river.

- **SP-GA01:** reads Brennin's contract off the Job Board at the Fiend's Rest; receives Brennin's field-credit report (60 / 50 / 40 / 30 / 20 by ending). Students attending her Wilderness Fieldcraft lectures lock in the Scene 2 restraint bonus and recognize Wolf sinew-fletching in Scene 4.

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
Not met in the field. If needed: **scout** (MM p. 349) with expertise in Survival.

## Appearances
- [[SP-GA01-The-False-Arrow]] — Scene 0
- [[Ritterstadt — Gazetteer (Book)]] — RG-08, RG-09

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Defined in the A Tourist In Greyhawk vault (`05 — Department of Exploration & Cartography`), where she is an **unstatted placeholder department head**. Everything below the Source line that isn't in that note is Sidebar Press elaboration — keep it consistent if the campaign vault promotes her to a full NPC.

## Continuity

## Her Department
- **Major:** Cartography. **Minors:** Subterranean Studies · Wilderness Fieldcraft.
- **Student organizations:** the Scouts & Surveyors (terrain log and map archive); the Ramblers' Fellowship.
- **Motto:** *Know the ground before you walk it. Know the exits before you enter.*
