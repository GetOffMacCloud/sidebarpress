---
type: npc
status: alive
canon: false
faction: Iuz — Kermin Mind-Bender's tether-mages (Greater Boneheart)
location: Ritterstadt, aboard the Graue Hecht (Brewfest 576)
aliases: [Vesharan, Herr Fesch, Fesch, Dawud]
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
tags: [iuz, kermin, tether-mage, villain, bakluni, shadow-on-the-quag, SP-GQ01]
---

# Dawud Vesharan

> Kermin Mind-Bender's field agent, about 24, Bakluni, Ket-born, taken from a schoolroom at nine. In Ritterstadt he passes as "Herr Fesch," Ottokar Brandmeier's clerk. The recurring villain of the Shadow on the Quag.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
![[SP-GQ01 Portrait - Dawud Vesharan.png|300]]

As Fesch: a thin Perrender clerk with ink on his cuffs and a glove on his left hand. As himself: a young Bakluni man with a close-trimmed beard, tired dark eyes, and a burn scar across his left palm from the one time he tried to hold a relic.

## Personality & Mannerisms
Courteous, precise and starved for respect. Corrects everyone's arithmetic. Keeps a table between himself and any holy symbol.

> *"The University will teach you to catalogue things like that. My master would teach you to use them."*

## Goals & Secrets
- **Loyalty:** [[Iuz]], through Kermin Mind-Bender. *Deity:* [Iuz], from habit more than faith.
- **Wants:** the [[The Gaoler's Link|Link]], and a place among Kermin's mid-level mages.
- **Fears:** going home empty-handed; his master's attention; being forgotten.
- **Knows:** the Link's powers, the tethers, the route north, and Liesl Amsel's name.
- **Escalation:** coax → recruit → threaten → grab ([[Scene 06 — The Handover]]).
- **Secret:** he would defect if he believed he could survive it (SP-GQ05).

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
[[Tether-Mage]] (Named Example). Carries a *potion of water breathing*. Familiar: [[Snick]] (quasit).

## Appearances
- [[SP-GQ01-The-Gaolers-Link]]: Scenes 01, 02, 06, 07 (as Fesch, then himself)
- [[SP-GQ00 — Prologue — The Crossing]]: Scenes 2–5 (as Fesch; flees into the fog if unmasked)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. His master, Kermin Mind-Bender, and Kermin's recruitment of gifted children are canon (WGR5 p. 86). Kermin's Greater Boneheart rank in 576 is a house ruling.

## Continuity
If he escaped, he returns in SP-GQ02 and SP-GQ05 with new faces. If captured, he talks only near the Link (the defection path). Thread: [[Kermin's Tethers]].
