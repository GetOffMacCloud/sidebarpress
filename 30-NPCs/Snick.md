---
type: npc
status: alive
canon: false
faction: Iuz — Dawud Vesharan's familiar
location: Wherever Vesharan sends it
aliases: [Snick]
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
tags: [iuz, fiend, quasit, familiar, shadow-on-the-quag, SP-GQ01]
---

# Snick

> Dawud Vesharan's quasit familiar: spiteful, talkative, greedy for sugar, and the arc's most reliable leak.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
![[SP-GQ01 Portrait - Snick.png|300]]

A finger-thin green imp with a pot belly and a too-wide grin, usually invisible, usually eating something that isn't its own.

## Personality & Mannerisms
Giggles when it should be quiet. Lies about everything except what it most wants to keep secret.

> *"Snick knows things. Snick wants sugar."*

## Goals & Secrets
- **Loyalty:** Vesharan, grudgingly; Iuz, as all the least of the tanar'ri are bullied to (WGR5 p. 15).
- **Wants:** sugar, gossip, and to be rid of Vesharan.
- **Knows:** everything Vesharan says aloud, including "the master's master is in the Heart of Bone," and "the priest-spy in Molag who hates the master's master" (Panshazek; SP-GQ03).
- **Reacts:** spies → mocks → bargains → betrays.

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
**Quasit** (MM p. 63).

## Appearances
- [[SP-GQ01-The-Gaolers-Link]]: Scenes 01, 03, 05, 06
- [[SP-GQ00 — Prologue — The Crossing]]: Scenes 3 and 5 (unseen; tries for the letter-case)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Least tanar'ri as Iuz's servants (WGR5 p. 15). Snick is homebrew.

## Continuity
Spared and bribed, it becomes an unreliable informant for the rest of the arc.
