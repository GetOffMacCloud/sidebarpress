---
type: species
canon: false
species_type: "" # humanoid | fey | giant | monstrosity | …
typical_alignment: ""
languages: []
lifespan: ""
adulthood: ""
avg_height: ""
avg_weight: ""
homelands: [] # links to Region notes
aliases: []
tags: [species]
---
<%*
// Sidebar Press world-note setup (Templater). Runs when the note is made from a Meta Bind button or Templater.
const isNew = /^(New|Untitled)/.test(tp.file.title);
let name = tp.file.title;
if (isNew) {
  name = await tp.system.prompt("Species name", "");
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

%>

# <%* tR += name %>

> One line: who they are, and their reputation among the peoples of the Flanaess.

> [!abstract]- Quick edit (Meta Bind)
> Type `INPUT[text:species_type]` · Typical alignment `INPUT[template-npc-alignment][:typical_alignment]` · Languages `INPUT[inlineList:languages]`
> Lifespan `INPUT[text:lifespan]` · Adulthood `INPUT[text:adulthood]` · Height `INPUT[text:avg_height]` · Weight `INPUT[text:avg_weight]`
> Homelands `INPUT[inlineListSuggester(optionQuery("20-World/Regions"), optionQuery("20-World/Greyhawk-Canon")):homelands]`

## Overview
Origin, role in the world, reputation.
- **Species type:** · **Typical alignment:** · **Languages:**

## Physiology
What they look like and what sets them apart.
- **Lifespan:** · **Adulthood:** · **Height:** · **Weight:**
- **Distinguishing features:**
- **Senses:**
- **Strengths:** · **Weaknesses:**

## Culture
- **Society:**
- **Religions and deities:** [Deity]
- **Traditions and customs:**
- **Attitude toward outsiders:**

## Distribution
- **Homelands:**
- **Population density:** rare / uncommon / common / dominant
- **Typical settlements:**

## Relations
| Species | Relationship | Notes |
|---|---|---|
| | | |

## Mechanics (2014 5e)
- **Size:** · **Speed:** · **Darkvision:**
- **Special abilities:**
- **Stat block:** 2014 block name, or a bestiary note.

## Notable Members
`BUTTON[button_person]`
NPC notes whose `species` is this species.

```dataview
TABLE WITHOUT ID file.link AS "Name", occupation AS "Occupation", location AS "Location"
FROM "30-NPCs" WHERE contains(string(species), this.file.name)
SORT file.name ASC
```

## GM Notes
What the party doesn't know yet.

## Canon Notes
Edition, book and page; deviations marked *(homebrew)*. No 5.5e sources.
