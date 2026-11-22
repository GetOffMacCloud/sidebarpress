---
type: npc
status: alive
canon: false
faction: House Brandmeier, Schwartzenbruin (merchant)
location: Aboard the Graue Hecht, Ritterstadt (Brewfest 576)
aliases: [Brandmeier, Herr Brandmeier, Ottokar]
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
tags: [perrenland, schwartzenbruin, merchant, tethered, shadow-on-the-quag, SP-GQ01]
---

# Ottokar Brandmeier

> A Schwartzenbruin merchant in furs, salt and copper. Since Flocktime he has been tethered: a bone pin in his collar makes his clerk's suggestions into his own memories.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
![[SP-GQ01 Portrait - Ottokar Brandmeier.png|300]]

Broad and red-faced, in a fur-trimmed coat; a big laugh. He used to sing at the tiller.

## Personality & Mannerisms
Tethered: genial, generous, repetitive; he glances at his clerk before every number. Awake: horrified, then grateful, then furious.

> *"It's mine by right, you understand. My grandfather's. The University only holds it — and holds it, and holds it."*

## Goals & Secrets
- **Loyalty:** his house and his wife Margarethe. *Deity:* {Zilchus}.
- **Wants (tethered):** "his reliquary." **Wants (awake):** his ship, his wife, his dignity.
- **Knows (awake):** almost nothing since Flocktime. He remembers Fesch arriving with "a letter of introduction from a counting-house in Molag" (thread [[The Molag Seal]]).
- **Secret:** his grandfather Ulrich never set foot in Ritterstadt.

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
**Noble** (MM p. 348).

## Appearances
- [[SP-GQ01-The-Gaolers-Link]]: Scenes 01, 02, 06, 07, 08
- [[SP-GQ00 — Prologue — The Crossing]]: Scenes 2–6 (tethered; free passage)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. Perrender coinage and Schwartzenbruin are canon ([[Perrenland]], [[Schwartzenbruin]]).

## Continuity
Freed, he is the party's friend and way in to Schwartzenbruin's counting-houses (SP-GQ03). Still tethered (Conclusion B or D), freeing him opens SP-GQ02.
