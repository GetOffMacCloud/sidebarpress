---
type: npc
status: alive
canon: false
faction: Halbritter of Erlenhof
location: Aerden
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
tags: [aerden, halbritter, noble, sp-pbs-00]
---

# Corwin Halbritter

> The Junker of Erlenhof, nineteen, who forged his father's seal to enter a horse at the Duffkyyn.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Grey coat, good boots, a new saddle he lets no one see. Wipes his hands on his coat when he is nervous, which is always.

## Personality & Mannerisms
Charming in a way that sounds practiced. Answers questions nobody asked and talks past the end of his own sentences. Goes quiet when someone competent questions the plan. From Scene 3 on he asks the party what to do, and means it.

## Goals & Secrets
- **Wants:** to be taken seriously, once.
- **Knows:** the mare, the forged seal on the Erlen Schuldbrief, the rented Ostvelt colors; not that Hessel sold the route.
- **Reacts:** won't offer his sister the ride; if a PC says it, he finally asks her himself. Wants to stand the Derby-eve watch alone.

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
**Noble** (MM p. 348) with changes; see [[SP-GA00 — Bestiary]].

## Appearances
- [[SP-GA00-Nobodys-Colors]] — Scenes 1–8; the stable-rows watch (Scene 6); the rider question (Scene 7)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
None.
