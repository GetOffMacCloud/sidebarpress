---
type: process
---

# Build Pipeline — from scene files to one book

Every adventure is written as pieces and assembled once. The pieces live in `10-Adventures/SP-PBS-NN — Title/`; the assembly order lives in that adventure's [[00 — Scene Index]] (the **manifest**). Progress is tracked on `SP-PBS-NN — Board`.

## 1. The manifest

Every file that can ship carries four frontmatter keys:

| Key | Values | Meaning |
|---|---|---|
| `adventure` | `"SP-PBS-NN"` | The join key. Same on every file of the adventure, including the main note. |
| `section` | `overview` · `act-1` · `act-2` · `act-3` · `appendix-mechanics` · `appendix-bestiary` · `appendix-handouts` · `appendix-maps` · `internal` | Where the file lands in the book. `internal` never ships. |
| `publish_order` | integer, gaps of 10 | Paste order within the book. `0` for internal files. |
| `publish` | `true` / `false` | Whether the file ships at all. |

Scenes also carry `status`: `outline` → `drafted` → `edited` → `final`.

The Scene Index renders the manifest as a Dataview table. It is also the **Longform project index**: its `longform:` block lists the scenes in order, and Longform's *Compile* produces the prose of acts 1–3 as a single file.

## 2. Compile

1. Confirm every shipping scene is `status: final` (the board blocks *Package* until this is true).
2. Open the Scene Index → Longform pane → **Compile**. Save the output as `SP-PBS-NN — Compiled.md` in the adventure folder (`section: internal`, `publish: false`).
3. Assemble the book in manifest order: overview → compiled scenes → appendices.

## 3. Strip list (never ships)

From the **main note**: Adventure Code, Fantasy Grounds Build, Playtest Notes, Publishing, Supporting Files, the Canon Check checkboxes (the *table* ships as "Sources").
From **scenes**: the nav line (`[[00 — Scene Index]] · ← …`), `**Budget:**` lines, "To the table:" prompts (keep as DM sidebars if desired).
From the **Scene Index**: everything (internal).
From **handouts**: any `## DM Notes` section.

## 4. Convert

Homebrewery conversion rules (callouts → statblock frames, read-aloud → descriptive boxes, page breaks per scene, image sizing in cm) are handled in the packaging pass. Statblocks are in `> [!example]-` callouts; each becomes a `{{monster,frame}}` block.

## 5. Ship

Export PDF, build the FG module, add the row to [[Release-Tracker]], move the board's last cards to *Done*.

## Dashboards
- [[Pipeline-Dashboard]] — every adventure, its status, and scene progress at a glance.
- Each adventure's board — the definition of done, in five columns.
