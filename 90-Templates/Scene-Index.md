---
type: scene-index
adventure: "SP-PBS-NN"
section: internal
publish_order: 0
publish: false
longform:
  format: scenes
  title: "{{title}}"
  workflow: Default Workflow
  sceneFolder: /
  scenes:
    - Scene 01 — Title
  ignoredFiles:
    - 00 — Scene Index
---
# Scene Index — {{title}}

Back to [[SP-PBS-NN-Title-Slug]] · Mechanics: [[SP-PBS-NN — Mechanic]] · Statblocks: [[SP-PBS-NN — Bestiary]] · Board: [[SP-PBS-NN — Board]]

> [!info] This note is the **build manifest** and the **Longform project index**. The table below is the canonical paste order for the compiled book. Reorder by changing `publish_order`; drop a file with `publish: false`. See [[Build-Pipeline]].

## Build Manifest

```dataview
TABLE WITHOUT ID
  file.link AS "File",
  section AS "Section",
  publish_order AS "Order",
  default(status, "—") AS "Status",
  choice(publish, "✅", "—") AS "Ships"
FROM "10-Adventures/SP-PBS-NN — Title" OR "99-Assets/SP-PBS-NN"
WHERE adventure = "SP-PBS-NN" AND publish_order > 0
SORT publish_order ASC
```

## Run Sheet

| # | Scene | Act | Budget | Clock | If you're running long | Core output |
|---|---|---|---|---|---|---|
| 01 | [[Scene 01 — Title]] | 1 — | 30 min | 0:30 | | |

## Standing Trackers
Copy from the mechanic note onto the table card.

## Clue Ledger (tick as found)
Three-clue rule: each conclusion has at least three routes.

**Conclusion**
- [ ] Clue (Scene)
- [ ] Clue (Scene)
- [ ] Clue (Scene)

## Prose Checklist (applies to all scenes)
- [ ] Every read-aloud ≤100 words, one paragraph, subject and verb early
- [ ] No feelings, conclusions, or certainty assigned to PCs
- [ ] One metaphor at most per box; no "seems" or "appears"; no mechanics words
- [ ] Register swept (Elfland test)
- [ ] Read each box aloud once before the session; cut any stumble
