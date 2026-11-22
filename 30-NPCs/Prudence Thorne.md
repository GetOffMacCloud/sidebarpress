---
type: npc
status: alive
canon: false
faction: The Sheaf
location: Thornbury — the Elder's House
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
tags: [sp-hal-04, thornbury, cult-leader, elder, human]
---

# Prudence Thorne

> Elder of Thornbury, great-granddaughter of Josiah Thorne, and leader of the Sheaf. She will give the party to the field to save her people, and she will cry while she does it.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Seventy, small, straight-backed, in a grey wool dress with a wheat-sheaf brooch at the collar. Hands always full: a plate, a cup, a shawl for someone else. She carries a plain iron sickle at the procession and nowhere else.

## Personality & Mannerisms
Grandmotherly, gentle, and never raises her voice. Presses food on everyone. Never asks a guest's business. Says "I am so sorry" and means it, then does the thing anyway. When she is lying she doesn't; she simply doesn't answer.

## Goals & Secrets
- **Wants:** a guest at the table by six and in the field by midnight, so Thornbury's children eat for another hundred years.
- **Knows:** everything. The pact's words, the loopholes (she has read them, and chosen not to think about them), the ninety-nine names in the root cellar, and that her great-grandfather is the reaper.
- **Secret:** she drew the lots last spring, in case no guest came. Her own granddaughter's name was in the bowl. She has not slept properly since.
- **Breaking point:** the fields withering in front of her at the pit. After the third Harvest Bounty she can be turned (DC 12 Persuasion) and calls the field's name to stop the Harvest Lord.

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
**Druid** (MM 346), but she does not cast unless attacked. At the pit she is there to speak. If she fights, she fights to protect the children on the threshing floor, not the Harvest Lord.

## Appearances
- [[SP-OS04-The-Tithe-of-Thornbury]] — Scenes 00, 01, 02, 04, 05

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
Tied to the pact of Thornbury and, through Josiah, to [[SP-OS03-The-Night-That-Doesnt-End]]. If the PCs ignore her, she gives Ned to the field at midnight and Thornbury gets its hundred years. If the pact is broken, she lays down the Sheaf and leads the village into its first hungry winter. If the barn burns, she leads the hunt for the party, quietly, for the rest of her life.
