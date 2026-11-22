---
type: npc
status: alive
canon: false
faction: Hired by Ulrich Dornhalm
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
tags: [schwartzenbruin, provocateur, brawler, sp-pbs-03]
---

# Rudi Brack

> A cashiered sergeant, paid ten marks to bait Ritter Konrad into cutting his cord.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Thick-necked and red-faced, in an old company coat with the badge torn off. His purse is full of new coin.

## Personality & Mannerisms
Loud, and he only seems drunk. He drinks alone and works through his barbs one every few minutes.

## Goals & Secrets
- **Wants:** his ten marks.
- **Knows:** that Dornhalm hired him, and the timber remark Dornhalm gave him.
- **Reacts:** he baits Konrad, then throws the first punch, then runs. Shown the tally-book, or beaten (Intimidation DC 13), he names Dornhalm. He carries a hidden dagger at APL 3–4, which is illegal under the cord.

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
**Thug** (MM p. 350), with the brawl swap. See [[SP-GA03 — Bestiary]].

## Appearances
- [[SP-GA03-The-Red-Cord]] — Scene 3 (the provocations), Scene 4 (the brawl), Scene 5 (at the yard, if he isn't caught)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
None.
