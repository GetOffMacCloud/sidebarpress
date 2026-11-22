---
type: scene-index
adventure: SP-GS02
section: internal
publish_order: 0
publish: false
longform:
  format: scenes
  title: The Long Night at Candlecrown
  workflow: Default Workflow
  sceneFolder: /
  scenes:
    - Scene 01 — The Candle Stair
    - Scene 02 — Candlecrown at Needfest
    - Scene 03 — The Second Day
    - Scene 04 — The Wind That Sings
    - Scene 05 — The Old Workings
    - Scene 06 — Dusk on the Stair
    - Scene 07 — The Rehearsal
    - Scene 08 — The Knock at the Gate
    - Scene 09 — The Short Day
    - Scene 10 — The Long Night
    - Scene 11 — The Seventh Verse
    - Scene 12 — Dawn at Candlecrown
    - Scene 13 — The Ice Library
  ignoredFiles:
    - 00 — Scene Index
---
# Scene Index — The Long Night at Candlecrown

Back to [[SP-GS02-The-Long-Night-at-Candlecrown]] · Front matter: [[SP-GS02 — Front Matter]] · Mechanics: [[SP-GS02 — The Lantern Line]] · Site: [[SP-GS02 — The Old Workings]] · Statblocks: [[SP-GS02 — Bestiary]] · Board: [[SP-GS02 — Board]]

> [!info] This note is the **build manifest** and the **Longform project index**. The table below is the canonical paste order for the compiled book. Reorder by changing `publish_order`; drop a file with `publish: false`. See [[Build-Pipeline]].

## Build Manifest

```dataview
TABLE WITHOUT ID
  file.link AS "File",
  section AS "Section",
  publish_order AS "Order",
  default(status, "—") AS "Status",
  choice(publish, "✅", "—") AS "Ships"
FROM "10-Adventures" OR "99-Assets/SP-GS02"
WHERE adventure = "SP-GS02" AND publish_order > 0
SORT publish_order ASC
```

## Run Sheet — three sessions of 3–4 hours (optional fourth)

| # | Scene | Session · Day | Budget | Clock | If you're running long | Core output |
|---|---|---|---|---|---|---|
| 01 | [[Scene 01 — The Candle Stair]] | 1 · Needfest 1 | 25 min | 0:25 | One climb check; start the fight at switchback 3. | Up the Stair; edge rules learned; runes melt under a lantern. |
| 02 | [[Scene 02 — Candlecrown at Needfest]] | 1 · Needfest 1 | 50 min | 1:15 | Gate, workshop and feast only. | The village loved; draft, carol rule and singing wind seeded. |
| 03 | [[Scene 03 — The Second Day]] | 1 · Needfest 2 | 60 min | 2:15 | Tansy leads them to Corin; Mother Sedge comes to them. | Corin's drawings, the curse, the ward-lore, the goat tracks. |
| 04 | [[Scene 04 — The Wind That Sings]] | 1 · night 2 | 30 min | 2:45 | End on Dob; skip the tyrg. | A voice taken; something comes up through the floor. |
| 05 | [[Scene 05 — The Old Workings]] | 2 · Needfest 3 | 90 min | 1:30 | M1 → M5 → M7 → M8 only. | The chapel's truth and counter-verse; fire proven; Aurel met. |
| 06 | [[Scene 06 — Dusk on the Stair]] | 2 · Needfest 3 | 35 min | 2:05 | Three tyrgs; straight to the offer. | Wave 1 held; Hrimvald's offer. |
| 07 | [[Scene 07 — The Rehearsal]] | 2 · night 3 | 25 min | 2:30 | Skip the vote. | Wenna's voice taken; the written verse found; the village votes to sing. |
| 08 | [[Scene 08 — The Knock at the Gate]] | 2 · night 3 | 20 min | 2:50 | Tansy speaks at once. | Aurel invited, refused, bargained with or destroyed. |
| 09 | [[Scene 09 — The Short Day]] | 3 · Needfest 4 | 40 min | 0:40 | Two picks each. | The siege prepared. |
| 10 | [[Scene 10 — The Long Night]] | 3 · Midwinter Night | 75 min | 1:55 | Wave 2 as three checks. | Three waves held; posts, choir and pack counted. |
| 11 | [[Scene 11 — The Seventh Verse]] | 3 · Midwinter Night | 60 min | 2:55 | Hrimvald bargains at once. | Fought, tricked or bargained. |
| 12 | [[Scene 12 — Dawn at Candlecrown]] | 3 · Needfest 5–7 | 15 min | 3:10 | — | Endings, rewards, sequels. |
| 13 | [[Scene 13 — The Ice Library]] | 4 (optional) | 3–4 hours | — | Go I1 → I3 → I5. | The voices brought home. |

**Slack:** Session 1 ends at 2:45, Session 2 at 2:50, Session 3 at 3:10. The remainder of each 4-hour slot is overrun buffer only.

## Standing Trackers
- **Voices taken:** Corin ☐ · Dob ☐ · Wenna ☐ · others: ______ (each is a rune on Hrimvald). See [[SP-GS02 — The Lantern Line#Stolen Voices]].
- **Storm stage:** Gathering ☐ · Howling ☐ · the Long Night ☐ · Breaking ☐
- **Lantern posts lit:** ____ / 24 · oil-wick cap: 12 / 18 / 24
- **Choir:** ____ / 40 (Full 30+ · Thin 15–29 · Broken 14−)
- **Hrimvald's pack:** 16 tyrgs + the alpha; killed: ____ (roster in [[SP-GS02 — Bestiary]])
- **Aurel Vasch:** in the mine · on the cliff · invited (by ____) · bargained with · destroyed
- **The hatch / the cliff mouth:** open · barred · sealed
- **The counter-verse:** not found · rubbing taken · read (by ____) · learned by the choir
- **Wenna's paper:** in her sewing box · with the party · burned · given away
- **The bargain on the table:** Hrimvald's (the verse for one voice) · other: ______

## Clue Ledger (tick as found)
Three-clue rule: each conclusion has at least three routes plus a last resort. Nudges are in [[SP-GS02 — The Lantern Line#Nudge List]].

**1. The immoth wants the seventh verse, not the village**
- [ ] Corin's drawings (Scene 03)
- [ ] Mother Sedge: "never write the seventh verse" (Scene 03)
- [ ] The apprentice's warning in the chapel (Scene 05, M5)
- [ ] *Last resort:* Hrimvald says so (Scene 06)

**2. Fire is its weakness; edged weapons barely bite**
- [ ] Ice runes melt under a lantern (Scene 01; again Scene 03)
- [ ] The hunter's shield and the gnawed tail-tip (Scene 05, M3)
- [ ] *Extra:* old Aldo Holm's "piece of blue ice" (Scene 03)
- [ ] Arcana or Nature on first sight (Scene 06)
- [ ] *Last resort:* lantern oil kills the rune-pillar in one splash (Scene 05, M7)

**3. It can be bargained with**
- [ ] It opens with an offer (Scene 06)
- [ ] "It took the words and went" in the chapel (Scene 05, M5)
- [ ] Aurel knows immoths from the Passage (Scenes 05, 08)
- [ ] *Last resort:* it offers again when bloodied (Scene 11)

**4. The stranger must be invited**
- [ ] Mother Sedge's ward-lore (Scene 03; again Scene 08)
- [ ] He never crosses the gate line (Scene 08)
- [ ] He casts no shadow in lantern light (Scenes 05, 08)
- [ ] *Last resort:* Tansy: "He's waiting for someone to say yes." (Scene 08)

**5. The old mine runs under the village**
- [ ] The miners' map in the workshop office (Scene 02)
- [ ] The goat tracks into the coal store (Scene 03)
- [ ] The draft under the workshop floor (Scene 02)
- [ ] *Extra:* old Aldo Holm's story (Scene 03)
- [ ] *Last resort:* a tyrg comes up out of the coal store (Scene 04)

## Climax at a Glance
Every solution in [[Scene 11 — The Seventh Verse]] and where it was seeded.

| Solution | What it takes | Seeded in | Ending |
|---|---|---|---|
| **Fight with fire** | Fire damage each round (stops lines), oil, fire pots, the bonfire | Scenes 01, 03 (runes melt), 05 (M3 shield, M7 oil), 06 (Arcana), 09 (fire pots, bonfire) | Saved (destroyed) or Driven Off |
| **Shelter the choir** | The singing room; the lantern line; the militia | Scenes 07 (the choir's worth), 09 | Makes every other solution easier |
| **The false verse** | A PC who knows the sounds; Deception vs. Insight | Scenes 04 (it's Suloise), 07 (Wenna's paper), 09 | Fooled |
| **The burning lure** | The written verse on an oil-soaked frame; a flame at the right moment | Scenes 02 ("never write it"), 03 (Mother Sedge: it hears writing), 07 (the paper), 09 (the lure) | Saved, after the bargain |
| **Pay its price** | One singer's voice and the verse | Scene 06 (the offer); Scene 11, round 1 | Paid |
| **A word no one living has spoken** | Aurel's master's true name, or a PC's own true secret | Scenes 05, 08 (Aurel); Scene 06 (it loves rare words) | Saved |
| **A confession** | A PC's true, never-told secret | Scene 06 (it trades in words) | Saved (if fewer than 4 lines gathered) |
| **The counter-verse** | The chapel rubbing, read or learned | Scene 05 (M5), Scene 08 (Aurel reads), Scene 09 (the choir learns it) | Unbound |

## Prose Checklist (applies to all scenes)
- [ ] Every read-aloud ≤100 words, one paragraph, subject and verb early
- [ ] No feelings, conclusions, or certainty assigned to PCs
- [ ] One metaphor at most per box; no "seems" or "appears"; no mechanics words
- [ ] Register swept (Elfland test)
- [ ] Read each box aloud once before the session; cut any stumble
- [ ] Every damage figure carries its dice
