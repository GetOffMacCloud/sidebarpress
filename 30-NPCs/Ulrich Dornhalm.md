---
type: npc
status: alive
canon: false
faction: Dornhalm & Söhne (timber, Schwartzenbruin)
location: Schwartzenbruin — Dornhalm's Yard
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
tags: [perrenland, schwartzenbruin, timber, villain, sp-pbs-03]
---

# Ulrich Dornhalm

> A polite timber factor in very good boots, who paid a cashiered sergeant ten marks to make a Ritter cut his cord.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Fifty, clean-shaven, in a good wool coat. He wears a silver measuring-chain fob and carries a wax tablet everywhere.

## Personality & Mannerisms
Courteous and unbothered. He speaks of people as prices. He never raises his voice, because he has never needed to.

> *"I bought nothing that wasn't for sale. Your Ritter's temper was cheap."*

## Goals & Secrets
- **Wants:** the Eisfeld timber rights. The [[The Kettenhaus|Kettenhaus]] has invited his firm to bid "should the instrument mature," and he means to be ready.
- **Fears:** that the Hundred's swords or coin keep the Schuldbrief from foreclosing.
- **Method:** he hired **Rudi Brack** to bait Konrad and **Little Fenna** to lift the Soldbrief. Both are in his tally-book.
- **Escalation:** he hires the bait, orders the theft, and burns the Soldbrief. Cornered, he talks and offers 50 marks. He surrenders to the patrol rather than fight.
- **The Kettenhaus is not party to any of this.** Its letter to him is ordinary business.

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
**Noble**, MM p. 348. Noncombatant.

## Appearances
- [[SP-GA03-The-Red-Cord]] — Scenes 3 (unseen), 5 and 6

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. *Ritterstadt continuity:* he can be identified with the unnamed Schwartzenbruin timber surveyor from the Ritterstadt campaign's 0005 if your table met him. That identification is optional, and SP-GA03 does not depend on it.

## Continuity
He is taken by the patrol (or flees south, disowned). Nothing continues after SP-GA03.
