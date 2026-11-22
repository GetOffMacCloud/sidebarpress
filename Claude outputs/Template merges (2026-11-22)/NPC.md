---
type: npc
status: alive # alive | dead | missing | unknown
canon: false
faction: ""
location: "" # link to the Settlement or Location note where they live
aliases: []
species: "" # link to a Sapient-Species note, or plain text
gender: ""
age: "" # child | young | adult | middle-aged | old | venerable
alignment: ""
occupation: ""
adventure_role: "" # ally | patron | rival | villain | informant | color
disposition: neutral # friendly | neutral | wary | hostile
party_trust: 0 # 0 stranger · 1 regular · 2 friend
items: [] # links to Item notes
connected_quests: [] # links to Quest notes
connected_groups: [] # links to Faction notes
parents: []
partner: []
children: []
siblings: []
allies: []
enemies: []
deceased_date: "" # CY
tags: []
---

# {{name}}

> One-line identity: who they are at a glance, the impression they leave on the party.

## Appearance
One or two physical details that are easy to recall and describe at the table.

## Personality & Mannerisms
How they talk, move and behave. Habits, tics, tells.

## Goals & Secrets
- **Wants (publicly):** what they want the party to believe about them.
- **The real story:** what's actually going on beneath the surface.
- **Knows but won't say:**
- **Fears:**
- **How to reveal it:** the condition or trigger that makes them open up.

## Role & Context
What purpose they serve in the adventure, and what would break if they were gone. How they connect to the larger campaign.

## Conversation Guide
| Topic | Freely discussed? | Notes / sample line |
|---|:---:|---|
| The current hook | | |
| The local area | | |
| Their faction or group | | |
| Other NPCs they know | | |
| Personal history | | |

**Trust-gated information:**
- **Stranger (0):** what a newcomer gets.
- **Regular (1):** what they share after a few genuine interactions.
- **Friend (2):** what only a trusted party hears.

## Services
| Service | Cost / notes |
|---|---|
| | |

## Quest Hooks
| Hook | Leads to | Trigger |
|---|---|---|
| | | |

## Relationships
Fill the frontmatter lists (parents, partner, children, siblings, allies, enemies) with links; they show here.

```dataview
TABLE WITHOUT ID parents AS "Parents", partner AS "Partner", children AS "Children", siblings AS "Siblings", allies AS "Allies", enemies AS "Enemies"
WHERE file.path = this.file.path
```

| NPC | Relationship | Notes |
|---|---|---|
| | | |

## Inventory
Items they carry (frontmatter `items`).

```dataview
LIST FROM "50-Items" WHERE contains(this.items, file.link)
```

## Stat Block
Link or reference: 2014 5e stat block used, or custom block location.

## Appearances
Adventures/sessions where they show up:
- [[SP-GANN-Title]] — scenes

## Player Log
Fill in after each session where this NPC appears.

| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
If `canon: true`, cite edition/book/page. If homebrew inspired by canon, link the source.

## Continuity
What threads are they tied to? What happens to them if the PCs ignore them?
