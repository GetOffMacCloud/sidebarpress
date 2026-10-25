---
publish: false
name: Vethkar Graun
MyContainer: "[[The Grey Wolf]]"
MyCategory:
image: Vethkar_Graun.png
tags:
  - Category/People
  - NPC
  - ritterstadt-npc
obsidianUIMode: preview
aliases:
  - The Man from the South
  - Professor Graun
  - The Southerner
NoteStatus: ❓
type: NPC
status: Alive
ancestry: Human (Oeridian)
location: "[[Ritterstadt]]"
occupation: Professor of Military Tactics & Logistics
town_role: Faculty — War Studies & Engineering; Fencing Club training master
alignment: Lawful Neutral
disposition: Cordial
shop: The Grey Wolf (corner room)
founder: false
party_trust: 1
deceased_date:
char_alignment: Lawful Neutral
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
Connected_Quests:
  - "[[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]]"
Connected_Groups:
  - "[[The Kettenhaus]]"
---




> [!NOTE|div-m] Parent Location: `INPUT[inlineListSuggester(optionQuery(#Category/Hub),optionQuery(#Category/Region),optionQuery(#Category/Place),optionQuery(#Category/PointofInterest)):MyContainer]`
%% DISPLAYS NOTES THAT MATCH THE TAGS ABOVE %% 

> [!column|no-i no-t]
>> [!div-m|no-title]
>> ![[Vethkar_Graun.png]]
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
A courteous southern appraiser who turned out to be a professor, and is still — quietly, and with the University's knowledge — an appraiser.

### 📝 Appearance
Adult human male, somewhere in his forties, nineteen years in a profession that ages people faster than that. Dressed exactly one notch better than whatever room he is in, and never two. Everything about him is unremarkable on purpose and slightly too well-maintained to be accidental: clean boots on a mud road, a travelling coat with no wear at the cuffs, a ledger he is always partway through.

He is never standing when you find him. He is always already seated, and he was there first.

### 🎭 Mannerisms
**The cup.** He turns it a precise quarter-turn before he says something that costs him. A full half-turn, in two moves, is as close as he comes to being upset. The party may never notice; it is there whether they do or not.

**He quotes people back to themselves.** Their own words, days later, in almost the same phrasing. This is his single most unsettling habit — use it at least twice a session.

**He finishes things.** The sentence before he stands. The line of the drawing before he turns around. The drink before he leaves a burning farmstead.

He never raises his voice and never threatens. He describes a consequence in the tone he uses to order a drink, and lets the table do the arithmetic.

### 💡 Key Motivation
To file an honest report and be paid for it. He is not loyal to the [[The Kettenhaus|Kettenhaus]] and not hostile to Ritterstadt — he is loyal to *his own professional record*, which is the only thing he owns outright. He withholds before he is cornered. Once cornered he tells the truth, cleanly, and charges for it. **That distinction is the whole character.**

## 🗺️ Town Role & Function

Two roles, held at once, and the village has only been told about one of them.

**Publicly, since 0004:** Professor of Military Tactics & Logistics in the **Department of War Studies & Engineering**, and the **Fencing Club's** resident training master. He revealed this himself at the Grey Wolf on 23 Harvester 576.

**Still concealed:** he is a **Schätzer** — a field appraiser — for the Kettenhaus of Traft, in Ritterstadt to assess whether [[Ritter Konrad von Eisfeld]]'s debt is recoverable or whether foreclosure is appropriate. **This contract is open. Nothing has been filed.** See GM Notes.

He keeps the corner room at [[The Grey Wolf]] and takes the same table most mornings. His standing invitation from 0004 has never been withdrawn: *he will be at that table, and the party knows where to find him.*

### 🏪 Services

| Service | Cost / Notes |
| :--- | :--- |
| Instruction — tactics, logistics, siege and supply | University course credit. He is a genuinely good teacher and a hard marker |
| Fencing Club training | Free to members. **Bethany's initiation spar is overdue** |
| Professional read on a situation | Free if it costs him nothing; priced if it does |
| Information he was paid to hold | Not for sale. Available only if cornered with evidence |
| Coin | **Refuses it.** *"I've been paid twice already this month and I don't triple-dip; it makes the reports difficult."* Wants a good word instead |

## 💬 Conversation Guide

| Topic | Freely Discussed? | Notes / Sample Line |
| :--- | :---: | :--- |
| Tactics, logistics, supply, siege | ✅ | His actual expertise. He warms up noticeably |
| The five men / the cleaners | ✅ | Told them unprompted on the first morning, free, and will remind them of it |
| Traft coin and where men are hired | ✅ | *"Not where they are from — it is where they were hired."* |
| Ewald Wennerberg | ✅ | Enjoys this one. Sells the identity freely now the man is dead |
| His faculty post | ✅ | Since the reveal. Dry about it |
| Konrad's finances | ⚠️ | Will not volunteer. Will confirm if the party already knows |
| His employer | ❌ | Not until cornered. DC 18 Persuasion fails; DC 14 buys a plausible lie |
| Varek Doss / the second contract | ❌ | **The thing he most needs kept quiet.** See GM Notes |
| The word "catastrophic" | ❌ | Confirms only if shown something that earns it. Never volunteers it |
| The six-months warning | ❌ | Handout D. Still undelivered — see GM Notes |

### 🔑 Trust-Gated Information

- **Low (stranger):** Courtesy, a free read on anything that costs him nothing, and the standing offer at his table. Performs normalcy, and performs it well. *DC 15 Insight to notice the performance; DC 14 to notice his eyes cataloguing the exits within a round of entering any room.*
- **Medium (post-0004, current):** He has told them about the cleaners, Traft coin, the farms east, and Ewald. He regards them as competent, which from him is close to affection. He will answer professional questions honestly and decline personal ones pleasantly.
- **High (cornered with evidence, or genuinely trusted):** Both briefs, the debt figure, Doss's name and location, the marginal note. He answers honestly **once**, and then negotiates what happened in the room.

## 🎯 Quest Hooks

| Hook | Leads To | Trigger Condition |
| :--- | :--- | :--- |
| A professor of logistics takes an interest in twelve carts moving up the south road in one column | [[0005 - The Timber Run]] | He hears the convoy's shape and cannot help himself |
| "Your Ritter owes a house in Traft nine hundred gold and has told no one" | [[Campaign Threads]] P1 | Cornered, or offered something worth the trade |
| The Fencing Club initiation spar | Personal — [[Bethany McCockin-Simmons]] | Her Major sits in his department. Overdue since before 0004 |
| A scholar in the south who pays men to draw walls he will not come and look at | [[Varek Doss]] / Wachturm Arc W10 | Both contracts surfaced at once |

## 🔗 Relationship Web

| NPC | Relationship Type | Notes |
| :--- | :--- | :--- |
| [[The Kettenhaus]] | Employer (concealed) | He is their Schätzer. He is not their man |
| [[Varek Doss]] | Second client (concealed from the above) | The dangerous one. Doss does not know Vethkar is Kettenhaus; the Kettenhaus does not know about Doss |
| [[Ritter Konrad von Eisfeld]] | Subject of assessment | Konrad knows exactly what he is. Neither has said so aloud |
| [[Lotte Kesselring]] | Mutual professional wariness | *"He is pleasant. That is what worries me."* He rates her highly: *"She's been doing my job for twelve years and doesn't charge for it."* |
| [[Hauptmann Hildegard Stahlwulf]] | Correct, distant | Two professionals who have not needed to test each other |
| **Marek** | Retained bodyguard | Named at the longhouse. Contracted, not enrolled. **Still needs a story now that Vethkar is faculty** |
| *(second bodyguard)* | Retained bodyguard | Unnamed. Same problem |
| [[Bethany McCockin-Simmons]] | Student — his department | Fencing Club recognition runs through him |

# Statblock

**Presents as an unarmed traveller. He is not unarmed.**

```statblock
monster: Spy
```

**Use:** Spy (MM p.349) with the modifications below. *(Canon per [[0004 - Level 3 Scaling Notes]] — that file is otherwise superseded, but this block is not.)*

| Stat | Value |
| :--- | :--- |
| HP | 27 |
| AC | 12 (leather), or 15 with Uncanny Dodge active |
| To Hit | +4 |
| Multiattack | 2× shortsword (1d6+2 piercing) or 2× hand crossbow (1d6+2 piercing, 30/120 ft) |
| Cunning Action | Bonus action: Dash, Disengage, or Hide |
| Sneak Attack | 3d6 (once per turn, with advantage or an adjacent ally) |
| Skills | Deception +6, Insight +4, Investigation +5, Perception +6, Stealth +6 |
| Languages | Common, Oeridian, Baklunish, thieves' cant |
| Gear | Hand crossbow, two shortswords, **flash powder**, hooded lantern, travel chest with a false bottom **on the left** |

**Retained muscle (2):** Thug, HP 32, AC 11, +4, 2d6+2 mace, Pack Tactics, Multiattack ×2. They move only on signal — a specific cough pattern, or a coin left on the windowsill.

> [!danger] He will not be taken prisoner
> *"I don't go in a cell. I want to be clear about that before either of us does something that can't be walked back."* No threat in it — a statement of fact, in the tone of a man declining a second helping. If pressed past that line he fights **to escape, not to win**: flash powder, Cunning Action, the stable yard.

# GM Notes

> [!danger] DM Eyes Only

## 🕵️ The Real Story

**Vethkar Graun holds two contracts, and the second one could get him killed by the first.**

1. **The Kettenhaus brief (open).** Assess Konrad's Schuldbrief — **700 gp principal, ~900 gp with interest**, secured on Eisfeld timber rights — and report whether foreclosure is appropriate. Also: document the Wachturm's existence for the house's records, and report on whether the University's Field Station is an obstacle or an opportunity. **Nothing has been filed. The decision is still live and the party can still move it.**
2. **The Doss brief (secret).** A scholar in the south — [[Varek Doss]], of Eru Tovar — pays him to sketch the Wachturm's base carvings. Doss will not come and look himself. In the margin of his instructions he wrote one word, underlined: **catastrophic**. Vethkar has chosen, for four months, not to think about it very hard.

**Why the second one is lethal.** In his own words: if the Kettenhaus learns he has taken outside work in their operational area, he does not get dismissed — *he gets assessed, by someone like him.* Surfacing both briefs at once is the only moment in 0004 he is visibly uncomfortable, and it remains his single largest pressure point.

### 📌 Current standing — post-0004

| | |
| :--- | :--- |
| Faculty post | **Revealed** to the party, 23 Harvester 576 |
| Kettenhaus contract | **Open. Unfiled.** Party does not know he is an agent |
| Doss contract | **Concealed.** Party does not know it exists |
| His warning (Handout D) | **Undelivered** — he never fought beside them |
| Hazard Billing | Not earned. He was never recruited to the longhouse |
| His bodyguards | Unexplained. He is faculty now; two retained thugs need a reason |
| Party trust | Cordial and mutually professional. Not friendship |

## ⚠️ The conflict of interest nobody has noticed yet

**This is the best unused hook on the character, better than the bodyguards.**

A Greyhawk University professor is simultaneously assessing foreclosure against the feudal lord who hosts the University's field station — on collateral (the Eisfeld timber rights) that the Field Station's own expansion depends on.

That is a scandal in three directions at once: the University, Konrad, and the Kettenhaus, which is not supposed to have its Schätzer holding a salaried position inside the interest it is assessing. **Nobody in Ritterstadt has put it together.** [[Lotte Kesselring]] is the most likely to, and she will not say it without trust. Whoever raises it first controls what happens next, and Vethkar knows this perfectly well — it is one reason he revealed the faculty post on his own terms rather than waiting to be caught with it.

## 🩹 The Traft ruling — reading A

**Canon:** the cleric who cast *regenerate* on [[Rowena Ithilbrook]] came from Traft as a **coincidence of geography**. Traft is simply the only place within reach that has institutions at all; when a frontier station needs a high-level casting, that is where the request goes. Nothing sinister, no strings, nobody owed.

**Vethkar's part in it: none.** He did not arrange it, does not take credit for it, and if asked, says so plainly — and then points out, because he cannot help himself, that the same four-day road carried the men who took her hand and the cleric who put it back. He offers no conclusion. *He wants them to notice the road.*

> [!note] What this closes
> ⚜ **Hazard Billing** stays unearned and undelivered. Reading A gives it no back route. If you want the party to have that award's *effect*, it now needs a different source — the likeliest being Vethkar's report itself, once filed, describing them as a stabilising local asset.

## 🎁 Handout D needs a new route

His parting warning — *"If you're still in this area in six months, and things go the way I think they will, you may want to be very far away from that tower"* — was gated behind him fighting beside the party at the longhouse. **That condition can never recur.** The line is too good to lose. Three replacement routes:

1. **The logistics consultation.** He is asked, as faculty, to look at something — a convoy, a supply line, the Field Station's expansion — and gives the warning as an aside at the end, unbilled. Cheapest and most in character.
2. **Cornered on the Doss brief.** If the party ever surfaces the second contract, the warning comes out with everything else, as part of the one honest answer.
3. **The spar.** Delivered to Bethany alone, in his department, after she finally takes her initiation bout. Quietest version and the one with the most teeth, because she then has to decide who to tell.

## 🗝️ What he knows and will not say

- Konrad's exact debt position, and that he cannot pay it
- Doss's name, location, and the marginal note
- That he saw the fifth man across a cattle track and went back inside — *told once, in confidence, with a request that it not be repeated*
- That the Kettenhaus's patron clan took the Voormannship this year, and what his kontor is doing with that window

## 🎨 Portrait prompt

Converted to the house black-and-white ink style, 2026-10-24 (see [[Art-Style-Guide]]). Print: 1-bit at 600 dpi per its Print production steps.

No portrait exists; `image:` above is a dangling reference. Add the result to [[NPC Portrait Prompts — Midjourney]].

```
portrait of a composed middle-aged Oerid man in his forties, seated at a tavern table, plain dark travelling coat immaculately kept, one hand resting on a closed leather ledger, a pewter cup turned precisely before him, faint dry amusement, eyes reading the viewer rather than meeting them, 14th century germanic alpine dress, lit by a single candle and a low window with hard crosshatched shadow, three-quarter view, classic 1970s fantasy role-playing game module character portrait, black ink pen-and-ink drawing on pure white paper, head and shoulders, bold contour lines, crosshatched shadow on one side of the face, stippled skin texture, plain white background, high contrast black and white line art --ar 2:3 --v 8.1 --style raw --stylize 75 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark
```

> [!tip] Cover the name and it should still read as him
> **Precise, unhurried, professionally amused.** If a line would sound the same in another NPC's mouth, cut it. Full voice reference and every scripted line: [[0004 - Dialogue — Vethkar Graun]].

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
- [[SP-PBS-03-The-Red-Cord]] — referenced only (his unfiled Kettenhaus report; Konrad's choice of swords or coin bears on it)

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
| 22 Harvester 576 | Ritterstadt Questers | First contact, the Grey Wolf. Claimed timber assessment "on paper." Warned them unprompted about five men working the village |
| 23 Harvester 576 | Ritterstadt Questers | Revealed his faculty post — Professor of Military Tactics & Logistics, Fencing Club training master |
| | | |
