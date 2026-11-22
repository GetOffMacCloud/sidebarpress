---
type: npc
status: alive
canon: false
faction: Ritterstadt — the Moot
location: Ritterstadt — the Taubers' lane
aliases: [the Speaker, Reinholt Tauber, Tauber]
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
tags: [ritterstadt, moot, speaker, cooper, gazetteer]
---

# Reinholt Tauber

> Cooper, and Moot Speaker since the Needfest Moot of 575. He speaks for twelve enrolled households to the Ritter and the Warden, and wants to speak for fifty.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Fifty, Oeridian, barrel-chested like his trade, forearms scarred by hoop-iron. Wears the Speaker's chain — a cooper's hoop cut and hammered flat — only on court day.

## Personality & Mannerisms
Plain-spoken, stubborn, slow to anger and slower to forget. Counts on his fingers in public so everyone can see the sum. Married to [[Mathilde Tauber]], who runs the Needfest market and most of his politics.

> *"Twelve seats speak. Thirty-eight are governed. I was elected by the twelve to say that out loud."*

## Goals & Secrets
- **Wants:** the Moot Roll filled to fifty before Needfest, and the labour-levy spent on the eastern gate, not the Ritter's debt.
- **Suspects:** that the Vogt is slowing enrollment. He is right and cannot prove it.
- **Secret:** he has quietly promised the Larch kin-band a seat on the Roll if the Moot ever gets a majority — a promise the Moot's Perrender households would not forgive.

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
**Commoner** (MM p. 345). Strength 15; a cooper's adze (handaxe) hangs on his wall and he knows how to use it.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-02, RG-03

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
Track the Moot Roll's count. If it passes 25, the Vogt starts losing votes.
