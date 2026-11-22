---
type: npc
status: alive
canon: true
faction: Chakyik (Tiger Nomads)
location: Yecha
aliases: [Cligir, the Unvanquishable Tiger Lord]
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
tags: [chakyik, tiger-nomads, ruler, baklunish, SP-GA01]
---

# Ilkhan Cligir

> The Unvanquishable Tiger Lord, ruler of the [[Chakyik]] in 576 CY. Old, small, and very still. He refused Iuz's alliance, and he is impressed only by people who keep their word.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Seventyish and small, with eyes like chipped flint and a white-streaked beard. He sits on a low throne draped in a saber-tooth robe the color of old blood.

## Personality & Mannerisms
He lets silence do the shouting. He speaks slowly, in Baklunish, through Sarnai, and while she translates he watches the party's faces. Dry, tired, amused at his own expense.

> *"You came in winter. Either you are very brave or your priest pays very well. Which is it?"*

## Goals & Secrets
- **Wants:** to die with the horde whole, and an heir who can tell a friend from a merchant.
- **Secret:** he suspects Kezrin but has no proof, and won't shame Temur without it.
- **Tradition:** by Ogobanuk's decree, he studies the art of beguilement (illusion). He never uses it on the party.
- **Knows:** that his nephew is being played, but not by whom. He knows the parley terms Brennin can afford.
- **Escalation:** he watches and says nothing until custom requires a ruling. Then he rules once, briefly, and doesn't revisit it.

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
Noncombatant in this adventure. If needed, use **noble** (MM p. 348) with *minor illusion* and *silent image* at will.

## Appearances
- [[SP-GA01-The-False-Arrow]] — Scenes 2 and 7

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
**Canon:** ruler of the Tiger Nomads, "the Unvanquishable Tiger Lord"; rebuffed Iuz's advances (*WoG* 1983; *LGG* 2000 p. 114). By 591 CY he is dead and Ilkhan Gajtak rules (*LGG*). **Homebrew:** his manner, his voice, and the tiger-claw token.

## Continuity
If the party earned Favor 7+, he gave them [[Tiger-Claw-Token|the tiger-claw token]] from his own wrist. He told Brennin to come in spring if the parley was refused.
