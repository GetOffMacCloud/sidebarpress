---
type: npc
status: dead
canon: false
faction: House Marrow
location: Marrow Hall — The Bridal Tower
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
tags: [hallows-eve-quartet, sp-hal-02, banshee, villain, bride]
---

# Lady Ysolde Marrow

> The bride. Poisoned her own wedding feast and opened the sluice; drowned in the tower waiting for a boat; a banshee who remembers herself as the victim.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
A drowned wedding dress, veil streaming water that pools on every step. Beautiful in the way a portrait is, and slashed across the eyes in the way hers is. When she smiles the candles lean away.

## Personality & Mannerisms
Wounded, regal, entirely sure she's the wronged one. A hostess first: polite to any guest who keeps the forms, and savage to any who break them. Argues. Says *at last* a great deal.

## Goals & Secrets
- **Wants:** the guest list finished: the four families who "left early" and their blood, every cup drunk at the toast.
- **The truth:** traded her mother's ring to a hag for Sweetsleep (see [[SP-OS01-Straw-Men]]), drugged the wine, opened the sluice with both hands, and waited in the tower for the fiddler's boat. He ran. She drowned.
- **What ends her:** destruction; exposure before the guests (Persuasion DC 15 with evidence); or her mother's voice, if the ring is back in Rowena's stone hand.

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
**Banshee** (MM 23), CR 4. Tactics in [[SP-OS02 — Bestiary]]: no Wail at APL 3; Wail telegraphed one round ahead; Edric immune.

## Appearances
- [[SP-OS02-The-Hollow-Lantern]] — Scene 05 (and her voice in Scene 01)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
Her ring and her Sweetsleep tie back to [[SP-OS01-Straw-Men]]. If the PCs ignore her, the invitees drink and the party's names are on next year's list.
