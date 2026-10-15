---
publish: false
name: Sigmund Holt
MyContainer: "[[The Ritter's Hall]]"
MyCategory:
image: Sigmund_Holt.png
tags:
  - "#Category/People"
  - "#NPC"
  - "#ritterstadt-npc"
  - "#gu"
obsidianUIMode: preview
aliases:
  - Field Research Officer
NoteStatus: ❓
type: NPC
status: Alive
ancestry: Human (Oeridian — University-educated, City of Greyhawk)
location: "[[Ritterstadt]]"
occupation: University Field Research Officer
town_role: Field Research Officer — Ritterstadt Satellite Station (Greyhawk University)
alignment: Lawful Neutral
disposition: Reserved but cordial
shop:
founder: false
party_trust: 2
deceased_date:
char_alignment: Lawful Neutral
char_status: Alive
char_race: Flannae Human
char_gender: Male
char_age: Adult
char_items: []
parents: []
children: []
siblings: []
partner: []
enemies: []
allies:
  - Ritter Konrad von Eisfeld
  - Drunik Runevault
  - Ritterstadt Questers
Connected_Quests:
  - "[[Greyhawk University/04. Campaign Logs/Session Notes/0001 - The Rust-Red Extraction]]"
Connected_Groups: []
---




> [!NOTE|div-m] Parent Location: `INPUT[inlineListSuggester(optionQuery(#Category/Hub),optionQuery(#Category/Region),optionQuery(#Category/Place),optionQuery(#Category/PointofInterest)):MyContainer]`
%% DISPLAYS NOTES THAT MATCH THE TAGS ABOVE %% 

> [!column|no-i no-t]
>> [!div-m|no-title]
>> ![[Sigmund_Holt.png]]
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
The University's man on the frontier — a methodical field scholar who treats the Sepia Uplands as the most important unpublished problem of his career, and who has learned to keep most of what he suspects to himself.

### 📝 Appearance
Middle-aged, lean, with ink-stained fingers and the slight forward stoop of a man who reads by candlelight more than he sleeps. Travel-worn academic dress kept deliberately neat. Carries a tri-compass and a field ledger everywhere, and consults both before he answers a question he hasn't already thought about. Calm eyes that go very still when something interests him — which is the only tell he has, and he knows it.

### 🎭 Mannerisms
Speaks in complete sentences, precise to the point of dryness. Asks for things "in writing, with notice." Logs everything. Defers reflexively to procedure when he wants time to think. When genuinely surprised he does not exclaim — he goes silent, re-reads, and asks the room to leave.

### 💡 Key Motivation
To establish the Ritterstadt Satellite Station as a permanent, credible University footprint, and — privately — to understand the binding network beneath the uplands before anyone with worse intentions does. The academic deliverables are real and he takes them seriously. They are also, increasingly, cover for a much larger inquiry he is not yet ready to name aloud.

## 🗺️ Town Role & Function

Sigmund Holt is the Field Research Officer (FRO) of the Greyhawk University Ritterstadt Satellite Station — the University's senior academic authority on site. He commissions and reviews field work, distributes survey instruments, maintains the examination ledger, and is co-custodian (with [[Ritter Konrad von Eisfeld]]) of the **Academic Registry lockbox** in the annex of [[The Ritter's Hall]]. He holds one of the two keys; access requires both keyholders or written authorisation from the absent one.

He is the faculty reviewer who signs off student papers and research filings, the secondary contact behind most University commissions, and the standing point of contact for the [[Ritterstadt Questers]] under their 90-day priority examination right. Examination requests go to him in writing with at least seven days' notice; he answers credentialed Quester requests personally.

Where [[Drunik Runevault]] handles the Mining Consortium's commercial commissions, Sigmund handles the *academic* deliverable — and the two do not always agree on what matters.

## 💬 Conversation Guide

| Topic | Freely Discussed? | Notes / Sample Line |
| :--- | :--- | :--- |
| University procedure, commissions, credits | ✅ | Precise and helpful. *"In writing, with seven days' notice, and I'll see it done properly."* |
| Mineral grades, survey method, instrumentation | ✅ | Genuinely enthusiastic. Will talk method longer than you want. |
| The Academic Registry / recovered items | ⚠️ | Will confirm custody arrangements; deflects on specifics. *"Catalogued, secured, and not for discussion in a common room."* |
| The clay registry vessel (Yrith Kael) | ⚠️ | Visibly careful. *"Under preservation restriction. I'd rather not, here."* |
| The binding network / Node 2 / the Erdgeist | ❌ | Until trust is high: *"That's outside the Station's published remit."* He has a working theory and will not air it. |

### 🔑 Trust-Gated Information
- **Low Trust:** Correct, procedural, useful for credits and commissions. Reveals nothing speculative.
- **Medium Trust:** Will discuss his preliminary reports on the Blackfrost Bloom ("the bloom is not natural — whatever feeds it is upstream of the symptom") and the warm-ground sites. Shares the four-site survey data.
- **High Trust:** Lays out his working theory — that the uplands sit over a failing binding network, that Node 2 at the Flan Waymark is one of several, and that the recovered vessel names something the murals only imply by absence: *the Erdgeist,* the held thing under stone. He has been waiting for a party he can say this to.

## 🎯 Quest Hooks

| Hook | Leads To | Trigger Condition |
| :--- | :--- | :--- |
| Priority examination of a recovered item | Registry / lore reveal | Questers bring in an anomaly under the 90-day right |
| "Speak to Konrad before this leaves the annex" | The vessel / Node 2 thread | Party recovers or asks to move Yrith Kael |
| A quiet request for further Waymark survey | The Wachturm & binding-network arc | High trust; party has proven discreet |

## 🔗 Relationship Web

| NPC | Relationship Type | Notes |
| :--- | :--- | :--- |
| [[Ritter Konrad von Eisfeld]] | Co-custodian of the Registry | Joint keyholders. Mutual respect, occasional friction over whether scholarship or security comes first. |
| [[Drunik Runevault]] | Professional counterpart | Drunik handles the commercial commissions and is openly sceptical of Sigmund's "methods." They cooperate; they do not entirely trust each other's priorities. |
| [[Vater Sigmund Wolfherz]] | Shared first name only | A *different* Sigmund — the chapel priest. The two are unrelated; the coincidence occasionally confuses newcomers. |
| [[Ritterstadt Questers]] | Preferred field party | After the vessel recovery, the Questers are the FRO's first choice for Sepia Uplands anomaly work. |

# Statblock

```statblock
monster: Commoner
```
%% Suggested SRD block for a non-combat field scholar. Adjust to taste. %%

# GM Notes

> [!danger] DM Eyes Only

## 🕵️ Secrets & Hidden Motivations

### The Working Theory
Sigmund's published remit is mineral and ecological survey. His private inquiry is the binding network. He has assembled — from the warm-ground sites, the acoustic data at the Waymark socket, the Blackfrost Bloom's "arcane axis," and the registry vessel's inscription — a working theory that the network restraining the Chained God is in slow civilisational failure, and that Node 2 is one degrading node of several. He tracks this carefully and tells almost no one. It is the inner ring of the regional threat picture, beneath the Iuz layer and the Temple of Elemental Evil.

### The Vessel (Yrith Kael)
When [[Felix Fleetfoot]] produced the clay vessel during the 0001 debrief, Sigmund went very still, read the title-page inscription twice, and asked the party to leave the room. His instruction afterward — *"Don't discuss the vessel outside this room until I've spoken to Konrad"* — was not procedure. He completed the translation himself against the second-edition Pre-Migration Flan lexicon held in the City of Greyhawk. He imposed a 30-day-notice, joint-signature restriction on moving it out of the Ritter's Hall annex on grounds of "preservation hazard." That justification is, in his own private view, only partly about preservation.

### What He Wants From the Party
A discreet, capable field party he can eventually trust with the real work. He is quietly hoping the Questers keep recovering registry material — and that when the time comes, they are people he can say the word *Erdgeist* to out loud.

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
| Flocktime 576 | Ritterstadt Questers | Briefed/​debriefed the [[Greyhawk University/04. Campaign Logs/Session Notes/0001 - The Rust-Red Extraction]] commission; took custody of the recovered vessel (AR-001). |
