---
type: npc
status: alive
canon: false
faction: ''
location: '[[Ritterstadt]]'
aliases: [Bruni]
species: Human
heritage: ''
gender: Female
age: Adult
alignment: Neutral Good
occupation: Blacksmith
class: ''
subclass: ''
prestige_class: ''
level: ''
adventure_role: ''
disposition: Neutral
party_trust: 0
items: []
connected_quests: ['[[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]]']
connected_groups: []
parents: []
partner: ['[[Dietrich Hammerschlag]]']
children: []
siblings: []
allies: [Vater Sigmund Wolfherz, Ritter Konrad von Eisfeld]
enemies: []
deceased_date: ''
tags: [Category/People, NPC, ritterstadt-npc]
publish: false
name: Brunhilde Hammerschlag
MyContainer: '[[The Smithy]]'
MyCategory: null
image: Brunhilde_Hammerschlag.png
obsidianUIMode: preview
NoteStatus: ❓
town_role: Industrial / Metalwork
shop: Hammerschlag Forge
founder: false
---

# Brunhilde Hammerschlag

> A controlled, spare woman who took over the smithy when her husband died and has been holding the whole weight of that loss at arm's length ever since — waiting, without quite knowing it, for someone to hand her what was in that cave.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
A powerfully built adult human woman, work-hardened from years at the forge. Her hands are calloused to the point where she doesn't feel heat the way others do. She doesn't fidget. When she's thinking about Dietrich, her expression goes very still — not sad exactly, just very quiet.

## Personality & Mannerisms
Speaks in spare, controlled sentences. Asks precise questions and waits for precise answers. Her prices are fair and she doesn't haggle; that's the only warmth she extends until she's decided she trusts you. She will ask, exactly once, if you found anything in the cave. She will not explain why until she trusts you more.

## Goals & Secrets
### 💡 Key Motivation
Maintain the forge. Keep working. Understand — eventually, when the time is right — what actually happened to Dietrich in that pass. She is not ready to open the coffer. She is waiting for enough information to make opening it mean something rather than just be terrifying.

### The Real Story
Dietrich Hammerschlag did not simply die in a wolf attack three winters ago. He found the limestone cave above the snowline — the same cave that will become the winter wolves' den in Adventure 0002 — and inside it, an artifact that had been sitting in the inner chamber for an indeterminate period. He took it. The wolves found him on the way back, drawn by the artifact's effect (animals are sensitive to its emanation). He killed two before the pack brought him down. The artifact came home in an oilcloth wrap. Bruni put it in a coffer. She has never opened the coffer.

### What They Know (But Won't Say)
- The coffer is real. It's in the forge, behind the coal store. She checks it periodically to confirm it's still there.
- The shape of what's inside — from the oilcloth wrap — is consistent with a **bound node-key**: an interface piece for the Wachturm's relay network, one of the devices used to interact with a binding node's empty socket (the socket seen in Adventure 0001's inner sanctum). She does not know this. She only knows its shape.
- She does not open it because she is afraid of what opening it might mean about why Dietrich thought it was worth dying for.

### What They Fear
That the coffer contains something that explains how Dietrich died — and that understanding it will make his death feel real in a way she has been successfully preventing for three years. The coffer is grief management as much as it is practical restraint.

### How to Reveal It
The trigger is the empty oilcloth from the wolf cave's inner chamber. When the party shows it to her — or describes it — she will go very still. The shape matches exactly what she imagines is inside the coffer. She will thank them quietly and ask: "Did you find anything else?" This is the moment. If they handle it gently, she will tell them about the coffer. If they press without care, she closes the conversation entirely and it requires a future approach to reopen.

> [!warning] This is one of the most important early roleplay moments in the campaign. Do not rush it. Let the silence land.

## Role & Context
Bruni runs Dietrich's old forge — Ritterstadt's full-service smithy. She can do what Hogar cannot: weapons, armor, structural metalwork. She is the hamlet's industrial backbone for anything metal. Without her, the village cannot arm itself or maintain its infrastructure above the level of basic tool repair.

## Conversation Guide
| Topic | Freely Discussed? | Notes / Sample Line |
| :--- | :---: | :--- |
| Smithing, metalwork, commissions | ✅ | Direct and professional |
| Dietrich (general) | ⚠️ | Spare and controlled. "He died in the pass. Wolves. Three winters ago." |
| The cave / northern pass | ⚠️ | Asks once: "Did you find anything up there? Anything that might have been his?" Won't explain. |
| The coffer | ❌ | "That's not something I discuss." |
| Hogar / The Iron Anvil | ❌ | "The other forge. Not my concern." |
| Brakken's disappearance | ❌ | "I heard. I don't know what happened. Neither does anyone else." |

### 🔑 Trust-Gated Information
- **Low Trust (stranger):** Professional service. Fair prices. One question about the cave if they've come from the north.
- **Medium Trust (regular):** Will tell them Dietrich found something in that pass the night he died. She doesn't know what. She knows it came home with him. She has not opened the coffer. "I was waiting until I knew enough to understand what it meant."
- **High Trust (friend / proven):** Will describe the coffer and what she imagines is inside. Will ask for the party's help in understanding it before she opens it. This is a significant roleplay commitment — she's trusting them with the most guarded thing she has.

## Services
| Service | Cost / Notes |
| :--- | :--- |
| Weapon smithing | Full service; standard rates |
| Armor repair & fabrication | Full service |
| Tool work & general metalwork | Standard rates |
| **0002 Reward:** 50% off all smithing | For one month; if party tells her what they found in the cave |

## Quest Hooks
| Hook | Leads To | Trigger Condition |
| :--- | :--- | :--- |
| "Did you find anything up there? Anything that might have been his?" | [[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]] — Bruni's Coffer thread | Party returns from the wolf cave |
| The empty oilcloth matches the coffer's shape | Wachturm Arc (coffer contents) | Party shows her the oilcloth from the inner chamber |
| Party asks to help her open the coffer | Future arc (the node-key) | High trust; Bruni's Coffer thread fully activated |

## Relationships
```dataview
TABLE WITHOUT ID parents AS "Parents", partner AS "Partner", children AS "Children", siblings AS "Siblings", allies AS "Allies", enemies AS "Enemies"
WHERE file.path = this.file.path
```
| NPC | Relationship Type | Notes |
| :--- | :--- | :--- |
| [[Dietrich Hammerschlag]] | Husband | Died three winters ago in the northern pass; wolves, officially |
| [[Hogar Irongrip]] | Separate operation | Different forge, different master — she leaves him to his own situation |
| [[Vater Sigmund Wolfherz]] | Quiet respect | He was the one who told her about Dietrich; he checks on her |
| [[Ritter Konrad von Eisfeld]] | Professional relationship | He paid the garrison's smith rate; she kept the garrison's arms in order |

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
%% Suggested SRD block for a civilian smith. Adjust to taste. %%

## Appearances

## Player Log
| Date (CY) | Party | Summary of Interaction |
| :--- | :--- | :--- |
| | | |

## Canon Notes

## Continuity

## GM Notes
> [!danger] DM Eyes Only
