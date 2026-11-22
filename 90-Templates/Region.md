---
type: region
canon: false
parent: "" # the continent or larger realm, as a link
climate: ""
seasons: ""
dominant_peoples: []
sovereignty: "" # who rules it in 576 CY
aliases: []
tags: [region]
---
<%*
// Sidebar Press world-note setup (Templater). Runs when the note is made from a Meta Bind button or Templater.
const isNew = /^(New|Untitled)/.test(tp.file.title);
let name = tp.file.title;
if (isNew) {
  name = await tp.system.prompt("Region name", "");
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
  const parent = await pick("Which continent or realm is it part of?", ["continent", "region"], []);
  setFM({ parent });
}
%>

# <%* tR += name %>

> One line: the land, who holds it, and what it's like to travel through.

> [!abstract]- Quick edit (Meta Bind)
> Part of `INPUT[suggester(optionQuery("20-World/Continents"), optionQuery("20-World/Regions")):parent]` · Ruled by `INPUT[text:sovereignty]`
> Climate `INPUT[text:climate]` · Seasons `INPUT[text:seasons]` · Peoples `INPUT[inlineList:dominant_peoples]`

## General
The region's description. Lead with what a traveler notices, not a gazetteer.

## Details
- **Dominant peoples:**
- **Climate and seasons:**
- **Rulers and powers:**
- **Coin, faiths, customs:**

## Hubs
`BUTTON[button_hub]`
Places where people live: cities, towns, villages, hamlets, encampments, keeps (any `type: settlement` note with `region` set to this region).

```dataview
TABLE WITHOUT ID file.link AS "Hub", category AS "Type", population AS "Population"
FROM ""
WHERE type = "settlement" AND contains(string(region), this.file.name)
SORT file.name ASC
```

## Points of Interest
`BUTTON[button_pointofinterest]`
Places that can be explored (any `type: location` note with `region` set to this region).

```dataview
TABLE WITHOUT ID file.link AS "Place", kind AS "Kind", category AS "Category"
FROM ""
WHERE type = "location" AND contains(string(region), this.file.name)
SORT file.name ASC
```

## Groups
`BUTTON[button_group]`
Groups of people and power: churches, cults, guilds, companies (any `type: faction` note with `territory` set to this region).

```dataview
LIST FROM "" WHERE type = "faction" AND contains(string(territory), this.file.name)
```

## Quests
`BUTTON[button_quest]`
```dataview
TABLE WITHOUT ID file.link AS "Quest", status AS "Status", giver AS "Giver"
FROM "" WHERE type = "quest" AND contains(string(location), this.file.name)
```

## GM Notes
What you need to track in the region.

## Adventure Use
- [[SP-GANN-Title]] — how it's used

## Canon Notes
Edition, book and page; deviations marked *(homebrew)*. If the region is canon, link its Lore note in `20-World/Greyhawk-Canon` instead of duplicating it.
