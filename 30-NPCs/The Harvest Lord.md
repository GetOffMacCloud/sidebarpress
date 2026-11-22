---
type: npc
status: alive
canon: false
faction: The pact
location: Thornbury — beneath the Tithe Barn
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
tags: [sp-hal-04, thornbury, villain, treant, plant, spirit]
---

# The Harvest Lord

> An ancient spirit of soil and root, now a corrupted treant rooted beneath the Tithe Barn, its roots under every field in the valley. It made the pact a hundred years ago and has kept every word of it. It speaks through rustling wheat.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
A treant the color of old bone, its crown lost in the barn's rafters, rooted in a pit of black, warm soil. Its bark is grown over with the pewter buttons, bone, and cloth of ninety-nine guests. The wheat on the threshing floor is its hair; the Gold Fields are its hands.

## Personality & Mannerisms
Patient, ancient, courteous in the way of a thing that has never been refused. Speaks in a rustle that is almost words, through any wheat within a mile. Faintly puzzled that anyone objects to a bargain freely made. Does not want a fight; wants what it is owed. Does not understand why healing itself makes the singing stop.

## Goals & Secrets
- **Wants:** the hundredth guest, given, as agreed. Then another hundred years of quiet.
- **Knows:** every word of the pact, and nothing of its loopholes, because a hungry thing doesn't check the fine print.
- **Secret:** its heart can be reached from the root cellar, under the pit's lip, out of sight of the floor. It has never been attacked from below.
- **Weakness:** the pact itself. It will accept anything the words allow: a bell with a reaper in it, a corn-dolly double, a corpse that was welcomed at the table. It cannot refuse what is legally given.

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
Custom: see [[SP-OS04 — Bestiary]] (**treant** base, MM 289, rooted, 20-ft reach, lair actions *Grasping Wheat* and *Harvest Bounty*). CR 9.

## Appearances
- [[SP-OS04-The-Tithe-of-Thornbury]] — Scene 05 (and the fields, Scenes 02–03, as its hands)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. The pact is the thing to keep if reskinning: the Harvest Lord can be any hungry land-spirit the setting already has.

## Continuity
Fed for a century by [[Josiah Thorne]]'s reaping (see [[SP-OS03-The-Night-That-Doesnt-End]]). If the pact is fulfilled by the letter (bell or doll), it closes and the Harvest Lord goes dormant: the fields are ordinary after, and it does not wake again unless someone makes a new bargain. If it is killed, the fields rot overnight. If it is paid, it sleeps for a hundred years, and the next hundredth Hallow's Eve is someone else's problem. If the party ignores it, it takes whoever is given and is perfectly satisfied.
