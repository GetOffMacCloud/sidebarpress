---
type: npc
status: alive
canon: false
faction: The Seam-Finders (gnome prospectors' syndicate)
location: Ritterstadt — the Burrows
aliases: [Nessa, Mistress Quillfeather]
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
tags: [ritterstadt, gnome, prospector, seam-finders, gazetteer]
---

# Nessa Quillfeather

> Head of the Seam-Finders, the gnome prospectors' syndicate in the Burrows under Market Hill. Her charts of the eastern valleys are the best in the north.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Middle-aged for a gnome, sun-browned, a prospector's hat stuck with feathers she's collected from every valley she's charted.

## Personality & Mannerisms
Energetic, chatty, and secretive about exactly one thing at a time.

> *"Rocks don't move. Maps do. That's why I keep two."*

## Goals & Secrets
- **Wants:** a University survey grant so the Seam-Finders' charts count as Field Reports.
- **Sells:** prospecting claims and chart copies; buys rumours of new seams.
- **Secret:** her second set of charts marks three places where the ground is warm in winter. She hasn't shown anyone. All three are on the binding network.

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
**Scout** (MM p. 349) with gnome traits.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-03, RG-04

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
