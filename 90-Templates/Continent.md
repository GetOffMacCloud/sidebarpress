---
type: continent
canon: false
aliases: []
tags: [continent]
---
<%*
// Sidebar Press world-note setup (Templater). Runs when the note is made from a Meta Bind button or Templater.
const isNew = /^(New|Untitled)/.test(tp.file.title);
let name = tp.file.title;
if (isNew) {
  name = await tp.system.prompt("Continent name", "");
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

> One line: what this landmass is and why it matters to the campaign.

## General
The continent's description: shape, peoples, what everyone knows about it.

## Details
- **Dominant peoples:**
- **Climate:**
- **Great powers:**

## Regions
`BUTTON[button_region]`
Regions on this continent (any note with `type: region` and `parent: "[[{{continent}}]]"`).

```dataview
TABLE WITHOUT ID file.link AS "Region", climate AS "Climate", dominant_peoples AS "Peoples"
FROM ""
WHERE type = "region" AND contains(string(parent), this.file.name)
SORT file.name ASC
```

## Capital Cities
Settlements flagged as capitals in this continent's regions.

```dataview
TABLE WITHOUT ID file.link AS "City", region AS "Region", population AS "Population"
FROM ""
WHERE type = "settlement" AND capital = true
SORT file.name ASC
```

## GM Notes
What you need to track at continent scale.

## Canon Notes
Edition, book and page for anything canon; deviations marked *(homebrew)*. Link Lore notes in `20-World/Greyhawk-Canon`.
