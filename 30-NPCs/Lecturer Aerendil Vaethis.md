---
type: npc
status: alive
canon: false
faction: Greyhawk University — Department of Letters & Cultures
location: Ritterstadt
aliases: [Aerendil Vaethis, Lecturer Vaethis]
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
tags: [ritterstadt, greyhawk-university, lecturer, linguistics, high-elf, gazetteer]
---

# Lecturer Aerendil Vaethis

> Lecturer in Linguistics & Philology, Department of Letters & Cultures. A high elf and the Polyglot Circle's quiet centre.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Slender, dark-haired, soft-voiced, ink-smudged fingers, a pocket-book of other people's proverbs.

## Personality & Mannerisms
Listens more than he speaks; corrects pronunciation by repeating the word correctly and waiting. Collects words like stones.

> *"A word is a fossil. Dig."*

## Goals & Secrets
- **Wants:** a lexicon of the old Flan place-names around Ritterstadt.
- **Works with:** Lecturer Tock on the tablet; Rook Ashveil in the Polyglot Circle.
- **Secret:** "Dreadverge," "Hush," and "Erikasrast" share a root he thinks means *threshold*. He has not published it.

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
Noncombatant. **Commoner** (MM p. 345), Intelligence 16; eight languages.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-09

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
