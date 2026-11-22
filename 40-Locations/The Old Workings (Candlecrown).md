---
type: location
canon: false
kind: site
category: Mine
region: '[[The-Tors]]'
parent_location: '[[Candlecrown]]'
aliases: []
tags: [mine, dungeon, suel, the-tors, sp-gs02]
---

# The Old Workings (Candlecrown)

> The worked-out Suel silver mine under Candlecrown, with a sealed chapel to Fortubo and a mouth onto the north cliff.

> [!abstract]- Quick edit (Meta Bind)
> Kind `INPUT[template-location-kind][:kind]` · Place district `INPUT[template-place-category][:category]` · Point-of-interest type `INPUT[template-poi-type][:category]`
> In `INPUT[suggester(optionQuery("40-Locations"), optionQuery("20-World/Regions")):parent_location]` · Region `INPUT[suggester(optionQuery("20-World/Regions"), optionQuery("20-World/Greyhawk-Canon")):region]`

## Description
> *Behind the heaped coal, a doorway of dressed stone has been unbricked, and a passage slopes down into the dark.*

## Notable Features
- Ten keyed areas, M1–M10: see the site key [[SP-GS02 — The Old Workings]].
- The apprentice's chapel (M5): the warning and the counter-verse.
- The hunter's end (M3), the rune-pillar (M7), Aurel's shelter (M8), the silver seam (M9), the cliff mouth (M10).

## Inhabitants
`BUTTON[button_person]`
- [[Aurel Vasch]]; an ice-rune guardian; tyrg scouts at night.

NPC notes whose `location` is this place:

```dataview
TABLE WITHOUT ID file.link AS "Name", occupation AS "Occupation", status AS "Status"
FROM "30-NPCs" WHERE contains(string(location), this.file.name)
SORT file.name ASC
```

## History
*Homebrew.* Sealed by the founders after a Keoish monster-hunter died there seventy years ago.

## Exploring
- **Approach:** through the coal-store hatch in [[The Lantern Workshop]], or the cliff mouth (M10).
- **Areas:** [[SP-GS02 — The Old Workings]].
- **Encounter:** [[Ice-Rune Guardian]] (M7), [[Aurel Vasch]] (M8).

## Adventure Use
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — [[Scene 05 — The Old Workings]]; siege wave 2 in [[Scene 10 — The Long Night]].

## Map Reference
M3 The Old Workings (see [[SP-GS02 — Map Assets]]).

## Canon Notes
Homebrew.
