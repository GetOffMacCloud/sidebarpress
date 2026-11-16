---
type: scene-index
adventure: SP-OP01
section: internal
publish_order: 0
publish: false
longform:
  format: scenes
  title: What the Dead Fear
  workflow: Default Workflow
  sceneFolder: /
  scenes: []
  ignoredFiles:
    - 00 — Scene Index
---
# Scene Index — What the Dead Fear

Back to [[SP-OP01-What-the-Dead-Fear]] · Statblocks: [[SP-OP01 — Bestiary]] · Board: [[SP-OP01 — Board]]

> [!info] This note is the **build manifest** and the **Longform project index**. Reorder by changing `publish_order`; drop a file with `publish: false`. See [[Build-Pipeline]].

## Build Manifest

```dataview
TABLE WITHOUT ID
  file.link AS "File",
  section AS "Section",
  publish_order AS "Order",
  default(status, "—") AS "Status",
  choice(publish, "✅", "—") AS "Ships"
FROM "10-Adventures/SP-OP01 — What the Dead Fear" OR "99-Assets/SP-OP01"
WHERE adventure = "SP-OP01" AND publish_order > 0
SORT publish_order ASC
```

## Run Sheet

| # | Scene | Budget | Clock | If you're running long | Core output |
|---|---|---|---|---|---|
| — | Seating, safety tools | 10 min | 0:10 | — | — |
| 01 | [[Scene 01 — The Grateful Mortician]] | 45 min | 0:55 | Skip the register; describe the fingers outright | The job, the advance, three clues |
| 02 | [[Scene 02 — The Catacombs]] | 45 min | 1:40 | C1 in one line; straight to Old Tam | The ledger, Tam's warning, the gouged doors |
| — | *Break* | 10 min | 1:50 | — | — |
| 03 | [[Scene 03 — What the Dead Fear]] | 60–90 min | 3:20 | Ossian flees at 60 hp | Harrow's truth, the trap, the Larder, an ending |

## Clue Ledger
| Conclusion | Routes |
|---|---|
| Ossian isn't human | Never blinks · wet skin · backward fingers · smell · *detect evil and good* · the animals |
| The dead are being kept and eaten | Burial register · cured limbs · the ledger · Old Tam |
| The real Ossian is dead | Ledger's first entry · Harrow · *speak with dead* on any old burial |
