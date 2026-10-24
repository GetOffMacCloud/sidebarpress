---
type: scene-index
adventure: SP-HAL-03
section: internal
publish_order: 0
publish: false
longform:
  format: scenes
  title: The Night That Doesn't End
  workflow: Default Workflow
  sceneFolder: /
  scenes:
    - Scene 00 — The Gate at Dusk
    - Scene 01 — Midnight, the First Time
    - Scene 02 — Not Again
    - Scene 03 — The Ossuary
    - Scene 04 — The Chain Crypt
    - Scene 05 — The Thirteenth Toll
  ignoredFiles:
    - 00 — Scene Index
---
# Scene Index — The Night That Doesn't End

Back to [[SP-HAL-03-The-Night-That-Doesnt-End]] · Mechanics: [[SP-HAL-03 — Loop Rules]] · Statblocks: [[SP-HAL-03 — Bestiary]] · Board: [[SP-HAL-03 — Board]]

> [!info] This note is the **build manifest** and the **Longform project index**. The table below is the canonical paste order for the compiled book. Reorder by changing `publish_order`; drop a file with `publish: false`. See [[Build-Pipeline]].

## Build Manifest

```dataview
TABLE WITHOUT ID
  file.link AS "File",
  section AS "Section",
  publish_order AS "Order",
  default(status, "—") AS "Status",
  choice(publish, "✅", "—") AS "Ships"
FROM "10-Adventures/SP-HAL-03 — The Night That Doesn't End" OR "99-Assets/SP-HAL-03"
WHERE adventure = "SP-HAL-03" AND publish_order > 0
SORT publish_order ASC
```

## Run Sheet

| # | Scene | Act | Budget | Clock | If you're running long | Core output |
|---|---|---|---|---|---|---|
| — | Seating, pregens, safety tools | — | 10 min | 0:10 | — | Ask: *who have you lost? what do you do when you can't sleep?* |
| 00 | [[Scene 00 — The Gate at Dusk]] | 1 — Loop 1 | 30 min | 0:40 | Skip the orchard; keep Hale, Wren's rhyme, and the feast toasts | The village is wrong; Wren's rhyme heard |
| 01 | [[Scene 01 — Midnight, the First Time]] | 1 — Loop 1 | 30 min | 1:10 | Run the Bell Ringer for 4 rounds, narrate the rest | The crows caw once; Marta taken or saved; reset |
| 02 | [[Scene 02 — Not Again]] | 2 — Loop 2 | 40 min | 1:50 | Hale's Q&A only; hand over the key by Benedikt's choice | The thirteenth toll known; crypt key in hand |
| — | *Break* | — | 10 min | 2:00 | — | — |
| 03 | [[Scene 03 — The Ossuary]] | 2 — Loop 2 | 35 min | 2:35 | One ghast; narrate the Bone Calendar read | The bone found; Elsbeth's lantern; second reset |
| 04 | [[Scene 04 — The Chain Crypt]] | 3 — Loop 3 | 25 min | 3:00 | Thorne's offer in two lines; straight to the fight | Thorne's lie heard; party split decided |
| 05 | [[Scene 05 — The Thirteenth Toll]] | 3 — Loop 3 | 50 min | 3:50 | **Never cut.** End Scene 4 one exchange earlier instead | The ending; the bell; the calendar read at dawn |

**Loop budget:** Loop 1 is 60 minutes and should feel fast; the players don't know the rules yet. Loop 2 is where they investigate, so give it the slack. Loop 3 is the fight.

**If the party breaks the loop early (nobody rings for 2 rounds in Loop 1 or 2):** Scene 05 runs now, with Thorne at full strength and the party under-informed. That's a legitimate hard ending, not a failure state. Scenes 02–04 become dawn-after cleanup.

**Total:** about 4 hours, ten minutes under on paper. Spend the slack on the Echo Lanes.

**Running short?** Let the party interview three more Echoes in the lanes (15 min); run the ghouls when someone disrupts an Echo (15 min); let Annick walk the party through the orchard with the crows naming tonight's taken (10 min); play the first midnight twice, once inside the inn and once in the belfry.

## Spotlight Check
| Scene | Belongs to |
|---|---|
| 00 | The social PC (reading the Echoes) |
| 01 | The front-liner (the rope) |
| 02 | The investigator |
| 03 | The cleric or paladin (Religion, the lanterns) |
| 04 | Whoever Thorne names |
| 05 | Everyone, split |

## Standing Trackers
Copy from [[SP-HAL-03 — Loop Rules]] onto the table card.

**Loop-Weariness (per PC):** ☐ 1 ☐ 2 ☐ 3 — *at 4, the PC becomes an Echo*
**Crows Count:** Loop 1 ___ · Loop 2 ___ · Loop 3 ___ (starts 1 / 3 / 5; −1 per soul protected the previous loop)
**The night:** 6 PM gate · 7 PM lanterns · 8 PM feast · 9 PM crows · 10 PM Hale climbs · 11 PM Echoes stare · 12 AM twelve tolls
**Souls protected through a midnight:** ___
**Lanterns shattered in the Hollow Choir:** ___ of ~70

## Clue Ledger (tick as found)
Three-clue rule: each conclusion has at least three routes.

**The bell makes the loop**
- [ ] Hale: "Don't go into the church after eleven" (Scene 00)
- [ ] Wren's rhyme: *"Toll the twelve and round we go"* (Scene 00)
- [ ] *Detect magic* on the belfry shows abjuration bound to the bell (Scene 01)
- [ ] Benedikt's parish record: the bell bought from Marrowmere forty years ago, "one that had rung over the drowned" (Scene 02)
- [ ] Hale's notes describe the binding rite (Scene 02)

**Hale is the jailer, not the villain**
- [ ] He says "not again" at the second dusk (Scene 02)
- [ ] He climbs the belfry at 10 PM every loop and fights the shadows alone (Scene 01)
- [ ] His cottage: forty years of notes in one hand (Scene 02)
- [ ] Elsbeth's lantern, set apart in the ossuary (Scene 03)

**Thorne is under the chapel**
- [ ] Wren: *"the reaper sleeps where bones lie low"* (Scene 00)
- [ ] The Echoes turn and stare at the chapel at 11 PM (Scene 00, 02)
- [ ] The shadows rise *through the belfry floor* (Scene 01)
- [ ] The chain clinking under Midnight Mass (Scene 02)
- [ ] Thorne's voice up the shaft: "I've counted you already" (Scene 03)

**The thirteenth toll binds him**
- [ ] Hale's Q&A: "thirteen tolls while he stands in his own bone circle" (Scene 02)
- [ ] Thorne's finger bone caps the first column of the calendar (Scene 03)
- [ ] The bone circle sits under the shaft to the belfry (Scene 04)
- [ ] Religion DC 15 on the circle: a binding needs the bound thing's own bone (Scene 04)
- [ ] Thorne's offer tells the truth backwards: "nobody could ring a thirteenth, there's no one left to try" (Scene 04)

## Prose Checklist (applies to all scenes)
- [ ] Every read-aloud ≤100 words, one paragraph, subject and verb early
- [ ] No feelings, conclusions, or certainty assigned to PCs
- [ ] One metaphor at most per box; no "seems" or "appears"; no mechanics words
- [ ] Register swept (Elfland test)
- [ ] Read each box aloud once before the session; cut any stumble
