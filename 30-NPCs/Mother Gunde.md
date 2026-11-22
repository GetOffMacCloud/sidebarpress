---
type: npc
status: alive
canon: false
faction: The Graue Hecht (crew)
location: Lake Quag — aboard the Graue Hecht
aliases: [Gunde, the Hecht's cook]
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
tags: [shadow-on-the-quag, rhennee, lake-quag, graue-hecht, functionary]
image: SP-GQ00 Portrait - Mother Gunde.png
---

# Mother Gunde

> The *Graue Hecht*'s cook: a Rhennee widow who has buried two husbands in the lake and knows exactly how much fog a lamp will hold back.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
![[SP-GQ00 Portrait - Mother Gunde.png|300]]
Tall and rawboned, sixty or so, bareheaded with two long grey braids, in a man's oilcloth coat over her skirts, with a brass ring in one ear and burn-scars across the backs of both hands from forty years of galley braziers. Always has a ladle or a lamp in her fist.

## Personality & Mannerisms
Brusque, superstitious, practical; talks to the lake as if it can hear her. Feeds students first and asks them questions while they eat.
> *"Say your prayers before the grey, not in it. In it, you hold a lamp."*

## Goals & Secrets
- *Deity:* [Osprem]
- **Wants:** the *Hecht* home, and her sugar to stop disappearing.
- **Knows:**
  - the Rhennee fog-charm: a lit lamp in each hand keeps the drowned off (fire and radiant stop the [[Fog-Drowned]] from regenerating);
  - "something with a sweet tooth and no feet" is stealing her sugar every night ([[Snick]]);
  - there are more drowned in the grey this year than she has ever seen (the Blackfrost Bloom);
  - the master hasn't been right since spring, and "the clerk eats nothing hot."
- **Secret:** her second husband went into the grey on another ship nine years ago. She thinks she saw him come over the rail once, and she has never told anyone.
- **Reacts:** gruff → warm to anyone who helps in the galley → fierce in a fight with a lamp in each hand.

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
**Commoner** (MM p. 345), or **bandit** (MM p. 343) with a cleaver if she must fight. In the fog boarding she keeps two lamps lit and shouts the fog-charm.

## Appearances
- [[SP-GQ00 — Prologue — The Crossing]]: Scenes 2–5 (the galley, H5; the fog-charm in Scene 4; the boarding in Scene 5)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
- She knows the grey better than anyone on the *Hecht*; a party heading onto the frozen Quag in GQ5 can find her wintering at the Landing.
- If the drowned in Scene 5 include her husband's face, that's the DM's call. It's a beat, not a mechanic.
- Named per the functionaries rule (2026-10-23).
