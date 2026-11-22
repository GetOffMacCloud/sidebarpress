---
type: npc
status: alive
canon: false
faction: Kalbach
location: Kalbach
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
tags: [kalbach, sexton, uplands, SP-GA05]
---

# Udo Pfaff

> Sexton of Kalbach, sixty-one, who dug one grave for four and expects to dig three more.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance

## Personality & Mannerisms

## Goals & Secrets

## Role & Context
> [!art]+ Portrait
> ![[SP-GA05 portrait-udo-pfaff.jpg|300]]

- **Loyalty:** Kalbach and its dead. [Pelor]
- **Appearance:** Stooped and wind-burned, in a patched coat, never without a spade or a lantern.
- **Manner:** Speaks to the ground. Counts graves on his fingers when he's frightened.
- **Wants:** His dead to stay in the ground.
- **Fears:** That he buried them wrong, and that it is his fault.
- **Knows:** Only the houses that drew from the square well sickened (F2). The grey folk blessed that well five days ago. He buried the two infants under the lychgate in blessed linen, the way his mother taught him.
- **Secret:** The pilgrims paid him three old silver pieces to "say nothing unkind". He took them, and he has not slept since.
- **Reaction:** Begs the wardens to stay the night. If they do, he gives them the hamlet's last two *potions of healing*. If they find out about the silver, he hands it over and asks them to take it out of the valley.

> *"Only the ones who drank from the square well. I dug for four and I'll be digging for three more."*
> *"I'm not asking the University. I'm asking you. One night."*

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
Commoner (MM p. 345).

## Appearances
- [[SP-GA05-The-Pilgrims-of-the-Hollow-Bell]]: Scene 3 ([[SP-GA05 — E1 — The Kalbach Churchyard|E1]]).

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
