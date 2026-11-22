---
type: npc
status: alive
canon: false
faction: House of Zilchus, Schwartzenbruin
location: Schwartzenbruin
aliases: []
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
tags: [schwartzenbruin, zilchus, merchant, witness, sp-pbs-03]
---

# Benedikt Roos

> A factor of Zilchus and the merchants' voice among the three witnesses at the Red Cord. He is fat, courteous, and memorising everything.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Heavy-set, in a good grey coat with a gold purse-pin, and he keeps a small ledger open on his knee.

## Personality & Mannerisms
Polite and exact. He writes down every promise said aloud and reads it back.

## Goals & Secrets
- **Wants:** a clean record for his house.
- **Knows:** the hiring-hall gossip about the Eisfeld debt, and that it came from his own clerks. That is how Dornhalm heard it.
- **Reacts:** he would rather leave than witness a cord being cut. If Konrad admits the debt aloud, Roos records it without comment. In Zilchus's eyes, that is a mark in Konrad's favour.

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
**Noble** (MM p. 348). Noncombatant.

## Appearances
- [[SP-GA03-The-Red-Cord]] — Scenes 3 and 6 (the merchants' witness)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. See [[Zilchus]].

## Continuity
None.
