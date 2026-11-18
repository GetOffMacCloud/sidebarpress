---
type: scene-index
adventure: SP-KA01
section: internal
publish_order: 0
publish: false
longform:
  format: scenes
  title: The False Arrow (Kestrel)
  workflow: Default Workflow
  sceneFolder: /
  scenes:
    - SP-KA01 — Scene 00 — Kestrel University
    - SP-KA01 — Scene 01 — The High Pass
    - SP-KA01 — Scene 02 — The Cold Welcome
    - SP-KA01 — Scene 03 — Trial of the Horse
    - SP-KA01 — Scene 04 — Trial of the Bow
    - SP-KA01 — Scene 05 — Night in Karash
    - SP-KA01 — Scene 06 — Trial of the Fire
    - SP-KA01 — Scene 07 — The War Council
  ignoredFiles:
    - SP-KA01 — Scene Index
---
# Scene Index — The False Arrow (Kestrel)

> [!info] This note is the **build manifest** for `SP-KA01` and the **Longform project index** (the `longform:` block in the frontmatter). The Dataview table below is the official paste order for the compiled book. To reorder, change `publish_order` in the file's frontmatter; to drop a file from the book, set `publish: false`.

## Build Manifest

```dataview
TABLE WITHOUT ID
  file.link AS "File",
  section AS "Section",
  publish_order AS "Order",
  default(status, "—") AS "Status",
  choice(publish, "✅", "—") AS "Ships"
FROM "10-Adventures"
WHERE adventure = "SP-KA01" AND publish_order > 0
SORT publish_order ASC
```

**Sections, in order:** `overview` (main note, with internal checklists stripped) → `act-1` → `act-2` → `act-3` → `appendix-mechanics` → `appendix-bestiary` → `appendix-handouts` → `appendix-maps`. Files tagged `internal` never ship.

**Compile:** Longform → *Compile* on this project produces the scene prose (acts 1–3). The overview and appendices are pasted around it in manifest order. See [[Build-Pipeline]] for the full procedure and the strip list.

**Scene status ladder:** `outline` → `drafted` → `edited` → `final`. The adventure cannot move to *Package* on its board until every shipping scene is `final`.

Back to [[SP-KA01-The-False-Arrow]] · Mechanics: [[SP-KA01 — The Favor Tracker]] · Statblocks: [[SP-KA01 — Bestiary]]

## Run Sheet — three and a half hours

| # | Scene | Act | Budget | Clock | If you're running long | Core output |
|---|---|---|---|---|---|---|
| 00 | [[SP-KA01 — Scene 00 — Kestrel University]] | 1 — The Road | 5 min | 0:05 | Ask the lecture question during character intros | Each PC's course of study |
| 01 | [[SP-KA01 — Scene 01 — The High Pass]] | 1 — The Road | 15 min | 0:20 | Skip the journey checks; no hazard | The parley letter; Halya's sealed letter |
| 02 | [[SP-KA01 — Scene 02 — The Cold Welcome]] | 1 — The Road | 20 min | 0:40 | Cut the interception to "blades on the snow" | Disarmed; Sorvash's question; the trials set; Favor explained |
| 03 | [[SP-KA01 — Scene 03 — Trial of the Horse]] | 2 — The Trials | 20 min | 1:00 | The best rider makes every check | Weapons back (or not); maybe Sarnai's endorsement |
| — | *Break* | | 10 min | 1:10 | | |
| 04 | [[SP-KA01 — Scene 04 — Trial of the Bow]] | 2 — The Trials | 35 min | 1:45 | Skip tracking; tiger at the den mouth | The false-flag evidence |
| 05 | [[SP-KA01 — Scene 05 — Night in Karash]] | 2 — The Trials | 30 min | 2:15 | Visit runs straight into the attack; spying happens during the fire (default). **Checkpoint:** start by 1:50 | Kezrin is dirty; spy or not |
| 06 | [[SP-KA01 — Scene 06 — Trial of the Fire]] | 2 — The Trials | 15 min | 2:30 | Two questions instead of three | Sarnai learns the truth (or a lie) |
| 07 | [[SP-KA01 — Scene 07 — The War Council]] | 3 — The Council | 45 min | 3:15 | Argue Round 3; chase as one DC 13 check | The ending |
| — | Endings & rewards | | 5 min | 3:20 | Send rewards after the session | |
| — | *Slack* | | 10 min | 3:30 | Table talk eats this first | |

## Standing Trackers
Copy these from [[SP-KA01 — The Favor Tracker]] onto the table card.

- Favor: [ ][ ][ ][ ][ ][ ][ ][ ][ ] (5 = voice · 7 = token)
- Weapons: held by Batzorig [ ] · returned [ ]
- Sarnai's endorsement [ ] · Spied unseen [ ] · Caught spying [ ] · Told Sarnai about Kezrin [ ] · Caught lying [ ]
- Council: R1 [ ] · R2 [ ] · R3 [ ]

## Clue Ledger (tick as found)
Three-clue rule: each conclusion has at least three routes.

**The Wolf Clan arrows are fakes**
- [ ] Glued fletching, grey paint over brown feather (S4, Investigation/Survival DC 13, or a fieldcraft/history student automatically)
- [ ] The beater: "someone's idea of Wolf Clan arrows" (S4)
- [ ] Bows left on the bodies; drag-marks to the den (S4)
- [ ] First sight of Tsolmon's arrow in Temur's sash (S2)
- [ ] The beater: Tsolmon's arrow "matches these" (S4)
- [ ] Tsolmon's arrow beside the ravine arrows (S7)

**Kezrin is behind it**
- [ ] Black-steel arrowhead in a dead rider's hand (S4)
- [ ] Amshari silver coin by the bodies (S4, Investigation DC 15)
- [ ] His bribe and his visit (S5)
- [ ] A captured attacker names him (S5, Intimidation DC 13)
- [ ] Black steel in Temur's war camp (S5, spying)
- [ ] The attackers shout to each other in Amshari (S5)
- [ ] Sarnai's softened line: his steel "came cheaper than bread" (S7, Federkiel PC)
- [ ] *Confirms:* his papers (S7)

**Malkor wants the war** *(optional: the series hook into The War Malkor Wants. The council can be won without it.)*
- [ ] The attackers' leader's grinning-skull brand (S5, Religion DC 12)
- [ ] Kezrin's papers: the skull seal, "from the Black Court" (S7)
- [ ] The ledger names Yulbar (S7)
- **Last resort:** if Kezrin escapes with his papers and no one read the brand, the fact waits for Part 2. Nothing in Part 1 depends on it.

## Prose Checklist (applies to all scenes)
- [x] Every read-aloud is a lead line plus beats; no box over 100 words *(re-counted 2026-10-18; longest is Scene 01's First Sight of Karash, at 99)*
- [x] No feelings, conclusions, or certainty assigned to PCs *(2026-10-18 pass)*
- [x] One metaphor or simile at most per box; no "seems" or "appears"; no mechanics words *(2026-10-18 pass)*
- [x] Each read-aloud ends with a **To the table** prompt. **Exception:** Scene 06, Sarnai's Fire, where the silence is the trial.
- [x] "X, not Y" constructions thinned; "The Weaver weaves" used twice only (S3, S6)
- [ ] **Read each box aloud once before the session.** Cut any stumble.
