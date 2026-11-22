---
type: npc
status: missing
canon: false
faction: Hollow Ford
location: The mill loft, Hollow Ford
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
tags: [hallows-eve-quartet, sp-hal-01, child, victim]
---

# Pip Tully

> Brann's son, nine years old, asleep in a sack in the mill loft. The one missing villager with no straw double.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Small, dark-haired, scabbed knees. Wearing the green cap his father bought him at last year's market.

## Personality & Mannerisms
Bold. Climbs things. Talks to strangers because his father does. Remembers faces.

## Goals & Secrets
*Wants:* to get home before supper, which is what he was doing when "the lady with green fingers" offered him an apple at the millrace. *Knows:* what [[Auntie Chaff]] looks like without her glamour; he saw her hands. Chaff ran short of straw and never made his double, which is why Brann noticed he was gone and nobody noticed anyone else.

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
**Commoner** (MM 345), 4 hp. Non-combatant.

## Appearances
- [[SP-OS01-Straw-Men]] — the hook; Scene 02 (the apple vision shows him); Scene 05 (asleep in M4). Appears awake only if rescued.

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
If rescued, Pip is the one person who can describe the hag's true face, which makes him useful if Chaff escaped. If lost, he is a corn dolly on the Gentleman in Grey's shelf, and a party that bargains with the Gentleman in [[SP-OS04-The-Tithe-of-Thornbury]] may see him there.
