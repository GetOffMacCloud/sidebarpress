---
type: npc
status: alive
canon: false
faction: Greyhawk University — Department of Statecraft & Commerce
location: Ritterstadt
aliases: [Bertram Falk, Lecturer Falk]
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
tags: [ritterstadt, greyhawk-university, lecturer, law, heraldry, half-elf, gazetteer]
---

# Lecturer Bertram Falk

> Lecturer in Law & Heraldry, Department of Statecraft & Commerce. A half-elf who identified the unfamiliar arms on the Ritter's Hall shield — and has not said whose they are.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Forties, neat, a lawyer's black coat with a heraldic pin he changes daily.

## Personality & Mannerisms
Precise, amused, careful about who asks. Answers legal questions with three possible answers.

> *"Heraldry is just law that learned to dress."*

## Goals & Secrets
- **Wants:** a copy of the original Land-Grant of 565.
- **Secret:** the arms on the old shield in the Ritter's Hall are those of a Furyondian house extinct since 494 — the same arms on the Founder Edmund von Eisfeld's mother's side. If the land-grant passed through that house, the Hanselmann letters under the dais matter even more.
- **Waiting:** to be asked by the right person.

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
Noncombatant. **Noble** (MM p. 348), Intelligence 16.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-09
- [[SP-GA03-The-Red-Cord]] — Scene 1 (optional consult: the halved-standard custom); extra credit for an account of the custom

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity
