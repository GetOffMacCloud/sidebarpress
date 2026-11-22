---
type: location
canon: false
kind: place # place (a building or business in a settlement) | point-of-interest (somewhere to explore) | site (a keyed dungeon or lair) | landmark
category: "" # place: Commerce | Agriculture | Military | Philosophy | Industrial | Nesting | Government · point-of-interest: Encounter | Ruins | Dungeon | Landmark | Lair | Cave | Shrine | Temple | Tomb | Barrow | Battlefield | Mine | Tower | Camp | Crossing | Waystation | Wreck | Grove | Standing Stones | Hazard | Portal
region: ""
parent_location: "" # link to the Settlement or Region it sits in
aliases: []
tags: []
---
<%*
// Sidebar Press world-note setup (Templater). Runs when the note is made from a Meta Bind button or Templater.
const isNew = /^(New|Untitled)/.test(tp.file.title);
let name = tp.file.title;
if (isNew) {
  name = await tp.system.prompt("Place name", "");
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
  let kind = tp.file.title.startsWith("NewPOI") ? "point-of-interest" : (tp.file.title.startsWith("NewPlace") ? "place" : null);
  if (!kind) kind = await tp.system.suggester(["place", "point-of-interest", "site", "landmark"], ["place", "point-of-interest", "site", "landmark"], false, "What kind of location?");
  const cats = kind === "place" ? ["Commerce", "Agriculture", "Military", "Philosophy", "Industrial", "Nesting", "Government"] : ["Encounter", "Ruins", "Dungeon", "Landmark", "Lair", "Cave", "Shrine", "Temple", "Tomb", "Barrow", "Battlefield", "Mine", "Tower", "Camp", "Crossing", "Waystation", "Wreck", "Grove", "Standing Stones", "Hazard", "Portal"];
  const category = await tp.system.suggester(cats, cats, false, "Category") ?? "";
  const parent_location = await pick("Which settlement or region is it in?", ["settlement", "region", "location"], ["20-World/Regions"]);
  setFM({ kind: kind ?? "place", category, parent_location });
}
%>

# <%* tR += name %>

> One-line description.

> [!abstract]- Quick edit (Meta Bind)
> Kind `INPUT[template-location-kind][:kind]` · Place district `INPUT[template-place-category][:category]` · Point-of-interest type `INPUT[template-poi-type][:category]`
> In `INPUT[suggester(optionQuery("40-Locations"), optionQuery("20-World/Regions")):parent_location]` · Region `INPUT[suggester(optionQuery("20-World/Regions"), optionQuery("20-World/Greyhawk-Canon")):region]`

## Description
What the PCs see, hear, smell. Boxed text goes here.

## Notable Features
## Inhabitants
`BUTTON[button_person]`
- [[NPC Name]]

NPC notes whose `location` is this place:

```dataview
TABLE WITHOUT ID file.link AS "Name", occupation AS "Occupation", status AS "Status"
FROM "30-NPCs" WHERE contains(string(location), this.file.name)
SORT file.name ASC
```

## History
Canon history linked; homebrew history marked.

## Business (places only; delete otherwise)
**Selling**
| Item | Cost | Weight |
|---|---|---|
| | | |

**Buying**
| Item | Pays | Notes |
|---|---|---|
| | | |

**Services**
| Service | Cost | Notes |
|---|---|---|
| | | |

## Exploring (points of interest only; delete otherwise)
`BUTTON[button_quest]`
- **Approach:** what the party sees before they arrive.
- **Interior / areas:** short subsections, or a link to a [[Site-Key]] note.
- **Encounter:** creatures here (count), and the bestiary note.
- **Quests tied here:**

## Travel
| Destination | Miles | Days on foot (24 mi/day) | Days mounted (48 mi/day) |
|---|---|---|---|
| [[Next place]] | | | |

## Rumors
What the party might overhear here.

## GM Notes

## Adventure Use
- [[SP-GANN-Title]] — how it's used

## Map Reference
Link to asset in `99-Assets`, or FG map name.

## Canon Notes
Edition/book/page citations. Deviations documented.
