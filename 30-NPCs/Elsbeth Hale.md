---
type: npc
status: missing
canon: false
faction: ''
location: Vesper Hollow — Sexton's Ossuary, Elsbeth's Niche (O4)
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
tags: [sp-hal-03, soul, lantern, hallows-eve-quartet]
---

# Elsbeth Hale

> Ambrose Hale's wife, the first soul Thorne took in Vesper Hollow, forty years ago. She exists now as a light in one polished lantern, set apart from the others.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
In the toasts, a name. In the Echo Lanes, "the sexton's wife, who went up to bring him his supper." In the ossuary, a single clean bone lantern in its own niche, with a steadier light than the rest.

## Personality & Mannerisms
Unknown to the party except through Hale's silence and the village's toast: *"To Elsbeth, wherever she's gone!"* — after which half the room goes quiet and nobody can say who she was.

## Goals & Secrets
- Her body is an Echo somewhere in the lanes, forty years old now, repeating the climb to the belfry with a covered dish. The party may find her and not know it.
- Thorne keeps her lantern where he can see it. *"I hadn't meant to take her. One does, though."*

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
None. As a soul she can't act. Her body, if found, is an **Echo** (see [[SP-OS03 — Bestiary]]).

## Appearances
- [[SP-OS03-The-Night-That-Doesnt-End]] — the toast; the Echo Lanes; Elsbeth's Niche (O4)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. No canon source.

## Continuity
Bringing her lantern to Hale is the price of his help: he rings the thirteenth toll no matter what it costs him, and goes below if asked. If the loop ends and her lantern is broken, she wakes at dawn in the lanes with a cold supper in her hands and forty years gone. What Hale and she say to each other is the party's to witness or not.
