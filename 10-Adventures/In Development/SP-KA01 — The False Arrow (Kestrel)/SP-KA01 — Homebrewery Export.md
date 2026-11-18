---
type: build-guide
adventure: "SP-KA01"
section: internal
publish_order: 0
publish: false
tags: [build, homebrewery, SP-KA01]
---

# SP-KA01 — Homebrewery Export

Back to [[SP-KA01-The-False-Arrow]] · Process: [[Build-Pipeline]] · Manifest: [[SP-KA01 — Scene Index|Scene Index]]

> [!warning] Recipe, not yet run. Every scene is still `drafted`, and the Board blocks *Package* until all are `final`. Build the brew from the Longform compile (`SP-KA01 — Compiled.md`), not from the live scene files.

> [!warning] Kestrel images. The art lives in the Greyhawk folder (`10-Adventures/SP-GA01 — The False Arrow/images/`). **Do not use** `Cover.png` (D&D logo, "Chakyik Steppe" subtitle, Greyhawk UNV crest) or `regional-map.png` (Greyhawk labels) until they are redone. Check every other image for labels or logos before it ships (see the Board).

## Paste Order
Strip the YAML frontmatter from every file before pasting. Each part starts on a new page (`\page`).

| # | Part | Manifest (section · order) | Notes |
|---|---|---|---|
| 1 | Cover | — | `{{frontCover}}`, title, series line, cover art |
| 2 | [[SP-KA01-The-False-Arrow]] | overview · 10 | Strip list below; ends before Supporting Files |
| 3 | [[SP-KA01 — Scene 00 — Kestrel University]] | act-1 · 100 | |
| 4 | [[SP-KA01 — Scene 01 — The High Pass]] | act-1 · 110 | |
| 5 | [[SP-KA01 — Scene 02 — The Cold Welcome]] | act-1 · 120 | |
| 6 | [[SP-KA01 — Scene 03 — Trial of the Horse]] | act-2 · 130 | |
| 7 | [[SP-KA01 — Scene 04 — Trial of the Bow]] | act-2 · 140 | |
| 8 | [[SP-KA01 — Scene 05 — Night in Karash]] | act-2 · 150 | |
| 9 | [[SP-KA01 — Scene 06 — Trial of the Fire]] | act-2 · 160 | |
| 10 | [[SP-KA01 — Scene 07 — The War Council]] | act-3 · 170 | |
| 11 | [[SP-KA01 — The Favor Tracker]] | appendix-mechanics · 200 | Table card as a `{{note}}`; cut *At a Virtual Table* |
| 12 | [[SP-KA01 — Bestiary]] | appendix-bestiary · 210 | Every creature to `{{monster,frame}}`; minion packs included |
| 13 | Handouts 1–3 | appendix-handouts · 220–222 | One page each, so they can be printed and cut out |
| 14 | [[SP-GA01 — Map Assets]] | appendix-maps · 230 | Player copies only; Duel Ring has one copy |

Never paste: the Scene Index, the Board, the Developmental Edit, the Midjourney Prompt Pack, this note, or [[SP-KA01 — VTT and Fantasy Grounds Kit]].

## Strip List
- **Main note:** Adventure Code, Fantasy Grounds Build, Playtest Notes, Publishing, Supporting Files, the Continuity Ledger checklist, and nothing from Setting (it ships as written).
- The `<!-- DRAFT NOTE … -->` comment and its rename key, at the top of the main note.
- The `original:` link and any mention of the Greyhawk edition.
- **Scenes:** the nav line, every `**Budget:**` line. Keep *To the table* prompts as one italic DM line, or cut them for space.
- **Scene minion packs:** keep the one-line description; the statblock is already in the Bestiary.
- **Bestiary:** every *FGU Import* callout, and the one-row *At other APLs* tables.
- **Handouts:** any `## DM Notes` section and the `> **DM:**` line (the text below the rule is the handout).

## Conversion
| In this adventure | Becomes |
|---|---|
| Read-aloud lead line `> *…*` plus its "deliver these one at a time" beats | One `{{descriptive}}` block: the lead line, then the beats as a bullet list. Drop the "Then deliver…" instruction line. |
| NPC lines `> **Name:** *"…"*` | Plain markdown blockquote (Homebrewery renders it). No callout needed. |
| `> [!info]-` (Scene 00's optional color) | `{{note}}` with `##### Optional Color` as the first line |
| Statblocks | `{{monster,frame}}`; `___` between sections; `::` on stat lines (example below) |
| `> **Sidebar Press dressing.**` | A plain paragraph straight after its statblock |
| `[[Note|Label]]` / `[[Note]]` | `Label` / `Note` as plain text (or a `#anchor` link inside the brew) |
| `![[file.svg]]` / local images | A hosted PNG URL with a width (see Images) |
| Code-block table card (Favor Tracker) | Keep the code block, inside a `{{note}}` |

**Statblock example (Ochir):**
```
{{monster,frame
## Ochir the Cut-Rein
*Medium humanoid (human), neutral evil*
___
**Armor Class** :: 15 (studded leather)
**Hit Points**  :: 52 (8d8 + 16)
**Speed**       :: 30 ft.
___
|STR|DEX|CON|INT|WIS|CHA|
|:---:|:---:|:---:|:---:|:---:|:---:|
|12 (+1)|16 (+3)|14 (+2)|11 (+0)|12 (+1)|14 (+2)|
___
**Saving Throws** :: Dex +5
**Skills**        :: Animal Handling +3, Intimidation +4, Perception +3, Stealth +5
**Senses**        :: passive Perception 13
**Languages**     :: Karashi, Common, Amshari
**Challenge**     :: 2 (450 XP)
___
***Tent-City Born.*** Ochir has advantage on Dexterity (Stealth) checks made in the Karashi camp.
### Actions
***Multiattack.*** Two scimitar attacks or two horn bow attacks.
***Scimitar.*** *Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 6 (1d6 + 3) slashing.
***Horn Bow.*** *Ranged Weapon Attack:* +5 to hit, range 150/600 ft., one target. *Hit:* 7 (1d8 + 3) piercing.
### Bonus Actions
***Cut-Rein's Order (Recharge 5–6).*** One ally within 30 ft. that can hear Ochir uses its reaction to move up to half its speed and make one weapon attack.
}}
```

## Images
Host every image permanently: Homebrewery's own upload, Imgur, or `raw.githubusercontent.com` links from the vault repo (only if the repo is public). **Never Discord CDN links**; they expire in about a day. Use `{width:…}`, never height.

| File (in `images/`) | Pixels | Suggested place | Size |
|---|---|---|---|
| `Cover.png` | 768 × 1376 | Cover | full page, absolutely positioned — **replace first (Kestrel)** |
| `regional-map.png` | 1999 × 1545 | Overview, after the hook | `{{wide}}`, `{width:100%}` — **relabel first (Kestrel)** |
| `scene-ritterstadt.png`, `scene-job-board.png` | 2464 × 1856 · 1456 × 816 | Scene 00 | `{width:100%}` |
| `scene-hospice.png` | 1456 × 816 | Scene 01 | `{width:100%}` |
| `scene-camp-panorama.png` | 2944 × 1648 | Scene 01, First Sight | `{{wide}}`, `{width:100%}` |
| `scene-pavilion.png` | 1456 × 816 | Scene 02 | `{width:100%}` |
| `scene-black-stallion.png` | 2944 × 1648 | Scene 03 | `{{wide}}` or `{width:100%}` |
| `scene-fog-ravine.png` | 2944 × 1648 | Scene 04 | `{{wide}}` or `{width:100%}` |
| `scene-night-attack.png` | 1456 × 816 | Scene 05 | `{width:100%}` |
| `scene-sarnais-fire.png` | 1456 × 816 | Scene 06 | `{width:100%}` |
| `scene-war-council.png` | 1456 × 816 | Scene 07 | `{width:100%}` |
| `npc-*.png` (7 portraits) | 896 × 1344 | Beside each NPC's first scene | `{width:5cm}` (7.5 cm tall) |
| `item-*.png` (3) | 1024 × 1024 | Rewards; Handout 3 | `{width:4cm}` |
| `map-winter-camp.png` | 2688 × 1792 | Scene 02 or Appendix | `{{wide}}` |
| `scene-yeti.png`, `scene-temurs-bowl.png` | 1456 × 816 | **Unplaced.** No matching scene; check before using | — |
| Battlemaps (Player PNGs, 100 px/sq) | see Map Assets | Appendix — Maps | `{width:100%}` |

## Pre-Flight
- [ ] No `> [!` callouts left anywhere
- [ ] No YAML frontmatter pasted
- [ ] No wikilink brackets or `![[` embeds left
- [ ] Every `\page` lands where intended; no orphaned headings
- [ ] Every image uses width and a permanent URL (no Discord links)
- [ ] Every statblock is a `{{monster,frame}}` with `___` and `::`; FGU import text removed
- [ ] `{{pageNumber,auto}}` and a footnote on each page
- [ ] Handouts each on their own page; Bestiary and maps at the back
- [ ] Kestrel: a search of the finished brew for Greyhawk, Iuz, Yecha, Chakyik, Cligir, Baklunish, Perrenland and Ekbir returns nothing
- [ ] PDF exported (Chrome: Print → Save as PDF, background graphics on); spot-check page count and art

## Export Log
| Date | Brew link | PDF | Notes |
|---|---|---|---|
| | | | |
