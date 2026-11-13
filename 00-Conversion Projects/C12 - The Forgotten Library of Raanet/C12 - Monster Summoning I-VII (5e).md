---
tags: [adventure/C12, conversion, spells, fgu-prep]
adventure: "C12 - The Forgotten Library of Raanet"
source: "1e PHB (spell text, magic-user spells 3rd–9th level); 1e DMG Appendix M (Summoned Monsters, pp. 222–224)"
status: review (PHB-verified)
created: 2026-11-09
publish: false
---
# Monster Summoning I–VII (5e conversion)

A seven-spell series rebuilt from AD&D 1e's *monster summoning* spells. C12 needs it because the Area 22 scroll holds **monster summoning IV**, and 5e has no equivalent. The whole series is here so the FG spell records stay consistent.

> [!info] What carried over from 1e, and what didn't
> - **Carried straight:** the spell level (1e *monster summoning I* was a 3rd-level magic-user spell, *VII* a 9th), range (1e 1" = 10 ft), the number summoned, the arrival delay, the material component, and the **d100 creature tables** from DMG Appendix M.
> - **Converted:** 1e creatures are mapped to 5e statblocks (MM 2014 unless noted). 1e duration (rounds of 1 minute each, plus 1 per caster level) becomes **Concentration, up to 10 minutes**.
> - **Added:** a **CR budget per spell level** (the *Budget rule* below). 1e's tables are uneven, and some 1e names (hydras, erinyes, rakshasa) became much stronger creatures in 5e.
> - **The C12 note:** the Temple's marble blocks teleportation but not summoning (ledger M1). This series works inside the dungeon.

> [!success] Checked against the 1e Players Handbook (2026-11-09)
> Every spell parameter below (level, range, number, arrival delay, duration, components) matches the PHB text. The PHB also settles how the creatures behave: **there is no control roll.** Per *monster summoning I*, the monsters *"will attack the spell user's opponents to the best of their ability until he or she commands that attack cease, or the spell duration expires, or the monsters are slain."* With no enemy to fight, they *"can, if communication is possible, and if they are physically capable, perform other services for the summoning magic-user."* The PHB also says the referee may pick the number *"according to the strength of the monster randomly determined"*, which is the 1e basis for the **budget rule** below.

---

## Shared rules (all seven spells)

***Monster Summoning [I–VII]***
*[level] conjuration*
**Casting Time:** 1 action
**Range:** see the table below
**Components:** V, S, M (a tiny bag and a small candle, not necessarily lit)
**Duration:** Concentration, up to 10 minutes
**Classes:** Wizard (and Sorcerer at the DM's option)

You call creatures from elsewhere to fight for you. Roll d100 on the spell's table to see what kind of creature answers, then roll the number that appears. **They don't arrive at once.** They appear in unoccupied spaces you can see within range **at the start of your turn**, after the number of rounds shown in the table. The spell's concentration starts on the turn you cast it.

The creatures are friendly to you and your companions. **No check is needed to control them** (1e PHB). Roll initiative for them as a group; they take their own turns. They attack your enemies to the best of their ability until you command them to stop (no action required), the spell ends, or they are slain. **With no enemy present**, a creature that can understand you and is physically able will perform other tasks for you instead. A creature disappears when it drops to 0 hit points or when the spell ends.

**Paired creatures.** Some table entries give two creatures, for example *Goblin (Dwarf)*. **Use the first creature for an evil or neutral caster, the bracketed one for a good caster.** ⚠️ The DMG literally says *"If the summoner is evil, the monster in parentheses may be used"* (p. 222). Every bracketed creature, though, is the good one: dwarf, elf, blink dog, couatl, werebear, lammasu, shedu, androsphinx. That reads as a 1e misprint for *good*, and this note assumes so.

**Water.** Cast on or under water, the spell uses that level's **water table** (fresh or salt) instead.

**Budget rule (5e addition).** Each spell has a **CR budget**. If the creature rolled, multiplied by the number rolled, would go over the budget, **reduce the number until it fits, to a minimum of one.** Entries marked ⚠️ are over budget even alone; **one appears and the spell's duration drops to 1 minute.** That keeps 1e's surprise ("you summoned a *hydra*?") without letting a 6th-level slot buy a CR 8 creature for ten minutes.

**At Higher Levels.** None. Cast a higher-numbered *monster summoning* instead, as in 1e.

| Spell | 5e level | Range (1e) | Number (1e) | Arrives after (1e) | 1e duration | CR budget |
|---|---|---|---|---|---|---|
| *Monster Summoning I* | 3rd | 30 ft (3") | 2d4 | 1d4 rounds | 2 rounds + 1/level | 2 |
| *Monster Summoning II* | 4th | 40 ft (4") | 1d6 | 1d4 rounds | 3 rounds + 1/level | 3 |
| *Monster Summoning III* | 5th | 50 ft (5") | 1d4 | 1d4 rounds | 4 rounds + 1/level | 5 |
| *Monster Summoning IV* | 6th | 60 ft (6") | 1d3 | 1d3 rounds | 5 rounds + 1/level | 6 |
| *Monster Summoning V* | 7th | 70 ft (7") | 1d2 | 1d3 rounds | 6 rounds + 1/level | 8 |
| *Monster Summoning VI* | 8th | 80 ft (8") | 1d2 | 1d3 rounds | 7 rounds + 1/level | 10 |
| *Monster Summoning VII* | 9th | 90 ft (9") | 1d2 | 1 round | 8 rounds + 1/level | 14 |

**📘** marks a creature with a custom statblock in [[C12 - Summoning Bestiary (5e)]], converted from the 1e *Monster Manual*. Unmarked entries are existing 5e statblocks.

*Budget basis:* the 5e conjure-spell benchmarks. *Conjure animals* at 3rd level buys about CR 2 in total, and *conjure elemental* at 5th buys CR 5, rising 1 per slot level. The arrival delay and the random table are the series' costs against those spells, so the budgets sit at or slightly above them.

---

## Monster Summoning I (3rd level)

| d100 | 1e (DMG App. M) | 5e creature | CR |
|---|---|---|---|
| 01–10 | Demon, manes | Manes | 1/8 |
| 11–25 | Goblin (Dwarf) | Goblin (📘 Dwarf) | 1/4 (1/4) |
| 26–40 | Hobgoblin (Elf) | Hobgoblin (📘 Elf) | 1/2 (1/4) |
| 41–55 | Kobold (Halfling) | Kobold (📘 Halfling) | 1/8 (1/8) |
| 56–70 | Orc (Gnome) | Orc (📘 Gnome) | 1/2 (1/8) |
| 71–00 | Rat, giant | Giant Rat | 1/8 |

**Water:** *Fresh* 01–67 Koalinth → 📘 Koalinth (1/2) · 68–00 Nixie → 📘 Nixie (1/8). *Salt* 01–50 Koalinth · 51–00 Merman → Merfolk (1/8).

## Monster Summoning II (4th level)

| d100 | 1e | 5e creature | CR |
|---|---|---|---|
| 01–15 | Centipede, giant | Giant Centipede | 1/4 |
| 16–25 | Devil, lemure | Lemure | 0 |
| 26–45 | Gnoll | Gnoll | 1/2 |
| 46–60 | Stirge | Stirge | 1/8 |
| 61–75 | Toad, giant | Giant Toad | 1 |
| 76–00 | Troglodyte | Troglodyte | 1/4 |

**Water:** *Fresh* 01–00 Lizard man → Lizardfolk. *Salt* 01–33 Ixitxachitl → 📘 Ixitxachitl (1/2) · 34–00 Locathah → 📘 Locathah (1/4).

## Monster Summoning III (5th level)

| d100 | 1e | 5e creature | CR |
|---|---|---|---|
| 01–07 | Beetle, boring | 📘 Boring Beetle | 2 |
| 08–17 | Bugbear | Bugbear | 1 |
| 18–25 | Gelatinous cube | Gelatinous Cube | 2 |
| 26–32 | Ghoul | Ghoul | 1 |
| 33–40 | Lizard, giant | Giant Lizard | 1/4 |
| 41–47 | Lycanthrope, wererat | Wererat | 2 |
| 48–57 | Ochre jelly | Ochre Jelly | 2 |
| 58–67 | Ogre | Ogre | 2 |
| 68–75 | Spider, huge | 📘 Huge Spider | 1 |
| 76–85 | Spider, large | Giant Wolf Spider | 1/4 |
| 86–95 | Tick, giant | 📘 Giant Tick | 1/2 |
| 96–00 | Weasel, giant | Giant Weasel | 1/8 |

**Water:** *Fresh* 01–33 Crab, giant → Giant Crab (1/8) · 34–00 Lacedon → 📘 Lacedon (1). *Salt* 01–50 Lacedon · 51–00 Sahuagin (1/2).

## Monster Summoning IV (6th level) · *the Area 22 scroll*

| d100 | 1e | 5e creature | CR |
|---|---|---|---|
| 01–07 | Ape, carnivorous | 📘 Carnivorous Ape | 3 |
| 08–15 | Gargoyle (Blink dog) | Gargoyle (Blink Dog) | 2 (1/4) |
| 16–25 | Ghast | Ghast | 2 |
| 26–35 | Gray ooze | Gray Ooze | 1/2 |
| 36–42 | Hell hound | Hell Hound | 3 |
| 43–50 | Hydra, 5 heads | 📘 Hydra (Greyhawk), 5-headed | 4 |
| 51–58 | Lycanthrope, werewolf | Werewolf | 3 |
| 59–67 | Owlbear | Owlbear | 3 |
| 68–76 | Shadow | Shadow | 1/2 |
| 77–86 | Snake, giant constrictor | Giant Constrictor Snake | 2 |
| 87–93 | Toad, ice | 📘 Ice Toad | 3 |
| 94–00 | Toad, poisonous | 📘 Poisonous Toad | 1/2 |

**Water:** *Fresh* 01–33 Giant water beetle → 📘 Giant Water Beetle (2) · 34–50 Giant crayfish → 📘 Giant Crayfish (2) · 51–67 Kopoacinth → 📘 Kopoacinth (2) · 68–00 Giant water spider → 📘 Giant Water Spider (1). *Salt* 01–40 Kopoacinth · 41–80 Giant lobster → 📘 Giant Crayfish (2) · 81–00 Triton *(VGtM/MPMM)* (1/2).

> [!example]- C12 Area 22: *Spell Scroll (Monster Summoning IV)*
> Very rare spell scroll (6th level). Save DC 17, attack bonus +9. A wizard who can't yet cast 6th-level spells must succeed on a **DC 16 ability check using their spellcasting ability** to read it. **It works inside the Temple** (summoning isn't blocked by the marble). At a budget of 6: a hell hound, werewolf or owlbear comes **1d3** strong (up to 3 × CR 3 = 9, so cut to **two**). A ghast or gargoyle fits all three. **A hydra roll gives one 5-headed hydra** (CR 4; a second would break the budget).

## Monster Summoning V (7th level)

| d100 | 1e | 5e creature | CR |
|---|---|---|---|
| 01–07 | Cockatrice | Cockatrice | 1/2 |
| 08–17 | Displacer beast | Displacer Beast | 3 |
| 18–26 | Doppleganger | Doppelganger | 3 |
| 27–36 | Hydra, 7 heads | 📘 Hydra (Greyhawk), 7-headed | 6 |
| 37–45 | Leucrotta | Leucrotta *(VGtM/MPMM)* | 3 |
| 46–55 | Lizard, subterranean | 📘 Subterranean Lizard | 2 |
| 56–63 | Lycanthrope, wereboar | Wereboar | 4 |
| 64–72 | Minotaur | Minotaur | 3 |
| 73–78 | Snake, giant amphisbaena | 📘 Giant Amphisbaena | 3 |
| 79–85 | Snake, giant poisonous | Giant Poisonous Snake | 1/4 |
| 86–90 | Snake, giant spitting | 📘 Giant Spitting Snake | 1 |
| 91–00 | Spider, giant | Giant Spider | 1 |

**Water:** *Fresh* 01–80 Crocodile, giant → Giant Crocodile · 81–00 Water weird → Water Weird. *Salt* 01–50 Giant Crocodile · 51–70 Sea Hag · 71–90 Sea lion → 📘 Sea Lion (3) · 91–00 Water Weird.

## Monster Summoning VI (8th level)

| d100 | 1e | 5e creature | CR |
|---|---|---|---|
| 01–06 | Carrion crawler | Carrion Crawler | 2 |
| 07–12 | Devil, erinyes | ⚠️ Erinyes | 12 |
| 13–19 | Hydra, 8 heads | 📘 Hydra (Greyhawk), 8-headed | 7 |
| 20–26 | Jackalwere (Lammasu) | Jackalwere *(VGtM/MPMM)* (📘 Lammasu) | 1/2 (5) |
| 27–31 | Lycanthrope, weretiger (Werebear) | Weretiger (Werebear) | 4 (5) |
| 32–38 | Manticore | Manticore | 3 |
| 39–43 | Ogre magi | Oni | 7 |
| 44–51 | Otyugh | Otyugh | 5 |
| 52–56 | Rakshasa | ⚠️ Rakshasa | 13 |
| 57–63 | Salamander | Salamander | 5 |
| 64–68 | Spider, phase | Phase Spider | 3 |
| 69–78 | Troll | Troll | 5 |
| 79–84 | Wight | Wight | 3 |
| 85–88 | Wind walker | 📘 Wind Walker | 5 |
| 89–92 | Wraith | Wraith | 5 |
| 93–00 | Wyvern | Wyvern | 6 |

**Water:** *Fresh or salt* 01–33 Octopus, giant → Giant Octopus · 34–00 Snake, sea, giant → 📘 Giant Sea Snake (5).

## Monster Summoning VII (9th level)

1e PHB: **1–2 seventh-level monsters arriving 1 round after casting, or 1 eighth-level monster arriving after 2 rounds.** DMG Appendix M gives one table for both, so this conversion uses the **budget rule** to decide how many appear.

| d100 | 1e | 5e creature | CR |
|---|---|---|---|
| 01–03 | Chimera (Couatl) | Chimera (Couatl) | 6 (4) |
| 04–06 | Demon, succubus | Succubus | 4 |
| 07–09 | Demon, type I | Vrock | 6 |
| 10–12 | Demon, type II | Hezrou | 8 |
| 13–15 | Demon, type III | Glabrezu | 9 |
| 16–18 | Devil, barbed | Barbed Devil | 5 |
| 19–21 | Devil, bone | Bone Devil | 9 |
| 22–23 | Devil, horned | Horned Devil | 11 |
| 24–26 | Ettin | Ettin | 4 |
| 27–29 | Giant, fire | Fire Giant | 9 |
| 30–32 | Giant, frost | Frost Giant | 8 |
| 33–35 | Giant, hill | Hill Giant | 5 |
| 36–38 | Giant, stone | Stone Giant | 7 |
| 39–41 | Gorgon | Gorgon | 5 |
| 42–43 | Groaning spirit | Banshee | 4 |
| 44–46 | Hydra, 10 heads | 📘 Hydra (Greyhawk), 10-headed | 9 |
| 47–49 | Hydra, pyro-, 8 heads | 📘 Pyrohydra, 8-headed | 8 |
| 50–52 | Intellect devourer | Intellect Devourer | 2 |
| 53–55 | Invisible stalker | Invisible Stalker | 6 |
| 56–58 | Lamia | Lamia | 4 |
| 59–61 | Lizard, fire | 📘 Fire Lizard | 5 |
| 62–64 | Mind flayer | Mind Flayer | 7 |
| 65–67 | Mummy | Mummy | 3 |
| 68–70 | Naga, spirit | Spirit Naga | 8 |
| 71–73 | Neo-otyugh | 📘 Neo-Otyugh | 6 |
| 74–76 | Night hag | Night Hag | 5 |
| 77–79 | Roper (Shedu) | Roper (📘 Shedu) | 5 (7) |
| 80–82 | Shambling mound | Shambling Mound | 5 |
| 83–85 | Slug, giant | 📘 Giant Slug | 6 |
| 86–88 | Spectre | Specter | 1 |
| 89–91 | Sphinx, hieraco- (andro-) | 📘 Hieracosphinx (⚠️ Androsphinx) | 4 (17) |
| 92–94 | Umber hulk | Umber Hulk | 5 |
| 95–97 | Will-o'-wisp | Will-o'-Wisp | 2 |
| 98–00 | Xorn | Xorn | 5 |

**Water:** *Fresh* 01–20 Morkoth → ⚠️ Morkoth *(VGtM/MPMM, CR 11)* · 21–00 Naga, water → 📘 Water Naga (5). *Salt* 01–15 Morkoth · 16–70 Ray, manta → 📘 Manta Ray (6) · 71–00 Squid, giant → 📘 Giant Squid (9).

---

## FG notes

- Build seven spell records under **Spells**, each with a **Description** carrying its table. FG can't roll an arbitrary d100 table from a spell, so **add each table as a separate FG Table record** (`Monster Summoning IV`, rolled as d100) and link it in the spell text.
- The spell has **no damage or save line**. The power line is just the cast, and the creatures come from the NPC library.
- **📘 = a custom statblock** in [[C12 - Summoning Bestiary (5e)]], converted from the 1e *Monster Manual* (39 creatures). Every other entry is an existing 5e statblock.
- **Sourcebooks used beyond the MM:** VGtM/MPMM (Leucrotta, Jackalwere, Triton, Morkoth). Swap in an MM creature if those books aren't loaded.
