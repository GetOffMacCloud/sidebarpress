---
type: npc
status: alive
canon: false
faction: Hollow Ford
location: The Sheaf & Sickle, Hollow Ford
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
tags: [hallows-eve-quartet, sp-hal-01, innkeeper, ally]
---

# Brann Tully

> Innkeeper of the Sheaf & Sickle in Hollow Ford; a big man trying to keep a festival going while his son is missing.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Broad, red-faced, apron over a good shirt for market day. Forearms like hams. Eyes that keep going to the door.

## Personality & Mannerisms
A big laugh that keeps cracking in the middle. Refills cups nobody asked him to refill. Says "he's fine, he's fine" about Pip and doesn't believe it. Will not hear a word against Mother Nettle, though he'd never say so in front of Father Corwin.

## Goals & Secrets
*Wants:* [[Pip Tully|Pip]] home, and the village to get through the night without noticing anything is wrong. *Knows:* Pip has never stayed out past supper. The mill has been "closed for repairs" exactly as long as things have been odd, and he's only just noticed. *Secret:* he tied the thread bracelet on Pip's scarecrow post himself, three nights ago, without knowing why he felt he had to.

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
**Commoner** (MM 345). If pushed to fight, he swings a cleaver (+2 to hit, 1d6 slashing) and has 11 hp.

## Appearances
- [[SP-OS01-Straw-Men]] — Scene 00 (the hook), Scene 02 (tips the barrel), Scene 04 (leads the party upstream if nobody else does), Denouement.

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. Built on the Hommlet "friendly innkeeper" pattern; in this adventure, the innkeeper is exactly what he looks like.

## Continuity
If the party saves Pip, Brann's inn is the party's home for life (free room and board). If Pip is lost, Brann sells the Sheaf & Sickle and goes looking for a grey carriage; he may turn up in a later adventure as a broken man with a very specific question.
