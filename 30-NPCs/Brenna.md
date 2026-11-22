---
type: npc
status: alive
canon: false
faction: The Yati
location: Sepia Uplands
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
tags: [yati, drover, old-faith, uplands, SP-GA05]
---

# Brenna

> A Yati drover bringing her flock down for the winter, with a dog, a crook, and no patience for students.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance

## Personality & Mannerisms

## Goals & Secrets

## Role & Context
> [!art]+ Portrait
> ![[SP-GA05 portrait-brenna.jpg|300]]

- **Loyalty:** Her flock, then her clan. [Obad-Hai, Beory]
- **Appearance:** Fifties, grey braids, a fleece coat, a sheepdog that watches whoever she is talking to.
- **Manner:** Answers a question with a shorter question. Softens for anyone who is good with animals.
- **Wants:** Her flock out of the valley before dark.
- **Fears:** The Tor. Her grandmother saw the bell struck by lightning and would never say what she heard.
- **Flaw:** She leaves at first light whatever happens. She will not fight for Kalbach.
- **Knows:** The lambskin custom (F4). The Hanged Stag rite and the Winter Telling (Handout 5). That orcs are camped under the Tor and aren't raiding.
- **Reaction:** Wary of University people; warms to anyone who knows the Old Faith or helps with the sheep. **Safety valve:** if the table is stuck, Brenna says plainly what she has seen and where the grey folk are going.

> *"University. You'll be wanting to write us down, then."*
> *"When the old priests rang it, they wrapped it in a lambskin after. So the sound would sleep."*

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
Scout (MM p. 349). Her dog is a mastiff.

## Appearances
- [[SP-GA05-The-Pilgrims-of-the-Hollow-Bell]]: Scene 3. The Yati who give [[The Yati Lambskin]] after Ending A are her clan.

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. The Yati are a house name for Flan-descended highland clans.

## Continuity
