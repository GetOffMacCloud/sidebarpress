---
type: npc
status: alive
canon: false
faction: ''
location: '[[Ritterstadt]]'
aliases: []
species: Dwarf
heritage: Dwarf — Mountain
gender: Male
age: Adult
alignment: Neutral
occupation: Blacksmith Apprentice (Acting)
class: ''
subclass: ''
prestige_class: ''
level: ''
adventure_role: ''
disposition: Neutral
party_trust: 0
items: []
connected_quests: []
connected_groups: []
parents: []
partner: []
children: []
siblings: []
allies: [Brunhilde Hammerschlag]
enemies: []
deceased_date: ''
tags: [Category/People, NPC, ritterstadt-npc]
publish: false
name: Hogar Irongrip
MyContainer: '[[The Iron Anvil]]'
MyCategory: null
image: Hogar_Irongrip.png
obsidianUIMode: preview
NoteStatus: ❓
town_role: Industrial / Basic Metalwork
shop: The Iron Anvil
founder: false
---

# Hogar Irongrip

> A soot-streaked dwarf with wide, panicked eyes and hands that tremble slightly when he isn't holding a hammer — a young apprentice thrust into a master's role he wasn't ready for, trying very hard not to show it.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
A young mountain dwarf with a thin, poorly-braided beard. His leather apron is several sizes too large — it belonged to his missing master, Brakken Hammer-Fall. His hands are steadier when he's working than when he isn't. He smells of coal and iron and something that might be anxiety.

## Personality & Mannerisms
Mumbles the steps of smithing out loud to remember them ("heat to orange, not yellow — Brakken said orange"). Frequently glances toward the dark corners of the forge, as if expecting something to emerge. Quotes Brakken like scripture. Flinches at sudden sounds after dark.

## Goals & Secrets
### 💡 Key Motivation
Keep the forge fires burning until Brakken comes back. Or prove he can handle the heat if Brakken doesn't. He hasn't decided yet which of those things he's actually preparing for.

### The Real Story
Brakken Hammer-Fall was not taken by wolves or bandits. Something came for him specifically — something that knew his name. Hogar heard Brakken say "you" in the dark, in the tone of recognition, before the sound stopped. He has told no one this because articulating it would make it real. He has convinced himself it was wolves. Wolves don't speak to their targets by name.

### What They Know (But Won't Say)
- Brakken's indenture papers are still in the forge office. Hogar is legally bound to The Iron Anvil until Brakken releases him or is confirmed dead. He has no idea what his legal status becomes if Brakken never returns.
- He arrived as an indentured apprentice from a dwarven clan in the Lortmils who owed a debt to Brakken's guild. He has one year of service remaining on a three-year indenture.
- He heard the word "you" — spoken by Brakken, not shouted. Recognition, not alarm.

### What They Fear
That Brakken isn't coming back, which means he's stuck here alone indefinitely, which means he will eventually have to admit to everyone that he can't actually run this forge at the level they need. And underneath that: that whatever took Brakken knows where the forge is.

### How to Reveal It
The "you" detail comes out only at high trust, in a private conversation, probably at night when the party is the only ones at the forge. He'll say it in the middle of something else, almost like he's been waiting to say it out loud: *"He said 'you.' Just that. Like he knew it. Like he'd been expecting it."* Then he'll go back to whatever he was doing, as if he didn't say anything.

## Role & Context
Hogar is currently the only person operating The Iron Anvil. He is the hamlet's source of basic tool repair, edge sharpening, and simple metalwork. He cannot forge weapons or plate armor without supervision. If he fails — if the forge goes cold — Ritterstadt loses its only accessible metalwork service until a replacement is found or Brakken returns.

## Conversation Guide
| Topic | Freely Discussed? | Notes / Sample Line |
| :--- | :---: | :--- |
| Basic smithing services | ✅ | Gets more confident once the conversation is practical |
| Brakken's absence | ⚠️ | "He was taken in the night. Three weeks ago. I'm managing." (He is not managing.) |
| What he heard that night | ❌ | "It was wolves. Probably wolves. I didn't look." |
| His indentured status | ❌ | Doesn't bring it up; panics if it's raised directly |
| Bruni / the other forge | ⚠️ | "She does the heavy work. I do... the other work." |
| The dark corners of the forge | ❌ | Denies looking at them. Looks at them again immediately. |

### 🔑 Trust-Gated Information
- **Low Trust (stranger):** Nervous, competent enough at the basics, will take any legitimate commission. Tells the party Brakken is "away" before correcting himself to "missing."
- **Medium Trust (regular):** Admits he's scared. Admits the forge is barely running. Will tell them Brakken was "taken" — not just gone — and that something came into the forge that night. He doesn't know what.
- **High Trust (friend / proven):** Describes what he heard: a sound that wasn't footsteps, a cold smell, Brakken calling out once — not in alarm, in recognition. As if he knew whatever came for him. Hogar has been too frightened to think about what that means.

## Services
| Service | Cost / Notes |
| :--- | :--- |
| Tool repair & sharpening | Standard rate; he's competent at this |
| Basic implement fabrication | Nails, brackets, hinges — manageable |
| Edge sharpening (weapons) | He can do this; he just won't say so confidently |
| Weapon or armor fabrication | ❌ — not without supervision; he will refuse or produce inferior work |

## Quest Hooks
| Hook | Leads To | Trigger Condition |
| :--- | :--- | :--- |
| "Brakken was taken in the night. I don't know by what." | Future arc: Brakken's disappearance | Party asks about the missing master at any point |
| The forge going cold / Hogar asking for help | Future arc: the Iron Anvil's survival | If the party doesn't intervene, quality of services degrades over time |
| Materials recovered in the field | Artisan growth system | Party brings Hogar rare metals or materials from uplands expeditions |

## Relationships
```dataview
TABLE WITHOUT ID parents AS "Parents", partner AS "Partner", children AS "Children", siblings AS "Siblings", allies AS "Allies", enemies AS "Enemies"
WHERE file.path = this.file.path
```
| NPC | Relationship Type | Notes |
| :--- | :--- | :--- |
| Brakken Hammer-Fall (missing) | Master / indenture holder | Hogar cannot legally leave Ritterstadt without Brakken's release — a problem if Brakken doesn't return |
| [[Brunhilde Hammerschlag]] | Professional parallel | She is the full smith; he is the apprentice. He is slightly in awe of her and tries not to show it. |
| [[Ritter Konrad von Eisfeld]] | Authority figure | Konrad has not yet decided what to do about Brakken's absence or Hogar's legal status |

mermaid\n" + lines.join("\n") + "\n```");
```

## Inventory
```dataview
LIST FROM "50-Items" WHERE contains(this.items, file.link)
```

## Stat Block
```statblock
monster: Commoner
```
%% Suggested SRD block for a young apprentice. Adjust to taste. %%

## Appearances
- [[SP-GQ01-The-Gaolers-Link]]: made the Ashbox; forges the false Link; Scenes 03, 07

## Player Log
| Date (CY) | Party | Summary of Interaction |
| :--- | :--- | :--- |
| | | |

## Canon Notes

## Continuity

## GM Notes
> [!danger] DM Eyes Only
