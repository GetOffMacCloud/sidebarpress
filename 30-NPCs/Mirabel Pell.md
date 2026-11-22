---
type: npc
status: alive
canon: false
faction: ''
location: Marrowmere — The Reed Landing
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
tags: [hallows-eve-quartet, sp-hal-02, invitee]
---

# Mirabel Pell

> Gaffer Pell's granddaughter; invited to the wedding, and furious at being treated as fragile.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Nineteen, reed-cutter's forearms, hair tied back with a strip of sailcloth. Has started humming a tune she's never heard.

## Personality & Mannerisms
Brave, practical, sharp with anyone who talks over her. Wants to row out and see the hall for herself. Says *I'm not a child* three different ways.

## Goals & Secrets
- **Wants:** to be treated as capable; to know what her grandfather is hiding.
- **Secret:** she has an invitation under her pillow and hasn't told him. She'll sleepwalk at 11 PM.
- **As an ally:** if the party gives her a job (a lantern, the boat, a watch on Tobias), she does it well and stays awake past 11 on a Wisdom save DC 13 with advantage.

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
**Commoner** (MM 345); as an ally, treat as a **guard** (MM 347) with a boat-hook.

## Appearances
- [[SP-OS02-The-Hollow-Lantern]] — Scenes 00, 02 (sleepwalker), 05 (invitee); the coffin's name if no PC is invited

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
The default stake if no PC takes one. If the PCs ignore her, she takes her seat at the feast and drinks.
