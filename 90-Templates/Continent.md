---
type: continent
canon: false
aliases: []
tags: [continent]
---

# {{continent}}

> One line: what this landmass is and why it matters to the campaign.

## General
The continent's description: shape, peoples, what everyone knows about it.

## Details
- **Dominant peoples:**
- **Climate:**
- **Great powers:**

## Regions
Regions on this continent (any note with `type: region` and `parent: "[[{{continent}}]]"`).

```dataview
TABLE WITHOUT ID file.link AS "Region", climate AS "Climate", dominant_peoples AS "Peoples"
FROM ""
WHERE type = "region" AND contains(string(parent), this.file.name)
SORT file.name ASC
```

## Capital Cities
Settlements flagged as capitals in this continent's regions.

```dataview
TABLE WITHOUT ID file.link AS "City", region AS "Region", population AS "Population"
FROM ""
WHERE type = "settlement" AND capital = true
SORT file.name ASC
```

## GM Notes
What you need to track at continent scale.

## Canon Notes
Edition, book and page for anything canon; deviations marked *(homebrew)*. Link Lore notes in `20-World/Greyhawk-Canon`.
