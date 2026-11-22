---
type: npc
status: alive
canon: false
faction: The Sheaf
location: Thornbury — the Bountiful Board
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
tags: [sp-hal-04, thornbury, innkeeper, cult, human]
---

# Barnaby Reap

> Innkeeper of the Bountiful Board and second in the Sheaf. He bakes the Hundredth Loaf, and he can't meet the party's eyes after ten.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Huge, red-faced, flour to the elbows at all hours, apron over a belly like a cask. Forty-five. A burn scar across the back of one hand from the oven, which he shows children to make them laugh.

## Personality & Mannerisms
Jolly, loud, weeps easily (at toasts, at hymns, at the oven). Laughs a half-second too long and stops a half-second too early. Leads the harvest hymn at the procession, badly, because nobody else will. After 10 PM he looks at the floor when he talks to the party.

## Goals & Secrets
- **Wants:** the party fed and comfortable, right up until midnight. Then he wants it over.
- **Knows:** the loaf's recipe (the binding is in the salt, which is dug from the pit's edge); that his daughter is a doubter; that Prudence drew lots last spring.
- **Secret:** he put a second slice on Ned's plate on purpose, the first night, so it wouldn't have to be a child. He has told no one and prays nobody asks.
- **Breaking point:** Tamsin in danger. If a PC puts Tamsin between themselves and the Sheaf, Barnaby stops singing.

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
**Commoner** (MM 345). He never fights. If the barn burns he carries children out of it until the roof comes down.

## Appearances
- [[SP-OS04-The-Tithe-of-Thornbury]] — Scenes 00, 01, 04, 05

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
Father of [[Tamsin Reap]]. If the pact ends, he keeps the inn and never bakes again; Tamsin runs the kitchen. If the pact is paid, he is the one who sets the Guest's Chair back at the head of the table the next morning, garlanded, empty, for luck.
