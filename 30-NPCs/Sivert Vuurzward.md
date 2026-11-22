---
type: npc
status: alive
canon: false
faction: Clan Vuurzward
location: Schwartzenbruin
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
tags: [schwartzenbruin, vuurzward, moneylender, antagonist, sp-pbs-00]
---

# Sivert Vuurzward

> A moneylender and breeder of Clan Vuurzward who holds the forged Erlen Schuldbrief and wants Erlenhof.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
A good hat, held in his hands the entire time. Vuurzward green, dark enough to read as black.

## Personality & Mannerisms
Courteous, patient, never threatens, never lies; he leaves things out. Makes his offer to the party, not to Corwin.

## Goals & Secrets
- **Wants:** Erlenhof: the land, the bloodline, and the grey mare. "Because I've seen her mother run."
- **Knows:** that the seal is forged; that Hessel sold the route; any debt a PC carries, which he has bought. His money behind the note is Kettenhaus credit.
- **Reacts:** offers to burn the note for the mare. Lies only once ("I don't know the name," Insight DC 18). Asked straight about the leak: "I don't lie, scholar. Ask me something else." Cannot be punched: his cousin is the Schultheiss.

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
Not fought; see [[SP-GA00 — Bestiary]].

## Appearances
- [[SP-GA00-Nobodys-Colors]] — Scene 5; offstage in Scenes 4, 6 and 7

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. Clan Vuurzward is Living Greyhawk material; see [[Perrenland-Mercenary-Companies]].

## Continuity
Dangling: his money is Kettenhaus credit. See [[The Kettenhaus]].
