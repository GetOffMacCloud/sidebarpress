---
type: npc
status: alive
canon: false
faction: The Quag Bargemen (Rhennee)
location: Ritterstadt — the Landing
aliases: [Baba Yeska, Yeska Marovna, the Warden of the Landing]
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
tags: [ritterstadt, rhennee, landing, warden, faction-leader, gazetteer]
---

# Baba Yeska Marovna

> ![[Ritterstadt baba-yeska.jpg|300]]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Sixty-some, small, brown as a barge-plank, in the layered skirts and head-scarf of the Rhennee with a toll-tally of knotted cord at her waist. Smokes a short clay pipe she never lights indoors.

## Personality & Mannerisms
Warm to children and customers, flat as still water to officials. Speaks Common, Rhennee, and enough Perrender to haggle. Answers questions with questions and prices with silences.

> *"The lake does not take tolls. I do. One of us is reasonable."*

## Goals & Secrets
- **Wants:** the Landing to grow with the town, and the Landing to be hers when it does.
- **Runs:** the ferry, the smokehouse, the salt pans, and night barges south that pay no toll.
- **Secret:** half her "Quag salt" is Traft salt sold back to Traft; the other half comes from a pan at the Mire margin where nothing should be dry. Twice a season a sealed crate goes north with a letter in her daughter's hand to Iuz's recruiter. Yeska reads the replies and burns them. Her grandchildren are the two tieflings the town does not discuss. The recruiter is Kermin Mind-Bender's: **Edrik Saumann**, who sat in her tally-house in 575 as Quagflood's harbour clerk and is now Commissioner Dray's junior secretary. He courts [[Liesl Amsel]] in SP-GQ02; Yeska will know his face ([[SP-GQ00 — The Shadow on the Quag]]).
- **Would:** burn the Landing before she let it be used against the town.

## Role & Context
> [!art]+ Portrait

> Matriarch of the four Rhennee barge-families at the Landing and Warden of the Landing by the Moot Roll. She keeps the toll-book, the salt pans, and the lake.

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
**Spy** (MM p. 349) without the weapons; Insight +6, Deception +5.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-02, RG-03, RG-04, RG-05, RG-06
- [[SP-GQ01-The-Gaolers-Link]]: the Landing; the Hecht's stores; Scenes 01, 03, 07
- [[SP-GQ00 — Prologue — The Crossing]]: Scene 6

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
Record whether a party learns about the northbound crate, and what Yeska does when they do. → [[Faction — The Quag Bargemen]]
