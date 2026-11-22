---
type: npc
status: alive
canon: false
faction: Chakyik (Tiger Nomads) — Temur's riders
location: Yecha
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
tags: [chakyik, rider, baklunish, SP-GA01]
---

# Batzorig

> Temur's rider-captain. He intercepts the party, takes their blades, and keeps them on his own saddle until they earn them back.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Broad and young, with a tiger-tail standard tied at his saddle and his mouth set hard. Six riders behind him, men and women both.

## Personality & Mannerisms
Rude, and for now that's as far as it goes. He speaks broken Common slowly, like each word costs him. He is a stickler for custom, even the customs that help the party.

> *"Letters are yours. Blades are ours. Custom."*

## Goals & Secrets
- **Wants:** Temur's war, and to see the south-men fail honestly.
- **Holds:** the party's weapons (returned on a Horse success, after the Bow on a partial, or when they leave Yecha).
- **Told Sarnai** about the second letter in their packs.
- **Knows:** the party's weapons by heart, and which PC laid down steel first.
- **Escalation:** first he demands ("blades on the snow"), then he draws (six bows), then he escorts the PC under guard. He never shoots to kill a guest.

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
**Scout** (MM p. 349), mounted on a steppe pony. See [[SP-GA01 — Bestiary]].

## Appearances
- [[SP-GA01-The-False-Arrow]] — Scenes 2 and 3

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
If Temur rides east, Batzorig rides at his side.
