---
type: npc
status: alive
canon: false
faction: Chakyik (Tiger Nomads) — war faction
location: Yecha
aliases: [Temur]
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
tags: [chakyik, tiger-nomads, heir, baklunish, SP-GA01]
---

# Khan Temur

> Cligir's nephew and heir-presumptive, thirty, built like a gate. He wants war with the Wolf Nomads before the thaw. He is proud, grieving, and being played — a decent man aimed at the wrong enemy.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Powerfully built, one warrior braid, a tiger-tail standard knotted at his belt, a black-steel sword at his hip, and a broken grey-fletched arrow tucked in his sash.

## Personality & Mannerisms
He paces when he talks, like a man who'd rather be riding. He touches the arrow in his sash when he's angry. Contemptuous of flattery; the young warriors love him.

> *"The south sends us words. Words do not fill bellies. Words do not bury brothers."*

## Goals & Secrets
- **Wants:** the Wolves bled for the winter raids, and his brother avenged.
- **Carries:** the arrow that killed **Tsolmon**, the patrol's lone survivor. He hasn't let anyone look at it. It is the same fake as the ravine arrows.
- **Doesn't know:** that his war-cry was written by [[Master-Kezrin]], or that his black steel came from Iuz.
- **Knows:** every rider's grievance against the Wolves, and how many blades came from Kezrin. He doesn't know what they cost.
- **Escalation:** first he denies ("Wolf arrows, in Wolf fashion"). Then he redirects ("the Wolves raided our herds; that part was true"). Then he acts (he rides east). Shown the arrows side by side, he wavers. Given his brother's body, he listens.

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
**Gladiator** (MM p. 346) if it ever comes to a fight. In the council duel he sends a champion (berserker; see [[SP-GA01 — Bestiary]]).

## Appearances
- [[SP-GA01-The-False-Arrow]] — Scenes 2, 3 (watching), 5 (war camp), 7

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. No canon heir is named for Cligir in the sources used.

## Continuity
Record whether he stood down, rode east with half his riders, or rode with all of them. If the false flag was exposed, he hunts [[Master-Kezrin]] and, through the papers, Yulbar of the Wolf.
