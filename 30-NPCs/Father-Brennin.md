---
type: npc
status: alive
canon: false
faction: Church of St. Cuthbert
location: Hospice of St. Cuthbert
aliases: [Brennin, Father Brennin]
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
tags: [cuthbert, priest, oeridian, patron, SP-GA01]
---

# Father Brennin

> Oeridian priest of St. Cuthbert in his sixties, keeper of the [[Hospice-of-St-Cuthbert|hospice]] in the high Yatil pass. Genuinely good, and out of his depth.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Plain grey robes with the cudgel emblem, a worry-worn gentle face, and hands that are always wringing.

## Personality & Mannerisms
He wrings his hands when he's worried, which is always. He holds things — letters, hands — a beat too long.

> *"They are not monsters, whatever the caravans say. They are people with hungry winters. Remember that when they test you — and they will test you."*

## Goals & Secrets
- **Wants:** the caravan road safe, by bread rather than swords.
- **Doesn't know:** that [[Sister-Halya]] asked the party to spy.

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
**Priest** (MM p. 348). Noncombatant.

## Appearances
- [[SP-GA01-The-False-Arrow]] — Scene 1 and the ending

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. St. Cuthbert's church is canon.

## Continuity
He posted his request on the Job Board at the Fiend's Rest in Ritterstadt, and he sends the party's field-credit report to [[Magister-Roswitha-Kartner]] (60/50/40/30/20 by ending). The party has free healing at the hospice forever. If Cligir refused the parley, he plans to go to Yecha himself in spring and asks the party to come.
