---
publish: false
name: Hanz Korngut
MyContainer: "[[The Mill]]"
MyCategory:
image: Hanz_Korngut.png
tags:
  - Category/People
  - NPC
  - ritterstadt-npc
obsidianUIMode: preview
aliases: []
NoteStatus: ❓
type: NPC
status: Alive
ancestry: Human
location: "[[Ritterstadt]]"
occupation: Miller
town_role: Agriculture & Local Lore-Keeper
alignment: Neutral Good
disposition: Neutral
shop: The Mill
founder: false
party_trust: 0
deceased_date:
char_alignment: Neutral Good
char_status: Alive
char_race: Human
char_gender: Male
char_age: Elder
char_items: []
parents: []
children: []
siblings: []
partner: []
enemies: []
allies:
  - Vater Sigmund Wolfherz
Connected_Quests:
  - "[[Greyhawk University/04. Campaign Logs/Session Notes/0003 - The Stolen Grain]]"
  - "[[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]]"
Connected_Groups: []
---




> [!NOTE|div-m] Parent Location: `INPUT[inlineListSuggester(optionQuery(#Category/Hub),optionQuery(#Category/Region),optionQuery(#Category/Place),optionQuery(#Category/PointofInterest)):MyContainer]`
%% DISPLAYS NOTES THAT MATCH THE TAGS ABOVE %% 

> [!column|no-i no-t]
>> [!div-m|no-title]
>> ![[Hanz_Korngut.png]]
>
>> [!div-m|no-title] Place Name
>> ~~~meta-bind
>> INPUT[select(
>> option(1, ℹ️General),
>> option(2, 📒Statblock),
>> option(3, 📝GM Notes),
>> class(tabbed)
>> )]
>> ~~~
>>>[!tabbed-box-maxh]
>>> >[!div-m|no-title]
>>> > ![[#General|no-h clean]]
>>>
>>> > [!div-m|no-title]
>>> > ![[#Statblock|no-h clean]]
>>> 
>>> > [!div-m|no-title]
>>> > ![[#GM Notes|no-h clean]]
>>> 

> [!NOTE|no-title]
> ~~~meta-bind
> INPUT[select(
> option(1, ⚔️Inventory),
> option(2, 🔗Connections),
> option(3, 🧑‍🤝‍🧑Relationships),
> class(tabbed)
> )]
> ~~~
> >[!tabbed-box]
> > >[!div-m|no-title]
> > > ![[#Inventory|no-h clean]]
> >
> > > [!div-m|no-title]
> > > ![[#Connections|no-h clean]]
> > 
> > > [!div-m|no-title]
> > > ![[#Relationships|no-h clean]]

---

# General

Name: `= this.file.name`

Alignment:  `INPUT[template-npc-alignment][:char_alignment]`

Status: `INPUT[template-person-status][:char_status]`

Race/Species: `INPUT[template-person-race][:char_race]`

Gender: `INPUT[template-person-gender][:char_gender]`

Age: `INPUT[template-person-age-range][:char_age]`

---

### Character Descriptor
A quiet miller who carries more uplands lore than most professors — and has been having strange dreams he doesn't mention to anyone.

### 📝 Appearance
An aging human male, always flour-dusted, with deeply calloused hands and a considering look that suggests he's heard more than he says. He moves slowly and deliberately, like a man who has spent decades working with heavy machinery that punishes carelessness.

### 🎭 Mannerisms
Slow to speak, careful when he does. Refers to old stories as plain facts. Will go quiet when asked about the east oak — not from evasion, but from not knowing how to explain it in modern terms. His grandmother's name comes up unprompted when the conversation touches the right things.

### 💡 Key Motivation
Keep the mill running, keep the village fed, and stay out of whatever trouble he can feel building in the uplands. He knows more than he lets on and is not sure what to do with what he knows.

## 🗺️ Town Role & Function

Hanz operates **Die Mühle am Bach** — the village's only mill. Without him, Ritterstadt cannot process its grain surplus. He is also, quietly, the settlement's most reliable repository of uplands folklore and old Flan-adjacent family memory. He won't volunteer this; it comes out in conversation.

### 🏪 Services

| Service | Cost / Notes |
| :--- | :--- |
| Grain milling | Standard village rate |
| Ledger review (harvest records) | Available; DC 11 Investigation reveals two separate irregularities |
| Uplands lore | Trust-gated; shares one piece freely after the party earns his respect |

## 💬 Conversation Guide

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

## 🎯 Quest Hooks

| Hook | Leads To | Trigger Condition |
| :--- | :--- | :--- |
| Ledger discrepancy (Beckenhaus grain withdrawals) | [[Greyhawk University/04. Campaign Logs/Session Notes/0003 - The Stolen Grain]] | Party or Vogt reviews the mill ledger |
| Ledger discrepancy (Ruprecht's tax skimming) | [[Greyhawk University/04. Campaign Logs/Session Notes/0003 - The Stolen Grain]] — Vogt subplot | DC 16 Investigation on the same ledger |
| "He asked about the tower specifically." (Vethkar) | [[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]] | Vethkar questions Hanz; Hanz tells the party immediately after |
| Uplands lore (one piece, freely given) | World-building / arc setup | After any quest where party returns and shares what they found |

## 🔗 Relationship Web

| NPC | Relationship Type | Notes |
| :--- | :--- | :--- |
| [[Vogt Ruprecht Ackermann]] | Uneasy authority | Ruprecht oversees his ledger; Hanz is careful around him |
| [[Vater Sigmund Wolfherz]] | Quiet respect | Sigmund knows about Hanz's grandmother's line; neither has said it directly |
| Kurt Beckenhaus | Supplier / community member | Knows about the grain withdrawals; has not reported them |

# Statblock

```statblock
monster: Commoner
```
%% Suggested SRD block for an elder miller. Adjust to taste. %%

# GM Notes

> [!danger] DM Eyes Only

## 🕵️ Secrets & Hidden Motivations

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

# Inventory

The following items belong to `= this.file.name`.

```dataviewjs
// 1. Get the list of items and strip brackets from links if they exist
let rawItems = dv.current().char_items;

if (rawItems && rawItems.length > 0) {
    // Convert links to plain text names for comparison
    let charItemNames = rawItems.map(item => {
        return (typeof item === 'string') ? item.replace(/[\[\]]/g, "") : item.path.split('/').pop().replace(".md", "");
    });

    // 2. Query the Items folder and filter for matches
    let items = dv.pages('"3-Mechanics/Items"')
        .where(p => charItemNames.includes(p.file.name));

    // 3. Render the table
    dv.table(
        ["Item", "Cost", "Weight"],
        items.map(p => [
            p.file.link, 
            p.cost ?? "—", 
            p.weight ?? "—"
        ])
    );
} else {
    dv.paragraph("*No items currently equipped.*");
}
```

# Connections
Is the person linked to any groups or quests?

Quests: `INPUT[inlineListSuggester(optionQuery(#Category/Quest)):Connected_Quests]`
%% DISPLAYS NOTES THAT MATCH THE TAGS ABOVE %% 

Groups: `INPUT[inlineListSuggester(optionQuery(#Category/Group)):Connected_Groups]`
%% DISPLAYS NOTES THAT MATCH THE TAGS ABOVE %% 

# Relationships

List important relationships here. 

```dataviewjs
var parents = dv.current().parents ?? [];
var children = dv.current().children ?? [];
var enemies = dv.current().enemies ?? [];
var allies = dv.current().allies ?? [];
var siblings = dv.current().siblings ?? [];
var current = dv.current().file.name;
var partner = dv.current().partner ?? [];

// Normalize: Dataview Link objects and [[wikilink]] strings -> plain display text
const norm = (v) => {
  if (v && v.path) return (v.display ?? v.path.split("/").pop().replace(/\.md$/, ""));
  return String(v).replace(/\[\[([^\]|]+)\|?([^\]]*)\]\]/g, (m, t, d) => d || t);
};
// Quote labels so parentheses, commas, etc. don't break Mermaid
const esc = (s) => `"${norm(s).replace(/"/g, "'")}"`;

let lines = ["flowchart LR", `Current[${esc(current)}]`];
let linked = ["Current"];

const groups = [
  ["Parents",  "P",  parents],
  ["Partner",  "PT", partner],
  ["Children", "C",  children],
  ["Siblings", "S",  siblings],
  ["Enemies",  "E",  enemies],
  ["Allies",   "A",  allies],
];

for (const [label, id, list] of groups) {
  if (!list.length) continue;
  if (id === "P") {
    // Parents point at Current directly (no group node)
    list.forEach((p, i) => {
      lines.push(`P${i + 1}[${esc(p)}]:::internal-link`, `P${i + 1} --> Current`);
      linked.push(`P${i + 1}`);
    });
  } else {
    lines.push(`${id}[${label}]`, `Current --> ${id}`);
    list.forEach((p, i) => {
      lines.push(`${id}${i + 1}[${esc(p)}]:::internal-link`, `${id} --> ${id}${i + 1}`);
      linked.push(`${id}${i + 1}`);
    });
  }
}

lines.push(`class ${linked.join(",")} internal-link;`);
dv.paragraph("```mermaid\n" + lines.join("\n") + "\n```");
```
%% CODE ABOVE CREATED WITH CHAT-GPT. ITS COMPLEX CODE THAT SHOULD NOT BE CHANGED UNLESS YOU KNOW WHAT YOU ARE DOING %%
%% MERMAID-FIX-TEXT-CLIPPING.CSS is enabled in Settings > Appearance > CSS Snippets. This fixes text clipping and styles the boxes %%

> [!NOTE]- Relationship Config - Enter name of People Notes
> `BUTTON[button_person]` Nodes will link to notes of the same name. 
> 
> | Parents    | Partner    | Children |
> | --- | --- | --- |
> | `INPUT[list:parents]`    | `INPUT[list:partner]`    | `INPUT[list:children]`  |
> 
> | Siblings    | Enemies    | Allies |
> | --- | --- | --- |
> | `INPUT[list:siblings]`    | `INPUT[list:enemies]`    | `INPUT[list:allies]`  |

# Player Log

| Date (CY) | Party | Summary of Interaction |
| :--- | :--- | :--- |
| | | |
