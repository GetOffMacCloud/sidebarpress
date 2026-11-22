---
type: settlement
adventure: "SP-GANN"
section: act-1
publish_order: 150
publish: true
status: outline
canon: false
category: "" # city 1,500+ | town 200+ | village 80+ | hamlet under 80 | encampment | keep | fortress | stronghold
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

# {{settlement}}

> One line: what kind of place this is, and what the party will come back here for.

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
Sort the places of the settlement by what they do. Each Location note with `kind: place`, `parent_location` set to this settlement and a `category` shows up below.
- **C**ommerce: shops, markets, theaters · **A**griculture: farms, mines, fisheries, lumber · **M**ilitary: forts, walls, armories, docks · **P**hilosophy: temples, schools, libraries · **I**ndustrial: smiths, mills, bakers, artisans · **N**esting: houses, inns, bridges, parks · **G**overnment: halls, courts, monuments

```dataview
TABLE WITHOUT ID file.link AS "Place", category AS "District"
FROM "40-Locations"
WHERE kind = "place" AND contains(string(parent_location), this.file.name)
SORT category ASC, file.name ASC
```

## People
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
