---
type: npc
status: dead
canon: false
faction: House Marrow
location: Marrow Hall — The Chapel (H4)
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
tags: [hallows-eve-quartet, sp-hal-02, ghost, mother]
---

# Lady Rowena Marrow

> Ysolde's mother, dead before the wedding; her tomb effigy's stone hand has been empty since her daughter pried the ring out of it. The one voice Ysolde cannot argue with.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
In the gallery portrait: a stern, handsome woman with her hand on a bible and a pearl ring on it. In the chapel: a stone effigy, one hand open, the setting empty. Risen: the portrait, in grey, with the ring back on her finger.

## Personality & Mannerisms
Stern and kind. Speaks once, and the room listens. *"You sold my ring to drown your guests, child. Come home."*

## Goals & Secrets
- **Wants:** her daughter home.
- **Condition:** she rises at the toast only if the pearl ring (from [[SP-OS01-Straw-Men]], or Pell's eel trap) is set in her effigy's hand before midnight.
- **Seeded by:** Sister Avelin's remark (Scene 00), Pell's confession (Scene 01), her portrait and the empty hand (Scene 03).

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
**Ghost** (MM 147). She does not fight. If attacked, she's incorporeal and simply finishes her sentence.

## Appearances
- [[SP-OS02-The-Hollow-Lantern]] — Scene 05 (the ring-returned ending)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
Her ending closes the Marrow haunting forever. If the PCs never find the hand, she stays stone, and the haunting ends only by force or exposure.
