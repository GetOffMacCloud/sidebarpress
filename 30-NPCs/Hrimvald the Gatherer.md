---
type: npc
status: alive
canon: false
faction: ''
location: '[[The Ice Library]]'
aliases: []
species: Other (NPC only)
heritage: ''
gender: ''
age: ''
alignment: ''
occupation: Immoth; gatherer of words
class: ''
subclass: ''
prestige_class: ''
level: ''
adventure_role: villain
disposition: wary
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
tags: [immoth, villain, cold, the-tors, sp-gs02]
---

# Hrimvald the Gatherer

> An immoth: a giant of written ice that has come to Candlecrown for the seventh verse of its carol, and will take the village's voices to get it.

**Loyal to:** the curse that drives it to gather, then its own hoard of words; it keeps bargains to the letter.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Twenty feet of glazed blue ice with a long tail, every inch carved with tiny runes. **Memorable:** it never speaks in its own voice; it speaks in the voices it has taken (a Keoish envoy's courtly Common, by default; Wenna's or Dob's dead wife's to make a point).

## Personality & Mannerisms
Patient, vain, curious, fair. Loves words for themselves: compliments a well-made sentence, asks names and repeats them. **Quirk:** pauses before it answers, as if choosing from a shelf.

## Goals & Secrets
- **Wants:** the seventh verse (it was made to gather the curse). *Will settle for:* a word worth more: a true name, a secret no one living has spoken, a confession, the counter-verse. *Fears:* fire, and never finishing.
- **Knows:** every language whose words it has taken; that the curse's verses are scattered across the Sheldomar Valley; that it is a bound thing (it has forgotten that it was made, until the counter-verse reminds it).
- **Reacts:** **offer** (Scene 06: the verse and one voice) → **take** (voices, one a night) → **siege** (Scene 10) → **offer again** (Scene 11, round 1) → **fight** → **offer again, bloodied** → **flee** at 50 hit points or fewer, to the Ice Library.

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
**Immoth** (CR 9); full block in [[Immoth]]; riders in [[SP-GS02 — Bestiary]].

## Appearances
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — Scenes 04 (unseen, the taking), 06 (the offer), 07 (Wenna), 09 (practicing), 11 (the climax), 13 (the rematch).

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
Unbound, it walks free in the high Tors and asks the party to sing the counter-verse to the others. Fooled, it returns in a year. Driven off, it waits in the Ice Library. Destroyed, it leaves the Heart-Rune.
