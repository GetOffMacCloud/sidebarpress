---
type: session-log
date: "" # real-world date played
adventure: ""
session: 1
in_world_date: "" # CY
one_liner: ""
players: 0
roster: []
absent: []
status: played # planned | played | cancelled
tags: []
---
<%*
// Sidebar Press world-note setup (Templater). Runs when the note is made from a Meta Bind button or Templater.
const isNew = /^(New|Untitled)/.test(tp.file.title);
let name = tp.file.title;
if (isNew) {
  name = await tp.system.prompt("Session note name (e.g. SP-GS02 Session 1)", "");
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

# Session {{n}} — [[Adventure]]

> One-line summary.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-session-status][:status]` · Played `INPUT[datePicker:date]` · In-world `INPUT[text:in_world_date]` · Players `INPUT[number:players]`
> Roster `INPUT[inlineList:roster]` · Absent `INPUT[inlineList:absent]`
> One-liner `INPUT[text:one_liner]`

## Date Played
Real-world date.

## In-World Date
Greyhawk reckoning (e.g. 12 Goodmonth, 576 CY).

## Roster
- **Present:**
- **Absent:**

## Summary
What happened, briefly.

## Player Decisions
Choices that could affect continuity. These feed plot threads.

## Deviations
Where the table went off the written adventure. Flag anything that changes canon or planned continuity.

## Follow-ups
- [ ] Update [[Plot-Threads]] with outcome
- [ ] Update NPC status (and Player Log) if changed
- [ ] Update quest status
