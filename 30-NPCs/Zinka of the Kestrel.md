---
type: npc
status: alive
canon: false
faction: The Rhennee barges
location: Lake Quag
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
tags: [lake-quag, rhennee, sp-pbs-00]
---

# Zinka of the Kestrel

> A Rhennee woman of the barge Kestrel who calls the grey mare by her stable name and offers 600 marks for her.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Grey-streaked hair under a lantern-lit awning, a voice that carries too well across water.

## Personality & Mannerisms
Amused, direct, and unwilling to say more than she has been paid to.

## Goals & Secrets
- **Wants:** the mare, for someone she won't name.
- **Knows:** only that she was told to watch this boat, and the mare's stable name; she wasn't told why, and has stopped asking.
- **Reacts:** makes the offer once, counts the coin onto the party's own deck if they accept, reads a fortune for anyone who crosses the plank, and lets the barges drop back if refused.

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
Not fought; **commoner** (MM p. 345) if needed.

## Appearances
- [[SP-GA00-Nobodys-Colors]] — Scene 4

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. The Rhennee are canon; their barges on Lake Quag are house. *(Dangling: who sent her?)*

## Continuity
None.
