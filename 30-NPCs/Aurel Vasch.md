---
type: npc
status: alive
canon: false
faction: none
location: Candlecrown
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
tags: [vampire-spawn, undead, the-tors, sp-gs02, slerotin]
---

# Aurel Vasch

> A polite vampire spawn whose master died in the Passage of Slerotin, sheltering in the mine under Candlecrown and asking, very nicely, to be let in. {Wee Jas, lapsed}

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Looks thirty, has been dead two months. Pale, dark-haired, in a good Keoish traveling cloak gone stiff with frost. **Memorable:** snow settles on his shoulders and doesn't melt; he casts no shadow.

## Personality & Mannerisms
Courtly, cold, tired, honest about bargains and nothing else. Was a manservant in life and still says "Forgive me" before every request. **Quirk:** always sits facing the door.

## Goals & Secrets
- **Wants:** warmth, blood, and a way out of the Tors (to Loftwick, and then anywhere). *Fears:* the immoth (he saw one in the Passage), sunlight, and being alone again.
- **Knows:** **Immoths:** he saw one at a sealed door in the Passage of Slerotin; it bargained with his master before it killed the others, and took "a name" from him (Fact 3). **The chapel:** he can read enough Suloise to read the counter-verse aloud. **His master's true name:** Ilvan Dross's secret name, given to Aurel the night he was made, "a word no one living has spoken." **The threshold:** he knows only a villager's invitation works, and won't say so unless asked directly.
- **Reacts:** **ask** ("May I come in?") → **plead** ("Two days on that cliff") → **bargain** (immoth lore, the reading, the true name, for an invitation; half of it for safe passage) → **try another door** (the wool loft window, a child). Inside, he feeds and makes a thrall. He keeps any bargain to the letter. He flees rather than fights.

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
**Vampire spawn** (MM p. 298) with SP-GS02 riders; see [[SP-GS02 — Bestiary]].

## Appearances
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — Scenes 05 (M8, his shelter), 08 (the knock), 09 (hunted), 10–12 (if invited or refused).

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
If he survives and a bargain is kept, he owes the party a favor and knows where his master's grave and papers lie at Bleak Gate, the eastern mouth of the Passage (see the C12 conversion). His master was **Ilvan Dross**, an explorer, now dead; no note.
