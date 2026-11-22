---
type: npc
status: alive
canon: false
faction: None
location: Thornbury — the Bountiful Board (visiting)
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
tags: [sp-hal-04, thornbury, tinker, guest, human, pc-tied]
---

# Old Ned Tallow

> A traveling tinker who came to Thornbury for the festival and has been treated like a lord for three days. He is the backup guest, and he is tied to a PC by default: an old friend, a patron, or the tinker who sold them their first blade.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Sixty, bandy-legged, a tinker's pack he hasn't opened since he arrived. Three days fatter than the PC remembers. A sheaf of wheat tucked in his hatband, a gift from the Elder, which he's very proud of.

## Personality & Mannerisms
Cheerful, oblivious, delighted. Greets the PC he knows like a cousin and tells everyone within earshot about their exploits, half of them wrong. Toasts generously. Takes a second slice of anything to cover a silence. Has no idea what he's been fed.

## Goals & Secrets
- **Wants:** another helping, and for his friend to see how well he's done for himself.
- **Knows:** nothing useful, except that "they keep asking if I've eaten," which is the whole adventure in a sentence.
- **Secret:** none of his own. *Tallow* is one of the six names on the pact, and the Sheaf noticed before he did; he was always going to be welcome at this table.
- **If marked:** he takes the sheaf-mark on his palm as another honor, and walks to the barn humming. He understands at the pit's edge, and then he looks for his friend.

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
**Commoner** (MM 345). In the Colossus's cage he cannot make the DC 15 Strength check to escape.

## Appearances
- [[SP-OS04-The-Tithe-of-Thornbury]] — Scenes 00, 01, 04, 05

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. Swap the surname for one that fits the PC's backstory if the DM prefers; keep it on the pact.

## Continuity
The *welcomed guest* subplot. If the PCs ignore him, he is given to the field at midnight and the pact is paid. If he is saved, he never fully understands what happened, sends the party a mended kettle every year, and never goes back to Thornbury without being able to say why.
