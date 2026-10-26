---
publish: false
name: Temür Bayan
MyContainer:
MyCategory:
image: Temür_Bayan.png
tags:
  - Category/People
  - town-npc
  - traveler
  - velvet-shadow
  - planned
  - dm-only-details
obsidianUIMode: preview
aliases:
  - Temür
  - Wegwiur trader
NoteStatus: ❓
type: npc
npc_status: planned-arrival
status: Alive
ancestry: Human (Flan — Wegwiur / Wolf Nomad)
occupation: Wolf Nomad (Wegwiur) amber-and-fur trader
town_role: Itinerant northern trader — not yet arrived
origin: The Wegwiur (Wolf Nomad) lands, bordering the Burneal
related-villain: "[[DM Reference — The Velvet Shadow]]"
founder: false
party_trust: 0
deceased_date:
char_alignment:
char_status: Alive
char_race: Human
char_gender: Male
char_age: Adult
char_items: []
parents: []
children: []
siblings: []
partner: []
enemies: []
allies: []
Connected_Quests: []
Connected_Groups: []
---




> [!NOTE|div-m] Parent Location: `INPUT[inlineListSuggester(optionQuery(#Category/Hub),optionQuery(#Category/Region),optionQuery(#Category/Place),optionQuery(#Category/PointofInterest)):MyContainer]`
%% DISPLAYS NOTES THAT MATCH THE TAGS ABOVE %% 

> [!column|no-i no-t]
>> [!div-m|no-title]
>> ![[Temür_Bayan.png]]
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

> [!warning] STATUS: not yet introduced — planned arrival
> Temür is a **deliberate future arrival**, not part of the caravan rotation. Bring him to Ritterstadt **somewhere down the line — roughly 3–6 months out IRL** — as the carrier who first drops the [[#The Winter Vanguard rumors he carries|Winter Vanguard rumors]] on the village. Until then he and his rumors stay staged. **Do not add him to [[Caravan Schedule]] yet.**

### Character Descriptor
A garrulous, road-worn Wegwiur trader who has come a very long way south — half to sell amber and furs, half because the north has stopped feeling like home. An unwitting witness to something he can't name.

### 📝 Appearance & Manner
A weather-cured Wegwiur trader of the Wolf Nomads, come a very long way south with a string of shaggy ponies carrying amber, white furs, horn, and felt, looking to trade for worked metal, salt, and Verbobonc steel. He is garrulous in the way of a man who has been alone on a cold road too long, superstitious, and quick to touch the wolf-tooth at his neck. He did not come south only to trade. He came because the north has stopped feeling like home — and a man tells that kind of thing to strangers over drink more easily than to his own khan.

### 🗺️ Who He Is
He is an **unwitting witness**: he has seen the [[Kaelen Vane, the Ashen Knight|Vanguard's]] work, fled the edge of it, and carries the truth without understanding it. He has never heard the name "Velvet Shadow." He thinks it's a bad winter with a war in it.

# Statblock

```statblock
monster: Scout
```
%% Suggested SRD block for a hardy long-road trader. Adjust to taste. %%

# GM Notes

> [!danger] DM Eyes Only

## How to bring him in

1. When the moment comes (the staged Wolf-Nomad beat), add him to [[Caravan Schedule]] as a one-off or rare-cadence entry (origin *the Wegwiur lands*, sells amber/furs/horn, buys steel/salt), or simply narrate his arrival and create a Travelers note by hand.
2. Set the staged **Winter Vanguard** rumors (below) to `status: live` over the days he's in town, and run their seed kits to bump [[The Velvet Shadow — Burneal Reach]] (and re-band its `axis_martial` upward — the army is now visible).
3. Consider advancing the global stage tag toward `closing` once he's spoken.

## The Winter Vanguard rumors he carries

These three staged notes in the Rumor Pool are his to deliver (tag `winter-vanguard`, `status: staged`, held out of template rotation):

- [[Rumor — Winter Vanguard — the winter that has captains]]
- [[Rumor — Winter Vanguard — the burned knight in black iron]]
- [[Rumor — Winter Vanguard — the diggers under the ice]]

## Related
> [!abstract] Connections
> - The threat he unwittingly reports: [[DM Reference — The Velvet Shadow]] · [[The Velvet Shadow — Burneal Reach]]
> - The army he saw: [[Kaelen Vane, the Ashen Knight]] and the Winter Vanguard

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
