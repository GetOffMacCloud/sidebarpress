---
type: npc
status: alive
canon: false
faction: Church of St. Cuthbert; Perrender interests
location: Hospice of St. Cuthbert
aliases: [Halya, Sister Halya]
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
tags: [cuthbert, priest, perrenland, spymaster, SP-GA01]
---

# Sister Halya

> Brennin's junior, in her thirties, sharp and pragmatic. She wants the horde as a buffer against Iuz and isn't sentimental about how. She gives the party a sealed letter asking them to spy.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Dark hair pulled back, plain traveling robes, intelligent watchful eyes.

## Personality & Mannerisms
She never raises her voice; she doesn't need to. She explains nothing she has written down.

> *"Brennin's letter is the mission. Mine is for later. Open it in Yecha, not before."*

## Goals & Secrets
- **Wants:** an honest count of the horde's riders and weapons for Perrenland.
- **Secret:** Brennin doesn't know she asked. See [[SP-GA01 — Handout — Halya's Sealed Instruction]].
- **Knows:** what Perrenland would pay to learn the horde's true strength.
- **Escalation:** asked about the letter, she deflects ("if I wanted to say it out loud…"). Confronted afterward, she owns it and writes her report either way (Scene 7: credits by whether they spied).

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
**Acolyte** (MM p. 342). Noncombatant.

## Appearances
- [[SP-GA01-The-False-Arrow]] — Scene 1 and the ending

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
She writes each party member a **letter of field expertise** to their Greyhawk University masters: 25 extra credits if they counted spears, 10 if they didn't. Whatever they told her goes into a report for Perrenland — a hook for a Perrender patron in later parts of *The Plains of Blood and Steel*.
