---
type: scene-index
adventure: SP-HAL-04
section: internal
publish_order: 0
publish: false
longform:
  format: scenes
  title: The Tithe of Thornbury
  workflow: Default Workflow
  sceneFolder: /
  scenes: []
  ignoredFiles:
    - 00 — Scene Index
---
# Scene Index — The Tithe of Thornbury

Back to [[SP-HAL-04-The-Tithe-of-Thornbury]] · Statblocks: [[SP-HAL-04 — Bestiary]] · Handout: [[SP-HAL-04 — Handout — The Pact]] · Board: [[SP-HAL-04 — Board]]

> [!info] This note is the **build manifest** and the **Longform project index**. The table below is the canonical paste order for the compiled book. Reorder by changing `publish_order`; drop a file with `publish: false`. See [[Build-Pipeline]].

## Build Manifest

```dataview
TABLE WITHOUT ID
  file.link AS "File",
  section AS "Section",
  publish_order AS "Order",
  default(status, "—") AS "Status",
  choice(publish, "✅", "—") AS "Ships"
FROM "10-Adventures/SP-HAL-04 — The Tithe of Thornbury" OR "99-Assets/SP-HAL-04"
WHERE adventure = "SP-HAL-04" AND publish_order > 0
SORT publish_order ASC
```

## Run Sheet

| # | Scene | Act | Budget | Clock | If you're running long | Core output |
|---|---|---|---|---|---|---|
| — | Seating, pregens, safety tools | — | 15 min | 0:15 | — | Two questions asked: *who do you owe? who's fed you?* |
| 00 | [[Scene 00 — Harvest Home]] | 1 — Harvest Home | 20 min | 0:35 | Narrate the welcome; keep the banner and one child with a roll | Everyone likes Thornbury; Ned is here |
| 01 | [[Scene 01 — The Hundredth Feast]] | 1 — Harvest Home | 40 min | 1:15 | Cut the toasts; keep the chair and the loaf | Someone has eaten; the chair's warning heard |
| 02 | [[Scene 02 — The Long Night]] | 2 — The Long Night | 45 min | 2:00 | Skip the flameskull unless they fight a lantern; give the pact through Tamsin | The four loopholes; Tamsin's rear door |
| — | *Break* | — | 10 min | 2:10 | — | — |
| 03 | [[Scene 03 — The Blackthorn Copse]] | 2 — The Long Night | 40 min | 2:50 | One shambling mound and Hesper's first three answers | Where the heart is; what breaking the pact costs |
| 04 | [[Scene 04 — The Procession]] | 3 — The Tithe | 35 min | 3:25 | End the Colossus fight when the cage is open or the barn doors are reached | The guest named; the Colossus done with |
| 05 | [[Scene 05 — The Tithe Barn]] | 3 — The Tithe | 50 min | 4:15 | **Never cut.** Shorten Scene 04 instead | The ending chosen; the guest's fate |

**Total:** about 4 hours, fifteen minutes over on paper. Cut from the long column, not from Scene 05.

**If the party goes to the barn early (before 10 PM):** Scene 04 becomes the Colossus at the barn doors (20 min), and the Sheaf's procession arrives mid-fight in Scene 05 with Ned in a cart. Banks about 15 minutes.

**Running short?** Let the party return a past guest's belongings to a Thornbury family that never knew (15 min of hard roleplay); run the Corn Maze as a chase with the lanterns reporting every turn (20 min); or let Hesper tell the story of her grandmother's burning in full.

## Standing Trackers
Copy onto the table card.

**The Midnight Clock**
| Time | Event | Done |
|---|---|---|
| 4 PM | Arrival and welcome | [ ] |
| 6 PM | The Hundredth Feast; the loaf is passed | [ ] |
| 8 PM | Bonfire and the Corn Maze | [ ] |
| 10 PM | The Choosing: the sheaf-mark appears | [ ] |
| 11 PM | The procession to the Tithe Barn | [ ] |
| Midnight | The guest is given to the field | [ ] |

**Who ate the loaf?** ______ (if nobody: Old Ned Tallow)

**Harvest Bounty (Scene 05)** — tick a field each time the Harvest Lord heals. At three, the Sheaf stops singing and can be turned.
- [ ] Reap's field (east) · [ ] Thorne's field (north) · [ ] The founders' field (west) · [ ] The children's field (south)

**Bundle items in play:** [ ] Vesper Bell (Thorne inside) · [ ] Thorne free · [ ] Gentleman's card · [ ] A PC with no reflection

## Clue Ledger (tick as found)
Three-clue rule: each conclusion has at least three routes.

**The whole village is the cult, and the party is the guest**
- [ ] The banner already has their names (Scene 00)
- [ ] Insight DC 16: everyone is too eager for them to eat (Scene 00)
- [ ] The Empty Chair's whisper: *"They smiled the whole time"* (Scene 01)
- [ ] Tamsin almost says it (Scene 01, 02)
- [ ] Hesper says it outright (Scene 03)

**The Hundredth Loaf is the binding**
- [ ] *Detect magic*: faint enchantment (Scene 01)
- [ ] Arcana/Nature DC 15: a binding (Scene 01)
- [ ] The chair's last words: *"Don't eat the bread"* (Scene 01)
- [ ] The sheaf-mark appears on the eater's palm at 10 PM (Scene 02/04)

**The pact has loopholes**
- [ ] The lintel of the Tithe Barn, in plain sight (Scene 02 or 04)
- [ ] The vellum in the Elder's house, Investigation DC 14 (Scene 02)
- [ ] Hesper: *"Josiah wrote them in a hurry"* (Scene 03)
- [ ] Bundle: the bone calendar from SP-HAL-03 (pre-seeded)

**The heart is under the barn**
- [ ] Hesper tells them (Scene 03)
- [ ] The wheat grows thickest over the barn, and the floor breathes (Scene 02 if they look, Scene 05)
- [ ] Tamsin's rear door leads to the root cellar (Scene 02)
- [ ] The procession goes nowhere else (Scene 04)

## Prose Checklist (applies to all scenes)
- [ ] Every read-aloud ≤100 words, one paragraph, subject and verb early
- [ ] No feelings, conclusions, or certainty assigned to PCs
- [ ] One metaphor at most per box; no "seems" or "appears"; no mechanics words
- [ ] Register swept (Elfland test)
- [ ] Read each box aloud once before the session; cut any stumble
