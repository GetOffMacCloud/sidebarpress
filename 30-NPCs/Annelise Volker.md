---
type: npc
status: alive
canon: false
faction: ''
location: '[[The Ritter''s Hall]]'
aliases: [Schatradt, The Iron Ledger]
species: Human
heritage: Human — Flan
gender: Female
age: Adult
alignment: Lawful Neutral
occupation: ''
class: ''
subclass: ''
prestige_class: ''
level: ''
adventure_role: ''
disposition: ''
party_trust: ''
items: ['[[dagger-xphb|Dagger]]', '[[fine-clothes-xphb|Fine Clothes]]', '[[abacus|Abacus]]']
connected_quests: []
connected_groups: ['[[Klauberstadt Council of Trust]]']
parents: [Dieter Volker, Elsbeth Volker]
partner: []
children: []
siblings: [Klaus Volker]
allies: [Gunter Hellsing, Dieter Klauber, Greta Becken]
enemies: []
deceased_date: ''
tags: ['#Category/People']
publish: false
MyContainer: '[[The Ritter''s Hall]]'
MyCategory: Government
image: Annelise_Volker.png
obsidianUIMode: preview
NoteStatus: ❓
---

# Annelise Volker

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
Annelise Volker is the **Exchequer (Schat-Rat)** of Klauberstadt. A native of the Sepia Uplands with strong Flan roots, she possesses an uncanny ability to sniff out hidden mineral wealth and fiscal discrepancies alike. While the others worry about walls and steel, Annelise focuses on the "Lifeblood of the Reach", coin. She is known for her cold, analytical demeanor and her refusal to approve even a single copper for the militia without a signed requisition form.

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
monster: Noble
```

## Appearances

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity

## GM Notes
- Annelise is secretly compiling a "Mineral Map" of the surrounding Uplands, hoping to leverage it to bring more investment from Perrenland.
    
- She shares a quiet, professional respect with Gunter Hellsing, as they are the only two who truly understand the town's logistical vulnerabilities.
    
- She is a devout follower of **Zodal**, god of Mercy and Hope, which creates a strange contrast with her "ruthless" tax collecting.
