---
type: hub
section: internal
publish: false
tags: [hub, homebrew, classes, subclasses]
---

# Classes and Subclasses

Homebrew classes and subclasses for Sidebar Press, built on the **2014 rules**. One note per class or subclass, named `Class — Subclass.md` (e.g. `Wizard — School of Cruormancy.md`) so they sort by class. A new homebrew class gets `Class.md`.

Frontmatter on every note: `type` (`class` | `subclass`), `class`, `subclass`, `rules_base`, `canon_status`, `dm_approval`, `status` (outline → drafted → edited → final), `publish`.

```dataview
TABLE class AS "Class", subclass AS "Subclass", rules_base AS "Rules", dm_approval AS "DM approval", status AS "Status"
FROM "55-Classes-and-Subclasses"
WHERE type = "class" OR type = "subclass"
SORT class ASC, subclass ASC
```
