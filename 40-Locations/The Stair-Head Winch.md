---
type: location
canon: false
kind: place
category: Military
region: '[[The-Tors]]'
parent_location: '[[Candlecrown]]'
aliases: []
tags: [candlecrown, sp-gs02]
---

# The Stair-Head Winch

> A timber crane and windlass on the east rim for hauling crates up from the valley road; its rope snapped in the frost on Sunsebb 26.

> [!abstract]- Quick edit (Meta Bind)
> Kind `INPUT[template-location-kind][:kind]` · Place district `INPUT[template-place-category][:category]` · Point-of-interest type `INPUT[template-poi-type][:category]`
> In `INPUT[suggester(optionQuery("40-Locations"), optionQuery("20-World/Regions")):parent_location]` · Region `INPUT[suggester(optionQuery("20-World/Regions"), optionQuery("20-World/Greyhawk-Canon")):region]`

## Description
> *A timber crane leans out over the drop, its rope hanging snapped and stiff with ice. Below, far down at the foot of the cliff, crates lie half-buried in snow.*

## Notable Features
- The windlass needs four people to turn. The rope can be spliced (DC 12 tool check, 1 hour) once a new length is found (the Carrow oil-house has one).
- The crates of oil-wicks for the full lantern line are at the foot of the cliff (see [[Scene 03 — The Second Day]] and [[Scene 09 — The Short Day]]).

## Inhabitants
`BUTTON[button_person]`
- Worked by whoever is strongest; Garth Vossmer's sons, usually.

NPC notes whose `location` is this place:

```dataview
TABLE WITHOUT ID file.link AS "Name", occupation AS "Occupation", status AS "Status"
FROM "30-NPCs" WHERE contains(string(location), this.file.name)
SORT file.name ASC
```

## History
*Homebrew.*

## Adventure Use
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — [[Scene 03 — The Second Day]] (the crates), [[Scene 09 — The Short Day]] (Fetch the crates).

## Map Reference
M2 Candlecrown (see [[SP-GS02 — Map Assets]]).

## Canon Notes
Homebrew.
