---
type: npc
status: alive
canon: false
faction: ''
location: Schwartzenbruin — the Red Cord
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
tags: [perrenland, schwartzenbruin, tavern, sp-pbs-03]
---

# Mutter Ilka Sennhauser

> Landlady of the Red Cord and keeper of the cords. Every company in Schwartzenbruin is a little afraid of her.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Past seventy, small and upright, with a lap full of red cord and hands that tie a knot faster than you can watch.

## Personality & Mannerisms
Dry and watchful. She sees everything that happens at the door and says nothing about it unless asked, and then says exactly what she saw.

> *"Wood is Kord's. Steel is murder. Supper's pork."*

## Goals & Secrets
- **Wants:** the peace of her house kept.
- **Knows:** her grandmother came out of the southern valley on the Kalte Klamm road in 480 and always said *"the Ritter sent them to us."*
- **Escalation:** she watches, and tells what she saw when asked. Her bouncers end any brawl at the end of round 3. She throws a cord-cutter into the lake herself.
- **Knows:** she has never seen Rudi Brack with a company, and he pays in new coin.

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
**Commoner**, MM p. 345. Her two bouncers are **Veterans** (retired Ernes).

## Appearances
- [[SP-GA03-The-Red-Cord]] — Scenes 3, 4 and 6

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
None after SP-GA03.
