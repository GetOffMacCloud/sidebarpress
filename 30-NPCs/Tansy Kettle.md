---
type: npc
status: alive
canon: false
faction: Candlecrown
location: '[[The Candlecrown Gate]]'
aliases: []
species: Human
heritage: ''
gender: Female
age: Child
alignment: ''
occupation: ''
class: None (NPC)
subclass: ''
prestige_class: ''
level: ''
adventure_role: informant
disposition: friendly
party_trust: ''
items: []
connected_quests: []
connected_groups: []
parents: ['[[Dob Kettle]]']
partner: []
children: []
siblings: []
allies: []
enemies: []
deceased_date: ''
tags: [candlecrown, child, sp-gs02]
---

# Tansy Kettle

> Dob Kettle's seven-year-old daughter, who leaves milk at the gate for "the cold man" and says the thing nobody else will.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Seven, in a red hood two sizes too big, with a gap in her teeth. **Memorable:** she stares at strangers without blinking until they say something.

## Personality & Mannerisms
Fearless, nosy, honest. Knows every hiding place on the crown. **Quirk:** repeats the last word anyone says to her, as a question.

## Goals & Secrets
- **Wants:** her father to smile again. *Fears:* nothing much, which is the problem.
- **Knows:** that someone was crying in the wool loft (Corin); that the cold man on the cliff is polite and likes milk; every hiding place on the crown.
- **Reacts:** leads the party to Corin if they're kind; at the gate, says, "He's waiting for someone to say yes," and then, "I could say yes." She won't fight. Keep her out of harm's way: the village does.

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
**Commoner** (MM p. 345), 2 hit points.

## Appearances
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — Scenes 02, 03, 04, 08, 10 (the wool loft, if Aurel tries it).

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
If Aurel was let in by her, she is the one who has to be told what he was.
