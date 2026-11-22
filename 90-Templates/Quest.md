---
type: quest
status: not-started # not-started | in-progress | complete | failed | abandoned
giver: "" # link to an NPC note
location: "" # where the quest was given (link)
obtained: "" # in-world date (CY)
session_obtained: "" # link to a session log
loot_available: []
loot_earned: []
adventure: "" # SP-GANN, if it belongs to one
tags: [quest]
---
<%*
// Sidebar Press world-note setup (Templater). Runs when the note is made from a Meta Bind button or Templater.
const isNew = /^(New|Untitled)/.test(tp.file.title);
let name = tp.file.title;
if (isNew) {
  name = await tp.system.prompt("Quest name", "");
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
  const giver = await pick("Who gave the quest?", ["npc"], ["30-NPCs"]);
  setFM({ giver });
}
%>

# <%* tR += name %>

> One line: what the party has been asked to do, and by whom.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-quest-status][:status]` · Giver `INPUT[suggester(optionQuery("30-NPCs")):giver]` · Where `INPUT[suggester(optionQuery("40-Locations")):location]`
> Obtained (CY) `INPUT[text:obtained]` · Session `INPUT[suggester(optionQuery("80-Sessions")):session_obtained]`
> Loot available `INPUT[inlineListSuggester(optionQuery("50-Items")):loot_available]` · Loot earned `INPUT[inlineListSuggester(optionQuery("50-Items")):loot_earned]`

## Quest Info
- [ ] Obtain the quest
- [ ] ___
- [ ] Complete the quest
- [ ] Collect the reward

## Details
- **Giver:** · **Where:** · **When (CY):** · **Session:**
- **Reward offered:** · **Reward earned:**

## Backstory
Why it matters, and why the party should care.

## Planning
How it might play out: routes, people to meet, places to go.

## People
`BUTTON[button_person]`
NPC notes that link to this quest (`connected_quests`).

```dataview
TABLE WITHOUT ID file.link AS "Name", occupation AS "Role", location AS "Location"
FROM "30-NPCs" WHERE contains(string(connected_quests), this.file.name)
```

## GM Notes

## Continuity
Plot threads it opens or advances: [[Plot-Threads]].
