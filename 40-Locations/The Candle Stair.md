---
type: location
canon: false
kind: point-of-interest
category: Crossing
region: '[[The-Tors]]'
parent_location: '[[Candlecrown]]'
aliases: []
tags: [path, cliff, the-tors, sp-gs02]
---

# The Candle Stair

> The only path up to Candlecrown: six switchbacks cut into a 400-foot cliff, 5 to 10 feet wide, with a sheer drop on the outside.

> [!abstract]- Quick edit (Meta Bind)
> Kind `INPUT[template-location-kind][:kind]` · Place district `INPUT[template-place-category][:category]` · Point-of-interest type `INPUT[template-poi-type][:category]`
> In `INPUT[suggester(optionQuery("40-Locations"), optionQuery("20-World/Regions")):parent_location]` · Region `INPUT[suggester(optionQuery("20-World/Regions"), optionQuery("20-World/Greyhawk-Canon")):region]`

## Description
> *A path is cut into the tor's face in tight switchbacks, barely wide enough for a cart.*

## Notable Features
- Six switchbacks with 20-foot landings at the turns; difficult terrain in snow.
- The edge rule (falls to the switchback below, 1d4 × 10 feet): see [[SP-GS02 — The Lantern Line]].
- Switchback 3: the frozen mules and the first ice rune. Switchback 5: where the cliff ledge from the mine's mouth joins the path.

## Inhabitants
`BUTTON[button_person]`
- Hrimvald's tyrgs, this winter.

NPC notes whose `location` is this place:

```dataview
TABLE WITHOUT ID file.link AS "Name", occupation AS "Occupation", status AS "Status"
FROM "30-NPCs" WHERE contains(string(location), this.file.name)
SORT file.name ASC
```

## History
*Homebrew.* Cut by the founders' miners; the lantern posts at its head are part of the lantern line.

## Exploring
- **Approach:** from the valley road, two miles of switchbacks in rising snow.
- **Encounter:** tyrgs (4) on switchbacks 4–5 ([[Tyrg]]).

## Travel
| Destination | Miles | Days on foot (24 mi/day) | Days mounted (48 mi/day) |
|---|---|---|---|
| [[Candlecrown]] | 2 (the climb) | 1 hour | — |
| Loftwick | about 30 | 1¼ | ¾ |

## Adventure Use
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — [[Scene 01 — The Candle Stair]] (the climb and the pack), [[Scene 06 — Dusk on the Stair]] (wave 1), [[Scene 10 — The Long Night]] (siege wave 1).

## Map Reference
M1 The Candle Stair (see [[SP-GS02 — Map Assets]]).

## Canon Notes
Homebrew.
