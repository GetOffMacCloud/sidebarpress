---
type: hub
section: internal
publish: false
tags: [hub, homebrew, mechanics]
---

# Rules and Mechanics

House subsystems for Sidebar Press, built on the **2014 rules**. One note per subsystem, with natural names (e.g. `The Price of Power.md`).

Frontmatter on every note: `type: mechanic`, `subsystem`, `scope`, `rules_base`, `canon_status`, `status` (outline → drafted → edited → final), `publish`.

```dataview
TABLE subsystem AS "Subsystem", scope AS "Scope", rules_base AS "Rules", status AS "Status"
FROM "56-Rules-and-Mechanics"
WHERE type = "mechanic"
SORT file.name ASC
```
