---
publish: false
name: Hogar Irongrip
MyContainer: "[[The Iron Anvil]]"
MyCategory:
image: Hogar_Irongrip.png
tags:
  - Category/People
  - NPC
  - ritterstadt-npc
obsidianUIMode: preview
aliases: []
NoteStatus: ❓
type: NPC
status: Alive
ancestry: Mountain Dwarf
location: "[[Ritterstadt]]"
occupation: Blacksmith Apprentice (Acting)
town_role: Industrial / Basic Metalwork
alignment: Neutral
disposition: Neutral
shop: The Iron Anvil
founder: false
party_trust: 0
deceased_date:
char_alignment: Neutral
char_status: Alive
char_race: Mountain Dwarf
char_gender: Male
char_age: Adult
char_items: []
parents: []
children: []
siblings: []
partner: []
enemies: []
allies:
  - Brunhilde Hammerschlag
Connected_Quests: []
Connected_Groups: []
---




> [!NOTE|div-m] Parent Location: `INPUT[inlineListSuggester(optionQuery(#Category/Hub),optionQuery(#Category/Region),optionQuery(#Category/Place),optionQuery(#Category/PointofInterest)):MyContainer]`
%% DISPLAYS NOTES THAT MATCH THE TAGS ABOVE %% 

> [!column|no-i no-t]
>> [!div-m|no-title]
>> ![[Hogar_Irongrip.png]]
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
A soot-streaked dwarf with wide, panicked eyes and hands that tremble slightly when he isn't holding a hammer — a young apprentice thrust into a master's role he wasn't ready for, trying very hard not to show it.

### 📝 Appearance
A young mountain dwarf with a thin, poorly-braided beard. His leather apron is several sizes too large — it belonged to his missing master, Brakken Hammer-Fall. His hands are steadier when he's working than when he isn't. He smells of coal and iron and something that might be anxiety.

### 🎭 Mannerisms
Mumbles the steps of smithing out loud to remember them ("heat to orange, not yellow — Brakken said orange"). Frequently glances toward the dark corners of the forge, as if expecting something to emerge. Quotes Brakken like scripture. Flinches at sudden sounds after dark.

### 💡 Key Motivation
Keep the forge fires burning until Brakken comes back. Or prove he can handle the heat if Brakken doesn't. He hasn't decided yet which of those things he's actually preparing for.

## 🗺️ Town Role & Function

Hogar is currently the only person operating The Iron Anvil. He is the hamlet's source of basic tool repair, edge sharpening, and simple metalwork. He cannot forge weapons or plate armor without supervision. If he fails — if the forge goes cold — Ritterstadt loses its only accessible metalwork service until a replacement is found or Brakken returns.

### 🏪 Services

| Service | Cost / Notes |
| :--- | :--- |
| Tool repair & sharpening | Standard rate; he's competent at this |
| Basic implement fabrication | Nails, brackets, hinges — manageable |
| Edge sharpening (weapons) | He can do this; he just won't say so confidently |
| Weapon or armor fabrication | ❌ — not without supervision; he will refuse or produce inferior work |

## 💬 Conversation Guide

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

## 🎯 Quest Hooks

| Hook | Leads To | Trigger Condition |
| :--- | :--- | :--- |
| "Brakken was taken in the night. I don't know by what." | Future arc: Brakken's disappearance | Party asks about the missing master at any point |
| The forge going cold / Hogar asking for help | Future arc: the Iron Anvil's survival | If the party doesn't intervene, quality of services degrades over time |
| Materials recovered in the field | Artisan growth system | Party brings Hogar rare metals or materials from uplands expeditions |

## 🔗 Relationship Web

| NPC | Relationship Type | Notes |
| :--- | :--- | :--- |
| Brakken Hammer-Fall (missing) | Master / indenture holder | Hogar cannot legally leave Ritterstadt without Brakken's release — a problem if Brakken doesn't return |
| [[Brunhilde Hammerschlag]] | Professional parallel | She is the full smith; he is the apprentice. He is slightly in awe of her and tries not to show it. |
| [[Ritter Konrad von Eisfeld]] | Authority figure | Konrad has not yet decided what to do about Brakken's absence or Hogar's legal status |

# Statblock

```statblock
monster: Commoner
```
%% Suggested SRD block for a young apprentice. Adjust to taste. %%

# GM Notes

> [!danger] DM Eyes Only

## 🕵️ Secrets & Hidden Motivations

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
