---
publish: false
MyContainer: "[[The Ritter's Hall]]"
MyCategory: Government
image: Ruprecht_Ackermann.png
tags:
  - Category/People
obsidianUIMode: preview
aliases:
  - The Vogt
  - Ackermann
  - Ruprecht
NoteStatus: ❓
char_alignment: Lawful Neutral
char_status: Alive
char_race: Human
char_gender: Male
char_items:
  - "[[fine-clothes-xphb|Fine Clothes]]"
  - "[[dagger-xphb|Dagger]]"
  - "[[abacus|Abacus]]"
char_age: Adult
parents: []
children: []
enemies: []
allies:
  - Ritter Konrad von Eisfeld
siblings: []
partner: []
Connected_Quests:
  - "[[Greyhawk University/05. The Hamlet of Ritterstadt/Buildings & Infrastructure/The Fiend's Rest Public House/The Job Board/0003 - The Stolen Grain|0003 - The Stolen Grain]]"
Connected_Groups: []
---

> [!NOTE|div-m] Parent Location: `INPUT[inlineListSuggester(optionQuery(#Category/Hub),optionQuery(#Category/Region),optionQuery(#Category/Place),optionQuery(#Category/PointofInterest)):MyContainer]`

> [!column|no-i no-t]
>> [!div-m|no-title]
>> ![[Ruprecht_Ackermann.png]]
>
>> [!div-m|no-title] Vogt Ruprecht Ackermann
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

Alignment: `INPUT[template-npc-alignment][:char_alignment]`

Status: `INPUT[template-person-status][:char_status]`

Race/Species: `INPUT[template-person-race][:char_race]`

Gender: `INPUT[template-person-gender][:char_gender]`

Age: `INPUT[template-person-age-range][:char_age]`

---

**Vogt Ruprecht Ackermann** is the reeve of Ritterstadt — the Ritter's appointed administrator, tax collector, record-keeper, and the person who ensures that the lord's decisions actually get implemented. He is 55, thin in a papery way, with ink-stained fingers and quick eyes that inventory a room in the first second and spend the rest of the conversation checking the math.

Ruprecht has held his position for nineteen years, through the end of the old Ritter's tenure and all of Konrad's. He knows where every coin in the village has come from and where it has gone. He is efficient, organized, and quietly indispensable. He is also, and has been for years, skimming. Not dramatically — a few coppers per household per quarter, rounded figures that never quite square with the stated totals, small adjustments that individually look like clerical error. Over nineteen years it has added up to a very comfortable private reserve, none of which Konrad knows about.

Ruprecht is not evil. He is cautious, self-interested, and experienced in the calculation that a little corruption, properly managed, is more stable than none at all. He genuinely believes the village is better off with him in his position than with anyone else. He may even be right.

He knows about the letters in the iron chest — the ones that could invalidate Konrad's claim. He has known for twelve years. He has not used them. He keeps them as insurance.

# Statblock

```statblock
monster: Noble
```

# GM Notes

- **The Skimming:** DC 16 Investigation on the village tax records to notice the discrepancies. DC 18 to prove it conclusively. Ruprecht has explanations for everything individually; the pattern is only damning in aggregate. If confronted, he will not confess — he will counter-accuse and muddy the waters. He is very good at this.
- **The Letters:** Ruprecht knows exactly where they are and what they say. He won't volunteer this information unless his back is truly to the wall. If the party threatens to expose his skimming, he may trade the information about the letters as a counter. This would be catastrophic — it could destroy the village's political stability at exactly the wrong moment.
- **Ruprecht and the Ritter's debt:** He knows about the debt. He has actually been trying, in his own way, to create a financial cushion that might help address it — using some of his private reserve to quietly pre-purchase timber rights before the Consortium can snap them up. He has not told Konrad because Konrad would ask where the money came from. This is, technically, protecting the village. It is also deeply compromised.
- **Roleplaying Ruprecht:** He is smooth and pleasant in a way that never quite feels warm. He laughs at exactly the right moments. He remembers every name and uses them deliberately. He is the kind of person who makes you feel like you're being managed, even when he's agreeing with you. He dislikes Hildegard intensely because she sees through him and doesn't bother to pretend otherwise.
- **What he wants:** To remain in his position until he dies, comfortable, having left the village functioning. He does not want power beyond what he has. He wants security, control, and to never have to account for the last nineteen years.

# Inventory

The following items belong to `= this.file.name`.

```dataviewjs
let rawItems = dv.current().char_items;
if (rawItems && rawItems.length > 0) {
    let charItemNames = rawItems.map(item => {
        return (typeof item === 'string') ? item.replace(/[\[\]]/g, "") : item.path.split('/').pop().replace(".md", "");
    });
    let items = dv.pages('"3-Mechanics/Items"')
        .where(p => charItemNames.includes(p.file.name));
    dv.table(
        ["Item", "Cost", "Weight"],
        items.map(p => [p.file.link, p.cost ?? "—", p.weight ?? "—"])
    );
} else {
    dv.paragraph("*No items currently equipped.*");
}
```

# Connections

Quests: `INPUT[inlineListSuggester(optionQuery(#Category/Quest)):Connected_Quests]`

Groups: `INPUT[inlineListSuggester(optionQuery(#Category/Group)):Connected_Groups]`

# Relationships

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

> [!NOTE]- Relationship Config
> `BUTTON[button_person]`
> 
> | Parents | Partner | Children |
> |---|---|---|
> | `INPUT[list:parents]` | `INPUT[list:partner]` | `INPUT[list:children]` |
> 
> | Siblings | Enemies | Allies |
> |---|---|---|
> | `INPUT[list:siblings]` | `INPUT[list:enemies]` | `INPUT[list:allies]` |
