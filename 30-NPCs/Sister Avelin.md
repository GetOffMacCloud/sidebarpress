---
type: npc
status: alive
canon: false
faction: Chapel of Last Light
location: Marrowmere — Chapel of Last Light
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
tags: [hallows-eve-quartet, sp-hal-02, priest, invitee]
---

# Sister Avelin

> Priestess of the Chapel of Last Light; granddaughter of the bridesmaid who fled the feast; lights every Wake-Light herself.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Forties, grey at the temples, wax on her sleeves. Moves slowly from grave to grave with a taper and never lets another hand light a candle.

## Personality & Mannerisms
Calm, tired, honest. Explains the rite of rest without being asked twice. Disapproves of the reed-cutters' bread on the water and says so mildly.

## Goals & Secrets
- **Wants:** the dead laid to rest; the village to stop barring its doors.
- **Knows:** *"A ghost stays for an unfinished thing. Finish it, and it goes."* She doesn't know what Ysolde's is. She knows that Lady Rowena's effigy in the hall chapel has had an empty hand since before she was born: the seed of the best ending.
- **Secret:** her grandmother was the bridesmaid who didn't drink. She has an invitation and has already decided to go, to finish it.

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
**Priest** (MM 348). Can cast *protection from evil and good* on an invitee if asked, which keeps them awake past 11.

## Appearances
- [[SP-OS02-The-Hollow-Lantern]] — Scenes 00, 02 (sleepwalker), 05 (invitee)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
Her remark about the empty hand must land in Scene 00; Pell repeats it in Scene 01 if it doesn't. If the PCs ignore her, she walks into the mere at 11 with her taper still lit.
