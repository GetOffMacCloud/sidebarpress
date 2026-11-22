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

# The Lantern Workshop

> Candlecrown's lantern-and-toy workshop, the reason the hamlet exists, with the elder's office, the wool loft and the coal-store hatch into the old mine.

> [!abstract]- Quick edit (Meta Bind)
> Kind `INPUT[template-location-kind][:kind]` · Place district `INPUT[template-place-category][:category]` · Point-of-interest type `INPUT[template-poi-type][:category]`
> In `INPUT[suggester(optionQuery("40-Locations"), optionQuery("20-World/Regions")):parent_location]` · Region `INPUT[suggester(optionQuery("20-World/Regions"), optionQuery("20-World/Greyhawk-Canon")):region]`

## Description
> *Long benches of carvers, tinsmiths and painters run the length of a timber hall that smells of pine shavings and hot tin. A forge glows at the north end. Needfest figures dry on racks: winter gods with icicle beards, hammer-bearing smiths, a dozen fat geese.*

## Notable Features
- **The forge** (north end): Nell Amberson's tin-bench and Garth Vossmer's carving benches either side.
- **The office:** glassed in; the founders' charter and the miners' map (see [[SP-GS02 — Handout — The Miners' Map]]) hang behind Brannoc's desk.
- **The wool loft:** packing fleece; where Brannoc hides Corin on Needfest 2.
- **The coal store and hatch:** into [[The Old Workings (Candlecrown)]]; the draft lifts the sawdust (Fact 5).
- **The inner store:** windowless; becomes the singing room in [[Scene 09 — The Short Day]].

## Inhabitants
`BUTTON[button_person]`
- [[Brannoc Tull]] (master), [[Pell and Ash]], [[Garth Vossmer]] (master carver), [[Nell Amberson]] (tinsmith), [[Ivo Pike]] (painter), eight journeymen and apprentices who lodge in the hall loft.

NPC notes whose `location` is this place:

```dataview
TABLE WITHOUT ID file.link AS "Name", occupation AS "Occupation", status AS "Status"
FROM "30-NPCs" WHERE contains(string(location), this.file.name)
SORT file.name ASC
```

## History
*Homebrew.* Built over the old mine head when the silver gave out; the coal store was dug into the founders' bricked-up doorway.

## Business
**Selling** (standard coin; Keoish and Yeomanry silver both pass)
| Item | Cost | Weight |
|---|---|---|
| Hooded lantern, Candlecrown make | 5 gp | 2 lb |
| Bullseye lantern | 10 gp | 2 lb |
| Pierced-tin carol lantern (six panes) | 25 gp | 3 lb |
| Painted Needfest figure | 1 gp | — |
| Carved toy goose / tin soldier | 5 sp | — |
| Tin whistle | 2 cp | — |

**Services**
| Service | Cost | Notes |
|---|---|---|
| Lantern repair | 1 sp | while you wait |
| Custom lantern or figure | 10 gp+ | a week; a month at Needfest |

## Rumors
"There's old tunnels under the workshop. Pa nailed the hatch shut when I was six." (Ash)

## Adventure Use
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — [[Scene 02 — Candlecrown at Needfest]] (C3), [[Scene 03 — The Second Day]], [[Scene 04 — The Wind That Sings]] (the tyrg in the workshop), [[Scene 05 — The Old Workings]], [[Scene 10 — The Long Night]] (wave 2).

## Map Reference
M2 Candlecrown (see [[SP-GS02 — Map Assets]]).

## Canon Notes
Homebrew.
