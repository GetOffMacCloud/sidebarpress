---
type: npc
status: alive # alive | dead | missing | unknown
canon: false
faction: ""
location: "" # link to the Settlement or Location note where they live
aliases: []
species: "" # broad race: Human, Elf, Dwarf, Gnome, Halfling, Half-Elf, Half-Orc, Goliath, Other
heritage: "" # Race — heritage (e.g. Elf — Grey (Faerie)); blank for Half-Elf, Half-Orc
gender: ""
age: "" # Infant | Child | Teenager | Young Adult | Adult | Elder
alignment: "" # Lawful Good … Chaotic Evil, Unaligned
occupation: ""
class: "" # PC-style class, or None (NPC)
subclass: "" # Class — Subclass
prestige_class: ""
level: ""
adventure_role: "" # ally | patron | rival | villain | informant | color
disposition: neutral # friendly | neutral | wary | hostile
party_trust: 0 # 0 stranger · 1 regular · 2 friend
items: [] # links to Item notes
connected_quests: [] # links to Quest notes
connected_groups: [] # links to Faction notes
parents: []
partner: []
children: []
siblings: []
allies: []
enemies: []
deceased_date: "" # CY
tags: []
---
<%*
// Sidebar Press world-note setup (Templater). Runs when the note is made from a Meta Bind button or Templater.
const isNew = /^(New|Untitled)/.test(tp.file.title);
let name = tp.file.title;
if (isNew) {
  name = await tp.system.prompt("Person's name", "");
  if (!name) { new Notice("No name entered; note left as " + tp.file.title + "."); name = tp.file.title; }
  else { await tp.file.rename(name); }
}
const pick = async (label, types, folders) => {
  const files = app.vault.getMarkdownFiles().filter(f => {
    const fm = app.metadataCache.getFileCache(f)?.frontmatter;
    return (fm && types.includes(fm.type)) || folders.some(d => f.path.startsWith(d + "/"));
  }).sort((a, b) => a.basename.localeCompare(b.basename));
  const choice = await tp.system.suggester(["— none —", ...files.map(f => f.basename)], [null, ...files], false, label);
  return choice ? "[[" + choice.basename + "]]" : "";
};
const setFM = (obj) => setTimeout(() => {
  const f = tp.file.find_tfile(tp.file.path(true));
  if (f) app.fileManager.processFrontMatter(f, fm => Object.assign(fm, obj));
}, 300);
if (isNew) {
  const location = await pick("Where do they live?", ["settlement", "location"], []);
  setFM({ location });
}
%>

# <%* tR += name %>

> One-line identity: who they are at a glance, the impression they leave on the party.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
One or two physical details that are easy to recall and describe at the table.

## Personality & Mannerisms
How they talk, move and behave. Habits, tics, tells.

## Goals & Secrets
- **Wants (publicly):** what they want the party to believe about them.
- **The real story:** what's actually going on beneath the surface.
- **Knows but won't say:**
- **Fears:**
- **How to reveal it:** the condition or trigger that makes them open up.

## Role & Context
What purpose they serve in the adventure, and what would break if they were gone. How they connect to the larger campaign.

## Conversation Guide
| Topic | Freely discussed? | Notes / sample line |
|---|:---:|---|
| The current hook | | |
| The local area | | |
| Their faction or group | | |
| Other NPCs they know | | |
| Personal history | | |

**Trust-gated information:**
- **Stranger (0):** what a newcomer gets.
- **Regular (1):** what they share after a few genuine interactions.
- **Friend (2):** what only a trusted party hears.

## Services
| Service | Cost / notes |
|---|---|
| | |

## Quest Hooks
| Hook | Leads to | Trigger |
|---|---|---|
| | | |

## Relationships
`BUTTON[button_person]`

| Parents | Partner | Children |
|---|---|---|
| `INPUT[inlineListSuggester(optionQuery("30-NPCs")):parents]` | `INPUT[inlineListSuggester(optionQuery("30-NPCs")):partner]` | `INPUT[inlineListSuggester(optionQuery("30-NPCs")):children]` |

| Siblings | Allies | Enemies |
|---|---|---|
| `INPUT[inlineListSuggester(optionQuery("30-NPCs")):siblings]` | `INPUT[inlineListSuggester(optionQuery("30-NPCs"), optionQuery("20-World/Factions")):allies]` | `INPUT[inlineListSuggester(optionQuery("30-NPCs"), optionQuery("20-World/Factions")):enemies]` |

Fill the frontmatter lists (parents, partner, children, siblings, allies, enemies) with links; they show here.

```dataview
TABLE WITHOUT ID parents AS "Parents", partner AS "Partner", children AS "Children", siblings AS "Siblings", allies AS "Allies", enemies AS "Enemies"
WHERE file.path = this.file.path
```

| NPC | Relationship | Notes |
|---|---|---|
| | | |

## Inventory
`BUTTON[button_item]`
Items they carry (frontmatter `items`).

```dataview
LIST FROM "50-Items" WHERE contains(this.items, file.link)
```

## Stat Block
Link or reference: 2014 5e stat block used, or custom block location.

## Appearances
Adventures/sessions where they show up:
- [[SP-GANN-Title]] — scenes

## Player Log
Fill in after each session where this NPC appears.

| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
If `canon: true`, cite edition/book/page. If homebrew inspired by canon, link the source.

## Continuity
What threads are they tied to? What happens to them if the PCs ignore them?
