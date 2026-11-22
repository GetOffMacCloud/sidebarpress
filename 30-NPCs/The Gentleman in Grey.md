---
type: npc
status: alive
canon: false
faction: The Feywild (no court named)
location: A carriage drawn by four black hares; no fixed house
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
tags: [hallows-eve-quartet, sp-hal-01, sp-hal-04, fey, collector, patron]
---

# The Gentleman in Grey

> A fey collector of *doll villages*: real people shrunk into corn dollies and arranged on his shelves. Polite, faceless, and impossible to harm on a road or a threshold.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
A grey frock coat, grey gloves, a grey hat, and under the hat brim, nothing anyone can describe afterward. His carriage is grey, lampless, and drawn by four black hares the size of ponies. Arrives at the stroke of midnight, never earlier.

## Personality & Mannerisms
Courteous to a fault. Tips his hat. Delighted by clever readings of a contract, and by people who refuse him well. Never raises his voice and never repeats an offer. Leaves a grey calling card "for the inconvenience" whether or not he got what he came for.

## Goals & Secrets
*Wants:* twelve folk of Hollow Ford for a new shelf. *Knows:* every bargain in Auntie Chaff's ledger, including the one for a PC's reflection. *Secret:* he honors the letter of a contract absolutely and the spirit not at all. "Folk of Hollow Ford" includes a hag who has lived there three weeks, and he finds that funny.

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
Unharmable in [[SP-OS01-Straw-Men]]: attacks pass through his coat, spells are courteously declined. If numbers are ever needed, start from a **noble** (MM 348) with the **green hag's** Illusory Appearance and Invisible Passage, legendary resistance 3/day, and immunity to all damage while standing on a road or a threshold. See [[SP-OS01 — Bestiary]].

## Appearances
- [[SP-OS01-Straw-Men]] — Scene 05, the landing at midnight; the contract; the calling card.
- [[SP-OS04-The-Tithe-of-Thornbury]] — called in by his card at the Tithe Barn; produces the reflection he bought; the "doll for the field" ending.

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew archfey. No published court; keep it that way so the bundle stays setting-agnostic.

## Continuity
The **calling card** is a fey debt the DM can call in at any time. The **reflection** he bought from Chaff belongs to the PC who ate the apple; in Thornbury, he produces it, and the price of the doll-for-the-field ending is a shadow that PC never gets back. If the party lost sleepers at the landing, those corn dollies are on his shelf, and finding the shelf is a campaign.
