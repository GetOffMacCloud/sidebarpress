---
type: npc
status: alive
canon: false
faction: Iuz (secret agent)
location: Yecha (trading); Ekbir (cover)
aliases: [Kezrin, Master Kezrin]
species: ''
heritage: ''
gender: ''
age: ''
alignment: ''
occupation: ''
class: ''
subclass: ''
prestige_class: ''
level: ''
adventure_role: ''
disposition: ''
party_trust: ''
items: []
connected_quests: []
connected_groups: []
parents: []
partner: []
children: []
siblings: []
allies: []
enemies: []
deceased_date: ''
tags: [ekbir, iuz, villain, merchant, SP-GA01]
---

# Master Kezrin

> An Ekbiri "horse-trader" in his forties, and an agent of Iuz. He arms Temur's war faction with black steel below cost and staged the Wolf-arrow murders. The villain of SP-GA01.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Too-clean hands, an oiled beard, a rich southern coat, and a ready smile that never reaches his calculating eyes.

## Personality & Mannerisms
Oil on water. He touches people when he talks — a hand on the elbow, steering. He pours other people's wine generously. He never fights if he can run, and he never leaves a loose end: anyone who has heard his offer gets a visit that night.

> *"My friends, the Ilkhan is old, the khan is young, and I am merely a merchant. But I will tell you what I tell everyone: steel keeps its promises."*

## Goals & Secrets
- **Wants:** Tiger and Wolf bled white before the thaw.
- **Secret:** his men, Wolf-dressed, ambushed Temur's brother's patrol and dumped the bodies by a saber-tooth's den. He pays Yulbar of the Wolf for raids on the Tiger's herds.
- **Carries:** an oilskin packet of orders from Dorakaa and a ledger ([[SP-GA01 — Handout — Kezrin's Papers]]).
- **Knows:** who in Temur's camp carries his steel, Yulbar's price, and that the old khan suspects him.
- **Escalation:** first he buys (the bribe in Scene 5). If refused, he burns the tent (Scene 5). If exposed, he runs: at the council flap, or at first light if Sarnai wasn't told (Scene 7, *Kezrin's Exit*). If cornered, he bargains with the names in his ledger.

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

## Inventory
```dataview
LIST FROM "50-Items" WHERE contains(this.items, file.link)
```

## Stat Block
**Spy** (MM p. 349). Full block in [[SP-GA01 — Bestiary]].

## Appearances
- [[SP-GA01-The-False-Arrow]] — Scenes 5 and 7

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew. Iuz's capital Dorakaa and his hostility to the Tiger Nomads are canon (*LGG* 2000).

## Continuity
Record: **captured**, **escaped (papers recovered)**, or **escaped with papers**. If the false flag was exposed, Cligir declared him wolf-head: any rider may take his head and keep his horses. → [[The War Iuz Wants]]
