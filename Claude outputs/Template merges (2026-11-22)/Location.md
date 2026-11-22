---
type: location
canon: false
kind: place # place (a building or business in a settlement) | point-of-interest (somewhere to explore) | site (a keyed dungeon or lair) | landmark
category: "" # place: commerce | agriculture | military | philosophy | industrial | nesting | government · point-of-interest: encounter | dungeon | lair | ruin | shrine | camp
region: ""
parent_location: "" # link to the Settlement or Region it sits in
aliases: []
tags: []
---

# {{name}}

> One-line description.

## Description
What the PCs see, hear, smell. Boxed text goes here.

## Notable Features
## Inhabitants
- [[NPC Name]]

NPC notes whose `location` is this place:

```dataview
TABLE WITHOUT ID file.link AS "Name", occupation AS "Occupation", status AS "Status"
FROM "30-NPCs" WHERE contains(string(location), this.file.name)
SORT file.name ASC
```

## History
Canon history linked; homebrew history marked.

## Business (places only; delete otherwise)
**Selling**
| Item | Cost | Weight |
|---|---|---|
| | | |

**Buying**
| Item | Pays | Notes |
|---|---|---|
| | | |

**Services**
| Service | Cost | Notes |
|---|---|---|
| | | |

## Exploring (points of interest only; delete otherwise)
- **Approach:** what the party sees before they arrive.
- **Interior / areas:** short subsections, or a link to a [[Site-Key]] note.
- **Encounter:** creatures here (count), and the bestiary note.
- **Quests tied here:**

## Travel
| Destination | Miles | Days on foot (24 mi/day) | Days mounted (48 mi/day) |
|---|---|---|---|
| [[Next place]] | | | |

## Rumors
What the party might overhear here.

## GM Notes

## Adventure Use
- [[SP-GANN-Title]] — how it's used

## Map Reference
Link to asset in `99-Assets`, or FG map name.

## Canon Notes
Edition/book/page citations. Deviations documented.
