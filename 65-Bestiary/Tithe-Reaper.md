---
type: creature
adventure: "SP-BST-01"
section: bestiary
publish_order: 260
publish: true
status: drafted
creature: "Tithe-Reaper"
cr: "7"
cr_num: 7
xp: 2900
size: Medium
creature_type: undead
alignment: neutral evil
environment: [village, graveyard, farmland]
origin: harvested
base_block: "Wraith (MM p. 302)"
source_adventures: ["SP-HAL-03", "SP-HAL-04"]
tags: [bestiary, statblock, 2014-5e, villain-type]
---

# Tithe-Reaper

*He doesn't raise his voice. He looks at you the way a reeve looks at a field, counting what is owed.*

> [!example]+ Tithe-Reaper (CR 7, 2,900 XP)
> *Medium undead, neutral evil*
> **Armor Class** 14 · **Hit Points** 97 (13d8 + 39) · **Speed** 0 ft., fly 60 ft. (hover)
>
> | STR | DEX | CON | INT | WIS | CHA |
> |---|---|---|---|---|---|
> | 6 (−2) | 18 (+4) | 16 (+3) | 14 (+2) | 16 (+3) | 17 (+3) |
>
> **Damage Resistances** acid, cold, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered
> **Damage Immunities** necrotic, poison
> **Condition Immunities** charmed, exhaustion, grappled, paralyzed, petrified, poisoned, prone, restrained
> **Senses** darkvision 60 ft., passive Perception 13 · **Languages** the languages it knew in life, plus the language of each creature it has reaped · **Challenge** 7 (2,900 XP)
>
> ***Incorporeal Movement.*** The reaper can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.
>
> ***Legendary Resistance (1/Day).*** If the reaper fails a saving throw, it can choose to succeed instead.
>
> ***Sunlight Sensitivity.*** While in sunlight, the reaper has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight.
>
> ***Anchor Bone.*** Every tithe-reaper left one bone behind when it died, usually a finger. While that bone is within 30 feet of the reaper, the reaper must succeed on a DC 15 Wisdom saving throw at the start of each of its turns or use its movement to move toward the bone by the most direct route. If the bone is destroyed with fire or holy water while the reaper is within 30 feet of it, the reaper loses Legendary Resistance and Create Specter until the next dusk.
>
> **Actions**
> ***Life Drain.*** *Melee Weapon Attack:* +7 to hit, reach 5 ft., one creature. *Hit:* 22 (4d8 + 4) necrotic damage. The target must succeed on a DC 14 Constitution saving throw or its hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0.
>
> ***Create Specter.*** The reaper targets a humanoid within 10 feet of it that has been dead for no longer than 1 minute and died violently. The target's spirit rises as a **specter** (MM p. 279) in the space of its corpse or in the nearest unoccupied space. The specter is under the reaper's control. The reaper can have no more than seven specters under its control at one time.

## Lore
In the old pact-villages, someone had to collect. When a community bargained with something in the fields or the woods (a harvest lord, a threshold lord, or a god nobody names), the bargain needed a reaper to take the tithe: a lamb, a tenth of the grain, or one life every seventh year. The reaper was usually chosen from among the villagers and usually hated. When the village finally turned on its reaper (and villages always do), it hanged him, burned him, or walled him up. It also usually forgot to bury every last bone.

A tithe-reaper is what rises from that. It remembers every name in the ledger, and it means to finish the count.

## Ecology
- **Environment:** pact-villages, ossuaries, crossroads gallows, tithe barns.
- **Encountered as:** alone, often with the specters it has made. It may be bound or chained by the village that killed it, and freeing it is often the inciting incident.
- **Signs:** a tally carved into every lintel, livestock found dead in tens, and the village's oldest residents refusing to say a certain surname.

## Tactics
The reaper wants three things in order: its anchor bone, the instrument of its death (the rope, the stake, the trowel), and the road out of the village. It drains whoever stands between it and those things and raises each victim to stand guard. It speaks to one PC by a name only their dead kin used, to unsettle them. It retreats from sunlight and avoids fighting near its own bone.

## Named Example
**Josiah Thorne** ([[Josiah Thorne]]). He is the Tithe-Reaper of [[SP-HAL-03-The-Night-That-Doesnt-End]] and returns in [[SP-HAL-04-The-Tithe-of-Thornbury]]. Unique to him:
- **Chained (until the first toll).** While chained in the Chain Crypt, he can't move or attack. Each grave-iron link has AC 19 and 50 hit points, and two links hold him.
- **The Bone Circle.** If his anchor bone lies at the center of the Bone Circle and he is inside the circle when the twelfth toll sounds, he is restrained until the end of the following round.
- His Create Specter targets only creatures that died in the ossuary during the current loop.

## Adventure Hooks
1. Grave-robbers broke into the old gallows-pit for the hangman's rope. Now the tithe ledger is open again, and the first name on it is a PC's.
2. A village has paid its tithe for a hundred years to keep its reaper chained. This year it can't pay.
3. A scholar wants the party to retrieve a tithe-reaper's anchor bone for study. The reaper wants it back more.

## Spoils
A destroyed reaper leaves its ledger, a rotted book naming every life it collected. Returned to the families, it lays the reaper's specters to rest. The village also owes the party a debt it won't want to acknowledge.

## Design Notes
**Changes from the Wraith block:** AC 14 (from 13); 97 hp (from 67); Dex 18, Wis 16, and Cha 17; Life Drain at +7 for 4d8 + 4; Legendary Resistance 1/day; and Anchor Bone added.

**Errata against SP-HAL-03.** The adventure's block prints 99 (18d8 + 18) hp, Dex 16, and a Life Drain save of DC 15. Those numbers don't agree with its own ability scores. Dex 18 is what makes AC 14, +7 to hit, and +4 damage consistent, and 13d8 + 39 = 97 is the closest valid hit point total for Con 16. The Con-based save DC is 8 + 3 + 3 = 14. This entry uses the corrected numbers. The adventure still needs the same fix, which is logged for its next edit pass.

**CR verification (DMG p. 274):** *Defensive:* 97 hp × 1.5 (broad resistances at expected CR 5–10) is about 146, plus 20 for Legendary Resistance (1/day), which gives about 166 effective hp. That is the CR 7 band (161–175). AC 14 is one below the expected 15, so defensive CR is about **6.5**. *Offensive:* Life Drain deals 22 damage per round, which is the CR 3 band (21–26). +7 to hit is three above the expected +4, so offensive CR is about **4.5**. *Average:* about 5.5, so the math gives **CR 6**. **It is published at CR 7 (2,900 XP)** because Create Specter turns every death near it into another attacker, which the formula doesn't count. Where nobody can die near it (for example, a chained or warded reaper), price the encounter at CR 6 (2,300 XP).

## Appears In
- [[SP-HAL-03-The-Night-That-Doesnt-End]]: Scenes 04–05, as the villain. Statblocks are in [[SP-HAL-03 — Bestiary]].
- [[SP-HAL-04-The-Tithe-of-Thornbury]]: Scenes 04–05, if he is free (Halloween bundle only).

## Art Prompt
```
A gaunt hovering wraith in the rotted black coat and broad hat of a village tithe-collector, a frayed hangman's rope still knotted at its throat, one finger missing from its long grey hand, a ledger chained to its belt, drifting above an ossuary floor of stacked bones, naturalist field-guide plate, a single creature studied in full on a plain warm parchment ground, oil on board, muted umber, bone, moss and slate palette, soft overcast light, eerie and restrained, folk-horror mood, no text --ar 3:4 --v 8.1 --style raw --seed 26500
```
