---
type: npc
status: alive
canon: true
faction: The Fiend's Rest Public House
location: Ritterstadt — the Fiend's Rest Public House
aliases: [Karet, Keeper of the Board]
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
tags: [ritterstadt, publican, job-board, fiends-rest, gazetteer]
source_canon: A Tourist In Greyhawk — The Fiend's Rest Public House (inline)
---

# Karet

> ![[Ritterstadt karet.jpg|300]]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance

## Personality & Mannerisms

## Goals & Secrets
- **The Hush ledger:** campaign canon places a ledger in her apron that maps the Hush's stress points. See the campaign Wachturm references.

## Role & Context
> [!art]+ Portrait

> Publican of the Fiend's Rest Public House and Keeper of the Board. Nothing goes on the Job Board without her stamp beside the Warden's seal.

### Roles (Ritterstadt Gazetteer)
- **Keeper of the Board** — by custom under the Field Station Charter: her stamp sits beside the Warden's seal on every Job Board posting.
- **Credit chits** — accepts University chits for beds and meals and redeems them with the Bursar at the quarter.
- **The ear of the road** — pack-merchants, travellers, and every party that comes home tell her first.

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

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-02, RG-03, RG-04, RG-05
- [[SP-GA01-The-False-Arrow]] — Scene 0 (the Job Board)
- [[SP-GQ01-The-Gaolers-Link]]: keeper of the Fiend's Rest; listens to the terms; Scene 02

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Karet appears inline in the campaign vault's **The Fiend's Rest Public House** note, which is the authority. This note collects her Gazetteer roles; if the campaign vault gives her a full note, that note wins.

## Continuity
