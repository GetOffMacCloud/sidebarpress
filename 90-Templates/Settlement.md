---
type: settlement
adventure: "SP-GANN"
section: act-1
publish_order: 150
publish: true
status: outline
canon: false
category: "" # City +1500 | Town +200 | Village +80 | Hamlet <80 | Encampment | Keep | Fortress | Stronghold
region: "" # link to the Region note
sovereignty: "" # who rules it
population: ""
population_mix: [] # human, dwarf, gnome, elf, halfling, other
capital: false
threat_level: 2 # 1–5
economic_stability: "" # thriving | stable | strained | failing
influencers: [] # churches, guilds, factions (links to Faction notes)
in_world_date: "576 CY"
aliases: []
---
<%*
// Sidebar Press world-note setup (Templater). Runs when the note is made from a Meta Bind button or Templater.
const isNew = /^(New|Untitled)/.test(tp.file.title);
let name = tp.file.title;
if (isNew) {
  name = await tp.system.prompt("Settlement name", "");
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
  const cats = ["City +1500", "Town +200", "Village +80", "Hamlet <80", "Encampment", "Keep", "Fortress", "Stronghold"];
  const category = await tp.system.suggester(cats, cats, false, "What kind of settlement?") ?? "";
  const region = await pick("Which region is it in?", ["region"], ["20-World/Regions", "20-World/Greyhawk-Canon"]);
  setFM({ category, region });
}
%>

# <%* tR += name %>

> One line: what kind of place this is, and what the party will come back here for.

> [!abstract]- Quick edit (Meta Bind)
> Category `INPUT[template-hub-category][:category]` · Threat `INPUT[template-threat-level][:threat_level]` · Economy `INPUT[template-settlement-economy][:economic_stability]` · Capital `INPUT[toggle:capital]`
> Region `INPUT[suggester(optionQuery("20-World/Regions"), optionQuery("20-World/Greyhawk-Canon")):region]` · Sovereignty `INPUT[text:sovereignty]` · Population `INPUT[text:population]`
> Population mix `INPUT[inlineList:population_mix]` · Influencers `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew"), optionQuery("20-World/Greyhawk-Canon")):influencers]`

## At a Glance
Population and makeup · who rules · temples · coin · what the place is known for · threat level · economy.

## Arrival
The gate or dock scene: who challenges the party, what they ask, where they send them by how they look.

> *Read-aloud for the first view.*

## Settlement Key
| # | Building | Occupants | Faith | Attitude | Full entry |
|---|---|---|---|---|---|
| 1 | | | [ ] | | * |

Unkeyed houses: one blanket rule.

### 1. BUILDING AS THE PLAYERS SEE IT
- **Who:** name [Deity], trade · one line of manner
- **Knows:**
- **Secret:**
- **Hidden cache:**
- **Will adventure?**
- **Rooms:** (communal / semi-private / private; Overlooks:)

## Districts (CAMPING)
`BUTTON[button_place]` `BUTTON[button_person]`
Sort the places of the settlement by what they do. Each Location note with `kind: place`, `parent_location` set to this settlement and a `category` shows up below.
- **C**ommerce: shops, markets, theaters · **A**griculture: farms, mines, fisheries, lumber · **M**ilitary: forts, walls, armories, docks · **P**hilosophy: temples, schools, libraries · **I**ndustrial: smiths, mills, bakers, artisans · **N**esting: houses, inns, bridges, parks · **G**overnment: halls, courts, monuments

```dataview
TABLE WITHOUT ID file.link AS "Place", category AS "District"
FROM "40-Locations"
WHERE kind = "place" AND contains(string(parent_location), this.file.name)
SORT category ASC, file.name ASC
```

## People
`BUTTON[button_person]`
NPC notes whose `location` is this settlement.

```dataview
TABLE WITHOUT ID file.link AS "Name", occupation AS "Trade", faction AS "Faction"
FROM "30-NPCs" WHERE contains(string(location), this.file.name)
SORT file.name ASC
```

## Information Carriers
Who knows what, and who sends the party to whom.
| Resident | Knows | Points to |
|---|---|---|
| | | |

## Hidden Hands
The two or three spies or cultists among ordinary folk, how they report, and their tell.

## Prices and Texture
Inn menu, prices, local coin, a posted notice.

## Travel
| Destination | Miles | Days on foot (24 mi/day) | Days mounted (48 mi/day) |
|---|---|---|---|
| [[Next town]] | | | |

## Between Forays
What changes in town each time the party returns.
- Visit 2:
- Visit 3:

## GM Notes
What you need to track here between sessions.

## Map Reference
Settlement map in `99-Assets`; FG map name.
