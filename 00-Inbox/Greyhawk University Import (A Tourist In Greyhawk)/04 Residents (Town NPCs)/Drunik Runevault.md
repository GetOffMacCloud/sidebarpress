---
publish: false
name: Drunik Runevault
MyContainer: "[[The Fiend's Rest Public House]]"
MyCategory:
image: Drunik_Runevault.png
tags:
  - Category/People
  - NPC
  - ritterstadt-npc
  - gu
obsidianUIMode: preview
aliases:
  - Drunik
  - Runevault
NoteStatus: ❓
type: NPC
status: Alive
ancestry: Dwarf
location: "[[Ritterstadt]]"
occupation: Ritterstadt Mining Consortium Liaison
town_role: Mining Consortium Liaison — commissions and assays field specimens for the University Field Station
alignment: Lawful Neutral
disposition: Curt but fair
shop:
founder: false
party_trust: 2
deceased_date:
char_alignment: Lawful Neutral
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
  - Sigmund Holt
  - Ritterstadt Questers
Connected_Quests:
  - "[[Greyhawk University/04. Campaign Logs/Session Notes/0001 - The Rust-Red Extraction]]"
  - "[[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]]"
Connected_Groups: []
---




> [!NOTE|div-m] Parent Location: `INPUT[inlineListSuggester(optionQuery(#Category/Hub),optionQuery(#Category/Region),optionQuery(#Category/Place),optionQuery(#Category/PointofInterest)):MyContainer]`
%% DISPLAYS NOTES THAT MATCH THE TAGS ABOVE %% 

> [!column|no-i no-t]
>> [!div-m|no-title]
>> ![[Drunik_Runevault.png]]
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
The Consortium's man in Ritterstadt — a dwarf assayer who pays promptly, says little, and knows more about what comes out of the Sepia Uplands than he is willing to file on paper.

### 📝 Appearance
Broad and unhurried, with stone-grey in his beard and the permanent squint of a man who reads mineral grain in poor light. Plain, hard-wearing dress kept clean; a loupe on a cord and an assayer's pick always within reach. His office at the Greyhawk University Field Station smells of cold stone and mineral oil — a standing desk buried in survey notes, two uncomfortable chairs, and a corkboard pinned with a hand-drawn map of the uplands.

### 🎭 Mannerisms
Speaks in short, exact sentences and corrects sloppy terminology by reflex — he uses *ferrotholite* and "rust-red" interchangeably and expects students to learn the difference. Conducts real business in the back room of [[The Fiend's Rest Public House]], behind the hearth, away from common earshot. When he is concealing something his left hand goes flat on his thigh — a tell he does not know he has.

### 💡 Key Motivation
To deliver the Consortium's commissions cleanly and on time — and, privately, to confirm a suspicion he is not ready to put in an official filing: that the secondary ferrotholite vein shares its composition with the foundation stone of [[The Wachturm]], which would make it older than Oeridian Ritterstadt entirely. He wants certainty before he writes a word that the University, or anyone above him, could act on.

## 🗺️ Town Role & Function

Drunik Runevault is the **Ritterstadt Mining Consortium Liaison** — the commercial counterpart to [[Sigmund Holt]]'s academic office. He commissions field expeditions, assays returned specimens, and pays in University credit vouchers (UC) drawn on the Consortium liaison office. The job-board post that opened [[Greyhawk University/04. Campaign Logs/Session Notes/0001 - The Rust-Red Extraction]] was his.

Where Sigmund handles the *academic* deliverable, Drunik handles the *commercial* one — and the two do not always agree on what matters. They cooperate; they do not entirely trust each other's priorities.

## 💬 Conversation Guide

| Topic | Freely Discussed? | Notes / Sample Line |
| :--- | :--- | :--- |
| Commissions, pay, specimen handling | ✅ | Direct and reliable. *"Bring it back sealed and intact. You'll be paid the same day."* |
| Mineral grades, ferrotholite, assay method | ✅ | Will correct your terms and talk longer than you'd like. |
| The Ochre Escarpment cairn / grid E3 | ⚠️ | Visibly reluctant; gives the agreed cover story and no more. |
| The secondary vein's true age / Wachturm link | ❌ | *"That's not confirmed, and I don't file guesses."* Left hand flat on thigh. |
| Osa Veld & Renn Farr | ⚠️ | Off the record only. *"Not a commission. Not logged. Just — keep your eyes open out there."* |

### 🔑 Trust-Gated Information
- **Low Trust:** A fair employer. Commissions, pay, and clear specimen requirements; nothing speculative.
- **Medium Trust:** Admits he filed an internal inquiry over the undocumented prior survey at E3 — University-issue tool marks, no paperwork, a team that never came back. Names [[Osa Veld]] and [[Renn Farr]].
- **High Trust:** Concedes his real suspicion — that the secondary vein and the Wachturm foundation stone are the same pre-Oeridian material — and that he re-sealed the Wachturm sub-floor himself, imperfectly, after the missing surveyors had opened it.

## 🎯 Quest Hooks

| Hook | Leads To | Trigger Condition |
| :--- | :--- | :--- |
| Extract intact specimens from the Ochre Escarpment | [[Greyhawk University/04. Campaign Logs/Session Notes/0001 - The Rust-Red Extraction]] | Party accepts the Consortium commission |
| "Find Osa and Renn — quietly, off the record" | [[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]] | Party earns enough goodwill for the unlogged ask |
| Confirm the secondary vein's composition | Wachturm / binding-network arc | High trust; party has proven discreet |

## 🔗 Relationship Web

| NPC | Relationship Type | Notes |
| :--- | :--- | :--- |
| [[Sigmund Holt]] | Professional counterpart | Drunik = commercial commissions, Sigmund = academic deliverable. They cooperate; Drunik is openly sceptical of Sigmund's "methods." |
| [[Osa Veld]] | Subject of inquiry | One of the missing prior surveyors. Drunik wants them found — unofficially. |
| [[Renn Farr]] | Subject of inquiry | The other missing surveyor; believed to have gone northeast toward the Quag Mire margin. |
| [[Ritterstadt Questers]] | Preferred field party | His first call for upland specimen work after the 0001 commission. |

# Statblock

```statblock
monster: Commoner
```
%% Suggested SRD block for a dwarf assayer. Adjust to taste. %%

# GM Notes

> [!danger] DM Eyes Only

## 🕵️ Secrets & Hidden Motivations

### The Vein and the Wachturm
Drunik genuinely wants the ore — the commission is real. But his private reason for re-running a survey no one had touched in two seasons is that he suspects the secondary ferrotholite vein is the same material as the Wachturm's foundation stone, which would date it four thousand years before Oeridian Ritterstadt. He will not file this until he is certain, because of what it would invite.

### The Prior Survey Team
University-issue tool marks at E3 belong to an undocumented survey that Drunik did not authorise. He filed an internal inquiry. The surveyors — [[Osa Veld]] and [[Renn Farr]] — accessed the Wachturm sub-floor (Node 1), then went northeast into the Quag Mire margin and never returned. Drunik re-sealed the sub-floor himself, imperfectly, and has been quietly trying to find them ever since. His off-record ask to the party is the bridge to [[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]].

### "The Second Window"
As of 25 Flocktime he was overheard at the Fiend's Rest speaking of *"the second window,"* paid for his bread in coin, and left half of it untouched. He is preoccupied, and not sleeping well. See [[Rumor — Drunik Runevault was overheard in the Fiend's Rest at midday]].

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
| Flocktime 576 | Ritterstadt Questers | Commissioned and debriefed [[Greyhawk University/04. Campaign Logs/Session Notes/0001 - The Rust-Red Extraction]]; paid 600 UC + coin. Made the off-record ask about Osa Veld and Renn Farr. |
