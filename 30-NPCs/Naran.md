---
type: npc
status: alive
canon: false
faction: Chakyik (Tiger Nomads) — Sarnai's household
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
tags: [chakyik, tent-guard, baklunish, SP-GA01]
---

# Naran

> Sixteen, Mother Sarnai's tent-guard and messenger, dying to try out his three words of Common.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Gangly and quick, in a coat too big for him, with a bow he is very proud of.

## Personality & Mannerisms
Eager and loud. He uses his three words ("hello," "horse," "good") at every chance and laughs at himself when they don't fit.

## Goals & Secrets
- **Wants:** to be trusted with something that matters.
- **Knows:** where Sarnai is at any hour, and who has been near the guest tents.
- **Reacts:** at the tent fire he runs for help and brings two riders and a bucket line. He comes on round 3, or on round 1 if Sarnai has endorsed the party. He holds the council flap if the party has prepared.

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
**Commoner** (MM p. 345) with a shortbow, or **Scout** (MM p. 349) if he has to fight.

## Appearances
- [[SP-GA01-The-False-Arrow]] — Scene 5 (guest tent; the fire), Scene 6 (fetches the party), Scene 7 (holds the flap; translates)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
None.
