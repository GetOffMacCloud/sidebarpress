---
type: npc
status: alive
canon: false
faction: ''
location: '[[The Ritter''s Hall]]'
aliases: [The Vogt, Ackermann, Ruprecht]
species: Human
heritage: ''
gender: Male
age: Adult
alignment: Lawful Neutral
occupation: ''
class: ''
subclass: ''
prestige_class: ''
level: ''
adventure_role: ''
disposition: ''
party_trust: ''
items: ['[[fine-clothes-xphb|Fine Clothes]]', '[[dagger-xphb|Dagger]]', '[[abacus|Abacus]]']
connected_quests: ['[[Greyhawk University/05. The Hamlet of Ritterstadt/Buildings & Infrastructure/The Fiend''s Rest Public House/The Job Board/0003 - The Stolen Grain|0003 - The Stolen Grain]]']
connected_groups: []
parents: []
partner: []
children: []
siblings: []
allies: [Ritter Konrad von Eisfeld]
enemies: []
deceased_date: ''
tags: [Category/People]
publish: false
MyContainer: '[[The Ritter''s Hall]]'
MyCategory: Government
image: Ruprecht_Ackermann.png
obsidianUIMode: preview
NoteStatus: ❓
---

# Vogt Ruprecht Ackermann

> 

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance

## Personality & Mannerisms

## Goals & Secrets

## Role & Context
**Vogt Ruprecht Ackermann** is the reeve of Ritterstadt — the Ritter's appointed administrator, tax collector, record-keeper, and the person who ensures that the lord's decisions actually get implemented. He is 55, thin in a papery way, with ink-stained fingers and quick eyes that inventory a room in the first second and spend the rest of the conversation checking the math.

Ruprecht has held his position for nineteen years, through the end of the old Ritter's tenure and all of Konrad's. He knows where every coin in the village has come from and where it has gone. He is efficient, organized, and quietly indispensable. He is also, and has been for years, skimming. Not dramatically — a few coppers per household per quarter, rounded figures that never quite square with the stated totals, small adjustments that individually look like clerical error. Over nineteen years it has added up to a very comfortable private reserve, none of which Konrad knows about.

Ruprecht is not evil. He is cautious, self-interested, and experienced in the calculation that a little corruption, properly managed, is more stable than none at all. He genuinely believes the village is better off with him in his position than with anyone else. He may even be right.

He knows about the letters in the iron chest — the ones that could invalidate Konrad's claim. He has known for twelve years. He has not used them. He keeps them as insurance.

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
mermaid\n" + lines.join("\n") + "\n```");
```

## Inventory
```dataview
LIST FROM "50-Items" WHERE contains(this.items, file.link)
```

## Stat Block
```statblock
monster: Noble
```

## Appearances

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity

## GM Notes
- **The Skimming:** DC 16 Investigation on the village tax records to notice the discrepancies. DC 18 to prove it conclusively. Ruprecht has explanations for everything individually; the pattern is only damning in aggregate. If confronted, he will not confess — he will counter-accuse and muddy the waters. He is very good at this.
- **The Letters:** Ruprecht knows exactly where they are and what they say. He won't volunteer this information unless his back is truly to the wall. If the party threatens to expose his skimming, he may trade the information about the letters as a counter. This would be catastrophic — it could destroy the village's political stability at exactly the wrong moment.
- **Ruprecht and the Ritter's debt:** He knows about the debt. He has actually been trying, in his own way, to create a financial cushion that might help address it — using some of his private reserve to quietly pre-purchase timber rights before the Consortium can snap them up. He has not told Konrad because Konrad would ask where the money came from. This is, technically, protecting the village. It is also deeply compromised.
- **Roleplaying Ruprecht:** He is smooth and pleasant in a way that never quite feels warm. He laughs at exactly the right moments. He remembers every name and uses them deliberately. He is the kind of person who makes you feel like you're being managed, even when he's agreeing with you. He dislikes Hildegard intensely because she sees through him and doesn't bother to pretend otherwise.
- **What he wants:** To remain in his position until he dies, comfortable, having left the village functioning. He does not want power beyond what he has. He wants security, control, and to never have to account for the last nineteen years.
