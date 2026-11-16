---
title: C12 - FG NPC Import (copy blocks)
tags: [c12, fgu, npc-import]
---

# C12 – FG NPC Import, one block per NPC

Fantasy Grounds' NPC importer takes one creature at a time. Each NPC below sits in its own code block: hover the block and click the copy icon, then paste it into **NPCs → Import** in FG and click **Import**.

**55 NPCs.** Source file: [[C12 - FG NPC Import.txt]]. After importing, run the checks in [[C12 - FG NPC Import (companion notes)]].

> [!tip] Not in this list
> Creatures that use Fantasy Grounds' own records (the A22 salamanders, the wandering efreeti, a summoned fire elemental and the like) aren't here. See the companion notes for the full list.

## Contents

- [[#01 Keeper-of-the-Hearth (Area 3)]]
- [[#02 Caryatid Column (Areas 4-5)]]
- [[#03 Wraith of the Oubliette (Area 9)]]
- [[#04 Magman (Areas 10, 11, 23, 28; wandering)]]
- [[#05 Air Elemental of the Retreat (Area 12)]]
- [[#06 Harginn Grue (Area 13; wandering)]]
- [[#07 Ranzaar (Area 15)]]
- [[#08 Fire Bat (Area 16; wandering)]]
- [[#09 Phantom Stalker (Area 19; wandering)]]
- [[#10 Ixthasus, Greater Salamander (Area 21)]]
- [[#11 Stone Guardian (Area 25)]]
- [[#12 Wight of the Cornucopia (Area 30)]]
- [[#13 Naskin ad-Laar (Area 32)]]
- [[#14 Yrsi ad-Laar (Area 32)]]
- [[#15 Yox (Area 33)]]
- [[#16 Avraasha, the First Servant (Area 35)]]
- [[#17 Dwarf (summoned)]]
- [[#18 Elf (summoned)]]
- [[#19 Gnome (summoned)]]
- [[#20 Halfling (summoned)]]
- [[#21 Koalinth]]
- [[#22 Nixie]]
- [[#23 Ixitxachitl]]
- [[#24 Locathah]]
- [[#25 Boring Beetle]]
- [[#26 Giant Tick]]
- [[#27 Huge Spider]]
- [[#28 Lacedon]]
- [[#29 Carnivorous Ape]]
- [[#30 Ice Toad]]
- [[#31 Poisonous Toad]]
- [[#32 Hydra (Greyhawk), 5-headed]]
- [[#33 Giant Water Beetle]]
- [[#34 Giant Crayfish]]
- [[#35 Kopoacinth]]
- [[#36 Giant Water Spider]]
- [[#37 Hydra (Greyhawk), 7-headed]]
- [[#38 Subterranean Lizard]]
- [[#39 Giant Amphisbaena]]
- [[#40 Giant Spitting Snake]]
- [[#41 Sea Lion]]
- [[#42 Hydra (Greyhawk), 8-headed]]
- [[#43 Lammasu]]
- [[#44 Wind Walker]]
- [[#45 Giant Sea Snake]]
- [[#46 Hydra (Greyhawk), 10-headed]]
- [[#47 Pyrohydra, 8-headed]]
- [[#48 Fire Lizard]]
- [[#49 Neo-Otyugh]]
- [[#50 Shedu]]
- [[#51 Giant Slug]]
- [[#52 Hieracosphinx]]
- [[#53 Water Naga]]
- [[#54 Manta Ray]]
- [[#55 Giant Squid]]

# Part 1 · Module creatures (Areas 3–35)

## 01 Keeper-of-the-Hearth (Area 3)

```text
Keeper-of-the-Hearth
Large elemental, neutral
Armor Class 13
Hit Points 102 (12d10 + 36)
Speed 50 ft.
STR DEX CON INT WIS CHA
10 (+0) 17 (+3) 16 (+3) 6 (-2) 10 (+0) 7 (-2)
Damage Resistances bludgeoning, piercing, and slashing from nonmagical attacks
Damage Immunities fire, poison
Condition Immunities exhaustion, grappled, paralyzed, petrified, poisoned, prone, restrained, unconscious
Senses darkvision 60 ft., passive Perception 10
Languages Ignan
Challenge 5 (1,800 XP)
Fire Form. The elemental can move through a space as narrow as 1 inch wide without squeezing. A creature that touches the elemental or hits it with a melee attack while within 5 feet of it takes 5 (1d10) fire damage. In addition, the elemental can enter a hostile creature's space and stop there. The first time it enters a creature's space on a turn, that creature takes 5 (1d10) fire damage and catches fire; until someone takes an action to douse the fire, the creature takes 5 (1d10) fire damage at the start of each of its turns.
Illumination. The elemental sheds bright light in a 30-foot radius and dim light in an additional 30 feet.
Water Susceptibility. For every 5 feet the elemental moves in water, or for every gallon of water splashed on it, it takes 1 cold damage.
Maddened. Six centuries alone have driven it mad. It attacks anyone who enters the Welcome Hearth, and its attacks are wild (+4 to hit rather than +6).
Actions
Multiattack. The elemental makes two touch attacks.
Touch. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) fire damage. If the target is a creature or a flammable object, it ignites. Until a creature takes an action to douse the fire, the target takes 5 (1d10) fire damage at the start of each of its turns.
```

## 02 Caryatid Column (Areas 4-5)

```text
Caryatid Column
Medium construct, unaligned
Armor Class 14 (natural armor)
Hit Points 33 (6d8 + 6)
Speed 15 ft.
STR DEX CON INT WIS CHA
16 (+3) 10 (+0) 13 (+1) 3 (-4) 10 (+0) 1 (-5)
Damage Resistances bludgeoning, piercing, and slashing from nonmagical attacks
Damage Immunities poison, psychic
Condition Immunities charmed, exhaustion, frightened, paralyzed, petrified, poisoned
Senses darkvision 60 ft., passive Perception 10
Languages understands Ancient Suloise but can't speak
Challenge 2 (450 XP)
False Appearance. While motionless, it is indistinguishable from a marble statue.
Dampening Stone. A magic weapon that hits the column deals its normal damage dice, but its bonus to attack and damage rolls doesn't apply.
Weapon Breaker. When a weapon hits the column, roll a d20. It snaps on 1-5 if nonmagical, 1-4 if +1, 1-3 if +2, 1-2 if +3, or a 1 if +4. A magic weapon with no bonus counts as +1; artifacts never break.
Robe-Bound. The column does not attack a creature wearing the robes of Raanet's faithful, or a creature accompanied by one.
Warded Stone. The column adds +4 to every saving throw.
Task-Bound. It acts only to carry out its guarding task. It won't pursue beyond its alcove and hall. When its task ends (intruders dead or gone), it returns to its place and reverts to stone, and so does its sword. If destroyed, it turns back to stone.
Actions
Concealed Sword. Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 9 (1d8 + 5) slashing damage.
```

## 03 Wraith of the Oubliette (Area 9)

```text
Wraith of the Oubliette
Medium undead, neutral evil
Armor Class 13
Hit Points 67 (9d8 + 27)
Speed 0 ft., fly 60 ft. (hover)
STR DEX CON INT WIS CHA
6 (-2) 16 (+3) 16 (+3) 12 (+1) 14 (+2) 15 (+2)
Damage Resistances acid, cold, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered
Damage Immunities necrotic, poison
Condition Immunities charmed, exhaustion, grappled, paralyzed, petrified, poisoned, prone, restrained
Senses darkvision 60 ft., passive Perception 12
Languages Ancient Suloise
Challenge 5 (1,800 XP)
Incorporeal Movement. The wraith can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.
Sunlight Sensitivity. While in sunlight, the wraith has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight.
Actions
Life Drain. Melee Weapon Attack: +6 to hit, reach 5 ft., one creature. Hit: 21 (4d8 + 3) necrotic damage. The target must succeed on a DC 14 Constitution saving throw or its hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0.
```

## 04 Magman (Areas 10, 11, 23, 28; wandering)

```text
Magman
Small elemental, chaotic neutral
Armor Class 13 (natural armor)
Hit Points 26 (4d6 + 12)
Speed 25 ft., swim 15 ft. (lava and magma only)
STR DEX CON INT WIS CHA
14 (+2) 12 (+1) 16 (+3) 6 (-2) 10 (+0) 6 (-2)
Damage Resistances bludgeoning, piercing, and slashing from nonmagical attacks
Damage Immunities fire
Senses darkvision 60 ft., passive Perception 10
Languages understands Ignan but speaks no Prime language
Challenge 1 (200 XP)
Melting Body. A nonmagical weapon, or a weapon with a +1 bonus, that hits the magman melts: after dealing damage it takes a permanent, cumulative -1 penalty to damage rolls, and it is destroyed when the penalty reaches -5. Nonmagical ammunition that hits is destroyed.
Combustion. Flammable objects the magman touches that aren't being worn or carried catch fire.
Bonfire Heat. It radiates heat like a small bonfire and sheds dim light for 10 ft.
Lava-Bound. Out of lava for more than 6 hours, it stiffens and can't move until returned to it.
Actions
Combustion Touch. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 13 (3d8) fire damage. A creature hit catches fire: it takes 4 (1d8) fire damage at the start of each of its turns for 1d4 + 2 rounds, or until it or a creature within reach spends an action to put the flames out. Flammable gear it carries burns too.
```

## 05 Air Elemental of the Retreat (Area 12)

```text
Air Elemental of the Retreat
Large elemental, neutral
Armor Class 15
Hit Points 90 (12d10 + 24)
Speed 0 ft., fly 90 ft. (hover)
STR DEX CON INT WIS CHA
14 (+2) 20 (+5) 14 (+2) 6 (-2) 10 (+0) 6 (-2)
Damage Resistances lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks
Damage Immunities poison
Condition Immunities exhaustion, grappled, paralyzed, petrified, poisoned, prone, restrained, unconscious
Senses darkvision 60 ft., passive Perception 10
Languages Auran
Challenge 5 (1,800 XP)
Air Form. The elemental can enter a hostile creature's space and stop there. It can move through a space as narrow as 1 inch wide without squeezing.
Maddened. Six centuries of cleaning the Temple's air alone have driven it mad. It won't pursue anyone who leaves the Retreat, and its attacks are wild (+6 to hit rather than +8).
Actions
Multiattack. The elemental makes two slam attacks.
Slam. Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) bludgeoning damage.
Whirlwind (Recharge 4-6). Each creature in the elemental's space must make a DC 13 Strength saving throw. On a failure, a target takes 15 (3d8 + 2) bludgeoning damage and is flung up to 20 feet away from the elemental in a random direction and knocked prone. If a thrown target strikes an object, such as a wall or floor, the target takes 3 (1d6) bludgeoning damage for every 10 feet it was thrown. If the target is thrown at another creature, that creature must succeed on a DC 13 Dexterity saving throw or take the same damage and be knocked prone. If the saving throw is successful, the target takes half the bludgeoning damage and isn't flung away or knocked prone.
```

## 06 Harginn Grue (Area 13; wandering)

```text
Harginn Grue
Medium elemental (shapechanger), neutral evil
Armor Class 15 (natural armor)
Hit Points 39 (6d8 + 12)
Speed 50 ft.
STR DEX CON INT WIS CHA
16 (+3) 16 (+3) 14 (+2) 12 (+1) 12 (+1) 8 (-1)
Damage Resistances bludgeoning, piercing, and slashing from nonmagical attacks
Damage Immunities fire
Senses darkvision 60 ft., passive Perception 11
Languages Ignan
Challenge 2 (450 XP)
Flame Eater. The grue is immune to spells that deal fire damage. Any fire spell or magical fire effect within 20 ft of the grue is dispelled, even a permanent one (such as wall of fire, flaming sphere or a fire trap). A spell cast with the grue in its area or as its target simply fails. Fire from magic items is unaffected.
Shapechanger. As an action, it takes the form of a bonfire, an 8-ft column of fire, a flame-legged humanoid (its true form) or a bronze statue. While motionless as a bonfire or statue, it is indistinguishable from the real thing.
Blinking. The grue flickers in and out of sight. Attack rolls against it have disadvantage unless it is incapacitated.
Actions
Gout of Flame. A gout of fire from its fingertips fills a 5-ft-wide, 10-ft line. Each creature in it makes a DC 13 Dexterity saving throw, taking 10 (2d6 + 3) fire damage on a failure or half as much on a success.
```

## 07 Ranzaar (Area 15)

```text
Ranzaar
Large elemental, neutral
Armor Class 13
Hit Points 102 (12d10 + 36)
Speed 50 ft.
STR DEX CON INT WIS CHA
10 (+0) 17 (+3) 16 (+3) 6 (-2) 10 (+0) 7 (-2)
Damage Resistances bludgeoning, piercing, and slashing from nonmagical attacks
Damage Immunities fire, poison
Condition Immunities exhaustion, grappled, paralyzed, petrified, poisoned, prone, restrained, unconscious
Senses darkvision 60 ft., passive Perception 10
Languages Ignan
Challenge 5 (1,800 XP)
Fire Form. The elemental can move through a space as narrow as 1 inch wide without squeezing. A creature that touches the elemental or hits it with a melee attack while within 5 feet of it takes 5 (1d10) fire damage. In addition, the elemental can enter a hostile creature's space and stop there. The first time it enters a creature's space on a turn, that creature takes 5 (1d10) fire damage and catches fire; until someone takes an action to douse the fire, the creature takes 5 (1d10) fire damage at the start of each of its turns.
Illumination. The elemental sheds bright light in a 30-foot radius and dim light in an additional 30 feet.
Water Susceptibility. For every 5 feet the elemental moves in water, or for every gallon of water splashed on it, it takes 1 cold damage.
Actions
Multiattack. The elemental makes two touch attacks.
Touch. Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) fire damage. If the target is a creature or a flammable object, it ignites. Until a creature takes an action to douse the fire, the target takes 5 (1d10) fire damage at the start of each of its turns.
```

## 08 Fire Bat (Area 16; wandering)

```text
Fire Bat
Small elemental, neutral evil
Armor Class 12
Hit Points 11 (2d6 + 4)
Speed 5 ft., fly 60 ft.
STR DEX CON INT WIS CHA
6 (-2) 15 (+2) 14 (+2) 6 (-2) 12 (+1) 6 (-2)
Damage Immunities fire
Senses blindsight 60 ft. (sees invisible creatures), darkvision 60 ft., passive Perception 11
Languages -
Challenge 1/4 (50 XP)
Flyby. The bat doesn't provoke opportunity attacks when it flies out of an enemy's reach.
Echolocation. The bat can't use its blindsight while deafened.
Pack Hunters. The colony spreads its attacks evenly across a group. When fewer than a quarter of the starting bats remain, the rest flee to their lair; cornered there, they fight to the death.
Doused. At least 10 gallons of cool water on one bat (create or destroy water is enough) puts it out for 10 rounds: it can't fly, and its bite deals only 2 (1d4) fire damage.
Return to Fire. When it dies, it bursts into flame and its body vanishes back to the Elemental Plane of Fire.
Actions
Burning Bite. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (2d4) fire damage, and the bat attaches. While attached it doesn't attack; instead, at the start of each of its turns, the target automatically takes 5 (2d4) fire damage from burning and blood loss. After two such turns (three rounds of damage in all) it drops off, sated, and flies home. A creature can pull it off with an action and a DC 12 Strength check.
```

## 09 Phantom Stalker (Area 19; wandering)

```text
Phantom Stalker
Large elemental, neutral evil
Armor Class 16 (natural armor)
Hit Points 52 (7d10 + 14)
Speed 30 ft., fly 60 ft.
STR DEX CON INT WIS CHA
18 (+4) 14 (+2) 15 (+2) 8 (-1) 12 (+1) 8 (-1)
Damage Vulnerabilities cold
Damage Immunities fire, poison
Condition Immunities exhaustion, poisoned
Senses darkvision 60 ft., passive Perception 11
Languages Ignan, understands Ancient Suloise
Challenge 3 (700 XP)
Fire Absorption. Whenever the stalker would take fire damage, it takes none and instead regains 1 hit point per damage die.
Shapechanger. As an action, the stalker polymorphs into a Large or smaller beast or humanoid, or back into its true form. Its statistics don't change. It reverts on death.
Medallion-Bound. If ad-Dax's medallion is destroyed, the stalker dies instantly.
Bound Bodyguard. A phantom stalker serves its summoner and obeys orders to the letter. If its summoner is slain, it vanishes, returns 1d4 hours later and hunts the slayer through the Ethereal Plane.
Unseen Vigil. As an action, the stalker becomes invisible until it attacks or uses Self-Immolation.
Actions
Multiattack. The stalker makes two claw attacks.
Claw. Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) slashing damage.
Self-Immolation. Usable only when the stalker has 15 hit points or fewer. The stalker explodes and dies. Each creature within 20 feet of it makes a DC 13 Dexterity saving throw, taking 28 (8d6) fire damage on a failure or half as much on a success. Other phantom stalkers in the area regain 8 hit points (Fire Absorption).
```

## 10 Ixthasus, Greater Salamander (Area 21)

```text
Ixthasus, Greater Salamander
Large elemental, chaotic evil
Armor Class 17 (natural armor)
Hit Points 136 (16d10 + 48)
Speed 30 ft.
STR DEX CON INT WIS CHA
20 (+5) 14 (+2) 17 (+3) 16 (+3) 12 (+1) 14 (+2)
Skills Perception +5
Damage Vulnerabilities cold
Damage Resistances bludgeoning, piercing, and slashing from nonmagical attacks
Damage Immunities fire
Condition Immunities charmed, paralyzed; magic can't put it to sleep
Senses darkvision 60 ft., passive Perception 15
Languages Ignan, Common
Challenge 10 (5,900 XP)
Heated Body. A creature that touches Ixthasus or hits it with a melee attack while within 5 feet of it takes 7 (2d6) fire damage.
Lava Shaper. Ixthasus can turn stone it touches into lava at a rate of one 5-foot square per minute.
Actions
Multiattack. Ixthasus makes one trident attack and one tail attack.
Trident +3. Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 15 (2d6 + 8) piercing damage plus 7 (2d6) fire damage.
Tail. Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 12 (2d6 + 5) bludgeoning damage plus 7 (2d6) fire damage, and the target is grappled (escape DC 15). Until the grapple ends, the target is restrained, Ixthasus can automatically hit it with its tail, and it can't make tail attacks against other targets.
Magma Spray (Recharge 5-6). Ixthasus sprays lava in a 60-foot cone. Each creature in the cone makes a DC 15 Dexterity saving throw, taking 45 (10d8) fire damage on a failure or half as much on a success.
```

## 11 Stone Guardian (Area 25)

```text
Stone Guardian
Medium construct, unaligned
Armor Class 17 (natural armor)
Hit Points 45 (6d8 + 18)
Speed 25 ft.
STR DEX CON INT WIS CHA
18 (+4) 8 (-1) 16 (+3) 3 (-4) 10 (+0) 1 (-5)
Damage Resistances piercing and slashing; cold, fire, and lightning damage from spells
Damage Immunities poison, psychic; damage from nonmagical ranged weapon attacks
Condition Immunities charmed, exhaustion, frightened, paralyzed, petrified, poisoned
Senses darkvision 60 ft., sees invisible creatures, passive Perception 10
Languages -
Challenge 3 (700 XP)
Mosaic Body. The guardian forms from the floor mosaic in 1 round when its trigger is met. It won't leave the room.
Mindless. It never makes Intelligence, Wisdom or Charisma saving throws against charm, fear, hold or paralysis effects; they simply fail.
Stone Vulnerability. Stone to flesh (or flesh to stone reversed), transmute rock (to mud), stone shape, and any spell that digs through stone destroy it instantly.
Fails to Heed. When it first animates, roll a d10. On a 1-2 it ignores its instructions and attacks every creature in sight, Xuel or not.
Actions
Multiattack. The guardian makes two fist attacks.
Fist. Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) bludgeoning damage.
```

## 12 Wight of the Cornucopia (Area 30)

```text
Wight of the Cornucopia
Medium undead, neutral evil
Armor Class 14 (natural armor)
Hit Points 45 (6d8 + 18)
Speed 30 ft.
STR DEX CON INT WIS CHA
15 (+2) 14 (+2) 16 (+3) 10 (+0) 13 (+1) 15 (+2)
Skills Perception +3, Stealth +4
Damage Resistances necrotic; bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered
Damage Immunities poison
Condition Immunities exhaustion, poisoned
Senses darkvision 60 ft., passive Perception 13
Languages Ancient Suloise
Challenge 3 (700 XP)
Sunlight Sensitivity. While in sunlight, the wight has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight.
Actions
Multiattack. The wight makes two claw attacks. It can use its Life Drain in place of one claw attack.
Life Drain. Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 5 (1d6 + 2) necrotic damage. The target must succeed on a DC 13 Constitution saving throw or its hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0.
Claw. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage.
```

## 13 Naskin ad-Laar (Area 32)

```text
Naskin ad-Laar
Medium undead, lawful evil
Armor Class 18 (chain shirt +1, shield)
Hit Points 127 (15d8 + 60)
Speed 30 ft.
STR DEX CON INT WIS CHA
18 (+4) 14 (+2) 18 (+4) 11 (+0) 12 (+1) 14 (+2)
Skills Perception +4
Damage Resistances necrotic; bludgeoning, piercing, and slashing from nonmagical attacks
Damage Immunities poison
Condition Immunities exhaustion, frightened, poisoned, unconscious
Senses darkvision 60 ft., passive Perception 14
Languages Ancient Suloise
Challenge 8 (3,900 XP)
Turning Defiance. Naskin and any sword wraiths within 30 feet of him have advantage on saving throws against effects that turn undead.
Barricade. If warned, the sword wraiths tip the dresser for half cover (+2 AC) and use their bows.
Actions
Multiattack. Naskin makes two longsword or longbow attacks.
Longsword +2. Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 10 (1d8 + 6) slashing damage.
Longbow. Ranged Weapon Attack: +5 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage.
Martial Fury (Bonus Action). Naskin makes one longsword or longbow attack, which deals an extra 9 (2d8) necrotic damage on a hit. Attack rolls against him have advantage until the start of his next turn.
```

## 14 Yrsi ad-Laar (Area 32)

```text
Yrsi ad-Laar
Medium undead, lawful evil
Armor Class 18 (chain shirt, shield +2)
Hit Points 45 (6d8 + 18)
Speed 30 ft.
STR DEX CON INT WIS CHA
18 (+4) 12 (+1) 17 (+3) 6 (-2) 9 (-1) 10 (+0)
Damage Resistances necrotic; bludgeoning, piercing, and slashing from nonmagical attacks
Damage Immunities poison
Condition Immunities exhaustion, frightened, poisoned, unconscious
Senses darkvision 60 ft., passive Perception 9
Languages Ancient Suloise
Challenge 3 (700 XP)
Barricade. If warned, the sword wraiths tip the dresser for half cover (+2 AC) and use their bows.
Actions
Longsword +2. Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 10 (1d8 + 6) slashing damage.
Longbow. Ranged Weapon Attack: +3 to hit, range 150/600 ft., one target. Hit: 5 (1d8 + 1) piercing damage.
Martial Fury (Bonus Action). Yrsi makes one longsword or longbow attack. Attack rolls against her have advantage until the start of her next turn.
```

## 15 Yox (Area 33)

```text
Yox
Large elemental, lawful evil
Armor Class 17 (natural armor)
Hit Points 200 (16d10 + 112)
Speed 40 ft., fly 60 ft.
STR DEX CON INT WIS CHA
22 (+6) 12 (+1) 24 (+7) 16 (+3) 15 (+2) 16 (+3)
Saving Throws Int +7, Wis +6, Cha +7
Damage Immunities fire
Senses darkvision 120 ft., passive Perception 12
Languages Ignan
Challenge 11 (7,200 XP)
Elemental Demise. If Yox dies, his body disintegrates in a flash of fire and puff of smoke, leaving behind only equipment he was wearing or carrying.
Surrender. When reduced to 100 hit points or fewer, Yox surrenders and offers to trade what he knows of the Summoning Sigil for a sworn oath of release.
Innate Spellcasting. Yox's innate spellcasting ability is Charisma (spell save DC 15, +7 to hit with spell attacks). He can innately cast the following spells, requiring no material components:
At will: detect magic
3/day: enlarge/reduce, tongues
1/day each: gaseous form, invisibility, major image, wall of fire
Actions
Multiattack. Yox makes two scimitar attacks or uses his Hurl Flame twice.
Scimitar. Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage plus 7 (2d6) fire damage.
Hurl Flame. Ranged Spell Attack: +7 to hit, range 120 ft., one target. Hit: 17 (5d6) fire damage.
```

## 16 Avraasha, the First Servant (Area 35)

```text
Avraasha, the First Servant
Huge elemental (pyroclastic sphinx), chaotic good (currently mad)
Armor Class 22 (natural armor)
Hit Points 324 (24d12 + 168)
Speed 45 ft., fly 75 ft.
STR DEX CON INT WIS CHA
26 (+8) 14 (+2) 24 (+7) 22 (+6) 24 (+7) 22 (+6)
Saving Throws Dex +9, Con +14, Int +13, Wis +14
Skills Arcana +20, History +20, Insight +14, Perception +14, Religion +20
Damage Immunities fire
Senses darkvision 120 ft., passive Perception 24
Languages all, spoken and written
Challenge 22 (41,000 XP)
Ember Sight. Avraasha sees invisible creatures and objects, and fog, smoke, and similar obscurement don't block her vision.
Heated Body. A creature that touches Avraasha or hits her with a melee attack while within 5 feet of her takes 10 (3d6) fire damage.
Legendary Resistance (3/Day). If Avraasha fails a saving throw, she can choose to succeed instead.
Magic Resistance. Avraasha has advantage on saving throws against spells and other magical effects.
Regeneration. Avraasha regains 10 hit points at the start of her turn if she is in contact with fire, magma, or lava.
Innate Spellcasting. Her spellcasting ability is Wisdom (spell save DC 22, +14 to hit with spell attacks). She needs no material components.
At will: comprehend languages, detect magic
5/day total, shared: fireball (cast as a 7th-level spell, 12d6), wall of fire
3/day each: clairvoyance, dispel magic, legend lore, locate object, remove curse, symbol
1/day each: incendiary cloud, power word stun, telekinesis
3/day (only once calmed): heal
Actions
Multiattack. Avraasha makes two claw attacks.
Claw. Melee Weapon Attack: +15 to hit, reach 10 ft., one target. Hit: 21 (3d8 + 8) slashing damage.
Legendary Actions
Avraasha can take 3 legendary actions, choosing from the options below. Only one legendary action can be used at a time and only at the end of another creature's turn. Avraasha regains spent legendary actions at the start of her turn.
Claw. Avraasha makes one claw attack.
Ashen Wings (Costs 2 Actions). Avraasha flies up to half her flying speed without provoking opportunity attacks.
Cast a Spell (Costs 3 Actions). Avraasha casts a spell from her 3/day or 5/day list, using a daily use.

######## PART 2 - MONSTER SUMMONING I-VII CREATURES ########
```

# Part 2 · Monster Summoning creatures

## 17 Dwarf (summoned)

```text
Dwarf (summoned)
Medium humanoid (dwarf), lawful good
Armor Class 16 (scale mail, shield)
Hit Points 13 (2d8 + 4)
Speed 25 ft.
STR DEX CON INT WIS CHA
14 (+2) 10 (+0) 15 (+2) 10 (+0) 11 (+0) 10 (+0)
Senses darkvision 60 ft., passive Perception 10
Languages Common, Dwarvish
Challenge 1/4 (50 XP)
Dwarven Resilience. Advantage on saving throws against poison; resistance to poison damage.
Stout. Advantage on saving throws against spells.
Actions
Battleaxe. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) slashing damage.
Light Crossbow. Ranged Weapon Attack: +2 to hit, range 80/320 ft., one target. Hit: 4 (1d8) piercing damage.
```

## 18 Elf (summoned)

```text
Elf (summoned)
Medium humanoid (elf), chaotic good
Armor Class 15 (chain shirt)
Hit Points 11 (2d8 + 2)
Speed 30 ft.
STR DEX CON INT WIS CHA
11 (+0) 15 (+2) 12 (+1) 12 (+1) 12 (+1) 11 (+0)
Skills Perception +3, Stealth +4
Senses darkvision 60 ft., passive Perception 13
Languages Common, Elvish
Challenge 1/4 (50 XP)
Fey Ancestry. Advantage on saves against being charmed; magic can't put it to sleep.
Mask of the Wild. It can hide when lightly obscured by foliage, rain, mist or similar.
Actions
Longsword. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) slashing damage.
Longbow. Ranged Weapon Attack: +5 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage.
```

## 19 Gnome (summoned)

```text
Gnome (summoned)
Small humanoid (gnome), neutral good
Armor Class 15 (leather, shield)
Hit Points 9 (2d6 + 2)
Speed 25 ft.
STR DEX CON INT WIS CHA
11 (+0) 13 (+1) 13 (+1) 12 (+1) 11 (+0) 10 (+0)
Senses darkvision 60 ft., passive Perception 10
Languages Common, Gnomish
Challenge 1/8 (25 XP)
Gnome Cunning. Advantage on Int, Wis and Cha saves against magic.
Speak with Small Beasts. It can talk with burrowing animals.
Actions
Spear. Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d6 + 1) piercing damage.
```

## 20 Halfling (summoned)

```text
Halfling (summoned)
Small humanoid (halfling), lawful good
Armor Class 13 (leather)
Hit Points 7 (2d6)
Speed 25 ft.
STR DEX CON INT WIS CHA
8 (-1) 15 (+2) 11 (+0) 10 (+0) 12 (+1) 11 (+0)
Skills Stealth +4
Senses passive Perception 11
Languages Common, Halfling
Challenge 1/8 (25 XP)
Lucky. It rerolls a 1 on an attack roll, ability check or saving throw.
Brave. Advantage on saves against being frightened.
Actions
Shortsword. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.
Sling. Ranged Weapon Attack: +6 to hit, range 30/120 ft., one target. Hit: 4 (1d4 + 2) bludgeoning damage.
```

## 21 Koalinth

```text
Koalinth
Medium humanoid (goblinoid), lawful evil
Armor Class 18 (chain mail, shield)
Hit Points 11 (2d8 + 2)
Speed 30 ft., swim 30 ft.
STR DEX CON INT WIS CHA
13 (+1) 12 (+1) 12 (+1) 10 (+0) 10 (+0) 9 (-1)
Senses darkvision 60 ft., passive Perception 10
Languages Common, Goblin
Challenge 1/2 (100 XP)
Amphibious. The koalinth can breathe air and water.
Martial Advantage. Once per turn, the koalinth can deal an extra 7 (2d6) damage to a creature it hits with a weapon attack if that creature is within 5 feet of an ally of the koalinth that isn't incapacitated.
Actions
Spear. Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d6 + 1) piercing damage, or 5 (1d8 + 1) piercing damage if used with two hands to make a melee attack.
```

## 22 Nixie

```text
Nixie
Small fey, neutral
Armor Class 12
Hit Points 5 (2d6 - 2)
Speed 20 ft., swim 40 ft.
STR DEX CON INT WIS CHA
8 (-1) 14 (+2) 9 (-1) 12 (+1) 10 (+0) 14 (+2)
Senses passive Perception 10
Languages Common, Sylvan
Challenge 1/8 (25 XP)
Amphibious. It breathes air and water.
Magic Resistance. Advantage on saves against spells and other magical effects.
Chorus Charm. If ten or more nixies are within 30 ft of each other, they can use their actions together to cast charm person (DC 12) on a humanoid within 30 ft. The victim is taken underwater as a slave for a year; the nixies cast water breathing on it so it doesn't drown.
Actions
Dagger. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage.
Javelin. Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage.
```

## 23 Ixitxachitl

```text
Ixitxachitl
Medium aberration, chaotic evil
Armor Class 13 (natural armor)
Hit Points 18 (4d8)
Speed 0 ft., swim 40 ft.
STR DEX CON INT WIS CHA
12 (+1) 15 (+2) 11 (+0) 12 (+1) 13 (+1) 7 (-2)
Senses blindsight 60 ft., passive Perception 11
Languages Abyssal
Challenge 1/2 (100 XP)
Water Breathing. It breathes only water.
Priests. 1 in 10 ixitxachitl casts as a 2nd-level cleric (bane, inflict wounds, 3/day each, DC 11).
Vampiric (variant). 1 in 20 regains 5 hit points at the start of its turn, and its bite reduces the target's hit point maximum by the damage dealt.
Actions
Bite. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (3d4 + 2) piercing damage.
```

## 24 Locathah

```text
Locathah
Medium humanoid (locathah), neutral
Armor Class 13 (natural armor)
Hit Points 13 (2d8 + 4)
Speed 10 ft., swim 40 ft.
STR DEX CON INT WIS CHA
12 (+1) 12 (+1) 14 (+2) 11 (+0) 12 (+1) 9 (-1)
Senses passive Perception 11
Languages Aquan, Common
Challenge 1/4 (50 XP)
Limited Amphibiousness. It breathes air and water but must be submerged at least once every 4 hours or begin to suffocate.
Actions
Spear. Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d6 + 1) piercing damage.
Light Crossbow. Ranged Weapon Attack: +3 to hit, range 80/320 ft., one target. Hit: 5 (1d8 + 1) piercing damage.
```

## 25 Boring Beetle

```text
Boring Beetle
Large beast, unaligned
Armor Class 16 (natural armor)
Hit Points 52 (7d10 + 14)
Speed 20 ft., burrow 10 ft. (wood and soft earth only)
STR DEX CON INT WIS CHA
17 (+3) 8 (-1) 14 (+2) 3 (-4) 10 (+0) 3 (-4)
Senses tremorsense 30 ft., passive Perception 10
Languages -
Challenge 2 (450 XP)
Hive Mind. While three or more boring beetles are within 60 ft of each other, each has Intelligence 10 and can't be surprised.
Actions
Bite. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 12 (2d8 + 3) slashing damage.
```

## 26 Giant Tick

```text
Giant Tick
Small beast, unaligned
Armor Class 15 (natural armor)
Hit Points 14 (4d6)
Speed 10 ft., climb 10 ft.
STR DEX CON INT WIS CHA
8 (-1) 12 (+1) 11 (+0) 1 (-5) 8 (-1) 2 (-4)
Senses blindsight 30 ft., passive Perception 9
Languages -
Challenge 1/2 (100 XP)
Tick Fever. A creature bitten makes a DC 11 Constitution saving throw. On a failure, its hit point maximum drops by 5 (1d10) at each dawn, and it dies if that reaches 0. Any magic that cures disease ends it.
Actions
Bite. Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) piercing damage, and the tick attaches. While attached it doesn't attack. At the start of each of its turns the target loses 7 (2d6) hit points to blood loss. The tick detaches once it has drained 14 hit points, when it dies, or when it is burned (1 fire damage) or submerged. A creature can pull it off with an action and a DC 12 Strength check.
```

## 27 Huge Spider

```text
Huge Spider
Medium beast, unaligned
Armor Class 13 (natural armor)
Hit Points 26 (4d8 + 8)
Speed 40 ft., climb 40 ft.
STR DEX CON INT WIS CHA
14 (+2) 16 (+3) 14 (+2) 2 (-4) 11 (+0) 4 (-3)
Skills Stealth +7
Senses blindsight 10 ft., darkvision 60 ft., passive Perception 10
Languages -
Challenge 1 (200 XP)
Pounce. It can leap 30 ft as part of its movement.
Ambusher. Advantage on attack rolls against any creature it has surprised.
Spider Climb. It can climb difficult surfaces, including ceilings, without a check.
Actions
Bite. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage, and the target makes a DC 11 Constitution saving throw, taking 14 (4d6) poison damage on a failure or half as much on a success.
```

## 28 Lacedon

```text
Lacedon
Medium undead, chaotic evil
Armor Class 12
Hit Points 22 (5d8)
Speed 30 ft., swim 30 ft.
STR DEX CON INT WIS CHA
13 (+1) 15 (+2) 10 (+0) 7 (-2) 10 (+0) 6 (-2)
Damage Immunities poison
Condition Immunities charmed, exhaustion, poisoned
Senses darkvision 60 ft., passive Perception 10
Languages Common
Challenge 1 (200 XP)
Aquatic Undead. The lacedon doesn't need to breathe and never surfaces.
Actions
Bite. Melee Weapon Attack: +2 to hit, reach 5 ft., one creature. Hit: 9 (2d6 + 2) piercing damage.
Claws. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) slashing damage. If the target is a creature other than an elf or undead, it must succeed on a DC 10 Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.
```

## 29 Carnivorous Ape

```text
Carnivorous Ape
Large beast, unaligned
Armor Class 13 (natural armor)
Hit Points 59 (7d10 + 21)
Speed 30 ft., climb 30 ft.
STR DEX CON INT WIS CHA
18 (+4) 14 (+2) 16 (+3) 6 (-2) 12 (+1) 6 (-2)
Skills Perception +5
Senses passive Perception 15
Languages -
Challenge 3 (700 XP)
Keen Senses. Advantage on Perception checks that rely on sight, hearing or smell.
Actions
Multiattack. Two fist attacks and one bite.
Fist. Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) bludgeoning damage. If both fists hit the same target, it takes an extra 9 (2d8) slashing damage (rending).
Bite. Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) piercing damage.
```

## 30 Ice Toad

```text
Ice Toad
Large monstrosity, neutral
Armor Class 15 (natural armor)
Hit Points 59 (7d10 + 21)
Speed 25 ft.
STR DEX CON INT WIS CHA
16 (+3) 10 (+0) 16 (+3) 9 (-1) 10 (+0) 7 (-2)
Damage Immunities cold
Senses darkvision 60 ft., passive Perception 10
Languages Ice Toad
Challenge 3 (700 XP)
Actions
Bite. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (3d4 + 3) piercing damage.
Frost Pulse (Recharge 4-6). Each creature within 10 ft that isn't immune to cold makes a DC 13 Constitution saving throw, taking 10 (3d6) cold damage on a failure or half as much on a success.
```

## 31 Poisonous Toad

```text
Poisonous Toad
Medium beast, unaligned
Armor Class 11
Hit Points 13 (3d8)
Speed 20 ft., swim 40 ft.
STR DEX CON INT WIS CHA
12 (+1) 13 (+1) 11 (+0) 2 (-4) 10 (+0) 3 (-4)
Senses darkvision 30 ft., passive Perception 10
Languages -
Challenge 1/2 (100 XP)
Amphibious. It breathes air and water.
Standing Leap. It long-jumps 20 ft and high-jumps 10 ft, with or without a running start.
Actions
Bite. Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) piercing damage, and the target makes a DC 11 Constitution saving throw, taking 10 (3d6) poison damage on a failure or half as much on a success.
```

## 32 Hydra (Greyhawk), 5-headed

```text
Hydra (Greyhawk), 5-headed
Large monstrosity, unaligned
Armor Class 14 (natural armor)
Hit Points 90 (12d10 + 24)
Speed 30 ft., swim 20 ft.
STR DEX CON INT WIS CHA
18 (+4) 12 (+1) 15 (+2) 2 (-4) 10 (+0) 7 (-2)
Skills Perception +6
Senses darkvision 60 ft., passive Perception 16
Languages -
Challenge 4 (1,100 XP)
Heads. It starts with 5 heads. It loses one head for every 18 damage it takes; heads don't regrow. It dies when its last head does.
Many Eyes. Advantage on Perception checks and saves against being blinded, charmed, deafened, frightened, stunned or knocked unconscious.
Actions
Multiattack. One bite per remaining head. No more than four bites can target the same creature.
Bite. Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 7 (1d6 + 4) piercing damage.
```

## 33 Giant Water Beetle

```text
Giant Water Beetle
Large beast, unaligned
Armor Class 16 (natural armor)
Hit Points 45 (6d10 + 12)
Speed 10 ft., swim 40 ft.
STR DEX CON INT WIS CHA
16 (+3) 10 (+0) 14 (+2) 1 (-5) 10 (+0) 3 (-4)
Senses blindsight 30 ft., tremorsense 60 ft. (in water), passive Perception 10
Languages -
Challenge 2 (450 XP)
Hold Breath. It can hold its breath for 1 hour (a trapped air bubble).
Actions
Bite. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 13 (3d6 + 3) piercing damage.
```

## 34 Giant Crayfish

```text
Giant Crayfish
Large beast, unaligned
Armor Class 15 (natural armor)
Hit Points 45 (6d10 + 12)
Speed 15 ft., swim 30 ft.
STR DEX CON INT WIS CHA
16 (+3) 10 (+0) 14 (+2) 1 (-5) 9 (-1) 3 (-4)
Skills Stealth +4
Senses blindsight 30 ft., passive Perception 9
Languages -
Challenge 2 (450 XP)
Amphibious. It breathes air and water.
Lurker. Advantage on Stealth checks made underwater.
Actions
Multiattack. Two claw attacks.
Claw. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage, and the target is grappled (escape DC 13). It has two claws, each able to grapple one target.
```

## 35 Kopoacinth

```text
Kopoacinth
Medium elemental, chaotic evil
Armor Class 15 (natural armor)
Hit Points 52 (7d8 + 21)
Speed 30 ft., swim 60 ft.
STR DEX CON INT WIS CHA
15 (+2) 11 (+0) 16 (+3) 6 (-2) 11 (+0) 7 (-2)
Damage Resistances bludgeoning, piercing, and slashing from nonmagical attacks that aren't adamantine
Damage Immunities poison
Condition Immunities exhaustion, petrified, poisoned
Senses darkvision 60 ft., passive Perception 10
Languages Terran
Challenge 2 (450 XP)
Amphibious. The kopoacinth can breathe air and water.
False Appearance. While the kopoacinth remains motionless, it is indistinguishable from an inanimate statue.
Actions
Multiattack. The kopoacinth makes two attacks: one with its bite and one with its claws.
Bite. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.
Claws. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage.
```

## 36 Giant Water Spider

```text
Giant Water Spider
Medium beast, unaligned
Armor Class 14 (natural armor)
Hit Points 33 (6d8 + 6)
Speed 30 ft., climb 30 ft., swim 40 ft.
STR DEX CON INT WIS CHA
14 (+2) 15 (+2) 12 (+1) 4 (-3) 10 (+0) 4 (-3)
Senses blindsight 10 ft., darkvision 60 ft., passive Perception 10
Languages -
Challenge 1 (200 XP)
Air Bell. It carries air down on its body and can hold its breath for 1 hour. A creature it drags into its nest can breathe there.
Water Walker. It moves across the surface of water as if it were solid ground.
Actions
Bite. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage, and the target makes a DC 11 Constitution saving throw, taking 9 (2d8) poison damage on a failure or half as much on a success.
```

## 37 Hydra (Greyhawk), 7-headed

```text
Hydra (Greyhawk), 7-headed
Large monstrosity, unaligned
Armor Class 14 (natural armor)
Hit Points 126 (12d10 + 60)
Speed 30 ft., swim 20 ft.
STR DEX CON INT WIS CHA
18 (+4) 12 (+1) 20 (+5) 2 (-4) 10 (+0) 7 (-2)
Skills Perception +6
Senses darkvision 60 ft., passive Perception 16
Languages -
Challenge 6 (2,300 XP)
Heads. The hydra starts with 7 heads. It loses one head for every 18 damage it takes; heads don't regrow. It dies when its last head does.
Many Eyes. The hydra has advantage on Wisdom (Perception) checks and on saving throws against being blinded, charmed, deafened, frightened, stunned, and knocked unconscious.
Actions
Multiattack. The hydra makes one bite attack per remaining head. No more than four bites can target the same creature.
Bite. Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 8 (1d8 + 4) piercing damage.
```

## 38 Subterranean Lizard

```text
Subterranean Lizard
Large beast, unaligned
Armor Class 14 (natural armor)
Hit Points 52 (7d10 + 14)
Speed 40 ft., climb 40 ft.
STR DEX CON INT WIS CHA
16 (+3) 13 (+1) 14 (+2) 2 (-4) 10 (+0) 5 (-3)
Senses darkvision 60 ft., passive Perception 10
Languages -
Challenge 2 (450 XP)
Spider Climb. It climbs walls and ceilings without a check.
Actions
Bite. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) piercing damage, plus 1d6 piercing if the lizard attacked from a wall or ceiling this turn.
```

## 39 Giant Amphisbaena

```text
Giant Amphisbaena
Large beast, unaligned
Armor Class 15 (natural armor)
Hit Points 45 (7d10 + 7)
Speed 40 ft.
STR DEX CON INT WIS CHA
14 (+2) 16 (+3) 12 (+1) 2 (-4) 10 (+0) 3 (-4)
Damage Immunities cold
Senses blindsight 10 ft., passive Perception 10
Languages -
Challenge 3 (700 XP)
Two Heads. It can't be flanked, and it has advantage on saves against being blinded or stunned.
Actions
Multiattack. Two bites, one from each head.
Bite. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) piercing damage, and the target makes a DC 12 Constitution saving throw, taking 14 (4d6) poison damage on a failure or half as much on a success.
```

## 40 Giant Spitting Snake

```text
Giant Spitting Snake
Medium beast, unaligned
Armor Class 14 (natural armor)
Hit Points 27 (5d8 + 5)
Speed 30 ft., swim 30 ft.
STR DEX CON INT WIS CHA
10 (+0) 16 (+3) 12 (+1) 2 (-4) 10 (+0) 3 (-4)
Senses blindsight 10 ft., passive Perception 10
Languages -
Challenge 1 (200 XP)
Actions
Bite. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) piercing damage, and the target makes a DC 11 Constitution saving throw, taking 10 (3d6) poison damage on a failure or half as much on a success.
Spit (Recharge 5-6). Ranged Weapon Attack: +5 to hit, range 30 ft., one target. Hit: The target must make a DC 11 Constitution saving throw, taking 10 (3d6) poison damage on a failed save, or half as much damage on a successful one. On a failed save, it is also blinded until the end of its next turn.
```

## 41 Sea Lion

```text
Sea Lion
Large monstrosity, unaligned
Armor Class 15 (natural armor)
Hit Points 59 (7d10 + 21)
Speed 10 ft., swim 50 ft.
STR DEX CON INT WIS CHA
18 (+4) 14 (+2) 16 (+3) 3 (-4) 12 (+1) 8 (-1)
Skills Perception +3
Senses passive Perception 13
Languages -
Challenge 3 (700 XP)
Water Breathing. It breathes only water.
Pack Tactics. Advantage on attack rolls against a creature if an ally is within 5 ft of that creature and isn't incapacitated.
Actions
Multiattack. Two claw attacks and one bite.
Claw. Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) slashing damage.
Bite. Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) piercing damage.
```

## 42 Hydra (Greyhawk), 8-headed

```text
Hydra (Greyhawk), 8-headed
Large monstrosity, unaligned
Armor Class 14 (natural armor)
Hit Points 142 (15d10 + 60)
Speed 30 ft., swim 20 ft.
STR DEX CON INT WIS CHA
18 (+4) 12 (+1) 18 (+4) 2 (-4) 10 (+0) 7 (-2)
Skills Perception +6
Senses darkvision 60 ft., passive Perception 16
Languages -
Challenge 7 (2,900 XP)
Heads. The hydra starts with 8 heads. It loses one head for every 18 damage it takes; heads don't regrow. It dies when its last head does.
Many Eyes. The hydra has advantage on Wisdom (Perception) checks and on saving throws against being blinded, charmed, deafened, frightened, stunned, and knocked unconscious.
Actions
Multiattack. The hydra makes one bite attack per remaining head. No more than four bites can target the same creature.
Bite. Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 8 (1d8 + 4) piercing damage.
```

## 43 Lammasu

```text
Lammasu
Large celestial, lawful good
Armor Class 14 (natural armor)
Hit Points 85 (10d10 + 30)
Speed 30 ft., fly 60 ft.
STR DEX CON INT WIS CHA
18 (+4) 12 (+1) 16 (+3) 17 (+3) 18 (+4) 16 (+3)
Saving Throws Wis +7, Cha +6
Skills Insight +7, Religion +6
Senses truesight 30 ft., passive Perception 14
Languages Celestial, Common, telepathy 60 ft
Challenge 5 (1,800 XP)
Magic Resistance. Advantage on saves against spells and other magical effects.
Aura of Warding. Evil creatures have disadvantage on attack rolls against creatures within 10 ft of the lammasu. Those creatures have advantage on saves against effects from evil creatures.
Healer. When it casts a spell that restores hit points, it restores the maximum possible.
Innate Spellcasting. At will: invisibility (self), dimension door (not inside the Temple).
Spellcasting. A 7th-level cleric (Wis, DC 15, +7 to hit). Slots 4/3/3/1. 1st: bless, cure wounds, protection from evil and good, sanctuary. 2nd: hold person, lesser restoration, silence. 3rd: dispel magic, remove curse, spirit guardians. 4th: death ward.
Actions
Multiattack. Two claw attacks.
Claw. Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage.
```

## 44 Wind Walker

```text
Wind Walker
Large elemental, neutral
Armor Class 13
Hit Points 75 (10d10 + 20)
Speed 0 ft., fly 90 ft. (hover)
STR DEX CON INT WIS CHA
14 (+2) 17 (+3) 14 (+2) 10 (+0) 12 (+1) 10 (+0)
Damage Immunities all damage except as noted under Ethereal Wind
Condition Immunities grappled, paralyzed, petrified, prone, restrained, unconscious
Senses blindsight 60 ft., passive Perception 11
Languages Auran, telepathy 120 ft
Challenge 5 (1,800 XP)
Ethereal Wind. The wind walker takes damage only from elementals, genies and invisible stalkers, and from these spells: slow deals 28 (8d6) force damage to it, with no save; haste deals 14 (4d6) force damage; control weather makes it succeed on a DC 15 Constitution saving throw or die; ice storm deals no damage but drives it away for 1d4 rounds.
Howling Approach. It can't hide, and it can be heard up to a mile away.
Detect Thoughts. It can cast detect thoughts at will (no components), reaching 300 ft.
Actions
Wind Blast. Each creature within 10 ft makes a DC 13 Strength saving throw, taking 10 (3d6) bludgeoning damage and being pushed 10 ft on a failure, or half damage and no push on a success.
```

## 45 Giant Sea Snake

```text
Giant Sea Snake
Huge beast, unaligned
Armor Class 14 (natural armor)
Hit Points 115 (11d12 + 44)
Speed 10 ft., swim 60 ft.
STR DEX CON INT WIS CHA
19 (+4) 14 (+2) 18 (+4) 1 (-5) 10 (+0) 3 (-4)
Senses blindsight 10 ft., passive Perception 10
Languages -
Challenge 5 (1,800 XP)
Hold Breath. It can hold its breath for 1 hour.
Ship Crusher. It deals double damage to objects and structures.
Actions
Multiattack. One bite and one constrict.
Bite. Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 8 (1d8 + 4) piercing damage, and the target makes a DC 14 Constitution saving throw, taking 14 (4d6) poison damage on a failure or half as much on a success.
Constrict. Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 14 (3d6 + 4) bludgeoning damage, and the target is grappled (escape DC 16) and restrained until the grapple ends.
```

## 46 Hydra (Greyhawk), 10-headed

```text
Hydra (Greyhawk), 10-headed
Huge monstrosity, unaligned
Armor Class 14 (natural armor)
Hit Points 180 (19d12 + 57)
Speed 30 ft., swim 20 ft.
STR DEX CON INT WIS CHA
20 (+5) 12 (+1) 16 (+3) 2 (-4) 10 (+0) 7 (-2)
Skills Perception +8
Senses darkvision 60 ft., passive Perception 18
Languages -
Challenge 9 (5,000 XP)
Heads. The hydra starts with 10 heads. It loses one head for every 18 damage it takes; heads don't regrow. It dies when its last head does.
Many Eyes. The hydra has advantage on Wisdom (Perception) checks and on saving throws against being blinded, charmed, deafened, frightened, stunned, and knocked unconscious.
Actions
Multiattack. The hydra makes one bite attack per remaining head. No more than four bites can target the same creature.
Bite. Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 9 (1d8 + 5) piercing damage.
```

## 47 Pyrohydra, 8-headed

```text
Pyrohydra, 8-headed
Large monstrosity, unaligned
Armor Class 14 (natural armor)
Hit Points 142 (15d10 + 60)
Speed 30 ft., swim 20 ft.
STR DEX CON INT WIS CHA
18 (+4) 12 (+1) 18 (+4) 2 (-4) 10 (+0) 7 (-2)
Skills Perception +6
Damage Immunities fire
Senses darkvision 60 ft., passive Perception 16
Languages -
Challenge 8 (3,900 XP)
Heads. The pyrohydra starts with 8 heads. It loses one head for every 18 damage it takes; heads don't regrow. It dies when its last head does.
Many Eyes. The pyrohydra has advantage on Wisdom (Perception) checks and on saving throws against being blinded, charmed, deafened, frightened, stunned, and knocked unconscious.
Actions
Multiattack. The pyrohydra makes one bite attack per remaining head. No more than four bites can target the same creature. It can replace any bite with that head's Fire Breath.
Bite. Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 8 (1d8 + 4) piercing damage.
Fire Breath (Each Head 2/Day). The head exhales fire in a 20-foot cone. Each creature in that area must make a DC 14 Dexterity saving throw, taking 14 (4d6) fire damage on a failed save, or half as much damage on a successful one.
```

## 48 Fire Lizard

```text
Fire Lizard
Huge monstrosity, neutral
Armor Class 16 (natural armor)
Hit Points 126 (12d12 + 48)
Speed 30 ft.
STR DEX CON INT WIS CHA
19 (+4) 9 (-1) 18 (+4) 2 (-4) 10 (+0) 5 (-3)
Damage Immunities fire
Senses darkvision 60 ft., passive Perception 10
Languages -
Challenge 5 (1,800 XP)
Sluggish. It has disadvantage on initiative rolls.
Actions
Multiattack. Two claw attacks and one bite.
Claw. Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) slashing damage.
Bite. Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 13 (2d8 + 4) piercing damage.
Fire Breath (Recharge 5-6). A 15-ft cone. Each creature in it makes a DC 15 Dexterity saving throw, taking 14 (4d6) fire damage on a failure or half as much on a success.
```

## 49 Neo-Otyugh

```text
Neo-Otyugh
Large aberration, neutral
Armor Class 17 (natural armor)
Hit Points 152 (16d10 + 64)
Speed 30 ft.
STR DEX CON INT WIS CHA
16 (+3) 11 (+0) 19 (+4) 9 (-1) 13 (+1) 6 (-2)
Saving Throws Con +7
Senses darkvision 120 ft., passive Perception 11
Languages Otyugh
Challenge 6 (2,300 XP)
Limited Telepathy. The neo-otyugh can magically transmit simple messages and images to any creature within 240 feet of it that can understand a language.
Unsurprisable. The neo-otyugh can't be surprised.
Actions
Multiattack. The neo-otyugh makes three attacks: one with its bite and two with its tentacles.
Bite. Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 12 (2d8 + 3) piercing damage. If the target is a creature, it must succeed on a DC 15 Constitution saving throw against disease or become poisoned until the disease is cured. Every 24 hours that elapse, the target must repeat the saving throw, reducing its hit point maximum by 5 (1d10) on a failure. The disease is cured on a success. The target dies if the disease reduces its hit point maximum to 0. This reduction to the target's hit point maximum lasts until the disease is cured.
Tentacle. Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage plus 7 (2d6) piercing damage. If the target is Medium or smaller, it is grappled (escape DC 13) and restrained until the grapple ends. The neo-otyugh has two tentacles, each of which can grapple one target.
Tentacle Slam. The neo-otyugh slams creatures grappled by it into each other or a solid surface. Each creature must succeed on a DC 15 Constitution saving throw or take 10 (2d6 + 3) bludgeoning damage and be stunned until the end of the neo-otyugh's next turn. On a successful save, the target takes half the bludgeoning damage and isn't stunned.
```

## 50 Shedu

```text
Shedu
Large celestial, lawful good
Armor Class 16 (natural armor)
Hit Points 114 (12d10 + 48)
Speed 40 ft., fly 80 ft.
STR DEX CON INT WIS CHA
20 (+5) 12 (+1) 18 (+4) 16 (+3) 18 (+4) 16 (+3)
Saving Throws Con +7, Wis +7
Skills Insight +7, Perception +7
Senses truesight 60 ft., passive Perception 17
Languages Celestial, Common, telepathy 120 ft
Challenge 7 (2,900 XP)
Magic Resistance. Advantage on saves against spells and other magical effects.
Innate Spellcasting (Psionics). Wis, DC 15, no components. At will: detect thoughts, etherealness (self only). 3/day each: calm emotions, hold monster, telekinesis. 1/day: mind blank.
Actions
Multiattack. Two hoof attacks.
Hoof. Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) bludgeoning damage.
```

## 51 Giant Slug

```text
Giant Slug
Huge beast, unaligned
Armor Class 11
Hit Points 162 (13d12 + 78)
Speed 20 ft., burrow 5 ft.
STR DEX CON INT WIS CHA
20 (+5) 6 (-2) 22 (+6) 1 (-5) 8 (-1) 2 (-4)
Damage Immunities bludgeoning
Senses blindsight 60 ft., passive Perception 9
Languages -
Challenge 6 (2,300 XP)
Boneless. It can move through a space as narrow as 1 ft without squeezing.
Ranging Shot. Its first Acid Spit in an encounter is made with disadvantage.
Actions
Bite. Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) piercing damage.
Acid Spit (Recharge 4-6). Ranged Weapon Attack: +5 to hit, range 60/120 ft., one target. Hit: 21 (6d6) acid damage.
```

## 52 Hieracosphinx

```text
Hieracosphinx
Large monstrosity, chaotic evil
Armor Class 16 (natural armor)
Hit Points 85 (10d10 + 30)
Speed 30 ft., fly 90 ft.
STR DEX CON INT WIS CHA
18 (+4) 14 (+2) 16 (+3) 6 (-2) 14 (+2) 8 (-1)
Skills Perception +5
Senses passive Perception 15
Languages understands Sphinx but can't speak
Challenge 4 (1,100 XP)
Keen Sight. Advantage on Perception checks that rely on sight.
Actions
Multiattack. Two claw attacks and one beak attack.
Claw. Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (2d4 + 4) slashing damage.
Beak. Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (1d10 + 4) piercing damage.
```

## 53 Water Naga

```text
Water Naga
Large monstrosity, neutral
Armor Class 15 (natural armor)
Hit Points 75 (10d10 + 20)
Speed 30 ft., swim 60 ft.
STR DEX CON INT WIS CHA
14 (+2) 16 (+3) 14 (+2) 15 (+2) 13 (+1) 14 (+2)
Saving Throws Dex +6, Wis +4
Senses darkvision 60 ft., passive Perception 11
Languages Common, Aquan
Challenge 5 (1,800 XP)
Amphibious. It breathes air and water.
Spellcasting. A 5th-level wizard (Int, DC 13, +5 to hit). No fire spells. Cantrips: mage hand, ray of frost, shocking grasp. 1st (4): charm person, fog cloud, magic missile, shield. 2nd (3): hold person, mirror image. 3rd (2): slow, water breathing.
Actions
Bite. Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 6 (1d6 + 3) piercing damage, and the target makes a DC 12 Constitution saving throw, taking 14 (4d6) poison damage on a failure or half as much on a success.
```

## 54 Manta Ray

```text
Manta Ray
Huge beast, unaligned
Armor Class 13 (natural armor)
Hit Points 126 (11d12 + 55)
Speed 0 ft., swim 60 ft.
STR DEX CON INT WIS CHA
20 (+5) 12 (+1) 20 (+5) 1 (-5) 10 (+0) 3 (-4)
Skills Stealth +4
Senses blindsight 60 ft., passive Perception 10
Languages -
Challenge 6 (2,300 XP)
Water Breathing. It breathes only water.
Sea-Floor Camouflage. Advantage on Stealth checks while lying on the sea floor.
Actions
Bite. Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 12 (3d4 + 5) piercing damage. If the roll beats the target's AC by 5 or more and the target is Large or smaller, it is swallowed: blinded and restrained, with total cover from outside, and it takes 10 (3d6) acid damage at the start of each of the ray's turns. A swallowed creature can attack the ray from inside. If the ray takes 25 or more damage in one turn from a swallowed creature, it regurgitates everything.
Tail Spine. Melee Weapon Attack: +8 to hit, reach 15 ft., one creature behind the ray. Hit: 16 (2d10 + 5) piercing damage, and the target must succeed on a DC 16 Constitution saving throw or be stunned for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.
```

## 55 Giant Squid

```text
Giant Squid
Huge beast, unaligned
Armor Class 15 (natural armor)
Hit Points 168 (16d12 + 64)
Speed 10 ft., swim 60 ft.
STR DEX CON INT WIS CHA
22 (+6) 13 (+1) 18 (+4) 2 (-4) 12 (+1) 3 (-4)
Senses darkvision 120 ft., passive Perception 11
Languages -
Challenge 9 (5,000 XP)
Water Breathing. It breathes only water.
Severable Tentacles. Each tentacle has AC 13 and 15 hit points. Severing one frees whatever it holds and doesn't harm the squid's main pool. It has 8 tentacles.
Actions
Multiattack. Four tentacle attacks and one beak attack.
Tentacle. Melee Weapon Attack: +9 to hit, reach 20 ft., one target. Hit: 9 (1d6 + 6) bludgeoning damage, and the target is grappled (escape DC 17). At the start of each of the squid's turns, each creature it is grappling takes 7 (2d6) bludgeoning damage (constriction).
Beak. Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 18 (5d4 + 6) piercing damage.
Reactions
Jet. When it takes damage, it swims up to 60 ft away without provoking opportunity attacks, dropping any grappled creatures.
```
