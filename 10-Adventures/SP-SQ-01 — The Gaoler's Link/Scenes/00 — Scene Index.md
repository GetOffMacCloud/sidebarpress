---
type: scene-index
adventure: SP-SQ-01
section: internal
publish_order: 0
publish: false
longform:
  format: scenes
  title: The Gaoler's Link
  workflow: Default Workflow
  sceneFolder: /
  scenes:
    - Scene 01 — Brewfest on the Landing
    - Scene 02 — Terms
    - Scene 03 — Legwork
    - Scene 04 — The Archive and the Sealed Stacks
    - Scene 05 — The Night of the Warden's Dinner
    - Scene 06 — The Handover
    - Scene 07 — Turning the Job
    - Scene 08 — Dawn on the Landing
  ignoredFiles:
    - 00 — Scene Index
---
# Scene Index — The Gaoler's Link

Back to [[SP-SQ-01-The-Gaolers-Link]] · Mechanics: [[SP-SQ-01 — The Job]] · Statblocks: [[SP-SQ-01 — Bestiary]] · Board: [[SP-SQ-01 — Board]]

> [!info] This note is the **build manifest** and the **Longform project index**. The table below is the canonical paste order for the compiled book. Reorder by changing `publish_order`; drop a file with `publish: false`. See [[Build-Pipeline]].

## Build Manifest

```dataview
TABLE WITHOUT ID
  file.link AS "File",
  section AS "Section",
  publish_order AS "Order",
  default(status, "—") AS "Status",
  choice(publish, "✅", "—") AS "Ships"
FROM "10-Adventures/SP-SQ-01 — The Gaoler's Link" OR "99-Assets/SP-SQ"
WHERE adventure = "SP-SQ-01" AND publish_order > 0
SORT publish_order ASC
```

## Run Sheet

| # | Scene | Act | Budget | Clock | If you're running long | Core output |
|---|---|---|---|---|---|---|
| — | Seating, safety tools, the Job card | — | 15 min | 0:15 | — | Who is broke? Who is Perrender? |
| 01 | [[Scene 01 — Brewfest on the Landing]] | 1 — The Offer | 20 min | 0:35 | Skip the barrel-wrestling; Brandmeier picks them anyway | Brandmeier and Fesch met |
| 02 | [[Scene 02 — Terms]] | 1 — The Offer | 10 min | 0:45 | Take the first number | Hired, or the decline path |
| 03 | [[Scene 03 — Legwork]] | 2 — Casing | 60 min | 1:45 | Three leads, then a montage for 2 Edges | 2–4 Edges; two facts begun |
| 04 | [[Scene 04 — The Archive and the Sealed Stacks]] | 2 — Casing | reference | — | — | The site key; used in 03 and 05 |
| — | *Break* | — | 10 min | 1:55 | — | — |
| 05 | [[Scene 05 — The Night of the Warden's Dinner]] | 3 — The Job | 50 min | 2:45 | Three checks and an Edge each; one complication | The Link in hand; Heat set |
| 06 | [[Scene 06 — The Handover]] | 4 — The Turn | 45 min | 3:30 | Open on the gangplank | The reveal; Vesharan's fate |
| 07 | [[Scene 07 — Turning the Job]] | 4 — The Turn | 20 min | 3:50 | Fold into Scene 06 if they already know | The double-cross executed |
| 08 | [[Scene 08 — Dawn on the Landing]] | 4 — The Turn | 15 min | 4:05 | The ending and the credits only | Ending A–E; credits; the arc hook |

**Total:** about 4 hours. Cut from the long column, never from Scene 06.

**Two-session option.** Session 1: Scenes 01–04 (end on the eve of the dinner, plans laid). Session 2: Scenes 05–08 with every complication.

**Running short?** Play the Weil cousins as a full rival crew in Scene 05 (20 min); run Snick's capture as its own scene (15 min); let a PC sit at the Warden's dinner as a guest while the rest work (the inside man).

## Spotlight Check
| Scene | Belongs to |
|---|---|
| 01–02 | The talker; whoever reads people |
| 03 | Everyone: one lead each, chosen by the player |
| 05 | The sneak, the lockpick, and whoever has a plan |
| 06 | The one holding the Link; the one who can talk Vesharan down |
| 07 | The planner; the dwarf or Hogar's friend (the false Link) |
| 08 | Whoever has been quiet. Ask them what they tell Grell. |

## Standing Trackers
Copy these from [[SP-SQ-01 — The Job]] onto the table card.
- Edges: [ ][ ][ ][ ]
- Heat: 0 1 2 | 3 4 | 5 6
- *Hecht*: **Lax** / Wary / Alert
- The Link: boxed / **unboxed**
- Vesharan: aboard / fled / captured / turned

## Clue Ledger (tick as found)
Three-clue rule: each conclusion has at least three routes.

**F1. The "reliquary" is no heirloom. It's a relic of Iuz's imprisonment**
- [ ] Vogelsang's provenance slip in the coffer, A6 (S04/S05)
- [ ] The six sigils: DC 13 Religion (St. Cuthbert's) or DC 15 History or Arcana (all six); Lecturer Tock in an hour (S04, S07)
- [ ] Snick, caught or bribed: *"Ooh, the Old One's jewelry."* (S03)
- [ ] "The University took it in 565": three years before there was a University here (S01)
- **Last resort:** Brandmeier wakes: *"I have no grandfather in Ritterstadt. What is that?"* (S06)

**F2. Brandmeier isn't himself. He's tethered**
- [ ] His bargemen: *"Hasn't been right since spring. Lets the clerk sign for him."* (S03)
- [ ] DC 14 Insight: he repeats Fesch's phrases word for word (S01, S02)
- [ ] The bone pin in his collar, DC 13 Investigation (S06, S07)
- **ESSENTIAL CLUE / last resort:** within 30 ft of the unboxed Link he forgets his own story mid-sentence (S06)

**F3. Herr Fesch is the real client, and he serves Iuz**
- [ ] Fesch won't pass the palisade gate (Hask, S03)
- [ ] Dolz reads his hand: *"A Ket schoolroom hand."* (S03)
- [ ] The cipher letter: a Horned Society seal and a skull-and-grin countermark (S07)
- **Last resort:** his disguise drops when he loses his temper (S06)

**F4. The Link blinds Iuz and burns his servants**
- [ ] Vogelsang's study notes in the coffer (S04/S05)
- [ ] Dolz: *"Every scrying of the Archive comes back fog."* (S03)
- [ ] The Ashbox's Abyssal lid, DC 14 Arcana (S03 via Hogar, S07)
- [ ] Snick loses track of the party once they hold it (S05)
- **Last resort:** Snick touches the Link and shrieks as its claws smoke (S06)

## Nudge List
1. Hogar grumbles about the lead box that "seals like a coffin." (S03)
2. Liesl Amsel complains that something reads over her shoulder in the reading room. (S03)
3. Baba Yeska: the *Hecht* bought winter furs and a Wolf Nomad pilot "for a run to Schwartzenbruin. In Brewfest. In furs." (S03)
