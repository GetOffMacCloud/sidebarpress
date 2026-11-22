---
type: npc
status: alive
canon: false
faction: Ritterstadt — the Moot (Renner household)
location: Ritterstadt — the Farmsteads (Renner longhouse)
aliases: [Jakob, the Reeve, Reeve Renner]
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
tags: [ritterstadt, farmer, reeve, moot, gazetteer]
---

# Jakob Renner

> Reeve of Fields by the Moot Roll. Head of the Renner longhouse, one of the old farming families of Ritterstadt. He allots the common fields and the peat-cuttings and settles boundary quarrels before they reach the Vogt.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Fifty, weather-cut, square hands, a felt hat that has outlived two wives' patience. Carries a tally-stick for every field he allots.

## Personality & Mannerisms
Slow-spoken, fair, stubborn about boundaries and soft about everything else. Walks a disputed field twice before he rules on it.

> *"The stone was here before your grandfather. The stone wins."*

## Goals & Secrets
- **Wants:** the Big Barn re-roofed before the long winter, and enough hay to get through it — Gerold's drying went wrong.
- **Worry:** his best milch cow died last month without cause, and the Brauers lost a pig three days later. People are starting to say "ill luck."
- **Knows:** the Larch elves trade staves for grain off the Moot's book, and lets it ride; the kin-band has never once cheated a field.
- **Secret:** he has noticed Kurt Beckenhaus leaving through the byre door on moonless nights, and has said nothing — yet.

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
**Commoner** (MM p. 345).

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-02, RG-03, RG-04a · [[The Farmsteads]]

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
