---
type: faction
adventure: "SP-GANN"
section: internal
publish_order: 0
publish: false
canon: false
category: "" # church | cult | guild | company | noble house | order | gang
alignment: ""
deity: "" # [Deity]
territory: "" # link to the Region or Settlement it operates in
status: active # active | covert | destroyed | defunct
founded: "" # CY
leader: "" # link
officers: []
members: []
initiates: []
primary_contact: "" # link
allies: []
enemies: []
aliases: []
---
<%*
// Sidebar Press world-note setup (Templater). Runs when the note is made from a Meta Bind button or Templater.
const isNew = /^(New|Untitled)/.test(tp.file.title);
let name = tp.file.title;
if (isNew) {
  name = await tp.system.prompt("Group name", "");
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
  const territory = await pick("Where do they operate?", ["region", "settlement"], ["20-World/Regions", "20-World/Greyhawk-Canon"]);
  setFM({ territory });
}
%>

# <%* tR += name %>

> [!abstract]- Quick edit (Meta Bind)
> Category `INPUT[template-group-type][:category]` · Status `INPUT[template-faction-status][:status]` · Alignment `INPUT[template-npc-alignment][:alignment]` · Deity `INPUT[text:deity]` · Founded `INPUT[text:founded]`
> Territory `INPUT[suggester(optionQuery("20-World/Regions"), optionQuery("40-Locations"), optionQuery("20-World/Greyhawk-Canon")):territory]` · Leader `INPUT[suggester(optionQuery("30-NPCs")):leader]` · Contact `INPUT[suggester(optionQuery("30-NPCs")):primary_contact]`
> Officers `INPUT[inlineListSuggester(optionQuery("30-NPCs")):officers]` · Members `INPUT[inlineListSuggester(optionQuery("30-NPCs")):members]` · Initiates `INPUT[inlineListSuggester(optionQuery("30-NPCs")):initiates]`
> Allies `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("30-NPCs")):allies]` · Enemies `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("30-NPCs")):enemies]`

**Wants** ___, **hopes to** ___.

- **Leader:** [[NPC]]
- **Members:** (count), where they are
- **Recognition sign or tell:**
- **Spies on:** · **Spied on by:**
- **Allies / rivals:**
- **If the party helps them:**
- **If the party crosses them:**
- **Succession:** who takes over if the leader falls, and how the deal changes.
- **What they do if nobody interferes:**

## Overview
Purpose, values, reach. Alignment, deity, territory, status.

## Goals
## Hierarchy
Leader → officers → members → initiates (frontmatter lists).

```dataview
TABLE WITHOUT ID leader AS "Leader", officers AS "Officers", members AS "Members", initiates AS "Initiates"
WHERE file.path = this.file.path
```

## People
`BUTTON[button_person]`
NPC notes whose `faction` or `connected_groups` names this faction.

```dataview
TABLE WITHOUT ID file.link AS "Name", occupation AS "Role", location AS "Location"
FROM "30-NPCs"
WHERE contains(string(faction), this.file.name) OR contains(string(connected_groups), this.file.name)
SORT file.name ASC
```

## Membership and Standing
**To join:** what a PC must do (and for how long).

| Standing | Title | Benefit |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |

## Services
What members (or paying outsiders) can get from them.

## History
The group's rise, fall and present, with CY dates.

## Sub-Factions
`BUTTON[button_group]`
| Sub-faction | Wants | Relation to the main body |
|---|---|---|
| | | |

## GM Notes
