---
type: npc
status: alive
canon: false
faction: ''
location: Marrowmere — The Lantern & Lily
aliases: [Tobias Fenn]
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
tags: [hallows-eve-quartet, sp-hal-02, innkeeper, marrow]
---

# Tobias Marrow

> "Tobias Fenn," innkeeper of the Lantern & Lily; the last Marrow heir, hiding the name and an invitation.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Fifty, trim, well-kept hands for a publican. Good coat, polished boots, the jaw of the portrait turned to the wall in the hall's gallery. Keeps the inn's best window, the one facing the hall, for himself.

## Personality & Mannerisms
Polished, careful, answers questions with questions. Glances at the hall whenever the fiddle reaches the inn. Flinches on the word *nobody.* Refills a cup he's just filled when he's rattled.

## Goals & Secrets
- **Wants:** to get through one more Hallow's Eve without saying his name aloud.
- **Secret:** grandson of Ysolde's little brother, who fled the feast. Bought the inn fifteen years ago with the last of the Marrow money. Has this year's invitation in his apron, addressed to *Master Marrow.* Knows where the chapel bell went.
- **If saved:** reclaims the Marrow name, becomes a lifelong patron (lodging, a boat, a little coin), and gives the party the Vesper Hollow letters.

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
**Commoner** (MM 345). Doesn't fight; weeps.

## Appearances
- [[SP-OS02-The-Hollow-Lantern]] — Scenes 00, 02 (sleepwalker), 05 (invitee), denouement (hook out)
- [[SP-OS03-The-Night-That-Doesnt-End]] — the Letters hook

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
Tied to the Marrow haunting and the missing bell. If the PCs ignore him, he sleepwalks at 11 and drinks at the toast; the Marrow line ends at the table.
