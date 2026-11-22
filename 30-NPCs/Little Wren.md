---
type: npc
status: alive
canon: false
faction: ''
location: Vesper Hollow — the chapel yard
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
tags: [sp-hal-03, echo, child, clue, hallows-eve-quartet]
---

# Little Wren

> A child Echo who skips rope under the yew lanterns every night and chants a rhyme nobody taught her. The rhyme is the first clue.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Eight or nine, in a patched festival dress, hair in two plaits that never come loose. Skips without tiring. Eyes grey and still.

## Personality & Mannerisms
Never stops skipping. Never answers a question. Chants, on the beat: *"Toll the twelve and round we go, the reaper sleeps where bones lie low."*

## Goals & Secrets
- **Wants:** nothing. She's hollow.
- **Knows:** the rhyme came from "the grandfather in the chains." Thorne sings it to her lantern, and she sings it to the yard. He wants to be found; he thinks whoever finds him will unchain him.
- **Reaching her:** *calm emotions*, or a kind and patient hour, gets one clear sentence: *"The grandfather in the chains asks me to sing it."* *Speak with dead* fails; she isn't dead.

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
**Echo** (see [[SP-OS03 — Bestiary]]). She never snaps; disrupting her routine only makes her skip faster.

## Appearances
- [[SP-OS03-The-Night-That-Doesnt-End]] — the chapel yard, every loop

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. No canon source.

## Continuity
Her lantern hangs in the Hollow Choir. If the loop ends and it's broken, she wakes at dawn and doesn't remember the rhyme. Prior Benedikt blames Annick Rook for teaching it to her; that accusation is the 7 PM sermon.
