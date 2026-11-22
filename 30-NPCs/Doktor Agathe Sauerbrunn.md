---
type: npc
status: alive
canon: false
faction: Greyhawk University — Department of Physic & Alchemy
location: Ritterstadt — the Infirmary
aliases: [Sauerbrunn, Doktor Sauerbrunn, the Infirmarian]
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
tags: [ritterstadt, greyhawk-university, department-head, infirmarian, medicine, gazetteer]
source_canon: A Tourist In Greyhawk — 03 — Department of Physic & Alchemy (placeholder head)
---

# Doktor Agathe Sauerbrunn

> ![[Ritterstadt sauerbrunn.jpg|300]]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Fifties, square, sleeves always rolled, a leather roll of instruments at her hip and a burn-scar across one palm from an early still.

## Personality & Mannerisms
Impatient with prayer as a substitute for washing hands, never with prayer as such. Works with [[Vater Sigmund Wolfherz]] next door and argues with him daily.

> *"You may pray. I will cauterize. We will see who is thanked."*

## Goals & Secrets
- **Wants:** a proper infirmary building and a second physician.
- **Holds:** the Infirmarian post as part of her headship; reports to the Warden and overrules him on medical grounds.
- **Secret:** she has two Bloom-sick patients from past expeditions who never fully warmed, and keeps their notes from the Regents.

## Role & Context
> [!art]+ Portrait

> Head of the Department of Physic & Alchemy and the Field Station's Infirmarian. Blunt, tireless, and keeps students alive — and charges the Bursar for every one of them.

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
**Priest** (MM p. 348) reskinned as a physician: healing spells as alchemical treatments; Medicine +7.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-04, RG-08, RG-09 · [[The Infirmary]]

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
A **placeholder department head** in the campaign vault's `03 — Department of Physic & Alchemy`. Everything below that isn't in that note is Gazetteer elaboration; if the campaign promotes her to a full NPC, that note wins.

## Continuity

## Her Department
**Major:** Medicine & Herbalism · **Minors:** Practical Alchemy · Necrology. Her lecturer: [[Lecturer Jorund Vesk]] (Necrology).
