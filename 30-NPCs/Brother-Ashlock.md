---
type: npc
status: alive
canon: false
faction: Nerullite barrow-cell (Schwartzenbruin)
location: The Dreadverge
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
tags: [villain, nerull, cleric, perrenland, SP-GA02]
---

# Brother Ashlock

> A priest of Nerull traveling as a grey-robed funeral mendicant of Wee Jas. He blesses grieving doors with ash, and the marked households lose someone the next night.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
He is spare and soft-spoken, with tidy grey robes and clean hands except for the ash under his nails. At night he wears the [[Antler-Crown-of-Kethra|Antler Crown]]. By day he hides a jet scythe-pendant under his collar.

## Personality & Mannerisms
He is gentle, unhurried, and genuinely kind to the dying, because he thinks of them as harvest. He speaks of the dead as guests. He wants witnesses more than he wants victories.

> *"The dark of the moon is a kind night for the dead, sister. Tonight they will be easy."*
> *"You are welcome. Every rite wants witnesses."*
> *"The Old One has his own dead. These are mine."*
> *"Eight more chiefs sleep under these hills. I was only the first one sent."*

## Goals & Secrets
- **Wants:** to raise a bone host from Waycombe's captives at Celene-set, then find the other eight chieftain-barrows of the Clatspurs.
- **Secret:** he serves **Nerull**. He reports to "Sister Morrow" of a cell in Schwartzenbruin.
- **Cover story:** he lets Waycombe blame Iuz, and when he wants a household to despair he calls the pack "the Witch's hounds come home," playing on Perrender memory of Iggwilv's dead.
- **Method:** he marks targets with ash circles "for blessing" and steers the pack with the crown.

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
- Cult Fanatic (MM p. 345), modified.
- See [[SP-GA02 — Bestiary#Brother Ashlock — two chassis]].

## Appearances
- [[SP-GA02-The-Bones-of-the-Dreadverge]] — Scenes 1, 2 (by reputation), 4 (camp), and 5 (climax)

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. His god Nerull and his cover deity Wee Jas are canon; see the main adventure note's Canon Check. If captured, he faces a cantonal Rechter (judge).

## Continuity
Tied to [[The Nine Chiefs of the Clatspurs]]. If he escapes, he becomes a recurring villain who knows the PCs' faces. If the PCs never come, he leaves Waycombe with a host by the turning of the year.
