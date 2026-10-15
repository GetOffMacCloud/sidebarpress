---
publish: false
type: DM-Reference
title: "PATCH — Kettenhaus ratification & 0004 recap corrections"
tags: [dm-only, patch, canon-correction, ritterstadt]
compiled: 2026-09-19
status: Unapplied
---

# 🔧 PATCH — Kettenhaus ratification & 0004 corrections

> [!warning] Why this is a patch file and not direct edits
> The Drive connector can only change a file's **title and folder**, not its contents. Every edit below is therefore a find-and-replace you apply in Obsidian. Delete this file once applied.

**Five files.** Work top to bottom — B depends on A being ratified.

- [ ] A — [[The Kettenhaus]]
- [ ] B — [[Campaign Threads]]
- [ ] C — [[DM Reference — Faction Dossiers]]
- [ ] D — [[0004 - Level 3 Scaling Notes]]
- [ ] E — [[0004 - Session 2 Recap & Arc Close — What Actually Happened]]

---

## ⚓ Rulings this patch applies

| Ruling | Decision |
| :--- | :--- |
| **Debt figure** | **700 gp principal / ~900 gp with interest.** Master-note figure wins |
| **The creditor** | **The Kettenhaus** — Hanselmann by family, Hussen by patronage, seated in Traft |
| **Vethkar's standing** | **Contract open. Report unfiled.** Party can still move the outcome |
| **Traft / Rowena's hand** | **Reading A — coincidence of geography.** Nobody owed, no strings |
| **⚜ Hazard Billing** | **Closed.** Reading A gives it no back route |

---

# A — The Kettenhaus

> [!danger] 🔥 New finding — read this before anything else
> The Faction Dossiers already answer the question my new Kettenhaus note left open. **The house intends to sell the timber rights to a Schwartzenbruin logging operation** — and those rights *sit directly over several resonance node sites.* Logging them would cause irreversible physical damage to the binding network.
>
> **The Kettenhaus is on course to produce the "catastrophic" outcome by purely mundane means, without ever knowing the network exists.** That is a far better engine than anything I wrote into the file, and it links P1 straight into the Wachturm Arc. Add it.

**Append to the end of `## 📜 The Eisfeld Schuldbrief`, before the "What the house actually wants" paragraph:**

```
### ⚠️ What the house intends to do with the timber

Per [[DM Reference — Faction Dossiers]]: on foreclosure, the Kettenhaus will **sell the timber rights on to a Schwartzenbruin logging operation.** Those rights sit directly over several **resonance node sites.** Logging them physically damages the node apparatus in ways that cannot be repaired.

**The house does not know this.** There is no malice anywhere in the chain — a lender recovers collateral, a logging concern buys it, men cut trees, and a binding network four thousand years old loses another anchor. Doss's underlined *"catastrophic"* and the Kettenhaus's ordinary commercial logic arrive at the same place from opposite directions, and only the party is positioned to see both.

**This is why P1 is a Wachturm thread, not just a political one.** If the party does nothing, logging begins within a year and Node 2 is damaged.
```

---

# B — Campaign Threads

### B1 — P1, the debt row

**FIND:**
```
| P1 | **Konrad's debt** — 800gp to Hanselmann Consortium. Timber rights at risk. Vethkar assessing foreclosure. | 0004 | 🔴 Urgent | — | Present Konrad with options before Vethkar files his report. |
```
**REPLACE:**
```
| P1 | **Konrad's debt** — **700 gp principal, ~900 gp with interest** to [[The Kettenhaus]] of Traft. Timber rights at risk — and those rights sit over node sites the house intends to sell to Schwartzenbruin loggers. Vethkar assessing foreclosure; **report unfiled.** | 0004 | 🔴 Urgent | 0004 | Present Konrad with options before Vethkar files his report. |
```

### B2 — P5, cross-link the two money-houses

**FIND:**
```
Ledger page + lead seal are the evidence chain. Ties to P1/Eisfeld toll politics. |
```
**REPLACE:**
```
Ledger page + lead seal are the evidence chain. Ties to P1/Eisfeld toll politics. **Decide before 0005 whether Marbrand & Fessel are the Kettenhaus's rivals, its Verbobonc front, or unconnected — see [[The Kettenhaus]] § Open question.** |
```

### B3 — NPC cross-reference row

**FIND:**
```
| **Vethkar Graun** | Konrad's debt; Ewald spy; Doss's research | Negotiates once cornered with evidence. |
```
**REPLACE:**
```
| **Vethkar Graun** | Konrad's debt; Ewald spy; Doss's research | Negotiates once cornered with evidence. **Now also Professor of Military Tactics & Logistics — see [[Vethkar Graun]].** |
```

---

# C — DM Reference — Faction Dossiers

### C1 — Section heading

**FIND:** `## The Hanselmann Consortium`
**REPLACE:** `## The Kettenhaus *(formerly written as "the Hanselmann Consortium")*`

> Full house record: [[The Kettenhaus]]. Hanselmann is the family; Kettenhaus is the house.

### C2 — The principal

**FIND:**
```
They lent Konrad 800 gold pieces against future timber rights in the uplands territory, secured by the Ritter's land-grant.
```
**REPLACE:**
```
They lent Konrad **700 gold pieces** against future timber rights in the uplands territory, secured by the Ritter's land-grant. With accrued interest the instrument now stands at roughly **900 gp**.
```

### C3 — What they want

**FIND:**
```
Repayment of 800 gold plus 200 gold accrued interest, or formal transfer of the timber rights.
```
**REPLACE:**
```
Repayment of **700 gold principal plus roughly 200 gold accrued interest — about 900 gp** — or formal transfer of the timber rights.
```

### C4 — The pay-off option

**FIND:** `- **Pay the debt** — 1,000 gold, or enough to satisfy Vethkar's report.`
**REPLACE:** `- **Pay the debt** — ~900 gold, or enough to satisfy Vethkar's report.`

### C5 — His job title

**FIND:** `Vethkar is a Consortium assessor who has been in this region`
**REPLACE:** `Vethkar is a Kettenhaus **Schätzer** (field appraiser) who has been in this region`

> The house calls its field agents **Schätzer**, deliberately — *the Assessor* is the node-agent in [[0006 - The Survey Line]] and the table will connect them if both use the word.

### C6 — Agents of Iuz cross-reference

**FIND:** `hence the Hanselmann Consortium angle (which they did not initiate, but have noticed and find useful)`
**REPLACE:** `hence the [[The Kettenhaus|Kettenhaus]] angle (which they did not initiate, but have noticed and find useful)`

---

# D — 0004 Level 3 Scaling Notes

**FIND:**
```
Vethkar Graun is a field operative for the Ritterstadt Consortium — a southern financial interest that has extended credit to Konrad von Eisfeld and holds his debts. He is:
```
**REPLACE:**
```
Vethkar Graun is a **Schätzer** (field appraiser) for [[The Kettenhaus]] — the Hanselmann lending house of Traft, which extended credit to Konrad von Eisfeld and holds his Schuldbrief. He is:
```

> *"Ritterstadt Consortium" was an early-draft slip. The house is seated in Traft and is not Ritterstadt's anything.*

---

# E — 0004 Session 2 Recap & Arc Close

Eleven edits. The stat block and structure of the file are otherwise fine.

### E1 — The roster claim excludes Phin

**FIND:**
```
> **The roster is now uniformly level 4** — Bethany, Rowena, Celenin, Tuldrim, Bromm, Fennel. That is worth noting for 0005's encounter maths: no more mixed-tier scaling, and the [[0004 - Level 3 Scaling Notes]] can be retired.
```
**REPLACE:**
```
> **The six active characters are now uniformly level 4** — Bethany, Rowena, Celenin, Tuldrim, Bromm, Fennel. No more mixed-tier scaling among the active roster, and the [[0004 - Level 3 Scaling Notes]] can be retired. **Phin Phicer Frice is the seventh sheet and this ruling does not cover him** — he missed the whole arc, takes no UC, and stays at his pre-arc level. Build 0005's encounter maths on six at L4, and re-check if he returns.
```

### E2 — Vethkar's day scene

**FIND:**
```
his contracts, his warning, and his two bodyguards are all still on the shelf. *(See* What the arc did not use.*)*
```
**REPLACE:**
```
his contracts, his warning, and his two bodyguards are all still on the shelf. *(See* What the arc did not use.*)* **NPC note now exists: [[Vethkar Graun]].**
```

### E3 — Date the Quiet Man's death

**FIND:** `| **The Quiet Man** | **Dead.** Killed at the camp |`
**REPLACE:** `| **The Quiet Man** | **Dead.** Killed at the cleaners' camp, 24 Harvester 576 |`

### E4 — Handout D + the missing Traft coin row

**FIND:**
```
| **Handout D** — Vethkar's parting word | **Not earned** — he never fought beside them |
```
**REPLACE:**
```
| **Handout D** — Vethkar's parting word | **Not earned** — he never fought beside them. Condition can never recur; three replacement routes in [[Vethkar Graun]] |
| **Traft coin** — off the five S1 bodies | **In party hands.** Physical evidence the cleaners were hired in Traft. Never entered in this ledger before |
```

### E5 — Vethkar's ledger row

**FIND:** `| Vethkar Graun | Faculty position revealed. Contracts untouched |`
**REPLACE:** `| Vethkar Graun | Faculty position revealed. **Both contracts open and unfiled** — Kettenhaus and Doss. See [[Vethkar Graun]] |`

### E6 — The debt in his portfolio

**FIND:**
```
- The **Hanselmann Consortium debt** — 700 gp principal, nearly 900 with interest, and a grey-faced Ritter Konrad. **The Consortium is based in Traft.** Hold that thought.
```
**REPLACE:**
```
- The **[[The Kettenhaus|Kettenhaus]] debt** — 700 gp principal, nearly 900 with interest, and a grey-faced Ritter Konrad. **The house is seated in Traft: Hanselmann by family, Hussen by patronage.** Hold that thought — and note that on foreclosure they sell the timber on to Schwartzenbruin loggers, over node sites. *(Figure ratified 19 Sep 2026; Campaign Threads P1 and the Faction Dossiers corrected to match.)*
```

### E7 — The bodyguards, and the better hook

**FIND:** `- **His two bodyguards**, who still need a story now that he's faculty.`
**REPLACE:**
```
- **His two bodyguards** — retained by contract, not enrolled; one is called **Marek**. Resolved in [[Vethkar Graun]].
- **⭐ The conflict of interest**, which is the better unused hook and which nobody in the hamlet has noticed: a University professor is assessing foreclosure against the lord who hosts the University's field station, on the very timber rights the Field Station expansion depends on. Lotte is the most likely to put it together, and she won't say it without trust.
```

### E8 — Traft condescension

**FIND:** `it was spent on a first-year student who lost a hand to her own botched casting in a guardhouse.`
**REPLACE:** `it was spent on a junior field student who lost a hand to her own botched casting in a guardhouse. *(That is Traft's view of them, not the file's — the party has four contracts behind them.)*`

### E9 — Hazard Billing is now closed

**FIND:**
```
| ⚜ **Hazard Billing** | ❌ **Not earned as written** — Vethkar never fought. **But see the Traft ruling below**, which may deliver this award's *effect* by a completely different route |
```
**REPLACE:**
```
| ⚜ **Hazard Billing** | ❌ **Not earned, and now closed.** Vethkar never fought, and the Traft ruling came down as **A (coincidence of geography)**, which gives it no back route. Only remaining source: Vethkar's own report once filed, if it describes them favourably |
```

### E10 — The A/B/C decision, resolved

**FIND:** `- [ ] **Decide A / B / C** before 0005, even if it never surfaces in play`
**REPLACE:**
```
- [x] **Decided 19 Sep 2026 — reading A, coincidence of geography.** Traft is simply the only place within reach with institutions; a frontier station needing a high-level casting sends its request there. Nobody owed, no strings, no invoice. The party still notices that the same four-day road carried the men who maimed her and the cleric who healed her — **they need to notice the road, not draw a conclusion.** Vethkar had no hand in it and says so if asked.
- [ ] ⚠️ **Still undecided: who sent for the cleric.** Reading A says *where* but not *who*, and the travel maths is tight — a rider had to leave Ritterstadt on the 22nd or 23rd, while the party was still in the field and Hildegard had five bodies. Somebody made that call within hours. **Hildegard is the strongest candidate** (she was briefed at three in the morning and acted immediately), with Drunik second. Pick one; it is a short, good scene either way.
```

### E11 — Closed bookkeeping items

**FIND:** `- [ ] **Vethkar Graun** — NPC note still does not exist. Now overdue; he's permanent faculty`
**REPLACE:** `- [x] **Vethkar Graun** — NPC note created 19 Sep 2026: [[Vethkar Graun]]. Faction record too: [[The Kettenhaus]]`

**FIND:**
```
- [ ] Move the 0004 folder from `Active Adventures/` to `Adventure Archive/` when you're satisfied nothing else is coming
```
**REPLACE:**
```
- [x] ~~Move the 0004 folder~~ — **already done.** It sits in `Adventure Archive/` as of 19 Sep 2026
- [ ] **Decide the emblem's location.** It is currently claimed twice — proposed onto the Quiet Man's body *and* listed as banked Episode 6 cairn material. Pick one and delete the other
- [ ] **Fill Tuldrim Hammerfall's player name** in the Who Played table (currently an em dash)
```

---

## After applying

Delete this file. Then the open decisions still standing are:

1. **Who sent for the cleric** (E10)
2. **The emblem** — corpse or cairn
3. **Marbrand & Fessel vs the Kettenhaus** — rivals, front, or unconnected (needed before 0005)
4. **0005 itself** — still written for Tier 1 / levels 2–3 against a party now flat at 4, and still dated to Goodmonth, which falls *before* 0004. Needs rescaling and re-dating to Patchwall
5. **Vethkar's portrait** — prompt is in his NPC note; `image:` is dangling until it's run
