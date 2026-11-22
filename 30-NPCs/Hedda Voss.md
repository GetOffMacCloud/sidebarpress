---
type: npc
status: missing
canon: false
faction: Hollow Ford militia
location: Hollow Ford (the double); the mill loft (the real Hedda)
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
tags: [hallows-eve-quartet, sp-hal-01, militia, straw-double]
---

# Hedda Voss

> Captain of the Hollow Ford militia. The one walking the village is a Straw Double; the real Hedda hangs in a sack in the mill loft.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Tall, grey at the temples, chain mail polished for market day. Gauntlets on, always, even at table. Stands far back from any fire.

## Personality & Mannerisms
**The double:** too calm. Never raises her voice. Says "everything's in hand" and "the boy's hiding" in the same flat tone. Doesn't eat. Doesn't remember last spring's flood.
**The real Hedda:** sharp, quick-tempered, fond of Pip, and furious when she wakes up and learns what's been walking around in her armor.

## Goals & Secrets
*The double wants:* nobody to look too closely at anything until midnight. It will arrest troublemakers, "lose" witnesses in the chapel cellar, and keep the militia away from the mill. *Secret:* under the gauntlets, her fingers are straw.

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
**The double:** Straw Double with 22 hp, AC 16, longsword +3 (1d8 + 1); see [[SP-OS01 — Bestiary]]. **The real Hedda:** **veteran** (MM 350), but she spends the adventure asleep.

## Appearances
- [[SP-OS01-Straw-Men]] — Scene 00 (first tell), Scene 01 (arrives after the fight), Scene 04 (unmasked), Scene 05 (wakes in M4).

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. The Hommlet "agent hidden in the guard" pattern, made literal.

## Continuity
If the party unmasks her publicly, the militia follows them to the mill, and the real Hedda owes the party a debt she'll repay in iron. If the double is never exposed, it collapses at dawn in the middle of the green, and the village has to explain to itself what it was taking orders from for three weeks.
