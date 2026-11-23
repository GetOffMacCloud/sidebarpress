---
type: npc
status: alive
canon: false
faction: Candlecrown
location: '[[Mother Sedge''s Shrine]]'
aliases: []
species: Human
heritage: ''
gender: Female
age: Elder
alignment: ''
occupation: Shrine-keeper of Telchur
class: None (NPC)
subclass: ''
prestige_class: ''
level: ''
adventure_role: informant
disposition: friendly
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
tags: [candlecrown, telchur, priest, sp-gs02]
---

# Old Mother Sedge

> Shrine-keeper of Telchur in Candlecrown and its oldest singer, who knows the seventh verse is a curse. [Telchur]

**Loyal to:** the unwritten seventh verse, then Telchur, then the village; she will give her own voice before the verse.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Past eighty, tiny, wrapped in so many shawls she is round. White hair in a single braid to her knees. **Memorable:** her eyes are pale grey, almost white, and she doesn't blink in the wind.

## Personality & Mannerisms
Dry, unhurried, unafraid. Says less than she knows and exactly what she means. Calls everyone under sixty "child." **Quirk:** hums the carol's tune under her breath while she listens to you, and stops the instant she hears a lie.

## Goals & Secrets
- **Wants:** the seventh verse kept safe and never written. *Fears:* that she'll die before anyone else understands what it is.
- **Knows:** her grandmother's warning (the verse is a curse; never write it); the old law of the hallowed gate (the dead must be invited); that the miners kept a chapel below; every verse by heart. She doesn't know about the counter-verse.
- **Reacts:** tells the truth to anyone who asks her privately, and to her kin at once. Opposes letting Aurel in and opposes the false verse ("It's still writing"), but can be persuaded. In the worst case (Scene 11), offers Hrimvald her own voice.

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
**Priest** (MM p. 348), with *protection from energy* in place of *spirit guardians* and *bless* in place of *guiding bolt*.

## Appearances
- [[SP-GS02-The-Long-Night-at-Candlecrown]] — Scenes 02, 03, 07, 08, 09, 10, 11, 12. Hook 4's letter writer; the safety valve's keeper.

## Player Log
| Date (CY) | Party | What happened |
|---|---|---|
| | | |

## Canon Notes
Homebrew.

## Continuity
She sent the letter that is hook 4. If she loses her voice, she communicates with a slate and is no less formidable.
