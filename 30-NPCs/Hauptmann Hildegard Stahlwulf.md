---
type: npc
status: alive
canon: false
faction: ''
location: '[[Ritterstadt]]'
aliases: [Hauptmann]
species: Human
heritage: ''
gender: Female
age: Adult
alignment: Lawful Good
occupation: Garrison Commander
class: ''
subclass: ''
prestige_class: ''
level: ''
adventure_role: ''
disposition: Neutral
party_trust: 0
items: []
connected_quests: ['[[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]]', '[[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]]']
connected_groups: []
parents: []
partner: []
children: []
siblings: []
allies: [Ritter Konrad von Eisfeld]
enemies: []
deceased_date: ''
tags: [Category/People, NPC, ritterstadt-npc]
publish: false
name: Hauptmann Hildegard Stahlwulf
MyContainer: '[[The Guardhouse]]'
MyCategory: null
image: Hildegard_Stahlwulf.png
obsidianUIMode: preview
NoteStatus: ❓
town_role: Military Authority
shop: The Guardhouse
founder: false
---

# Hauptmann Hildegard Stahlwulf

> A watchful woman who assesses everything in a room before saying a word — and usually knows more than she lets on.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Adult human female, always in chain mail when in public — no exceptions. A longsword at her hip, a hand crossbow sometimes. Military bearing, hair kept short and practical. She doesn't fidget. She stands with her back to walls when she can.

## Personality & Mannerisms
Speaks in direct, economical sentences. Rarely volunteers information — answers exactly what was asked, nothing more. Will state her limits plainly ("I want to expel him, but I lack grounds") rather than pretend she has authority she doesn't. Assesses the party from the moment she meets them, thoroughly and without advertising it.

## Goals & Secrets
### 💡 Key Motivation
Keep Ritterstadt physically safe. Serve Konrad's vision of the hamlet while maintaining her own professional integrity. She will not bend a rule she believes in, even for Konrad.

### The Real Story
Hildegard is carrying two quiet concerns she hasn't voiced to Konrad: the garrison is underfunded relative to the threat level in the uplands, and one of her soldiers — Ewald Wennerberg — has been behaving unusually. Off-route patrols, unexplained absences, specific nervousness near the mill. She hasn't connected it to anything yet. It reads as stress, not treason.

### What They Know (But Won't Say)
- That Ewald has been on at least three unauthorized patrol routes in the past month (players can discover this via the travel encounter table in 0002: Ewald moving north, fast, startled to see them)
- That she is privately worried about the garrison's ability to hold the palisade if a gnoll warband — not scouts — came south
- That she doesn't trust the Vogt and has said nothing about it because she has no proof of misconduct, only instinct

### What They Fear
A coordinated external threat arriving before the garrison is ready. The thing she won't say aloud: she's not sure they'd hold.

### How to Reveal It
The Ewald thread surfaces naturally in 0002 if the party rolls his encounter and asks why he's heading north off-route. Hildegard's private garrison concerns come out only at high trust, in a private conversation, after the party has proven their competence in the field. She will say it bluntly: *"If twenty gnolls came through that gate tonight, I do not know that we hold it. I would like to not need to find out."*

## Role & Context
Hildegard commands the garrison — the hamlet's only organized military force. She sets patrol routes, responds to threats, and maintains discipline among the soldiers. She is the first line of defense against gnoll incursions, wolf raids, and unwanted visitors. Without her, the garrison loses cohesion.

## Conversation Guide
| Topic | Freely Discussed? | Notes / Sample Line |
| :--- | :---: | :--- |
| Known threats (gnolls, wolves) | ✅ | Direct and specific. Will pull maps if available. |
| Garrison capability | ⚠️ | Honest about what they can and cannot do |
| Vethkar Graun | ⚠️ | "I want to expel him. I lack grounds. That's all I'll say." |
| Ewald Wennerberg | ❌ | Has noticed his behavior but says nothing |
| Konrad's finances | ❌ | "That is not my office." |
| The Wachturm | ❌ | "It's been there longer than any of us. It'll be there after." |

### 🔑 Trust-Gated Information
- **Low Trust (stranger):** Professional assessment of the party. Gives a clear picture of known threats in the uplands. Will ask directly about their experience and capabilities.
- **Medium Trust (regular):** Actively supports sanctioned missions. Coordinates garrison patrol routes to avoid conflicting with party operations. Will mention if she's noticed something unusual (Ewald's off-route patrol in 0002 is the key example).
- **High Trust (friend / proven):** Shares her private assessment of village vulnerabilities — specifically that the garrison is understaffed and that she has concerns about at least one soldier's reliability (Ewald, without naming him directly until pressed).

## Services
| Service | Cost / Notes |
| :--- | :--- |
| Threat assessment / briefing | Available to any party she's judged capable |
| Garrison coordination | Sanctioned missions only; she'll cooperate if Konrad has commissioned the party |
| Patrol intelligence | Trust-gated; she'll share route information with established parties |

## Quest Hooks
| Hook | Leads To | Trigger Condition |
| :--- | :--- | :--- |
| Brief encounter at The Ritter's Hall before Konrad's commission | [[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]] | Party meets Konrad; she's present, assessing |
| "A garrison soldier came back from patrol with a slash across his shoulder. He wouldn't say what made it." | [[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]] | Party asks about the north pass before taking the contract |
| Flags Vethkar as a concern without actionable grounds | [[Greyhawk University/04. Campaign Logs/Session Notes/0004 - The Man from the South]] | Party asks why the garrison is watching the inn |

## Relationships
```dataview
TABLE WITHOUT ID parents AS "Parents", partner AS "Partner", children AS "Children", siblings AS "Siblings", allies AS "Allies", enemies AS "Enemies"
WHERE file.path = this.file.path
```
| NPC | Relationship Type | Notes |
| :--- | :--- | :--- |
| [[Ritter Konrad von Eisfeld]] | Trusted ally | She is loyal to his vision; he relies on her judgment |
| [[Vogt Ruprecht Ackermann]] | Professional tolerance | She does not respect him but works within the same authority structure |
| Ewald Wennerberg | Commander (unaware) | She has noticed his unusual patrol behavior but has not connected it to anything actionable yet |

mermaid\n" + lines.join("\n") + "\n```");
```

## Inventory
```dataview
LIST FROM "50-Items" WHERE contains(this.items, file.link)
```

## Stat Block
```statblock
monster: Veteran
```
%% Suggested SRD block for a garrison commander. Adjust to taste. %%

## Appearances
Sidebar Press adventures this NPC appears in:
- [[SP-GA03-The-Red-Cord]] — Scene 1 (Hook 2: "Keep his hand off it"; packs the half-banner)

## Player Log
| Date (CY) | Party | Summary of Interaction |
| :--- | :--- | :--- |
| | | |

## Canon Notes

## Continuity

## GM Notes
> [!danger] DM Eyes Only
