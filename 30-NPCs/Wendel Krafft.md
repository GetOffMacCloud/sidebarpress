---
type: npc
status: alive
canon: false
faction: Greyhawk University
location: Ritterstadt
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
tags: [ritterstadt, field-office, clerk, university, SP-GA05]
---

# Wendel Krafft

> The Field Office clerk at the Ritterstadt Field Station. He signs wardens out. He would like to sign them back in.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance

## Personality & Mannerisms

## Goals & Secrets

## Role & Context
> [!warning] Placeholder name
> Named 2026-11-19 for SP-GA05. If the Tourist vault already has a Field Station clerk, use that person and merge this note.

> [!art]+ Portrait
> ![[SP-GA05 portrait-field-office-clerk.jpg|300]]

- **Loyalty:** The Field Office and its ledgers. [Delleb]
- **Appearance:** Thickset, ink to the wrists, wild grey curls, two pairs of spectacles: one on his nose, one forgotten in his hair.
- **Manner:** Dry and exact. Stamps things while he talks. Never says "north" if he can say "the line".
- **Wants:** Every warden he signs out signed back in.
- **Fears:** The drawer of tokens that came back without their wardens.
- **Knows:** The relay is two riders and a signaller, and the beacon brings the garrison by noon. He believes it. He does not know the second patrol was recalled.
- **Reaction:** Answers any question about procedure and none about the north. At the end he reads the relay log twice, signs the chit without a word, and will not touch the bone clapper.

> *"Sign here. And here. That one's so we know whose token it was."*
> *"The beacon was seen from the palisade. There was no one to send."*

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
Commoner (MM p. 345), with History +4 and Investigation +4.

## Appearances
- [[SP-GA05-The-Pilgrims-of-the-Hollow-Bell]]: Scene 1 and The Report.

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
