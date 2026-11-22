---
type: npc
status: alive
canon: false
faction: The Sheaf (doubter)
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
tags: [sp-hal-04, thornbury, ally, doubter, human]
---

# Tamsin Reap

> Barnaby's daughter, nineteen, and the only person in the Sheaf who has done the arithmetic. She'll help the party if they give her a reason to believe there's another way.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Thin, quick, cider-jug on one hip, hair tied back with a strip of sacking. Her hands are never still. She wears no wheat: no garland, no sheaf, no brooch. Nobody in Thornbury has noticed.

## Personality & Mannerisms
Sharp, nervous, keeps almost saying something and then saying her father's name instead. Watches one PC from the green onward, the one she's decided is most likely to listen. Says *"Don't—"* and then pours cider.

## Goals & Secrets
- **Wants:** nobody in the pit tonight, and to still have a village in the morning. She knows those might not both be possible.
- **Knows:** the procession route (the long way round the north field), that the heart is under the threshing floor, and that the barn's rear door into the root cellar has a key, which she holds.
- **Secret:** she has read the pact's vellum a dozen times, alone, and found the loopholes herself. She hasn't told Prudence because she's afraid Prudence already knows.
- **Breaking point:** she will not leave Thornbury, whatever happens. *"Someone has to be here after."*

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
**Commoner** (MM 345). Not a fighter. She holds doors.

## Appearances
- [[SP-OS04-The-Tithe-of-Thornbury]] — Scenes 00, 01, 02, 05

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
Daughter of [[Barnaby Reap]]. If the pact is broken, she and [[Hesper Gloam]] teach the village to farm ordinary seasons. If the pact is paid, she leaves the Sheaf, stays in Thornbury, and starts counting the years to the next hundredth. A PC who earned her trust gets a letter from her every Hallow's Eve.
