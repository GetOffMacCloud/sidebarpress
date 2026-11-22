---
type: npc
status: alive
canon: false
faction: The Old Kerk (Perrenland), the elders' council
location: Schwartzenbruin, the Elders' Kerk
aliases: [Machteld Vreeswijk, Ouderling Vreeswijk, Elder Vreeswijk, the Keeper of Oaths]
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
tags: [shadow-on-the-quag, old-kerk, perrenland, schwartzenbruin, priest, gaolers-link]
image: SP-GQ00 Portrait - Machteld Vreeswijk.png
---

# Ouderling Machteld Vreeswijk

> An elder of Perrenland's Old Kerk and its Keeper of Oaths: the cleric who gave the Chancellor his "second opinion" on the Gaoler's Link, and the woman who sent Dominie Roth north.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
![[SP-GQ00 Portrait - Machteld Vreeswijk.png|300]]
Seventy, small and very upright, white hair under the black cap of a Kerk elder, the Old Kerk's dark green coat with every one of its small buttons done up. She carries an ivory oath-rod banded in iron and taps it once on the table before she says anything she means.

## Personality & Mannerisms
Dry, precise and unhurried. Treats every promise as a contract and every contract as a prayer. Never writes a sentence she would not swear to, and expects the same of others.
> *"An oath is a chain. You may forget the chain. The chain does not forget you."*

## Goals & Secrets
- *Deity:* [Allitur]
- **Rank:** one of the Old Kerk's elders' council at Schwartzenbruin, and its **Keeper of Oaths**, the elder who judges vows, recantations and bindings. Dominie Roth's brief to read St. Erika's foundation stone is hers ([[Faction — The Old Kerk Mission]]).
- **Wants:** the Kerk in place at Ritterstadt before any canton or any Regent, with a chapel lot inside the palisade. Her price for the opinion was the Chancellor's quiet support for that lot.
- **Knows:**
  - In Patchwall 574 the Chancellor's sealed crate waited three nights in the Elders' Kerk undercroft for a ship north. **Broeder Wouter**, a penitent lay-brother who was sworn to Iuz on the Vesve border in his youth and long since recanted, carried it down the stair and came up grey and shaking. When the lid split, he put the thing back with his bare hand, and it burned his palm to the bone. She wrote it down.
  - In 576 the Chancellor wrote to ask whether a creature sworn to the Old One could carry the consignment. She sent him Wouter's record and her ruling: *"The sworn cannot hold it. A recanted oath is still a scar."* That is the "second opinion" in [[SP-GQ00 — Handout — The Chancellor's Letter]].
  - She does not know what the object is, only what it does to the sworn.
- **Secret:** she has told no other elder. Her letters go by the Kerk's own couriers, never the Voormann's post, because she knows who reads the Voormann's post.
- **Reacts:** courteous → exacting (*"What will you swear to?"*) → a firm ally to anyone who keeps their word to her, and an implacable enemy of anyone who breaks it.

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
**Priest** (MM p. 348), with *zone of truth* in place of *spiritual weapon*. **Broeder Wouter:** **commoner** (MM p. 345), his right palm a white scar.

## Appearances
- [[SP-GQ00 — Handout — The Chancellor's Letter]]: the "second opinion" (offstage)
- SP-GQ03 *The Molag Contract* (planned): a contact in Schwartzenbruin. Broeder Wouter knows how the sworn talk and can pick one out of a counting-house.
- SP-GQ04 *The Quiet Cargo* (planned): the answer if the party asks who gave the opinion

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
- If the Old Kerk gets its chapel lot in Ritterstadt, she arranged it, and the Chancellor paid for it with a favour the Regents' Commission doesn't know about.
- She is the reason the Chancellor trusts the Kerk and not the Commission with the question: the Kerk and the Commission are rivals over the town's future ([[RG-06 — Factions]]).
- Allitur is in the Old Kerk's pantheon ([[Perrenland]]). New NPC, 2026-11-13.
