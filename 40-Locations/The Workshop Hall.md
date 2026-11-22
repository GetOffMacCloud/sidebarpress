---
type: location
canon: false
kind: place
category: Government
region: '[[The-Tors]]'
parent_location: '[[Candlecrown]]'
aliases: []
tags: [candlecrown, sp-gs02]
---

# The Workshop Hall

> The great timber hall joined to the workshop, where the village meets, feasts and sings the Long Night Carol, with the Carol Lantern over the hearth.

> [!abstract]- Quick edit (Meta Bind)
> Kind `INPUT[template-location-kind][:kind]` · Place district `INPUT[template-place-category][:category]` · Point-of-interest type `INPUT[template-poi-type][:category]`
> In `INPUT[suggester(optionQuery("40-Locations"), optionQuery("20-World/Regions")):parent_location]` · Region `INPUT[suggester(optionQuery("20-World/Regions"), optionQuery("20-World/Greyhawk-Canon")):region]`

## Description
> *Rafters hung with lanterns of every kind the village has ever made. Benches for forty singers face a great stone hearth. Over the fire turns a six-sided lantern of pierced tin, its painted panes throwing colored light across the room.*

## Notable Features
- **The Carol Lantern:** six panes painted with the six Common verses (see [[The Long Night Lantern]], its twin). There is no seventh pane.
- **The benches:** forty places; the choir track counts from here ([[SP-GS02 — The Lantern Line]]).
- **The hall loft:** where the journeymen sleep and the party lodges.
- **The north wall:** 30 feet from the north rim; Hrimvald's approach in the climax.

## Inhabitants
`BUTTON[button_person]`
- [[Wenna Tull]] leads the choir; [[Old Mother Sedge]] leads the seventh verse.

NPC notes whose `location` is this place:

```dataview
TABLE WITHOUT ID file.link AS "Name", occupation AS "Occupation", status AS "Status"
FROM "30-NPCs" WHERE contains(string(location), this.file.name)
SORT file.name ASC
```

## History
*Homebrew.* The village has sung the carol here every Midwinter Night since the founders.

## Adventure Use
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — [[Scene 02 — Candlecrown at Needfest]] (C4), [[Scene 07 — The Rehearsal]], [[Scene 10 — The Long Night]], [[Scene 11 — The Seventh Verse]].

## Map Reference
M2 Candlecrown (see [[SP-GS02 — Map Assets]]).

## Canon Notes
Homebrew.
