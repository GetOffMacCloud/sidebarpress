---
publish: false
name: Detlef Fellmann
MyContainer: "[[The Drying Shed]]"
MyCategory:
image: Detlef_Fellmann.png
tags:
  - Category/People
  - NPC
  - ritterstadt-npc
obsidianUIMode: preview
aliases:
  - Old Fellmann
  - The Furrier
NoteStatus: ❓
type: NPC
status: Alive
ancestry: Human
location: "[[Ritterstadt]]"
occupation: Fur Trader & Furrier
town_role: Commerce / Pelts & Hides (University-contracted buyer)
alignment: Neutral Good
disposition: Gruff but fair
shop: The Drying Shed
founder: false
party_trust: 0
deceased_date:
char_alignment: Neutral Good
char_status: Alive
char_race: Human
char_gender: Male
char_age: Elder
char_items: []
parents: []
children: []
siblings: []
partner: []
enemies: []
allies:
  - Brunhilde Hammerschlag
  - Hanz Korngut
  - Hogar Irongrip
Connected_Quests:
  - "[[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]]"
Connected_Groups: []
---




> [!NOTE|div-m] Parent Location: `INPUT[inlineListSuggester(optionQuery(#Category/Hub),optionQuery(#Category/Region),optionQuery(#Category/Place),optionQuery(#Category/PointofInterest)):MyContainer]`
%% DISPLAYS NOTES THAT MATCH THE TAGS ABOVE %% 

> [!column|no-i no-t]
>> [!div-m|no-title]
>> ![[Detlef_Fellmann.png]]
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
A weathered old trapper-turned-buyer who pays honest weight for honest work — and who has skinned enough of the uplands to know when something out there has changed.

### 📝 Appearance
A broad, stooped elder in a much-mended fur coat that is its own advertisement. Grey stubble, a face like cured leather, and a left hand missing the last two fingers to an old frostbite — he'll tell you the story for free if you let him. He smells of cedar smoke, tallow, and the sharp tang of the tanning racks. His eyes are quick and appraising; he reads a pelt the way a scholar reads a page.

### 🎭 Mannerisms
Talks to the hides, not the hunter — turns a skin over, clucks his tongue, names the flaw before he names the price. Never haggles up; states a fair number once and means it. Calls every student "pup" regardless of age or ancestry. Goes quiet and careful when a pelt comes in from the deep north.

### 💡 Key Motivation
Keep the trade alive and keep faith with the University that licenses him. He's too old to run traplines now, so he buys what the young ones bring down — and he means to die owing no one a bent coin or a bad weight.

## 🗺️ Town Role & Function

Fellmann runs **The Drying Shed**, the racks-and-tanning yard at the edge of Ritterstadt where pelts are stretched, scraped, and cured. He is the village's only proper furrier, and — more importantly for students — he holds a **University Requisition charter** as a licensed field-materials buyer. He appraises skins, hides, and pelts brought in from sanctioned hunts and **pays in University Credits**, posted directly to the student's ledger. He handles no gold with students; the University settles his account, not the party.

> [!info] Why Credits, not coin
> Fellmann is a **contracted University buyer.** Students don't carry a gold economy (their currency is narrative only) — so when they bring him a pelt, he weighs it, grades it, and files a requisition chit that credits their academic account. He keeps a standing **float of Credits** advanced by the Requisition Office and reconciles it each tenday. This is the in-fiction reason a hunter's spoils become Credits. See [[DM Guide - Quest & Credits System]].

### 🏪 Services

| Service | Cost / Notes |
| :--- | :--- |
| **Buy pelts / hides / skins** | Pays **Credits** to the student's ledger — see Appraisal table below |
| Skinning knife / field skinning kit | 15 cr — improves pelt grade; advantage on the skinning check |
| Cured fur garments (cold-weather gear) | Cloak 20 cr · mittens & mask 10 cr · lined bedroll 25 cr |
| Trapping supplies | Snares, wire, scent — small Credit sums; useful in the uplands |
| Uplands beast lore | Free with a sold pelt — what it was, where it ranges, what it's worth |

## 💰 The Pelt Board *(buy-rates)*

> [!important] How appraisal works
> **Value = Base (by creature) × Quality (by condition).** Posted to the student's Credit ledger. Fellmann grades the *condition* on sight; a clean kill skinned with care is worth far more than a thing burned, dissolved, or hacked apart.

**Base value — clean pelt, by creature:**

| Creature tier (examples) | Base Credits |
|---|---|
| Tiny game — hare, marten, fox | 3 |
| CR ⅛–¼ — **wolf**, boar, giant rat | 8 |
| CR ½–1 — **dire wolf**, black bear, giant badger | 20 |
| CR 2–3 — brown bear, great elk | 50 |
| **CR 3 — winter wolf** *(prized: cold-warding fur)* | **75** |
| CR 4–6 — large/exotic predators | 120 |
| CR 7+ / rare / clearly magical hide | *By appraisal — usually routed to the University FRO* |

**Quality multiplier — condition of the skin:**

| Grade | Condition | ×Base |
|---|---|---|
| **Pristine** | Clean kill, skinned with care (**DC 13 Survival + a skinning kit**) | ×1.0 |
| **Serviceable** | Ordinary kill, rough skinning | ×0.6 |
| **Damaged** | Fire / acid / lightning / over-chopped, or a failed skinning check | ×0.25 |
| **Ruined** | Charred, dissolved, shredded | no value |

> [!note] Skinning a kill
> Takes ~10 minutes per beast and a blade (a proper **skinning kit** gives advantage). One **DC 13 Survival** check per creature sets the grade: success = the grade its damage allows; failure = drops one grade. *Alchemist's Fire, fireballs, and acid ruin pelts* — a tactical trade-off worth telling the players about once.

> [!warning] Float cap — keeps it from breaking the economy
> Fellmann can pay out roughly **300 Credits per tenday** from his University float. Beyond that he writes an honest **chit** ("redeem when the wagon comes up from Leukish, pup") — the Credits still post, just delayed. This rewards hunting without letting a pelt-farm replace quest income.

> [!example] Tonight's haul (0002)
> Three **winter wolves** killed in the den. If skinned cleanly (DC 13 each, with a kit): **3 × 75 = 225 cr** to split. Rougher work grades them down. A **dire wolf** (from C1/C2+) adds **20 cr** clean. *Alchemist's Fire used in the fight will have scorched whatever it touched — grade those hides down.*

## 📌 The Wanted Board — Standing Pelt Bounties *(CR ~5)*

> [!info] What this is
> A slate nailed beside the Drying Shed door, re-inked when the ink runs. These are **standing special orders** Fellmann holds open — big, dangerous quarry he can't get from a student's stray kill. Bounties are **premium over the normal Pelt Board** and double as **uplands hunting seeds** (a renewable reason to range out). The **Quality multiplier still applies** (values shown are **Pristine** — clean kill, careful skinning); grade down by the usual ×0.6 / ×0.25 for damage. Most of these exceed his tenday float — expect a **chit** for the balance.

> *"These I'll pay dear for, pup. Bring 'em in whole if you can. Burn 'em or boil 'em and you've cost us both."*

| Wanted | ~CR | Ranges in | Why he wants it | Bounty *(Pristine)* |
|---|:--:|---|---|:--:|
| **Bulette** *("landshark")* | 5 | Sepia Uplands scree & broken moor | Armor-plate hide — the shieldwrights in Leukish pay him, he pays you | **200 cr** |
| **Gorgon** *(iron-scaled bull)* | 5 | The high stony moors | Grey metal-scaled hide; the smiths ([[Brunhilde Hammerschlag|Bruni]] / [[Hogar Irongrip|Hogar]]) covet it | **225 cr** |
| **Giant Crocodile** | 5 | The **Quag Mire** fringes | Thick belly-hide for boots and brigandine | **175 cr** |
| **Great Snow Bear** *(boosted bear)* | ~5 | Uplands tree-line, first snows | A full winter coat — the trophy pelt of the season | **200 cr** |
| **Winter-Wolf Pack-Lord** *(true alpha)* | ~5 | Above the snowline, deep north | The cold-warding pelt of a real pack-lord; he's wanted one since Dietrich | **250 cr** |

**By appraisal only *(rare — usually a University FRO referral):***

| Wanted | ~CR | Why it's special |
|---|:--:|---|
| **Displacer Beast** | 3 | The shimmering hide makes a *displacer cloak* — he'll pay **250+** but routes it past the FRO first |
| **Wyvern** | 6 | Hide *and* an intact venom gland — Sigmund's office will outbid him for the gland; bring both, name your price |

> [!note] DM — how to use the board
> - **Renewable income + adventure seeds.** Each line is a one-sentence hunt prompt for a west-marches session in the uplands. Drop the quarry into a hex when the party goes looking.
> - **Thread ties:** the **Pack-Lord** points up the snowline toward the Wachturm disturbance (a bigger, older winter wolf than the 0002 alpha — *what's making them grow?*). The **Giant Crocodile** points at the **Quag Mire** ([[0001 - The Rust-Red Extraction]]'s Osa Veld / Renn Farr thread). The **Gorgon** loops pelt-money back to the smiths.
> - **Balance:** these are **CR 5 fights for a Level 3 party** — Deadly-plus by design. They're *aspirational*: meant to pull the party out to hunt deliberately, geared and rested, not to be stumbled into. Bounties scale with the danger; the chit-for-the-balance keeps the Credit spike from landing all at once.
> - **Refresh it:** cross one off when claimed and pencil a new beast in — the board should never be empty. Swap quarry to match wherever your hexes point.

## 💬 Conversation Guide

| Topic | Freely Discussed? | Notes / Sample Line |
| :--- | :---: | :--- |
| Pelts, prices, grading | ✅ | *"Bring it here. Let the hide tell me what you won't."* |
| Uplands beasts & ranges | ✅ | Generous with lore; he's trapped all of it once |
| How he lost the fingers | ✅ | *"Trapline, winter of '68. Left two fingers on the Wolf's Tooth ridge. Cheap, for the lesson."* |
| The deep north / game thinning | ⚠️ | *"Pelts from up past the snowline have gone... wrong. Few, and skittish. I don't like it."* (won't speculate further) |
| Dietrich Hammerschlag | ⚠️ | Goes quiet. *"Bought that man's furs twenty years. Best trapper I knew. Then one winter, nothing."* |
| His University charter / the float | ✅ | *"I don't pay gold, pup. I pay Credits. The school's good for it, and I'm good for the school."* |

### 🔑 Trust-Gated Information

- **Low Trust (stranger):** Fair grading, fair prices, calls you "pup," tells you what your pelt is and where the beast ranges.
- **Medium Trust (regular):** Will hold a chit open generously, throw in lore and a free skinning tip, and warn you which uplands quarters have gone quiet lately.
- **High Trust (friend / proven):** Talks about Dietrich plainly — the kind of trapper he was, the winter he didn't come back, and the one odd thing: *"The last pelts he sold me were winter-wolf. Three winters back. I've not seen another till you walked in just now."* **This is a soft echo of the Bruni thread — offer it after the Peak Beat, not before.**

## 🎯 Quest Hooks

| Hook | Leads To | Trigger Condition |
| :--- | :--- | :--- |
| Buys winter-wolf pelts; remarks the last he saw were Dietrich's | [[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]] — Bruni / Dietrich thread | Party sells winter-wolf pelts after the den |
| "Game's gone wrong up past the snowline" | Wachturm / upper-slope thread | Party asks about the deep north |
| Standing bounty board — he'll name beasts he wants skins of | Recurring hunting income | Any time; a renewable reason to range the uplands |

## 🔗 Relationship Web

| NPC | Relationship Type | Notes |
| :--- | :--- | :--- |
| [[Brunhilde Hammerschlag]] | Old acquaintance | He bought her late husband Dietrich's furs for twenty years; they don't speak of it |
| [[Hanz Korngut]] | Quiet agreement | Both old enough to feel the uplands changing; neither says it loudly |
| University Requisition Office | Licenser / creditor | Advances his Credit float; he reconciles each tenday |
| [[Hogar Irongrip]] | Trade neighbor | Buys his bone and sinew offcuts for glue and grips |

# Statblock

```statblock
monster: Scout
```
%% Suggested SRD block for an old trapper-turned-buyer. Adjust to taste. %%

# GM Notes

> [!danger] DM Eyes Only

## 🕵️ Secrets & Hidden Motivations

### The Real Story
Fellmann is exactly what he appears to be — an honest old furrier — which on this frontier is its own kind of rare. He has no scheme. What he *has* is forty years of reading the uplands through their pelts, and that long memory is quietly useful to the campaign: he is a **barometer of the Wachturm's failing ward.** Game has thinned and gone strange in the deep north — fewer prints, skittish animals, pelts that "don't sit right" — exactly the disturbance that pushed the winter wolves down in 0002. He doesn't know why. He just knows the north feels wrong, and he's old enough to trust the feeling.

### What He Knows (But Won't Volunteer)
- That winter-wolf pelts haven't crossed his counter since **Dietrich's last sale three winters ago** — until the party's. He finds this more unsettling than he lets on.
- Which quarters of the uplands have gone quiet (useful tracking intel if the party asks).
- That Dietrich, near the end, was bringing in pelts from *higher* than a sane trapper ranges — chasing something up the snowline. He never knew what.

### What He Fears
Not danger — he's old and unbothered by that. He fears the trade dying with him, and he fears, in a way he can't name, whatever is hollowing out the north. He'd rather sell furs and not think about it.

### How to Use Him at the Table
He's a **service NPC and a slow-lore valve.** Primary function: convert the party's kills into Credits, cleanly and renewably, with grading that rewards clean hunting. Secondary function: drip uplands/Wachturm foreshadowing through the *condition and rarity of pelts*, never through exposition. If the players want a sage, send them to Sigmund or Hanz; Fellmann only knows what the hides tell him — but the hides have been telling him something is wrong.

## ⚙️ DM Tuning Notes
*Defaults are set conservative so pelts supplement, not replace, quest Credits. Dials to adjust:*
- **Generosity:** raise the winter-wolf base (75 → 100) or the float cap (300/tenday) if your table hunts a lot and you want it to matter more.
- **Skinning friction:** drop the DC to 11 or waive the kit requirement if you'd rather not gate it; raise to 15 if you want clean pelts to feel earned.
- **Big specimens:** anything CR 7+ or magical (e.g., a **xorn hide**) should route to the **University FRO / Sigmund**, not Fellmann — he'll honestly tell students so. Keeps academic specimens flowing to the right place.

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
