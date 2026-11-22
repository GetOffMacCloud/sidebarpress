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

# {{faction}}

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
| Sub-faction | Wants | Relation to the main body |
|---|---|---|
| | | |

## GM Notes
