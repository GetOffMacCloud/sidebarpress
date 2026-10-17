---
type: scene-index
adventure: SP-PBS-01
section: internal
publish_order: 0
publish: false
longform:
  format: scenes
  title: The False Arrow
  workflow: Default Workflow
  sceneFolder: /
  scenes:
    - Scene 00 — Greyhawk University
    - Scene 01 — The High Pass
    - Scene 02 — The Cold Welcome
    - Scene 03 — Trial of the Horse
    - Scene 04 — Trial of the Bow
    - Scene 05 — Night in Yecha
    - Scene 06 — Trial of the Fire
    - Scene 07 — The War Council
  ignoredFiles:
    - 00 — Scene Index
---
# Scene Index — The False Arrow

> [!info] This note is the **build manifest** for `SP-PBS-01` and the **Longform project index** (the `longform:` block in the frontmatter). The Dataview table below is the canonical paste order for the compiled book. To reorder, change `publish_order` in the file's frontmatter; to drop a file from the book, set `publish: false`.

## Build Manifest

```dataview
TABLE WITHOUT ID
  file.link AS "File",
  section AS "Section",
  publish_order AS "Order",
  default(status, "—") AS "Status",
  choice(publish, "✅", "—") AS "Ships"
FROM "10-Adventures/SP-PBS-01 — The False Arrow" OR "99-Assets/SP-PBS-01"
WHERE adventure = "SP-PBS-01" AND publish_order > 0
SORT publish_order ASC
```

**Sections, in order:** `overview` (main note, with internal checklists stripped) → `act-1` → `act-2` → `act-3` → `appendix-mechanics` → `appendix-bestiary` → `appendix-handouts` → `appendix-maps`. Files tagged `internal` never ship.

**Compile:** Longform → *Compile* on this project produces the scene prose (acts 1–3). The overview and appendices are pasted around it in manifest order. See [[Build-Pipeline]] for the full procedure and the strip list.

**Scene status ladder:** `outline` → `drafted` → `edited` → `final`. The adventure cannot move to *Package* on its board until every shipping scene is `final`.

Back to [[SP-PBS-01-The-False-Arrow]] · Mechanics: [[SP-PBS-01 — The Favor Tracker]] · Statblocks: [[SP-PBS-01 — Bestiary]]

## Run Sheet — four hours

| # | Scene | Act | Budget | Clock | If you're running long | Core output |
|---|---|---|---|---|---|---|
| 00 | [[Scene 00 — Greyhawk University]] | 1 — The Road | 5 min | 0:05 | Start at the posting | Each PC's course of study |
| 01 | [[Scene 01 — The High Pass]] | 1 — The Road | 20 min | 0:25 | Skip the journey checks; no hazard | The parley letter; Halya's sealed letter |
| 02 | [[Scene 02 — The Cold Welcome]] | 1 — The Road | 25 min | 0:50 | Cut the interception to "blades on the snow" | Disarmed; Cligir's question; the trials set; Favor explained |
| 03 | [[Scene 03 — Trial of the Horse]] | 2 — The Trials | 30 min | 1:20 | One attempt, by the best rider | Weapons back (or not); maybe Sarnai's endorsement |
| — | *Break* | | 10 min | 1:30 | | |
| 04 | [[Scene 04 — Trial of the Bow]] | 2 — The Trials | 40 min | 2:10 | Skip tracking; tiger at the den mouth | The false-flag evidence |
| 05 | [[Scene 05 — Night in Yecha]] | 2 — The Trials | 40 min | 2:50 | **Checkpoint:** if this scene starts after 2:20, run Kezrin's visit straight into the attack and spy during the fire | Kezrin is dirty; spy or not |
| 06 | [[Scene 06 — Trial of the Fire]] | 2 — The Trials | 15 min | 3:05 | Two questions instead of three | Sarnai learns the truth (or a lie) |
| 07 | [[Scene 07 — The War Council]] | 3 — The Council | 50 min | 3:55 | Argue Round 3; chase as one DC 13 check | The ending |
| — | Endings & rewards | | 5 min | 4:00 | Send rewards after the session | |

## Standing Trackers
Copy these from [[SP-PBS-01 — The Favor Tracker]] onto the table card.

- Favor: [ ][ ][ ][ ][ ][ ][ ][ ][ ] (5 = voice · 7 = token)
- Weapons: held by Batzorig [ ] · returned [ ]
- Sarnai's endorsement [ ] · Spied unseen [ ] · Caught spying [ ] · Told Sarnai about Kezrin [ ] · Caught lying [ ]
- Council: R1 [ ] · R2 [ ] · R3 [ ]

## Clue Ledger (tick as found)
Three-clue rule: each conclusion has at least three routes.

**The Wolf arrows are fakes**
- [ ] Glued fletching, grey paint over brown feather (S4, Investigation/Survival DC 13, or a fieldcraft/history student automatically)
- [ ] The beater: "someone's idea of Wolf arrows" (S4)
- [ ] Bows left on the bodies; drag-marks to the den (S4)
- [ ] Tsolmon's arrow beside the ravine arrows (S7)

**Kezrin is behind it**
- [ ] Black-steel arrowhead in a dead rider's hand (S4)
- [ ] Ekbiri silver coin by the bodies (S4, Investigation DC 15)
- [ ] His bribe and his visit (S5)
- [ ] A captured attacker names him (S5, Intimidation DC 13)
- [ ] Black steel in Temur's war camp (S5, spying)
- [ ] His papers (S7)

**Iuz wants the war** *(optional: the series hook into [[The War Iuz Wants]]. The council can be won without it.)*
- [ ] The attackers' leader's grinning-skull brand (S5, Religion DC 12)
- [ ] Kezrin's papers: the skull seal, "from Dorakaa" (S7)
- [ ] The ledger names Yulbar (S7)
- **Last resort:** if Kezrin escapes with his papers and no one read the brand, the fact waits for Part 2. Nothing in Part 1 depends on it.

## Prose Checklist (applies to all scenes)
- [x] Every read-aloud is a lead line plus beats; no box over 100 words
- [x] No feelings, conclusions, or certainty assigned to PCs
- [x] Each read-aloud ends with a **To the table** prompt
- [x] "X, not Y" constructions thinned; "Istus weaves" used twice only (S3, S6)
- [ ] **Read each box aloud once before the session.** Cut any stumble.
