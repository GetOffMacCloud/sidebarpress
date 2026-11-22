---
type: npc
status: alive
canon: false
faction: The Pale Ledger (Scarlet Brotherhood)
location: Ritterstadt — the lane behind the Grey Wolf
aliases: [Hesta, Hesta Varnholm]
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
tags: [ritterstadt, suel, scarlet-brotherhood, copyist, gazetteer]
---

# Hesta Varnholm

> ![[Ritterstadt hesta-varnholm.jpg|300]]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Thirties, pale and fair as her people, ink-stained fingers, a plain grey dress with a copyist's leather cuff. Keeps her hair under a cap. Smiles with her mouth.

## Personality & Mannerisms
Quiet, helpful, forgettable on purpose. Charges fairly, finishes early, asks nothing. Hums Suel lullabies while she works and stops when anyone notices.

> *"I only write what I'm given. What I remember is my own affair."*

## Goals & Secrets
- **Public:** to be left alone, as Perrenland leaves Suel exiles alone.
- **Actual:** to count everything that moves north and send it south twice a year in a calfskin ledger sewn into a bolt of [[Yusuf al-Rashad]]'s cloth. He does not know.
- **Holds:** three logged Bloom crystals missing from the Assay House, and a second copy of the Grey Sickle's barrow list.
- **Handler:** the "retired factor" who walks the palisade every evening.
- **Would sell:** Ewald to Stahlwulf, for the right price. She regards Iuz's agents as competitors.

## Role & Context
> [!art]+ Portrait

> A Suel "exile," letter-writer and copyist on the lane behind the Grey Wolf. She fair-copies for the Illuminators' Guild and reads everything she copies. She is the Pale Ledger's pen.

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
**Spy** (MM p. 349). Forgery kit; Deception +5, Sleight of Hand +4, Stealth +4.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-03, RG-04, RG-06

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
If the ledger is ever read by someone outside the Brotherhood, Hesta leaves Ritterstadt within the week and the tailor stays. → [[Faction — The Pale Ledger]]
