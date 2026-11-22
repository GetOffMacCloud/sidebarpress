---
type: npc
status: alive
canon: false
faction: ''
location: '[[Ritterstadt]]'
aliases: [Vater Sigmund]
species: Human
heritage: ''
gender: Male
age: Elder
alignment: Lawful Good
occupation: Village Priest & Healer
class: ''
subclass: ''
prestige_class: ''
level: ''
adventure_role: ''
disposition: Friendly
party_trust: 0
items: []
connected_quests: ['[[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]]', '[[Greyhawk University/04. Campaign Logs/Session Notes/0003 - The Stolen Grain]]', '[[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]]']
connected_groups: []
parents: []
partner: []
children: []
siblings: []
allies: [Ritter Konrad von Eisfeld, Hanz Korngut, Lotte Kesselring]
enemies: []
deceased_date: ''
tags: [Category/People, NPC, ritterstadt-npc]
publish: false
name: Vater Sigmund Wolfherz
MyContainer: '[[St. Erika''s Chapel]]'
MyCategory: null
image: Sigmund_Wolfherz.png
obsidianUIMode: preview
NoteStatus: ❓
town_role: Spiritual Anchor & Lore-Keeper
shop: St. Erika's Chapel
founder: true
---

# Vater Sigmund Wolfherz

> A gentle elder with the patience of a man who has been waiting for the right moment to say something important — and is no longer certain it will ever come on its own.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
An older man with careful, clean hands and simple robes. His quarterstaff is worn smooth from decades of use. A healer's kit is always at his side. His face is kind and unhurried. On clear mornings, he stands at his window and watches the Wachturm to the north.

## Personality & Mannerisms
Speaks quietly and at length, rarely in a hurry. Does not ask direct questions — prefers to share something and wait for the response it draws. Goes very still when surprised; it's the only crack in his composure. Refers to Hassenrath by name occasionally, in passing, as if testing whether anyone recognizes it.

## Goals & Secrets
### 💡 Key Motivation
Keep Ritterstadt safe from a threat that most of its residents do not know exists. He has the knowledge to explain it. He has been waiting for someone worth explaining it to.

### The Real Story
Sigmund holds **Hassenrath's notes** — the research of a prior scholar who documented the Wachturm's binding function, the ward-panel system, and what the structure was built to contain. Sigmund has been building on these notes privately for years. He knows the ward-panels are degrading. He knows something beneath the tower is faintly stirring. He does not know what to do about it — and he has been waiting for capable people to arrive before he says anything.

### What They Know (But Won't Say)
- The full contents of Hassenrath's notes: the binding network, the six sites, the "do not open alone" warning at the Wachturm entry
- That the Erdgeist at the east shrine is connected to the tower's protective network and is currently agitated
- That Hanz Korngut's strange dreams are a symptom of the ward degradation
- That the ward-panels have been weakening for at least a generation and the timeline is accelerating

### What They Fear
That he waited too long to trust someone. That the thing beneath the tower stirs before anyone who can act is in position to do so. He is afraid of being wrong about the party — of giving the notes to people who will make things worse.

### How to Reveal It
The trigger is the east shrine investigation in **0003** — if the party consults Sigmund about the Erdgeist's agitation and its connection to the tower, he goes very quiet, then asks them to sit down. He shares Hassenrath's notes. He says: *"I have been waiting for someone to come along who would do something other than make it worse."*

A secondary trigger is **0004**: if the party shows him Varek Doss's research notes (obtained from Vethkar), he asks to meet privately. Doss's partial picture combined with Hassenrath's complete one gives him the first full understanding of the timeline. He will be frightened in the way quiet men are frightened — very still, very careful.

## Role & Context
Sigmund is the village's priest and healer — the spiritual and medical center of Ritterstadt. He buries the dead, heals the sick, settles disputes with quiet authority, and serves as the closest thing the hamlet has to a living institutional memory. Without him, the village loses its moral compass and its only trained healer.

## Conversation Guide
| Topic | Freely Discussed? | Notes / Sample Line |
| :--- | :---: | :--- |
| Faith, healing, village welfare | ✅ | Open and warm |
| Village history (general) | ✅ | Shares freely, carefully |
| The east treeline shrine | ⚠️ | "Not every old thing is dangerous. Some were put here to protect." |
| The Wachturm | ⚠️ | "It is older than the church. Older than the land-grant. I have... notes." |
| Hassenrath | ⚠️ | Drops the name in passing. Waits to see if anyone reacts. |
| What's beneath the tower | ❌ | Not until the party has proven they'll do something useful with it |

### 🔑 Trust-Gated Information
- **Low Trust (stranger):** Heals freely. Shares village history without agenda. Gentle, open, nothing withheld that he judges them ready for.
- **Medium Trust (regular):** Mentions Hassenrath's name without explaining who he was. Notes that the tower has been "studied before." Asks quiet questions about what the party has seen in the uplands.
- **High Trust (friend / proven):** Shares Hassenrath's notes. This is the moment the campaign's central mystery becomes explicit. He will say: *"I have been waiting for someone to come along who would do something other than make it worse."*

## Services
| Service | Cost / Notes |
| :--- | :--- |
| Healing (basic) | Free. He never charges. |
| Spiritual counsel | Free |
| Lore consultation (history, religion) | Free — but he gives what he judges you're ready for |
| Hassenrath's notes | Trust-gated. This is the Wachturm arc reveal. |

## Quest Hooks
| Hook | Leads To | Trigger Condition |
| :--- | :--- | :--- |
| Blesses a party member's weapon (quietly, unbidden) | Goodwill / relationship | Party spares the winter wolves in 0002 |
| Shares Hassenrath's notes | Wachturm Arc reveal | Party consults him about the east shrine in 0003 |
| Asks to meet privately after seeing Doss's research | Wachturm Arc escalation | Party obtains Vethkar's notes in 0004 and shows him |

## Relationships
```dataview
TABLE WITHOUT ID parents AS "Parents", partner AS "Partner", children AS "Children", siblings AS "Siblings", allies AS "Allies", enemies AS "Enemies"
WHERE file.path = this.file.path
```
| NPC | Relationship Type | Notes |
| :--- | :--- | :--- |
| [[Ritter Konrad von Eisfeld]] | Respectful advisor | Konrad trusts his moral judgment; Sigmund is careful not to alarm him unnecessarily |
| [[Hanz Korngut]] | Quiet concern | Knows Hanz has been having strange dreams; hasn't told him why |
| The Erdgeist (east shrine) | Informed neutral | Knows it exists, considers it benign, does not want it disturbed |
| Hassenrath (deceased scholar) | Inherited custodian | Holds his notes; has built on his research privately |

mermaid\n" + lines.join("\n") + "\n```");
```

## Inventory
```dataview
LIST FROM "50-Items" WHERE contains(this.items, file.link)
```

## Stat Block
```statblock
monster: Priest
```
%% Suggested SRD block for a village priest & healer. Adjust to taste. %%

## Appearances
Sidebar Press adventures this NPC appears in:
- [[SP-GA03-The-Red-Cord]] — Scene 1 (persuades Konrad to go; walks him to the Landing if he refuses)

## Player Log
| Date (CY) | Party | Summary of Interaction |
| :--- | :--- | :--- |
| | | |

## Canon Notes

## Continuity

## GM Notes
> [!danger] DM Eyes Only
