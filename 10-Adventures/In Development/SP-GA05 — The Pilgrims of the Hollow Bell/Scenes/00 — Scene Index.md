---
type: scene-index
adventure: SP-GA05
section: internal
publish_order: 0
publish: false
longform:
  format: scenes
  title: The Pilgrims of the Hollow Bell
  workflow: Default Workflow
  sceneFolder: /
  scenes: []
  ignoredFiles:
    - 00 — Scene Index
---
# Scene Index — The Pilgrims of the Hollow Bell

Back to [[SP-GA05-The-Pilgrims-of-the-Hollow-Bell]] · Statblocks: [[SP-GA05 — Bestiary]] · Board: [[SP-GA05 — Board]]

> [!info] This note is the **build manifest**. Reorder by changing `publish_order`; drop a file with `publish: false`. See [[Build-Pipeline]].

> [!warning] Longform can't compile this adventure
> SP-GA05 was written as one main note plus four encounter notes, not as scene files, so the Longform scene list is empty on purpose. The manuscript is compiled by `FGU Kit/build/compile.py`, which writes [[SP-GA05 — Compiled]] in the order below.

## Build Manifest

```dataview
TABLE WITHOUT ID
  file.link AS "File",
  section AS "Section",
  publish_order AS "Order",
  default(status, "—") AS "Status",
  choice(publish, "✅", "—") AS "Ships"
FROM "10-Adventures/In Development/SP-GA05 — The Pilgrims of the Hollow Bell" OR "65-Bestiary/SP-GA05"
WHERE adventure = "SP-GA05" AND publish_order > 0
SORT publish_order ASC
```

## Compile Order (what `compile.py` assembles)

| # | Part | Source |
|---|---|---|
| 1 | The adventure (overview, background, Parts 1–5, conclusion) | [[SP-GA05-The-Pilgrims-of-the-Hollow-Bell]] |
| 2 | Running the Adventure | [[SP-GA05 — DM's Notes]] (minus the Friday insert and Open Items) |
| 3 | Encounters | [[SP-GA05 — E1 — The Kalbach Churchyard]] · [[SP-GA05 — E2 — The Hollen Ford Relay]] · [[SP-GA05 — E3 — The Orc Camp]] · [[SP-GA05 — E4 — Thirteen Tolls]] |
| 4 | Appendix A: Bestiary | [[SP-GA05 — Bestiary]] |
| 5 | Appendix B: Spells and Items | `Spells/`, `50-Items/` |
| 6 | Appendix C: Dramatis Personae | `30-NPCs/` dossiers |
| 7 | Appendix D: Handouts | six handout notes |
| 8 | Appendix E: The Field Warden's Primer | [[SP-GA05 — Player Gazetteer — The Field Warden's Primer]] |
| 9 | Appendix F: Continuing the Adventure | `Side Quests/` |

## Run Sheet

| # | Scene | Budget | Clock | If you're running long | Core output |
|---|---|---|---|---|---|
| 1 | The Field Office | 10 min | 0:10 | — | The job, the orders, the theme line |
| 2 | Shadowing the Procession | 20 min | 0:30 | Two legs, not three | Notice track; F1 |
| 3 | Kalbach (E1, Easy) | 40 min | 1:10 | Hand out the Winter Telling; 2-round fight | F2; the first choice |
| 4 | Hollen Ford (E2, Medium) | 40 min | 1:50 | Give the short rest, skip its roleplay | F3; Halse's notes |
| — | *Break* | 10 min | 2:00 | — | — |
| 5 | The Orc Camp (E3, Hard) | 35 min | 2:35 | Grukka offers the duel at once | The road up; maybe allies |
| 6 | Thirteen Tolls (E4, Deadly) | 60 min | 3:35 | Next muffle, grapple or consecration ends it | An ending |
| — | Conclusion and credits | 15 min | 3:50 | — | The report |

## Clue Ledger
See **Facts the Players Must Learn** in the main note: four facts, each with three routes and a last resort.
