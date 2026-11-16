---
type: series-hub
adventure: "SP-OP00"
section: internal
publish_order: 0
publish: false
title: "Pocket Modules"
created: 2026-11-16
tags: [pocket-module, series-hub, monthly]
---

# Pocket Modules (OP)

The monthly **Sidebar Press Pocket Module**: one session, setting-agnostic, 2014 5e. Code line **OP** (O for Open, P for Pocket Module), printed **OP1**, vault key **SP-OP01**. See `claude/module-codes.md` in the project.

## The format
- **Post:** about three pages plus a stat-block page, as a Claude doc. A guide, not a hard limit.
- **Contents:** the adventure; maps; one custom monster; one custom item; one custom spell; a write-up of the main location and the main NPC.
- **Play:** one 4-hour session, APL set per module, 4–6 characters, scaling for 4 / 5 / 6 PCs.
- **Fights:** standard fights that push the party to its limits, plus one avoidable problem the party has to manage or the session gets much harder (OP1: Wandering Husks, which are Hard fights; the Larder heals the boss).
- **Day budget:** set fights land at 75–85% of the DMG adventuring day; the avoidable problem pushes it to about 100% if the party ignores it.
- **Maps:** one painted CharGen battlemap per fight area (built from an ink layout reference), an ink DM map of the climax, and an ink site key.
- **Build:** vault notes, then the Claude doc for the post, then an FGU module from `FGU Kit/build/module.py`.

## Modules
```dataview
TABLE WITHOUT ID
  file.link AS "Module",
  adventure AS "Code",
  levels AS "Levels",
  status AS "Status"
FROM "10-Adventures/Pocket Modules"
WHERE type = "adventure"
SORT adventure ASC
```

| Code | Title | Post | Levels | Status |
|---|---|---|---|---|
| OP1 / SP-OP01 | [[SP-OP01-What-the-Dead-Fear\|What the Dead Fear]] | November 2026 | 6–8 (APL 7) | draft; maps done |

## Open threads
- OP1's **Ossian escapes** ending opens *The face on the road*: a possible OP2 seed.
