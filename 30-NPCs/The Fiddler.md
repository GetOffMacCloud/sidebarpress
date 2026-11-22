---
type: npc
status: dead
canon: false
faction: ''
location: Marrow Hall — The Great Hall
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
tags: [hallows-eve-quartet, sp-hal-02, ghost, lover, musician]
---

# The Fiddler

> The wedding fiddler and Ysolde's lover; the man who was to bring the boat and ran instead; a ghost in the great hall held by guilt.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
A young man's shape in a harvest-fair coat, fifty years out of date, bow never stopping. His fiddle case is still in the escape boat at the water stair. No name survives; Ysolde's diary calls him only *he.*

## Personality & Mannerisms
Plays faster when the subject comes near. Won't meet a musician's eye. Speaks only when asked gently (Persuasion DC 12, automatic for a PC who plays the reel back to him).

## Goals & Secrets
- **Wants:** to be forgiven, by her or by anyone.
- **Confession:** *"I saw her at the wheel. Both hands. I had the boat ready at the water stair and I ran instead. She sang once, the night she died. Don't make her sing again."*
- **At the toast:** plays her out if she's exposed; hides under the table if she's fought; stops playing forever if Rowena takes her home.

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
**Ghost** (MM 147), but he does not fight or possess. Treat him as a haunt with a voice.

## Appearances
- [[SP-OS02-The-Hollow-Lantern]] — Scenes 03, 05, denouement (the bell line)
- Subplot: *the fiddler's tune*; a musician PC's teacher learned the reel from him

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
Lingers after the exposure ending until someone forgives him: a dangling hook. His last line is the bridge to [[SP-OS03-The-Night-That-Doesnt-End]]: *"That bell rang the night we drowned. Wherever it hangs, that night hangs with it."*
