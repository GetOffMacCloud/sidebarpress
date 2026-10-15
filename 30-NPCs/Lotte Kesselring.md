---
publish: false
name: Lotte Kesselring
MyContainer: "[[The Grey Wolf]]"
MyCategory:
image: Lotte_Kesselring.png
tags:
  - Category/People
  - NPC
  - ritterstadt-npc
obsidianUIMode: preview
aliases:
  - The Grey Wolf Innkeeper
NoteStatus: ❓
type: NPC
status: Alive
ancestry: Human
location: "[[Ritterstadt]]"
occupation: Innkeeper
town_role: Social Hub & Intelligence Node
alignment: Neutral Good
disposition: Friendly
shop: The Grey Wolf
founder: false
party_trust: 0
deceased_date:
char_alignment: Neutral Good
char_status: Alive
char_race: Human
char_gender: Female
char_age: Adult
char_items: []
parents: []
children: []
siblings: []
partner: []
enemies: []
allies:
  - Vater Sigmund Wolfherz
  - Ritter Konrad von Eisfeld
Connected_Quests:
  - "[[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]]"
Connected_Groups: []
---




> [!NOTE|div-m] Parent Location: `INPUT[inlineListSuggester(optionQuery(#Category/Hub),optionQuery(#Category/Region),optionQuery(#Category/Place),optionQuery(#Category/PointofInterest)):MyContainer]`
%% DISPLAYS NOTES THAT MATCH THE TAGS ABOVE %% 

> [!column|no-i no-t]
>> [!div-m|no-title]
>> ![[Lotte_Kesselring.png]]
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
A sharp-eyed innkeeper who has run the Grey Wolf for twelve years and knows exactly what every silence in this village means.

### 📝 Appearance
Adult human female, practical working clothes, always moving — never idle behind the bar. Hair pinned back efficiently. Her dog, **Grauer**, follows her like a shadow and is a more reliable gauge of her opinion of someone than anything she'll say.

### 🎭 Mannerisms
Asks exactly one apparently-innocent question per new arrival that reveals background research — she already knows more about them than she lets on. Refills drinks without being asked when she wants someone to keep talking. When something genuinely worries her, she goes still behind the bar. Grauer sitting near a patron is the clearest sign she trusts them.

### 💡 Key Motivation
Protect the specific community of people she has spent twelve years building her life around. She has no illusions about the world, but she has deep investment in this corner of it.

## 🗺️ Town Role & Function

The Grey Wolf is where Ritterstadt's social life happens. Lotte is the center of that network — she hears everything, remembers everything, and has been keeping careful notes for twelve years. She is the party's primary social contact in the hamlet, the person most likely to know what's wrong before anyone official does.

### 🏪 Services

| Service | Cost / Notes |
| :--- | :--- |
| Room & board | Standard rates |
| Meals | Hot food always available; she sets the table for the party without asking |
| Information (general) | Free — but she decides what to share and when |
| Her private journal | Trust-gated. Not for sale. |

## 💬 Conversation Guide

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

## 🎯 Quest Hooks

| Hook | Leads To | Trigger Condition |
| :--- | :--- | :--- |
| "Someone needs to find out what this man is doing here — carefully." | [[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]] | Vethkar Graun arrives; Lotte flags him within 24 hours |
| "Ruprecht accepted something from the southerner. I saw it. He hasn't mentioned it to anyone." | [[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]] | High trust; she shares this as additional leverage |

## 🔗 Relationship Web

| NPC | Relationship Type | Notes |
| :--- | :--- | :--- |
| [[Ritter Konrad von Eisfeld]] | Respectful distance | She respects him; would not act against him without cause |
| [[Vogt Ruprecht Ackermann]] | Quiet suspicion | Has noticed discrepancies in his behavior; holds her tongue |
| [[Vater Sigmund Wolfherz]] | Warm respect | The two understand each other without much needing to be said |
| Grauer (her dog) | Companion / trust indicator | His behavior around the party is a reliable signal of her opinion |
| Vethkar Graun | Subject of concern | Watching him carefully; flagged him as a threat within hours of arrival |

# Statblock

```statblock
monster: Spy
```
%% Suggested SRD block for a watchful innkeeper-informant. Adjust to taste. %%

# GM Notes

> [!danger] DM Eyes Only

## 🕵️ Secrets & Hidden Motivations

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
