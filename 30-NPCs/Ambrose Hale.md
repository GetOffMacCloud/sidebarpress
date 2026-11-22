---
type: npc
status: alive
canon: false
faction: Chapel of St. Vesper (lapsed)
location: Vesper Hollow — Sexton's Cottage and the belfry
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
tags: [sp-hal-03, ally, jailer, cleric, hallows-eve-quartet]
---

# Ambrose Hale

> The sexton of Vesper Hollow, who caged a reaper under the chapel forty years ago and has rung the bell that holds it every midnight since. The only one in the village who remembers.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Ancient, stooped, with a cleric's big hands gone knotted. A cassock over a chain shirt he never takes off. A bottle in reach at all times, usually unopened by Loop 3. Eyes like an old dog's.

## Personality & Mannerisms
Sardonic, precise, tired past caring about manners. Answers a question with a smaller question. Talks to strangers as if he's met them a hundred times, because he may have. Goes silent when Elsbeth is named. Sits on the gate wall at every dusk and says "new faces" or "not again."

## Goals & Secrets
- **Wants:** the night to end, and someone else to do it. Forty years ago he had the nerve to chain Thorne and not the nerve to go below and finish.
- **Secret:** the first soul Thorne took in Vesper Hollow was Hale's wife, Elsbeth, who brought him supper in the belfry. He has never told anyone. Her lantern is set apart in the ossuary.
- **Knows:** the binding rite exactly. Thirteen tolls with Thorne in his own bone circle seals him in the bell. Someone below with the bone, someone above with the rope.
- **Price:** bring him Elsbeth's lantern and he rings the thirteenth toll no matter what it costs him.

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
**Acolyte** (MM 342) with 22 hit points and AC 12 (chain shirt under the cassock). Carries a *mace of disruption* he no longer uses; gives it to the party at the end. In the belfry he fights the shadows with luck and stubbornness.

## Appearances
- [[SP-OS03-The-Night-That-Doesnt-End]] — the jailer; gate, cottage, belfry, dawn

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. No canon source.

## Continuity
If the party ignores him, he rings the bell every midnight until a PC takes a fourth level of Loop-Weariness; the loop never ends. If the loop ends, he walks out at dawn and doesn't look back. In the "rope" ending he leaves with the party and a PC stays in his place.
