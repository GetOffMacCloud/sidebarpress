---
publish: false
name: Kurt Beckenhaus
MyContainer: "[[The Farmsteads]]"
MyCategory:
image: Kurt_Beckenhaus.png
tags:
  - Category/People
  - NPC
  - ritterstadt-npc
obsidianUIMode: preview
aliases: []
NoteStatus: ❓
type: NPC
status: Alive
ancestry: Human (Flan/Oeridian mixed — Flan line unrecognized)
location: "[[Ritterstadt]]"
occupation: Farmer
town_role: Farmstead Resident — The Beckenhaus Longhouse
alignment: Neutral Good
disposition: Guarded
shop:
founder: false
party_trust: 0
deceased_date:
char_alignment: Neutral Good
char_status: Alive
char_race: Human
char_gender: Male
char_age: Adult
char_items: []
parents:
  - Gottfried Beckenhaus
  - Ilse Beckenhaus
children:
  - Marta (daughter)
siblings: []
partner:
  - Marta-elder
enemies: []
allies:
  - Vater Sigmund Wolfherz
Connected_Quests:
  - "[[Greyhawk University/04. Campaign Logs/Session Notes/0003 - The Stolen Grain]]"
Connected_Groups: []
---




> [!NOTE|div-m] Parent Location: `INPUT[inlineListSuggester(optionQuery(#Category/Hub),optionQuery(#Category/Region),optionQuery(#Category/Place),optionQuery(#Category/PointofInterest)):MyContainer]`
%% DISPLAYS NOTES THAT MATCH THE TAGS ABOVE %% 

> [!column|no-i no-t]
>> [!div-m|no-title]
>> ![[Kurt_Beckenhaus.png]]
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
A young father running out of things he has not yet tried, who has arrived at the place where desperation meets the supernatural and is not sure he believes in the supernatural, except that it is the last option left.

### 📝 Appearance
Late twenties, looks older. The particular exhaustion of someone who has not slept cleanly in months. Dark-browned Oeridian complexion with Flan undertones he doesn't recognize in the mirror — the slightly wider set of the cheekbones, the quality of the hair, the way he goes very still when afraid, which is an old Flan reflex from a very old memory. Work-roughened hands. Tends to look at the ground when he's lying and at you steadily when he's telling the truth, which makes him easy to read once you know the tell.

### 🎭 Mannerisms
Polite to the point of stiffness with strangers. Relaxes in increments. Deflects questions about Marta with short answers and subject changes. His mother covers for him smoothly; he covers for himself badly. Has a habit of touching his left coat pocket when the shrine comes up in his mind — there's a folded piece of bark-parchment in there, the words he says at the tree. He doesn't know he does it.

### 💡 Key Motivation
His daughter Marta, six years old, has had a wasting illness since midsummer. Three different remedies from Vater Sigmund's kit. Two rounds of prayer. One expensive herb packet from a Traft trader. Nothing. He found the old tree-shrine at the forest edge by accident three months ago and started leaving grain there. He doesn't know if it's working. She hasn't gotten worse.

## 🗺️ Town Role & Function

Kurt is one of Ritterstadt's farming residents, arrived with his family from Edgerton (a small village two days east) two years ago after a poor harvest made staying untenable. He works the Beckenhaus family's longhouse field, participates in communal labor without issue, and has a reputation as a reliable if quiet neighbor. The hamlet considers the Beckenhausen unremarkable. This assessment is partially correct.

The Beckenhaus family is four adults and two children: Kurt, his wife **Marta-elder** (called by her full name to distinguish her from the sick daughter they named after her), his father **Gottfried**, and his mother **Ilse**, who has taken on primary care of little Marta while Kurt works. The second child — a boy, seven years old — is healthy and cheerful and not the source of any problems.

### The Stolen Grain
Kurt has been taking small amounts of grain from the mill's community surplus — not through the front door, but through a hole in the mill's east wall he found and quietly enlarged. He leaves the grain at the root-base of the old oak that marks the forest shrine. He takes what seems like enough to matter but not enough to be missed. He has miscalculated.

## 💬 Conversation Guide

| Topic | Freely Discussed? | Notes / Sample Line |
| :--- | :--- | :--- |
| Weather, farming, village life | ✅ | Open enough. Standard neighbor conversation. |
| His family's origins (Edgerton) | ✅ | *"Bad harvest three years running. We weren't the only ones."* |
| Little Marta's illness | ⚠️ | *"She's... the same. We're managing."* Changes subject quickly. Touches his pocket. |
| The mill, the grain stores | ⚠️ | Goes very still. *"What do you mean?"* Waits to hear how much you know before deciding anything. |
| The forest shrine | ❌ | Until trust is established: *"I don't know what you're talking about."* Then silence. |
| His family's Flan ancestry | ❌ | He genuinely doesn't know. His mother might. She won't say. |

### 🔑 Trust-Gated Information

- **Low Trust (stranger):** Polite, guarded. Good neighbor impression. Nothing useful.
- **Medium Trust (knows you're investigating the grain):** Cornered, afraid. Will not lie to someone who clearly already knows. Will confess to the grain if the party demonstrates they're not going to destroy his family. Tells them about Marta. Tells them about the shrine. Does not beg but comes close.
- **High Trust (treated with compassion):** Will show them the shrine. Will describe everything he's done there, the words, the offerings, how long. If the party helps Marta — genuinely helps, not just tries — he becomes a loyal contact. A man who owes you his daughter's life is not a small asset in a village.

## 🎯 Quest Hooks

| Hook | Leads To | Trigger Condition |
| :--- | :--- | :--- |
| Identified as the grain thief | Confrontation / resolution | Party investigates the stolen grain in 0003 |
| Shows the party the east forest shrine | Erdgeist connection / Wachturm thread | Trust established; Marta's illness explored |
| Beckenhaus family's Flan bloodline | Ward network thread (later arc) | Deep investigation into the family's eastern origins |

## 🔗 Relationship Web

| NPC | Relationship Type | Notes |
| :--- | :--- | :--- |
| [[Vater Sigmund Wolfherz]] | Trusted healer (increasingly desperate) | Sigmund has done what he can for Marta. He suspects more is going on — something residual, environmental — but hasn't told Kurt. |
| [[Vogt Ruprecht Ackermann]] | Indirect victim | Ruprecht is skimming the same grain supply Kurt is stealing from. They are independently depleting the same store without knowing about each other. |
| [[Hanz Korngut]] | Mill owner (unaware of the breach) | Hanz hasn't noticed the hole in the east wall yet. He will. |
| **Ilse Beckenhaus** (Kurt's mother) | Protector | She knows where Kurt goes on moonless nights. She has not asked why. She covers for him because this is what mothers do and because she has been covering for that family's strange relationship to the forest since long before she understood it. |

# Statblock

```statblock
monster: Commoner
```
%% Suggested SRD block for a farmer. Adjust to taste. %%

# GM Notes

> [!danger] DM Eyes Only

## 🕵️ Secrets & Hidden Motivations

### The Real Story
Kurt is doing what he is doing out of pure desperation. He has no occult knowledge, no training, no understanding of what the shrine actually is. He found it — an old oak with a hollow base, surrounded by stones in a pattern too deliberate to be natural, at the forest margin east of the palisade — and intuited that it was a place of asking. So he asks. Grain for the spirit's attention. Words he made up himself because he doesn't know the right ones.

What he doesn't know: the shrine *is* the east forest Erdgeist's focal point. The genius loci is real, is active, and has been noticing his offerings. The Erdgeist's agitation during 0003 is partly a symptom of the wider network distress — but the consistent, genuine offerings from a desperate father have had a small, partial, actual effect. Marta has not gotten worse. This is not coincidence.

### The Flan Bloodline
The Beckenhaus family are descended from a Flan shrine-tender lineage — one of the old families who maintained the outdoor spirit-sites before Oeridian settlement and organized religion pushed those practices underground. They moved eastward generations ago, intermarried with Oeridian settlers, and lost the knowledge. What remained is Ilse's instinct for the forest margin and the fact that the Erdgeist responds to their blood more readily than it would to most.

This matters for the ward network later. The binding system was maintained partly by Flan families who understood the sites as sacred obligations. If the network is to be repaired, having a living Flan-line family near one of the active minor nodes is significant.

### Ilse Beckenhaus (Kurt's Mother)
Ilse is approximately sixty, and knows more than she has said to anyone. She cannot explain why she knows the tree-shrine is real. She cannot explain why she has always stepped around the marked stones without being told where they are. She covered for Kurt immediately when she saw where he was going, before he said a word. If a player character gets to know her — which takes time and patience — she can become the most unexpected source of genuine lore in the hamlet.

### Marta's Recovery
Depends entirely on how the party handles the shrine. Options:
- **Appease/restore the Erdgeist properly (0003):** Marta begins recovering within a week. She is herself again by end of month. Kurt's loyalty is absolute.
- **Disrupt or damage the shrine:** Marta's condition destabilizes. Kurt is devastated and will blame the party if he learns they were involved, even if their intent was good.
- **Do nothing (shrine ignored):** The Erdgeist's distress continues; Marta holds at her current diminished state; Kurt keeps stealing grain.

### How to Play the Confession
When Kurt confesses about the grain and the shrine — which he will do if the party finds him out and treats him with even basic decency — play it without drama. He is not theatrical. He is just tired. He explains it the way you explain something you have been carrying alone for a long time: *"I found the old tree. I thought — I don't know what I thought. I left grain. I said some words. She didn't get worse."* Then: *"I know it's not enough. I know I've taken too much. Tell me what I owe."*

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
