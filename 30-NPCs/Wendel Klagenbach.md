---
type: npc
status: alive
canon: false
faction: ''
location: '[[02. World/Hubs/Ritterstadt|Ritterstadt]]'
aliases: [Wendel, The Sentry]
species: Human
heritage: ''
gender: Male
age: Young Adult
alignment: Neutral Good
occupation: Garrison Soldier (night watch)
class: ''
subclass: ''
prestige_class: ''
level: ''
adventure_role: ''
disposition: Friendly
party_trust: 1
items: []
connected_quests: ['[[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South|0004 - The Man from the South]]']
connected_groups: []
parents: []
partner: []
children: []
siblings: []
allies: [Hauptmann Hildegard Stahlwulf, Rowena Ithilbrook]
enemies: []
deceased_date: ''
tags: [Category/People, NPC, ritterstadt-npc]
publish: false
name: Wendel Klagenbach
MyContainer: '[[The Guardhouse]]'
MyCategory: null
image: null
obsidianUIMode: preview
NoteStatus: 🌱
town_role: Garrison — junior
shop: null
founder: false
first_appearance: 0004, Session 1 — 22 Harvester 576 CY
---

# Wendel Klagenbach

> The night watch's youngest and least impressive soldier — the man who was on duty when the Guardhouse was robbed, and who contributed nothing at all to stopping it.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Early twenties, thin, a helmet a half-size too large. Garrison issue kept technically correct and visibly unloved. Since the twenty-second he walks with a stick he does not need.

## Personality & Mannerisms
Loud in distress and quiet the rest of the time. Explains things nobody asked about. Says *"I'm not complaining"* immediately before complaining. Since his splinting he has developed a habit of appearing wherever Rowena Ithilbrook is, holding something, in case she wants it held.

### 🗣️ Voice
> **Wendel:** "It's *broken*. I heard it. You don't hear a thing like that and then it turns out to be nothing, do you? Do you?"

> **Wendel** *(later, to anyone, unprompted):* "I want it on the record that I was at my post. I was at my post and then I was behind the woodstack. I'm not saying those things are the same. I'm saying there was an order to them."

## Goals & Secrets

## Role & Context

## Conversation Guide
| Topic | Freely discussed? | Notes / sample line |
|---|:---:|---|
| | | |

## Services
| Service | Cost / notes |
|---|---|
| | |

## Quest Hooks
| Hook | Leads to | Trigger |
|---|---|---|
| | | |

## Relationships
```dataview
TABLE WITHOUT ID parents AS "Parents", partner AS "Partner", children AS "Children", siblings AS "Siblings", allies AS "Allies", enemies AS "Enemies"
WHERE file.path = this.file.path
```
- **[[Greyhawk University/05. The Hamlet of Ritterstadt/Town NPCs/Hauptmann Hildegard Stahlwulf|Hauptmann Hildegard Stahlwulf]]** — his commander. Has said nothing to him about the twenty-second. He would rather she shouted.
- **[[Rowena Ithilbrook]]** — set his leg. He is hers now, in the way of young men who have been shown a kindness they did not deserve.
- **[[Greyhawk University/05. The Hamlet of Ritterstadt/Town NPCs/Ewald Wennerberg|Ewald Wennerberg]]** — served alongside him. Wendel thought he was fine. Everyone did.

## Inventory
```dataview
LIST FROM "50-Items" WHERE contains(this.items, file.link)
```
Spear, garrison-issue. Shield. A splint and bandage he refuses to remove. A walking stick he does not need.

## Stat Block
**Guard** (MM p.347), unmodified. He will not win a fight and he knows it.

## Appearances

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity

## GM Notes
**What happened on the 22nd.** He was the sentry on the Guardhouse door the night the Traft crew came over the wall. He was found afterward behind the woodstack, uninjured, weeping, and absolutely certain his leg was broken. It was a sprain. **Rowena Ithilbrook splinted it one-handed**, an hour after losing her left hand to her own *spiritual weapon*, and never said a word about the comparison. Neither did anyone else. Wendel has worked it out since.

**How to play him now.** The comedy is real but it is the setup, not the payoff. The payoff is that **he is ashamed** — a robbery happened on his watch and he was not part of stopping it — and **Hildegard has never mentioned it to him**, which is worse than a reprimand. He is looking for a way to be useful once, to anybody, and the party are the obvious candidates.

**What he is for, mechanically:**
- **He is the garrison's leak.** He talks. He will pass on things Stahlwulf would consider none of the students' business — patrol rotations, who came to the Guardhouse and when, what the Hauptmann said to the Ritter and in what tone. He does not think of this as betrayal; he thinks of it as helping.
- **He owes Rowena specifically** and will do something unwise to repay it.
- **He is the obvious man to be standing somewhere he should not be** when the cleaners move. If the arc needs a witness, a body, or a hostage who is not a Beckenhaus, he is already in position and the table will feel it.
- **Long-term:** if he survives 0004 and gets one competent moment, he becomes the Ritterstadt fixture the players actually like. That is worth more than another grim soldier.

> [!warning] Do not kill him for shock value
> He is funny, and the table adopted him inside a minute. Spending him early buys one gasp; keeping him buys a recurring NPC the players will protect. If he must be endangered, let them get there in time — at least once.

## Connections
- **Post:** [[The Guardhouse]] — night rotation, under [[Greyhawk University/05. The Hamlet of Ritterstadt/Town NPCs/Hauptmann Hildegard Stahlwulf|Hauptmann Hildegard Stahlwulf]]
- **Debut:** [[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South|0004 — The Man from the South]] · [[0004 - Session 1 Recap — What Actually Happened]]
