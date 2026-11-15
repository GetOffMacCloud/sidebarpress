---
tags: [adventure/C12, conversion, fgu-prep]
adventure: "C12 - The Forgotten Library of Raanet"
source: "C12 PDF (casl Entertainment, 2nd ed. Dec 2019, OSRIC)"
status: review (round 2, 2026-11-08)
created: 2026-11-08
publish: false
---
# C12 — 5e Conversion Ledger

Every number in the module that the 5e table or the FGU build has to touch, with its 1e source, its 5e conversion, and the reasoning. **Review this before any vault notes or FG import blocks are generated from it.**

> [!info] Scope of this pass
> - **Straight 1e → 5e conversion, party-agnostic.** This is a Sidebar Press conversion of the module as published, not a prep for any one table. Placing it in a campaign is the DM's job; §8 gives the Greyhawk names to help.
> - **Pregens (Appendix C)** are converted in [[C12 - Pregenerated Characters (5e)]]. **The spell series** that replaces 1e monster summoning is in [[C12 - Monster Summoning I-VII (5e)]].
> - Page numbers are PDF pages.

## 0 · Recommended 5e level

**Answer: 5e level 6 for six PCs (the module's own convention table), or level 7 for a group of four or five.**

The module says 1e levels 5–7 with six players, and its pregens are all 1e level 5. Once the monsters are converted (CRs 1–11, plus the CR 22 sphinx), the 5e numbers support that answer:

- **At 6 × level 5 the conversion plays like the 1e original.** The wraiths are Hard, and Yox and the wights are Deadly. The salamander rooms are 218–287% of the Deadly threshold. That matches a tournament module built to kill people.
- **At 6 × level 7 most rooms become Medium or easier.** Only the two salamander set pieces stay Deadly, and they are meant to be. The ring of fire resistance in Area 29 and the Area 22 safe zone are the module's intended answers.
- **Level 6 sits between the two**, and it is where the 1e-to-5e power curve puts a 1e level 5–7 party.
- **Avraasha is not meant to be fought** at any of these levels. The module says so: *"The Player Characters have little chance of defeating Avraasha in direct combat"* (p. 33). She converts to CR 22, so the 5e version keeps that.

Full table in **§6 Encounter math**.

---

## 1 · Conversion rules used throughout

| 1e / OSRIC | 5e rule applied | Why |
|---|---|---|
| Descending AC | **19 − AC**, then sanity-checked against a comparable MM creature | Standard mapping |
| Movement `12"` | **30 ft** (×2.5). `9"` → 25 ft, `6"` → 15 ft, `18"` → 45 ft, `24"` → 60 ft, `30"` → 75 ft | 12" is the human baseline |
| Hit points | **Not carried.** Rebuilt to the DMG CR table for the creature's threat | 1e and 5e price HP in different currencies (conversion doctrine) |
| Existing 1e monster with an MM equivalent | **Use the MM (2014) statblock** and add only the module's riders | FG already ships it, and it was designed as the 1e equivalent |
| "+1 or better weapon to hit" | Resistance to bludgeoning, piercing and slashing from nonmagical attacks | MM convention |
| "+2 or better weapon to hit" (custom creatures only) | Immune to nonmagical B/P/S, **and resistant to +1 weapons** | Preserves the stronger gate. MM creatures keep their MM line |
| Magic resistance % | *Magic Resistance* (advantage on saves vs spells). At 50%+, add *Legendary Resistance* | No percentile resistance in 5e |
| Energy drain | MM *Life Drain* (necrotic + max HP reduction) | MM wraith and wight already do this |
| Strength drain | Shadow-style: Str reduced by 1d4, death at 0, restored on short or long rest | MM shadow precedent |
| Save vs breath | Dexterity save | |
| Save vs poison or death | Constitution save | |
| Save vs spell | The save the equivalent 5e spell uses | |
| Bend bars / lift gates % | Strength (Athletics) check at the DC that gives the same success chance | |
| Concealed-door check | DC 15 Wisdom (Perception) | |
| Spell cast "at 12th level" | Dispel DC **16**, worked as the 5e spell cast with a 6th-level slot | 1e caster level to 5e slot |
| Trap damage | Mapped to DMG severity tiers for levels 5–10. **Setback** 2d10 / DC 10–11. **Dangerous** 4d10 / DC 12–15. **Deadly** 10d10 / DC 16–20. Where 1e fixed a die value, the nearest 5e die expression to the tier is used | DMG p. 121 |
| "No saving throw" | **Kept as no save** when the module says so explicitly | Straight conversion. Every case is flagged so you can soften it |
| Wandering-monster check per Turn | Every **10 minutes** | 1 Turn = 10 minutes |

> [!warning] Rarities and the "+2 = rare" problem
> 1e handed out +2 items like candy. **5e caps protection items at +1** (ring and cloak of protection), and **+2 weapons and armor are rare or very rare.** This module contains **four** 1e "+2 protection" items. The ledger converts them to the 5e item, not the 1e number (doctrine rule 4), and lists them in **D4**.

---

## 2 · Dungeon-wide mechanics

| # | 1e text (page) | 5e conversion |
|---|---|---|
| M1 | **The marble blocks travel magic.** Dimension door, plane shift, teleport and anything like them fail. Monster summoning still works (p. 6) | **No teleportation or planar travel in or out of the Temple** (or, once restored, the Athenium). This includes *misty step, dimension door, thunder step, teleport, plane shift, gate, word of recall, etherealness*, the *blink* spell, and any creature trait that teleports. **Conjuration (summoning) spells work normally.** Detected by *detect magic* as faint abjuration in every wall |
| M2 | No light anywhere (p. 7) | Darkness throughout. Plan light sources |
| M3 | Doors are thin iron. **Str 9+** to move them, **36 hp** to sunder (p. 7) | A creature with Str 9+ opens them; otherwise **DC 10 Strength (Athletics)**. Door: **AC 19, 36 HP**, immune to poison and psychic |
| M4 | Corridors 10 ft wide, 20 ft tall (p. 7) | Unchanged. Map surfaces at 5-ft squares |
| M5 | Wandering monsters: **1 on d6 per Turn**, Temple Incandescent only, campaign play only, and only in halls, empty rooms or cleared rooms (p. 6) | **1 on d6 every 10 minutes.** Same restrictions. The table is converted in §4.3 |
| M6 | **Ancient Xuloise** script everywhere | Not a PC language. Readable with *comprehend languages* or *tongues*. Without magic: DC 20 Intelligence (History) for the gist, **DC 15 if the reader knows a Suel-descended language** *(conversion call; the 1e text gives no rule)* |
| M7 | Xuel heritage "at least half" bypasses the Area 24 runes and the Area 25 guardian | Unchanged as a fiction test. In FG, a note on the door and on the vessels |
| M8 | Robes of Raanet's faithful (Area 6) bypass the Historium traps (Areas 4–5) | Unchanged. In FG, an item record: *Robe of Raanet's Faithful (mundane)*, two in Area 6 |
| M9 | Overland trip from the Freehold: **5% per day lost**, encounters checked **3×/day at 1 in 12**, encounter distance 6d4" (p. 4) | 5% per day lost (DC 10 Wisdom (Survival) to retrace with the map). Encounters 3×/day on a d12 roll of 1. Distance **6d4 × 10 yards** |

### 2.1 · The Summoning Sigil (the module's spine)

| Question | Module says | 5e ruling |
|---|---|---|
| How many rods? | **Chapter One: four** (p. 7). **Appendix A: five** (p. 37) | 🔒 **Four** (decided 2026-11-08). Appendix A's "five" is a module error. The four are placed in **A13** (charged, in the strongbox), **A15** (charged), **A22** (charged) and **A33** (quiescent) |
| How is a rod charged? | Chapter One: *"exposure to a fire capable of inflicting 8HD or more damage, or steeping it within the substance of a fire-based creature of 8HD or more"* (p. 7). Appendix A: touching it to an elemental-fire creature of 8HD+ **destroys that creature, no save** (p. 37) | **Two routes. Choose in D1.** **(a) Creature route:** touch the quiescent rod to an eligible creature. It is a melee attack using the rod as an improvised weapon (proficiency applies if the wielder is proficient with simple weapons). On a hit, the creature is **destroyed, no save**, and the rod is charged. Eligible creatures in this module: **Keeper-of-the-Hearth, Ranzaar, Yox, Ixthasus**, 🔒 **but not the salamanders** (D1a): they are 1e 7+7 HD, short of 8, and Appendix A's own examples name the *greater* salamander, not the ordinary one. **(b) Fire route:** 🔒 the rod is charged by **a single instance of fire damage rolled with 10 or more dice** (decided 2026-11-08). A 3rd-level *fireball* (8d6) doesn't qualify, and neither does the A22 wand. It takes *fireball* cast at 5th level or higher, *incendiary cloud* (10d8), Ixthasus's Magma Spray (10d8) or Avraasha's 12d6 fireball |
| Assembly | Rods fuse when touched end to end (pp. 7, 37) | Unchanged. No check |
| Activation | Place the assembled Sigil on the Area 34 pedestal (p. 30) | Unchanged. Opens Chapter Two |
| Durability | "As difficult to damage as an artifact" | Immune to all damage except the *Destroying the Sigil* clause, which the module doesn't give. Treat it as an artifact |
| Yox can charge it | p. 29 | Yes. Yox is eligible |

---

## 3 · Room-by-room conversion

> [!note] Reading the table
> **Module-keyed** facts are the module's own, converted. *(Conversion call)* marks a rule I had to supply because the 1e text gives none. **⚠️** marks a module error or contradiction.

### Chapter One — The Temple Incandescent

| Area | Content | 5e conversion |
|---|---|---|
| **1** Slender Stairway (p. 8) | 100 ft descent at about 45°. Old traps and alarms have faded | No mechanics. Passive Perception 12+ notices *"hot, stale smoke drifting up"* |
| **2** Foyer (p. 9) | Names of every resident, in Ancient Xuloise | Treasure: **inscription record, 500 gp to a sage** (it has to be copied, so it is not an FG item; put it in a parcel note) |
| **3** Welcome Hearth (p. 10) | **Keeper-of-the-Hearth**, small fire elemental, insane, attacks on entry | **MM Fire Elemental (CR 5)** with *Maddened*: Touch **+4** instead of +6 (1e THAC0 14 "reduced by insanity" against a normal 12). **Sigil-eligible.** Treasure: wall lyrics **2,500 gp** to a sage (copied); **iron star-barrier, 1,000 gp, 200 lb**, rolls into a 2-ft cylinder. The room's acoustics are enchanted (flavour) |
| **4** Historium West (p. 10) | Walking into an alcove without a robe (or an escort wearing one) raises a **wall of stone (12th level)** that seals the short hall and wakes that alcove's **Caryatid Column**. History book with the "First Servant lost" passage | **Trap:** magic, triggered by entering an alcove. *Detect magic* shows evocation. Spotting the glyph line: **DC 16 Intelligence (Investigation)**. **Wall of stone as the spell, but permanent.** A creature in its path makes a **DC 16 Dexterity save** to choose which side it ends on (on a failure the trap chooses). Dispel **DC 16**. Each panel: AC 15, 180 HP (6 in thick). **One caryatid per triggered alcove**, so normally one at a time. Book: player handout **H1** (verbatim passage, p. 11) |
| **5** Historium East (p. 11) | Twin of Area 4. **Mariana il-Xanna's diary**, with the Sigil passage and a blood smear | Same trap and caryatids. Diary is worth **15,000 gp** (sellable). Diary excerpt is player handout **H2**. ⚠️ The module calls Mariana both **"she"** (p. 7) and **"His personal account"** (p. 11). **Use she** |
| **6** A Watcher, Long Gone (p. 12) | Ash circle (a self-immolation). **Robes of the faithful** on a bench | Robes: two sets, the black-and-red toga. **Wearing one bypasses the Area 4/5 trap and the caryatids** |
| **7** Echoes (p. 13) | A cold, non-evil spirit. *Speak with dead* is resisted | No mechanics. *Divine Sense* or *detect evil and good* register **nothing** (it is not undead), but a cleric or paladin feels it anyway. Narrative only |
| **8** Office of the Castellan (p. 13) | Poisoned skeleton. **Iron key** dispels the illusion on the A9 secret door and disarms its trap. Ten Xuel coins (50 gp each to a collector). **Breastplate (as elfin chain +2), raptor helm (see invisible 3/day, 3"), short sword of sharpness** | Secret door: illusory wall; **DC 16 Investigation** to see through it without the key. Coins: **10 × Xuel gold coin (50 gp collector value)**, tracked as an item. Gear: see §5 items **I1–I3** |
| **9** The Oubliette (p. 14) | **Trapped door: negative energy, 3d8+3** to all within 10 ft unless opened with the key. 40-ft pit. **2 wraiths** rise through the shadows and fight on the pit's edge | **Trap (Dangerous):** **22 (4d8 + 4) necrotic** to each creature within 10 ft, **DC 15 Constitution save for half** (🔒 D6: the module gives no save, but this one is shaped like a 5e trap, so it gets one). Detect: **DC 15 Investigation**, or *detect magic* (necromancy). Disarm: the key, or *dispel magic* (DC 15). **2 × MM Wraith (CR 5).** Skip their *Create Specter* (not in 1e). **Pit edge:** a creature shoved or knocked prone within 5 ft of the edge makes a **DC 13 Dexterity save** or falls 40 ft (4d6). Treasure at the bottom: **27 Xuel coins** (bags of 15 and 12), **cursed silver dagger −1** (I4) |
| **10** Brothers' Suites (p. 14) | **5 magmen.** Combat noise brings A11. **Bracers of defense AC5, ring of protection +2**, gold slag 250 gp | **5 × Magman (CR 1)** (§4.2). Noise rule kept: full combat here **automatically** draws A11's magmen at the start of round 3 *(conversion call on timing)*. Treasure: **bracers of defense** (5e DMG), **ring of protection** (5e +1; see D4), **gold slag 250 gp** |
| **11** Sisters' Suites (p. 15) | **4 magmen.** Noise brings A10. **Lyre of building** (three strings broken). Slag here is worthless | **4 × Magman.** ✅ **Treasure split confirmed against the p. 15 page image** (the PDF's text layer runs the two rooms together): **A10 has the bracers, the ring and the 250 gp slag; A11 has only the lyre**, and its slag is worthless. Lyre: §5 **I7**. Restringing it is a DC 15 check with a musical instrument or tinker's tools, or 50 gp at a luthier *(conversion call)* |
| **12** The Retreat (p. 15) | **Small air elemental**, insane. Won't pursue. If the party hasn't met it within a day, it escapes up the stairs | **MM Air Elemental (CR 5)** with *Maddened* (Slam **+6** instead of +8). Escape rule kept. No treasure |
| **13** Office of the Bellows (p. 16) | **4 harginn grues.** Footman's flail +2. **Strongbox: locked, with an acid-gas trap** (3d4 then 1d4 for 3 rounds, save half on the first burst, douse to stop). Inside: 250 Xuel coins, 5 small rubies (100 gp), **wand of ice storms (10 charges)** at double value, **ring of warmth**, **Sigil rod (charged)** | **4 × Harginn Grue (CR 2)** (§4.2). **Lock:** DC 15 thieves' tools. **Trap (Setback):** fills a 10-ft cube, **10 (3d6) acid, DC 13 Constitution save for half**, then **5 (2d4) acid at the start of each of the target's next 3 turns** (no save). An action spent dousing with water or wine ends it. Detect and disarm **DC 15**. Treasure: **flail +2**, **250 Xuel coins**, **5 × small ruby (100 gp)**, **wand of ice storms** (I8), **ring of warmth** (DMG), **Sigil rod #1 (charged)** |
| **14** Night Gallery (p. 17) | **9 portraits by Karvik il-Xon, 2,000–5,000 gp each.** The last is Leathri il-Varzii, Child of Fire | ✅ **"Child of Fire" is a title, not a name** (D7). The gallery shows nine portraits, *"each … a leader in the faith of Raanet"*, and at least three different people hold the title in the text: the **man** who built the Oubliette (*"the Child of Fire … He called this place The Oubliette"*, A8), **Kaara ad-Karza** (A15), and **Leathri il-Varzii**, *"the Child of Fire … at the time of the Temple's collapse"* (A14, the last portrait). **Reading:** Kaara held the title while Mariana was alive (she holds a charged rod and M.'s letter), immolated herself with Ranzaar, and **Leathri succeeded her** and was the last. Leathri's body and room are unkeyed. Treasure: **9 portraits**. Roll **(1d4 + 1) × 1,000 gp** each, or fix the values at 3,500 gp each (31,500 gp total) for FG |
| **15** Abode of the Child of Fire (p. 17) | **Ranzaar**, small fire elemental. Unlocked footlocker: 2,500 Xuel gold pieces, potion of extra-healing, potion of levitation, cloak of protection +2, gauntlets of ogre power, robe of scintillating colors, *Warmed by the Flame* (2,500 gp), M.'s letter, **Sigil rod (charged)** | **MM Fire Elemental (CR 5).** ⚠️ The statline says THAC0 12 *"(reduced by insanity)"*, but 12 is a normal 8 HD THAC0, so nothing is reduced. **Use the MM +6.** Sigil-eligible. Treasure: 🔒 **240 Xuel gold coins at the standard 50 gp collector rate = 12,000 gp** (D8; the module's literal "2,500" would be 125,000 gp). Then **potion of greater healing**, **potion of levitation** (custom, I9), **cloak of protection** (5e +1; D4), **gauntlets of ogre power**, **robe of scintillating colors**, *Warmed by the Flame* (2,500 gp), **M.'s letter** (player handout **H3**; ⚠️ it misspells **"Azraasha"** and may be kept as in-world), **Sigil rod #2 (charged)** |
| **16** The Nest (p. 19) | **12 fire bats** around a hot tar nest. Carnelian 50 gp, jacinth 250 gp | **12 × Fire Bat (CR 1/4)** (§4.2). The nest is flavour; touching it deals 3 (1d6) fire *(conversion call)*. Treasure: **carnelian (50 gp)** and **jacinth (250 gp)**, kept at the module's values, not the DMG gem table's |
| **17** Pantry (p. 19) | Stone slab carries permanent chill, flavor, freshen and preserve cantrips. Silver plate 100 gp, **2 casks of Xuel wine (2,500 gp each)**, **decanter of endless water** | The slab is a permanent *prestidigitation* (chill, flavour and clean food only). Treasure: **platters and cutlery (100 gp)**, **2 × cask of Xuel wine (2,500 gp; about 250 lb each, *conversion call*)**, **decanter of endless water** (DMG) |
| **18** Road to Perdition (p. 19) | *Audible glamer* footsteps and a *spectral force* door, the image also faking a cool temperature. Entering the last 20 ft drops a **wall of stone 50 ft from the end** and opens a **10-ft pit with a permanent wall of fire: 1d6 fall + 2d6+12 fire per round, no save** | Illusions: *minor illusion* (sound) and permanent *major image* (door, with temperature). **DC 16 Investigation** to see through either. **Trap (Deadly):** trigger is the last 20 ft. The wall of stone seals the 50-ft stretch behind (DC 16 Dex to end up on the outside). The floor drops: **3 (1d6) bludgeoning** for the 10-ft fall, then **22 (5d8) fire** on entering the pit and at the start of each turn there, **no save** (1e; D6). Climbing out: DC 12 Athletics. **5d8 is the 5e *wall of fire* value.** Detect: **DC 18 Investigation**; the illusion hides the heat, but DC 13 for anyone who has already seen through the *major image*. Disarm: *dispel magic* DC 16 on the wall of fire |
| **19** Where We Consume (p. 20) | **3 phantom stalkers** bound to ad-Dax's golden medallion. **Destroying the medallion (5 hp) kills all three** | **3 × Phantom Stalker (CR 3)** (§4.2). **Medallion:** Tiny object, **AC 15, 5 HP**, in the ash where the table stood. Visible as a glint; DC 10 Perception to pinpoint while fighting. **Destroying it kills all three stalkers instantly.** No other treasure |
| **20** Kitchen (p. 20) | **Dust of disappearance (5 applications)** in a spice jar. The jar is a **bag of holding (500 lb)**. A **ring of protection +2** sits invisible in it | **Dust of disappearance** (DMG; one packet). The module's 5 applications become **5 uses** (D4). **ad-Dax's Glass Jar:** *bag of holding* reskin (500 lb, 64 cu ft; identical rules) (I10). **Ring of protection** (5e +1; D4). The jar bears ad-Dax's rune: DC 13 Investigation |
| **21** The Burning Sentinel (p. 21) | **Ixthasus, greater salamander.** Lava floor; Con −2 until 5 rounds in cool air; **1d6 fire per round** without fire resistance. Violent fights here have a **50% chance** of alerting A22, and then **half the salamanders** come. Gem cache of 22 | **Ixthasus (CR 10)** (§4.2). **Room hazard:** a creature without fire resistance or immunity takes **3 (1d6) fire** at the start of each of its turns in the room *(1e die kept; D6)*, and has **disadvantage on Constitution saving throws, including concentration**, until it spends **5 minutes** out of the room (1e −2 Con, 5 rounds = 5 minutes). Fire resistance negates both. **Alarm:** at the end of each round of combat, roll d100; on 01–50 *(once only)*, **2 salamanders** arrive the next round (half of four). Gems: **6 × 50 gp, 4 × 75 gp, 3 × 100 gp, 5 × 500 gp, 3 × 1,000 gp, 1 × 5,000 gp fist-sized ruby = 11,400 gp** |
| **22** The Conflagration (p. 22) | Permanent *hallucinatory terrain* and *spectral force* make a sea of fire. **1d6 per round to anyone who doesn't disbelieve.** Salamanders: the text says **four**, the statline says **(5)** (resolved below). They **avoid the desk and bookcases**. Treasure: **wand of fire (5 charges)**, scroll (comprehend languages, contact other plane, monster summoning IV, slow, wall of stone), **dagger +2**, **hat of disguise** (black hair ribbon), fire tomes 2,500 gp, **Sigil rod (charged)** | **Illusion:** permanent *hallucinatory terrain* plus *major image*. Seeing through it takes **an action and DC 16 Intelligence (Investigation)**. Until then the creature takes **3 (1d6) psychic** at the start of each turn *(1e die kept; it is the illusion damage of 5e* phantasmal force*)*. 🔒 **Four salamanders** (D2). Four is closer to the 5e Deadly threshold: at the recommended 6 × level 6 (Deadly 8,400), four come to 14,400 adjusted (171%) and five to 18,000 (214%). **MM Salamander (CR 5).** If Ixthasus's alarm pulled two of them into A21, only two remain here. The module's spear-and-tail statline is the MM salamander almost exactly. **Safe zone:** salamanders will not move within 5 ft of the desk or bookcases and **won't make attacks that would hit them** *(conversion call: no fire breath at the shelves)*. Treasure: **alabaster wand of fire** (I11), **5 spell scrolls**, including *monster summoning IV* (see §5.3), **dagger +2**, **hat of disguise**, **fire tomes (2,500 gp)**, **Sigil rod #3 (charged)** |
| **23** Incinerator (p. 23) | Waste pit, equal to a wall of fire. **5 magmen** climb out if anyone comes within 20 ft | Falling in: 7 (2d6) for 20 ft *(depth not given; conversion call)* plus **22 (5d8) fire** on entering and at the start of each turn, no save. **5 × Magman.** No treasure |
| **24** Heart of Fire (p. 23) | Raanet mosaic; prophecy walls (500 gp if copied). **North door: explosive runes, 6d4+6, no save, unless at least half Xuel** | **Trap (Dangerous):** *glyph of warding* (explosive runes, fire), **22 (5d8) fire** to the opener, **DC 15 Dexterity save for half** (🔒 D6: the module gives no save; *glyph of warding* always has one). Detect: **DC 15 Investigation** or *detect magic* (abjuration). Disarm: *dispel magic* DC 15, or have a half-Xuel character open it |
| **25** In Memoriam (p. 24) | Ten urns, **a–j**. Touching any urn without Xuel heritage animates a **stone guardian** from the floor mosaic. Contents per letter | **Stone Guardian (CR 3)** (§4.2). It forms in 1 round, attacks until everyone is dead or has left, and won't leave the room *(conversion call, consistent with the 1e text)*. **a** **ring of human influence** (I12), plus a **hidden switch** that opens A26: **DC 15 Wisdom (Perception)**. **b** plumb line (mundane). **c** **stone of good luck** if carried by a worshipper of the Xuel pantheon, otherwise a **stone of weight** (I13), plus a secret door to A27/29 (**DC 15 Perception**, unlocked). **d** miniature spyglass (mundane; *conversion call: 25 gp curio*). **e** gold piece and lead piece, plus a secret door to A28 (DC 15, unlocked; **A28 is a magma room**, see there). **f** **2 golden wedding rings, 100 gp each**. **g** **miniature sword → "broadsword +2" for a Fighter** (I14), plus a secret door to A33: **trap (Dangerous), 22 (4d10) lightning, DC 15 Dexterity save for half**; detect and disarm DC 15. **h** holy symbol that acts as **ring of protection +2, stacking, for a devotee of Raanet** (I15). **i** golden needle (1 gp). **j** iron link, plus a **locked, untrapped** secret door to **A26**. Lock DC 15. The **looting-consequences** note for good characters stays at DM discretion |
| **26** Crematorium (p. 25) | Opening the door starts the vacuum. Hold on with **double bend bars %** or be pulled in. **10d6 per round, no save.** Off switch in the opposite alcove | **Trap (Deadly):** when the door opens, each creature within 30 ft of it makes a **DC 18 Strength saving throw** at the start of each of its turns. On a failure it is pulled 15 ft toward the room; inside, it takes **35 (10d6) fire** at the start of each turn, **no save** (1e). *(DC 18: a 1e Str 16–18 character succeeds 14–32% of the time; DC 18 with a +3 to +5 Strength save gives 30–40%.)* The switch in the opposite alcove takes an action to reach and use. Leaving the room takes a DC 18 Athletics check per 5 ft |
| **27** Empty Vessels (p. 26) | Urns, pigments. **Marvelous pigments (3 applications)** in a pot marked "A" | **Nolzur's Marvelous Pigments** (DMG) with **3 uses** (5e: 1d4 pots) |
| **28** Playing with Fire (p. 26) | **4 magmen** in a magma floor. Falling in: **10d10 per round, save vs breath for half**, then **3d6 until scraped off** | **4 × Magman.** **Magma (DMG):** **55 (10d10) fire** on entering and at the start of each turn in it, **DC 15 Dexterity save for half** (1e save kept). On leaving, **10 (3d6) fire** at the start of each turn until someone spends an action scraping it off. Arriving through the A25e secret door while fleeing: **DC 13 Dexterity save** or stumble in *(conversion call; the 1e text says "a good chance")* |
| **29** Prayers for Flame (p. 27) | Cold fire pit. **Ring of fire resistance** | **Ring of resistance (fire)** (DMG). Finding it in the ashes: **DC 10 Investigation** *(conversion call)* |
| **30** Creatio Ex Nihilo (p. 27) | **5 wights**, cannibal survivors, around the **Bountiful Cornucopia** | **5 × MM Wight (CR 3)**, re-armed: **no longbow; claw attacks** (**+4, 1d6+2 slashing**) in place of the longsword. *Life Drain* kept. CR unchanged. Treasure: **Bountiful Cornucopia** (I16) |
| **31** Various & Sundry (p. 28) | Xar'bik skins hold **yellow mold. 75% chance they burst** if disturbed (10-ft radius). Tools 100 gp | **Yellow Mold (DMG hazard):** if the bundles are disturbed, roll d4; on 1–3 they burst. Each creature within **10 ft** makes a **DC 15 Constitution save**: on a failure, **11 (2d10) poison** and poisoned for 1 minute, taking 5 (1d10) poison at the start of each of its turns while poisoned and repeating the save at the end of each turn to end it. Fire or sunlight destroys the mold. Treasure: **tools (100 gp)**. ⚠️ The text splits this room across A30's column. **Yellow mold is A31, not A30** |
| **32** The Fallen Champions (p. 28) | **Naskin and Yrsi ad-Laar, swordwraiths.** Warned, they tip the dresser over for cover (**AC −2**) and use bows. 25% chance combat rouses Yox. Treasure: **2 bastard swords +2** (Naskin), **chain shirt +1**, (Yrsi) **small shield +2**, all at double value; 120 Xuel coins, 3 flawed diamonds (25 gp), **2 adamantite rings (250 gp)** | **2 × Swordwraith (CR 5)** (§4.2). **Dresser = half cover (+2 AC).** **Yox alarm:** 25% per fight, rolled once. Treasure: **2 × longsword +2** (*Xuel bastard sword*; versatile; see I17), **chain shirt +1**, **shield +2**, **120 Xuel coins**, **3 × flawed diamond (25 gp)**, **2 × adamantite ring (250 gp)** |
| **33** Death's Companion (p. 29) | **Yox, efreeti.** Warned, it goes invisible, splits the party with a **wall of fire**, and kills casters first. **Surrenders below 50% HP** and offers the rod's location for an oath of release. Can charge the rod. Treasure: **footman's flail +2**, **brooch of shielding (77 charges)**, **Sigil rod (quiescent)** | **MM Efreeti (CR 11).** **Strip *conjure elemental* and *plane shift*** (plane shift is blocked by M1; conjure elemental is not in the 1e efreet and would work here). **Surrenders at 100 HP or less.** Sigil-eligible. Room: the flames on the floor are illusory flavour; the module gives no damage. Treasure: **flail +2**, **brooch of shielding** (DMG; it has no charges in 5e, so drop the 77), **Sigil rod #4 (quiescent)** |
| **34** The Precipice (p. 30) | Pedestal for the Sigil | Seat the Sigil here to start Chapter Two. No check |

### Chapter Two — The Burning Athenium

| Area | Content | 5e conversion |
|---|---|---|
| **M10** Athenium properties (p. 31) | Same anti-travel properties as the Temple. No wandering monsters | As M1 |
| **35** The Burning Athenium (p. 32) | **Avraasha**, mad. She asks who they are, then attacks: **power word stun first**, then fireballs, walls of fire and an incendiary cloud steered **with telekinesis**. She won't leave the central area | **Avraasha (CR 22)** (§4.2). 🔒 *Telekinesis* added to her list (D3), so the tactic works as written. Her **concentration** is the weak point: *telekinesis* and *incendiary cloud* both need it, so she can't hold one and steer the other. She uses the telekinesis to shove fleeing creatures back into the burning cloud |
| **35** "Surviving the Fire" (p. 33) | **10% base** to calm her by appeal. **+15%** if Xuel are present, **+10%** for using her name, **+10%** for invoking Raanet, **+10%** for quoting scripture, **+5% per point of Charisma above 15** | **Calming Avraasha.** As an action, a creature that can speak to her makes a **DC 22 Charisma (Persuasion)** check. **+3** if Xuel are among the party. **+2** each for using her name, invoking Raanet, and quoting Raanet scripture (learned from the Temple's writings: H1, the A24 prophecies, *Warmed by the Flame*). The Charisma modifier is already in the roll. **The math matches.** A Cha 18 speaker proficient in Persuasion (+7) with every bonus (+9) succeeds 75% of the time, against 70% in 1e. The same speaker with no bonuses succeeds 30%, against 25% in 1e. An untrained Cha 10 speaker with no bonuses can't succeed, against 10% in 1e; that is the one place 5e is harsher. One attempt per speaker per round, no penalty for failing (the 1e text gives none) |
| **35** Library rewards (p. 33) | 25,000 books, 500 tons. A Magic-User researching **fire** items or spells with the whole collection saves **50% of the cost and time**; **+1d20+5%** to devise an original fire spell. A **cleric or paladin of a Xuel deity** studying for a year gains **50,000 XP**; a **worshipper of Raanet** first rises to their next level, **then** gets the 50,000 | **Crafting:** half the time and gold cost for any magic item that deals fire damage or has a fire theme. **Spell research:** copying fire spells into a spellbook costs half; designing a new fire spell is at the DM's discretion, with advantage on related Arcana checks. **Study:** one year of study gives a cleric or paladin of a Suel/Xuel deity **one level**. A **worshipper of Raanet gains two** (1e: next level, plus 50,000 XP on top, which at 1e levels 5–8 is about one more) |
| **Epilogue** (p. 34) | Calmed, she weeps, **heals the party**, tells her tale, grants **each PC a *wish***, and promises to answer **if her name is spoken thrice** in their hour of need. Then she leaves | **Heal:** she casts *heal* on the party (🔒 D3: 3/day, added to her list; enough for six PCs over the scene if she uses *mass cure wounds*-style narration, or cast *heal* on the three worst-hurt and let the rest short-rest by her fire). **Wish:** each PC gains **one use of *wish*** that they speak aloud to her in the moment, or bank as a one-use item (*Avraasha's Ember*, I18). It is granted **by her**, so there is **no wish stress** (like a djinni's wish). **Thrice-spoken name:** once per PC, for the rest of the campaign, Avraasha answers. DM-side plot hook, not a mechanic |

---

## 4 · Monsters

### 4.1 · Using the MM (2014) statblock, with module riders

| Module creature | 1e line (page) | 5e statblock | Riders |
|---|---|---|---|
| Keeper-of-the-Hearth | Fire elemental (small), 8 HD, 44 hp, 3d8, +2 to hit (p. 10) | **Fire Elemental** (CR 5) | *Maddened*: Touch +4. Sigil-eligible |
| Ranzaar | Same (p. 18) | **Fire Elemental** (CR 5) | Touch +6 (see the A15 note). Sigil-eligible |
| Small air elemental | 8 HD, 44 hp, 2d10, whirlwind (p. 15) | **Air Elemental** (CR 5) | *Maddened*: Slam +6. Escapes after a day (A12) |
| Wraith ×2 | 5+3 HD, 1d6 + energy drain (p. 14) | **Wraith** (CR 5) | No *Create Specter* |
| Salamander ×4 (or 5) | 7+7 HD, spear 1d6 + tail 2d6, heat (p. 22) | **Salamander** (CR 5) | Safe zone (A22) |
| Wight ×5 | 4+3 HD, 1d4 + energy drain (p. 27) | **Wight** (CR 3) | Claws instead of sword and bow |
| Yox | Efreeti, 10 HD, 3d8 (p. 29) | **Efreeti** (CR 11) | No *conjure elemental* or *plane shift*. Surrenders at 100 HP. Sigil-eligible |
| Yellow mold | (p. 28) | **DMG hazard** | 75% burst → d4, 1–3 |

> [!tip] Why the MM elementals and not the 1e numbers
> The 1e "small" elemental (8 HD) is exactly what *conjure elemental* summons in both editions, and the MM fire elemental was built as that creature. Converting from the 1e 44 hp would create a *third* fire elemental that is weaker than the one players already know.

### 4.2 · Custom statblocks (no 5e equivalent)

Nine creatures need new blocks. They are presented as Obsidian callouts; FG Import Text blocks get generated from these after you approve them.

> [!example]- Magman — CR 1 (200 XP) · Area 10 ×5, 11 ×4, 23 ×5, 28 ×4, wandering 1d12
> *Small elemental, chaotic neutral*
> **Armor Class** 13 (natural armor) · **Hit Points** 26 (4d6 + 12) · **Speed** 25 ft., swim 15 ft. (lava and magma only)
>
> | STR | DEX | CON | INT | WIS | CHA |
> |---|---|---|---|---|---|
> | 14 (+2) | 12 (+1) | 16 (+3) | 6 (−2) | 10 (+0) | 6 (−2) |
>
> **Damage Resistances** bludgeoning, piercing, and slashing from nonmagical attacks
> **Damage Immunities** fire
> **Senses** darkvision 60 ft., passive Perception 10 · **Languages** understands Ignan but speaks no Prime language · **Challenge** 1 (200 XP) · **Proficiency Bonus** +2
>
> ***Melting Body.*** A nonmagical weapon, or a weapon with a +1 bonus, that hits the magman melts: after dealing damage it takes a permanent, cumulative −1 penalty to damage rolls, and it is destroyed when the penalty reaches −5. Nonmagical ammunition that hits is destroyed.
> ***Combustion.*** Flammable objects the magman touches that aren't being worn or carried catch fire.
> ***Bonfire Heat (MM2).*** It radiates heat like a small bonfire and sheds dim light for 10 ft.
> ***Lava-Bound (MM2).*** Out of lava for more than 6 hours, it stiffens and can't move until returned to it.
>
> **Actions**
> ***Combustion Touch.*** *Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* 13 (3d8) fire damage. A creature hit **catches fire** (MM2): it takes **4 (1d8) fire** at the start of each of its turns for **1d4 + 2 rounds**, or until it or a creature within reach spends an action to put the flames out. Flammable gear it carries burns too.
>
> **Conversion note.** 1e: AC 6, MV 9"/6", HD 2, 3d8 combustion touch, +1 weapons to hit, weapons under +2 melt. **The 3d8 carries straight across**, which is the right damage for CR 1–2. The low CR comes from defence: 26 HP with resistance.
> **✅ Checked against *Monster Manual II* (p. 82), 2026-11-15.** MM2: AC 6, MV 9" (6"), HD 2, combustion touch 3–24, **the victim burns for 1–8 a round for 3–6 rounds** (added), +1 or better weapon to hit, immune to fire, **any weapon below +2 that touches one melts** (🔒 kept as the gentler cumulative −1 rule, 2026-11-15), **size S (3')** (fixed; it was Medium), low intelligence, CN, no Prime languages. MM2 magmen are mischievous rather than murderous: they **run when hurt** unless cornered. **C12 overrides that**: six centuries trapped, they fight to the death (p. 14). With the burning added, its damage per round sits near CR 2, but its low defence keeps it at **CR 1**.

> [!example]- Caryatid Column — CR 2 (450 XP) · Areas 4–5, one per alcove (four total)
> *Medium construct, unaligned*
> **Armor Class** 14 (natural armor) · **Hit Points** 33 (6d8 + 6) · **Speed** 15 ft.
>
> | STR | DEX | CON | INT | WIS | CHA |
> |---|---|---|---|---|---|
> | 16 (+3) | 10 (+0) | 13 (+1) | 3 (−4) | 10 (+0) | 1 (−5) |
>
> **Damage Resistances** bludgeoning, piercing, and slashing from nonmagical attacks
> **Damage Immunities** poison, psychic
> **Condition Immunities** charmed, exhaustion, frightened, paralyzed, petrified, poisoned
> **Senses** darkvision 60 ft., passive Perception 10 · **Languages** understands Ancient Suloise but can't speak · **Challenge** 2 (450 XP) · **Proficiency Bonus** +2
>
> ***False Appearance.*** While motionless, it is indistinguishable from a marble statue.
> ***Dampening Stone.*** A magic weapon that hits the column deals its normal damage dice, but its bonus to attack and damage rolls doesn't apply.
> ***Weapon Breaker (FF).*** When a weapon hits the column, roll a d20. It snaps on **1–5 if nonmagical, 1–4 if +1, 1–3 if +2, 1–2 if +3, or a 1 if +4**. A magic weapon with no bonus counts as +1; artifacts never break.
> ***Robe-Bound.*** The column does not attack a creature wearing the robes of Raanet's faithful, or a creature accompanied by one.
> ***Warded Stone (FF: all saving throws at +4).*** The column adds +4 to every saving throw.
> ***Task-Bound (FF).*** It acts only to carry out its guarding task. It won't pursue beyond its alcove and hall. When its task ends (intruders dead or gone), it returns to its place and reverts to stone, and so does its sword. If destroyed, it turns back to stone.
>
> **Actions**
> ***Concealed Sword.*** *Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 9 (1d8 + 5) slashing damage.
>
> **Conversion note.** 1e: AC 5, MV 6", HD 5, 2d4+2, normal weapons do half damage, magic weapons do full but without their bonus, 25% weapon breakage. **The sword's +2 is built into +7/+5** ("equivalent of +2 weapons" that become useless when the column falls). 1e breakage applied to all weapons; 5e breaks nonmagical ones only (**D5**).
> **✅ Checked against the *Fiend Folio* (p. 18), 2026-11-15.** FF: AC 5, MV 6", **22 hit points (fixed)**, one sword attack for 2–8 striking as a 5 HD monster, **all saving throws at +4**, normal weapons do half damage, magic weapons full damage without their bonus. Height 7' as a pillar, shrinking to about 5½' as it animates and takes on the look of a fair young maiden. Created like a stone golem, by a 16th-level magic-user. **Weapon breakage in the FF:** *any* weapon, magical or not, that hits has a 25% chance to snap, **minus 5% per plus** (a +4 sword: 5%). A magic weapon with no plus counts as +1. 🔒 **Adopted** (D5, revised 2026-11-15). The module's 2d4+2 (the FF's 2–8 plus its sword's +2) is kept.

> [!example]- Harginn Grue — CR 2 (450 XP) · Area 13 ×4, wandering 1d2
> *Medium elemental (shapechanger), neutral evil*
> **Armor Class** 15 (natural armor) · **Hit Points** 39 (6d8 + 12) · **Speed** 50 ft.
>
> | STR | DEX | CON | INT | WIS | CHA |
> |---|---|---|---|---|---|
> | 16 (+3) | 16 (+3) | 14 (+2) | 12 (+1) | 12 (+1) | 8 (−1) |
>
> **Damage Resistances** bludgeoning, piercing, and slashing from nonmagical attacks
> **Damage Immunities** fire
> **Senses** darkvision 60 ft., passive Perception 11 · **Languages** Ignan · **Challenge** 2 (450 XP) · **Proficiency Bonus** +2
>
> ***Flame Eater (MM2).*** The grue is immune to spells that deal fire damage. **Any fire spell or magical fire effect within 20 ft of the grue is dispelled, even a permanent one** (such as *wall of fire*, *flaming sphere* or a fire trap). A spell cast with the grue in its area or as its target simply fails. **Fire from magic items is unaffected** (MM2).
> ***Shapechanger (MM2).*** As an action, it takes the form of a bonfire, an 8-ft column of fire, a flame-legged humanoid (its true form) or a bronze statue. While motionless as a bonfire or statue, it is indistinguishable from the real thing.
> ***Blinking.*** The grue flickers in and out of sight. Attack rolls against it have disadvantage unless it is incapacitated. (It doesn't move, so the Temple's marble doesn't stop it.)
>
> **Actions**
> ***Gout of Flame (MM2).*** A gout of fire from its fingertips fills a **5-ft-wide, 10-ft line**. Each creature in it makes a **DC 13 Dexterity save**, taking **10 (2d6 + 3) fire** on a failure or half as much on a success.
>
> **Conversion note.** 1e (via 2e grue): AC 3, MV 15", HD 4+4, 1d4+4, +1 weapons to hit, dispels fire spells, blinking. **Flame Eater is the danger to plan around:** a caster who opens with *fireball* loses the spell entirely.
> **✅ Checked against *Monster Manual II* (p. 73), 2026-11-15.** The harginn ("flame horror") is an MM2 elemental grue: AC 3, MV 15", HD 4+4, **one attack of 5–8 that is a gout of flame filling an area 3 ft wide and 6 ft long** (rebuilt as a line attack; it was a single-target claw), +1 or better weapon to hit, immune to fire-based spells, and **its presence within 20 ft dispels fire magic, even permanent effects; magic items are unaffected** (Flame Eater widened to match). Shapes: bonfire, column of fire, humanoid, bronze statue (added). **Average to high intelligence** (Int fixed from 6 to 12). NE. ⚠️ **MM2's blink is the 1e *blink* spell, a short random teleport, which the Temple's marble would block (ledger M1).** The module's own statline still lists *Blinking* in the Temple, so the in-place flicker (disadvantage on attacks) is kept as the conversion of that. FG can't automate it; use a label-only effect: `Flame Eater - fire spells touching me are dispelled`.

> [!example]- Fire Bat — CR 1/4 (50 XP) · Area 16 ×12, wandering 1d6
> *Small elemental, neutral evil*
> **Armor Class** 12 · **Hit Points** 11 (2d6 + 4) · **Speed** 5 ft., fly 60 ft.
>
> | STR | DEX | CON | INT | WIS | CHA |
> |---|---|---|---|---|---|
> | 6 (−2) | 15 (+2) | 14 (+2) | 6 (−2) | 12 (+1) | 6 (−2) |
>
> **Damage Immunities** fire
> **Senses** blindsight 60 ft. (sees invisible creatures), darkvision 60 ft., passive Perception 11 · **Languages** — · **Challenge** 1/4 (50 XP) · **Proficiency Bonus** +2
>
> ***Flyby.*** The bat doesn't provoke opportunity attacks when it flies out of an enemy's reach.
> ***Echolocation.*** The bat can't use its blindsight while deafened.
> ***Pack Hunters (MM2).*** The colony spreads its attacks evenly across a group. When fewer than a quarter of the starting bats remain, the rest flee to their lair; cornered there, they fight to the death.
> ***Doused (MM2).*** At least 10 gallons of cool water on one bat (*create or destroy water* is enough) puts it out for 10 rounds: it can't fly, and its bite deals only 2 (1d4) fire.
> ***Return to Fire.*** When it dies, it bursts into flame and its body vanishes back to the Elemental Plane of Fire.
>
> **Actions**
> ***Burning Bite.*** *Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* 5 (2d4) fire damage, and the bat **attaches** (MM2). While attached it doesn't attack; instead, at the start of each of its turns, the target **automatically takes 5 (2d4) fire** from burning and blood loss. After two such turns (three rounds of damage in all) it drops off, sated, and flies home. A creature can pull it off with an action and a DC 12 Strength check.
>
> **Conversion note.** 1e: AC 8, MV 6"/20", HD 2, 2d4, immune to fire. The 2d4 carries straight across.
> **✅ Checked against *Monster Manual II* (p. 16), 2026-11-15.** MM2: size **S** (2' body, wingspan nearly 4'; changed from Tiny), **semi-intelligent**, NE. It **attaches on a hit and burns automatically for three rounds in all, then drops off sated** (added). It sees invisible creatures by sonar and infravision, isn't harmed by sunlight, flees as a colony below 25% strength, is doused by 10 gallons of cool water, and is allied to fire elementals (it never attacks one). Lair treasure is gems, especially rubies, jacinths and carnelians, which fits Area 16's carnelian and jacinth. Each bat's damage over three rounds is now about 15, so it sits at the top of **CR 1/4**.

> [!example]- Phantom Stalker — CR 3 (700 XP) · Area 19 ×3, wandering 1d2
> *Large elemental, neutral evil (FF: neutral; the module's are maddened)*
> **Armor Class** 16 (natural armor) · **Hit Points** 52 (7d10 + 14) · **Speed** 30 ft., fly 60 ft.
>
> | STR | DEX | CON | INT | WIS | CHA |
> |---|---|---|---|---|---|
> | 18 (+4) | 14 (+2) | 15 (+2) | 8 (−1) | 12 (+1) | 8 (−1) |
>
> **Damage Vulnerabilities** cold
> **Damage Immunities** fire, poison
> **Condition Immunities** exhaustion, poisoned
> **Senses** darkvision 60 ft., passive Perception 11 · **Languages** Ignan, understands Ancient Suloise · **Challenge** 3 (700 XP) · **Proficiency Bonus** +2
>
> ***Fire Absorption.*** Whenever the stalker would take fire damage, it takes none and instead regains 1 hit point per damage die.
> ***Shapechanger.*** As an action, the stalker polymorphs into a Large or smaller beast or humanoid, or back into its true form. Its statistics don't change. It reverts on death.
> ***Medallion-Bound.*** If ad-Dax's medallion is destroyed, the stalker dies instantly.
> ***Bound Bodyguard (FF).*** A phantom stalker serves its summoner and obeys orders to the letter. If its summoner is slain, it vanishes, returns 1d4 hours later and hunts the slayer through the Ethereal Plane. ad-Dax died of age, so in C12 this is grief, not vengeance (module text).
> ***Unseen Vigil.*** As an action, the stalker becomes invisible until it attacks or uses Self-Immolation.
>
> **Actions**
> ***Multiattack.*** The stalker makes two claw attacks.
> ***Claw.*** *Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 7 (1d6 + 4) slashing damage.
> ***Self-Immolation (FF: a last resort when its death is imminent).*** **Usable only when the stalker has 15 hit points or fewer.** The stalker explodes and dies. Each creature within 20 feet of it makes a DC 13 Dexterity saving throw, taking 28 (8d6) fire damage on a failure or half as much on a success. Other phantom stalkers in the area regain 8 hit points (Fire Absorption).
>
> **Conversion note.** 1e: AC 3, MV 12"/24", HD 6, 1d4/1d4, detonates as a 6 HD fireball, heals 1 hp per die of fire damage, polymorph, vulnerable to cold. **The 1e 6-dice fireball becomes the 5e 8d6 fireball**, the same conversion WotC made for the spell. ⚠️ **Unseen Vigil comes from the module's prose** ("invisible guardians", p. 20), not from its statline (**D5**).
> **✅ Checked against the *Fiend Folio* (p. 72), 2026-11-15.** FF: AC 3, MV 12"/24" (it can fly in any shape), HD 6, claws 1–4/1–4, **impervious to fire, and magical fire heals it 1 hp per die**, saves against cold at −2 and takes +1 per die from cold (→ vulnerability), polymorph self (usually a reddish 8' humanoid with fiery eyes), size variable (usually L), semi-intelligent, **neutral**. It explodes as a 6-dice fireball **only as a last resort when its death is imminent**, and never if the blast would harm its summoner. **Two changes made:** Self-Immolation is now limited to 15 HP or fewer, and the FF's summoner-vengeance rule is added. **The FF gives phantom stalkers no invisibility.** *Unseen Vigil* comes only from the module's "invisible guardians" line, and 🔒 **it is kept for C12's stalkers** (D5, reconfirmed 2026-11-15).

> [!example]- Stone Guardian — CR 3 (700 XP) · Area 25
> *Medium construct, unaligned*
> **Armor Class** 17 (natural armor) · **Hit Points** 45 (6d8 + 18) · **Speed** 25 ft.
>
> | STR | DEX | CON | INT | WIS | CHA |
> |---|---|---|---|---|---|
> | 18 (+4) | 8 (−1) | 16 (+3) | 3 (−4) | 10 (+0) | 1 (−5) |
>
> **Damage Resistances** piercing and slashing; cold, fire, and lightning damage from spells
> **Damage Immunities** poison, psychic; damage from nonmagical ranged weapon attacks
> **Condition Immunities** charmed, exhaustion, frightened, paralyzed, petrified, poisoned
> **Senses** darkvision 60 ft., *see invisibility* (always active; module, and MM2 when built with *detect invisibility*), passive Perception 10 · **Languages** — · **Challenge** 3 (700 XP) · **Proficiency Bonus** +2
>
> ***Mosaic Body.*** The guardian forms from the floor mosaic in 1 round when its trigger is met. It won't leave the room.
> ***Mindless (MM2).*** It never makes Intelligence, Wisdom or Charisma saving throws against charm, fear, hold or paralysis effects; they simply fail.
> ***Stone Vulnerability (MM2).*** *Stone to flesh* (or *flesh to stone* reversed), *transmute rock* (to mud), *stone shape*, and any spell that digs through stone **destroy it instantly**.
> ***Fails to Heed (MM2: 20%).*** When it first animates, roll a d10. On a 1–2 it ignores its instructions and attacks every creature in sight, Xuel or not.
>
> **Actions**
> ***Multiattack.*** The guardian makes two fist attacks.
> ***Fist.*** *Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 8 (1d8 + 4) bludgeoning damage.
>
> **Conversion note.** 1e: AC 2, MV 10", HD 4+4, 1d8+1 ×2, **¼ damage from edged weapons**, immune to normal missiles, many spell immunities, sees invisible. **¼ damage becomes resistance**; 5e has no quarter step.
> **✅ Checked against *Monster Manual II* (p. 115), 2026-11-15.** MM2: AC 2, MV 10", HD 4+4, fists 2–9/2–9 (= 1d8+1, matches), **¼ damage from edged weapons**, normal missiles can't harm it, **half damage from cold, fire and electrical spells** (added; replaces the invented *Spell Warding*), can't be poisoned, held, charmed, paralysed or frightened, attacks until destroyed, **killed instantly by stone to flesh, transmute rock to mud, stone shape or dig** (added), and a **20% chance on activation of disobeying and attacking anything** (added). Size 75% M / 25% L. It is built from mud with a heart of stone, using *enchant an item*, *transmute mud to rock*, *magic mouth*, *detect invisibility* and *limited wish*. A special **ring of protection from stone guardians** makes its wearer and everyone within 10 ft immune to its attacks; none is placed in C12. CR stays **3**.

> [!example]- Swordwraith (Naskin and Yrsi ad-Laar) — CR 5 (1,800 XP) each · Area 32
> *Medium undead, lawful evil*
> **Armor Class** 18 (Naskin: chain shirt +1, shield) / 19 (Yrsi: chain shirt, shield +2) · **Hit Points** 78 (12d8 + 24) · **Speed** 25 ft.
>
> | STR | DEX | CON | INT | WIS | CHA |
> |---|---|---|---|---|---|
> | 18 (+4) | 14 (+2) | 15 (+2) | 10 (+0) | 12 (+1) | 14 (+2) |
>
> **Saving Throws** Str +7, Con +5
> **Skills** Athletics +7, Perception +4
> **Damage Resistances** necrotic; bludgeoning, piercing, and slashing from magic weapons with less than a +2 bonus
> **Damage Immunities** poison; bludgeoning, piercing, and slashing from nonmagical attacks
> **Condition Immunities** exhaustion, poisoned
> **Senses** darkvision 60 ft., passive Perception 14 · **Languages** Ancient Suloise · **Challenge** 5 (1,800 XP) · **Proficiency Bonus** +3
>
> ***Barricade.*** If warned, the swordwraiths tip the dresser for half cover (+2 AC) and use their bows.
>
> **Actions**
> ***Multiattack.*** The swordwraith makes two longsword attacks.
> ***Longsword +2.*** *Melee Weapon Attack:* +9 to hit, reach 5 ft., one target. *Hit:* 10 (1d8 + 6) slashing damage, and the target's Strength score is reduced by 1d4. The target dies if this reduces its Strength to 0. Otherwise the reduction lasts until it finishes a short or long rest.
> ***Longbow.*** *Ranged Weapon Attack:* +5 to hit, range 150/600 ft., one target. *Hit:* 6 (1d8 + 2) piercing damage.
>
> **Conversion note.** 1e: AC 3, MV 9", HD 7, **3/2 attacks**, 1d10, Strength drain, **+2 or better to hit**. 3/2 becomes two attacks. **The +2 gate is load-bearing:** at 5e level 6–7 a party with only +1 weapons does half damage. **The swords, shirt and shield are the room's treasure**, so the AC and to-hit come straight from their gear.

> [!example]- Ixthasus, Greater Salamander — CR 10 (5,900 XP) · Area 21
> *Large elemental, chaotic evil*
> **Armor Class** 17 (natural armor) · **Hit Points** 136 (16d10 + 48) · **Speed** 30 ft.
>
> | STR | DEX | CON | INT | WIS | CHA |
> |---|---|---|---|---|---|
> | 20 (+5) | 14 (+2) | 17 (+3) | 16 (+3) | 12 (+1) | 14 (+2) |
>
> **Skills** Perception +5
> **Damage Vulnerabilities** cold
> **Damage Resistances** bludgeoning, piercing, and slashing from nonmagical attacks
> **Damage Immunities** fire
> **Condition Immunities** charmed, paralyzed; magic can't put it to sleep
> **Senses** darkvision 60 ft., passive Perception 15 · **Languages** Ignan, Common · **Challenge** 10 (5,900 XP) · **Proficiency Bonus** +4
>
> ***Heated Body.*** A creature that touches Ixthasus or hits it with a melee attack while within 5 feet of it takes 7 (2d6) fire damage.
> ***Lava Shaper.*** Ixthasus can turn stone it touches into lava at a rate of one 5-foot square per minute. (This is how it remade Area 21.)
>
> **Actions**
> ***Multiattack.*** Ixthasus makes one trident attack and one tail attack.
> ***Trident +3.*** *Melee Weapon Attack:* +12 to hit, reach 10 ft., one target. *Hit:* 15 (2d6 + 8) piercing damage plus 7 (2d6) fire damage.
> ***Tail.*** *Melee Weapon Attack:* +9 to hit, reach 10 ft., one target. *Hit:* 12 (2d6 + 5) bludgeoning damage plus 7 (2d6) fire damage, and the target is grappled (escape DC 15). Until the grapple ends, the target is restrained, Ixthasus can automatically hit it with its tail, and it can't make tail attacks against other targets.
> ***Magma Spray (Recharge 5–6).*** Ixthasus sprays lava in a 60-foot cone. Each creature in the cone makes a DC 15 Dexterity saving throw, taking 45 (10d8) fire damage on a failure or half as much on a success.
>
> **Conversion note.** 1e: AC 3/1, MV 12", HD 9+9, trident 1d6+4 (+3 weapon) + 1d6 heat, tail 4d4 + 1d6, lava cone 9" for 9d4+9 (save half), +1 weapons to hit, immune to *sleep, charm* and *hold*, +1 damage per die from cold. **The 1e split AC (3 upper / 1 lower) becomes 17**, and the cold "+1 per die" becomes vulnerability. ⚠️ **The trident is not treasure.** The 1e text gives it no loot line, though the appendix says greater salamanders "universally carry" one (**D4**). ⚠️ **Appendix B prints XP 11,076**, copied from Avraasha; the room statline says 2,090. **Use the room.**

> [!example]- Avraasha, the First Servant — CR 22 (41,000 XP) · Area 35
> *Huge elemental (pyroclastic sphinx), chaotic good (currently mad)*
> **Armor Class** 22 (natural armor) · **Hit Points** 324 (24d12 + 168) · **Speed** 45 ft., fly 75 ft.
>
> | STR | DEX | CON | INT | WIS | CHA |
> |---|---|---|---|---|---|
> | 26 (+8) | 14 (+2) | 24 (+7) | 22 (+6) | 24 (+7) | 22 (+6) |
>
> **Saving Throws** Dex +9, Con +14, Int +13, Wis +14
> **Skills** Arcana +20, History +20, Insight +14, Perception +14, Religion +20
> **Damage Immunities** fire
> **Senses** darkvision 120 ft., passive Perception 24 · **Languages** all, spoken and written · **Challenge** 22 (41,000 XP) · **Proficiency Bonus** +7
>
> ***Ember Sight.*** Avraasha sees invisible creatures and objects, and fog, smoke, and similar obscurement don't block her vision.
> ***Heated Body.*** A creature that touches Avraasha or hits her with a melee attack while within 5 feet of her takes 10 (3d6) fire damage.
> ***Legendary Resistance (3/Day).*** If Avraasha fails a saving throw, she can choose to succeed instead.
> ***Magic Resistance.*** Avraasha has advantage on saving throws against spells and other magical effects.
> ***Regeneration.*** Avraasha regains 10 hit points at the start of her turn if she is in contact with fire, magma, or lava.
> ***Innate Spellcasting.*** Her spellcasting ability is Wisdom (spell save DC 22, +14 to hit with spell attacks). She needs no material components.
> - At will: *comprehend languages, detect magic*
> - 5/day total, shared: *fireball* (cast as a 7th-level spell, 12d6), *wall of fire*
> - 3/day each: *clairvoyance, dispel magic, legend lore, locate object, remove curse, symbol*
> - 1/day each: *incendiary cloud, power word stun, telekinesis*
> - 3/day (only once she is calmed; see Epilogue): *heal*
>
> **Actions**
> ***Multiattack.*** Avraasha makes two claw attacks.
> ***Claw.*** *Melee Weapon Attack:* +15 to hit, reach 10 ft., one target. *Hit:* 21 (3d8 + 8) slashing damage.
>
> **Legendary Actions**
> Avraasha can take 3 legendary actions, choosing from the options below. Only one legendary action can be used at a time and only at the end of another creature's turn. Avraasha regains spent legendary actions at the start of her turn.
> - ***Claw.*** Avraasha makes one claw attack.
> - ***Ashen Wings (Costs 2 Actions).*** Avraasha flies up to half her flying speed without provoking opportunity attacks.
> - ***Cast a Spell (Costs 3 Actions).*** Avraasha casts a spell from her 3/day or 5/day list, using a daily use.
>
> **Conversion note.** 1e: AC −5, MV 18"/30", **HD 24 (168 hp)**, 3d8/3d8, MR 50%, always *detect invisible* and *detect magic*, *read magic* at will, sees through fog and smoke, 12-dice *fireball* or *wall of fire* 5/day, 3/day each of 7 spells, 1/day *power word stun* and *incendiary cloud*, immune to fire, lava and smoke, 2d6 on contact (save half), regenerates 2/round in fire. **The 24 HD carries across as 24 Hit Dice**, and the **12-dice fireball carries across as 12d6**. MR 50% becomes Magic Resistance plus Legendary Resistance. Regeneration scales off the troll (1e 3/round → 5e 10). **CR check:** defence 324 + 30 regeneration + 90 Legendary Resistance = 444 effective (CR 21), AC 22 against an expected 19, plus Magic Resistance → **22**. Offence around 150 DPR across three rounds (two-target fireballs plus legendary claws), DC 22 → **22**. The 1e XP ratio to Yox (11,076 : 2,720 ≈ 4.1) against the 5e ratio (41,000 : 7,200 ≈ 5.7) shows she is placed slightly higher relative to Yox than in 1e. That is deliberate; the module wants her unwinnable. 🔒 **D3:** *telekinesis* (1/day) and *heal* were added because the module's own prose uses them. *Telekinesis* adds no damage, and *heal* is post-combat only, so **the CR stays 22.**

### 4.3 · Wandering monster tables

**Temple Incandescent (d100, every 10 minutes on a d6 roll of 1, p. 6)**

| d100 | 1e | 5e |
|---|---|---|
| 01–05 | Efreeti (1) | 🔒 **A second efreeti** (MM, CR 11), not Yox. The text ties Yox to his room (*"Yox yet remains within the chamber"*, A33) and never links him to the table. It is one of the summoned creatures *"not yet released … when The Burning Athenium tore free"* (p. 6). **Sigil-eligible.** It has none of Yox's knowledge and doesn't offer his bargain |
| 06–25 | Fire bats (1d6) | Fire Bat (custom) |
| 26–35 | Air elemental, small (1) | **The A12 air elemental** if still alive; otherwise reroll *(conversion call: the module has exactly one)* |
| 36–40 | Fire elemental, small (1) | Fire Elemental (MM) |
| 41–55 | Grue, harginn (1d2) | Harginn Grue (custom) |
| 56–95 | Magmen (1d12) | Magman (custom). ⚠️ **1d12 CR 1s, at 40% odds**, is the table's real danger: 12 magmen is 7,200 adjusted XP |
| 96–00 | Phantom stalker (1d2) | Phantom Stalker (custom, no medallion bond) |

**Freehold Foothills (overland, p. 4)** — optional if the site is relocated.

| d100 | 1e | 5e MM |
|---|---|---|
| 01–10 | Dwarves 2d10 | Guard (dwarf), with a Veteran per 5 |
| 11–15 | Giants 1d6 | Hill Giant (or roll a giant type) |
| 16–20 | Fire giants 1d6 | Fire Giant (CR 9). ⚠️ 1d6 of them is lethal in either edition |
| 21–23 | Goblins 3d10 | Goblin |
| 24–25 | Hell hounds 1d4 | Hell Hound |
| 26–30 | Kobolds 3d10 | Kobold |
| 31–32 | Cavemen 1d10 | Tribal Warrior |
| 33–37 | Ogres 1d8 | Ogre |
| 38–47 | Orcs 3d10 | Orc |
| 48–50 | Trolls 1d6 | Troll |
| 51–00 | Standard tables | DMG mountain table |

---

## 5 · Items, spells, treasure

### 5.1 · 1e items with a direct 5e equivalent

| Item (area) | 5e item | Note |
|---|---|---|
| Bracers of defense AC5 (A10) | **Bracers of defense** | 1e AC5 → 5e +2 AC unarmoured |
| Ring of warmth (A13) | **Ring of warmth** | |
| Footman's flail +2 ×2 (A13, A33) | **Flail +2** ×2 | |
| Potion of extra-healing (A15) | **Potion of greater healing** | |
| Gauntlets of ogre power (A15) | **Gauntlets of ogre power** | |
| Robe of scintillating colors (A15) | **Robe of scintillating colors** | |
| Decanter of endless water (A17) | **Decanter of endless water** | |
| Dust of disappearance (A20) | **Dust of disappearance** | 5 uses (D4) |
| Dagger +2 (A22) | **Dagger +2** | |
| Hat of disguise (A22) | **Hat of disguise** | Shaped as a black hair ribbon |
| Marvelous pigments (A27) | **Nolzur's marvelous pigments** | 3 pots |
| Ring of fire resistance (A29) | **Ring of resistance (fire)** | |
| Chain shirt +1 (A32) | **Chain shirt +1** | Xuel antique, double value |
| Small metal shield +2 (A32) | **Shield +2** | Xuel antique, double value |
| Brooch of shielding (A33) | **Brooch of shielding** | Drop the 77 charges |
| Ring of protection +2 ×2 (A10, A20) | **Ring of protection** (+1) | D4 |
| Cloak of protection +2 (A15) | **Cloak of protection** (+1) | D4 |

### 5.2 · Custom items (no 5e equivalent)

| ID | Item (area) | 5e build | Rarity |
|---|---|---|---|
| **I1** | Castellan's breastplate, "as elfin chain +2" (A8) | **Breastplate +2.** Its wearer counts as proficient with it (the elfin-chain property) | Very rare |
| **I2** | Raptor-feathered helm (A8) | While worn **with I1**: cast *see invisibility* (self) 3/day; it ends after 1 minute and reaches only 30 ft (1e 3"). Requires attunement | Uncommon |
| **I3** | Short sword of sharpness (A8) | **Sword of sharpness**, shortsword. ⚠️ 5e sharpness needs a slashing sword and the shortsword is piercing. **This one deals slashing damage** (D4) | Very rare |
| **I4** | Ornate silver dagger −1, cursed (A9) | Silvered dagger, **−1 to attack and damage**. **Curse:** once attuned you can't voluntarily discard it, and you must draw it whenever you draw a weapon (1e cursed-weapon behaviour). *Remove curse* ends the attunement | Uncommon (cursed) |
| **I5** | Xuel gold coin | Treasure item, **50 gp each** to a collector. ⚠️ Enter as an **item**, never as a coin field (I7 rule) | — |
| **I6** | Robe of Raanet's faithful (A6) | Mundane. Disarms Areas 4/5 | — |
| **I7** | Lyre of building, 3 strings broken (A11) | Built from the **1e DMG entry**. It looks like an ordinary lyre and is indistinguishable from an *instrument of the bards* until played. **Doesn't work until restrung.** **Protect (1/day):** as a reaction, playing it negates, *for constructions only*, a *horn of blasting*, a *disintegrate* spell, or up to 6 minutes of an earth elemental's siege damage (1e: 6 rounds). **Build (1/week):** 30 minutes of playing (1e: 3 turns) does the work of **100 labourers for 3 days**: buildings, mines, tunnels, ditches. **False chord:** each use, roll a d20. On 1–4 (1e 20%) the effect is negated. **If the player is proficient with the lyre** (1e "knows the proper chords"), only a 1 negates it (5%). **If the player takes damage or is subjected to a mental attack while playing**, 1–10 negates it (50%) | Rare |
| **I8** | Wand of ice storms, 10 charges (A13) | **Wand of ice storm.** Expend 1 charge to cast *ice storm* (DC 15). **10 charges, no recharge** (1e wands don't recharge; D4). Double value as a Xuel antique | Rare |
| **I9** | Potion of levitation (A15) | Drink it to gain the effect of *levitate* on yourself for 10 minutes, with no concentration | Uncommon |
| **I10** | ad-Dax's glass jar (A20) | **Bag of holding** reskinned as a glass jar. ad-Dax's rune on the base | Uncommon |
| **I11** | Alabaster wand of fire, 5 charges (A22) | Built from the **1e DMG entry**. **5 charges remaining, out of 7 at full. Regains 1d6 + 1 charges at dawn** (1e: "it can be recharged"). Requires attunement by a spellcaster. Spell save DC 15. **1 charge:** *burning hands* · **1 charge:** *pyrotechnics* (XGE) · **2 charges:** *fireball* (8d6) · **2 charges:** *wall of fire*. Usable once per round. **It doesn't charge a Sigil rod**: its fireball is 8 dice, short of the 10 required | Rare |
| **I12** | Ring of human influence (A25a) | Built from the **1e DMG entry**. Requires attunement. **Your Charisma counts as 18** for Charisma checks to influence humanoids (no effect if it is already 18 or higher). **1/day:** *suggestion* (DC 15) on a humanoid you are talking with. **1/day:** *charm person* cast as a 5th-level spell (DC 15, up to five humanoids). That is 1e's "charm up to 21 levels/HD of humans" expressed as 5e targets | Rare |
| **I13** | Luck stone / stone of weight (A25c) | **Stone of good luck** for a worshipper of the Xuel pantheon. For anyone else, a cursed **stone of weight**: your speed drops by 10 ft, and you can't get rid of it until it is the target of *remove curse* (1e loadstone) | Uncommon |
| **I14** | Miniature sword → broadsword +2 (A25g) | Tiny sword charm. Held by a **fighter, paladin or ranger** (1e "Fighter or subclass"), it becomes a **longsword +2** | Rare |
| **I15** | Priestess's holy symbol (A25h) | Requires attunement **by a devotee of Raanet**. +1 bonus to AC and saving throws (5e ring of protection value; D4) that **stacks** with other protective items. Works as a holy symbol | Rare |
| **I16** | Bountiful Cornucopia (A30, App. A) | Ceramic figurine. **3/day:** concentrate on hunger to create **12 cu ft of food and drink**, enough for **36 humanoids or 12 horses for a day** (1e numbers, larger than *create food and water*). Fine quality. **A fourth use in a day** fails and ruins it for good | Very rare |
| **I17** | Xuel bastard sword +2 ×2 (A32) | **Longsword +2** (versatile 1d8/1d10). Xuel antique, double value | Rare |
| **I18** | Avraasha's wish (Epilogue) | DM-held. One *wish* per PC, granted by Avraasha. No stress. Used immediately, or banked as *Avraasha's Ember* | Artifact-grade |
| **I19** | Sigil rod ×4 (A13, A15, A22, A33) | Plot item, §2.1. Immune to damage | Artifact |
| **I20** | ad-Dax's golden medallion (A19) | Plot object. AC 15, 5 HP. Attuned to the dead bard and useless to anyone else. Destroying it kills the stalkers. Gold value (*conversion call*): 100 gp | — |

### 5.3 · Spells referenced (no new spells needed)

Every module spell maps to a 5e spell, so **no custom spells are needed.**

| 1e spell | Where | 5e |
|---|---|---|
| Wall of stone | A4–5, A18, A22 scroll | *Wall of stone* |
| Audible glamer | A18 | *Minor illusion* (sound) |
| Spectral force | A18, A22 | *Major image* (permanent) |
| Hallucinatory terrain | A22 | *Hallucinatory terrain* (permanent) |
| Explosive runes | A24 | *Glyph of warding* (explosive runes) |
| Chill / flavor / freshen / preserve cantrips | A17 | *Prestidigitation* |
| Create food (cornucopia) | A30 | (I16) |
| Commune | Intro | *Commune* |
| Comprehend languages | A22 scroll | *Comprehend languages* (1st) |
| Contact other plane | A22 scroll | *Contact other plane* (5th) |
| **Monster summoning IV** | A22 scroll | 🔒 ***Monster summoning IV*** (6th level), from the new series [[C12 - Monster Summoning I-VII (5e)]]. It works inside the Temple |
| Slow | A22 scroll | *Slow* (3rd) |
| Fireball, wall of fire, incendiary cloud, power word stun, symbol, legend lore, locate object, dispel magic, remove curse, clairaudience/clairvoyance | Avraasha | Same names; clairaudience and clairvoyance merge into *clairvoyance* |
| Speak with dead | A7 | *Speak with dead* (resisted, no save; it simply fails) |

The A22 scroll becomes **five 5e spell scrolls** (one spell each), all wizard.

### 5.4 · Treasure ledger (module values)

Shown so the FG parcels can be checked later. Excludes the sage-only finds, which have to be copied before they can be sold.

| Area | Coin / gem / art (gp) |
|---|---|
| A3 | Iron barrier 1,000 |
| A5 | Diary 15,000 |
| A8 | 10 Xuel coins = 500 |
| A9 | 27 Xuel coins = 1,350 |
| A10 | Gold slag 250 |
| A13 | 250 Xuel coins = 12,500 · 5 rubies = 500 |
| A14 | 9 portraits ≈ 31,500 (3,500 each) |
| A15 | 240 Xuel coins = 12,000 · *Warmed by the Flame* 2,500 |
| A16 | Carnelian 50 · jacinth 250 |
| A17 | Silver plate 100 · 2 wine casks 5,000 |
| A21 | 22 gems = 11,400 |
| A22 | Fire tomes 2,500 |
| A25 | Wedding rings 200 · needle 1 |
| A31 | Tools 100 |
| A32 | 120 Xuel coins = 6,000 · diamonds 75 · adamantite rings 500 |
| **Total** | **103,276 gp** (machine-summed), plus the sage-only finds: A2 500, A3 lyrics 2,500, A24 script 500 |

---

## 6 · Encounter math (DMG 2014, adjusted XP)

| Encounter | Raw XP | Adjusted | 6 × L5 | **6 × L6** | 6 × L7 | 5 × L8 |
|---|---|---|---|---|---|---|
| A3 Keeper-of-the-Hearth | 1,800 | 1,800 | Easy | **Easy** | Trivial | Trivial |
| A4 / A5 caryatid (one per alcove) | 450 | 450 | Trivial | **Trivial** | Trivial | Trivial |
| A9 2 wraiths | 3,600 | 5,400 | Hard | **Hard** | Medium | Medium |
| A10 5 magmen | 1,000 | 2,000 | Easy | **Easy** | Trivial | Trivial |
| A10 + A11 together (9 magmen) | 1,800 | 4,500 | Hard | **Medium** | Medium | Medium |
| A12 air elemental | 1,800 | 1,800 | Easy | **Easy** | Trivial | Trivial |
| A13 4 harginn grues | 1,800 | 3,600 | Medium | **Medium** | Easy | Easy |
| A15 Ranzaar | 1,800 | 1,800 | Easy | **Easy** | Trivial | Trivial |
| A16 12 fire bats | 600 | 1,800 | Easy | **Easy** | Trivial | Trivial |
| A19 3 phantom stalkers | 2,100 | 4,200 | Medium | **Medium** | Easy | Easy |
| A21 Ixthasus alone | 5,900 | 5,900 | Hard | **Hard** | Medium | Medium |
| A21 Ixthasus + 2 salamanders (50% alarm) | 9,500 | 19,000 | Deadly 287% | **Deadly 226%** | Deadly 186% | Deadly 180% |
| A22 4 salamanders | 7,200 | 14,400 | Deadly 218% | **Deadly 171%** | Deadly 141% | Deadly 137% |
| A22 2 salamanders (after the A21 alarm) | 3,600 | 5,400 | Hard | **Hard** | Medium | Medium |
| A23 5 magmen | 1,000 | 2,000 | Easy | **Easy** | Trivial | Trivial |
| A25 stone guardian | 700 | 700 | Trivial | **Trivial** | Trivial | Trivial |
| A28 4 magmen | 800 | 1,600 | Easy | **Trivial** | Trivial | Trivial |
| A30 5 wights | 3,500 | 7,000 | Deadly 106% | **Hard** | Hard | Hard |
| A32 2 swordwraiths | 3,600 | 5,400 | Hard | **Hard** | Medium | Medium |
| A33 Yox | 7,200 | 7,200 | Deadly 109% | **Hard** | Hard | Hard |
| A35 Avraasha | 41,000 | 41,000 | Deadly 621% | **Deadly 488%** | Deadly 401% | Deadly 390% |

> [!warning] What the XP tier hides (doctrine rule 5)
> - **Magmen** melt nonmagical and +1 weapons. A martial party with mundane steel loses its weapons fight by fight, which compounds across four magmen rooms.
> - **Swordwraiths** halve +1 weapons and ignore mundane ones entirely. A party without +2 weapons may simply not be able to win A32. The Area 8 sword of sharpness and the A13 flail +2 are the module's answers, and **both sit behind other fights.**
> - **Harginn grues** turn every fire spell into a wasted slot.
> - **Room hazards** (A21 heat, A22 illusion) add 3–4 damage per creature per round on top of the monsters, and A21 strips concentration.
> - **The Sigil's creature route kills with a touch, no save** (§2.1). A rogue with the rod can delete a CR 11 efreeti. That is the module's intended answer to Yox and Ixthasus, and it should stay.

---

## 7 · Decisions for you

- [x] **D1a · Do salamanders charge a rod?** 🔒 **No, by either route.** *Creature route:* 1e 7+7 HD is short of 8 HD, and Appendix A's examples name the *greater* salamander. *Fire route:* an MM salamander's biggest single hit carries **3d6 fire** (spear) or 2d6 (tail), far short of 10 dice. **Ixthasus does qualify by both routes:** 9+9 HD, and Magma Spray is 10d8.
- [x] **D1b · Fire route.** 🔒 **Ten or more dice of fire damage in one instance** (2026-11-08).
- [x] **Rod count.** 🔒 **Four** (2026-11-08).
- [x] **D2 · A22 salamanders.** 🔒 **Four.** At 6 × L6, four are 171% of Deadly and five are 214%, so four is the closer of the two (2026-11-08). For reference, three would be 129% and two would be Hard. The wandering efreeti is 🔒 **a second efreeti** (§4.3).
- [x] **D3 · Avraasha's missing powers.** 🔒 *Telekinesis* 1/day and *heal* 3/day (once calmed) added. CR unchanged (2026-11-08).
- [x] **D4 · Item power limits.** 🔒 **Accepted as recommended** (2026-11-09): the +2 rings and cloak become +1, the ice-storm wand has 10 non-recharging charges, the dust has 5 uses, the shortsword of sharpness deals slashing damage, and Ixthasus's trident isn't treasure.
- [x] **D5 · Abilities from the prose.** 🔒 (2026-11-09) The phantom stalkers **keep Unseen Vigil** (invisibility). The caryatids break weapons **by the *Fiend Folio* rule**: any weapon, less likely the higher its plus (revised 2026-11-15; the first ruling was nonmagical only). *Monster summoning IV* becomes a **new 5e series**, [[C12 - Monster Summoning I-VII (5e)]], rebuilt from the 1e DMG Appendix M tables. The Area 22 scroll is the **fourth spell in that series**.
- [x] **D6 · "No save" traps.** 🔒 **No save on A18, A23, A26 and the A21 heat. Saves for half on A9 (DC 15 Con) and A24 (DC 15 Dex)** (2026-11-08). Applied in §3.
- [x] **D7 · Child of Fire.** ✅ **A title passed from leader to leader.** At least three holders appear in the text: an unnamed man (built the Oubliette, A8), **Kaara ad-Karza** (A15), and **Leathri il-Varzii**, her successor and the last (A14). No edit to the module is needed. See §3, A14.
- [x] **D8 · A15's coins.** 🔒 **240 Xuel coins at 50 gp = 12,000 gp** (2026-11-08).
- [x] **Area 10 / 11 treasure.** ✅ Confirmed against the page image and fixed in §3.
- [x] **Lyre of building and ring of human influence.** ✅ Rebuilt from the 1e DMG (§5.2, I7 and I12). The alabaster wand of fire (I11) was also corrected to the 1e DMG: four functions, rechargeable.
- [x] **D9 · Pregens.** 🔒 **All eight converted** to 5e level 6. See [[C12 - Pregenerated Characters (5e)]] (2026-11-09).
- [x] **D10 · Greyhawk names.** ✅ The module text stays as published; §8 is a DM conversion note mapping each name to its Greyhawk counterpart.

---

## 8 · DM conversion note: Greyhawk names

> [!note] For the DM
> C12 is set in Greyhawk with the names filed off, usually by **reversing or anagramming** the canon name. The module text and the FG build **keep the module's names as published**. Use this table to place the adventure in a canon Greyhawk game. **✅** = certain (a clear reversal or anagram, or the same story). **🟡** = likely, by geography or title. **❓** = no counterpart identified; treat it as the module's own invention.

### Peoples, gods and history

| Module | Greyhawk | Confidence and how |
|---|---|---|
| Xuel, Xuloise | **Suel, Suloise** | ✅ X for S |
| Xuel Imperium | **Suel Imperium** | ✅ |
| Rain of Invisible Flame / "colorless fire" | **Rain of Colorless Fire** | ✅ |
| Twin Cataclysms · Mages of Power · the Invisible Art | Same names | ✅ Canon, unchanged |
| Ancient Xuloise (script) | **Ancient Suloise** | ✅ |
| Nitorels, "Last Mage of Power" | **Slerotin** | ✅ Spelled backwards |
| Passage of Nitorels | **Slerotin's Passage** (under the Hellfurnaces) | ✅ |
| Wee Saj · the Ruby Sorceress · Sajians | **Wee Jas** · the Ruby Sorceress · Jasians | ✅ Reversed. "Ruby Sorceress" is her canon title, unchanged |
| **Raanet**, Xuel goddess of fire and hospitality | **Ranet**, Suel goddess of fire | ✅ Same story: in canon, **Pyremius poisoned Ranet and took her fire portfolio**, and her final fate is left unresolved |
| The "sinister god" who poisons her cup and steals her flame (Intro) | **Pyremius** | ✅ |
| Gladsheim (Muspelheim) · Surtur · City of Brass · Elemental Plane of Fire | Same names | ✅ Canon 1e cosmology |

### Places

| Module | Greyhawk | Confidence and how |
|---|---|---|
| Hellforge Mountains | **Hellfurnaces** | ✅ |
| Jötunn Mountains | **Jotens** | ✅ |
| Oekland | **Keoland** | ✅ Anagram |
| Looh River · Looh Marshes | **Hool** River and **Hool Marshes** | ✅ Reversed |
| Freehold (box canyon of grassland below the Jotens and Hellfurnaces, Xuel refugees, strong militia) | **Yeomanry** | 🟡 By geography and history |
| Wickloft (seat of the Ruby Cathedral) | **Loftwick**, capital of the Yeomanry | 🟡 Syllables swapped |
| Hold of the Sea Barons | **Hold of the Sea Princes** | ✅ |
| Crimson Brotherhood | **Scarlet Brotherhood** | ✅ |
| Javan River | Javan River | ✅ Canon, unchanged |
| Doomwood (pregen text) | **Dreadwood** | 🟡 The Keoland forest on the Hool Marshes |
| Vast basin of ash beyond the western mountains | **Sea of Dust** | ✅ |
| Bleak Gate (where the passage opens into the Freehold) | Eastern mouth of **Slerotin's Passage** | 🟡 Location only; no canon name confirmed |
| Little Hills (gnome and halfling homeland in the Freehold) | ❓ | Possibly the hills of the Yeomanry; not confirmed |
| Elrub (pregen text) | ❓ | No match found |
| Mount Xavi | ❓ | The module itself says "or whatever geological event you choose" |
| Sól ("Sól's revealing kiss") | ❓ | The sun, by Norse name; no Suel counterpart identified |
| "Caves of Chaos" (pregen text) | Module B2 | ✅ A nod to *The Keep on the Borderlands* |

### Using the canon in play

- **Who killed Raanet?** In canon it was Pyremius, by poison. Nothing in C12 names him, and Avraasha doesn't know (her *"dire revenge"* in the Epilogue is aimed at someone she hasn't learned of yet). A DM who restores the names gets a ready sequel hook: **Pyremius's cult**.
- **Where is it?** Under the Hellfurnaces on the Yeomanry side, near the eastern mouth of Slerotin's Passage. ⚠️ The module gives two distances: *"nearly 30 miles north of Bleak Gate"* (Adventure Location, p. 3) and *"almost 60 miles northwest"* (Campaign Notes, p. 5). Pick one.
- **Wee Jas** fits canon as written: the death-and-magic goddess whose priestess, Anras il-Fruztii (A33), stayed to tend the dead.

Sources: [Ranet — Greyhawk Wiki](https://www.greyhawkonline.com/greyhawkwiki/Ranet) · [Pyremius — Greyhawk Wiki](https://greyhawkonline.com/greyhawkwiki/Pyremius)

---

## 9 · What comes next (after review)

1. ✅ All decisions are closed.
2. Generate **FG Import Text blocks** for the nine custom creatures and the **List Import** for items I1–I20 (with an effects appendix).
3. Count map surfaces from the PDF map pages (not done yet).
4. Player handouts **H1** (A4 history book), **H2** (A5 diary), **H3** (A15 letter) from verbatim module text.
5. Treasure parcels, one per place the party finds something, reconciled to §5.4.
