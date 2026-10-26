---
type: scene-index
adventure: SP-PBS-00
section: internal
publish_order: 0
publish: false
longform:
  format: scenes
  title: Nobody's Colors
  workflow: Default Workflow
  sceneFolder: /
  scenes:
    - Scene 00 — Three Weeks in Aerden
    - Scene 01 — Erlenhof
    - Scene 02 — The Erlen Bridge
    - Scene 03 — Osterschlauss
    - Scene 04 — Two Nights on the Quag
    - Scene 05 — The Stewards' Tent
    - Scene 06 — The Stable Rows
    - Scene 07 — Post Time
    - Scene 08 — The Sale Ring
  ignoredFiles:
    - 00 — Scene Index
---
# Scene Index — Nobody's Colors

Back to [[SP-PBS-00-Nobodys-Colors]] · Mechanics: [[SP-PBS-00 — The Mare, the Clock and the Cord]] · Statblocks: [[SP-PBS-00 — Bestiary]] · Board: [[SP-PBS-00 — Board]]

> [!info] This note is the **build manifest** and the **Longform project index**. The table below is the canonical paste order for the compiled book. Reorder by changing `publish_order`; drop a file with `publish: false`. See [[Build-Pipeline]].

## Build Manifest

```dataview
TABLE WITHOUT ID
  file.link AS "File",
  section AS "Section",
  publish_order AS "Order",
  default(status, "—") AS "Status",
  choice(publish, "✅", "—") AS "Ships"
FROM "10-Adventures/SP-PBS-00 — Nobody's Colors" OR "99-Assets/SP-PBS-00"
WHERE adventure = "SP-PBS-00" AND publish_order > 0
SORT publish_order ASC
```

## Run Sheet

| # | Scene | Act | Budget | Clock | If you're running long | Core output |
|---|---|---|---|---|---|---|
| — | Seating, pregens, safety tools | — | 15 min | 0:15 | — | Two questions asked: *a debt? horses?* |
| 00 | [[Scene 00 — Three Weeks in Aerden]] | 1 — Aerden | 20 min | 0:35 | Skip the market and the butts; keep the board and the notice | Everyone knows they're broke; the notice |
| 01 | [[Scene 01 — Erlenhof]] | 1 — Aerden | 25 min | 1:00 | One question to Adalinde, not three | Hired; the third wagon found or ignored |
| 02 | [[Scene 02 — The Erlen Bridge]] | 1 — The road | 30 min | 1:30 | At 25 minutes, Boedic says *"I've cows to move"* and takes the bribe | Across; the writ in hand |
| 03 | [[Scene 03 — Osterschlauss]] | 2 — The lake | 15 min | 1:45 | Narrate the loading; keep the clerk's one question | The mare aboard; trail or none |
| — | *Break* | — | 10 min | 1:55 | — | — |
| 04 | [[Scene 04 — Two Nights on the Quag]] | 2 — The lake | 40 min | 2:35 | Cut the card game; keep the offer; open on the second night | Vuurzward's name and *ten days* |
| 05 | [[Scene 05 — The Stewards' Tent]] | 3 — The Flats | 25 min | 3:00 | Vuurzward makes his offer in the rows instead | The unsigned book; the offer |
| 06 | [[Scene 06 — The Stable Rows]] | 3 — The Flats | 30 min | 3:30 | One round and a fled saboteur | The mare's Condition settled |
| 07 | [[Scene 07 — Post Time]] | 3 — The Flats | 25 min | 3:55 | **Never cut.** End Scene 6 on the next round instead | Who rides; the race in three sentences |
| 08 | [[Scene 08 — The Sale Ring]] | 3 — The Flats | 10 min | 4:05 | The letter only | Hessel named or not; the letter |

**If the mare was sold to the Rhennee (Scene 4):** Scene 5 runs short (15 min: the line struck, the note called in), Scene 6 is cut, and Scene 7 is a 10-minute beat at an empty stall. That banks about 45 minutes: give it to the city (the hiring halls, the undercard, the Tanner's Rest) or end early.

**Total:** about 4 hours, five minutes over on paper. Cut from the long column, not from Scene 7.

**Running short?** Let the party investigate the *Maid*'s sixteen passengers (20 min); move Weisel's hunt to Derby eve (a whole scene of leaning on a coward); enter a PC in the mounted-archery undercard on Derby morning (15 min); or have Otwin catch them at Osterschlauss even if they weren't held.

## Spotlight Check
| Scene | Belongs to |
|---|---|
| 01 | The negotiator; the one who inspects things |
| 02 | The talker, the lawyer, the one with a clan name |
| 03 | The thief, the forger, the liar |
| 04 | The watchful one; the one who knows horses |
| 05 | The talker again, and whoever carries a debt |
| 06 | The fighters — their only real scene, so give it room |
| 07 | Whoever has been quiet. Ask them directly. |

If a player has not had a scene by Scene 5, hand them the Vuurzward conversation.

## Standing Trackers
Copy these from [[SP-PBS-00 — The Mare, the Clock and the Cord]] onto the table card.

- Maus: **Sound** / Sore / Lame
- Sabotage Clock (S4, S6): [ ][ ][ ]
- Spook die (S6): 0 1 2 3 4 5
- Roodberg: Hostile / **Indifferent** / Friendly
- Bell: the third bell after noon, Richfest 4

## Clue Ledger (tick as found)
Three-clue rule: each conclusion has at least three routes.

**There is a racehorse in the third wagon**
- [ ] The wagon rides low, is bedded with straw, and shifts when nothing touches it (S1)
- [ ] Adalinde: *"It weighs nine hundredweight and it kicked the boards out last Godsday."* (S1)
- [ ] Tilo: the Junker's new saddle that nobody's allowed to see (S0)
- [ ] Boedic says *horse* (S2)
- **Last resort:** at the bridge the mare kicks the shutter open herself.

**Vuurzward paid to stop the mare**
- [ ] Krul, caught or cornered: *"Vuurzward's man. Forty marks."* (S4)
- [ ] The odds-book: an account laying against her, in Vuurzward's name (S5)
- [ ] The bravos wear Vuurzward green under plain cloaks, and their cords are already cut (S6)
- [ ] Vuurzward's one lie, *"I don't know the name"* (Insight DC 18) (S5)
- **Last resort:** a bravo the party drags clear of the stampede says, *"Herr Sivert said nobody gets hurt."* (S6)

**Hessel Amtmann sold the route**
- [ ] Grete: *"He's never bought his own ale in fifteen years. Every market day he's paid a Vuurzward man at the well instead. Not this week."* (S0)
- [ ] Tilo: *"The sergeant's wife was a Vuurzward. And he didn't pay the green man at the well this week."* (S0)
- [ ] Krul: *"The boat and the day, ten days back."* Ten days ago only Corwin and Hessel knew (S4)
- [ ] The odds-book account was opened ten days ago (S5)
- [ ] Vuurzward, asked straight, does not deny it: *"I don't lie, scholar. Ask me something else."* (S5)
- **Last resort:** at the sale ring Adalinde says, *"Hessel booked the passage. Nobody else knew the day."* (S8)

**Whoever signs the book names the rider**
- [ ] Roodberg explains the rule (S5)
- [ ] Weisel: *"I rent cloth. I don't rent promises."* (S5 or S7)
- [ ] Adalinde: *"I ride."* (S1)
- [ ] Adalinde in riding boots she hasn't explained (S7)
- **Last resort:** the steward's boy: *"Ostvelt Grey. The book's still not signed. Whoever signs names the rider. Third bell."* (S7)

**Second place is enough**
- [ ] Otwin's ledger: the place purse is 500, and the note is 400 (S2, if held)
- [ ] The purses are posted on the stewards' board (S5)
- [ ] Adalinde: *"She won't beat the Roodberg colt. She'll beat most of the rest."* (S4)
- **Last resort:** Corwin works it out aloud at post time if someone mentions the purse.

## Prose Checklist (applies to all scenes)
- [ ] Every read-aloud ≤100 words, one paragraph, subject and verb early
- [ ] No feelings, conclusions, or certainty assigned to PCs
- [ ] One metaphor at most per box; no "seems" or "appears"; no mechanics words
- [ ] Register swept (Elfland test)
- [ ] Read each box aloud once before the session; cut any stumble
