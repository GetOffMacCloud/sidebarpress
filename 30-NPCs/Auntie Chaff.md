---
type: npc
status: alive
canon: false
faction: ''
location: The mill, Hollow Ford (as Widow Haskell, the green on market day)
aliases: [Widow Haskell]
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
tags: [hallows-eve-quartet, sp-hal-01, hag, villain, fey]
---

# Auntie Chaff

> A green hag under contract to the Gentleman in Grey, delivering twelve folk of Hollow Ford as corn dollies by midnight. Walks the village as **Widow Haskell**, a traveling tinker who sells the prettiest corn dollies anyone has seen.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
**As Haskell:** plump, rosy, a patched shawl, a battered tinker's hat (a *hat of disguise*, though her Illusory Appearance does the real work). Clean, short nails. **As herself:** gaunt, green-grey, hair like wet rope, nails long and crescent-green. Smells of river mud under lavender.

## Personality & Mannerisms
Warm, motherly, presses a dolly into any friendly hand for a copper. Gives sweets to children and counts them while she does it. As herself: patient, sly, a little vain about her workmanship. Says "closed for repairs" in Aldous Crane's exact cadence, because she wrote the line.

## Goals & Secrets
*Wants:* five more villagers before midnight and the Gentleman's wish. *Knows:* the terms of her contract, which she hasn't read as closely as she should. *Secret:* she has lived in Hollow Ford for three weeks, which makes her, by the contract's wording, "folk of Hollow Ford."

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
**Green hag** (MM 177), CR 3. 82 hp (55 at APL 1). Illusory Appearance, Invisible Passage, Mimicry, *dancing lights*, *minor illusion*, *vicious mockery*. **Tactics:** she is not meant to die. At 41 hp she goes invisible and drops down the grain chute. See [[SP-OS01 — Bestiary]] and [[Scene 05 — The Mill]].

## Appearances
- [[SP-OS01-Straw-Men]] — Scene 00 (the busiest stall), Scene 01 (clapping time), Scene 02 (the hand in the barrel), Scene 04 (the stall), Scene 05 (the mill, the climax).

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. Green hag per the 2014 *Monster Manual*; the coven rules don't apply, she works alone.

## Continuity
If she escapes, she carries a grudge and the party's faces, and may surface in any later adventure as a stall-keeper, a midwife, or a kindly aunt. If the party out-reads the contract, the Gentleman takes her as a hag-shaped corn dolly, and that is the end of Auntie Chaff. If she dies, her ledger still names [[The Gentleman in Grey]] and Lady Ysolde Marrow ([[SP-OS02-The-Hollow-Lantern]]).
