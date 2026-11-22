---
type: npc
status: alive
canon: false
faction: Greyhawk University — Ritterstadt Field Station
location: Ritterstadt — the Archive
aliases: [the Archivist, Saelithan]
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
tags: [ritterstadt, greyhawk-university, archivist, high-elf, administration, gazetteer]
---

# Saelithan Verenwyr

> The Field Station's Archivist: a high elf of 212 who keeps the maps, field reports, Publications — and the sealed stacks the Registrar closes.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Tall, silver-haired, in a grey archivist's smock with sleeve-guards. Reading spectacles she does not need and wears for the effect.

## Personality & Mannerisms
Dry, impatient with carelessness, generous with anyone who handles paper properly. Built the Archive's slate roof by browbeating the Ritter.

> *"Paper burns. That is why I have a slate roof and no patience."*

## Goals & Secrets
- **Wants:** to know why the Registrar seals what she seals.
- **Knows:** what is in the sealed stacks, because she shelved them — but not what they mean.
- **Secret:** she has read Calloway's charter correspondence and suspects the Regents' promise about the Embrace.

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
Noncombatant. **Mage** (MM p. 347) if pressed; she prefers not to be pressed near paper.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-04, RG-08, RG-09
- [[SP-GQ01-The-Gaolers-Link]]: the Archive by day; Scene 03

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
