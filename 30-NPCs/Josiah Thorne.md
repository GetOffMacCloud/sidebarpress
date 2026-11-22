---
type: npc
status: unknown
canon: false
faction: The Sheaf (Thornbury); the Harvest Lord
location: Vesper Hollow — the Chain Crypt (O6); later, the Vesper Bell or the road west
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
tags: [sp-hal-03, sp-hal-04, villain, wraith, reaper, hallows-eve-quartet]
---

# Josiah Thorne

> Elder of Thornbury a century ago, who made the pact with the Harvest Lord and became its reaper. A wraith in grave-iron chains under Vesper Hollow's chapel, counting the souls he's owed.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
A thin old man in a Thornbury elder's coat, hands folded, one of them missing a finger. In the dark he's a stooped shadow with something cupped in its hands. He stands to greet guests, as a host does.

## Personality & Mannerisms
Patient, courteous, endlessly hungry. Speaks like a kindly grandfather and never raises his voice. Never lies outright; lies by arrangement. Greets one PC by a name only their dead parent used, and means it as a kindness.

## Goals & Secrets
- **Wants:** the chains off, the bell silent, the road west. The hundredth harvest is this year and Thornbury needs its guest.
- **Knows:** the binding rite exactly. He'll describe it to the party, backwards: *"Nobody's managed it. There's been nobody to try."*
- **Secret:** he's the one who sings the rhyme to Wren's lantern. He wants to be found.
- **The offer:** unchain him and he'll spare the party and leave Vesper Hollow forever. The first half is true. He means to take Hale first and then walk west.

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
**Josiah Thorne, the Tithe-Reaper** — wraith (MM 302) with changes; roughly CR 7. Full block in [[SP-OS03 — Bestiary]]. *Bound to the Bone:* he must move toward his severed finger when it's within 30 feet.

## Appearances
- [[SP-OS03-The-Night-That-Doesnt-End]] — the Chain Crypt; the Thirteenth Toll; a voice from the bell at dawn
- [[SP-OS04-The-Tithe-of-Thornbury]] — sealed in the Vesper Bell as a substitute guest, or free and arriving at 11 PM to claim one

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. No canon source.

## Continuity
Three fates, decided in SP-OS03 and paid in SP-OS04:
- **Bound in the bell:** carried to Thornbury, set at the Empty Chair, and given to the field as the guest who came uninvited.
- **Destroyed:** gone. Thornbury must find its own guest.
- **Escaped:** rides west; joins the Tithe Barn climax as a wraith with his changes, and the Harvest Lord is reduced to 110 hit points to compensate.

The last words from inside the bell: *"They'll have the tables laid by now. Do give them my regards."*
