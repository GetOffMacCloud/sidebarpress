---
type: location
canon: false
kind: place
category: Nesting
region: '[[The-Tors]]'
parent_location: '[[Candlecrown]]'
aliases: []
tags: [candlecrown, sp-gs02]
---

# Candlecrown Green

> The open crown between the hall and the gate, where the feast tables stand under sailcloth and, on Midwinter Night, the bonfire goes up.

> [!abstract]- Quick edit (Meta Bind)
> Kind `INPUT[template-location-kind][:kind]` · Place district `INPUT[template-place-category][:category]` · Point-of-interest type `INPUT[template-poi-type][:category]`
> In `INPUT[suggester(optionQuery("40-Locations"), optionQuery("20-World/Regions")):parent_location]` · Region `INPUT[suggester(optionQuery("20-World/Regions"), optionQuery("20-World/Greyhawk-Canon")):region]`

## Description
> *A trampled square of snow between the hall and the gate, with long trestle tables under a sailcloth awning heavy with snow. Lantern posts march away along the rim in both directions.*

## Notable Features
- **The feast tables** (Needfest 1–7).
- **The bonfire spot** (Scene 09).
- **The lantern line:** 24 iron posts around the rim; 12 lit on the Stair and workshop sides at the start ([[SP-GS02 — The Lantern Line]]).

## Inhabitants
`BUTTON[button_person]`
- Everyone, at mealtimes; [[Marra Fallow]] runs the feast.

NPC notes whose `location` is this place:

```dataview
TABLE WITHOUT ID file.link AS "Name", occupation AS "Occupation", status AS "Status"
FROM "30-NPCs" WHERE contains(string(location), this.file.name)
SORT file.name ASC
```

## History
*Homebrew.*

## Adventure Use
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — [[Scene 02 — Candlecrown at Needfest]] (C6), [[Scene 09 — The Short Day]] (the bonfire), [[Scene 10 — The Long Night]].

## Map Reference
M2 Candlecrown (see [[SP-GS02 — Map Assets]]).

## Canon Notes
Homebrew.
