---
type: item
rarity: "" # common | uncommon | rare | very rare | legendary | artifact
canon: false
item_type: "" # weapon | armor | wondrous | potion | scroll | wand | ring | gear | treasure
cost: ""
weight: ""
attunement: false
aliases: []
connected_quests: []
connected_groups: []
tags: []
---
<%*
// Sidebar Press world-note setup (Templater). Runs when the note is made from a Meta Bind button or Templater.
const isNew = /^(New|Untitled)/.test(tp.file.title);
let name = tp.file.title;
if (isNew) {
  name = await tp.system.prompt("Item name", "");
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

> One-line description.

> [!abstract]- Quick edit (Meta Bind)
> Rarity `INPUT[template-item-rarity][:rarity]` · Type `INPUT[template-item-type][:item_type]` · Attunement `INPUT[toggle:attunement]`
> Cost `INPUT[text:cost]` · Weight `INPUT[text:weight]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions")):connected_groups]`

*Source:* (book and page, or homebrew)

## Properties
2014 5e mechanics. Attunement, charges, etc.
- **Activate:** how it's used.
- **Frequency:** how often.
- **Trigger:** what sets it off, if anything.
- **Effect:** what happens.

## History
Where it came from. Canon cited or homebrew marked.

## Found In
- [[SP-GANN-Title]] — location/context

## Carried By
NPC notes that list this item in `items`.

```dataview
LIST FROM "30-NPCs" WHERE contains(items, this.file.link)
```

## GM Notes
Secrets, curses, what the owner doesn't know.

## Continuity
Does this item matter beyond its adventure? Cursed? Sought by a faction?
