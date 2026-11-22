---
type: location
canon: false
kind: place
category: Philosophy
region: '[[The-Tors]]'
parent_location: '[[Candlecrown]]'
aliases: []
tags: [candlecrown, sp-gs02]
---

# Mother Sedge's Shrine

> A windbreak cave cut into a knuckle of rock beside the hall: Candlecrown's shrine to Telchur, the warmest stone on the crown.

> [!abstract]- Quick edit (Meta Bind)
> Kind `INPUT[template-location-kind][:kind]` · Place district `INPUT[template-place-category][:category]` · Point-of-interest type `INPUT[template-poi-type][:category]`
> In `INPUT[suggester(optionQuery("40-Locations"), optionQuery("20-World/Regions")):parent_location]` · Region `INPUT[suggester(optionQuery("20-World/Regions"), optionQuery("20-World/Greyhawk-Canon")):region]`

## Description
> *A low cave mouth in the rock, hung with a felt curtain. Inside, a leafless tree is carved on the back wall over a bare stone altar. A brazier burns without smoke. The air is warm.*

## Notable Features
- **The safety valve:** tyrgs won't enter; the cold save is never needed inside ([[SP-GS02 — The Lantern Line#The Safety Valve]]).
- **The brazier:** never goes out; Mother Sedge says it was lit by the founders and has never been relit.
- **Mother Sedge's cottage:** a stone room built onto the cave mouth; she sleeps in the shrine itself in winter.

## Inhabitants
`BUTTON[button_person]`
- [[Old Mother Sedge]]

NPC notes whose `location` is this place:

```dataview
TABLE WITHOUT ID file.link AS "Name", occupation AS "Occupation", status AS "Status"
FROM "30-NPCs" WHERE contains(string(location), this.file.name)
SORT file.name ASC
```

## History
*Homebrew.* A permanent "natural temple" to [[Telchur]], unusual for his faith, whose windbreak shrines are usually rebuilt each autumn.

## Adventure Use
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — [[Scene 02 — Candlecrown at Needfest]] (C5), [[Scene 03 — The Second Day]] (Mother Sedge's truth), [[Scene 10 — The Long Night]] (the safety valve).

## Map Reference
M2 Candlecrown, C5.

## Canon Notes
Homebrew.
