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

# The Mine Head (Candlecrown)

> A round stone cap the size of a cart on the north rim, sealing the old Suel shaft; solid since the founders sealed it.

> [!abstract]- Quick edit (Meta Bind)
> Kind `INPUT[template-location-kind][:kind]` · Place district `INPUT[template-place-category][:category]` · Point-of-interest type `INPUT[template-poi-type][:category]`
> In `INPUT[suggester(optionQuery("40-Locations"), optionQuery("20-World/Regions")):parent_location]` · Region `INPUT[suggester(optionQuery("20-World/Regions"), optionQuery("20-World/Greyhawk-Canon")):region]`

## Description
> *A round cap of fitted stone the size of a cart, with a rusted iron ring, half-buried in snow at the north rim.*

## Notable Features
- Sealed with rubble two generations ago, by order of the founders (see [[Aldo Holm]], whose grandfather did it).
- It is solid; the only open way down is the coal store in [[The Lantern Workshop]].

## Inhabitants
`BUTTON[button_person]`
- None.

NPC notes whose `location` is this place:

```dataview
TABLE WITHOUT ID file.link AS "Name", occupation AS "Occupation", status AS "Status"
FROM "30-NPCs" WHERE contains(string(location), this.file.name)
SORT file.name ASC
```

## History
*Homebrew.* The original Suel shaft head; the shaft runs down to the silver seam (M9).

## Adventure Use
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — [[Scene 02 — Candlecrown at Needfest]] (C9); the shaft is M2 in [[SP-GS02 — The Old Workings]].

## Map Reference
M2 Candlecrown (see [[SP-GS02 — Map Assets]]).

## Canon Notes
Homebrew.
