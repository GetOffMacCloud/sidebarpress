---
tags: [adventure/T1, conversion, fgu-prep, toee]
adventure: "T1 - The Village of Hommlet"
source: "T1-4 The Temple of Elemental Evil (TSR 1985), PDF pp. 5–30"
status: draft for review (round 1, 2026-11-16)
created: 2026-11-16
publish: false
---
# T1 — 5e Conversion Ledger

This ledger records every number the 5e table or the FGU build has to touch: the 1e source, the 5e conversion, and the reason for the change. **Review it before any vault notes, statblocks or FG import blocks are generated from it.** Page numbers are PDF pages in `_source/T1-4 source.pdf`, where printed page = PDF page − 1.

> [!info] Scope of this pass
> - **A straight 1e → 5e conversion that fits any campaign.** It converts T1 as published (the Introduction, Part 1 Hommlet, Part 1A the Moathouse, and the Interlude). It isn't prep for any one table. The Tourist In Greyhawk notes were used as a cross-check only.
> - **Rules:** 5e 2014 (PHB, DMG, MM). Statblocks come from the MM wherever it has an equivalent. Custom statblocks are marked **(custom)**.
> - **Text:** stays close to Gygax. This ledger changes numbers, not prose.
> - **Decisions waiting on Greybeard** are marked **⚑ D#** and collected in §9.

---

## 0 · Recommended 5e level

**Answer: start at 1st level, finish T1 at 4th, for 4–6 PCs.**

The module is written for 5–8 characters of 1st–2nd level (p. 5, p. 21) and was meant to be deadly. With the MM conversions below, the 5e math gives this progression:

| Stretch | 5e level (4 PCs) | Why |
|---|---|---|
| Hommlet (social play, hirelings, intrigue) | 1 | Almost no combat unless the PCs pick a fight |
| Moathouse upper ruins (areas 1–17) | 1–2 | The frogs are Deadly at L1 and Medium at L2. The brigands are Deadly at L2, but they flee from a capable party (p. 23) |
| Moathouse dungeon, west and south (areas 18–31) | 3 | The ogre and the crayfish are Easy. The ghouls are Deadly. The bugbears and gnolls are Deadly by design, and the gnolls can be talked out (p. 26) |
| The north wing (areas 32–35, Lareth) | 4 | Lareth alone is Medium. **Once the alarm goes up, the north wing is Deadly at any tier-1 level.** The original is built the same way, so it stays: the right play is to split the guards up or avoid them |

Suggested milestones: level 2 after the upper ruins, level 3 on entering the dungeon, level 4 after clearing the west wing, level 5 at the end of T1 (the Interlude). T2-4 opens at 5th level.

**Party size.** The module has its own scaling rule (p. 21, area 1): for a small or weak party, *remove* creatures, never add them. Keep that rule and apply it everywhere. The §6 table gives the scaled numbers for a party of 4.

---

## 1 · Conversion rules used throughout

These are the C12 rules, plus the T1-specific lines marked 🆕.

| 1e | 5e rule applied | Why |
|---|---|---|
| Descending AC | **19 − AC**, then checked against what the creature is wearing. 🆕 **Armored NPCs use the 5e value of the armor named** (plate & shield = 20, chain & shield = 18, scale & shield = 16, leather & shield = 13, padded = 11) | The 1e Dex bonuses on NPCs don't map cleanly; the armor named in the text does |
| Movement `12"` | **30 ft** (×2.5). `9"` → 25 ft (MM creatures keep their MM speed), `6"` → 15 ft, `15"` → 35–40 ft, `18"` → 45 ft | 12" is the human baseline |
| Hit points | **Not carried.** Rebuilt to the DMG CR table, or taken from the MM statblock | 1e and 5e price HP differently |
| 1e monster with an MM equivalent | **Use the MM statblock**, plus only the module's riders | FG already ships it |
| 🆕 **Level 0 villager / militiaman** ("treat as 1-1 HD", p. 7) | **Commoner** (CR 0). An armored militiaman (scale, ring or chain) is a **Guard** (CR 1/8). Weapons swapped to the ones named | That's what the text says they are |
| 🆕 **Named NPC classes** | Fighter 1–3 → Guard or Thug. Fighter 4–6 → Veteran or Knight. Cleric 3 → Acolyte+ / Priest. Druid 3 → Druid. Thief 3–4 → Spy. M-U 8 → Mage. Assassin 7–10 → Assassin. Bigger names are custom (§3) | |
| Saving throws | Breath → Dex · Poison/death → Con · Paralysis → Con · Spell → the save the 5e spell uses | |
| % chances in the text | Converted to a DC that gives about the same success chance at the expected level. Where the text rolls dice for an NPC's choice (e.g., "50% likely to be here"), **the die roll is kept as printed** | Same doctrine as C12 |
| Surprise "on 1–3 / 1–4 / 1–5 (d6)" | The creature makes a Dex (Stealth) check against passive Perception: **advantage for 1–4, advantage +5 for 1–5.** Creatures that "always surprise" are hidden at the start | 5e has no surprise die |
| 1 Turn | **10 minutes.** Wandering-monster checks every 10 minutes | |
| 🆕 1e rounds in timing text ("arrive in 4–5 rounds") | **Kept as 5e rounds.** This makes the 1e timings faster at the table, which suits the alarm design | 1e rounds were 1 minute, but the pacing intent is "arrives mid-fight" |
| Thief % abilities | Rogue skill checks and Sneak Attack | |
| "+1 or better weapon to hit" | Resistance to nonmagical B/P/S | None in T1 |
| Concealed / secret door | **DC 15 Wisdom (Perception)** unless noted (e.g., area 22) | |
| Trap damage | DMG severity for levels 1–4: **Setback 1d10 / DC 10–11 · Dangerous 2d10 / DC 12–15 · Deadly 4d10 / DC 16–20** | DMG p. 121 |
| XP lines in statblocks | **Dropped.** Use MM CR XP. The module's story awards are restated in §8 | |
| Ability scores | 1e 18/xx → 5e 18. Otherwise kept | |
| Spells | Mapped to the 2014 PHB. Where nothing matches, the closest PHB spell is used and flagged (§5) | |

---

## 2 · Module-wide mechanics

| # | 1e text (page) | 5e conversion |
|---|---|---|
| M1 | **Agents report** to their masters. If they're mistreated, the masters "seek to redress matters" (p. 7) | Unchanged. The agent web is in §3.4 so the DM can track who reports to whom |
| M2 | **Lareth's avenger.** If Lareth's possessions turn up, a **10th-level assassin** comes in 5–20 days (p. 26) | **Assassin** (MM, CR 8) arrives in **1d16+4 days**. Jaroo and Terjon help the targets. If the assassin dies, nothing more follows. Unchanged otherwise |
| M3 | **Moathouse upper level:** random encounter 1 in 12 each Turn; 1d6 table (p. 21) | **1 on a d12 every 10 minutes.** Table in §4.3 |
| M4 | **Moathouse dungeon:** 1 in 6 each Turn; 1d8 table (p. 23) | **1 on a d6 every 10 minutes.** Table in §4.3 |
| M5 | **Mounts in the marsh:** 90% (warhorse 10%) panic at the frogs; then 50% throw the rider, 50% mired (p. 21) | DC 15 Wisdom (Animal Handling) check by the rider. A warhorse is calm on a 3+ on a d20. If the check fails, roll twice: the rider makes a **DC 10 Dex save or is thrown** (1d6 bludgeoning, prone); the mount is mired on a 50% roll (DC 12 Strength (Athletics) by the mount, with help, to pull it free) |
| M6 | **Drawbridge** (area 2): a mount breaks through. Horse 50%, mule 30%, pony 20%. It ends up at ⅔ hp, half speed (p. 22) | Same percentages (d10: horse 1–5, mule 1–3, pony 1–2). The mount's hit point maximum drops by a third and its speed is halved until it gets magical healing |
| M7 | **The Moathouse sigil:** the yellow eye of fire, and the crossed-arms-before-the-face sign (area 24) | Unchanged. Wearing the cape *and* making the sign stops Lubash attacking. Anyone who saw it done can copy the sign with **DC 10 Wisdom (Insight)** |
| M8 | **Hommlet militia muster** (p. 7): fight it out on the tabletop if there's a general battle | Militia = Commoners and Guards (§3.1). The Elder musters about 40 militia in 10 minutes. Rufus commands, and Burne's Badgers (§3.3) form the core |
| M9 | **Prices.** The Inn menu, Trading Post markups, moneychanger fees and armor availability (pp. 14–18) | **Kept as printed.** 5e uses the same coins, electrum included. "List price" means the PHB price |

---

## 3 · Hommlet — NPC conversions

### 3.1 Villagers and militia (level 0)

Each 1e line maps to a **Commoner** (CR 0) or a **Guard** (CR 1/8), with the named weapon. Armor sets AC per §1. Hit points: Commoner 4, Guard 11, unless rolled. **The printed hidden caches stay as printed** (⚑ D1).

| Area | Who | 5e | AC | Notes |
|---|---|---|---|---|
| 1 | Farmer; sons (2) | Commoner ×3 | 12 / 13 | Bill-guisarme → glaive 1d10. Flail, axe. Of the Old Faith |
| 1 | Farm dogs (2) | Mastiff ×2 | 12 | Attack only if the family is threatened |
| 2 | Elmo's father (Captain of the militia), Ftr 4 | **Veteran** (CR 3) | 16 (scale & shield, if prepared) / 10 | Longsword, light crossbow. Hides his rank |
| 2 | Servant | Commoner (club) | 12 (shield) | |
| 3 | Woodcutter | Commoner | 11 | Battleaxe, heavy crossbow |
| 4 | Sons (2) | Commoner ×2 | 11 | Handaxe or club |
| 5 | Farmer; manservant | Commoner ×2 | 11 / 10 | Longsword; voulge → glaive |
| 6 | Leatherworker; eldest son | Commoner ×2 | 13 / 11 | Sling, axe, dagger |
| 7 | Stableboy, groom | Commoner ×2 | 10 | Spear or club |
| 10 | Son-in-law; apprentices (4) | Commoner ×5 | 13 / 10 | Spear, dagger; awl (1 piercing) |
| 11 | Tailor | **Commoner (custom rider)** | 10 | **Knife Expert:** dagger and light crossbow attacks at **+5, 1d4+4** (1e: "as a 7th-level fighter, +2 damage"). Speaks Dwarvish, Elvish, Halfling. CR 1/4 |
| 12 | Farmer and son | Commoner ×2, Str 16 | 13 | Flail, morningstar |
| 14 | Carter; son; drivers (2) | **Guard** ×2; Commoner ×2 | 16 / 16 / 11 | Glaive; spear; club, light crossbow |
| 16 | Cabinet maker; apprentice | **Guard**; Commoner | 16 / 13 | Spear, morningstar |
| 17 | Potter; sons (2) | Commoner ×3 | 13 / 11 | Glaive; spear, light crossbow |
| 18 | Braumeister; nephew; apprentices (3) | **Guard** ×2; Commoner ×3 | 16 / 16 / 10 | Mace; shortsword. **Dog: Mastiff**, CR 1/8. *The braumeister's 1e line has no XP. OCR/print gap, no effect* |
| 19 | Herdsman Black Jay, Ftr 2 | **Thug** (CR ½) | 18 (chain & shield) | Longsword; longbow. Friend of the elves. Dogs (3): Mastiff |
| 21 | Farmer; sons (3) | Commoner ×4 | 11 / 11 / 13 | Military fork → spear; guisarme → glaive |
| 22 | Mytch the Miller; servant | **Guard**; Commoner | 16 / 11 | Servant fires 2 arrows → shortbow. Dog: Mastiff |
| 23 | Farmer; son; daughter (Ftr 1) | Commoner ×2; **Guard** (unarmored) | 11 / 11 / 10 | Fauchard-fork → glaive. Sling |
| 25 | Herdsman; son; cousin | Commoner ×3 | 11 | Shortbow; spear. Dogs (2): Mastiff |
| 26 | Wainwright; nephews (2) | Commoner ×3 | 13 / 11 | |
| 27 | Elder's sons (4); hired hand | **Guard** ×4; Commoner | 16 / 11 | Longsword or spear; heavy crossbow |
| 28 | Carpenter; brother | Commoner ×2 | 14 (studded & shield) / 11 | Battleaxe; spetum → spear |
| 29 | Stonemason; apprentices (3) | **Guard**; Commoner ×3 | 18 (chain & shield) / 10 | Military pick → war pick |
| 32 | Laborers (10) | Commoner ×10 | 10 | |

### 3.2 Named NPCs

| Area | NPC | 1e | 5e | AC | Key riders and gear |
|---|---|---|---|---|---|
| 2 | **Elmo** (the Viscount's agent, plays a drunk) | Rgr 4 (HD 5), hp 41, S 18 | **Veteran** (CR 3), *Elmo variant* | 20 (chain +1, shield +1) / 10 in town | **Battleaxe +1** (1d8+5), **dagger +2**. Advantage on Wisdom (Survival). Longbow and 40 arrows (20 silvered) kept at home. Feigns drunkenness: Deception +4 |
| 7 | **Ostler Gundigoot**, innkeeper and sergeant of the militia | Ftr 2, hp 17 | **Thug** (CR ½) | 11 | Longsword. Insight +3 |
| 8 | **Brother Smyth**, the smith and assistant druid | Drd 3 | **Druid** (MM, CR 2) | 11 | Hammer (1d4) |
| 13 | **Rannos Davl**, the trader (secret Temple agent) | Thf 10, hp 48 | **Rannos Davl (custom, CR 4)** | 18 | *Studded leather +1*, *ring of protection*, *amulet of proof against detection and location*, *dagger +1*; *shortsword +1* under the counter. Sneak Attack 4d6, Cunning Action, Evasion, multiattack (2). hp 60 |
| 13 | **Gremag**, the trader (secret Temple agent) | Asn 7, hp 39 | **Assassin** (MM, CR 8) | 16 | *Chain shirt +1* (⚑ D2), *dagger of venom* (3 doses), *dust of disappearance* (3 pinches) |
| 13 | Groom; man-at-arms (Ftr 1) | — | Commoner (AC 13); **Guard** (AC 11, longbow) | | Both hire out at 2 gp/day, and both spy for the traders |
| 15 | **Nira Melubb**, moneychanger | Thf 3 | **Spy** (CR 1) | 12 | *Dagger +1* in his boot; *longsword +1* under the counter |
| 15 | Moneychanger's guard | Ftr 3, hp 17 | **Thug** (CR ½) | 18 (chain & shield) | Longsword, light crossbow |
| 15 | War dogs (2) | HD 2+2 | **Wolf** (CR ¼), reskinned as *war dog* | 13 | |
| 20 | **Calmert**, priest of St. Cuthbert | Clr 3, hp 14 | **Acolyte** (CR ¼), upgraded to 3rd-level casting | 20 (plate & shield) | *Mace +1*. hp 21. Spells in §5 |
| 20 | **Canon Terjon**, chief cleric | Clr 6, hp 41 | **Priest** (MM, CR 2), upgraded to 6th-level casting → **CR 3** | 15 | *Mace +1*, *ring of invisibility* (⚑ D2), *ring of animal influence* (1e *mammal control*). hp 45. Spells in §5 |
| 24 | **Jaroo Ashstaff**, druid of the Grove | Drd 7, hp 44 | **Jaroo (custom, CR 4)**: MM Druid with 7th-level casting | 11 (padded, Dex −1, *cloak of protection*); 16 with *barkskin* | *Scimitar +1*, *staff of the python*, *ring of invisibility* (⚑ D2), *cloak of protection*. **Shapechanger** (3/day: beast of CR 1 or lower). Advantage on saves vs lightning damage. hp 52 |
| 24 | Jaroo's bear | HD 3+3 | **Black bear** (CR ½) | 11 | Hides 95% of the time |
| 31 | **Burne**, "His Most Worshipful Mage of Hommlet" | M-U 8, hp 30 | **Mage** (MM, CR 6), 8th-level casting | 13 (*ring of protection*, mage armor if cast) | *Dagger +1*, *chime of opening* (10 uses left; 1e "51 charges"), *wand of magic missiles* (7 charges). Spells in §5 |
| 31 | **Rufus** | Ftr 6, hp 32 | **Knight** (MM, CR 3) | 20 (chain +1, shield +1) | *Battleaxe +1* replaces the greatsword (1d8+4). *Dust of disappearance* (12), *periapt of proof against poison* (1e *carnelian scarab*). Leadership kept |
| 31 | Badgers' captain | Ftr 5, hp 31 | **Veteran** (CR 3) | 20 (splint & *shield +1*) | *Longsword +1*, light crossbow |
| 31 | Badgers' lieutenant | Ftr 4, hp 28 | **Veteran** (CR 3) | 19 (chain & *shield +1*) | Flail, dagger, light crossbow |
| 31 | Tower guards (5) | Ftr 2 | **Guard** ×5 | 16 | Longsword. NG/LG |
| 31 | Men-at-arms a–p (16) | Level 0 | **Guard** ×16 | per table, p. 20 | Weapons per the chart. *Catapult* (a–d) and *scorpion* (e–f) operators: DMG siege rules (ballista stats for the scorpion; mangonel-lite for the light catapult: +5 to hit, 3d10) |
| I 6 | **Zert**, fighter (secret Temple spy) | Ftr 2, CE | **Thug** (CR ½) | 16 (scale & shield) | Longsword, dagger. Medium warhorse → *warhorse*. Double drinking capacity: advantage on saves vs drunkenness |
| I 10 | **Spugnoir**, evoker | M-U 2, hp 4 | **Spugnoir (custom, CR ⅛)**: Commoner with 1st-level wizard casting | 12 | Cantrips: *light*, *fire bolt*. 1st (2 slots): *detect magic*, *sleep* (1e *read magic* is free in 5e). Will trade for scrolls |
| I 13 | **Furnok of Ferd**, "treasure finder" | Thf 4, hp 18 | **Spy** (CR 1) | 15 | *Dagger +1* in his boot, the scroll (§7), a *ring of invisibility* (⚑ D2). Cheats: advantage at cards and dice (1e 60% / 75%) |
| I 14 | **Kobort** | Ftr 2, S 18 | **Thug** (CR ½), Str 18 | 19 (splint & shield) | Longsword, flail, lance. Heavy warhorse → *warhorse* |
| I 14 | **Turuko**, Baklunish monk | Mnk 3, MV 17" | **Turuko (custom, CR 1)** | 14 (Unarmored Defense) | Speed 40 ft. Multiattack: two unarmed strikes or quarterstaff, +5, 1d6+3. **Deflect Missiles** (reduce by 1d10+5). hp 27. LE |
| 32 | **The laborer-spy** | Ftr 2, hp 14 | **Thug** (CR ½) | 10 | *Dagger +1*, club |

### 3.3 Burne's Badgers

The roster (captain, lieutenant, 16 men-at-arms a–p, 5 tower guards) carries over **letter for letter**, as Guards in the AC column worked out from the armor in the chart. *Errata: p. 20 says "the four guards at areas T1, T4 and T10", but the tower key puts five guards at GT1, GT4, GT10 (two) and GT12. Use five.*

### 3.4 The agent web (for M1)

| Agent | Reports to | How |
|---|---|---|
| Elmo | Viscount of Verbobonc | Joins parties as a hireling |
| Otis (Nulb, T2) | Elmo's brother; Viscount | Avenges anything done to Elmo |
| Jaroo | Druids of the Gnarley Wood | Follows suspicious parties at a distance |
| Burne and Rufus | Viscount; Archcleric of Veluna | Council; hold the area |
| Rannos and Gremag | Temple, through a brigand courier | Spy through their groom and man-at-arms, and the laborer at 32 |
| Zert | Temple (he doesn't know about the traders) | Joins parties to betray them |
| Lareth | Temple and Lolth | Raids from the Moathouse. Paid through the traders' wagons |

---

## 4 · Moathouse — creature conversions

### 4.1 Upper level (areas 1–17)

| Area | 1e | 5e | CR | Riders and notes |
|---|---|---|---|---|
| 1 | Giant frogs, average (2), HD 2 | **Giant frog** ×2 | ¼ | The MM bite already grapples and swallows. **Tongue** (keep the module's version): reach 15 ft (large) / 10 ft (small). On a hit the target is pulled 10 ft, no damage. Escape DC 11, or hit the tongue (AC 11; any damage makes the frog let go and not use the tongue again). Largest frog has swallowed an amethyst (100 gp) |
| 1 | Giant frogs, small (4), HD 1 | **Giant frog, small** ×4 (MM giant frog: hp 9, bite 1d4+1, can't swallow) | ⅛ | Surprise on 1–4 → advantage on Stealth. The module's scaling rule applies |
| 4 | Huge spider (wolf spider), HD 2+2 | **Giant wolf spider** | ¼ | Hidden 15 ft overhead. Leaps 15 ft (1e 3") as part of its move. Advantage +5 on Stealth (1e 1–5). 71 cp, 38 sp, ivory box (50 gp) |
| 7 | Brigand leader, Ftr 2 | **Thug**, chain & shield, longsword or spear | 1 | AC 18. hp 32 |
| 7 | Aide, Lvl 0 | **Bandit** | ⅛ | AC 16 (ring & shield). Longsword or flail |
| 7 | Brigands (7), Lvl 0 | **Bandit** ×7 | ⅛ | Weapons per the chart (halberd, voulge → glaive). Behavior tiers (weak / capable / overwhelming) kept word for word |
| 11 | "Scores of bats" | **Swarm of bats** ×2 | ¼ | Anyone holding a light: **DC 13 Dex save or drop it**, and the flame goes out. In the dark, a melee attack that misses a bat **hits an adjacent ally on 11+ (d20)**. If it hits from behind, the ally takes an extra die of damage (1e "double damage vs rear AC") |
| 12 | Giant snake (huge adder), HD 4+2 | **Giant poisonous snake, elder (custom)** | 1 | MM giant poisonous snake with hp 33, bite +6, 1d4+4 piercing plus **3d6 poison** (DC 12 Con, half). The 1e poison was 2–8, or 1–3 on a save. Jeweled dagger (850 gp) |
| 13 | Giant rats (13), HD ½ | **Swarm of rats ×2 + giant rat ×3** | ¼, ⅛ | 13 single rats are Deadly at L1 because of action economy, while 1e HD ½ rats were fodder. Swarms keep the threat right. Disease (1e 5%/hit): **DC 10 Con save** on each hit, failure = MM giant rat *diseased* rider (sewer plague, DMG p. 257). Gold ring on the 5th stair: **passive Perception 18** or DC 18 search (1e 1 in 20) |
| 16 | Giant tick, HD 3 | **Giant tick (custom)** | ½ | AC 15, hp 22, speed 15 ft, climb 15 ft. *Bite:* +4, 1d6+2 piercing, and it attaches. *Blood drain:* while attached, the target loses **1d6 hp at the start of each of the tick's turns** (no roll needed). An action or a DC 12 Strength check pulls it off. Stirge pattern |
| 17 | Giant lizard, HD 3+1 | **Giant lizard** | ¼ | 1e "double damage on a 20" is just a crit in 5e. It swallowed a *shield +1*. **Rubble:** each round of disturbance, 50% chance it collapses: **DC 12 Dex save**, 2d10 bludgeoning (half on a save). Dangerous tier |

### 4.2 Dungeon level (areas 18–35)

| Area | 1e | 5e | CR | Riders and notes |
|---|---|---|---|---|
| 18 | Green slime (2) | **Green slime** (DMG p. 105 hazard) ×2 | — | Over the arch. 1e 75% → **DC 15 Dex save** for the first PC through the square, and for anyone crossing the north half of it. Looking up first or hugging the walls: **passive Perception 13** spots it and there's no save. Damage per the DMG (1d10 acid per turn; destroys nonmagical wood and metal; cure with fire, cold, radiant or *lesser restoration*) |
| 19–20 | Locked doors | Lock **DC 15** (thieves' tools). Door **AC 15, 50 hp** (1e "50 points of damage") | — | Contents in §7 |
| 21 | Zombies (12) | **Zombie** ×12 | ¼ | The ambush keeps its wave timing: 2 zombies, then 2 from the rear a round later, then 2 per round. 🆕 1e "piercing weapons do 1 point" → **resistance to piercing**. Zombies always act last in initiative (1e "always lose initiative"). Peridot (500 gp) behind a loose stone: **DC 13 Investigation** (1e 50%/round) |
| 22 | Secret door in the pillar | **DC 20** Perception to find it cold. **DC 15** once the blood trail is found (trail: **DC 15 Investigation**, only if the PCs search the floor carefully) | — | 30-ft shaft with iron rungs |
| 23 | Greased door | Opens silently. **DC 12** Perception notices the grease | — | |
| 24 | **Lubash**, ogre (HD 5+1 in the key, 4+1 in the stats summary) | **Ogre** | 2 | Bardiche → **greatclub damage, reach 10 ft** (polearm). The yellow eye + the sign stops him (M7). He chases only as far as area 18. *Small cloak of elvenkind* in his bedding |
| 25 | Prisoners | 2 merchants (**Commoner**), gnome (**Commoner**, Gnome Cunning) | 0 | Story awards in §8. The gnome's iron ring: gnomes within 100 miles have advantage on attitude checks toward the bearer (1e 70% / +25%) |
| 26 | Iron grate | **Trap: falling grate.** No damage in 1e, so none in 5e. It blocks the corridor. **Lifting it: DC 25 Strength (Athletics), up to 3 creatures can help (each helper with Str 19+ gives +5)**, or use the winch at 26a (secret door, DC 15) | — | Triggered by either false door (28). The far-off clang is heard throughout the level |
| 27 | Bugbears (6) | **Bugbear** ×6 | 1 | Surprise on 1–3 → MM *Surprise Attack* applies. ⚑ Scale: 4 bugbears for 4 PCs. Leader's "bracelet" = silver necklace (450 gp) with 5 chrysoprase (4 × 50, 1 × 100) |
| 29 | Gnolls (9) | **Gnoll** ×9 | ½ | **Parley:** 1e 75% they stop and listen → **DC 8 Charisma (Persuasion)**, with advantage if the offer is coin. They desert for 6 gp each (18 for the leader). For double, they guide the PCs north. They speak Gnoll, Goblin (bugbear) and Giant (ogre); no Common. Two carry longbows |
| 30 | Giant crayfish, HD 4+4 | **Giant crayfish (custom)** | 2 | Large beast. AC 15, hp 45, speed 15 ft, swim 30 ft. Multiattack: two claws, +5, **2d6+3** each; grappled on a hit (escape DC 13, one target per claw). Retreats into the deep pool when below half hp and doesn't come back for 24 hours. Treasure on the ledge: **DC 10 Dex check** unless searched by hand, or it slips away (1e 50%) |
| 31 | Ghouls (4) | **Ghoul** ×4 | 1 | The MM elf exception matches 1e. The den (31a), the gold trail and the warren (31b) are kept word for word |
| 33 | Guardsmen (6), Ftr 1 | **Guard** ×6 | ⅛ | AC 16 (scale & shield). Longsword, dagger, light crossbow (30 bolts). **Hoot** → the alarm. **Howl** → everyone, Lareth included |
| 33 | Sergeant, Ftr 2 | **Thug**, chain & shield | 1 | AC 18. Morningstar, warhammer, dagger |
| 34 | 12 guards, 2 sergeants | as at 33 (6 of the guards carry spears, not crossbows) | | Six guards and a sergeant reinforce area 33 in **4–5 rounds** |
| 34 | **The lieutenant**, an "evil hero" | Ftr 4, hp 31 | **Veteran** | 3 | AC 20 (plate & shield). Longsword, longbow, handaxe, dagger. Always beside Lareth. *The Tourist vault calls him Osred Burch; the module leaves him unnamed* |
| 35 | **Lareth the Beautiful** | Clr 5, hp 44 | **Lareth (custom)** | 4 | See below |

**Lareth the Beautiful (custom, CR 4).** Medium humanoid (human), chaotic evil. **AC 19** (*plate armor +1*). **hp 58** (9d8+18). Speed 30 ft. Str 18, Dex 14, Con 14, Int 12, Wis 18, Cha 18. Saves Wis +6, Cha +6. Skills Deception +6, Insight +6, Persuasion +6, Religion +3. **Condition immunities: paralyzed** (*phylactery of action*). Languages Common, Abyssal, Undercommon.
- *Spellcasting.* 5th-level cleric, Wis, spell save DC 14, +6 to hit. Spells in §5.
- *Multiattack.* *Staff of striking* and mace.
- *Staff of striking* (right hand): +9 to hit, **1d6+7** bludgeoning. He can spend up to 3 charges on a hit for **+1d6 force** each. 10 charges (⚑ D2).
- *Mace* (left hand, off-hand): +6 to hit, 1d6 bludgeoning (no ability modifier to damage).
- *Tactics (p. 26).* Stays defensive and commands. Casts *hold person* and *command* on the strongest PCs, *silence* on casters, *darkness* to cover a retreat. If the fight turns, he offers all his nonmagical treasure as ransom.

### 4.3 Random encounters

**Upper level:** 1 on a d12 every 10 minutes. Roll a d6. They **don't** deplete the keyed areas.

| d6 | 1e | 5e |
|---|---|---|
| 1 | Giant rats (2–8) | Giant rats (1d4+1), or 1 swarm of rats |
| 2 | Scraping noise | Unchanged |
| 3 | Giant tick overhead | Giant tick (custom). Hidden: advantage on Stealth |
| 4 | Squeaking and rustling | Unchanged |
| 5 | Brigands (2–5) | Bandits (1d4+1), reinforcing area 7 |
| 6 | Footsteps (echoes) | Unchanged |

**Dungeon level:** 1 on a d6 every 10 minutes. Roll a d8.

| d8 | 1e | 5e |
|---|---|---|
| 1 | Footsteps (echo) | Unchanged |
| 2 | Giant rats (3–12) | 1 swarm of rats + 1d4 giant rats |
| 3 | Thumping (the lizard) | Unchanged |
| 4 | Zombies (2–8) | Zombies (1d4+1) |
| 5 | Bugbears (1–2) on patrol | Bugbears (1d2) |
| 6 | Moaning wind | Unchanged |
| 7 | Distant rattling | Unchanged |
| 8 | Gnolls (2–5) on patrol | Gnolls (1d4+1) |

*The dungeon "Statistics" box (p. 23) includes an ogre that isn't on the d8 table. It's Lubash's statline. HD 4+1 there, 5+1 in area 24: use the MM ogre either way.*

---

## 5 · Spell lists (1e → 2014 PHB)

| NPC | 5e casting | Prepared (5e) | Notes on the mapping |
|---|---|---|---|
| **Calmert** (Clr 3) | 3rd-level cleric, DC 13. 4 / 2 slots | 1st: *bless*, *command*, *detect evil and good*, *detect magic*. 2nd: *aid*, *silence* | *chant* → *aid*. *know alignment* → *detect evil and good* (1st) |
| **Terjon** (Clr 6) | 6th-level cleric, DC 13. 4 / 3 / 3 | 1st: *bless*, *command*, *cure wounds*, *detect magic*, *sanctuary*. 2nd: *hold person*, *lesser restoration*, *silence*. 3rd: *dispel magic*, *remove curse* | *slow poison* and *cure disease* → *lesser restoration*. *know alignment* dropped. *remove curse* fills the gap (1e cure disease was 3rd level) |
| **Brother Smyth** (Drd 3) | MM Druid as printed | MM list | 1e "any" |
| **Jaroo** (Drd 7) | 7th-level druid, DC 14. 4 / 3 / 3 / 1 | 1st: *animal friendship*, *cure wounds*, *detect magic*, *entangle*, *faerie fire*, *speak with animals*. 2nd: *barkskin*, *heat metal*, *pass without trace*. 3rd: *conjure animals*, *dispel magic*, *plant growth*. 4th: *freedom of movement* | *invisibility to animals* → *animal friendship*. *charm person or mammal* → *animal friendship*. *trip* and *warp wood* → nothing. *summon insects* → *conjure animals* (insects). *tree* → nothing. *neutralize poison* → *protection from poison* (choose instead of *plant growth*). *plant door* → nothing. *cure serious wounds* → *cure wounds* upcast |
| **Burne** (M-U 8) | 8th-level wizard (MM Mage adjusted), DC 14. 4 / 3 / 3 / 2 | 1st: *burning hands*, *detect magic*, *feather fall*, *jump*. 2nd: *levitate*, *mirror image*, *phantasmal force*. 3rd: *dispel magic*, *fireball*, *tongues*. 4th: *confusion*, *wall of fire*. **Spellbook extras:** *comprehend languages*, *light*, *darkness*, *see invisibility*, *gust of wind*, *dimension door*, *darkvision* (1e *plant growth* dropped: not a wizard spell in 5e) | *scare* → *phantasmal force*. *fumble* → *confusion*. *strength* → none. *infravision* → *darkvision*. *detect invisibility* → *see invisibility*. *read magic* is free |
| **Spugnoir** (M-U 2) | 1st-level wizard, DC 12. 2 slots | Cantrips: *light*, *fire bolt*. 1st: *detect magic*, *sleep* | |
| **Lareth** (Clr 5) | 5th-level cleric, DC 14. 4 / 3 / 2 | Cantrips: *guidance*, *sacred flame*, *thaumaturgy*. 1st: *command*, *cure wounds*, *protection from evil and good*, *sanctuary*. 2nd: *blindness/deafness*, *darkness*, *hold person*, *silence*. 3rd: *protection from energy* | *cause blindness* → *blindness/deafness*. *continual darkness* → *darkness*. *resist fire* → *protection from energy*. *know alignment* dropped. *cure light wounds* ×2 → *cure wounds* |

---

## 6 · Encounter math

2014 DMG thresholds and multipliers. The CRs are from §4. **Party of 4** (the 5-PC table follows).

| Encounter | Raw XP | Adj XP | L1 | L2 | L3 | L4 |
|---|---|---|---|---|---|---|
| M1 Pool: 2 giant frogs + 4 small | 200 | 400 | Deadly | Medium | Easy | Trivial |
| M4 Tower: giant wolf spider | 50 | 50 | Trivial | Trivial | Trivial | Trivial |
| M7 Brigands: leader + aide + 7 | 425 | 1,062 | Deadly+ | Deadly | Hard | Medium |
| M12 Elder adder | 200 | 200 | Medium | Easy | Trivial | Trivial |
| M13 Rats: 2 swarms + 3 giant | 175 | 350 | Hard | Easy | Easy | Trivial |
| M16 Giant tick | 100 | 100 | Easy | Trivial | Trivial | Trivial |
| M17 Giant lizard | 50 | 50 | Trivial | Trivial | Trivial | Trivial |
| M21 Zombies, first wave (4) | 200 | 400 | Deadly | Medium | Easy | Trivial |
| M21 Zombies, all 12 | 600 | 1,800 | Deadly+ | Deadly+ | Deadly | Hard |
| M24 Lubash | 450 | 450 | Deadly | Medium | Easy | Trivial |
| M27 6 bugbears | 1,200 | 2,400 | Deadly+ | Deadly+ | Deadly+ | Deadly |
| M27 4 bugbears (scaled) | 800 | 1,600 | Deadly+ | Deadly+ | Deadly | Hard |
| M29 9 gnolls | 900 | 2,250 | Deadly+ | Deadly+ | Deadly | Deadly |
| M30 Giant crayfish | 450 | 450 | Deadly | Medium | Easy | Trivial |
| M31 4 ghouls | 800 | 1,600 | Deadly+ | Deadly+ | Deadly | Hard |
| M33 6 guardsmen + sergeant | 350 | 875 | Deadly+ | Deadly | Medium | Easy |
| M33+34 full alarm | 1,400 | 5,600 | Deadly+ | Deadly+ | Deadly+ | Deadly+ |
| M35 Lareth alone | 1,100 | 1,100 | Deadly+ | Deadly | Hard | Medium |
| M35 Lareth + lieutenant + 4 guards | 1,900 | 3,800 | Deadly+ | Deadly+ | Deadly+ | Deadly+ |

**Party of 5**, in the same order: Pool Hard / Easy / Easy / Trivial · Brigands Deadly+ / Deadly / Medium / Easy · All 12 zombies Deadly+ / Deadly+ / Hard / Medium · 6 bugbears Deadly+ / Deadly+ / Deadly / Hard · 9 gnolls Deadly+ / Deadly+ / Deadly / Hard · Ghouls Deadly+ / Deadly+ / Hard / Medium · Lareth alone Deadly+ / Deadly / Medium / Easy.

**What the math says:**
- **The zombie gauntlet** (21) is fine as written, because the zombies come in pairs. Each round is Medium at L3, and the party can fall back up the stairs.
- **The bugbears and gnolls** are Deadly on purpose. The module gives a way out of each: the gnolls can be bribed, and the bugbears come to investigate a light, so the PCs can ambush them at the door. Use the module's scaling rule at 4 PCs (4 bugbears, 6 gnolls).
- **The north wing** is the original T1 meat-grinder. In 5e, as in 1e, it can't be won in a straight fight once the alarm is up. Keep it, and print a DM sidebar on how the alarm works (hoot → reinforcements in 4–5 rounds → howl → Lareth).

---

## 7 · Treasure and magic items

### 7.1 Treasure policy (⚑ D1)

As printed, T1 is rich by 5e standards. Hommlet's townsfolk hold tens of thousands of gp between them, though good PCs aren't meant to loot them. The Moathouse dungeon holds about **30,000 gp**, most of it in Lareth's fire-opal necklace (15,000 gp). The DMG expects about 2,000 gp for the whole of tier 1.

**Recommendation: keep the printed values,** since this edition stays close to the text. Add a one-box DM sidebar, *"Treasure at 5e scale"*, listing a ÷10 alternative for gems and art. The module limits the money in two ways: Lareth's assassin clause (anyone selling his things gets found out), and the Interlude's land and castle costs. The money is there for those.

### 7.2 Magic items (⚑ D2)

**Recommended rule:**
- Armor, shields and protection items are **capped at +1** (5e bounded accuracy).
- Weapons keep their printed bonus up to +2.
- Every other item converts to its nearest DMG item at whatever rarity that item has.
- Items that only NPCs hold (Jaroo's, Terjon's and Burne's) keep their printed power, because good PCs aren't meant to loot them.

| Where | 1e item | 5e item | Rarity | Note |
|---|---|---|---|---|
| 2 Elmo | chain mail +1, shield +2, battle axe +1, dagger +2 | *chain mail +1*, ***shield +1*** (cap), *battleaxe +1*, *dagger +2* | rare, uncommon, uncommon, rare | Cache in a lead-lined chest (blocks detection) |
| 13 Rannos | leather +1, ring of protection +1, medallion vs crystal balls & ESP, dagger +1, shortsword +1 | *studded leather +1*, *ring of protection*, *amulet of proof against detection and location*, *dagger +1*, *shortsword +1* | rare, rare, uncommon, uncommon ×2 | |
| 13 Gremag | shirt of chain mail +3, dagger of venom, dust of disappearance | ***chain shirt +1*** (cap; 1e +3), *dagger of venom*, *dust of disappearance* | rare, rare, uncommon | |
| TP 11 | 2 potions of invisibility, potion of speed, black scarab (TZGY) | *potion of invisibility* ×2, *potion of speed*, **scarab pass** (plot item, T2-4) | very rare ×2, very rare | 1e "20% a sage recognizes it" → **DC 20 Intelligence (Arcana or History)** |
| 15 Melubb | dagger +1, sword +1 | *dagger +1*, *longsword +1* | uncommon | |
| 19 Black Jay | 10 arrows +1, elven boots, elven cloak | *arrows +1* ×10, *boots of elvenkind*, *cloak of elvenkind* | uncommon | |
| 20 Terjon | rings of invisibility and mammal control, mace +1 | *ring of invisibility*, *ring of animal influence*, *mace +1* | legendary, rare, uncommon | NPC-only |
| C 11 | scroll of 7 clerical spells (1st–7th), amulet of life protection | *spell scrolls* (1st–7th, one each), **amulet of life protection (custom, rare, attunement):** advantage on saves vs possession and *magic jar*, and your soul can't be trapped or held | — | DM picks the scroll spells from the cleric list |
| C 14 | mace +1, scroll of protection from demons | *mace +1*, *scroll of protection (fiends)* | uncommon, rare | Y'dey's cache |
| 24 Jaroo | scroll of weather summoning, potion of invulnerability, decanter of endless water, cloak +2, ring of invisibility, staff of the serpent (python), scimitar +1 | *spell scroll (control weather)*, *potion of invulnerability*, *decanter of endless water*, *cloak of protection*, *ring of invisibility*, *staff of the python*, *scimitar +1* | — | NPC-only. Fire-trapped stone box: **2d10 fire, DC 13 Dex half**; finding it is **DC 18 Perception** (1e "½ normal chance") |
| 31 Burne | ring of protection +2, chime of opening, wand of magic missiles, dagger +1 | *ring of protection* (+1), *chime of opening*, *wand of magic missiles*, *dagger +1* | rare, rare, uncommon, uncommon | Staff has *Nystul's magic aura* on it (*arcanist's magic aura*): not magic |
| 31 Rufus | chain +1, shield +1, battle axe +1, dust (12), carnelian scarab vs poison | *chain mail +1*, *shield +1*, *battleaxe +1*, *dust of disappearance*, *periapt of proof against poison* | rare, uncommon ×2, uncommon, rare | |
| GT 5 | 6 arrows +2 | *arrows +2* ×6 | rare | |
| GT 6 | scroll: comprehend languages, mirror image, pyrotechnics, web, suggestion, ice storm, transmute rock to mud | *spell scroll* ×7, same spells | — | 5e has all seven |
| I 13 Furnok | dagger +1, scroll of protection from magic, ring of invisibility | *dagger +1*, **scroll of protection (magic) (custom, rare):** 10-ft radius around the reader, 5 minutes; spells cast from outside can't affect creatures inside. ***Ring of invisibility*** (⚑ D2: legendary, and Furnok can easily die with the party → recommend *potion of invisibility* ×2 instead) | | |
| M 7 | 4 arrows +1 (buried chest) | *arrows +1* ×4 | uncommon | |
| M 9 | very fine broadsword | *longsword* (fine work, 50 gp) | — | Not magic |
| M 17 | shield +1 (in the lizard) | *shield +1* | uncommon | |
| M 24 | elven cloak (small) | *cloak of elvenkind* (Small) | uncommon | |
| M 30 | scroll: push, stinking cloud, fly | *spell scroll* ×3: *thunderwave* (1e *push*), *stinking cloud*, *fly* | — | Watertight bone tube |
| M 31a | potion of undead control, scroll of protection from undead, 7 holy water | **potion of undead control (custom, rare):** for 1 hour, cast *command* (DC 13) on undead as a bonus action, once per round. *Scroll of protection (undead)*. *Holy water* ×7 | | |
| M 35 | plate mail +1, staff of striking (20 charges), phylactery of action | *plate armor +1*, *staff of striking* (10 charges, ⚑ D2), **phylactery of action (custom, rare, attunement):** you can't be paralyzed | rare, very rare, rare | The *staff of striking* is very rare. As Lareth's weapon it's the point of the fight. Once the PCs have it, the 10 charges are the dial |

### 7.3 The big numbers (as printed)

| Where | Treasure | gp |
|---|---|---|
| 15 Melubb's trapped chest | coins, gems, 7 pieces of jewelry, 50 gold ingots | ≈ 29,100 |
| 27 The Elder's iron box and plate | coins, 4 pieces of jewelry, silver and gold dishes | ≈ 15,800 |
| 24 Jaroo's stone box | 42 gems | 16,380 |
| I 19 Gundigoot's iron box | 6 pieces of jewelry, coins | ≈ 17,400 |
| GT 6 Burne's rafter chest | 122 gems, emerald ring, coins | ≈ 17,700 |
| 18 Braumeister | silver service, gold decanter, pearls, jewelry | ≈ 12,800 |
| M 35 Lareth's cabinet | fire-opal necklace | 15,000 |
| M 33–35 Lareth's people | gems, chains, silver service, unguents, black opal | ≈ 10,400 |

**Melubb's chest trap (area 15):** *poison needle* in the lock, 1 piercing + **2d10 poison**, DC 13 Con half. *Acid spray*, a 10-ft cone in front: **4d6 acid, DC 13 Dex half**. The trick catch on the back opens it safely: **DC 15 Investigation** to find it.

---

## 8 · Story awards and XP

The 1e XP figures in the statlines are dropped, since 5e awards XP by CR. The module's story awards carry over:

| Event (page) | 1e | 5e |
|---|---|---|
| Free the merchants (area 25) | +14 XP each; −50 XP each if they're slain | **+50 XP each.** If they die through the PCs' choices: **no award, and Hommlet hears of it**. In 4 weeks, a caravan brings 100 sp per merchant |
| Free the gnome (area 25) | +20 XP | **+50 XP** and the iron ring |
| Bribe the gnolls (area 29) | — | Award the gnolls' full XP (CR ½ ×9 = 900) if they desert. A bloodless win counts |
| Lareth ransomed instead of slain | — | Award his XP. The assassin clause still applies if his things are sold |

On milestone play, use the milestones in §0.

---

## 9 · Decisions for Greybeard

| # | Question | Recommendation |
|---|---|---|
| **D1** | Treasure: keep the printed values or scale them to 5e? | **Keep as printed**, plus a DM sidebar with a ÷10 alternative for gems and art |
| **D2** | Magic items: cap armor, shields and protection at +1? Replace Furnok's *ring of invisibility*? Give the *staff of striking* 10 charges instead of 20? | **Yes to all three.** NPC-only items keep their printed power |
| **D3** | 13 giant rats → 2 swarms + 3 giant rats (§4.1 area 13)? | **Yes.** Same threat, playable action economy |
| **D4** | Print a party-size scaling box for the bugbears, gnolls and the north wing? | **Yes.** It's the module's own rule (p. 21), applied consistently |
| **D5** | Hommlet–Nulb distance: the text says 6 miles (p. 6), 7 leagues from the moathouse (p. 21), "a half-day's journey… about two hours' ride" (p. 28) and "about thirty miles" (p. 29) | **Use Map 1** (pp. 130–131) and say so in Development Notes. The Interlude's ride is the one players see |

---

## 10 · Errata and OCR notes

**Errata in the 1985 text** (fixed silently in the vault notes, and listed in Development Notes):

| Page | Text | Fix |
|---|---|---|
| p. 20 | "the four guards at areas T1, T4, and T10" | Five guards: GT1, GT4, GT10 (×2), GT12 |
| p. 23 / p. 25 | Ogre HD 4+1 in the statistics box; 5+1 in area 24 | The MM ogre covers both |
| p. 11 | Braumeister statline has no XP | No effect in 5e |
| p. 9 | "and and small pearls worth 100 gp each" (no count given) | **Use 5 pearls** (⚑ minor; the Tourist vault assumed 5) |
| pp. 6, 21, 28, 29 | Hommlet–Nulb distance | D5 |
| p. 27 | Lareth's ability line prints no Intelligence ("S 18 W 18 D 17 C 16 Ch 18") | **Int 12** assumed in the custom statblock |

**OCR errors** in the extracted text, to be fixed when the vault notes are written: "wand stone chimneys" → "with stone chimneys" (p. 8); "Calmer" → Calmert (p. 12); "Ramos" → Rannos (p. 10); "S 9 116" → S 9 I 16 (p. 11); "Menu and WPrEicNeCs H" → "Menu and Prices" (p. 15); "10f lasks" → "10 flasks" (p. 24); "luz" → Iuz (throughout); "ores" → orcs (p. 29).

---

*Next, after review: write the T1 vault notes from this ledger (keyed areas, NPCs, bestiary, items, encounters), then the FGU import.*
