---
type: npc
status: alive
canon: false
faction: The Rotting Table
location: The Smokehouse (Hommlet)
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
tags: [hommlet, zuggtmoy, temple-of-elemental-evil, villain, sp-gs01]
---

# Deacon Mungo Brindlewick

> A surviving priest of the Temple of Elemental Evil who serves Zuggtmoy, raised the Gluttonwretch, and says grace before every mouthful.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Round, pink and cheerful, in brewer's leathers stained black with mold. Mushroom spores in his beard. Always has a napkin tucked into his collar.

## Personality & Mannerisms
Genial, devout and completely sincere. Treats every meeting as a meal and every meal as worship. Never raises his voice; always invites people to say grace.

## Goals & Secrets
- **Wants:** to gorge Hommlet at its Brewfest feast, crack one of Zuggtmoy's seals under the Temple, and be promoted out of a burned rendering house.
- **Knows:** the rite that raised the Wretch; the Wishbone; Rannos and Gremag's supply line; the "second table" in the Temple's lower halls.
- **Reacts:** deny ("I'm a brewer") → redirect (invites the party to dinner) → infiltrate (sits in the feast crowd) → betray (snaps the Wishbone himself if about to be captured: "If she can't have the village, she'll have the bird.").

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
**Mage** (MM p. 347), reskinned; spell swaps and Grace Before Meat in [[SP-GS01 — Bestiary]].

## Appearances
- [[SP-GS01-The-Gluttonwretch-of-Hommlet]] — Scenes 05 and 07; the cult's handler for the Wretch.

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. Zuggtmoy as the Temple's patron follows T1-4 *The Temple of Elemental Evil* (1985).

## Continuity
Opens [[The Rotting Table]]. If he escapes, he reaches Nulb and the Temple; his cipher book names the "second table."
