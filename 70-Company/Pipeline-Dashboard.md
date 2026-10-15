---
type: dashboard
---

# Pipeline Dashboard

## Adventures
```dataview
TABLE WITHOUT ID
  file.link AS "Adventure",
  adventure AS "Code",
  status AS "Status",
  levels AS "Levels",
  in_world_date AS "In-world date",
  estimated_hours AS "Hours"
FROM "10-Adventures"
WHERE type = "adventure" AND adventure != "A00"
SORT adventure ASC
```

## Scene progress
```dataview
TABLE WITHOUT ID
  adventure AS "Code",
  length(rows) AS "Scenes",
  length(filter(rows.status, (s) => s = "drafted")) AS "Drafted",
  length(filter(rows.status, (s) => s = "edited")) AS "Edited",
  length(filter(rows.status, (s) => s = "final")) AS "Final"
FROM "10-Adventures"
WHERE type = "scene" AND publish = true
GROUP BY adventure
SORT adventure ASC
```

## Open board cards
```dataview
TASK
FROM "10-Adventures"
WHERE contains(file.name, "Board") AND !completed
GROUP BY file.link
```

## Files missing manifest keys
```dataview
LIST
FROM "10-Adventures"
WHERE (type = "scene" OR type = "adventure" OR type = "bestiary" OR type = "handout" OR type = "adventure-mechanic") AND (!section OR !publish_order OR !adventure)
```
