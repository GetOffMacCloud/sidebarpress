---
publish: true
permalink: /greyhawk-university/compendium
description: "The Compendium — bestiary, house rules, items, and spells of Greyhawk University and the Flanaess."
tags: [university, compendium]
---

# ⚔️ The Compendium

*The working reference shelf of Greyhawk University — every creature catalogued by field teams, every house rule in force at the table, and the growing archive of items and spells recovered from the Flanaess.*

---

## 🐺 Bestiary

*Homebrew creatures of the Sepia Uplands and the Quag Mires. New entries created from the Creature Template appear here automatically.*

%% DATAVIEW_PUBLISHER: start
```dataview
TABLE creature-type AS "Type", challenge-rating AS "CR", environment AS "Environment"
FROM #bestiary
WHERE publish = true
SORT challenge-rating ASC
```
%%

| File                                                                    | Type                                                           | CR | Environment |
| ----------------------------------------------------------------------- | -------------------------------------------------------------- | -- | ----------- |
| [[z_Templates/5_GHU Templates/Creature Template.md\|Creature Template]] | {{Beast / Elemental / Humanoid / Monstrosity / Undead / etc.}} | 0  | <ul></ul>   |

%% DATAVIEW_PUBLISHER: end %%
> [!note]- Manual index (fallback if Dataview is off)
> [[3-Mechanics/Bestiary/homebrew/Alpha Wolf]] · [[Dust Elemental]] · [[Fiendish Mount]] · [[Greater Swamp Swarm]] · [[Hunting Tiger]] · [[Ice Elemental]] · [[Thunder Hoof Centaur]] · [[Wolfling]]

---

## 📜 House Rules

*The rulings that shape play at Greyhawk University. These override or extend the core rules.*

| Rule | Covers |
|:---|:---|
| [[Campaign House Rules]] | The master list of table rulings |
| [[Morale Checks]] | When and how enemies break and flee |
| [[Spell Strain]] | The cost of pushing magic too far |

---

## 🎒 Items

*Magic items, relics, and notable gear recovered in the field.*

> [!abstract] Coming soon
> Item entries are being catalogued. The campaign relic — the **[[Fiend's Embrace]]** — is the first of the archive.

---

## ✨ Spells

*Homebrew and regionally-flavored spells of the Flanaess.*

> [!abstract] Coming soon
> Spell entries tied to the [[Spell Strain]] system and University departments are in preparation.

---

> [!info] Back to [[Greyhawk University Home|🗺️ The Chronicles of Oerth]]
