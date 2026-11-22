---
type: region
canon: false
parent: "" # the continent or larger realm, as a link
climate: ""
seasons: ""
dominant_peoples: []
sovereignty: "" # who rules it in 576 CY
aliases: []
tags: [region]
---

# {{region}}

> One line: the land, who holds it, and what it's like to travel through.

## General
The region's description. Lead with what a traveler notices, not a gazetteer.

## Details
- **Dominant peoples:**
- **Climate and seasons:**
- **Rulers and powers:**
- **Coin, faiths, customs:**

## Hubs
Places where people live: cities, towns, villages, hamlets, encampments, keeps (any `type: settlement` note with `region` set to this region).

```dataview
TABLE WITHOUT ID file.link AS "Hub", category AS "Type", population AS "Population"
FROM ""
WHERE type = "settlement" AND contains(string(region), this.file.name)
SORT file.name ASC
```

## Points of Interest
Places that can be explored (any `type: location` note with `region` set to this region).

```dataview
TABLE WITHOUT ID file.link AS "Place", kind AS "Kind", category AS "Category"
FROM ""
WHERE type = "location" AND contains(string(region), this.file.name)
SORT file.name ASC
```

## Groups
Groups of people and power: churches, cults, guilds, companies (any `type: faction` note with `territory` set to this region).

```dataview
LIST FROM "" WHERE type = "faction" AND contains(string(territory), this.file.name)
```

## Quests
```dataview
TABLE WITHOUT ID file.link AS "Quest", status AS "Status", giver AS "Giver"
FROM "" WHERE type = "quest" AND contains(string(location), this.file.name)
```

## GM Notes
What you need to track in the region.

## Adventure Use
- [[SP-GANN-Title]] — how it's used

## Canon Notes
Edition, book and page; deviations marked *(homebrew)*. If the region is canon, link its Lore note in `20-World/Greyhawk-Canon` instead of duplicating it.
