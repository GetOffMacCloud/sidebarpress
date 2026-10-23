---
type: scene-index
adventure: SP-HAL-02
section: internal
publish_order: 0
publish: false
longform:
  format: scenes
  title: The Hollow Lantern
  workflow: Default Workflow
  sceneFolder: /
  scenes: []
  ignoredFiles:
    - 00 — Scene Index
---
# Scene Index — The Hollow Lantern

Back to [[SP-HAL-02-The-Hollow-Lantern]] · Statblocks: [[SP-HAL-02 — Bestiary]] · Board: [[SP-HAL-02 — Board]]

> [!info] This note is the **build manifest** and the **Longform project index**. The table below is the canonical paste order for the compiled book. Reorder by changing `publish_order`; drop a file with `publish: false`. See [[Build-Pipeline]].

## Build Manifest

```dataview
TABLE WITHOUT ID
  file.link AS "File",
  section AS "Section",
  publish_order AS "Order",
  default(status, "—") AS "Status",
  choice(publish, "✅", "—") AS "Ships"
FROM "10-Adventures/SP-HAL-02 — The Hollow Lantern" OR "99-Assets/SP-HAL-02"
WHERE adventure = "SP-HAL-02" AND publish_order > 0
SORT publish_order ASC
```

## Run Sheet

| # | Scene | Act | Budget | Clock | If you're running long | Core output |
|---|---|---|---|---|---|---|
| — | Seating, pregens, safety tools | — | 10 min | 0:10 | — | One question asked: *who in your past never got a goodbye?* |
| 00 | [[Scene 00 — Marrowmere at Dusk]] | 1 — The Wake-Lights | 30 min | 0:40 | Skip the landing; Osk can be met on the marsh instead | Avelin's empty hand; Tobias is hiding something; Pell won't talk sober |
| 01 | [[Scene 01 — The Mourning Procession]] | 1 — The Wake-Lights | 45 min | 1:25 | Don't let the fight start; the specters set the coffin down and go | The coffin's name; the whispered guest list; Pell's confession and the ring |
| — | *Break* | — | 10 min | 1:35 | — | — |
| 02 | [[Scene 02 — Crossing the Mere]] | 2 — Crossing the Mere | 45 min | 2:20 | One wisp, one voice; cut the sleepwalker chase to a single roll | Across the water; *"She poured the wine herself"* |
| 03 | [[Scene 03 — The Great Hall]] | 3 — Marrow Hall | 40 min | 3:00 | Cut the gallery; keep the fiddler and the chapel | Fiddler's confession; the slashed portrait; Rowena's empty hand seen |
| 04 | [[Scene 04 — Below the Water]] | 3 — Marrow Hall | 30 min | 3:30 | Edric talks instead of fighting; the cask residue is found in one roll | Cask residue; Edric's bargain or his cloak |
| 05 | [[Scene 05 — The Toast]] | 3 — Marrow Hall | 40 min | 4:10 | **Never cut.** End Scene 04 early instead | The ending; the missing bell |

**If the party crosses before 10 PM:** Scene 02 runs short (15 min, causeway rolls only, no wisps); give the time to the great hall, where the guests still believe it's early.

**If the party stays in the village to guard the invitees:** Scenes 03–04 collapse into the sleepwalk chase, and the toast comes to them: Ysolde walks the causeway at midnight with the whole feast behind her. Run Scene 05 on the Reed Landing.

**Total:** about 4 hours, ten minutes over on paper. Cut from the long column, not from Scene 05.

**Running short?** Let the party interview the Wake-Light mourners (15 min of village grief); have Edric's zombies follow them up the stair (10 min); or let Widow Osk read the water for a PC and tell them something true about their own dead (10 min).

## Standing Trackers
Copy onto the table card.

**The Midnight Clock**
| Time | Event | If the party doesn't intervene |
|---|---|---|
| 6 PM | Wake-Lights lit; the hall's windows glow | Doors barred |
| 8 PM | Wedding fiddle across the water | The invited hum it without noticing |
| 9 PM | The Mourning Procession | A coffin on the next invitee's doorstep |
| 10 PM | High tide floods the causeway | Boats or the marsh path only |
| 11 PM | Every invitee sleepwalks toward the mere | Mirabel, Tobias, Avelin wade in |
| Midnight | The toast | Anyone who drinks sleeps forever |

**Scandal (great hall only)** — ☐ ☐ ☐ · At three, the music stops and two specters attack.

**Invitees** — ☐ Mirabel Pell · ☐ Tobias Marrow · ☐ Sister Avelin · ☐ the invited PC. Tick when protected or when seated at the feast.

## Clue Ledger (tick as found)
Three-clue rule: each conclusion has at least three routes.

**Ysolde poisoned the feast herself**
- [ ] Pell's confession: *"She was at the sluice wheel, smiling"* (Scene 00 or 01)
- [ ] The bribed wisp: *"She poured the wine herself"* (Scene 02)
- [ ] The cook's cask: Sweetsleep residue, Investigation DC 13 (Scene 04)
- [ ] Her diary: *"Tonight I will be free of all of them"* (Scene 05)
- [ ] The fiddler: *"I saw her at the wheel. I ran."* (Scene 03)

**Tobias Fenn is a Marrow**
- [ ] Insight DC 14 on his deflections (Scene 00)
- [ ] The invitation in his apron, addressed to *"Master Marrow"* (Scene 00 or 01)
- [ ] The brother's portrait turned to the wall, same jaw (Scene 03)
- [ ] He sleepwalks at 11 (Scene 02)

**The ring belongs in Rowena's tomb**
- [ ] Avelin: *"an empty hand since before I was born"* (Scene 00)
- [ ] Pell: *"her mother's ring. She sold it to pay for the wine."* (Scene 01)
- [ ] Rowena's portrait, ring on her hand (Scene 03)
- [ ] The empty setting on the effigy, same size (Scene 03, H4)

**The fiddler was her lover and the boat was his to bring**
- [ ] The packed trunk in the escape boat, a man's fiddle case beside it (Scene 04, H1)
- [ ] The fiddler's guilt when asked gently, Persuasion DC 12 (Scene 03)
- [ ] The diary: *"He has promised the boat at the water stair"* (Scene 05)
- [ ] A musician PC's tune subplot: his teacher's teacher (Scene 03)

## Spotlight Check
| Scene | Belongs to |
|---|---|
| 00 | The talker (Tobias, Pell) |
| 01 | The named PC |
| 02 | The scout or the druid-type (Osk, the marsh) |
| 03 | The face and the bard |
| 04 | The fighter and the swimmer |
| 05 | Whoever holds the ring or the evidence |

## Prose Checklist (applies to all scenes)
- [ ] Every read-aloud ≤100 words, one paragraph, subject and verb early
- [ ] No feelings, conclusions, or certainty assigned to PCs
- [ ] One metaphor at most per box; no "seems" or "appears"; no mechanics words
- [ ] Register swept (Elfland test)
- [ ] Read each box aloud once before the session; cut any stumble
