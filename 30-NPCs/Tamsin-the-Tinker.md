---
type: npc
status: alive
canon: false
faction: ''
location: Waycombe (passing through)
aliases: [Tamsin]
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
tags: [merchant, tinker, perrenland, SP-GA02]
---

# Tamsin the Tinker

> A road-tinker with a red-and-yellow cart. She bought the Hound-Mother's torc for twelve kleinmarks and has had her cart attacked twice since.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
She is in her thirties and sunburned, with a hammer always in her belt. Her braid is threaded with tin rings she sells as charms against Iuz.

## Personality & Mannerisms
She is a haggler, practical, and superstitious only when it is profitable. She counts in marks and turns every kindness into a price.

> *"That's twice they've come for my wagon. Twice. What's a dog want with pans?"*

## Goals & Secrets
- **Wants:** to sell the torc to a Schwartzenbruin collector for 250 marks, or at least to get her cart out of Waycombe in one piece.
- **Secret:** she suspects the ring is why the hounds come. She will not admit it until it costs her nothing to.

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
Commoner (MM p. 345). Armed with a hammer (club numbers).

## Appearances
- [[SP-GA02-The-Bones-of-the-Dreadverge]] — Scenes 1 and 2 (the torc negotiation)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. Renamed (formerly "Ysolde") to keep the series' names distinct.

## Continuity
She works the High Gallery and the Traft road. She is a useful recurring merchant or rumor-carrier. If the PCs bullied her, she spreads their names on every road she drives.
