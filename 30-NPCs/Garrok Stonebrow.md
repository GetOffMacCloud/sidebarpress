---
type: npc
status: alive
canon: false
faction: Greyhawk University — Ritterstadt Field Station
location: Ritterstadt — the Drill Yard
aliases: [Garrok, the Drill-Sergeant, Sergeant Stonebrow]
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
tags: [ritterstadt, greyhawk-university, drill-sergeant, goliath, training, gazetteer]
---

# Garrok Stonebrow

> The Field Station's Drill-Sergeant: a goliath of the Yatil Mountaineer clan, thirty-three, who came north as a caravan guard and stayed when the caravan left.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
![[SP-GQ00 Portrait - Garrok Stonebrow.png|300]]
Seven and a half feet of grey-mottled mountain, tattooed with his clan's scree-marks, a practice shield always on his back.

## Personality & Mannerisms
Loud on the yard, quiet off it. Counts every student's mistakes and forgives them all at sundown.

> *"The shield wall holds or the town does not. Again."*

## Goals & Secrets
- **Wants:** every student able to hold a line before their first expedition.
- **Teaches:** War Studies practicals, weapon drill, and Stahlwulf's watch drill. Runs the Scouts' Field Day.
- **Secret:** his clan wants him home and has sent word twice. He has not answered.

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
**Veteran** (MM p. 350) with goliath traits (Stone's Endurance).

## Appearances
- [[SP-GQ00 — Prologue — The Crossing]]: Scene 6 (the gate at landfall)
- [[Ritterstadt — Gazetteer (Book)]] — RG-04, RG-08, RG-09
- [[SP-GQ01-The-Gaolers-Link]]: runs the palisade gate and the gate rota; says the clerk won't come inside (Scene 03, F3); shuts the gate at Alert (Scene 05); the trap on the quay (Scenes 06–08). Took over this role from Sergeant Hask, who belongs to Schwartzenbruin (2026-11-07).

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
