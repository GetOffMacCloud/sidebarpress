---
tags: [adventure/C12, fgu-prep]
adventure: "C12 - The Forgotten Library of Raanet"
status: ready-to-import
created: 2026-11-15
publish: false
---
# C12 - FG Item Import (companion notes)

**The paste file:** `C12 - FG Item Import.txt` in this folder, for the **5E Custom Item Importer → List Import**. **58 items**, `Version: Legacy`.

Machine-checked: every label is one of the importer's nineteen, there are no duplicate labels or names, every `Description:` is on one line, and the text is pure ASCII.

| Group | Count | What |
|---|---|---|
| Module magic and plot items | 26 | The custom items, the Xuel antique weapons and armor, the Sigil rods (charged and quiescent), the medallion, the *Monster Summoning IV* scroll and *Avraasha's Ember* |
| Pregen items | 9 | Horn of Acheron, Ruby Skull, Gnome-Forged Halberd +1, Potion of Rainbow Hues, The Sorceress' Gaze, Handaxe of Hurling +1, Horn of Fog, Helm of Comprehending Languages and Reading Magic, Moonsight |
| Treasure (gems, art, goods) | 23 | Every priced treasure in the dungeon, for the parcels. Quantities are in each `DM Only:` line |

## ⚠️ Before the batch: import two items first

The importer publishes **no list of valid `Type` values**. These types are used here: `Weapon`, `Armor`, `Wondrous Item`, `Ring`, `Wand`, `Potion`, `Scroll`, plus two that may not be recognised: **`Treasure`** and **`Adventuring Gear`**.

**Import `Xuel Gold Coin` (Treasure) and `Robe of Raanet's Faithful` (Adventuring Gear) on their own first**, and check which list they land in. If either goes astray, find-and-replace that type across the file before the full paste.

Armor carries **no `Dex Bonus:` line**, because its value format isn't documented. Set it on the sheet: the Castellan's Breastplate and the Xuel Chain Shirt are medium armor (Dex max 2).

## Use FG's own records for these (not in the file)

Bracers of defense · ring of protection ×2 (Areas 10 and 20; the Area 25 holy symbol is custom, above) · ring of warmth · potion of greater healing · cloak of protection · gauntlets of ogre power · robe of scintillating colors · decanter of endless water · dust of disappearance (**set 5 uses**) · hat of disguise · Nolzur's marvelous pigments (**set 3 pots**) · ring of resistance (fire) · brooch of shielding · **Spell Scroll** ×4 (comprehend languages, contact other plane, slow, wall of stone).

**Pregen gear FG already ships:** elven chain (Adria), chain mail +1, leather armor +1, shield +1, longsword +1, arrow +2, potion of healing, potion of diminution, potion of gaseous form, potion of resistance (fire), bracers of defense, ring of protection.

## Things the importer can't carry

- **Attunement:** there's no field for it, so it's written at the start of each `Description:`. Tick the box on the sheet.
- **Charges:** set them on the sheet. Wand of Ice Storm **10**; Alabaster Wand of Fire **5** (max 7); dust of disappearance **5**.
- **Effects:** the importer carries no effect strings. Paste these by hand:

| Item | Effect | Exact for / over-applies to |
|---|---|---|
| Holy Symbol of Raanet | `Holy Symbol of Raanet; AC: 1; SAVE: 1` | Exact (verified keywords). Only add it for a devotee of Raanet |
| Xuel Luckstone (devotee) | `Luckstone; SAVE: 1; CHECK: 1` | Exact for a Suel worshipper. For anyone else use the label `Stone of weight - speed -10 ft, cursed` |
| Ornate Silver Dagger -1 | (none needed) | The `Bonus: -1` field already applies the penalty. Add the label `Cursed - can't discard; always drawn` |
| Castellan's Raptor Helm | `See invisibility 30 ft (3/day, with the Breastplate)` | Label |
| Lyre of Building | `Lyre - d20: 1-4 false chord (1 if proficient; 1-10 if disturbed)` | Label |
