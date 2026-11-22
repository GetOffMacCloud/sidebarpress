---
type: npc
status: alive
canon: false
faction: The Old Kerk Mission (Perrenland)
location: Ritterstadt — lodging at the Grey Wolf
aliases: [Dominie Roth, Anselm Roth, the Dominie]
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
tags: [ritterstadt, old-kerk, perrenland, priest, gazetteer]
---

# Dominie Anselm Roth

> ![[Ritterstadt dominie-roth.jpg|300]]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Late forties, broad Perrender face, close-cropped beard, the Old Kerk's dark green coat with its many small buttons. Walks with a staff he does not need.

## Personality & Mannerisms
Patient, genial, and genuinely charitable. Remembers every fisher's child's name. Asks about the chapel's history the way a man asks about the weather.

> *"A Pholtine lamp is a good lamp. I only wonder who lit it, and on what."*

## Goals & Secrets
- **Public:** an Old Kerk chapel in Ritterstadt for Perrender souls.
- **Actual:** if a canton ever claims Ritterstadt, the Kerk means to have been here first — congregation, chapel, and a correspondence with the Voormann's council about what the University digs up.
- **Brief from the elders:** learn whether St. Erika's foundation stone is the Flan threshold marker the old songs say it is.
- **Has already written** south that the University is "digging where it should not." He does not know the Hanselmann Consortium reads the Voormann's post.

## Role & Context
> [!art]+ Portrait

> A priest of Perrenland's Old Kerk, sent north from Schwartzenbruin in 575 "to serve the Perrender faithful of the frontier." He preaches in the market on fair days and is courteous to Vater Sigmund, who likes him and does not trust him.

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
**Priest** (MM p. 348). Sincere.

## Appearances
- His brief comes from [[Ouderling Machteld Vreeswijk]] (the Old Kerk's Keeper of Oaths), who has her own reasons ([[SP-GQ00 — The Shadow on the Quag]]).
- [[Ritterstadt — Gazetteer (Book)]] — RG-03, RG-06, RG-07

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
Record whether he gets his chapel, and whether the Wolf Nomads come down off the moor when he has the stone read. → [[Faction — The Old Kerk Mission]]
