---
type: location
canon: false
kind: place
category: Industrial
region: '[[The-Tors]]'
parent_location: '[[Candlecrown]]'
aliases: []
tags: [candlecrown, sp-gs02]
---

# The Carrow Oil-House

> Edda Carrow's rendering shed and cooperage, where Candlecrown's lantern oil is pressed, barreled and stored: 40 gallons of it this winter.

> [!abstract]- Quick edit (Meta Bind)
> Kind `INPUT[template-location-kind][:kind]` · Place district `INPUT[template-place-category][:category]` · Point-of-interest type `INPUT[template-poi-type][:category]`
> In `INPUT[suggester(optionQuery("40-Locations"), optionQuery("20-World/Regions")):parent_location]` · Region `INPUT[suggester(optionQuery("20-World/Regions"), optionQuery("20-World/Greyhawk-Canon")):region]`

## Description
> *A low stone shed that smells of tallow and pitch. Barrels are stacked to the roof, each stenciled with a lantern. A press and a copper stand against the back wall.*

## Notable Features
- **The oil store:** 40 gallons in 2-pint flasks (160 flasks); the siege's ammunition ([[SP-GS02 — The Lantern Line]]).
- **Rope:** the length that would fix the winch.
- **Fire pots:** the clay pots for Scene 09 come from here.

## Inhabitants
`BUTTON[button_person]`
- [[Edda Carrow]], her husband Brom (gate-watch) and three children.

NPC notes whose `location` is this place:

```dataview
TABLE WITHOUT ID file.link AS "Name", occupation AS "Occupation", status AS "Status"
FROM "30-NPCs" WHERE contains(string(location), this.file.name)
SORT file.name ASC
```

## History
*Homebrew.*

## Business
**Selling**
| Item | Cost | Weight |
|---|---|---|
| Lantern oil (flask) | 1 sp | 1 lb |
| Barrel (empty) | 2 gp | 70 lb |
| Rope, hempen (50 ft.) | 1 gp | 10 lb |

## GM Notes
Edda counts every flask. A party that takes oil without asking hears about it at supper.

## Adventure Use
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — supplies the lantern oil for [[Scene 09 — The Short Day]] and [[Scene 10 — The Long Night]].

## Map Reference
M2 Candlecrown (see [[SP-GS02 — Map Assets]]).

## Canon Notes
Homebrew.
