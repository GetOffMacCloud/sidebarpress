---
type: npc
status: alive
canon: false
faction: ''
location: '[[Ritterstadt]]'
aliases: [Drunik, Runevault]
species: Dwarf
heritage: Dwarf — Mountain
gender: Male
age: Adult
alignment: Lawful Neutral
occupation: Ritterstadt Mining Consortium Liaison
class: ''
subclass: ''
prestige_class: ''
level: ''
adventure_role: ''
disposition: Curt but fair
party_trust: 2
items: []
connected_quests: ['[[Greyhawk University/04. Campaign Logs/Session Notes/0001 - The Rust-Red Extraction]]', '[[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]]']
connected_groups: []
parents: []
partner: []
children: []
siblings: []
allies: [Sigmund Holt, Ritterstadt Questers]
enemies: []
deceased_date: ''
tags: [Category/People, NPC, ritterstadt-npc, gu]
publish: false
name: Drunik Runevault
MyContainer: '[[The Fiend''s Rest Public House]]'
MyCategory: null
image: Drunik_Runevault.png
obsidianUIMode: preview
NoteStatus: ❓
town_role: Mining Consortium Liaison — commissions and assays field specimens for the University Field Station
shop: null
founder: true
---

# Drunik Runevault

> The Consortium's man in Ritterstadt — a dwarf assayer who pays promptly, says little, and knows more about what comes out of the Sepia Uplands than he is willing to file on paper.

> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`

## Appearance
Broad and unhurried, with stone-grey in his beard and the permanent squint of a man who reads mineral grain in poor light. Plain, hard-wearing dress kept clean; a loupe on a cord and an assayer's pick always within reach. His office at the Greyhawk University Field Station smells of cold stone and mineral oil — a standing desk buried in survey notes, two uncomfortable chairs, and a corkboard pinned with a hand-drawn map of the uplands.

## Personality & Mannerisms
Speaks in short, exact sentences and corrects sloppy terminology by reflex — he uses *ferrotholite* and "rust-red" interchangeably and expects students to learn the difference. Conducts real business in the back room of [[The Fiend's Rest Public House]], behind the hearth, away from common earshot. When he is concealing something his left hand goes flat on his thigh — a tell he does not know he has.

## Goals & Secrets
### 💡 Key Motivation
To deliver the Consortium's commissions cleanly and on time — and, privately, to confirm a suspicion he is not ready to put in an official filing: that the secondary ferrotholite vein shares its composition with the foundation stone of [[The Wachturm]], which would make it older than Oeridian Ritterstadt entirely. He wants certainty before he writes a word that the University, or anyone above him, could act on.

### 🕵️ Secrets & Hidden Motivations
### The Last Founder (Sidebar Press ruling, 2026-11-13)
Drunik is one of the **Five Founders** of Ritterstadt: the six who went to Cold Stone Keep from Eru Tovar in 565 came home five. **Eglantine Price** put on the Fiend's Embrace at the Keep and vanished; she is now the Velvet Shadow. The Founders came south with the Keep's gold and the Knights of the Hart, built the town, and sealed an **empty** iron reliquary on the Wachturm's locked ground floor so that Iuz would watch a tower and not hunt their friend. Kuruk, Lealand, Toaren and Dah Voud rode south in 576. Drunik stayed. He is the only person in Ritterstadt who knows the box is empty, and the nearest of the companions the Velvet Shadow needs.

### The Vein and the Wachturm
Drunik genuinely wants the ore — the commission is real. But his private reason for re-running a survey no one had touched in two seasons is that he suspects the secondary ferrotholite vein is the same material as the Wachturm's foundation stone, which would date it four thousand years before Oeridian Ritterstadt. He will not file this until he is certain, because of what it would invite.

### The Prior Survey Team
University-issue tool marks at E3 belong to an undocumented survey that Drunik did not authorise. He filed an internal inquiry. The surveyors — [[Osa Veld]] and [[Renn Farr]] — accessed the Wachturm sub-floor (Node 1), then went northeast into the Quag Mire margin and never returned. Drunik re-sealed the sub-floor himself, imperfectly, and has been quietly trying to find them ever since. His off-record ask to the party is the bridge to [[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]].

### "The Second Window"
As of 25 Flocktime he was overheard at the Fiend's Rest speaking of *"the second window,"* paid for his bread in coin, and left half of it untouched. He is preoccupied, and not sleeping well. See [[Rumor — Drunik Runevault was overheard in the Fiend's Rest at midday]].

## Role & Context
Drunik Runevault is the **Ritterstadt Mining Consortium Liaison** — the commercial counterpart to [[Sigmund Holt]]'s academic office. He commissions field expeditions, assays returned specimens, and pays in University credit vouchers (UC) drawn on the Consortium liaison office. The job-board post that opened [[Greyhawk University/04. Campaign Logs/Session Notes/0001 - The Rust-Red Extraction]] was his.

Where Sigmund handles the *academic* deliverable, Drunik handles the *commercial* one — and the two do not always agree on what matters. They cooperate; they do not entirely trust each other's priorities.

## Conversation Guide
| Topic | Freely Discussed? | Notes / Sample Line |
| :--- | :--- | :--- |
| Commissions, pay, specimen handling | ✅ | Direct and reliable. *"Bring it back sealed and intact. You'll be paid the same day."* |
| Mineral grades, ferrotholite, assay method | ✅ | Will correct your terms and talk longer than you'd like. |
| The Ochre Escarpment cairn / grid E3 | ⚠️ | Visibly reluctant; gives the agreed cover story and no more. |
| The secondary vein's true age / Wachturm link | ❌ | *"That's not confirmed, and I don't file guesses."* Left hand flat on thigh. |
| Osa Veld & Renn Farr | ⚠️ | Off the record only. *"Not a commission. Not logged. Just — keep your eyes open out there."* |

### 🔑 Trust-Gated Information
- **Low Trust:** A fair employer. Commissions, pay, and clear specimen requirements; nothing speculative.
- **Medium Trust:** Admits he filed an internal inquiry over the undocumented prior survey at E3 — University-issue tool marks, no paperwork, a team that never came back. Names [[Osa Veld]] and [[Renn Farr]].
- **High Trust:** Concedes his real suspicion — that the secondary vein and the Wachturm foundation stone are the same pre-Oeridian material — and that he re-sealed the Wachturm sub-floor himself, imperfectly, after the missing surveyors had opened it.

## Services
| Service | Cost / notes |
|---|---|
| | |

## Quest Hooks
| Hook | Leads To | Trigger Condition |
| :--- | :--- | :--- |
| Extract intact specimens from the Ochre Escarpment | [[Greyhawk University/04. Campaign Logs/Session Notes/0001 - The Rust-Red Extraction]] | Party accepts the Consortium commission |
| "Find Osa and Renn — quietly, off the record" | [[Greyhawk University/04. Campaign Logs/Session Notes/0002 - Cold Trails]] | Party earns enough goodwill for the unlogged ask |
| Confirm the secondary vein's composition | Wachturm / binding-network arc | High trust; party has proven discreet |

## Relationships
```dataview
TABLE WITHOUT ID parents AS "Parents", partner AS "Partner", children AS "Children", siblings AS "Siblings", allies AS "Allies", enemies AS "Enemies"
WHERE file.path = this.file.path
```
| NPC | Relationship Type | Notes |
| :--- | :--- | :--- |
| [[Sigmund Holt]] | Professional counterpart | Drunik = commercial commissions, Sigmund = academic deliverable. They cooperate; Drunik is openly sceptical of Sigmund's "methods." |
| [[Osa Veld]] | Subject of inquiry | One of the missing prior surveyors. Drunik wants them found — unofficially. |
| [[Renn Farr]] | Subject of inquiry | The other missing surveyor; believed to have gone northeast toward the Quag Mire margin. |
| [[Ritterstadt Questers]] | Preferred field party | His first call for upland specimen work after the 0001 commission. |

mermaid\n" + lines.join("\n") + "\n```");
```

## Inventory
```dataview
LIST FROM "50-Items" WHERE contains(this.items, file.link)
```

## Stat Block
```statblock
monster: Commoner
```
%% Suggested SRD block for a dwarf assayer. Adjust to taste. %%

## Appearances

## Player Log
| Date (CY) | Party | Summary of Interaction |
| :--- | :--- | :--- |
| Flocktime 576 | Ritterstadt Questers | Commissioned and debriefed [[Greyhawk University/04. Campaign Logs/Session Notes/0001 - The Rust-Red Extraction]]; paid 600 UC + coin. Made the off-record ask about Osa Veld and Renn Farr. |

## Canon Notes

## Continuity

## GM Notes
> [!danger] DM Eyes Only
