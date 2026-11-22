---
type: npc
status: alive
canon: false
faction: ''
location: ''
aliases: [Temür, Wegwiur trader]
species: Human
heritage: Human — Flan
gender: Male
age: Adult
alignment: ''
occupation: Wolf Nomad (Wegwiur) amber-and-fur trader
class: ''
subclass: ''
prestige_class: ''
level: ''
adventure_role: ''
disposition: ''
party_trust: 0
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
tags: [Category/People, town-npc, traveler, velvet-shadow, planned, dm-only-details]
publish: false
name: Temür Bayan
MyContainer: null
MyCategory: null
image: Temür_Bayan.png
obsidianUIMode: preview
NoteStatus: ❓
npc_status: planned-arrival
town_role: Itinerant northern trader — not yet arrived
origin: The Wegwiur (Wolf Nomad) lands, bordering the Burneal
related-villain: '[[DM Reference — The Velvet Shadow]]'
founder: false
---

# Temür Bayan — Wolf Nomad trader (planned arrival)

> A garrulous, road-worn Wegwiur trader who has come a very long way south — half to sell amber and furs, half because the north has stopped feeling like home. An unwitting witness to something he can't name.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
A weather-cured Wegwiur trader of the Wolf Nomads, come a very long way south with a string of shaggy ponies carrying amber, white furs, horn, and felt, looking to trade for worked metal, salt, and Verbobonc steel. He is garrulous in the way of a man who has been alone on a cold road too long, superstitious, and quick to touch the wolf-tooth at his neck. He did not come south only to trade. He came because the north has stopped feeling like home — and a man tells that kind of thing to strangers over drink more easily than to his own khan.

## Personality & Mannerisms

## Goals & Secrets

## Role & Context
> [!warning] STATUS: not yet introduced — planned arrival
> Temür is a **deliberate future arrival**, not part of the caravan rotation. Bring him to Ritterstadt **somewhere down the line — roughly 3–6 months out IRL** — as the carrier who first drops the [[#The Winter Vanguard rumors he carries|Winter Vanguard rumors]] on the village. Until then he and his rumors stay staged. **Do not add him to [[Caravan Schedule]] yet.**

He is an **unwitting witness**: he has seen the [[Kaelen Vane, the Ashen Knight|Vanguard's]] work, fled the edge of it, and carries the truth without understanding it. He has never heard the name "Velvet Shadow." He thinks it's a bad winter with a war in it.

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
monster: Scout
```
%% Suggested SRD block for a hardy long-road trader. Adjust to taste. %%

## Appearances

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes

## Continuity

## GM Notes
> [!danger] DM Eyes Only

## How to bring him in
1. When the moment comes (the staged Wolf-Nomad beat), add him to [[Caravan Schedule]] as a one-off or rare-cadence entry (origin *the Wegwiur lands*, sells amber/furs/horn, buys steel/salt), or simply narrate his arrival and create a Travelers note by hand.
2. Set the staged **Winter Vanguard** rumors (below) to `status: live` over the days he's in town, and run their seed kits to bump [[The Velvet Shadow — Burneal Reach]] (and re-band its `axis_martial` upward — the army is now visible).
3. Consider advancing the global stage tag toward `closing` once he's spoken.

## The Winter Vanguard rumors he carries
These three staged notes in the Rumor Pool are his to deliver (tag `winter-vanguard`, `status: staged`, held out of template rotation):

- [[Rumor — Winter Vanguard — the winter that has captains]]
- [[Rumor — Winter Vanguard — the burned knight in black iron]]
- [[Rumor — Winter Vanguard — the diggers under the ice]]

## Related
> [!abstract] Connections
> - The threat he unwittingly reports: [[DM Reference — The Velvet Shadow]] · [[The Velvet Shadow — Burneal Reach]]
> - The army he saw: [[Kaelen Vane, the Ashen Knight]] and the Winter Vanguard
