---
type: location
canon: false
kind: place
category: Commerce
region: '[[The-Tors]]'
parent_location: '[[Candlecrown]]'
aliases: []
tags: [candlecrown, sp-gs02]
---

# The Teller Storehouse

> The village granary and storehouse, kept by the Tellers, where the Needfest gift ledger and the founders' keys are kept.

> [!abstract]- Quick edit (Meta Bind)
> Kind `INPUT[template-location-kind][:kind]` · Place district `INPUT[template-place-category][:category]` · Point-of-interest type `INPUT[template-poi-type][:category]`
> In `INPUT[suggester(optionQuery("40-Locations"), optionQuery("20-World/Regions")):parent_location]` · Region `INPUT[suggester(optionQuery("20-World/Regions"), optionQuery("20-World/Greyhawk-Canon")):region]`

## Description
> *A thick-walled stone storehouse with a heavy door and a slate by it listing what's inside: barley, salt fish, honey, cheeses, candles, wool.*

## Notable Features
- **The gift ledger:** every lantern and toy owed to every valley farm and Loftwick buyer, including Ardo Pennick's order (hook 1).
- **The keys:** to the gate, the storehouse, the oil-house and (Osric thinks) a door "down below" nobody has opened in his lifetime.
- **Winter stores:** enough for 60 people for six weeks.

## Inhabitants
`BUTTON[button_person]`
- [[Osric Teller]] and his family.

NPC notes whose `location` is this place:

```dataview
TABLE WITHOUT ID file.link AS "Name", occupation AS "Occupation", status AS "Status"
FROM "30-NPCs" WHERE contains(string(location), this.file.name)
SORT file.name ASC
```

## History
*Homebrew.*

## Business
**Selling** (to guests, at cost during Needfest)
| Item | Cost | Weight |
|---|---|---|
| Winter rations (1 day) | 5 sp | 2 lb |
| Candles (10) | 1 sp | — |
| Wool blanket | 5 sp | 3 lb |
| Cold-weather cloak | 5 gp | 4 lb |

## GM Notes
The key Osric can't place is the old key to the miners' chapel (M5). It fits.

## Adventure Use
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — background; Osric is an information carrier in [[Candlecrown]].

## Map Reference
M2 Candlecrown (see [[SP-GS02 — Map Assets]]).

## Canon Notes
Homebrew.
