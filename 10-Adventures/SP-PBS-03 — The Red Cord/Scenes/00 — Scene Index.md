---
type: scene-index
adventure: SP-PBS-03
section: internal
publish_order: 0
publish: false
longform:
  format: scenes
  title: The Red Cord
  workflow: Default Workflow
  sceneFolder: /
  scenes:
    - Scene 01 — The Ritter's Hall
    - Scene 02 — Across the Quag
    - Scene 03 — Under the Red Cord
    - Scene 04 — The Brawl
    - Scene 05 — Dornhalm's Yard
    - Scene 06 — The Midnight Bell
  ignoredFiles:
    - 00 — Scene Index
---
# Scene Index — The Red Cord

Back to [[SP-PBS-03-The-Red-Cord]] · Mechanics: [[SP-PBS-03 — Cord, Temper and Trust]] · Statblocks: [[SP-PBS-03 — Bestiary]] · Board: [[SP-PBS-03 — Board]]

> [!info] This note is the **build manifest** and the **Longform project index**. The table below is the canonical paste order for the compiled book. Reorder by changing `publish_order`; drop a file with `publish: false`. See [[Build-Pipeline]].

## Build Manifest

```dataview
TABLE WITHOUT ID
  file.link AS "File",
  section AS "Section",
  publish_order AS "Order",
  default(status, "—") AS "Status",
  choice(publish, "✅", "—") AS "Ships"
FROM "10-Adventures/SP-PBS-03 — The Red Cord" OR "99-Assets/SP-PBS-03"
WHERE adventure = "SP-PBS-03" AND publish_order > 0
SORT publish_order ASC
```

## Run Sheet

| # | Scene | Act | Budget | Clock | If you're running long | Core output |
|---|---|---|---|---|---|---|
| 01 | [[Scene 01 — The Ritter's Hall]] | 1 — Ritterstadt | 15 min | 0:15 | Skip the Falk consult; Hildegard delivers the banner beat | Konrad agrees to go; the half-banner travels with him |
| 02 | [[Scene 02 — Across the Quag]] | 1 — The Lake | 15 min | 0:30 | Cut the dock patrol to one question | Gerhard's memory; first Trust |
| 03 | [[Scene 03 — Under the Red Cord]] | 2 — The Red Cord | 30 min | 1:00 | Two provocations, not four | The law, the witnesses, the relic, the timber remark |
| 04 | [[Scene 04 — The Brawl]] | 2 — The Red Cord | 15 min | 1:15 | End it at the end of round 2 | The Soldbrief is stolen |
| 05 | [[Scene 05 — Dornhalm's Yard]] | 3 — Before the Bell | 20 min | 1:35 | Replace the chase with one Perception check | The Soldbrief back; Dornhalm exposed |
| 06 | [[Scene 06 — The Midnight Bell]] | 3 — Before the Bell | 25 min | 2:00 | Skip the bout; go to the standards | The truth; the amends; swords or coin |

**Total:** about 2 hours.

## Standing Trackers
Copy these from [[SP-PBS-03 — Cord, Temper and Trust]] onto the table card.

- Temper: [1][2][3][4][5][6]
- Trust: [ ][ ][ ]
- Bell: [ ][ ][ ][ ][ ][ ] (starts at 2 on entering the Red Cord)

## Clue Ledger (tick as found)
Three-clue rule: each conclusion has at least three routes.

**Someone is baiting Konrad on purpose, and it isn't Jost**
- [ ] The provocateur knows about the timber, which only someone who knows about the Schuldbrief could know (S3)
- [ ] Rudi Brack's purse is full of new Schwartzenbruin coin and he drinks alone; Ilka has never seen him with a company (S3)
- [ ] The cutpurse moves the moment Rudi throws the first punch (S4)
- [ ] The trail leads to Dornhalm's Yard, not to the Hundred's chapter-house (S5)
- [ ] Dornhalm's tally-book lists "Brack — 10 marks — the Ritter's cord" (S5)
- **Last resort:** if nobody has connected it by the yard, the dock sergeant arrives with Fenna in hand. She was caught running with the case, and she names Dornhalm on the spot.

**The Hundred did not break its contract**
- [ ] The "torn" banner in the Hall has a clean, straight cut (S1, Investigation DC 10 or just looking closely)
- [ ] Gerhard's memory: "my father on the wall, cutting the banner down" (S2)
- [ ] Mutter Ilka's grandmother: "the Ritter sent them to us" (S3)
- [ ] Ilse's relic, "the banner we failed," is the other half (S3/S6)
- [ ] Jost: "Some debts are paid by saying nothing. Mine is." (S3)
- [ ] The halved-standard custom (History DC 13, Falk in S1, or Korporal Mattis of the Ernes if asked in S3)
- **Last resort:** at the last quarter-bell, Mutter Ilka tells the whole room her grandmother's story and asks Konrad to lay his colours beside Ilse's. The cut does the rest.

**The amends needs the Soldbrief, and the Soldbrief needs the bell**
- [ ] Ilse explains the ceremony when the party sits down (S3)
- [ ] The Council's clerk taps the bell-glass on his table (S3)
- [ ] Ilka: "Clerk goes home at the bell. Always has." (S3)
- **Last resort:** the clerk says it himself when the Soldbrief goes missing: *"Midnight, sirs. Then I go home."*

## Prose Checklist (applies to all scenes)
- [ ] Every read-aloud ≤100 words, one paragraph, subject and verb early
- [ ] No feelings, conclusions, or certainty assigned to PCs
- [ ] One metaphor at most per box; no "seems" or "appears"; no mechanics words
- [ ] Register swept (Elfland test)
- [ ] Read each box aloud once before the session; cut any stumble
