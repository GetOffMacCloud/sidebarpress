---
type: npc
status: alive
canon: false
faction: ''
location: '[[The Guardhouse]]'
aliases: [Konstabler]
species: Human
heritage: ''
gender: Male
age: Adult
alignment: ''
occupation: ''
class: ''
subclass: ''
prestige_class: ''
level: ''
adventure_role: ''
disposition: ''
party_trust: ''
items: ['[[longsword-xphb|Longsword]]', '[[chain-shirt-xphb|Chain Shirt]]', '[[longbow-xphb|Longbow]]']
connected_quests: []
connected_groups: ['[[Klauberstadt Council of Trust]]', '[[Klauberstadt Volunteer Militia]]']
parents: [Wilhelm Hellsing, Greta Hellsing]
partner: [Brunhilda Hellsing]
children: []
siblings: []
allies: [Dieter Klausfer, Annelise Volker, Kaelen Stonebeard]
enemies: [Tiger Nomad Raiders]
deceased_date: ''
tags: [Category/People]
publish: false
MyContainer: '[[The Guardhouse]]'
MyCategory: null
image: Gunter_Hellsing.png
obsidianUIMode: preview
NoteStatus: ❓
---

# Gunter Hellsing

> 

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance

## Personality & Mannerisms

## Goals & Secrets

## Role & Context
Gunter Hellsing is the **High Constable (Rat-Konstabler)** of Klauberstadt. A veteran of the brutal skirmishes along the Perrenland border, he carries the scars of nomadic raids and the pragmatic weight of frontier justice. He is a man of few words, preferring the sharp snap of a bowstring to the long-winded debates of the council. Gunter views the Sepia Uplands as a land that must be tamed with iron and vigilance, serving as the iron fist that protects the village's budding commerce.

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
mermaid\n" + lines.join("\n") + "\n```");
```

## Inventory
```dataview
LIST FROM "50-Items" WHERE contains(this.items, file.link)
```

## Stat Block
```statblock
monster: Veteran
```

## Appearances

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity

## GM Notes
- Gunter harbors a deep-seated distrust of the Tiger Nomads after losing his previous unit to a night raid.
    
- He is secretly training the volunteer militia in unconventional forest warfare techniques learned in the Vesve.
    
- He respects Kaelen Stonebeard more than any other council member because the dwarf "speaks in metal."
