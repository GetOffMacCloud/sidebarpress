---
type: location
canon: false
kind: point-of-interest
category: Cave
region: '[[The-Tors]]'
parent_location: '[[The-Tors]]'
aliases: []
tags: [cave, dungeon, immoth, the-tors, sp-gs02]
---

# The Ice Library

> Hrimvald the Gatherer's cave in the high Tors, where it keeps the words and voices it has taken as runes on shelves of ice.

> [!abstract]- Quick edit (Meta Bind)
> Kind `INPUT[template-location-kind][:kind]` · Place district `INPUT[template-place-category][:category]` · Point-of-interest type `INPUT[template-poi-type][:category]`
> In `INPUT[suggester(optionQuery("40-Locations"), optionQuery("20-World/Regions")):parent_location]` · Region `INPUT[suggester(optionQuery("20-World/Regions"), optionQuery("20-World/Greyhawk-Canon")):region]`

## Description
> *A cave mouth opens in a wall of blue ice. Wind pours out of it, and with the wind come voices.*

## Notable Features
- I1 the Mouth, I2 the Door of Words, I3 the Gallery of Runes, I4 the Still Pool, I5 Hrimvald's Hearth, I6 the Old Hoard: see [[Scene 13 — The Ice Library]].

## Inhabitants
`BUTTON[button_person]`
- [[Hrimvald the Gatherer]]; an ice-rune guardian.

NPC notes whose `location` is this place:

```dataview
TABLE WITHOUT ID file.link AS "Name", occupation AS "Occupation", status AS "Status"
FROM "30-NPCs" WHERE contains(string(location), this.file.name)
SORT file.name ASC
```

## History
*Homebrew.* Two days east and up from Candlecrown in winter.

## Exploring
- **Approach:** two days on foot east and up from Candlecrown (DC 12 Survival each day).
- **Encounter:** [[Ice-Rune Guardian]] (I2), [[Immoth]] (I5).

## Travel
| Destination | Miles | Days on foot (24 mi/day) | Days mounted (48 mi/day) |
|---|---|---|---|
| [[Candlecrown]] | about 30 | 2 (winter) | — |

## Adventure Use
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — [[Scene 13 — The Ice Library]] (optional Session 4, or a spring rescue).

## Map Reference
M4 The Ice Library (see [[SP-GS02 — Map Assets]]).

## Canon Notes
Homebrew.
