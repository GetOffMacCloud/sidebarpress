---
type: quest
status: not-started # not-started | in-progress | complete | failed | abandoned
giver: "" # link to an NPC note
location: "" # where the quest was given (link)
obtained: "" # in-world date (CY)
session_obtained: "" # link to a session log
loot_available: []
loot_earned: []
adventure: "" # SP-GANN, if it belongs to one
tags: [quest]
---

# {{quest}}

> One line: what the party has been asked to do, and by whom.

## Quest Info
- [ ] Obtain the quest
- [ ] ___
- [ ] Complete the quest
- [ ] Collect the reward

## Details
- **Giver:** · **Where:** · **When (CY):** · **Session:**
- **Reward offered:** · **Reward earned:**

## Backstory
Why it matters, and why the party should care.

## Planning
How it might play out: routes, people to meet, places to go.

## People
NPC notes that link to this quest (`connected_quests`).

```dataview
TABLE WITHOUT ID file.link AS "Name", occupation AS "Role", location AS "Location"
FROM "30-NPCs" WHERE contains(string(connected_quests), this.file.name)
```

## GM Notes

## Continuity
Plot threads it opens or advances: [[Plot-Threads]].
