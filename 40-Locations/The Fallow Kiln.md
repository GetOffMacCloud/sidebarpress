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

# The Fallow Kiln

> Hob Fallow's glass kiln, where every pane in every Candlecrown lantern is blown and cut.

> [!abstract]- Quick edit (Meta Bind)
> Kind `INPUT[template-location-kind][:kind]` · Place district `INPUT[template-place-category][:category]` · Point-of-interest type `INPUT[template-poi-type][:category]`
> In `INPUT[suggester(optionQuery("40-Locations"), optionQuery("20-World/Regions")):parent_location]` · Region `INPUT[suggester(optionQuery("20-World/Regions"), optionQuery("20-World/Greyhawk-Canon")):region]`

## Description
> *A beehive kiln of brick, warm right through, with racks of cooling glass panes in every color: amber, green, a deep winter blue.*

## Notable Features
- The only other fire that never goes out on the crown (besides the shrine's).
- Spare panes: 200, in racks.

## Inhabitants
`BUTTON[button_person]`
- [[Hob Fallow]] and [[Marra Fallow]], and their three children.

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
| Lantern pane, clear | 2 sp | — |
| Lantern pane, colored | 5 sp | — |
| Glass bottle | 2 gp | 2 lb |

## Rumors
"Snow this early means Telchur's angry. We've been slack with the shrine." (Hob)

## Adventure Use
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — [[Scene 02 — Candlecrown at Needfest]] (C7, the Fallows); a possible victim in Scene 02 beat 5.

## Map Reference
M2 Candlecrown (see [[SP-GS02 — Map Assets]]).

## Canon Notes
Homebrew.
