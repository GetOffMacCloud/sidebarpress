---
type: npc
status: alive
canon: false
faction: The Hundred (Hundertschaft)
location: Schwartzenbruin — the Hundred's chapter-house
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
tags: [perrenland, schwartzenbruin, mercenary, sp-pbs-03]
---

# Hauptfrau Ilse Brandauer

> The newly elected captain of the Hundred, Perrenland's oldest chartered free company. She has come to clear its name this winter, whatever it costs her.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Forty-four, Oeridian-Flan, grey at the temples. She wears a plain company coat with the Hundred's red knot at the collar and keeps her hands folded on the table when she talks.

## Personality & Mannerisms
Precise and dignified, with no small talk. She says "the company" rather than "I." She answers a question fully the first time and will not repeat herself.

> *"The company does not ask to be forgiven. It asks to be finished."*

## Goals & Secrets
- **Wants:** the 480 breach answered before the Council of Hetmen's winter review, so the rival company's petition fails.
- **Believes:** the company's own record that it broke its contract. She brings "the banner we failed" to return it.
- **Escalation:** she proceeds whatever happens. If Jost blocks her, she orders him out (he won't go). If the Soldbrief is lost, she asks the party to recover it, because she cannot leave the clerk. If steel is drawn, she voids the meeting and offers a dawn meeting at the chapter-house.
- **Does not know:** the truth. Kammerer's release-copy lies in the company chest under a seal she has never had cause to break.

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
**Knight**, MM p. 347. Not fought.

## Appearances
- [[SP-GA03-The-Red-Cord]] — Scenes 3 and 6

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. See [[The Hundred]].

## Continuity
None after SP-GA03. This is a one-and-done.
