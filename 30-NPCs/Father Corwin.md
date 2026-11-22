---
type: npc
status: alive
canon: false
faction: Chapel of the Sower, Hollow Ford
location: Chapel of the Sower, Hollow Ford
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
tags: [hallows-eve-quartet, sp-hal-01, priest, red-herring]
---

# Father Corwin

> Priest of the Sower, a harvest god, in Hollow Ford. Honest, frightened, and sure that Mother Nettle is the problem.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Thin, fortyish, a brown robe with wheat embroidered at the hem. Hands folded when he's worried, which is always.

## Personality & Mannerisms
Stern in public, kind in private. Preaches against "the witch on the wood's edge" because he can feel something wrong and needs it to have a face. Will not lie, even when lying would be easier. Blesses the market takings with real feeling.

## Goals & Secrets
*Wants:* his flock safe and Nettle gone. *Knows:* that two of his parishioners haven't taken the sacrament in three weeks, and can't say why that frightens him. *Secret:* he has suspected the mill since the wheel changed, and prays about it instead of walking up the road.

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
**Priest** (MM 348). He never fights as written; if forced, he casts *sanctuary* on whoever is being hurt, villager or PC.

## Appearances
- [[SP-OS01-Straw-Men]] — Scene 00 (blessing the market), Scene 01 (watching from the edge of the light), Scene 03 (the 10 PM mob), Denouement.

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. The Hommlet "rival faiths" pattern: the priest is the red-herring accuser, the druid is the ally.

## Continuity
If the party unmasks a double in front of him, he becomes an ally for the rest of the night (rings the bell, slows the clock by an hour) and walks to Nettle's door at dawn to apologize. If the party kills a villager in his mob, he will not forgive it, and Hollow Ford's chapel is closed to them.
