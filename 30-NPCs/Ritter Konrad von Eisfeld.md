---
type: npc
status: alive
canon: false
faction: ''
location: '[[Ritterstadt]]'
aliases: [Ritter Konrad]
species: Human
heritage: ''
gender: Male
age: Elder
alignment: Lawful Neutral
occupation: Feudal Lord
class: ''
subclass: ''
prestige_class: ''
level: ''
adventure_role: ''
disposition: Neutral
party_trust: 0
items: []
connected_quests: ['[[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]]', '[[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]]']
connected_groups: []
parents: []
partner: []
children: []
siblings: []
allies: [Hauptmann Hildegard Stahlwulf, Vater Sigmund Wolfherz]
enemies: []
deceased_date: ''
tags: [Category/People, NPC, ritterstadt-npc]
publish: false
name: Ritter Konrad von Eisfeld
MyContainer: '[[The Ritter''s Hall]]'
MyCategory: null
image: Konrad_von_Eisfeld.png
obsidianUIMode: preview
NoteStatus: ❓
town_role: Governing Authority
shop: The Ritter's Hall
founder: true
---

# Ritter Konrad von Eisfeld

> A composed elder soldier who projects calm authority — and is quietly drowning in a debt he has told no one about.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
An older man with a soldier's bearing that age hasn't entirely taken from him. He wears fine clothes over chain mail when receiving guests, his longsword always at his hip. His face is weathered, his hands still strong. He holds eye contact slightly too long when something is worrying him.

## Personality & Mannerisms
Speaks in measured, deliberate sentences — never wastes words. Pauses before answering any question about money or the garrison. Makes direct eye contact, but it slips when the conversation nears the Consortium. Has a habit of glancing at the eastern timber line when he stands near a window.

## Goals & Secrets
### 💡 Key Motivation
Protect Ritterstadt's survival and the von Eisfeld name. He built this village with a loan he now cannot repay, and his greatest fear is that the hamlet falls apart on his watch.

### The Real Story
Three years ago, Konrad took a 700–800 gp loan from the **Hanselmann Consortium** — a Keoish merchant association based in Ungra Balan — to fund the garrison's initial establishment after a catastrophic raid destroyed the original palisade. The loan has been serviced through timber rights. The old-growth north of Ritterstadt is running short. The Consortium's patience is shorter still.

### What They Know (But Won't Say)
- The exact size of the debt and the current shortfall
- That Vethkar Graun is a Consortium field factor, sent to assess Ritterstadt's assets
- That he received Vethkar formally at The Ritter's Hall and answered his questions with extreme care — revealing nothing, but confirming nothing either
- That he has no viable plan and has been sitting alone with this for months

### What They Fear
That the hamlet — everything he built and everyone who trusted him — collapses because of a financial mistake he made before the walls were even finished. The shame of it is almost worse than the threat.

### How to Reveal It
If the party surfaces the debt crisis explicitly — via Vethkar's notes, Lotte's journal, or direct confrontation — Konrad will be furious for a long moment. Not at the party. At himself and at the situation. He dismisses them. Three days later he sends for them privately. He will say: *"I need to know what our options are."* From that point he is fully cooperative — but he needs to be led, not pushed.

## Role & Context
Konrad is the hamlet's feudal lord — the legal, military, and social authority of Ritterstadt. He commissions the garrison, approves contracts, and sets the tone for how the village presents itself to outsiders. Without him, the hamlet has no recognized authority and no organized defense.

## Conversation Guide
| Topic | Freely Discussed? | Notes / Sample Line |
| :--- | :---: | :--- |
| Village safety & threats | ✅ | Direct and candid about known dangers |
| The garrison | ⚠️ | Selective — speaks to strength, not strain |
| The Wachturm | ⚠️ | "Old stone. Older than us. Leave it." |
| His finances | ❌ | Deflects with composure. "The village manages." |
| Vethkar Graun | ❌ | Goes very quiet. "He was received formally." |
| Timber rights | ❌ | "A matter for the Vogt's office." |

### 🔑 Trust-Gated Information
- **Low Trust (stranger):** Formal and measured. Commissions the party clearly, pays promptly, asks no questions about methods. He's assessing them without showing it.
- **Medium Trust (regular):** Will speak candidly about village threats. Asks the party's opinion on what they've seen in the uplands. Begins to rely on them as an informal advisory capacity.
- **High Trust (friend / proven):** If the debt crisis is surfaced explicitly, he dismisses the party — then goes silent for three days. When he returns: "I need to know what our options are." He needs solutions, not judgment. Will work with the party if they bring him anything viable.

## Services
| Service | Cost / Notes |
| :--- | :--- |
| Quest commission (civic contracts) | Pays from personal funds; 10 gp/wolf ear in 0002 |
| Garrison access & coordination | Requires trust or Hildegard's endorsement |
| Village record access | Requires persuasion (DC 14) or established trust |
| Formal introductions to other officials | Available to any party he's assessed as capable |

## Quest Hooks
| Hook | Leads To | Trigger Condition |
| :--- | :--- | :--- |
| Livestock missing north of the village | [[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]] | Party arrives or asks about the north pass |
| "I received Vethkar formally. He asked about the road north." | [[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]] | Lotte tips off the party; Konrad confirms the visit |
| Hanselmann Consortium debt | [[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]] | Party surfaces it via Vethkar's notes or Lotte's journal |

## Relationships
```dataview
TABLE WITHOUT ID parents AS "Parents", partner AS "Partner", children AS "Children", siblings AS "Siblings", allies AS "Allies", enemies AS "Enemies"
WHERE file.path = this.file.path
```
| NPC | Relationship Type | Notes |
| :--- | :--- | :--- |
| [[Hauptmann Hildegard Stahlwulf]] | Trusted ally | She commands the garrison; he relies on her judgment completely |
| [[Vogt Ruprecht Ackermann]] | Nominal ally | Konrad doesn't know about Ruprecht's skimming |
| [[Vater Sigmund Wolfherz]] | Respectful distance | Trusts him as the village's moral compass |
| Hanselmann Consortium | Creditor (secret) | 700–800 gp outstanding; timber rights as collateral |

mermaid\n" + lines.join("\n") + "\n```");
```

## Inventory
```dataview
LIST FROM "50-Items" WHERE contains(this.items, file.link)
```

## Stat Block
```statblock
monster: Knight
```
%% Suggested SRD block for an elder feudal lord & soldier. Adjust to taste. %%

## Appearances
Sidebar Press adventures this NPC appears in:
- [[SP-GA03-The-Red-Cord]] — Scenes 1–6 (the noble; Temper and Trust tracks; swords or coin)

## Player Log
| Date (CY) | Party | Summary of Interaction |
| :--- | :--- | :--- |
| | | |

## Canon Notes

## Continuity

## GM Notes
> [!danger] DM Eyes Only
