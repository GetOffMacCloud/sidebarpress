---
type: npc
status: alive
canon: false
faction: The Regents' Commission (Greyhawk University)
location: City of Greyhawk; Ritterstadt every second Patchwall
aliases: [Commissioner Dray, Lucan Dray, the Commissioner]
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
tags: [ritterstadt, greyhawk-university, regents, commissioner, gazetteer]
---

# Commissioner Lucan Dray

> ![[Ritterstadt commissioner-dray.jpg|300]]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Fifties, lean, City-of-Greyhawk tailoring under a frontier cloak that has never been rained on. Carries a flat leather case he does not open in company.

## Personality & Mannerisms
Courteous, exact, and never in a hurry to be disliked. Writes his findings before he arrives and revises them generously. Calls every faculty member by title.

> *"The University funds the station. The station finds things. I am only here to see that the sentence has both halves."*

## Goals & Secrets
- **Public:** a productive station, sound ledgers, and the Regents' tenth of any relic recovered under commission.
- **Actual:** the Fiend's Embrace, promised to the Regents in 568 "when safely movable." He carries a drafted commission — *Recover and convey the object held at Ritterstadt under the Founders' Compact* — and the **second seal** that makes it an order the Warden cannot refuse.
- **Saw it arrive:** in Patchwall 574, on his first audit, he watched the Chancellor's sealed crate come off the barge and go into the sealed stacks, and logged it *"not inventoried."* Vogelsang has told him only that it is a fetter fragment of the Zagyg period.
- **Also wants:** the "consignment of 574" ([[The Gaoler's Link]]) sent south. On this the Chancellor disagrees and has told Vogelsang to stall ([[SP-GQ00 — Handout — The Chancellor's Letter]]).
- **Waits for:** the Chancellor's word, which waits on Varek Doss.
- **His junior secretary:** Edrik Saumann, appointed on a Regent's letter Dray accepted without question. Saumann is Kermin Mind-Bender's recruiter (SP-GQ02); before the Commission he clerked for Quagflood's harbour-reeve at the Landing (575).
- **His man on the faculty:** Professor Casimir Vogelsang, who expects the Wardenship.

## Role & Context
> [!art]+ Portrait

> The Regents' Commission's envoy to the Ritterstadt Field Station. He arrives every second Patchwall to audit the station and leaves with a crate. He carries the second seal.

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
**Noble** (MM p. 348). Travels with two hired guards (**veterans**) who wait at the Grey Wolf.

## Appearances
- SP-GQ02 *Tethers* (planned): the Patchwall 576 audit
- [[Ritterstadt — Gazetteer (Book)]] — RG-04, RG-06, RG-08, RG-09

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
Record what goes in the crate each audit, and whether the second seal has been used. → [[Faction — The Regents' Commission]]
