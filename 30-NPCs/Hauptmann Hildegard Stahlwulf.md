---
publish: false
name: Hauptmann Hildegard Stahlwulf
MyContainer: "[[The Guardhouse]]"
MyCategory:
image: Hildegard_Stahlwulf.png
tags:
  - Category/People
  - NPC
  - ritterstadt-npc
obsidianUIMode: preview
aliases:
  - Hauptmann
NoteStatus: ❓
type: NPC
status: Alive
ancestry: Human
location: "[[Ritterstadt]]"
occupation: Garrison Commander
town_role: Military Authority
alignment: Lawful Good
disposition: Neutral
shop: The Guardhouse
founder: false
party_trust: 0
deceased_date:
char_alignment: Lawful Good
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
  - Ritter Konrad von Eisfeld
Connected_Quests:
  - "[[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]]"
  - "[[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]]"
Connected_Groups: []
---




> [!NOTE|div-m] Parent Location: `INPUT[inlineListSuggester(optionQuery(#Category/Hub),optionQuery(#Category/Region),optionQuery(#Category/Place),optionQuery(#Category/PointofInterest)):MyContainer]`
%% DISPLAYS NOTES THAT MATCH THE TAGS ABOVE %% 

> [!column|no-i no-t]
>> [!div-m|no-title]
>> ![[Hildegard_Stahlwulf.png]]
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
A watchful woman who assesses everything in a room before saying a word — and usually knows more than she lets on.

### 📝 Appearance
Adult human female, always in chain mail when in public — no exceptions. A longsword at her hip, a hand crossbow sometimes. Military bearing, hair kept short and practical. She doesn't fidget. She stands with her back to walls when she can.

### 🎭 Mannerisms
Speaks in direct, economical sentences. Rarely volunteers information — answers exactly what was asked, nothing more. Will state her limits plainly ("I want to expel him, but I lack grounds") rather than pretend she has authority she doesn't. Assesses the party from the moment she meets them, thoroughly and without advertising it.

### 💡 Key Motivation
Keep Ritterstadt physically safe. Serve Konrad's vision of the hamlet while maintaining her own professional integrity. She will not bend a rule she believes in, even for Konrad.

## 🗺️ Town Role & Function

Hildegard commands the garrison — the hamlet's only organized military force. She sets patrol routes, responds to threats, and maintains discipline among the soldiers. She is the first line of defense against gnoll incursions, wolf raids, and unwanted visitors. Without her, the garrison loses cohesion.

### 🏪 Services

| Service | Cost / Notes |
| :--- | :--- |
| Threat assessment / briefing | Available to any party she's judged capable |
| Garrison coordination | Sanctioned missions only; she'll cooperate if Konrad has commissioned the party |
| Patrol intelligence | Trust-gated; she'll share route information with established parties |

## 💬 Conversation Guide

| Topic | Freely Discussed? | Notes / Sample Line |
| :--- | :---: | :--- |
| Known threats (gnolls, wolves) | ✅ | Direct and specific. Will pull maps if available. |
| Garrison capability | ⚠️ | Honest about what they can and cannot do |
| Vethkar Graun | ⚠️ | "I want to expel him. I lack grounds. That's all I'll say." |
| Ewald Wennerberg | ❌ | Has noticed his behavior but says nothing |
| Konrad's finances | ❌ | "That is not my office." |
| The Wachturm | ❌ | "It's been there longer than any of us. It'll be there after." |

### 🔑 Trust-Gated Information

- **Low Trust (stranger):** Professional assessment of the party. Gives a clear picture of known threats in the uplands. Will ask directly about their experience and capabilities.
- **Medium Trust (regular):** Actively supports sanctioned missions. Coordinates garrison patrol routes to avoid conflicting with party operations. Will mention if she's noticed something unusual (Ewald's off-route patrol in 0002 is the key example).
- **High Trust (friend / proven):** Shares her private assessment of village vulnerabilities — specifically that the garrison is understaffed and that she has concerns about at least one soldier's reliability (Ewald, without naming him directly until pressed).

## 🎯 Quest Hooks

| Hook | Leads To | Trigger Condition |
| :--- | :--- | :--- |
| Brief encounter at The Ritter's Hall before Konrad's commission | [[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]] | Party meets Konrad; she's present, assessing |
| "A garrison soldier came back from patrol with a slash across his shoulder. He wouldn't say what made it." | [[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]] | Party asks about the north pass before taking the contract |
| Flags Vethkar as a concern without actionable grounds | [[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]] | Party asks why the garrison is watching the inn |

## 🔗 Relationship Web

| NPC | Relationship Type | Notes |
| :--- | :--- | :--- |
| [[Ritter Konrad von Eisfeld]] | Trusted ally | She is loyal to his vision; he relies on her judgment |
| [[Vogt Ruprecht Ackermann]] | Professional tolerance | She does not respect him but works within the same authority structure |
| Ewald Wennerberg | Commander (unaware) | She has noticed his unusual patrol behavior but has not connected it to anything actionable yet |

# Statblock

```statblock
monster: Veteran
```
%% Suggested SRD block for a garrison commander. Adjust to taste. %%

# GM Notes

> [!danger] DM Eyes Only

## 🕵️ Secrets & Hidden Motivations

### The Real Story
Hildegard is carrying two quiet concerns she hasn't voiced to Konrad: the garrison is underfunded relative to the threat level in the uplands, and one of her soldiers — Ewald Wennerberg — has been behaving unusually. Off-route patrols, unexplained absences, specific nervousness near the mill. She hasn't connected it to anything yet. It reads as stress, not treason.

### What They Know (But Won't Say)
- That Ewald has been on at least three unauthorized patrol routes in the past month (players can discover this via the travel encounter table in 0002: Ewald moving north, fast, startled to see them)
- That she is privately worried about the garrison's ability to hold the palisade if a gnoll warband — not scouts — came south
- That she doesn't trust the Vogt and has said nothing about it because she has no proof of misconduct, only instinct

### What They Fear
A coordinated external threat arriving before the garrison is ready. The thing she won't say aloud: she's not sure they'd hold.

### How to Reveal It
The Ewald thread surfaces naturally in 0002 if the party rolls his encounter and asks why he's heading north off-route. Hildegard's private garrison concerns come out only at high trust, in a private conversation, after the party has proven their competence in the field. She will say it bluntly: *"If twenty gnolls came through that gate tonight, I do not know that we hold it. I would like to not need to find out."*

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
- [[SP-PBS-03-The-Red-Cord]] — Scene 1 (Hook 2: "Keep his hand off it"; packs the half-banner)

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
