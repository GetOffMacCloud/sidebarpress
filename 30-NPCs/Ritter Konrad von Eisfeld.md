---
publish: false
name: Ritter Konrad von Eisfeld
MyContainer: "[[The Ritter's Hall]]"
MyCategory:
image: Konrad_von_Eisfeld.png
tags:
  - Category/People
  - NPC
  - ritterstadt-npc
obsidianUIMode: preview
aliases:
  - Ritter Konrad
NoteStatus: ❓
type: NPC
status: Alive
ancestry: Human
location: "[[Ritterstadt]]"
occupation: Feudal Lord
town_role: Governing Authority
alignment: Lawful Neutral
disposition: Neutral
shop: The Ritter's Hall
founder: true
party_trust: 0
deceased_date:
char_alignment: Lawful Neutral
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
  - Hauptmann Hildegard Stahlwulf
  - Vater Sigmund Wolfherz
Connected_Quests:
  - "[[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]]"
  - "[[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]]"
Connected_Groups: []
---




> [!NOTE|div-m] Parent Location: `INPUT[inlineListSuggester(optionQuery(#Category/Hub),optionQuery(#Category/Region),optionQuery(#Category/Place),optionQuery(#Category/PointofInterest)):MyContainer]`
%% DISPLAYS NOTES THAT MATCH THE TAGS ABOVE %% 

> [!column|no-i no-t]
>> [!div-m|no-title]
>> ![[Konrad_von_Eisfeld.png]]
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
A composed elder soldier who projects calm authority — and is quietly drowning in a debt he has told no one about.

### 📝 Appearance
An older man with a soldier's bearing that age hasn't entirely taken from him. He wears fine clothes over chain mail when receiving guests, his longsword always at his hip. His face is weathered, his hands still strong. He holds eye contact slightly too long when something is worrying him.

### 🎭 Mannerisms
Speaks in measured, deliberate sentences — never wastes words. Pauses before answering any question about money or the garrison. Makes direct eye contact, but it slips when the conversation nears the Consortium. Has a habit of glancing at the eastern timber line when he stands near a window.

### 💡 Key Motivation
Protect Ritterstadt's survival and the von Eisfeld name. He built this village with a loan he now cannot repay, and his greatest fear is that the hamlet falls apart on his watch.

## 🗺️ Town Role & Function

Konrad is the hamlet's feudal lord — the legal, military, and social authority of Ritterstadt. He commissions the garrison, approves contracts, and sets the tone for how the village presents itself to outsiders. Without him, the hamlet has no recognized authority and no organized defense.

### 🏪 Services

| Service | Cost / Notes |
| :--- | :--- |
| Quest commission (civic contracts) | Pays from personal funds; 10 gp/wolf ear in 0002 |
| Garrison access & coordination | Requires trust or Hildegard's endorsement |
| Village record access | Requires persuasion (DC 14) or established trust |
| Formal introductions to other officials | Available to any party he's assessed as capable |

## 💬 Conversation Guide

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

## 🎯 Quest Hooks

| Hook | Leads To | Trigger Condition |
| :--- | :--- | :--- |
| Livestock missing north of the village | [[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]] | Party arrives or asks about the north pass |
| "I received Vethkar formally. He asked about the road north." | [[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]] | Lotte tips off the party; Konrad confirms the visit |
| Hanselmann Consortium debt | [[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]] | Party surfaces it via Vethkar's notes or Lotte's journal |

## 🔗 Relationship Web

| NPC | Relationship Type | Notes |
| :--- | :--- | :--- |
| [[Hauptmann Hildegard Stahlwulf]] | Trusted ally | She commands the garrison; he relies on her judgment completely |
| [[Vogt Ruprecht Ackermann]] | Nominal ally | Konrad doesn't know about Ruprecht's skimming |
| [[Vater Sigmund Wolfherz]] | Respectful distance | Trusts him as the village's moral compass |
| Hanselmann Consortium | Creditor (secret) | 700–800 gp outstanding; timber rights as collateral |

# Statblock

```statblock
monster: Knight
```
%% Suggested SRD block for an elder feudal lord & soldier. Adjust to taste. %%

# GM Notes

> [!danger] DM Eyes Only

## 🕵️ Secrets & Hidden Motivations

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

## Appearances
Sidebar Press adventures this NPC appears in:
- [[SP-PBS-03-The-Red-Cord]] — Scenes 1–6 (the noble; Temper and Trust tracks; swords or coin)

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
