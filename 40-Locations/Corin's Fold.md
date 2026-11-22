---
type: location
canon: false
kind: place
category: Agriculture
region: '[[The-Tors]]'
parent_location: '[[Candlecrown]]'
aliases: []
tags: [candlecrown, sp-gs02]
---

# Corin's Fold

> A drystone sheepfold and one-room hut on the east rim, the farthest building from the hall: where the first voice is taken.

> [!abstract]- Quick edit (Meta Bind)
> Kind `INPUT[template-location-kind][:kind]` · Place district `INPUT[template-place-category][:category]` · Point-of-interest type `INPUT[template-poi-type][:category]`
> In `INPUT[suggester(optionQuery("40-Locations"), optionQuery("20-World/Regions")):parent_location]` · Region `INPUT[suggester(optionQuery("20-World/Regions"), optionQuery("20-World/Greyhawk-Canon")):region]`

## Description
> *A drystone wall in a horseshoe against the wind, forty sheep huddled in its lee. A one-room hut with a turf roof. A crook leans by the door. Two lantern posts at the rim beyond are dark.*

## Notable Features
- The east rim drops 400 feet to the scree.
- Hrimvald's rune on the rim stones melts under a flame (Fact 2).
- Biscuit, Corin's dog, won't leave the fold.

## Inhabitants
`BUTTON[button_person]`
- [[Corin the Shepherd]] (alone).

NPC notes whose `location` is this place:

```dataview
TABLE WITHOUT ID file.link AS "Name", occupation AS "Occupation", status AS "Status"
FROM "30-NPCs" WHERE contains(string(location), this.file.name)
SORT file.name ASC
```

## History
*Homebrew.*

## Adventure Use
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — [[Scene 02 — Candlecrown at Needfest]] (C8), [[Scene 03 — The Second Day]] (the empty fold), [[Scene 04 — The Wind That Sings]] (the east rim).

## Map Reference
M2 Candlecrown (see [[SP-GS02 — Map Assets]]).

## Canon Notes
Homebrew.
