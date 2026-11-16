---
tags: [adventure/C12, fgu-prep]
adventure: "C12 - The Forgotten Library of Raanet"
status: ready-to-import
created: 2026-11-15
publish: false
---
# C12 - FG NPC Import (companion notes)

**The paste file:** `C12 - FG NPC Import.txt` in this folder. **55 NPCs**, plain ASCII, 2014/MotM profile, one block per creature.
- **Part 1:** the 16 C12 module creatures, in area order.
- **Part 2:** the 39 Monster Summoning creatures.

**Generated, not hand-typed.** The blocks were parsed straight from the statblock callouts in [[C12 - 5e Conversion Ledger]] and [[C12 - Summoning Bestiary (5e)]]. Then they were machine-checked: ASCII only, no blank lines, the six-score row present, every ability modifier correct, and **every damage average matching its dice**. 0 errors. The nine "as X, with changes" creatures (the koalinth, lacedon, kopoacinth, the three larger hydras, pyrohydra and neo-otyugh) and the eight module NPCs built on SRD creatures were written out in full.

## How to import

FG → **NPCs** → **Import** → paste **one** block, from the name line down to the line before the next `####` header. Never paste the `####` lines. **Import one creature first** (Magman is a good test) and open it before running the rest.

## Use FG's own records for these (not in the file)

| Creature | Where | Use |
|---|---|---|
| Salamander ×4 | Area 22 (2 more if A21's alarm fires) | SRD / MM **Salamander**, unchanged |
| Efreeti (wandering, 01-05) | Temple wandering table | SRD **Efreeti**, unchanged. It's a second efreeti, not Yox |
| Fire Elemental (wandering) | Temple wandering table | SRD **Fire Elemental** |
| Wight, Wraith | Only if you'd rather not use the C12 versions | The C12 versions are in the file: claws instead of a sword and bow, no Create Specter |
| Everything else on the summoning tables | MS I-VII | SRD / MM / *Volo's* records, as named in [[C12 - Monster Summoning I-VII (5e)]] |

## Check these after import (the parser may misread them)

| NPC | Line | What to check |
|---|---|---|
| **Naskin, Yrsi** | Martial Fury | The importer has no Bonus Actions header, so Martial Fury imports as an action labelled **(Bonus Action)**. Run it as a bonus action. If you own FG's *Tome of Foes* or *Monsters of the Multiverse* module, you can instead drag its Sword Wraith Commander / Warrior and swap in the gear (AC 18, longsword +2). |
| **Stone Guardian** | Damage Resistances | "cold, fire, and lightning damage **from spells**." FG may apply that to all cold, fire and lightning. Edit to match, or adjudicate. |
| **Wind Walker** | Damage Immunities | "all damage except as noted under Ethereal Wind" **won't parse.** Leave immunities empty and run the trait by hand. |
| **Avraasha, Yox** | Innate Spellcasting | Confirm the spell lines became clickable powers. Avraasha's *fireball* must be set to 12d6 (cast at 7th level). |
| **Avraasha** | Legendary Actions | Confirm all three options imported. |
| **The four hydras** | Multiattack | FG makes one bite entry. Roll it once per remaining head. |
| **Keeper-of-the-Hearth, Air Elemental of the Retreat** | Attacks | "Maddened" is already built into their lower attack bonuses (+4 and +6). Don't add a penalty on top. |

## Tracker effects

**Only one line here uses a verified FG keyword.** Everything else is a **label-only effect**: a string with no keyword, which FG displays and never applies. It can't fail silently, and the table can see a state the DM is running by hand.

| NPC / place | Effect string | Notes |
|---|---|---|
| Caryatid Column | `Warded Stone; SAVE: 4` | ✅ verified keyword. Exact: +4 to all its saves |
| Caryatid Column | `Dampening Stone - magic weapon bonus doesn't apply` | Label. Subtract the weapon's plus by hand |
| Caryatid Column | `Weapon Breaker - d20 on hit: mundane 1-5, +1 1-4, +2 1-3, +3 1-2, +4 1` | Label |
| Magman | `Melting Body - nonmagical/+1 weapon that hits: permanent -1 damage` | Label. Track on the PC's weapon |
| Magman (on a PC) | `Burning - 1d8 fire at start of turn, 1d4+2 rounds (action to douse)` | Label, on the burning PC |
| Harginn Grue | `Flame Eater - fire spells and magical fire within 20 ft dispelled` | Label |
| Harginn Grue | `Blinking - attacks against it have disadvantage` | Label. FG's `GRANTDISATK` isn't on the verified list, so it's adjudicated |
| Fire Bat (on a PC) | `Fire bat attached - 5 (2d4) fire at start of bat's turn, rounds 1-3` | Label |
| Giant Tick (on a PC) | `Tick attached - lose 7 (2d6) HP at start of tick's turn (max 14)` | Label |
| Naskin, Yrsi | `Martial Fury - attacks against it have advantage until its next turn` | Label. `GRANTADVATK` would do it, but it isn't on the verified list |
| Phantom Stalker | `Fire Absorption - fire heals 1 HP per die` | Label |
| Hydras | `Heads remaining - N (lose 1 per 18 damage)` | Label. Update N as it takes damage |
| Avraasha | `Regeneration 10 - start of turn while touching fire/magma` | Label (`REGEN:` not verified) |
| Avraasha | `Calming - DC 22 Persuasion; +3 Xuel present, +2 name, +2 Raanet, +2 scripture` | Label, as a reminder |
| Area 21 (on PCs) | `Area 21 heat - 1d6 fire at start of turn; disadvantage on Con saves` | Label. Fire resistance negates it |
| Area 22 (on PCs) | `Illusory fire - 1d6 psychic at start of turn until disbelieved (DC 16 Investigation)` | Label |
| Sigil rod (on its wielder) | `Quiescent rod - a hit on an eligible fire creature destroys it, no save` | Label. Eligible: Keeper, Ranzaar, Yox, Ixthasus |
| Wind Walker | `Ethereal Wind - only elementals/genies/stalkers harm it; slow 8d6, haste 4d6` | Label |
