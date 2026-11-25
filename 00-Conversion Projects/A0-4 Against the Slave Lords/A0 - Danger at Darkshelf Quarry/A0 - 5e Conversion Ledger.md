---
tags: [adventure/A0, conversion, fgu-prep, slave-lords]
adventure: "A0 - Danger at Darkshelf Quarry"
source: "A0–A4 Against the Slave Lords (WotC 2013 compilation), A0 by Skip Williams, PDF pp. 5–29"
status: draft for review (2026-11-25) — D1–D8 open
created: 2026-11-25
publish: false
---
# A0 — 5e Conversion Ledger

This ledger records every number the 5e table or the FGU build has to touch: the 1e source, the 5e conversion, and the reason for the change. **Review it before any vault notes, statblocks or FG import blocks are generated from it.** Page numbers are PDF pages in `_source/A0-A4 source.pdf`; printed page = PDF page − 1. Maps are on PDF pp. 28–29.

> [!info] Scope of this pass
> - **A straight 1e → 5e conversion that fits any campaign**, run as the opener of a five-module chain (A0 → A4). Darkshelf stays where Skip Williams put it (the Nyrond coast of the Sea of Gearnat, at the mouth of the Pelyra).
> - **Rules:** 5e 2014 (PHB, DMG, MM), with the C12 / T1 ledger rules (§1). MM statblocks wherever an equivalent exists; custom blocks are marked **(custom)**.
> - **Text:** stays close to Williams. This ledger changes numbers, not prose.
> - **Deliverable:** the FGU module only (no print PDF). Maps are cleaned scans for now (§9); traced house-style maps come in a later pass.
> - **Decisions waiting on Greybeard** are marked **⚑ D#** and collected in §10.

---

## 0 · Recommended 5e level

**Answer: start at 1st level, finish A0 at 3rd and level to 4th on the way out, for 4–6 PCs.** The series chain is A0 1–3 · A1 4–5 · A2 5–6 · A3 6–7 · A4 7–8.

The module is written for 6–8 characters of 1st–3rd level (p. 8), with a 1st-level party needing seven or eight. It has three sections, and the party can enter by any of three doors (front bridge, ventilation shaft, river jetty), so **milestones are by section, not by order**:

| Section | Areas | 5e level (4 PCs) | Notes |
|---|---|---|---|
| **Guardhouse** | 1–32 | 1 (main and lower levels), 2 (upper level) | The upper level holds Brubgrok, Glyrthiel and the two bugbear taskmasters: Deadly at L1 if they fight together |
| **Quarry** | 33–53 | 1–2 (main level), 2–3 (lower level) | The Elemental Temple (42–44) fights as one block once alerted; it is the quarry's climax |
| **Caverns** | 54–66 | 3 | Water weird (avoidable), the mudtiger breeding pool (64) is the cavern climax |

**Milestones:** level 2 when the party clears its first section, level 3 after the second, level 4 at the end of the adventure (A1 opens at 4th).

**Entry by the river (area 56) at 1st level drops the party into the 3rd-level section.** The module calls the shaft and the caverns "the safest bets" (p. 7); in 5e that holds for the shaft, not the caverns. The Introduction page gets a one-line DM warning.

**Party size.** Numbers as printed suit **6 PCs** (the module's own floor). For **4 PCs remove one rank-and-file creature in three** (goblins, guards, troglodytes, zombies, killer frogs, slaves who fight), for **5 PCs one in six**; for 7–8 PCs add one in four. Named NPCs, bugbears, mudtigers, ghouls and the water weird never change. §6 lists the scaled numbers.

---

## 1 · Conversion rules used throughout

The C12 / T1 rules, plus the A0 lines marked 🆕.

| 1e | 5e rule applied | Why |
|---|---|---|
| Descending AC | **19 − AC**, checked against the armor named. Armored NPCs use the 5e value of the armor named | As T1 |
| Movement | 12" → 30 ft (×2.5); 9" → 25–30 ft (MM creatures keep MM speed); 6" → 15 ft; 18" → 45 ft. 🆕 Mudtiger `6"//12" (3")` → walk 15 ft, swim 30 ft, burrow 10 ft | |
| Hit points | Not carried. Rebuilt to the DMG CR table or taken from the MM | |
| 1e monster with an MM equivalent | **MM statblock** plus only the module's riders | FG already ships it (SRD copy in the module) |
| 🆕 Level 0 slaves, cooks, grooms, free workers ("HD 1; hp 3–5") | **Commoner** (CR 0), improvised weapon = club 1d4 | They are noncombatants who fight from fear |
| Named NPC classes | Fighter 1 → Guard. Fighter 2 → **Sergeant** (custom). Fighter 3, F/MU 2, Monk 2, Cleric 2 → custom (§3) | |
| Saving throws | Breath → Dex · Poison/death → Con · Paralysis → Con · Spell → the save the 5e spell uses | |
| % chances | DC with about the same success chance at the expected level. NPC whereabouts rolls ("here on a 1–2 on 1d6") are **kept as printed** | Same doctrine as C12 |
| Surprise "on 1–3 / 1–4 / 1–5 (d6)" | Dex (Stealth) vs passive Perception: advantage for 1–4, advantage +5 for 1–5. MM Bugbear's Surprise Attack and the troglodyte's Chameleon Skin already cover these two | |
| 1 Turn | 10 minutes | |
| 1e rounds in timing text ("arrives in two rounds") | **Kept as 5e rounds** | The alarm chain is the design; faster is fine |
| Open Doors / Bend Bars | **Open Doors → DC 15 Strength (Athletics)**; "reduce the chance by 1" → DC 17. **Bend Bars → DC 20 Strength** | |
| Open Locks / climbing | Thieves' tools DC 15. Climb: "somewhat rough, slightly slippery" → **DC 12 Athletics**; cavern walls ("ten times the chance of a fall") → **DC 15**; fail by 5+ = fall | DMG p. 19 (1e) → PHB climbing |
| Doors with "withstands N points" | AC 15 (wood) or AC 19 (iron bars, grates), **hp as printed** | DMG object rules, printed hp kept |
| Cover | 50% cover (+4) → **half cover (+2)**; 90% cover (+10) → **three-quarters cover (+5)** | |
| Trap damage | DMG severity, levels 1–4: Setback 1d10 / DC 10–11 · Dangerous 2d10 / DC 12–15 | As T1 |
| Spells | 2014 PHB. *cure light wounds* → *cure wounds*; *curse* → *bane*; *read magic* → *comprehend languages*; *continual light* → *continual flame*; *cause fear* ⚑ D4 | |
| XP lines | Dropped. CR XP from the MM; story award (§8) | |
| Treasure | **÷ 5, priced on DMG tiers** (§7) ⚑ D2 | Lands on the DMG hoard budget |

---

## 2 · Module-wide mechanics

| # | 1e text (page) | 5e conversion |
|---|---|---|
| M1 | **Neistor's reward:** 500 gp; keep any gold found (p. 7) | Kept: 500 gp. It is not scaled; it is a hire fee, not a hoard |
| M2 | **Random encounters** around Darkshelf: 1 in 6 each hour; 1d6: 1–2 animal, 3 ghoul(s), 4–6 patrol (p. 8) | Unchanged. Statblocks in §4.1 |
| M3 | **River encounters:** as the forest, but a 4-HD mudtiger replaces the huge spider (p. 8) | **Mudtiger** (CR 1) replaces the Huge Spider on a roll of 8 |
| M4 | **Finding the ventilation shaft:** an hour's careful search, even with Kwon's report; **finding the jetty:** an hour or two along the south bank (pp. 7–8) | Kept as time costs, no roll. A DC 15 Wisdom (Survival) check halves the time |
| M5 | **Oil lamps** mortared into the walls: Bend Bars to wrench off; 1–3 on 1d6 spills the oil; burning oil 2–12 then 1–6 (p. 9) | DC 20 Strength to wrench a lamp free; on a 1–3 (d6) the oil spills: a lit lamp deals **2d6 fire, then 1d6 fire** at the start of the bearer's next turn unless they use an action to put it out |
| M6 | **Openly entering / bluffing** (p. 9): Glyrthiel tests stone buyers: a price of 1,000 gp/ton or more gives the game away; so does not knowing stonework; she wants 20% down | **Charisma (Deception) vs Glyrthiel's Wisdom (Insight)**. A character who discusses stonework needs a **DC 12 Intelligence check** (proficiency with mason's tools adds; a dwarf's Stonecunning gives advantage). Agreeing to the inflated price or failing the stonework check ends the bluff automatically |
| M7 | **The guardhouse alarm chain** (areas 1, 6, 10, 17, 18, 19, 20) | Unchanged, in rounds. A guard runs 17 → 6 in **3 rounds** |
| M8 | **Dropped rocks** (areas 1, 22, 23): 15-lb rocks through the murder hole, 1–6; from area 17 onto the pit floor, 2–8; misses bounce (p. 10) | Ranged attack **+3** (the guard's), **1d6 bludgeoning** (murder hole) or **2d4** (from 17 to the pit). On a miss, the rock bounces to a random adjacent square: roll the attack again against anyone there; a second miss stops it |
| M9 | **Climbing the crevice / walls / parapet** (p. 10) | Crevice: DC 12 Athletics, 2 rounds down or up; a fall slides 1d4. Wall to parapet: DC 12, 1 round; over the parapet: another round at DC 15. A fall from the wall: 1d6 + 1d4 and into the crevice |
| M10 | **Cold water in the caverns** (p. 23): after 5 minutes, System Shock or lose 1 hp, 1 Str, 1 Dex each round; regained 1/day of rest | **After 5 minutes in the water, a DC 10 Constitution save each minute or gain one level of exhaustion.** Rest removes it as normal. (The DMG's frigid-water rule, started at the module's 5 minutes) |
| M11 | **The Elder Elemental Eye** clerics, and Brubgrok's link to Highport (pp. 19, 26) | Unchanged. The A-series chain hook: capture Brubgrok, Glyrthiel or a cleric alive, or read the clerics' accounts (they keep Brubgrok's books) |
| M12 | **Prisoners** (p. 9): captured PCs are stripped and put in area 53; Kwon frees them, raids the armory (10) and leads them to area 61 | Unchanged. Kwon brings back simple weapons and one light armor per PC from area 10 |

---

## 3 · NPC conversions

### 3.1 Rank and file

| Who (areas) | 1e line | 5e | CR |
|---|---|---|---|
| **Human guard** (6, 17, 22, 34, 36; patrols) | AC 4/5, HD 1, hp 4, broadsword 2–8 or shortbow 1–6; shield unusable with the bow | **Guard** (MM). Spear → **longsword 1d8+1**; add **shortbow +3, 1d6+1, 80/320**. AC 16 (chain shirt, shield), **14 while using the bow** ⚑ D1 | 1/8 |
| **Goblin** (17, 22, 27, 28, 30, 31, 34, 36, 39, 41, 43, 46, 47) | AC 6, HD 1−1, hp 3; spear 1–6, short sword 1–6, sling 1–4 | **Goblin** (MM). Scimitar → short sword (1d6+2 piercing); add **spear (1d6, thrown 20/60)** and **sling +4, 1d4+2, 30/120**. Diggers (39, 41, 43, 46, 47) carry a **pick** in place of the spear (1d6+2 piercing) | 1/4 |
| **Worg** (28, 32; patrols) | AC 6, HD 3+3, hp 15, bite 2–8 | **Worg** (MM) | 1/2 |
| **Goblin worg-rider** (30, 31, 32; patrols) | split move and fire when mounted | Goblin on a worg. 5e already lets a rider split movement around an attack; nothing added. Saddling takes **2 rounds** | — |
| **Bugbear** (20, 27, 51, 52, 53) | AC 5, HD 3+1, hp 14, 2–8; surprise 1–3 | **Bugbear** (MM). Morningstar and javelin lines as MM; "spear" uses the javelin line | 1 |
| **Troglodyte** (58, 59, 63, 64) | AC 5, HD 2, hp 9; battle axe 2–5 + 1–8 or javelin 1–6; odor, camouflage, surprise 1–4 | **Troglodyte** (MM) with the slavers' weapons: **Multiattack: bite 1d4+2 and battleaxe 1d8+2** (replaces the claws); **javelin +4, 1d6+2, 30/120**. Stone weapons and no metal armor: ignores Magnetize | 1/4 |
| **Zombie** (60) | AC 8, HD 2, hp 8, 1–8 | **Zombie** (MM) | 1/4 |
| **Ghoul** (62; random) | AC 6, HD 2, hp 9, 1–3/1–3/1–6, paralysis | **Ghoul** (MM) | 1 |
| **Human slave, cook, groom** (12, 21, 24, 53) | AC 9, HD 1, hp 3, improvised 1–4 / 1–6 / none | **Commoner** (MM); the stable slaves' pitchforks and staves = **quarterstaff 1d6** | 0 |
| **Free quarry worker** (39) | AC 8, HD 1, hp 5, improvised 1–6 | **Commoner** with a **pick (1d6)**. They don't fight unless attacked | 0 |
| **Light warhorse** (patrol mounts) | AC 7, HD 2+2, hp 10, 1–4/1–4 | **Riding Horse** (MM) | 1/4 |

### 3.2 Named NPCs and the clerics

> [!example] Brubgrok, "Bazili Erak" (custom) · CR 2 (450 XP)
> *1e: 3rd-level half-orc fighter, AC 2, MV 6", hp 18, long sword +1 with Str (+2 to hit, 5–12) or long bow 4–9.*
> Medium humanoid (half-orc), neutral evil. **AC 20** (plate, shield; 18 with the bow). **HP 52** (8d8 + 16). Speed 30 ft. STR 18 DEX 12 CON 15 INT 12 WIS 11 CHA 13. Saves Str +6, Con +4. Skills Athletics +6, Deception +5, Intimidation +3. Darkvision 60 ft. Languages Common, Dwarvish, Orc.
> **Relentless Endurance** (1/long rest): drops to 1 hp instead of 0. **Savage Attacks:** one extra weapon die on a critical hit. **Disguise:** as Bazili Erak he passes for a tall, hunched dwarf; a creature that studies him notices the oddness with **DC 14 Wisdom (Insight)**; a dwarf has advantage.
> **Actions.** *Longsword +1:* +7, 1d8 + 5 slashing (1d10 + 5 two-handed). *Longbow:* +3, range 150/600, 1d8 + 1 piercing. **Action Surge** (1/short rest). **Second Wind** (bonus action, 1/short rest): regains 1d10 + 3 hp.
> Tactics as printed: arrows at casters for a few rounds when he has allies, then the most dangerous foe first.

> [!example] Glyrthiel (custom) · CR 1 (200 XP)
> *1e: 2nd-level elf fighter/magic-user, AC 5, MV 9", hp 9, long sword 1–8 or long bow 1–6; sleep, shield.*
> Medium humanoid (elf), neutral evil. **AC 16** (chain mail). **HP 27** (5d8 + 5). Speed 30 ft. STR 12 DEX 16 CON 12 INT 15 WIS 12 CHA 14. Skills Deception +4, Insight +3, Perception +3. Darkvision 60 ft, Fey Ancestry, Trance. Languages Common, Elvish, Goblin.
> **Spellcasting** (Int, DC 12, +4). Cantrips: *friends*, *mage hand*. 1st level (2 slots): *shield*, *sleep*.
> **Actions.** *Longsword:* +3, 1d8 + 1 (1d10 + 1). *Longbow:* +5, 150/600, 1d8 + 3.
> Tactics as printed: bow first, *shield* against counterattacks, *sleep* on the most foes with the fewest allies in it, even if she waits for allies to fall. **At 1st level *sleep* (5d8) can end the fight; that is the module's capture route (M12).**

> [!example] Sergeant of the Guard (custom) · CR 1/2 (100 XP)
> *1e: 2nd-level human fighter, AC 2, MV 6", hp 15, long sword plus Str 2–9 or shortbow 1–6.*
> **AC 20** (plate, shield). **HP 26** (4d8 + 8). Speed 30 ft. STR 16 DEX 11 CON 14. *Longsword:* +5, 1d8 + 3. *Shortbow:* +2, 80/320, 1d6. **Second Wind** (1/short rest, 1d10 + 2). Bellows for help (area 10 alarm chain).

> [!example] Cleric of the Eye (custom) · CR 1/2 (100 XP) — areas 42, 44, 65
> *1e: 2nd-level human cleric, AC 6, MV 9", hp 9, footman's mace 2–7 or sling 1–4; curse, command, cure light wounds, cause fear.*
> **AC 15** (studded leather, shield). **HP 22** (4d8 + 4). Speed 30 ft. WIS 14. Skills Deception +4, Religion +2.
> **Spellcasting** (Wis, DC 12, +4). Cantrips: *sacred flame*, *thaumaturgy*. 1st level (3 slots): *bane*, *bless*, *command*, *cure wounds*, + *cause fear* ⚑ D4.
> *Mace:* +2, 1d6. *Stone-headed mace* (used beside mudtigers): as the mace, but **−1 to hit against a creature wearing medium or heavy armor**. *Sling:* +3, 30/120, 1d4 + 1.
> Mudtiger-wise: stays out of 10 ft of any mudtiger whose burst is charged.
> *Area 65 casts* bless *on its allies* (the 1e cleric didn't have it memorized; in 5e it's on the list, so the text works as written).

> [!example] Kwon (custom, ally) · CR 1/2 (100 XP)
> *1e: 2nd-level human monk, AC 9, MV 16", hp 7, unarmed 1–4.*
> **AC 15** (Unarmored Defense). **HP 17** (3d8 + 3). Speed 40 ft. DEX 16 WIS 14. Skills Acrobatics +5, Stealth +5, Sleight of Hand +5 (picks his manacles: DC 12).
> *Unarmed strike:* +5, 1d4 + 3. **Flurry of Blows** (2 ki): two unarmed strikes as a bonus action. **Patient Defense / Step of the Wind** (1 ki each). Ki 2.
> Can join the party as a guide (or replace a fallen PC; a DM may level him with the party).

| Who | 1e | 5e | CR |
|---|---|---|---|
| **Zodznog** (12), half-orc cook | AC 6, HD 1, hp 6, improvised 1–4 | (custom) AC 12 (hide), HP 16, Speed 30. *Cleaver* melee or thrown +4, 20/60, 1d6 + 2; *heavy pot* thrown +4, 20/60, 1d4 + 2. Relentless Endurance | 1/4 |
| **Uzgrod** (24), half-orc groom | AC 5, HD 1, hp 6, scimitar 1–8 or dagger 1–4 | (custom) AC 14 (studded leather), HP 16. *Scimitar* +4, 1d6 + 2; *dagger* thrown +4, 20/60, 1d4 + 2. Relentless Endurance; prefers cover behind the wall or an ox (half cover) | 1/4 |
| **Snikscab, Nubgrod** (20, 21) | bugbears, hp 14 each | **Bugbear** (MM), named. Hostage rule (area 21): when one is dead and the other has **15 hp or fewer**, the survivor grabs a slave | 1 |
| **Wartslag** (27), bugbear smith | AC 5, HD 3+1, hp 16, 2–8 or hammer 2–5 | **Bugbear** (MM); his hammers use the javelin line (2d6 + 2 melee, 1d6 + 2 thrown). Seven hammers | 1 |

---

## 4 · Custom monsters

### 4.1 Mudtiger (three sizes)
*1e: AC 6, MV 6"//12" (3"), HD 2–5, bite 2–5 (2–3 HD) or 2–8 (4–5 HD); electric burst 10 ft, 2–8 or 2–12, save vs breath for half, recharges on 5–6 (d6); magnetize; immune to electricity.*

| | **Mudtiger Fingerling-grown** (2 HD) | **Mudtiger** (4 HD) | **Great Mudtiger** (5 HD, area 64) |
|---|---|---|---|
| CR | 1/2 (100 XP) | 1 (200 XP) | 2 (450 XP) |
| AC / HP | 13 (natural) / 22 (4d8 + 4) | 13 / 37 (5d8 + 15) | 13 / 52 (7d8 + 21) |
| Bite | +4, 1d6 + 2 piercing | +5, 1d8 + 3 | +5, 1d8 + 3 |
| Electric Burst (Recharge 5–6) | 10-ft radius, **DC 11 Dex, 2d6 lightning**, half on a success | DC 12, **3d6** | DC 13, **3d6** |
| Where | 42 (×2), 63 (×1) | random (river), 56 (×2) | 64 |

All three: Medium monstrosity, unaligned. Speed 15 ft, swim 30 ft, burrow 10 ft (sand, mud, loose earth). STR 14 DEX 12 CON 14 INT 1 WIS 10 CHA 3. **Immune** to lightning. Amphibious. Can rear out of the water to bite someone in a boat.
**Magnetize.** Ferrous metal caught in the burst is magnetized for **1d4 + 1 rounds**. A creature wearing magnetized armor has its **speed halved**; a creature wielding a ferrous weapon while wearing magnetized armor, or within 5 ft of 30+ lb of magnetized metal, takes **−2 to attack and damage rolls** with it. A creature in ferrous armor within 5 ft of someone in magnetized armor also moves at half speed.
**Mudtiger fingerlings (area 63)** are a hazard, not a creature: a creature that enters the north pool or starts its turn there takes **2d4 piercing** (1d4 if it wears medium or heavy armor, the 5e reading of the 1e "plus half your AC"). The school also produces one **2d6 burst (DC 11)** filling the pool and 10 ft around it, Recharge 5–6.

### 4.2 Killer Frog (custom) · CR 1/4 (50 XP) — area 66
*1e: AC 8, MV 6"//12", HD 1+4, hp 8, 1–2/1–2/2–5.*
Small beast. **AC 11. HP 13** (3d6 + 3). Speed 20 ft, swim 40 ft. STR 12 DEX 13 CON 12. Amphibious, Standing Leap (20 ft long, 10 ft high). *Multiattack:* two claws (+3, 1 slashing) and a bite (+3, 1d4 + 1 piercing). They attack the moment anyone comes into sight; the fog makes the chamber **heavily obscured beyond 15 ft**.

### 4.3 Water Weird — area 55
**Water Weird** (MM, CR 3, 700 XP) with the module's riders: it attacks anyone who **stays in the chamber longer than one round** (searching the pool or fiddling with the doors counts). Reduced to 0 hp, it **re-forms in 2 rounds** at full hp unless *purify food and drink* is cast on the pool ⚑ D5.

### 4.4 Huge Spider (random) — the C12 / T1 block, CR 1.

---

## 5 · Hazards and traps

| Area | 1e | 5e |
|---|---|---|
| 1 | Murder hole and parapet | M8; murder hole = three-quarters cover, parapet = half cover |
| 1 door | Barred; knock opens; Open Doors −1; Bend Bars; 40 points | DC 17 Strength (Athletics), *knock*, or AC 15 / 40 hp. No lock to pick |
| 15, 16 | Top step bear trap: save vs breath or caught, 1–4, Open Doors to free, half speed until healed; lever in 17 locks it | **DC 11 Dex save** or **1d10 piercing** and **restrained**; **DC 15 Strength** (by the victim or a helper) opens the jaws. Speed halved until the damage is healed. Spotting the hinged step: **DC 15 Wisdom (Perception)** |
| 23 doors | latched; Open Doors; Open Locks jimmies; knock | DC 15 Strength or DC 15 thieves' tools |
| 26 door | locked; keys with Uzgrod and Wartslag; Open Doors −1; Bend Bars; 30 points | DC 15 thieves' tools, DC 17 Strength, or AC 15 / 30 hp |
| 27 | Stinkbomb: cloud over the dais and adjacent squares, 5 rounds; save vs poison or −1 Str per round, lasting 10 rounds | **DC 11 Constitution save** or **poisoned** while in the cloud and for **1 minute** after leaving it. Wartslag and the goblins are immune. One bomb |
| 37, 48 | Grates: Open Doors −1, Bend Bars, 50 points | DC 17 Strength, DC 20 to bend, or AC 19 / 50 hp |
| 51 | Barred iron door; padlock; 50 points; weapons through the bars | DC 15 thieves' tools (reaching through, with the bugbear watching), DC 17 Strength, AC 19 / 50 hp. **Through the bars:** spears and pikes normal; daggers and short swords −1; swords −2 (thrust only); slashing and bludgeoning can't pass. Ranged attacks: target has **half cover** |
| 55 doors | three keyholes, two fakes ring a chime; 40 points | The true keyhole (north: middle; east: bottom) can be spotted with **DC 15 Intelligence (Investigation)**. A wrong key or a failed pick rings the chime (draws the clerics, nothing else). AC 15 / 40 hp |
| 57 | Four counterweight snares: save vs breath or 1–4 and hung 15 ft up; loop AC 2, 8 points; a fall when cut free 1–6 | Spot a snare: **DC 13 Wisdom (Perception)**. Triggered: **DC 11 Dex save** or **1d10 bludgeoning** and hung upside down 15 ft up (restrained). The loop: **AC 11, 8 hp**, or cut automatically by someone at the ceiling. Cut free without a rope: **1d6** fall. Shouts here alert 58–59 |
| 61 | Puffballs: 5-ft cloud, save vs paralysis or paralyzed 3–18 turns; then die in 2–8 weeks unless cured | **DC 12 Constitution save** or **paralyzed for 3d6 × 10 minutes**. Then **puffball rot** (disease): no effect for 2d4 weeks, then death. Cured by *lesser restoration*, any magic that cures disease, or one dose of the clerics' **herbal cure** (5 doses: area 44 ×3, area 65 ×2) |
| 63 | Fingerling pool | §4.1 |
| 60 | Unholy relic aura | §7.2 |

---

## 6 · Encounters (difficulty checked for 4 PCs, scaled numbers)

Thresholds for 4 PCs (2014 DMG): L1 E 100 / M 200 / H 300 / D 400 · L2 200 / 400 / 600 / 800 · L3 300 / 600 / 900 / 1,600.

| Area | 6 PCs (as printed) | 4 PCs | Adj. XP (4 PCs) | Difficulty |
|---|---|---|---|---|
| 6 Barracks | 6 guards | 4 guards | 200 | L1 Medium; with the sergeant (2 rounds) 400 = **L1 Deadly**. Fight them apart |
| 10 Armory | Sergeant | Sergeant | 100 | L1 Easy |
| 12 Kitchen | Zodznog, 4 cooks | Zodznog, 3 cooks | 160 | L1 Easy–Medium |
| 17 North posts (night) | 4 goblins | 3 goblins | 300 | L1 Hard |
| 17 / 22 (day) | 2 guards each | 2 guards each | 75 | L1 Easy |
| 18 Glyrthiel | Glyrthiel | Glyrthiel | 200 | L1 Medium (*sleep*) |
| 19 Brubgrok | Brubgrok | Brubgrok | 450 | **L1 Deadly**, L2 Medium |
| 18 + 19 together | | | 1,300 | L2 Deadly, L3 Hard |
| 20 Taskmasters | 2 bugbears | 2 bugbears | 600 | L1 Deadly, **L2 Hard** |
| 24 Stable | Uzgrod, 6 slaves | Uzgrod, 4 slaves | 180 | L1 Medium |
| 27 Smithy | Wartslag, 2 goblins | Wartslag, 1 goblin | 375 | L1 Hard, L2 Easy |
| 28 Stair post | 2 goblins, 1 worg | 1 goblin, 1 worg | 225 | L1 Medium |
| 30 Den (night) | 8 goblins | 5 goblins | 500 | L1 Deadly, L2 Medium |
| 31 Barracks (day) | 8 goblins | 5 goblins | 500 | as 30 |
| 32 Worg den | 2 worgs | 2 worgs | 300 | L1 Hard |
| 34 Gallery (night) | 4 goblins | 3 goblins | 300 | L1 Hard |
| 39 Diggings (night) | teams of 2–5 goblins | teams of 2–3 | 200–300 | L1 Medium–Hard each |
| 41 Lower tunnel | 5 goblins | 3 goblins | 300 | L2 Medium |
| 42 Temple | cleric, 2 mudtigers | same | 600 | L2 Hard |
| 42–44 alarmed | + cleric, 6 goblins | + cleric, 4 goblins | 2,000 | **L3 Deadly**: the quarry climax; let them arrive in waves as printed (2 rounds) |
| 46 Goblin barracks (day) | 10 goblins | 7 goblins | 875 | L2 Deadly, L3 Hard |
| 47 Old diggings | 4 goblins | 3 goblins | 300 | L2 Medium |
| 51–53 Cells | 2 bugbears (+1 patrolling) | same | 600 | L2 Hard |
| 55 Antechamber | water weird | same | 700 | L3 Medium–Hard; avoidable |
| 56 Beach | 2 mudtigers (4 HD) | same | 600 | L3 Medium; avoidable (killer frogs as bait) |
| 58–59 Troglodytes | 3 | 2 | 150 | L3 Easy |
| 60 Rubbish | 4 zombies | 3 zombies | 300 | L3 Easy |
| 62 Charnel | 2 ghouls | 2 ghouls | 600 | L3 Medium |
| 63 Nursery | troglodyte, mudtiger (2 HD) + pool | same | 225 | L3 Easy + hazard |
| 64 Breeding pool | great mudtiger, 2 troglodytes, cleric (65) | same | 1,300 | **L3 Hard**: the cavern climax |
| 66 Frogs | 8 killer frogs | 5 | 500 | L3 Medium (fog) |

**Random encounters (M2):** wild boar (**Boar**, MM, its Relentless trait is the 1e fight-on rule), black bear (**Black Bear**), wolves 2–5 (**Wolf**; 2–3 for 4 PCs), panther (**Panther**), Huge Spider; ghouls 1–2 (**1 at L1**); patrol: 2–5 Guards on riding horses (2–3 for 4 PCs) **or** 2 goblin worg-riders (**1 at L1**: 2 riders and 2 worgs are 600 XP, Deadly). Brubgrok or Glyrthiel rides with a patrol 25% of the time.

---

## 7 · Treasure and items

### 7.1 Treasure ⚑ D2
The printed hoards total about **12,800 gp** (1e gold-for-XP). The DMG budget for a 1st–3rd level stretch is roughly 7–8 CR 0–4 hoards, about **2,500–3,000 gp**, which is where T1's Moathouse landed. **Dividing every coin and gem/art value by 5, and snapping gems and art to the nearest DMG tier (10 / 25 / 50 / 100 gp), gives 2,640 gp**, with every description kept. Under 10 gp, items are trade goods at ÷ 5.

| Area | Printed | 5e |
|---|---|---|
| 3 | 3 carpets + 12 tapestries, 75 gp each (bulky: 50 / 30 lb) | 15 at **10 gp** each (150 gp) |
| 6 | 24 locked chests: 3,000 sp, seven 100-gp jewels (silver rings and armbands) | **600 sp**; seven **25-gp** art objects |
| 10 | pay chest (sergeant's key): 5,000 sp | **1,000 sp** |
| 13 | 15 rare bottles, 1,500 gp (two turns to sort) | 15 bottles at **25 gp** (375 gp); 20 minutes to sort |
| 18 | ring 75; 3 jade figurines 100 each; pouch 10 sp, 15 gp, 5 pp; carpet 75; 8 tapestries 30 each; spellbook | ring **10 gp**; figurines **25 gp** each; pouch **2 sp, 3 gp, 1 pp**; carpet **10 gp**; tapestries **6 gp** each; **spellbook** (§7.2) |
| 19 | strongbox (20 points to break): 350 pp, 10 carnelians 50 each; 5 furs and silks 200 each | **70 pp**; 10 carnelians at **10 gp**; 5 furs at **50 gp**; strongbox AC 19 / 20 hp, or Brubgrok's key. **+ Brubgrok's longsword +1** |
| 20 | two pouches, 100 gp each | **20 gp** each |
| 30 | 9 pots: 700 sp, 200 gp, 9 bloodstones 15 each | **140 sp, 40 gp**, 9 bloodstones at **3 gp** |
| 44 | 2 chests: 3 silver unholy symbols, 260 gp, 18 pp, 6 bloodstones, 3 potions of healing, 3 herbal cures; keys to area 55 | 3 symbols at **5 gp**; **52 gp, 4 pp**; 6 bloodstones at **3 gp**; **3 potions of healing**; **3 herbal cures**; keys |
| 46 | 12 pots: 900 sp, 250 gp, 23 quartz crystals 10 each | **180 sp, 50 gp**; 23 quartz at **2 gp** |
| 52 | 3 silver urns 25 each; two hold 300 gp each | urns **5 gp** each; **60 gp** in each of two |
| 60 | unholy relic, 500 gp art | **100 gp**; magic (§7.2) |
| 65 | chest: 2 herbal cures | **2 herbal cures** |
| Reward | Neistor, 500 gp | **500 gp** (not scaled) |

Individual treasure on guards and goblins: none printed; none added.

### 7.2 Items (each gets a vault note ending in `## FGU Import`)

| Item | 1e | 5e |
|---|---|---|
| **Brubgrok's Longsword +1** | long sword +1 | *Weapon +1 (longsword)*, uncommon (DMG) |
| **Potion of Healing** ×3 | potions of healing | *Potion of healing* (DMG), common |
| **Herbal Cure** ×5 | herbal preparation that cures the puffball malady | (custom) common potion: drinking it ends **puffball rot**. Worthless for anything else |
| **Glyrthiel's Spellbook** | *friends, read magic, shield, sleep, unseen servant* | Spellbook (custom record): *comprehend languages*, *shield*, *sleep*, *unseen servant* (*friends* is a 5e cantrip, so it isn't in the book; *read magic* → *comprehend languages*) |
| **Relic of the Staring Eye** | pyramid of greased iron with onyx and copper eyes; 30-ft aura, −2 to turn undead, +2 to control | (custom) wondrous item, uncommon: **undead within 30 ft have advantage on saving throws against Turn Undead**; a creature that casts *animate dead* within the aura can control **one extra** undead with that casting. Art value 100 gp |
| **Stone-headed Mace** ×3 | stone mace, −1 vs AC 5 or better | (custom) mundane: as a mace, **−1 to attack rolls against a creature in medium or heavy armor**; not ferrous (immune to Magnetize) |
| **Glyrthiel's Chandelier** | *continual light* on one arm; lead cap and rod | *continual flame*; no market value. Room description only, no item record |

---

## 8 · Story award and advancement

Milestones (§0). For tables using XP: monsters' CR XP, plus **a story award of 100 XP per PC** for each of: Kwon found alive; the slaves in 12, 21, 24 and 53 freed; Brubgrok exposed (captured, or his papers taken to Neistor); the Highport link learned.

---

## 9 · Maps (cleaned scans, this pass)

Source: PDF pp. 28–29, 150-dpi greyscale (1163 × 1442 px each), cartography by Mike Schley. **Seven maps:**

| Map | Page | Scale | Notes |
|---|---|---|---|
| A0-1 Quarry (overview) | 28 | not to scale | Hilltop, shaft, cave entrance, guardhouse, paths |
| A0-2 Guardhouse Upper Level | 28 | 5 ft | Areas 15–22 |
| A0-3 Guardhouse Main Level | 28 | 5 ft | Areas 1–14; the shaded murder-hole square at 1 |
| A0-4 Guardhouse Lower Level | 28 | 5 ft | Areas 23–32 |
| A0-5 Quarry Main Level | 29 | 5 ft | Areas 33–39 |
| A0-6 Quarry Lower Level | 29 | 5 ft | Areas 40–53 |
| A0-7 Caverns | 29 | 5 ft | Areas 54–66 |

Per map: crop to the frame, level and despeckle, upscale ×2 (Lanczos), and export **GM** (as printed) and **Player** (area numbers, the arrow captions that give away connections such as "Sinkhole leads down to 61", and the 15/16 trap steps masked over with the floor tone). FGU images at the printed 5-ft grid, with the grid size set so FGU's grid lines up with the drawn one. Traced house-style versions (four per map, parchment) replace these in a later pass.

---

## 10 · Decisions for Greybeard

| # | Question | Recommendation |
|---|---|---|
| **D1** | Guards' AC. T1's rule says use the armor named; the armory rack holds **chain mail**, which with a shield is AC 18, and six of them become Deadly at 1st level. | **Use the MM Guard as is (AC 16, chain shirt and shield).** 1e AC 4 is the plain armored soldier, which is what the MM Guard is. The sergeant and Brubgrok keep plate (AC 20) |
| **D2** | Treasure: ÷ 5 with DMG-tier snapping (2,640 gp + 500 reward), or another method? | **÷ 5.** It lands on the DMG hoard budget and keeps every description, as T1 did with its budget |
| **D3** | Distances. The Background puts the quarry **half a mile** from the village (p. 6); Darkshelf and Environs says **about three miles inland** (p. 7). The tributary to the jetty "twists for more than a mile" (p. 8), but area 56 says "a little more than a quarter mile" (p. 23). | **Three miles inland; a mile of tributary** (the Environs section is the more detailed and the patrols need room). Recorded in Development Notes |
| **D4** | *Cause fear* isn't in the 2014 PHB (it's in *Xanathar's*, which isn't in the SRD that the FGU build copies from). | **Keep *cause fear* (XGE)** as a homebrew spell record in the module (the build supports homebrew spells), so the clerics play as printed. Fallback: a second *command* |
| **D5** | Water weird: MM CR 3, and it re-forms in 2 rounds. Fair in a 3rd-level section, but harsh if the party comes in by the river at 1st level. | **Keep both.** It only attacks those who linger, and the Introduction warns about the river entry |
| **D6** | Kwon as a PC replacement? | **Yes**, as an option on his NPC page; he stays a 2nd-level monk unless the DM levels him |
| **D7** | Tournament extras: A0 has none (it was written in 2013). Nothing to add | — (A1–A4 get pregens and a convention-mode page) |
| **D8** | FGU book layout: one page per keyed area (66 pages) or one page per section with areas as headings? | **One page per keyed area**, grouped in chapters: Introduction · Guardhouse · Quarry · Caverns · Conclusion · Appendices (Bestiary, Treasure, Development Notes). Matches the C12 module and makes every area linkable |

---

## 11 · Errata and source notes

- **Area 63:** the single troglodyte's line reads "hp 9 each".
- **Area 65:** the cleric casts *bless*, which isn't on his memorized list (*curse* is its reverse in 1e). Works as written in 5e.
- **Area 55:** "puify water" → *purify water* (5e *purify food and drink*).
- **Area 52:** three silver urns at 25 gp each; only two hold coins (the third is a working bed warmer).
- **Area 51** says the only other way into 52–53 is up the sinkhole of 49 and across to 50; **Kwon uses that route** (area 53). Kept.
- **Personnel roster (p. 9):** the column layout jumbles in text extraction; the day/night counts are Brubgrok 1, Glyrthiel 1, goblins 16 / 24, sergeant 1 / 1, guards 10 / 6, slaves 28 / 28, Nubgrod, Snikscab, Uzgrod, Wartslag, Zodznog 1 each, worgs 3 / 3.
- **Text extraction:** `_source/A0 - extracted source text.md`, column-aware. The map insets on pp. 13, 15, 17, 19, 21, 23 and 25 leave stray letter fragments down the column edge; the vault notes are written from the page images where that happens.
