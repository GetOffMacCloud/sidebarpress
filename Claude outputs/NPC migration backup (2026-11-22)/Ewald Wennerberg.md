---
publish: false
name: Ewald Wennerberg
MyContainer: "[[The Guardhouse]]"
MyCategory:
image: Ewald_Wennerberg.png
tags:
  - Category/People
  - NPC
  - ritterstadt-npc
obsidianUIMode: preview
aliases: []
NoteStatus: ❓
type: NPC
status: Dead
ancestry: Human (Oeridian)
location: "[[Ritterstadt]]"
occupation: Garrison Soldier
town_role: Second Watch — The Guardhouse
alignment: Neutral
disposition: Cautious
shop: The Guardhouse
founder: false
party_trust: 0
deceased_date: 0576-10-12
char_alignment: Neutral
char_status: Dead
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
  - "[[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]]"
  - "[[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]]"
Connected_Groups: []
---




> [!NOTE|div-m] Parent Location: `INPUT[inlineListSuggester(optionQuery(#Category/Hub),optionQuery(#Category/Region),optionQuery(#Category/Place),optionQuery(#Category/PointofInterest)):MyContainer]`
%% DISPLAYS NOTES THAT MATCH THE TAGS ABOVE %% 

> [!column|no-i no-t]
>> [!div-m|no-title]
>> ![[Ewald_Wennerberg.png]]
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

> [!danger] Deceased — 12 Harvester, 576 CY
> Killed by a gorgon on the descent from the northern pass while travelling under the Ritterstadt Questers' escort during [[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails|0002 — Cold Trails]]. He died first in that fight. The party carried the news and what remained of him back to the garrison. Reported to [[Hauptmann Hildegard Stahlwulf]], who asked that the circumstances — that he was met well off his patrol line and heading north — be held close.
>
> **Everything below the descriptor is a record of the living man.** It is still live material: the party has not learned what he was, and the question of what he was doing on that road is now a *posthumous* investigation. See [[#After His Death]] for how thread **P2** continues without him.

### Character Descriptor
A garrison soldier who gave the impression of being exactly what he appeared to be — which, on a frontier where that is unusual, should itself have been unusual.

### 📝 Appearance
Average height, average build. Brown hair kept short and well-maintained in the manner of military habit. He is clean-shaven when most of the garrison isn't. His uniform is always regulation-correct. His eyes are light grey and move with the controlled sweep of someone who was trained to observe without appearing to. He smiles readily and the smile is real enough that you cannot be certain it isn't.

### 🎭 Mannerisms
Friendly without being forthcoming. Asks questions that seem like small talk but are precise: *"How long were you out past the palisade?" "Which direction did you come in from?"* Volunteers for northern watch rotations without being asked. Disappears on certain nights — not every night, not on a predictable schedule — and returns before the change of watch. If noticed and asked, he says he needed air, couldn't sleep, went to check on something. These are not good explanations but he delivers them without visible concern.

### 💡 Key Motivation
Do the job he was sent here to do. Get out without being identified. These goals have become complicated by the fact that Ritterstadt turned out to be more interesting than his handler anticipated, and by the fact that Vethkar Graun identified him within a fortnight of arriving.

## 🗺️ Town Role & Function

Ewald is the garrison's second watch leader — a competent, reliable soldier who has given Hauptmann Hildegard no cause for concern. He pulls difficult rotations without complaint, handles equipment maintenance with precision, and has a measured, professional manner that reads as military discipline. He is good at his job. This is not incidental.

His actual function — information collection on the University's activities, Ritterstadt's strategic position, and whatever is happening at the Wachturm — is conducted in the margins of his garrison duties and is not visible to any resident of Ritterstadt. Except Vethkar, who was looking for it.

### Known Services / Interactions
| Role | Notes |
| :--- | :--- |
| Garrison watch | Reliable, professional; volunteers for northern exposure |
| Equipment upkeep | Takes this seriously; genuinely good at it |
| Casual conversation | Friendly, measured, asks questions he doesn't explain |

## 💬 Conversation Guide

| Topic | Freely Discussed? | Notes / Sample Line |
| :--- | :--- | :--- |
| Garrison duties, equipment, watch schedules | ✅ | Happy to discuss. Precise. |
| Where he came from | ⚠️ | *"Traft, originally. Did a stint with a private company in the south."* (partially true) |
| The Wachturm | ⚠️ | Expresses appropriate frontier-soldier wariness. *"Old places like that, you leave well alone."* Then asks what prompted the question. |
| His nighttime absences | ❌ | *"Couldn't sleep. Needed air."* Doesn't elaborate. Changes subject with a question. |
| Vethkar Graun | ⚠️ | *"Southerner. You know the type — always asking about who owns what."* Mild, dismissive. Not entirely unconvincing. |
| Whether he's a spy | ❌ | Will not engage with this framing. Politely. |

### 🔑 Trust-Gated Information

> [!note] Historical — for flashback, recollection, and any scene set before 12 Harvester
> He cannot be negotiated with now. Preserved because the party *did* travel with him for four days, and what they remember of those conversations is worth asking them to recall — especially the questions he asked, which they had no reason to find strange at the time.

- **Low Trust (stranger):** Friendly, professional, slightly more curious about you than a random soldier has reason to be.
- **Medium Trust (regular):** The questions become more targeted. He is genuinely skilled at making information-gathering feel like conversation.
- **High Trust / Cornered:** If the party obtains evidence of his activities and presents it, he does not panic. He gets very still, assesses his options for several long seconds, and then asks what they want. He can negotiate. He has information that has value. He is not loyal to his handler to the point of self-destruction.

> [!tip] What the party can still recall (no roll, or DC 10 Intelligence if you want a gate)
> He asked where they had come in from. He asked how long they had been out past the palisade. He asked what the University was doing at the tower. At the time this was a soldier making a march pass quickly. In hindsight it is a debrief.

## 🎯 Quest Hooks

> [!warning] Superseded by his death
> The three original hooks assumed a living man who could be watched, cornered, and turned. He can no longer be any of those. The replacements below deliver the same information through his remains, his effects, and the people who knew what he was.

| Hook | Leads To | Trigger Condition |
| :--- | :--- | :--- |
| His effects are logged at the guardhouse and nobody has read them properly | P2 thread — investigation begun | Party asks after him, or Hildegard asks them to help account for him |
| Vethkar offers his identity — and now has nothing to lose by it | P2 thread — confirmation | Party corners Vethkar with evidence in 0004 |
| The dead-drop is still live, and someone is still checking it | Unknown employer thread | Party back-tracks his route north, ~90 minutes out from the palisade |
| A dispatch he never sent is still on his body or in his kit | Unknown employer thread | Party or Hildegard searches his effects with any care at all |

## 🔗 Relationship Web

| NPC | Relationship Type | Notes |
| :--- | :--- | :--- |
| [[Hauptmann Hildegard Stahlwulf]] | Commanding officer | She trusts him. This is, from her perspective, a significant problem she doesn't know she has. |
| [[Vethkar Graun]] | Mutual knowledge | Vethkar identified him early. Neither has acted on this. It is held information, pending negotiation. |
| [[Ritter Konrad von Eisfeld]] | Employer (indirect) | Works for the garrison Konrad funds. Konrad has no reason to suspect him. |

# Statblock

```statblock
monster: Spy
```
%% Suggested SRD block for an embedded agent posing as a soldier. Adjust to taste. %%

# GM Notes

> [!danger] DM Eyes Only

## 🕵️ Secrets & Hidden Motivations

### The Real Story
Ewald is a foreign agent embedded in Ritterstadt's garrison. He arrived approximately three months ago with a plausible military background, arranged through a contact in Traft. **Who he works for is deliberately not specified at this stage** — his handler's identity and the organization behind him are a long-form mystery thread that should not be resolved early. Candidates include: Wolf Nomad political faction seeking intelligence on the University's land claim; a rival mercantile consortium to the Hanselmann group; an agent of Iuz's cult mapping the Fiend's Embrace situation; a Perrenlander intelligence operation that Perrenland would officially deny. The DM should choose or leave open based on campaign direction.

What is known: he goes north. He has a specific dead-drop site or contact point roughly 90 minutes out from the palisade. He has sent at least three dispatches since arriving. The content of those dispatches includes accurate information about the University's expedition structure, the Fiend's Rest job board, Ritter Konrad's financial difficulties, and the existence of the Wachturm as a point of unusual interest.

### What He Knows (But Won't Share)
- The identity of his handler and the dead-drop site
- What he has already transmitted
- His real name (Ewald Wennerberg may or may not be accurate)

### What He Fears
Being identified before he completes his assignment. Vethkar Graun. The party being more competent than he expected.

### What He'll Trade
If cornered with real evidence, Ewald is pragmatic. He can offer: his handler's identity, the dead-drop location, the content of his dispatches, and — if he likes his odds with the party better than his odds with his handler — his services as a double agent. He will not martyr himself for an employer he was paid to work for.

### Vethkar's Angle
Vethkar identified Ewald within two weeks. He has held this information as leverage against both Ewald (compliance) and the village (a card to play if negotiations over Konrad's debt become difficult). He will offer Ewald's identity to the party during **0004** if cornered — as proof of goodwill and as a way to redirect their attention to a more dangerous problem than a debt collector.

**His death changes the price, not the offer.** Vethkar's leverage over *Ewald* is gone; his leverage over the *village* is sharper than ever, because the thing he knows is now unfalsifiable by the only man who could have denied it. He gives it up more readily and enjoys doing it: *"Your garrison's second watch was selling you by the fortnight. He's dead, so you'll have to take my word — and you'll notice I'm the only one here who ever told you the truth about anything."*

## 💀 After His Death

> [!danger] Thread P2 continues — it does not close
> The reveal was never really about cornering Ewald. It was about the party learning that Ritterstadt is being *read* by someone outside it. A corpse delivers that as well as a confession does, and it removes the escape hatch where a clever party turns him and the mystery becomes a manageable asset. Play his death as having made the thread **harder**, not finished.

**Where the evidence now sits:**

| Evidence | Where it is | How it surfaces |
| :--- | :--- | :--- |
| His kit and personal effects | Guardhouse, in Hildegard's custody, unexamined | She has no reason to suspect anything and every reason to be gentle with a dead soldier's things. She will let the party help account for them, or ask them to. |
| An undelivered dispatch | On his body, or sewn into the kit | Anyone who searches with care. Written in a hand and a shorthand no one in Ritterstadt reads. |
| The dead-drop | ~90 minutes north of the palisade, off his patrol line | Back-tracking the route he was on when the party met him. **Still being serviced** — see below. |
| Three dispatches already sent | Gone, in someone else's hands | Recoverable only at the far end of the chain; not in Ritterstadt. |
| His real name and handler | Died with him | Never confirmable from his own mouth. Deliberately still open. |

**The handler does not know he's dead.** This is the useful part. Someone continues to check the drop on schedule, finds nothing, and escalates — first by waiting, then by coming to look. That gives you a live, escalating clock that costs the party nothing to trigger and everything to ignore:

1. **Weeks 1–2.** The drop is serviced and empty. No visible change in Ritterstadt.
2. **Weeks 3–4.** A stranger asks careless questions at the [[The Fiend's Rest Public House|Fiend's Rest]] about the garrison's rotations. Not skilled. Not the same calibre as Ewald.
3. **Beyond.** A replacement arrives, or a cleaner does. A replacement is a new NPC to unmask. A cleaner is a threat, and will want to know who searched the body.

> [!tip] Whether to leave the drop live
> If you would rather not run the clock, the simplest close is that the drop is serviced once, found empty, and abandoned — the handler assumes Ewald was burned and cuts the line. The party can still find the site, cold, and read the *fact* of it: someone was being paid to watch them, and that someone is careful enough to know when to vanish. That is a complete beat on its own.

**The suspicion problem.** If the party makes his espionage public, they retroactively poison a death the garrison is currently mourning cleanly, and they do it on the word of Vethkar Graun. Hildegard trusted Ewald. She will not enjoy being right to have done so and wrong to have kept doing it, and she will want proof before she lets the party rewrite one of her soldiers. This is the scene the thread was always building toward; his death just means she is defending a memory instead of a man.

> [!warning] What not to do with this
> Do not let the party conclude the gorgon was sent, or that his death was arranged. It was a random beast on a descent, and the campaign is better for the frontier occasionally killing someone important by accident. The horror in this thread is administrative, not supernatural: a man was spying on them, he died of something unrelated, and the machine he was part of has not noticed yet.

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
