---
publish: false
name: Vater Sigmund Wolfherz
MyContainer: "[[St. Erika's Chapel]]"
MyCategory:
image: Sigmund_Wolfherz.png
tags:
  - Category/People
  - NPC
  - ritterstadt-npc
obsidianUIMode: preview
aliases:
  - Vater Sigmund
NoteStatus: ❓
type: NPC
status: Alive
ancestry: Human
location: "[[Ritterstadt]]"
occupation: Village Priest & Healer
town_role: Spiritual Anchor & Lore-Keeper
alignment: Lawful Good
disposition: Friendly
shop: St. Erika's Chapel
founder: true
party_trust: 0
deceased_date:
char_alignment: Lawful Good
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
  - Ritter Konrad von Eisfeld
  - Hanz Korngut
  - Lotte Kesselring
Connected_Quests:
  - "[[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]]"
  - "[[Greyhawk University/04. Campaign Logs/Session Notes/0003 - The Stolen Grain]]"
  - "[[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]]"
Connected_Groups: []
---




> [!NOTE|div-m] Parent Location: `INPUT[inlineListSuggester(optionQuery(#Category/Hub),optionQuery(#Category/Region),optionQuery(#Category/Place),optionQuery(#Category/PointofInterest)):MyContainer]`
%% DISPLAYS NOTES THAT MATCH THE TAGS ABOVE %% 

> [!column|no-i no-t]
>> [!div-m|no-title]
>> ![[Sigmund_Wolfherz.png]]
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
A gentle elder with the patience of a man who has been waiting for the right moment to say something important — and is no longer certain it will ever come on its own.

### 📝 Appearance
An older man with careful, clean hands and simple robes. His quarterstaff is worn smooth from decades of use. A healer's kit is always at his side. His face is kind and unhurried. On clear mornings, he stands at his window and watches the Wachturm to the north.

### 🎭 Mannerisms
Speaks quietly and at length, rarely in a hurry. Does not ask direct questions — prefers to share something and wait for the response it draws. Goes very still when surprised; it's the only crack in his composure. Refers to Hassenrath by name occasionally, in passing, as if testing whether anyone recognizes it.

### 💡 Key Motivation
Keep Ritterstadt safe from a threat that most of its residents do not know exists. He has the knowledge to explain it. He has been waiting for someone worth explaining it to.

## 🗺️ Town Role & Function

Sigmund is the village's priest and healer — the spiritual and medical center of Ritterstadt. He buries the dead, heals the sick, settles disputes with quiet authority, and serves as the closest thing the hamlet has to a living institutional memory. Without him, the village loses its moral compass and its only trained healer.

### 🏪 Services

| Service | Cost / Notes |
| :--- | :--- |
| Healing (basic) | Free. He never charges. |
| Spiritual counsel | Free |
| Lore consultation (history, religion) | Free — but he gives what he judges you're ready for |
| Hassenrath's notes | Trust-gated. This is the Wachturm arc reveal. |

## 💬 Conversation Guide

| Topic | Freely Discussed? | Notes / Sample Line |
| :--- | :---: | :--- |
| Faith, healing, village welfare | ✅ | Open and warm |
| Village history (general) | ✅ | Shares freely, carefully |
| The east treeline shrine | ⚠️ | "Not every old thing is dangerous. Some were put here to protect." |
| The Wachturm | ⚠️ | "It is older than the church. Older than the land-grant. I have... notes." |
| Hassenrath | ⚠️ | Drops the name in passing. Waits to see if anyone reacts. |
| What's beneath the tower | ❌ | Not until the party has proven they'll do something useful with it |

### 🔑 Trust-Gated Information

- **Low Trust (stranger):** Heals freely. Shares village history without agenda. Gentle, open, nothing withheld that he judges them ready for.
- **Medium Trust (regular):** Mentions Hassenrath's name without explaining who he was. Notes that the tower has been "studied before." Asks quiet questions about what the party has seen in the uplands.
- **High Trust (friend / proven):** Shares Hassenrath's notes. This is the moment the campaign's central mystery becomes explicit. He will say: *"I have been waiting for someone to come along who would do something other than make it worse."*

## 🎯 Quest Hooks

| Hook | Leads To | Trigger Condition |
| :--- | :--- | :--- |
| Blesses a party member's weapon (quietly, unbidden) | Goodwill / relationship | Party spares the winter wolves in 0002 |
| Shares Hassenrath's notes | Wachturm Arc reveal | Party consults him about the east shrine in 0003 |
| Asks to meet privately after seeing Doss's research | Wachturm Arc escalation | Party obtains Vethkar's notes in 0004 and shows him |

## 🔗 Relationship Web

| NPC | Relationship Type | Notes |
| :--- | :--- | :--- |
| [[Ritter Konrad von Eisfeld]] | Respectful advisor | Konrad trusts his moral judgment; Sigmund is careful not to alarm him unnecessarily |
| [[Hanz Korngut]] | Quiet concern | Knows Hanz has been having strange dreams; hasn't told him why |
| The Erdgeist (east shrine) | Informed neutral | Knows it exists, considers it benign, does not want it disturbed |
| Hassenrath (deceased scholar) | Inherited custodian | Holds his notes; has built on his research privately |

# Statblock

```statblock
monster: Priest
```
%% Suggested SRD block for a village priest & healer. Adjust to taste. %%

# GM Notes

> [!danger] DM Eyes Only

## 🕵️ Secrets & Hidden Motivations

### The Real Story
Sigmund holds **Hassenrath's notes** — the research of a prior scholar who documented the Wachturm's binding function, the ward-panel system, and what the structure was built to contain. Sigmund has been building on these notes privately for years. He knows the ward-panels are degrading. He knows something beneath the tower is faintly stirring. He does not know what to do about it — and he has been waiting for capable people to arrive before he says anything.

### What They Know (But Won't Say)
- The full contents of Hassenrath's notes: the binding network, the six sites, the "do not open alone" warning at the Wachturm entry
- That the Erdgeist at the east shrine is connected to the tower's protective network and is currently agitated
- That Hanz Korngut's strange dreams are a symptom of the ward degradation
- That the ward-panels have been weakening for at least a generation and the timeline is accelerating

### What They Fear
That he waited too long to trust someone. That the thing beneath the tower stirs before anyone who can act is in position to do so. He is afraid of being wrong about the party — of giving the notes to people who will make things worse.

### How to Reveal It
The trigger is the east shrine investigation in **0003** — if the party consults Sigmund about the Erdgeist's agitation and its connection to the tower, he goes very quiet, then asks them to sit down. He shares Hassenrath's notes. He says: *"I have been waiting for someone to come along who would do something other than make it worse."*

A secondary trigger is **0004**: if the party shows him Varek Doss's research notes (obtained from Vethkar), he asks to meet privately. Doss's partial picture combined with Hassenrath's complete one gives him the first full understanding of the timeline. He will be frightened in the way quiet men are frightened — very still, very careful.

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
- [[SP-PBS-03-The-Red-Cord]] — Scene 1 (persuades Konrad to go; walks him to the Landing if he refuses)

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
