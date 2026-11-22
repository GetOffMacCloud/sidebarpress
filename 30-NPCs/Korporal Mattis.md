---
type: npc
status: alive
canon: false
faction: Jürgen's Ernes (free company of Traft)
location: Schwartzenbruin
aliases: [Mattis of the Ernes]
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
tags: [schwartzenbruin, mercenary, ernes, witness, sp-pbs-03]
---

# Korporal Mattis

> A lean, bored corporal of Jürgen's Ernes, sent as the swords' voice among the three witnesses.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Lean and sunburnt, with the Ernes' diving eagle stitched on his collar. His boots are up on the bench.

## Personality & Mannerisms
Laconic, with a soldier's humour, and he would rather be drinking.

## Goals & Secrets
- **Wants:** to get back to his beer.
- **Knows:** the halved-standard custom. He names it only if a soldier asks him.
- **Reacts:** he cheers anyone who disarms a knife bare-handed, and he reports the night faithfully to Jürgen.

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
**Veteran** (MM p. 350). Not fought.

## Appearances
- [[SP-GA03-The-Red-Cord]] — Scenes 3, 4 and 6 (the swords' witness)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. His company comes from fan material (*Oerth Journal* #5). See [[Perrenland-Mercenary-Companies]].

## Continuity
None.
