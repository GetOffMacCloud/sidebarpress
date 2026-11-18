---
type: scene-index
adventure: SP-GS01
section: internal
publish_order: 0
publish: false
longform:
  format: scenes
  title: "The Gluttonwretch of Hommlet"
  workflow: Default Workflow
  sceneFolder: /
  scenes:
    - Scene 01 — Brewfest Eve
    - Scene 02 — What Hommlet Isn't Saying
    - Scene 03 — The War Council
    - Scene 04 — The Grove and the Offering-Heap
    - Scene 05 — The Smokehouse
    - Scene 06 — The Hunt on Emridy Meadows
    - Scene 07 — The Brewfest Feast
    - Scene 08 — The Last Toast
  ignoredFiles:
    - 00 — Scene Index
---
# Scene Index — The Gluttonwretch of Hommlet

Back to [[SP-GS01-The-Gluttonwretch-of-Hommlet]] · Front matter: [[SP-GS01 — Front Matter]] · Mechanic: [[SP-GS01 — The First Fruits]] · Statblocks: [[SP-GS01 — Bestiary]] · Board: [[SP-GS01 — Board]]

> [!info] This note is the **build manifest** and the **Longform project index**. The table below is the canonical paste order for the compiled book. Reorder by changing `publish_order`; drop a file with `publish: false`. See [[Build-Pipeline]].

## Build Manifest

```dataview
TABLE WITHOUT ID
  file.link AS "File",
  section AS "Section",
  publish_order AS "Order",
  default(status, "—") AS "Status",
  choice(publish, "✅", "—") AS "Ships"
FROM "10-Adventures" OR "99-Assets/SP-GS01"
WHERE adventure = "SP-GS01" AND publish_order > 0
SORT publish_order ASC
```

## Run Sheet — three and a half hours (4-hour hard cap)

Act 2 runs two of its three scenes, or all three in parallel if the party splits (cut between groups film-style). Its clock is shared: 65 minutes in total, ending at 2:10 when the feast bell rings.

| # | Scene | Act | Budget | Clock | If you're running long | Core output |
|---|---|---|---|---|---|---|
| 01 | [[Scene 01 — Brewfest Eve]] | 1 | 15 min | 0:15 | Skip the tour of the green; go straight to Pip in the kitchen. | The party sees a gorging, meets Gundigoot and Terjon, and learns of the Open Door. |
| 02 | [[Scene 02 — What Hommlet Isn't Saying]] | 1 | 40 min | 0:55 | Run only the Elder and one other lead; Wat arrives at 0:55 regardless. | The party learns the village's sin and finds the cult's supply line. |
| 03 | [[Scene 03 — The War Council]] | 1 | 10 min | 1:05 | Give each NPC one line and let the players pick. | The party chooses its paths, splits or not, and knows the clock. |
| 04 | [[Scene 04 — The Grove and the Offering-Heap]] | 2 | 25 min | (parallel) | Calm the Heap with one check; run three households, not eight. | Households won over (Offerings banked); the Heap calmed or fought. |
| 05 | [[Scene 05 — The Smokehouse]] | 2 | 30 min | (parallel) | Skip the upper floor; open in the cellar chapel. | The Wishbone taken or smashed; Brindlewick captured, killed or fled. |
| 06 | [[Scene 06 — The Hunt on Emridy Meadows]] | 2 | 25 min | 2:10 | End after the Wretch's third round, whatever has happened. | Damage on the Wretch that carries into the feast. |
| 07 | [[Scene 07 — The Brewfest Feast]] | 3 | 70 min | 3:20 | If phase 2 triggers with under 50 minutes left, skip Second Helpings. | The Wretch laid to rest, destroyed, or victorious. |
| 08 | [[Scene 08 — The Last Toast]] | 3 | 10 min | 3:30 | — | The village gives thanks; the players get the last word. |

**Slack:** 3:30–4:00 is overrun buffer only. Never plan into it.

## Standing Trackers
- **First Fruits:** Offerings banked ☐☐☐☐☐☐ (6 lays the Wretch to rest; at most 3 may come from PCs). See [[SP-GS01 — The First Fruits]].
- **The Wretch's carried damage** from [[Scene 06 — The Hunt on Emridy Meadows]]: ____
- **Brindlewick:** at large · captured · dead · fled
- **The Wishbone:** at the Smokehouse · with the party · with Brindlewick · snapped

## Clue Ledger (tick as found)
Three-clue rule: each conclusion has at least three routes.

**The Wretch is Old Gobbler, starved by the skipped offering**
- [ ] The Elder's confession (Scene 02)
- [ ] The rotted 575 offering in the Elder's cellar (Scene 02)
- [ ] Widow Bree (Scene 02)
- [ ] Jaroo (Scene 04)

**Six offerings freely given will lay it to rest**
- [ ] Jaroo at the war council (Scene 03)
- [ ] The offering shrine's carvings (Scene 04)
- [ ] The Offering-Heap calms when fed (Scene 04)

**A Temple priest binds it with a wishbone at the Smokehouse**
- [ ] Rannos and Gremag's crates and ledger (Scene 02)
- [ ] Wat Thistlewood (Scenes 02–03)
- [ ] Cart tracks from the Meadows (Scene 06)

**Snapping the Wishbone destroys Old Gobbler's spirit**
- [ ] Jaroo's warning (Scene 03)
- [ ] The rite text in the cipher book (Scene 05)
- [ ] Religion or *detect magic* on the Wishbone (Scene 05)

## Prose Checklist (applies to all scenes)
- [ ] Every read-aloud ≤100 words, one paragraph, subject and verb early
- [ ] No feelings, conclusions, or certainty assigned to PCs
- [ ] One metaphor at most per box; no "seems" or "appears"; no mechanics words
- [ ] Register swept (Elfland test)
- [ ] Read each box aloud once before the session; cut any stumble
- [ ] Every damage figure carries its dice
