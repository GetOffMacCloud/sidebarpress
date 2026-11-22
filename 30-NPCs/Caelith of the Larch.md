---
type: npc
status: alive
canon: false
faction: The Larch kin-band (sylvan elves of the Vesve border)
location: Ritterstadt — the Larch camp, outside the east gate
aliases: [Caelith, Caelith of the Larch]
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
tags: [ritterstadt, elf, sylvan, forester, kin-leader, gazetteer]
---

# Caelith of the Larch

> ![[Ritterstadt caelith.jpg|300]]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Ageless in the way of the wood-elves, weathered rather than fair, in larch-bark greens and a cloak that has been mended more than it has been made. Carries no bow in town. That is the point.

## Personality & Mannerisms
Courteous, brief, and literal. Answers the question asked and no other. Will not step inside the palisade without being invited, and turns out for the wall when the horn sounds twice anyway.

> *"A stave is a promise to make something. An arrow is the thing made. I sell promises."*

## Goals & Secrets
- **Wants:** the forest edge left to the kin-band, a seat on the Moot Roll one day, and never to go back to the Vesve.
- **Trades:** bow-staves to the brewer for grain, off the Moot's book — which is Hanz Korngut's grain discrepancy.
- **Keeps:** a watch on the Hush, run by [[Ysmay Larchwind]]. The kin-band knows where the Hush is thickest and has not told the University.
- **Secret:** what the kin-band fled in the Vesve in 575. Lecturer Ilvadriel knows and has promised not to say. It was not Grugach.

## Role & Context
> [!art]+ Portrait

> Kin-leader of the fourteen sylvan elves at the tree line outside Ritterstadt's east gate. A forester and bowyer. Sells bow-staves and will not sell arrows at any price.

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
**Scout** (MM p. 349) with elf traits; longbow +6 if it ever comes to that.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-03, RG-04, RG-05, RG-07

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
Record whether the kin-band gets a Moot seat, and whether anyone learns what they fled.
