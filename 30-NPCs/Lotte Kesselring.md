---
type: npc
status: alive
canon: false
faction: ''
location: '[[Ritterstadt]]'
aliases: [The Grey Wolf Innkeeper]
species: Human
heritage: ''
gender: Female
age: Adult
alignment: Neutral Good
occupation: Innkeeper
class: ''
subclass: ''
prestige_class: ''
level: ''
adventure_role: ''
disposition: Friendly
party_trust: 0
items: []
connected_quests: ['[[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]]']
connected_groups: []
parents: []
partner: []
children: []
siblings: []
allies: [Vater Sigmund Wolfherz, Ritter Konrad von Eisfeld]
enemies: []
deceased_date: ''
tags: [Category/People, NPC, ritterstadt-npc]
publish: false
name: Lotte Kesselring
MyContainer: '[[The Grey Wolf]]'
MyCategory: null
image: Lotte_Kesselring.png
obsidianUIMode: preview
NoteStatus: ❓
town_role: Social Hub & Intelligence Node
shop: The Grey Wolf
founder: false
---

# Lotte Kesselring

> A sharp-eyed innkeeper who has run the Grey Wolf for twelve years and knows exactly what every silence in this village means.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Adult human female, practical working clothes, always moving — never idle behind the bar. Hair pinned back efficiently. Her dog, **Grauer**, follows her like a shadow and is a more reliable gauge of her opinion of someone than anything she'll say.

## Personality & Mannerisms
Asks exactly one apparently-innocent question per new arrival that reveals background research — she already knows more about them than she lets on. Refills drinks without being asked when she wants someone to keep talking. When something genuinely worries her, she goes still behind the bar. Grauer sitting near a patron is the clearest sign she trusts them.

## Goals & Secrets
### 💡 Key Motivation
Protect the specific community of people she has spent twelve years building her life around. She has no illusions about the world, but she has deep investment in this corner of it.

### The Real Story
Lotte's private journal is twelve years of careful observation — every major family, every unusual visitor, every financial irregularity she's overheard, every story that didn't quite add up. It is low-grade intelligence of remarkable depth. She has never shared it with anyone because no one has yet seemed like the right person to share it with.

### What They Know (But Won't Say)
- Ruprecht Ackermann accepted something from Vethkar (almost certainly money) and has said nothing about it to anyone — she saw the exchange from behind the bar
- She has noted systematic patterns in who visits the village when, including a recurring contact of Ewald's that she has not been able to identify
- She knows Konrad is under financial strain from the way he answered Vethkar's questions — she knows this man, and that was not his composed face

### What They Fear
That Ritterstadt gets quietly dismantled — not attacked, but *purchased* or *managed* into something unrecognizable — by external interests before anyone organized enough to stop it is paying attention. She has been paying attention for twelve years. She has been waiting for someone else to start.

### How to Reveal It
Two or more genuine conversations (not purely transactional) earn voluntary access to the journal. A DC 15 Persuasion to ask directly. The key is that she responds to people who are *actually interested in the village* — not just their next contract. If the party demonstrates that they care about what happens to Ritterstadt specifically, she opens up.

## Role & Context
The Grey Wolf is where Ritterstadt's social life happens. Lotte is the center of that network — she hears everything, remembers everything, and has been keeping careful notes for twelve years. She is the party's primary social contact in the hamlet, the person most likely to know what's wrong before anyone official does.

## Conversation Guide
| Topic | Freely Discussed? | Notes / Sample Line |
| :--- | :---: | :--- |
| Village gossip (general) | ✅ | Shares selectively — always with a purpose |
| New arrivals | ✅ | Forthcoming once she's decided to trust the party |
| Vethkar Graun | ✅ | "He is pleasant. That is what worries me." |
| Konrad / the garrison | ⚠️ | Respectful; won't speculate on his finances |
| The Wachturm | ⚠️ | "Old stone. I've never asked questions about old stone." |
| Her journal | ❌ | Not until she's decided the party deserves it |
| Ruprecht's conduct | ❌ | She has noticed things. She will not say them without trust. |

### 🔑 Trust-Gated Information
- **Low Trust (stranger):** Room, board, and what's common knowledge. Watches. Assesses. Grauer stays near her.
- **Medium Trust (regular):** Shares observations about recent unusual behavior — strangers asking pointed questions, soldiers acting strangely, a farmer on an unusual schedule. Grauer comes to the table.
- **High Trust (friend / proven):** Shares her journal. In the resolution of 0004, she shows the party three specific pages she judges they need most — her choice, not theirs. Becomes an ongoing intelligence asset. Will say: *"I've been keeping this for twelve years. I think it's time someone else knew what I know."*

## Services
| Service | Cost / Notes |
| :--- | :--- |
| Room & board | Standard rates |
| Meals | Hot food always available; she sets the table for the party without asking |
| Information (general) | Free — but she decides what to share and when |
| Her private journal | Trust-gated. Not for sale. |

## Quest Hooks
| Hook | Leads To | Trigger Condition |
| :--- | :--- | :--- |
| "Someone needs to find out what this man is doing here — carefully." | [[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]] | Vethkar Graun arrives; Lotte flags him within 24 hours |
| "Ruprecht accepted something from the southerner. I saw it. He hasn't mentioned it to anyone." | [[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]] | High trust; she shares this as additional leverage |

## Relationships
```dataview
TABLE WITHOUT ID parents AS "Parents", partner AS "Partner", children AS "Children", siblings AS "Siblings", allies AS "Allies", enemies AS "Enemies"
WHERE file.path = this.file.path
```
| NPC | Relationship Type | Notes |
| :--- | :--- | :--- |
| [[Ritter Konrad von Eisfeld]] | Respectful distance | She respects him; would not act against him without cause |
| [[Vogt Ruprecht Ackermann]] | Quiet suspicion | Has noticed discrepancies in his behavior; holds her tongue |
| [[Vater Sigmund Wolfherz]] | Warm respect | The two understand each other without much needing to be said |
| Grauer (her dog) | Companion / trust indicator | His behavior around the party is a reliable signal of her opinion |
| Vethkar Graun | Subject of concern | Watching him carefully; flagged him as a threat within hours of arrival |

mermaid\n" + lines.join("\n") + "\n```");
```

## Inventory
```dataview
LIST FROM "50-Items" WHERE contains(this.items, file.link)
```

## Stat Block
```statblock
monster: Spy
```
%% Suggested SRD block for a watchful innkeeper-informant. Adjust to taste. %%

## Appearances

## Player Log
| Date (CY) | Party | Summary of Interaction |
| :--- | :--- | :--- |
| | | |

## Canon Notes

## Continuity

## GM Notes
> [!danger] DM Eyes Only
