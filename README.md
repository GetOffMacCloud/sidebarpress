# Sidebar Press Vault

The Obsidian vault for **Sidebar Press, LLC** — adventure writing for D&D 2014 5e, set in the World of Greyhawk.

## Folder Guide

| Folder | Purpose |
| ------------------------- | ---------------------------------------------------------------------- |
| `00-Inbox` | Raw ideas, half-formed hooks, things not yet filed. Clear weekly. |
| `10-Adventures` | One folder per adventure. The product pipeline. |
| `20-World/Greyhawk-Canon` | Canon reference only. Every note cites its edition and source. |
| `20-World/Homebrew` | Your inventions for the setting. Marked clearly as non-canon. |
| `30-NPCs` | Named NPCs. One note each, linked from everywhere they appear. |
| `40-Locations` | Places. Linked from adventures and lore. |
| `50-Items` | Magic items, artifacts, notable treasure. |
| `60-Continuity` | The connective tissue: plot threads, timeline, dangling hooks. |
| `70-Company` | Publishing checklists, release tracker, style guide. |
| `80-Sessions` | Actual-play logs from your table, used to validate adventures. |
| `90-Templates` | Note templates (Adventure, Scene, Scene-Index, Adventure-Board, NPC, Location, Item, Lore, Plot-Thread, Session-Log). Copy, don't edit. |
| `99-Assets` | Maps, handouts, art. Subfolder per adventure code. |

## Core Rules

1. **Canon notes never contain homebrew.** If you invent something, it goes in `20-World/Homebrew` with a link to the canon it's based on.
2. **Every NPC, location, and item gets one note.** Adventures link to them; never duplicate them.
3. **Plot threads live in `60-Continuity`.** Adventures reference threads, they don't own them.
4. **Source everything.** Canon notes require edition + book + page. See the Lore template.
5. **Dates use Greyhawk reckoning** (e.g. 576 CY) in-world, with real-world dates in frontmatter. The house default is **576 CY**, the *World of Greyhawk* (1983) baseline. An adventure set in another year must say so in its frontmatter (`in_world_date`) and be listed under "Adventures Set Outside 576 CY" in [[Timeline]].

## Naming

- **Adventure codes:** `SP-PBS-NN`, a two-digit sequence (`SP-PBS-01`, `SP-PBS-02`, …). Codes are sequential and never reused, even for scrapped adventures.
- **Adventure folders:** `10-Adventures/SP-PBS-NN — Title/`, e.g. `SP-PBS-02 — The Bones of the Dreadverge/`.
  - Main note: `SP-PBS-NN-Title-Slug.md`, e.g. `SP-PBS-02-The-Bones-of-the-Dreadverge.md`.
  - Supporting notes: `SP-PBS-NN — Bestiary.md`, `SP-PBS-NN — Handout — <Title>.md`, and so on.
  - Scene notes: `Scenes/00 — Scene Index.md` and `Scenes/Scene NN — <Title>.md`.
- **Assets:** `99-Assets/SP-PBS-NN/`, with files prefixed `SP-PBS-NN - `.
- **NPCs / Locations / Items:** natural names, e.g. `Mordenkainen.md`, `Greyhawk-City.md`.
- **Canon lore:** topic-based, e.g. `The-Greyhawk-Wars.md`.

## How an Adventure Is Built

Pieces first, one book at the end. See [[Build-Pipeline]] for the full procedure.

1. **Frame** — copy [[90-Templates/Adventure]], [[90-Templates/Scene-Index]] and [[90-Templates/Adventure-Board]] into the new folder; replace `SP-PBS-NN`.
2. **Write** — one note per scene from [[90-Templates/Scene]]; NPCs, locations and items get their own notes outside the adventure folder.
3. **Track** — the adventure's `Board` note is the definition of done (Frame → Write → Edit → Package → Release). The [[Pipeline-Dashboard]] shows every adventure at once.
4. **Assemble** — the Scene Index is the **manifest** (`section` + `publish_order` + `publish` on every file) and the **Longform project**. Compile scenes with Longform, paste overview and appendices around them in manifest order.

Plugins are kept to the minimum that serves this flow; see [[Plugin-Policy]].

> The earlier `A01-The-Sunken-Crypt.md` pattern is retired. The `A00-Sample.md` note and the template placeholders still show it; read `A00`/`A01` there as `SP-PBS-NN`.
