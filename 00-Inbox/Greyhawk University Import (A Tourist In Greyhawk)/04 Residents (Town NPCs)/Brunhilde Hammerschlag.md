---
publish: false
name: Brunhilde Hammerschlag
MyContainer: "[[The Smithy]]"
MyCategory:
image: Brunhilde_Hammerschlag.png
tags:
  - Category/People
  - NPC
  - ritterstadt-npc
obsidianUIMode: preview
aliases:
  - Bruni
NoteStatus: ❓
type: NPC
status: Alive
ancestry: Human
location: "[[Ritterstadt]]"
occupation: Blacksmith
town_role: Industrial / Metalwork
alignment: Neutral Good
disposition: Neutral
shop: Hammerschlag Forge
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
partner:
  - "[[Dietrich Hammerschlag]]"
enemies: []
allies:
  - Vater Sigmund Wolfherz
  - Ritter Konrad von Eisfeld
Connected_Quests:
  - "[[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]]"
Connected_Groups: []
---




> [!NOTE|div-m] Parent Location: `INPUT[inlineListSuggester(optionQuery(#Category/Hub),optionQuery(#Category/Region),optionQuery(#Category/Place),optionQuery(#Category/PointofInterest)):MyContainer]`
%% DISPLAYS NOTES THAT MATCH THE TAGS ABOVE %% 

> [!column|no-i no-t]
>> [!div-m|no-title]
>> ![[Brunhilde_Hammerschlag.png]]
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
A controlled, spare woman who took over the smithy when her husband died and has been holding the whole weight of that loss at arm's length ever since — waiting, without quite knowing it, for someone to hand her what was in that cave.

### 📝 Appearance
A powerfully built adult human woman, work-hardened from years at the forge. Her hands are calloused to the point where she doesn't feel heat the way others do. She doesn't fidget. When she's thinking about Dietrich, her expression goes very still — not sad exactly, just very quiet.

### 🎭 Mannerisms
Speaks in spare, controlled sentences. Asks precise questions and waits for precise answers. Her prices are fair and she doesn't haggle; that's the only warmth she extends until she's decided she trusts you. She will ask, exactly once, if you found anything in the cave. She will not explain why until she trusts you more.

### 💡 Key Motivation
Maintain the forge. Keep working. Understand — eventually, when the time is right — what actually happened to Dietrich in that pass. She is not ready to open the coffer. She is waiting for enough information to make opening it mean something rather than just be terrifying.

## 🗺️ Town Role & Function

Bruni runs Dietrich's old forge — Ritterstadt's full-service smithy. She can do what Hogar cannot: weapons, armor, structural metalwork. She is the hamlet's industrial backbone for anything metal. Without her, the village cannot arm itself or maintain its infrastructure above the level of basic tool repair.

### 🏪 Services

| Service | Cost / Notes |
| :--- | :--- |
| Weapon smithing | Full service; standard rates |
| Armor repair & fabrication | Full service |
| Tool work & general metalwork | Standard rates |
| **0002 Reward:** 50% off all smithing | For one month; if party tells her what they found in the cave |

## 💬 Conversation Guide

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

## 🎯 Quest Hooks

| Hook | Leads To | Trigger Condition |
| :--- | :--- | :--- |
| "Did you find anything up there? Anything that might have been his?" | [[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]] — Bruni's Coffer thread | Party returns from the wolf cave |
| The empty oilcloth matches the coffer's shape | Wachturm Arc (coffer contents) | Party shows her the oilcloth from the inner chamber |
| Party asks to help her open the coffer | Future arc (the node-key) | High trust; Bruni's Coffer thread fully activated |

## 🔗 Relationship Web

| NPC | Relationship Type | Notes |
| :--- | :--- | :--- |
| [[Dietrich Hammerschlag]] | Husband | Died three winters ago in the northern pass; wolves, officially |
| [[Hogar Irongrip]] | Separate operation | Different forge, different master — she leaves him to his own situation |
| [[Vater Sigmund Wolfherz]] | Quiet respect | He was the one who told her about Dietrich; he checks on her |
| [[Ritter Konrad von Eisfeld]] | Professional relationship | He paid the garrison's smith rate; she kept the garrison's arms in order |

# Statblock

```statblock
monster: Commoner
```
%% Suggested SRD block for a civilian smith. Adjust to taste. %%

# GM Notes

> [!danger] DM Eyes Only

## 🕵️ Secrets & Hidden Motivations

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
