---
type: scene-index
adventure: SP-HAL-01
section: internal
publish_order: 0
publish: false
longform:
  format: scenes
  title: Straw Men
  workflow: Default Workflow
  sceneFolder: /
  scenes:
    - Scene 00 — Arrival at Hollow Ford
    - Scene 01 — The Closing Reel
    - Scene 02 — The Bobbing Game
    - Scene 03 — Mother Nettle's Cottage
    - Scene 04 — Fields and Stall
    - Scene 05 — The Mill
  ignoredFiles:
    - 00 — Scene Index
---
# Scene Index — Straw Men

Back to [[SP-HAL-01-Straw-Men]] · Statblocks: [[SP-HAL-01 — Bestiary]] · Board: [[SP-HAL-01 — Board]] · Bundle: [[SP-HAL-00-Hallows-Eve-Quartet]]

> [!info] This note is the **build manifest** and the **Longform project index**. The table below is the canonical paste order for the compiled book. Reorder by changing `publish_order`; drop a file with `publish: false`. See [[Build-Pipeline]].

## Build Manifest

```dataview
TABLE WITHOUT ID
  file.link AS "File",
  section AS "Section",
  publish_order AS "Order",
  default(status, "—") AS "Status",
  choice(publish, "✅", "—") AS "Ships"
FROM "10-Adventures/SP-HAL-01 — Straw Men" OR "99-Assets/SP-HAL-01"
WHERE adventure = "SP-HAL-01" AND publish_order > 0
SORT publish_order ASC
```

## Run Sheet

| # | Scene | Act | Budget | Clock | If you're running long | Core output |
|---|---|---|---|---|---|---|
| — | Seating, pregens, safety tools | — | 10 min | 0:10 | — | Two questions asked: *who do you trust? who's missing?* |
| 00 | [[Scene 00 — Arrival at Hollow Ford]] | 1 — Market day | 25 min | 0:35 | Skip the stalls; keep Brann, the hook, and one tell | Hired or invited; one tell noticed |
| 01 | [[Scene 01 — The Closing Reel]] | 1 — Market day | 35 min | 1:10 | Scarecrow flees at 15 damage whatever the APL | The straw trail upstream; the village won't believe them |
| 02 | [[Scene 02 — The Bobbing Game]] | 2 — The long night | 20 min | 1:30 | Offer the apple once; don't stall | Pip's location, or the scrapings; one reflection taken or not |
| — | *Break* | — | 10 min | 1:40 | — | — |
| 03 | [[Scene 03 — Mother Nettle's Cottage]] | 2 — The long night | 35 min | 2:15 | Two questions to Nettle, then the mob arrives | "Stop the wheel"; Corwin turned or not |
| 04 | [[Scene 04 — Fields and Stall]] | 2 — The long night | 35 min | 2:50 | Pick one: the stall or Voss. The fields can be a line | Haskell named; Voss unmasked; the dollies burned |
| 05 | [[Scene 05 — The Mill]] | 3 — The mill | 70 min | 4:00 | Cut M2 and M5; go straight from the race to the loft | Sleepers saved; the wheel; the carriage |

**Total:** about 4 hours. Cut from the long column, never from Scene 05.

**Running short?** Let the party stake out a scarecrow post and watch a double climb onto it (15 min); have Aldous Crane invite them into the "closed" mill by day and give them the three phrases (10 min); run the market as a haggling scene where every stall-keeper gets one tell wrong (15 min).

## Spotlight Check
| Scene | Belongs to |
|---|---|
| 00 | The face (Insight, Investigation), the talker (Brann) |
| 01 | The fighter; the one who can see through the glamour (Wis save) |
| 02 | Whoever leans in. Give the choice to the player who likes risk |
| 03 | The talker (the mob), the scholar (Nettle's lore) |
| 04 | The sneak (the stall), the fighter (Voss), the arcanist (the dollies) |
| 05 | Everyone: wheel, sacks, hag, and the contract are four jobs |

## Standing Trackers
Copy onto the table card.

**The Midnight Clock.** Each hour the party doesn't interfere, Chaff takes another villager.

| Time | Event | If the party doesn't intervene |
|---|---|---|
| 6 PM | The party arrives as the market winds down. Widow Haskell's stall is the busiest on the green. | Chaff sells corn dollies to her next five targets. |
| 8 PM | The closing reel begins. | A scarecrow leads a dancer into the dark (Scene 01). |
| 9 PM | The Bobbing Game in the inn yard. | Doesn't advance unless an apple is eaten. |
| 10 PM | Father Corwin leads a mob to Mother Nettle's cottage. | Nettle driven off or hurt; the party loses its best ally. |
| 11 PM | The last villagers are taken. | Twelve sleepers fill the mill loft. |
| Midnight | The Gentleman in Grey's carriage arrives at the mill. | All twelve vanish as corn dollies; their doubles collapse. |

If Corwin becomes an ally, he rings the chapel bell to keep villagers indoors: **slow the clock by one hour.**

**Sleepers in the loft:** 7 at dusk. Tally up with each hour the clock advances; tally down with each double destroyed.

## Clue Ledger (tick as found)
Three-clue rule: each conclusion has at least three routes.

**The doubles are fake**
- [ ] No breath in the cold; won't eat; flinch from fire (Scene 00, 01)
- [ ] A corn kernel where a tooth should be (Scene 00)
- [ ] They don't remember anything from before three weeks ago (Scene 00, 04)
- [ ] The scarecrow at the reel wears a farmer's coat and nobody reacts (Scene 01)
- [ ] Voss won't remove her gauntlets; straw fingers (Scene 04)

**The mill is the source**
- [ ] The wheel turns backward, visible from the road (Scene 00)
- [ ] The straw trail after the reel leads upstream (Scene 01)
- [ ] The apple vision: Pip in a sack, a waterwheel groaning (Scene 02)
- [ ] Nettle: "a wheel that turns backward unwinds a soul" (Scene 03)
- [ ] The doubles' resting posts face the mill; Crane's three phrases (Scene 04)

**Widow Haskell is the hag**
- [ ] Green fingernail scrapings on the barrel rim; Pip's "lady with green fingers" (Scene 02)
- [ ] Nettle: "Hags love a market. Who's the one stranger nobody suspects?" (Scene 03)
- [ ] A single hair braided into every dolly, one per remaining target (Scene 04)
- [ ] Confronted, she laughs, packs up, and heads upstream (Scene 04)

**The contract has a loophole**
- [ ] Nettle: "a contract read closely. The last one hurts most." (Scene 03)
- [ ] "Twelve folk of Hollow Ford," and Chaff has lived here three weeks (Scene 05, M6)
- [ ] The ledger's prior customers show the Gentleman likes a clever reading (Scene 05, M6)

## Prose Checklist (applies to all scenes)
- [x] Every read-aloud ≤100 words, one paragraph, subject and verb early
- [x] No feelings, conclusions, or certainty assigned to PCs
- [ ] One metaphor at most per box; no "seems" or "appears"; no mechanics words
- [ ] Register swept (Elfland test)
- [ ] Read each box aloud once before the session; cut any stumble
