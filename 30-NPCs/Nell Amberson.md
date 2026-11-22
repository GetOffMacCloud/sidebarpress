---
type: npc
status: alive
canon: false
faction: Candlecrown
location: '[[Candlecrown]]'
aliases: []
species: Human
heritage: ''
gender: Female
age: Adult
alignment: ''
occupation: Tinsmith
class: None (NPC)
subclass: ''
prestige_class: ''
level: ''
adventure_role: color
disposition: friendly
party_trust: '0'
items: []
connected_quests: []
connected_groups: []
parents: []
partner: [Tam Amberson]
children: []
siblings: []
allies: []
enemies: []
deceased_date: ''
tags: [candlecrown, the-tors, sp-gs02, tinsmith]
---

# Nell Amberson

> Candlecrown's tinsmith, with a new baby on her hip and a nanny goat missing from her shed. [Fortubo]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Thirty, wiry, burn-flecked forearms, the baby (Hollin) strapped to her back while she works. **Memorable:** sings to the baby in a whisper over the hammering.

## Personality & Mannerisms
Blunt, quick, practical. Has no time for ghost stories and no patience for people who waste tin. **Quirk:** bites coins.

## Goals & Secrets
- **Wants:** her goat back, and a quiet winter for the baby.
- **Knows:** the goat was taken from a latched shed with no tracks but its own (Fact 5, route b): "Whatever took her could open a latch."
- **Fears:** that the baby will lose its voice before it learns to talk.

## Role & Context
Head of the Amberson household (4): Nell; her husband Tam (gate-watch); baby Hollin; Nell's mother Gret. They keep the village's six goats.

## Conversation Guide
| Topic | Freely discussed? | Notes / sample line |
|---|---|---|
|  |  |  |

## Services
| Service | Cost / notes |
|---|---|
| Tin repairs, buckles, lantern frames | 1 sp–1 gp |

## Quest Hooks
| Hook | Leads to | Trigger |
|---|---|---|
|  |  |  |

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
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — [[Scene 03 — The Second Day]] (the missing goat); [[Candlecrown]] (household 5).

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
If the goat is found alive in the mine (M8), Nell gives the party a tin lantern badge each: the village's mark of thanks.
