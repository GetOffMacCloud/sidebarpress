---
type: npc
status: alive
canon: false
faction: The Burrows (gnome artisans)
location: Ritterstadt — the Burrows
aliases: [Pim, Wobblewright]
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
tags: [ritterstadt, gnome, instrument-maker, tinker, training, gazetteer]
---

# Pim Wobblewright

> Instrument-maker in the Burrows. Compasses, astrolabes, and the bog-sounder — a gnome invention nobody else makes. The University buys every compass he finishes.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Young for a gnome, goggles pushed up into wild hair, fingers bandaged from a dozen small cuts, a lathe-pedal callus on his right foot.

## Personality & Mannerisms
Excitable, distractible, brilliant. Explains three inventions in the time it takes to sell one.

> *"It's not broken, it's measuring something we didn't know was there."*

## Goals & Secrets
- **Sells:** compass 25 gp; bog-sounder 15 gp. Teaches **instrument use** for a fee.
- **Wants:** someone to walk a sounder along the tree line near the Hush and bring back the numbers. His sounders have started reading wrong there.
- **Secret:** the "wrong" readings are regular — a pulse every 77 heartbeats.

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
Noncombatant. **Commoner** (MM p. 345) with gnome traits; tinker's tools expertise.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-03, RG-04, RG-05

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
