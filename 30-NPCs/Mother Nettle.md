---
type: npc
status: alive
canon: false
faction: ''
location: The wood's edge, Hollow Ford
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
tags: [hallows-eve-quartet, sp-hal-01, hedge-witch, ally, druid]
---

# Mother Nettle

> Hollow Ford's outcast herbwoman. Looks exactly like what the village imagines a hag looks like, and is the only person in it who knows what a hag actually is.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Old, small, a face like a walnut, a shawl of undyed wool. Hands stained green to the wrist from the garden. Dried crows' feet nailed along her lintel.

## Personality & Mannerisms
Prickly and sharp-tongued. Opens the door a hand's width. Respects proof and nerve, not manners. Says less than she knows and never less than the truth. Hands people nettles without warning and watches what they do.

## Goals & Secrets
*Wants:* her neighbors back and to be left alone, in that order. *Knows:* hag lore; that the backward wheel is the key; that Widow Haskell is the one stranger nobody suspects; that a fey contract read closely hurts a hag more than iron. *Secret:* she wrote to a temple three weeks ago (the Hedge-Witch's Letter hook) and never told the village, because they'd have burned her for admitting she could.

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
**Druid** (MM 346). Prepared: *entangle*, *thunderwave*, *speak with animals*, *produce flame*, *shillelagh*. Carries one sprig of **iron-rue** (reveals every Straw Double within 30 feet for 1 minute when burned).

## Appearances
- [[SP-OS01-Straw-Men]] — the Hedge-Witch's Letter hook; Scene 03 (her cottage, the Q&A, the mob); Scene 05 (fights beside the party at APL 1 if protected); Denouement (names Marrowmere).

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. The Hommlet "sinister druid" pattern, inverted: she's the ally.

## Continuity
If protected, she offers the party spellcasting services at cost for life and is the voice that points them to [[SP-OS02-The-Hollow-Lantern]]. She can reappear at the Tithe Barn in [[SP-OS04-The-Tithe-of-Thornbury]] if the party sends word ahead. If driven off at 10 PM, she's gone from Hollow Ford for good, and Father Corwin has to live with that.
