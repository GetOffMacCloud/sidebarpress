---
type: npc
status: alive
canon: false
faction: ''
location: '[[Ritterstadt]]'
aliases: []
species: Human
heritage: ''
gender: Male
age: Elder
alignment: Neutral Good
occupation: Miller
class: ''
subclass: ''
prestige_class: ''
level: ''
adventure_role: ''
disposition: Neutral
party_trust: 0
items: []
connected_quests: ['[[Greyhawk University/04. Campaign Logs/Session Notes/0003 - The Stolen Grain]]', '[[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]]']
connected_groups: []
parents: []
partner: []
children: []
siblings: []
allies: [Vater Sigmund Wolfherz]
enemies: []
deceased_date: ''
tags: [Category/People, NPC, ritterstadt-npc]
publish: false
name: Hanz Korngut
MyContainer: '[[The Mill]]'
MyCategory: null
image: Hanz_Korngut.png
obsidianUIMode: preview
NoteStatus: ❓
town_role: Agriculture & Local Lore-Keeper
shop: The Mill
founder: false
---

# Hanz Korngut

> A quiet miller who carries more uplands lore than most professors — and has been having strange dreams he doesn't mention to anyone.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
An aging human male, always flour-dusted, with deeply calloused hands and a considering look that suggests he's heard more than he says. He moves slowly and deliberately, like a man who has spent decades working with heavy machinery that punishes carelessness.

## Personality & Mannerisms
Slow to speak, careful when he does. Refers to old stories as plain facts. Will go quiet when asked about the east oak — not from evasion, but from not knowing how to explain it in modern terms. His grandmother's name comes up unprompted when the conversation touches the right things.

## Goals & Secrets
### 💡 Key Motivation
Keep the mill running, keep the village fed, and stay out of whatever trouble he can feel building in the uplands. He knows more than he lets on and is not sure what to do with what he knows.

### The Real Story
Hanz's grandmother was from an old Flan-adjacent family line — the same bloodline responsible for tending the east treeline shrine for generations. She never explained it that way; she just told him not to cut the old oak, not to move the stones, and that the Warden in the Green was older than the village and was there for a reason. Hanz has honored this without fully understanding it.

His strange dreams are a direct symptom of the Wachturm's ward degradation. The binding network is failing, and people with old Flan bloodline sensitivity feel it first — in sleep, as cold imagery of stone and stillness and pressure.

### What They Know (But Won't Say)
- He knows the Beckenhaus grain withdrawals are real and has not reported them because he suspects the reason and finds himself unable to condemn a father trying to save his daughter
- He has also noted Ruprecht's systematic skimming in the tax column of the same ledger, which he has absolutely not reported, because he doesn't know what would happen to him if he did
- His dreams have been getting worse over the past several months — more frequent, more vivid

### What They Fear
The quiet destruction of the things his grandmother told him to protect — not through malice, but through ignorance. He is afraid the party will pull the wrong thread and collapse something that has been holding for centuries.

### How to Reveal It
The dream revelation requires high trust and a conversation that touches on the Wachturm or the uplands directly. He won't volunteer it. If the party mentions unusual animal behavior near the tower, or the east shrine, or if they've talked to Sigmund — any of these opens the door. He will look at them for a moment before speaking, as if deciding something. Then: *"I think the dreams started around the same time the animals near the north tower started acting strange. I've not told anyone that."*

## Role & Context
Hanz operates **Die Mühle am Bach** — the village's only mill. Without him, Ritterstadt cannot process its grain surplus. He is also, quietly, the settlement's most reliable repository of uplands folklore and old Flan-adjacent family memory. He won't volunteer this; it comes out in conversation.

## Conversation Guide
| Topic | Freely Discussed? | Notes / Sample Line |
| :--- | :---: | :--- |
| Mill operations, grain, harvest | ✅ | Will talk about this at length |
| The uplands (general) | ✅ | Shares lore naturally in conversation |
| The east oak / forest spirit | ⚠️ | "My grandmother called it 'Wächter im Grünen' — the Warden in the Green. She said it was older than us. She was right." (won't elaborate unprompted) |
| His ledger | ⚠️ | Will confirm the Beckenhaus withdrawals if asked directly; will not name Kurt unprompted |
| His dreams | ❌ | "Nothing worth mentioning." |
| Vethkar Graun | ✅ (once flagged) | "He asked about the tower specifically. Its age. Its construction. I told him nothing. I thought you should know." |

### 🔑 Trust-Gated Information
- **Low Trust (stranger):** Mills grain, discusses weather and harvest yields. Courteous but not forthcoming.
- **Medium Trust (regular):** Shares uplands lore freely. Will confirm ledger discrepancies if questioned. Opens up about the old Flan family names in the village, his grandmother's stories.
- **High Trust (friend / proven):** Will tell the party about his dreams — cold stone, pale light, something held very still under great pressure. He doesn't understand them. He will say, quietly: *"I think the dreams started around the same time the animals near the north tower started acting strange."* This is a significant lore moment.

## Services
| Service | Cost / Notes |
| :--- | :--- |
| Grain milling | Standard village rate |
| Ledger review (harvest records) | Available; DC 11 Investigation reveals two separate irregularities |
| Uplands lore | Trust-gated; shares one piece freely after the party earns his respect |

## Quest Hooks
| Hook | Leads To | Trigger Condition |
| :--- | :--- | :--- |
| Ledger discrepancy (Beckenhaus grain withdrawals) | [[Greyhawk University/04. Campaign Logs/Session Notes/0003 - The Stolen Grain]] | Party or Vogt reviews the mill ledger |
| Ledger discrepancy (Ruprecht's tax skimming) | [[Greyhawk University/04. Campaign Logs/Session Notes/0003 - The Stolen Grain]] — Vogt subplot | DC 16 Investigation on the same ledger |
| "He asked about the tower specifically." (Vethkar) | [[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]] | Vethkar questions Hanz; Hanz tells the party immediately after |
| Uplands lore (one piece, freely given) | World-building / arc setup | After any quest where party returns and shares what they found |

## Relationships
```dataview
TABLE WITHOUT ID parents AS "Parents", partner AS "Partner", children AS "Children", siblings AS "Siblings", allies AS "Allies", enemies AS "Enemies"
WHERE file.path = this.file.path
```
| NPC | Relationship Type | Notes |
| :--- | :--- | :--- |
| [[Vogt Ruprecht Ackermann]] | Uneasy authority | Ruprecht oversees his ledger; Hanz is careful around him |
| [[Vater Sigmund Wolfherz]] | Quiet respect | Sigmund knows about Hanz's grandmother's line; neither has said it directly |
| Kurt Beckenhaus | Supplier / community member | Knows about the grain withdrawals; has not reported them |

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
%% Suggested SRD block for an elder miller. Adjust to taste. %%

## Appearances

## Player Log
| Date (CY) | Party | Summary of Interaction |
| :--- | :--- | :--- |
| | | |

## Canon Notes

## Continuity

## GM Notes
> [!danger] DM Eyes Only
