---
type: npc
status: alive
canon: false
faction: Greyhawk University — Department of Statecraft & Commerce
location: Ritterstadt
aliases: [Goldwaage, Professor Goldwaage]
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
tags: [ritterstadt, greyhawk-university, department-head, statecraft, law, gazetteer]
source_canon: A Tourist In Greyhawk — 08 — Department of Statecraft & Commerce (placeholder head)
---

# Professor Aldemar Goldwaage

> ![[Ritterstadt goldwaage.jpg|300]]

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Fifties, neat grey beard, merchant's spectacles, a lawyer's satchel of other people's contracts.

## Personality & Mannerisms
Dry, patient, and fond of the clause nobody read. Answers questions with a question about the fine print.

> *"The Cantons will not send a garrison. They will send a form. Learn to read forms."*

## Goals & Secrets
- **Wants:** Ritterstadt to stay unincorporated, and the Moot Roll filled.
- **Drafted:** the 574 Moot Roll amendment, at the Vogt's request.
- **Secret:** he wrote the labour-levy clause the way the Vogt asked, knowing it would slow enrollment. He has regretted it since Reinholt Tauber became Speaker.

## Role & Context
> [!art]+ Portrait

> Head of the Department of Statecraft & Commerce. He teaches the Vogt's clerks, drafted the Moot Roll's wording in 574, and reads every form the Cantons send.

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
Noncombatant. **Noble** (MM p. 348), Intelligence 16, expertise in Persuasion.

## Appearances
- [[Ritterstadt — Gazetteer (Book)]] — RG-02, RG-08, RG-09
- [[SP-GA03-The-Red-Cord]] — Scene 1 (posts the commission); Konrad's report to him sets the field credits

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
A **placeholder department head** in the campaign vault's `08 — Department of Statecraft & Commerce`. Anything beyond that note is Gazetteer elaboration; a full campaign note overrides this one.

## Continuity

## His Department
**Major:** Political Philosophy & Diplomacy · **Minors:** Economics & Trade · Law & Heraldry. His lecturer: [[Lecturer Bertram Falk]] (Law & Heraldry).
