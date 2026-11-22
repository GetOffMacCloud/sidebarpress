---
type: npc
status: alive
canon: false
faction: The Hundred (Hundertschaft)
location: Schwartzenbruin
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
tags: [perrenland, schwartzenbruin, mercenary, red-herring, sp-pbs-03]
---

# Feldwebel Jost Kammerer

> Seventy-six, the Hundred's oldest serving man, and grandson of the captain who held the Kalte Klamm. He is bound by an oath he can't explain, which makes him look like a saboteur.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Bald and broad, with a beard like a hedge and a pike-scar across both forearms. He moves slowly and sits very still.

## Personality & Mannerisms
Taciturn and stubborn. He drinks with soldiers, not officers. When he cannot answer a question, he says nothing at all rather than lie.

> *"Some debts are paid by saying nothing. Mine is."*

## Goals & Secrets
- **Wants:** to keep the company from swearing to a guilt he knows is false, without breaking his grandfather's oath.
- **Secret:** he holds Hauptmann Lorenz Kammerer's daybook, which records Ritter Wolfram von Eisfeld's written release, the halved standard, and the oath of silence "until the head of my house releases you."
- **Escalation:** first silent refusal, then his one line, then a challenge under Kord. If the oath is forced through anyway, he walks out of the company that night.
- **Released by:** Konrad speaking the words, the two half-standards matched (the proof speaks so he doesn't have to), or a lost bout under Kord.

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
**Veteran** (MM p. 350), with the brawl swap. See [[SP-GA03 — Bestiary]].

## Appearances
- [[SP-GA03-The-Red-Cord]] — Scenes 3 and 6

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. See [[The Hundred]].

## Continuity
He gives the daybook to Konrad at the end. Nothing continues after SP-GA03.
