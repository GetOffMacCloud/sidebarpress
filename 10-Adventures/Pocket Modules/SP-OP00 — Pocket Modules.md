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
- **Standard extras (from OP1):** player handouts (built in Canva); a "Drop it in" sidebar (no named settings); a rumor table (d6); a Running It at Other Levels box (APL −2 / +2); a Stream Twists table (d6) for chat; a sequel seed.
- **Locations are setting-agnostic.** Write only the history of the place, its buildings and its denizens.
- **Play:** one 4-hour session, APL set per module, 4–6 characters, scaling for 4 / 5 / 6 PCs.
- **Fights:** standard fights that push the party to its limits, plus one avoidable problem the party has to manage or the session gets much harder (OP1: Wandering Husks, which are Hard fights; the Larder heals the boss).
- **Day budget:** set fights land at 75–85% of the DMG adventuring day; the avoidable problem pushes it to about 100% if the party ignores it.
- **Maps:** one painted CharGen battlemap per fight area (built from an ink layout reference), an ink DM map of the climax, and an ink site key.
- **Build:** vault notes, then the Claude doc for the post, then an FGU module from `FGU Kit/build/module.py`.

## House template (adopted 2026-11-16)
Templates: `90-Templates/Pocket-Module.md` (module) and `90-Templates/Pocket-Module-Scene.md` (scenes). Adopted from a review of the Adventurers League house style (ELW-01 *Murder in Skyway*, ELW-02 *The Boromar Ball*). Every Pocket Module now carries:
- **Front matter:** APL, **tier**, estimated duration; **Story Objective** and **Bonus Objective**; an **adventure flowchart**; a **How Will You Play?** box (short session, long session, combat-heavy, roleplay-heavy, streamed).
- **Scene header block:** Estimated Duration · Location · Prerequisites · Objectives.
- **Area Information:** Dimensions & Terrain · Lighting · sounds and smells.
- **Creatures/NPCs:** each with *Objectives/Goals* and *What do they know?*; inline notation **Name** (alignment sex race **statblock**).
- **Developments**, **Treasure & Rewards**, and a **Playing the Pillars** box (Combat / Exploration / Social) in every scene.
- **Appendices:** NPC Summary (pronunciation; Personality / Ideal / Bond / Flaw), Adventure Flowchart, Bestiary, Spell, Item, maps, player handouts (one in-world map handout where the story allows).
- **A Story Award** and **a Bonus Objective**, each in its own note.
- **A Ritterstadt Rewards note** for Greyhawk University play: APL × 100 credits each, outcome percentages, extra credit, lead credits, Buy-Back values, a Loadout Package. Rules: [[The Tuition & Leveling Table]] (rule set 2026-11-16).
- **Credits & legal** block with the SRD 5.1 CC-BY-4.0 attribution.
- Not adopted: AL's "weak/strong party" boxes (our 4 / 5 / 6 PC encounter tables cover it) and AL downtime/renown (not used here).

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
| OP1 / SP-OP01 | [[SP-OP01-What-the-Dead-Fear\|What the Dead Fear]] | November 2026 | 6–8 (APL 7) | draft; maps done; house template applied |

## Open threads
- OP1's **Ossian escapes** ending opens *The face on the road*: a possible OP2 seed.
