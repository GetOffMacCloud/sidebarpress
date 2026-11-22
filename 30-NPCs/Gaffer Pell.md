---
type: npc
status: alive
canon: false
faction: ''
location: Marrowmere — The Reed Landing
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
tags: [hallows-eve-quartet, sp-hal-02, boatman, witness]
---

# Gaffer Pell

> Old boatman of Marrowmere; the page boy who carried the cups and saw the bride open the sluice.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Past sixty, hands like knotted rope, a reed-cutter's oilskin he never takes off. Eyes that go to the hall and come back fast. Smells of eel and cider.

## Personality & Mannerisms
Gruff, guilt-ridden, drinks to sleep. Won't talk sober. Treats Mirabel as fragile, which she hates. Once he's talking, he can't stop.

## Goals & Secrets
- **Wants:** Mirabel kept from the water. Not to go inside the hall, ever.
- **Secret:** he was the page at the wedding and didn't drink because he was working. He saw Ysolde at the sluice wheel, both hands, smiling. Fifty years and he's never said it. Standalone, he pulled Rowena's ring from an eel trap last spring and kept it; that's what woke her.
- **Unlock:** cider + Persuasion DC 13, or the coffin's name, or Mirabel sleepwalking.

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
**Commoner** (MM 345). Rows the party across if asked; Strength DC 14 against whatever drags the oars.

## Appearances
- [[SP-OS02-The-Hollow-Lantern]] — Scenes 00, 01, 02; the Frightened Grandfather hook

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
His testimony is one of the exposure ending's pieces. If the PCs ignore him, Mirabel drinks at the toast and he rows out alone at dawn to look for her.
