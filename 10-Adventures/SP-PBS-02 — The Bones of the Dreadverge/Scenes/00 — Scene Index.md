---
type: scene-index
adventure: SP-PBS-02
section: internal
publish_order: 0
publish: false
longform:
  format: scenes
  title: The Bones of the Dreadverge
  workflow: Default Workflow
  sceneFolder: /
  scenes:
    - Scene 01 — Dusk at the Pound
    - Scene 02 — Counting the Missing
    - Scene 03 — Crossing the Dreadverge
    - Scene 04 — The Cutters' Camp
    - Scene 05 — The Three Sisters
  ignoredFiles:
    - 00 — Scene Index
---
# Scene Index — The Bones of the Dreadverge

> [!info] This note is the **build manifest** for `SP-PBS-02` and the **Longform project index** (the `longform:` block in the frontmatter). The Dataview table below is the canonical paste order for the compiled book. To reorder, change `publish_order` in the file's frontmatter; to drop a file from the book, set `publish: false`.

## Build Manifest

```dataview
TABLE WITHOUT ID
  file.link AS "File",
  section AS "Section",
  publish_order AS "Order",
  default(status, "—") AS "Status",
  choice(publish, "✅", "—") AS "Ships"
FROM "10-Adventures/SP-PBS-02 — The Bones of the Dreadverge" OR "99-Assets/SP-PBS-02"
WHERE adventure = "SP-PBS-02" AND publish_order > 0
SORT publish_order ASC
```

**Sections, in order:** `overview` (main note, with internal checklists stripped) → `act-1` → `act-2` → `act-3` → `appendix-mechanics` → `appendix-bestiary` → `appendix-handouts` → `appendix-maps`. Files tagged `internal` never ship.

**Compile:** Longform → *Compile* on this project produces the scene prose (acts 1–3). The overview and appendices are pasted around it in manifest order. See [[Build-Pipeline]] for the full procedure and the strip list.

**Scene status ladder:** `outline` → `drafted` → `edited` → `final`. The adventure cannot move to *Package* on its board until every shipping scene is `final`.

## Run Sheet

Back to [[SP-PBS-02-The-Bones-of-the-Dreadverge]] · Mechanics: [[SP-PBS-02 — The Howl and the Rite]] · Statblocks: [[SP-PBS-02 — Bestiary]]

| # | Scene | Act | Budget | Core output |
|---|---|---|---|---|
| 01 | [[Scene 01 — Dusk at the Pound]] | 1 — Waycombe | 30 min | The pack is real, bludgeoning works, and the hounds want the cart |
| 02 | [[Scene 02 — Counting the Missing]] | 1 — Waycombe | 45 min | Where they go, why they woke, who marks the doors, and the deadline |
| 03 | [[Scene 03 — Crossing the Dreadverge]] | 2 — The Dreadverge | 60 min | Trackers run; the cut-trenches fight |
| 04 | [[Scene 04 — The Cutters' Camp]] | 2 — The Dreadverge | 30 min (optional) | Unmasking, the letter, the sequel hook |
| 05 | [[Scene 05 — The Three Sisters]] | 3 — The Stones | 60 min | Climax and denouement |

**Total:** about 4 hours, or about 3.5 hours if Scene 4 is skipped. Tables that play every beat run nearer 4½–5 hours; use the box below.

> [!tip] Running long
> - **At 1:15 on the clock**, end Scene 2: Hild is at the door with her crook, and the party leaves now.
> - **Skip the Leg 1 beat.** Narrate it in one sentence and advance the Rite Clock.
> - **Make The Pack Hunts the only Howl fight.** If the Howl reaches 3 first, the hounds shadow the party instead of attacking.
> - **At APL 1–2, run the cut-trenches with half the creatures** (round down; keep at least one boar).
> - **Skip Scene 4.** The clues it carries resurface in Scene 5 (see Scene 4's Alternates).

## Standing Trackers
Copy these from [[SP-PBS-02 — The Howl and the Rite]] onto the table card.

- Rite Clock: [ ][ ][ ][ ][ ][ ]
- Howl: [ ][ ][ ][ ][ ][ ]
- Rite Track: Brannoc [ ][ ][ ] · Wenna [ ][ ][ ] · Tam [ ][ ][ ]

## Clue Ledger (tick as found)
The three-clue rule applies. Each conclusion has at least three routes.

**The pack lairs at the Three Sisters**
- [ ] Hild saw the drag-trail go toward the Sisters (S2)
- [ ] The song: "Three sisters keep the Mother's door, her hounds asleep upon the floor" (S2, Mother Gest)
- [ ] Drag trails on the Dreadverge (S3)
- [ ] The green fire between the three stones, seen from the camp (S4)
- **Last resort:** Hild guides the party there (S2 transition).

**The torc woke them and returning it ends it**
- [ ] The hounds claw Tamsin's cart (S1)
- [ ] Tamsin's green-bronze neck-ring with the same spiral (S2)
- [ ] Kester's chafed wrist and confession (S2)
- [ ] History/Religion DC 13 on the torc: "a binding, not a treasure" (S2)
- [ ] The song: "Bring back the ring, bring back the band" (S2)
- [ ] Ashlock's letter: "her own boy went down into the dark and took the seal… He spared me the work" (S4)
- **Last resort:** if the party skipped the torc, it lies in the heather at the Sisters (S2 alternate).

**Ashlock is the enemy**
- [ ] Ash circles were on the doors of the taken, the day before each was taken (S2)
- [ ] A fresh circle on the mill door today (S2)
- [ ] Hild's "man with antlers" (S2)
- [ ] A scrap of grey wool on a trench stack (S3)
- [ ] The wayside shrine's bent sickle-tooth (S2 alternate, Religion DC 10)
- [ ] The camp, sickle, and letter (S4)
- **Last resort:** he stands in the ring wearing the antlers (S5).

**The deadline is Celene-set**
- [ ] Ashlock says the line about the dark of the moon (S1)
- [ ] The song's last line: "before the small moon leaves the land" (S2)
- [ ] Hild's letter (Hook 4 only)
- [ ] The letter (S4)
- **Last resort:** explain both trackers at the start of S3 (Setting Out).

## Prose Checklist (applies to all scenes)
- [x] Every read-aloud ≤100 words, one paragraph, subject and verb early *(re-checked 2026-10-18; the longest box is Scene 05's mound, at 78. Beats delivered "as their attention finds them" are answers, not part of the box, but each must still be perception only. DM asides belong outside the beat list.)*
- [x] No feelings, conclusions, or certainty assigned to PCs *(2026-10-18: the dawn box no longer moves the party)*
- [x] One metaphor at most per box; no "seems" or "appears"; no mechanics words *(2026-10-18: Scene 03's Setting Out box cut to one figure)*
- [x] Register swept (Elfland test)
- [ ] **Read each box aloud once at the table before the session.** Cut any stumble.
