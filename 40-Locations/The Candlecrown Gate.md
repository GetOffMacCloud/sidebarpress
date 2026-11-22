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

# The Candlecrown Gate

> The only way onto the crown: a timber gate in a drystone wall at the head of the Candle Stair, with the warden's hut beside it.

> [!abstract]- Quick edit (Meta Bind)
> Kind `INPUT[template-location-kind][:kind]` · Place district `INPUT[template-place-category][:category]` · Point-of-interest type `INPUT[template-poi-type][:category]`
> In `INPUT[suggester(optionQuery("40-Locations"), optionQuery("20-World/Regions")):parent_location]` · Region `INPUT[suggester(optionQuery("20-World/Regions"), optionQuery("20-World/Greyhawk-Canon")):region]`

## Description
> *A timber gate, iron-strapped and frosted white, stands in a waist-high drystone wall. A line of salt runs under it, crusted with snow. Beside it, a one-room hut with a smoking chimney and a lantern on a ten-foot pole leaning by the door.*

## Notable Features
- **The salt line:** Mother Sedge renews the hallowing every Needfest; the founders hallowed the whole crown as "one house," so the gate is a threshold the undead can't cross uninvited (see [[Aurel Vasch]]).
- **The gate bell:** an old mine bell on a frame; it rings for wagons, for weddings and, this winter, for tyrgs.
- **The warden's hut:** two cots, a stove, a slate of the day's comings and goings, Tansy's cup of milk on the outside sill.

## Inhabitants
`BUTTON[button_person]`
- [[Dob Kettle]] (gate-warden) and [[Tansy Kettle]].
- The gate-watch (6): Dob; Jakob and Lute Vossmer; Rolf Holm; Brom Carrow; Tam Amberson.

NPC notes whose `location` is this place:

```dataview
TABLE WITHOUT ID file.link AS "Name", occupation AS "Occupation", status AS "Status"
FROM "30-NPCs" WHERE contains(string(location), this.file.name)
SORT file.name ASC
```

## History
*Homebrew.* The founders built the wall and gate the year they came up out of the mine.

## Rumors
Tansy says the cold man on the cliff "says thank you for the milk."

## Adventure Use
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — [[Scene 01 — The Candle Stair]] (arrival), [[Scene 06 — Dusk on the Stair]] (wave 1), [[Scene 08 — The Knock at the Gate]], [[Scene 10 — The Long Night]] (wave 3).

## Map Reference
M2 Candlecrown (see [[SP-GS02 — Map Assets]]).

## Canon Notes
Homebrew.
