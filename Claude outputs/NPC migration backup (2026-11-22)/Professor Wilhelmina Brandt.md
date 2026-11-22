---
publish: false
name: Professor Wilhelmina Brandt
MyContainer: "[[The Ritter's Hall]]"
MyCategory:
image: Wilhelmina_Brandt.png
tags:
  - Category/People
  - NPC
  - ritterstadt-npc
  - gu
  - visiting-faculty
obsidianUIMode: preview
aliases:
  - Professor Brandt
NoteStatus: ❓
type: NPC
status: Alive
ancestry: Human (Oeridian–Suel — City of Greyhawk)
location: "[[Ritterstadt]]"
occupation: Professor of Antiquarian Wardcraft, Greyhawk University
town_role: Visiting Faculty — sent from the City of Greyhawk to examine Registry holdings AR-001 (and the recovered anchor stone)
alignment: Lawful Neutral
disposition: Blunt, imperious, intellectually fearless
shop:
founder: false
party_trust: 1
deceased_date:
char_alignment: Lawful Neutral
char_status: Alive
char_race: Human
char_gender: Female
char_age: Adult (older — senior faculty)
char_items: []
parents: []
children: []
siblings: []
partner: []
enemies: []
allies:
  - Ritterstadt Questers
  - Brunhilde Hammerschlag
  - Sigmund Holt
Connected_Quests:
  - "[[0003 - The Anchor Stone|GHU3 — The Anchor Stone]]"
Connected_Groups: []
---




> [!NOTE|div-m] Parent Location: `INPUT[inlineListSuggester(optionQuery(#Category/Hub),optionQuery(#Category/Region),optionQuery(#Category/Place),optionQuery(#Category/PointofInterest)):MyContainer]`
%% DISPLAYS NOTES THAT MATCH THE TAGS ABOVE %% 

> [!column|no-i no-t]
>> [!div-m|no-title]
>> ![[Wilhelmina_Brandt.png]]
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
The University's foremost living authority on pre-Migration Flan binding-magic — a senior scholar who came to the frontier because the frontier finally produced something worth the journey, and who says the frightening thing out loud that everyone else has been carefully not saying.

### 📝 Appearance
Tall, straight-backed, past sixty and utterly unbothered by it. Iron-grey hair pinned severely. City tailoring, expensive and out of place in a hamlet, worn without apology. She wears a jeweler's loupe on a chain and a set of bronze reading-styli in a roll she never lets out of reach. Her hands are steady and deliberate; she handles a four-thousand-year-old vessel the way a surgeon handles a heart. Pale Suel colouring under the Oeridian name — a detail she neither hides nor explains.

### 🎭 Mannerisms
Speaks in declaratives. Does not soften findings. Interrupts hedging. When a student says "it might be," she says "it is, or it isn't — which." She thinks by lecturing, so she will explain a thing at length and expect you to keep up. The one crack in the certainty: when something genuinely surprises her she stops mid-sentence, goes to the object, and forgets the room is there.

### 💡 Key Motivation
To read the binding network whole before it fails — as scholarship, and as the only intellectual problem left that she considers her equal. She is not reckless with the artifacts; she is reckless with comfort. She would rather the party know a terrifying truth than be spared it, because in her experience people who are spared truths get other people killed.

## 🗺️ Town Role & Function

Professor Brandt holds the Greyhawk University chair in Antiquarian Wardcraft at the City of Greyhawk campus. She is the credentialed authority behind the second-edition Pre-Migration Flan lexicon that [[Sigmund Holt]] used for his own translation of [[AR-001 — Yrith Kael, the Registry Sealed|Yrith Kael]] — meaning Sigmund has been reading *her* work at second hand for months.

She travels to Ritterstadt in Wealsun 576 CY on a **supervised examination request**: the vessel cannot leave the Ritter's Hall annex without thirty days' notice and joint custodial signature, so the mountain comes to Muhammad. Her remit expands the moment [[Brunhilde Hammerschlag|Bruni]] surfaces the anchor stone — because now there are *two* pieces of the same architecture on one table, and she is the only person in the Flanaess qualified to read them against each other.

She and Sigmund are natural antagonists of temperament: he guards, she publishes; he withholds, she declares. They need each other and both know it. She defers to no one on the Flan and to almost no one on anything else.

## 💬 Conversation Guide

| Topic | Freely Discussed? | Notes / Sample Line |
| :--- | :--- | :--- |
| Ur-Flan script, binding notation, the lexicon | ✅ | Expansive, brilliant, will teach for an hour. *"This register isn't liturgical. It's an instruction. They were engineers who happened to pray."* |
| The registry vessel & the anchor stone | ✅ | She wants the party to understand. Unlike Sigmund, she *explains.* |
| What the network holds / the thing beneath | ⚠️ | She'll go as far as the evidence and then stop — honestly. *"I can tell you the architecture is a cage. I cannot yet tell you the animal. Anyone who claims otherwise is selling you something."* |
| Whether it can be fixed | ⚠️ | *"In principle. In practice you are six students and a smith's grief, and I am one old woman. So: cautiously."* |
| Her opinion of Sigmund's caution | ⚠️ | Dry. *"Holt is a fine surveyor. He has confused discretion with a plan."* |

### 🔑 Trust-Gated Information
- **Low Trust:** Delivers the analysis plainly and completely — she does not gate the *findings*. What she gates is candor about her own uncertainty and fear.
- **Medium Trust:** Admits what she does *not* know: that the registry names a containment, that the anchor stone is one physical key of several, and that the removal of keys — like the one Dietrich carried off — is part of why the network is failing. She'll concede the problem may be past a single generation's fixing.
- **High Trust:** Says the quiet part. The warmth in these objects is not residual — it is *live*. Something is still being held, right now, by an architecture that is coming apart, and the fact that no one in living memory has felt the consequences is not reassurance. It is the measure of how much the old builders over-engineered, and of how little margin is left.

## 🎯 Quest Hooks

| Hook | Leads To | Trigger Condition |
| :--- | :--- | :--- |
| The paired analysis of vessel + anchor stone | [[0003 - The Anchor Stone\|GHU3 — The Anchor Stone]] | She arrives to examine AR-001; Bruni surfaces the stone |
| Coordinates back to the Flan Waymark (Node 2) | The first sanctioned node repair | She reads the anchor's destination-glyph against the registry diagram |
| "Bring me anything that hums" | The wider Wachturm arc; future registry material | Any trust; she is building a corpus |
| The Second Voice question | The Negotiation capstone; Pair-Walker lineage | High trust; she reads the vessel's ritual constraint and grasps its implication faster than Sigmund is comfortable with |

## 🔗 Relationship Web

| NPC | Relationship Type | Notes |
| :--- | :--- | :--- |
| [[Sigmund Holt]] | Professional rival / reluctant ally | He has translated *from her lexicon* for months. Mutual respect wrapped in constant friction over discretion vs. disclosure. |
| [[Ritter Konrad von Eisfeld]] | Co-custodian she must work around | Konrad holds the second key. She finds his security-mindedness tiresome and his authority real. |
| [[Brunhilde Hammerschlag]] | Source of the anchor stone | Brandt is, uncharacteristically, gentle with Bruni. She understands exactly what the stone cost. |
| [[Ritterstadt Questers]] | Her chosen instrument | She has decided the Questers are competent. She will spend them like good coin — and defend them like it, too. |

# Statblock

```statblock
monster: Mage
```
%% Suggested SRD block for a senior arcane scholar. Adjust to taste. %%

# GM Notes

> [!danger] DM Eyes Only

## 🕵️ Secrets & Hidden Motivations

### What She Actually Concluded
Brandt read both objects in a single afternoon and understood more than she said in the room. The registry (Yrith Kael) is a *catalog* of a six-node containment lattice. The basalt stone Dietrich carried out of the northern cave is a genuine **anchor key** — one of the physical stones that "hold" the lattice — and it has been out of a socket for years, which she correctly infers has measurably worsened the network's decline. The two objects together let her triangulate the lattice's registry node: the **Flan Waymark at Hex E3 (Node 2)** — the only site where the repair sequence can *begin* and the only intact socket where this stone's notation can be read and re-seated. That is the coordinate she hands the party.

### What She Withholds (For Now)
She suspects — from the live warmth, the 4-second broadcast, the way both objects "listen" — that the containment is not dormant but *active and straining.* She does not yet name the Chained God layer (she can't; the evidence isn't there), but her private assessment is bleaker than Sigmund's, not milder. She also grasps the **Second Voice / Pair** constraint on the vessel faster than Sigmund did, and privately files it as the likeliest real solution — and the likeliest thing to get people killed.

### The Friction With Sigmund
Sigmund imposed the preservation restriction partly to control the pace of disclosure. Brandt's arrival takes that control away from him, and he knows it. Their conflict is genuine and useful at the table: **Sigmund is the brake, Brandt is the accelerator, and the party is the steering.** Neither is wrong. Let them argue in front of the players and let the players feel the weight of choosing whom to believe.

### What She Wants From the Party
A field instrument she can trust to go to the sites she cannot reach and bring back readings she can trust. She is old, she is City-soft, and she cannot spend a tenday sleeping on cold stone. The Questers can. She intends to make them the hands of her scholarship — and she will be more loyal to them than her manner suggests, because competence is the only thing she has ever truly respected.

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
| Wealsun 576 | Ritterstadt Questers | Arrived from the City of Greyhawk for supervised examination of AR-001. Delivered the paired analysis of the registry vessel and Dietrich's anchor stone; produced coordinates directing a return to the Flan Waymark (Node 2). |
