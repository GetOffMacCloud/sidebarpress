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
tags: [aerden, halbritter, horses, sp-pbs-00]
---

# Adalinde Halbritter

> The Jungfer of Erlenhof, twenty-four, who bred the grey mare and is the better rider.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
A grey riding coat, a bucket in one hand, and riding boots she doesn't explain on Derby Day.

## Personality & Mannerisms
Dry and slow to speak. Says less than she knows, and never less than the truth. The only person in the adventure who never lies to the party.

## Goals & Secrets
- **Wants:** to ride Maus at Duffkyyn in her own name, and she will not say so.
- **Knows:** everything about the mare, including when she has been got at; nothing about the note.
- **Reacts:** answers "I ride" and stops. Hands the nearest PC the bucket. If the table sits silent at post time, starts unbuckling her spurs. Delivers the patron's letter on almost every branch.

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
Social only; **scout** (MM p. 349) if she must ride or run.

## Appearances
- [[SP-GA00-Nobodys-Colors]] — Scenes 1, 4, 7, 8; the decline-path re-hook (Scene 0–1)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
None.
