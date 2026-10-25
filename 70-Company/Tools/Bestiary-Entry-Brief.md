---
type: tool-note
section: internal
publish: false
---
# Bestiary Entry Brief (writer's brief for SP-BST-01)

The brief every writer, human or Claude, follows when turning a raw statblock into a 65-Bestiary entry. Read this whole note before writing.

## Where things are
- Vault root (in device_bash): `$HOME/mnt/Sidebar Press Vault`. Source statblocks: `$HOME/mnt/Monster Unload/<Name>.md` (**read-only**: never modify or move these).
- Write each entry to `$HOME/mnt/Sidebar Press Vault/65-Bestiary/<Name>.md`. Write **only** your own entry files. Do not edit the index, the appendices, other creatures, or anything outside 65-Bestiary.
- Model entries to match exactly (read at least two before you start): `65-Bestiary/Pale Chimera.md` (a contributed creature re-rated, with a changes table), `65-Bestiary/Gluttonwretch.md` (a legendary unique), and `65-Bestiary/Harvest Lord.md` (lair actions and regional effects in separate callouts).
- Write files with `cat > file <<'EOF' … EOF` (quoted heredoc). Don't produce a `## FGU Import` section, because a generator adds it afterward.

## Frontmatter (exact keys)
```
---
type: creature
adventure: "SP-BST-01"
section: bestiary            # or rogues-gallery (see Naming)
publish_order: 1             # placeholder; renumbered centrally
publish: true
status: drafted
creature: "<display name>"
cr: "<printed CR>"           # string, e.g. "1/2", "12"
cr_num: <decimal>            # 0.125, 0.25, 0.5, 1 …
xp: <int>
size: <Size>
creature_type: <type>        # bare type, e.g. undead, fiend, humanoid
alignment: <alignment>
environment: [ … ]           # from: arctic, coastal, desert, forest, grassland, hill, mountain, swamp, underdark, underwater, urban, farmland, village, ruins, graveyard, road
origin: contributed
credit: "GrimmGrixis"
base_block: "none (contributed statblock[, re-rated from CR X to CR Y])"
source_adventures: []
tags: [bestiary, statblock, 2014-5e, contributed]   # add legendary / villain-type / rogues-gallery where true
---
```

## Entry layout (in this order)
1. `# <Name>`
2. An italic read-aloud line, 25 words or fewer, describing what the players see.
3. `*Created by **GrimmGrixis**, Writers Guild.*`
4. An image callout directly above the statblock: `> [!art]+ Plate` then `> ![[99-Assets/SP-BST-01/plates/<file name>.png|360]]`. Rogues' Gallery entries add a collapsed `> [!art]- Splash (full page)` with `![[99-Assets/SP-BST-01/splashes/<file name> — Splash.png|500]]`. The portrait and token callout is generated inside FGU Import, so don't write it by hand.
5. The statblock, in house format (copy the punctuation from Pale Chimera exactly):
   - `> [!example]+ <Name> (CR X, N XP)`, then `> *Size type, alignment*`.
   - `> **Armor Class** … · **Hit Points** … · **Speed** …`
   - The ability table as a 3-line markdown table inside the callout. Use the true minus sign `−` in modifiers.
   - Defense and sense lines joined with ` · `, ending with `**Challenge** X (N XP)`.
   - Traits as `> ***Name.*** text`, with a blank `>` line between entries.
   - Headings `> **Actions**`, `> **Bonus Actions**`, `> **Reactions**`, and `> **Legendary Actions**`, only these. Fold any nonstandard section (e.g. "Vanguard Actions") into the closest standard one, or into a trait, and say so in the changes table.
   - Attack lines use `*Melee Weapon Attack:* +X to hit, reach 5 ft., one target. *Hit:* N (dice + mod) type damage.` and the 2014 MM wording throughout.
   - Lair actions go in a **separate** callout, `> [!example]+ <Name> — Lair Actions`, with `- ***Name.*** text` bullets. Regional effects go in `> [!example]+ <Name> — Regional Effects`.
   - A creature with two forms gets two statblock callouts in one note (e.g. "… (Spectral Form)").
5. `## Lore` (2–3 paragraphs) · `## Ecology` (Environment / Encountered as / Signs) · `## Tactics` (plus a **Running it:** line) · `## Lair / Regional Effects` (only if it has them; refer to the callouts) · `## Variants` (only if real) · `## Named Example` (generic types that came from a named creature) · `## Adventure Hooks` (3 numbered, each with a twist) · `## Spoils` · `## Design Notes` · `## Appears In` (`- Not yet placed.` unless a Sidebar Press adventure uses it) · `## Art Prompt`.
6. **Design Notes** must contain:
   - "**Contributed by GrimmGrixis** (Realms / Writers Guild). The lore, ecology, tactics, hooks, and spoils were drafted by Sidebar Press and need the contributor's review."
   - A **changes table** (`| Change | As submitted | Now | Why |`) covering every rules change, including arithmetic fixes and copy fixes. If nothing changed, say "Statblock unchanged apart from house formatting."
   - **CR verification (DMG p. 274)** with the working shown: defensive CR, offensive CR, and the average. If you re-rated, show the math both as submitted and as retuned, and explain in one short paragraph headed "**Why CR X, not Y.**"
   - Any IP substitutions (original name → replacement) and the campaign it came from, if known.
7. **Art Prompt**: one code block, in the house black-and-white ink style ([[Art-Style-Guide]], PLATE spine). The subject is the creature alone with only the ground it stands on: no scenery, and colors written as ink values or patterns ("dark hide", "bold black-and-white bands"). Then: `full figure centered with the head and shoulders in the upper middle of the frame and clear space on every side, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 3:4 --v 8.1 --style raw --stylize 75 --seed 26500 --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark`

8. **Color portrait**: a second code block under Art Prompt, headed `**Color portrait** (screen only: the FGU portrait and the token-maker source).` The creature is described **in full color**, then: `head and shoulders portrait in three-quarter view, the head in the upper middle of the frame with clear space around it, stylized fantasy tabletop RPG creature portrait, crisp painted digital game art, clean confident linework with painterly cel-like shading, vivid but controlled color, soft rim light, strong readable silhouette, on a soft light cream and warm pale grey background with a gentle vignette --ar 3:4 --v 8.1 --stylize 150 --seed 26500 --no text, letters, signature, watermark, frame, border, dark background, black background`. Pale creatures use `soft light dusty blue-grey`.

## Naming (Greybeard's ruling, 2026-10-24)
- A **named individual** (a proper name, or "The X" meaning one unique being) keeps its name, gets `section: rogues-gallery`, and adds the tag `rogues-gallery`. Its Lore section is about that individual. Use `## Named Example` only for generic types.
- A **kind of creature** gets `section: bestiary`.
- **Setting-agnostic:** strip setting-specific references. Ravnica, guild names, and campaign place names become generic placeholders (e.g. "a fire-cult guild" → "a fire cult"). WotC-specific named deities and demon lords become generic epithets (Yeenoghu → "the Ravening Lord"; Tiamat or "the Queen" of dragons → "the Dragon Queen"). Note the original in Design Notes. SRD creature names (erinyes, gnoll, kobold, ogre, etc.) are fine to keep.
- Drop source-vault links (`[[Homebrew - …]]`, `#CR…Monster` tags, `![[…art…]]` embeds). Mention in Design Notes where the creature originally appeared, if the source says (e.g. "The Chronicle, Session 1: The Deeproot Cradle").

## House copy style
American spelling (except "grey"), serial comma, en dashes in ranges in body text (e.g. "Recharge 5–6"), the true minus `−` in ability modifiers, bare skill names in checks ("Wisdom (Perception) check"), and "its" not "it's". Write clear prose with no filler.

## CR policy (Greybeard's ruling, 2026-10-24)
Compute the CR per the DMG (p. 274). **If the computed CR is within 1 of the stated CR, keep the stated CR**, but still fix internal arithmetic (dice averages, proficiency-derived bonuses, DCs that match no ability, HP dice that don't average to the HP). **If it is off by 2 or more, re-rate** to the computed CR. Fix proficiency, attack bonuses, saves, skills, and DCs for the new CR, keeping the creature's attacks and identity. Adjust the numbers only as far as needed for a clean average, and show everything.

### DMG p. 274 table (2014)
| CR | Prof | AC | HP | Atk | DPR | DC |
|---|---|---|---|---|---|---|
| 0 | +2 | ≤13 | 1–6 | ≤+3 | 0–1 | ≤13 |
| 1/8 | +2 | 13 | 7–35 | +3 | 2–3 | 13 |
| 1/4 | +2 | 13 | 36–49 | +3 | 4–5 | 13 |
| 1/2 | +2 | 13 | 50–70 | +3 | 6–8 | 13 |
| 1 | +2 | 13 | 71–85 | +3 | 9–14 | 13 |
| 2 | +2 | 13 | 86–100 | +3 | 15–20 | 13 |
| 3 | +2 | 13 | 101–115 | +4 | 21–26 | 13 |
| 4 | +2 | 14 | 116–130 | +5 | 27–32 | 14 |
| 5 | +3 | 15 | 131–145 | +6 | 33–38 | 15 |
| 6 | +3 | 15 | 146–160 | +6 | 39–44 | 15 |
| 7 | +3 | 15 | 161–175 | +6 | 45–50 | 15 |
| 8 | +3 | 16 | 176–190 | +7 | 51–56 | 16 |
| 9 | +4 | 16 | 191–205 | +7 | 57–62 | 16 |
| 10 | +4 | 17 | 206–220 | +7 | 63–68 | 16 |
| 11 | +4 | 17 | 221–235 | +8 | 69–74 | 17 |
| 12 | +4 | 17 | 236–250 | +8 | 75–80 | 17 |
| 13 | +5 | 18 | 251–265 | +8 | 81–86 | 18 |
| 14 | +5 | 18 | 266–280 | +8 | 87–92 | 18 |
| 15 | +5 | 18 | 281–295 | +8 | 93–98 | 18 |
| 16 | +5 | 18 | 296–310 | +9 | 99–104 | 18 |
| 17 | +6 | 19 | 311–325 | +10 | 105–110 | 19 |
| 18 | +6 | 19 | 326–340 | +10 | 111–116 | 19 |
| 19 | +6 | 19 | 341–355 | +10 | 117–122 | 19 |
| 20 | +6 | 19 | 356–400 | +10 | 123–140 | 19 |
| 21 | +7 | 19 | 401–445 | +11 | 141–158 | 20 |
| 22 | +7 | 19 | 446–490 | +11 | 159–176 | 20 |
| 23 | +7 | 19 | 491–535 | +11 | 177–194 | 20 |
| 24 | +7 | 19 | 536–580 | +12 | 195–212 | 21 |

XP by CR: 0 10 · 1/8 25 · 1/4 50 · 1/2 100 · 1 200 · 2 450 · 3 700 · 4 1,100 · 5 1,800 · 6 2,300 · 7 2,900 · 8 3,900 · 9 5,000 · 10 5,900 · 11 7,200 · 12 8,400 · 13 10,000 · 14 11,500 · 15 13,000 · 16 15,000 · 17 18,000 · 18 20,000 · 19 22,000 · 20 25,000 · 21 33,000 · 22 41,000 · 23 50,000 · 24 62,000.

### Method
- **Defensive:** start from HP and apply the effective-HP multiplier for resistances or immunities. Use it only for broad ones (e.g. nonmagical bludgeoning, piercing, and slashing, or three or more common types). Expected CR 1–4: resistance ×2, immunity ×2. CR 5–10: ×1.5 / ×2. CR 11–16: ×1.25 / ×1.5. CR 17+: ×1 / ×1.25. Legendary Resistance adds HP **per daily use**: 10 (expected CR 1–4), 20 (5–10), or 30 (11+). Regeneration adds 3 × its per-round amount. Find the HP band, then move the CR 1 step for every 2 points the AC is above or below the band's expected AC. Magic Resistance counts as +2 AC, and so do flying plus ranged attacks at CR ≤ 10. Vulnerabilities aren't adjusted.
- **Offensive:** model three rounds: use the best options, include recharge abilities on the first round, include legendary-action damage, and assume area effects hit two targets. Average the damage per round and find the DPR band. Then move the CR 1 step for every 2 points the attack bonus (or save DC, if that dominates) is above or below expected.
- **Final CR:** the average of defensive and offensive CR, rounded to the nearest whole step (round .5 up only if an uncounted feature, such as control effects, justifies it, and say so).
- **Check the internals:** dice averages (floor of the true average), HP = dice average + Con × dice, attack = proficiency + ability, save DC = 8 + proficiency + ability, saves and skills = ability + proficiency (+ proficiency again for expertise), and passive Perception = 10 + Perception bonus.

## Report back (keep it short)
One line per file: `file | stated CR → final CR | re-rated? | section | IP substitutions | anything odd`.
