---
type: process
---

# Plugin Policy

The vault runs on plain Markdown + frontmatter. Plugins are *consumers* of that data, never owners of it. Anything that only works inside a plugin's own format is out.

## Keep
| Plugin | Job | Replace with? |
|---|---|---|
| **Longform** | Compiles scene files into one document. Project index = each adventure's `00 — Scene Index`. | — |
| **Dataview** | Renders the manifests, [[Pipeline-Dashboard]], and any "what's missing" query. | — |
| **Kanban** | The per-adventure board (definition of done). Board files are plain checklists, so nothing is lost if the plugin goes. | — |
| **Obsidian Git** | Auto-commit/push every 10 min (`vault auto-sync`). This is the one with the configured settings. | — |
| **Fantasy Statblocks** *(optional)* | Rendered statblocks. Bestiaries currently use plain callouts, so it is not load-bearing. | Plain callouts (current) |

## Remove
| Plugin | Why |
|---|---|
| **Git Obsi Sync** | Second git plugin, no configuration; two auto-committers fight. |
| **StoryLine** | Wants its own `Scenes/` + `Codex/` layout and JSON state; overlaps Longform + Kanban. |
| **Codex Narrative Engine** | Expects its own `_codex/templates`; link-checking is useful but we do it in review. Delete `_codex/` with it. |
| **The DM Compendium** | Table-running tool, not a writing tool. |
| **BRAT** | Only needed to install beta plugins. |
| **Folder Notes** | Cosmetic; the main note already names the folder. |
| **Admonition** | Native callouts cover every case used in the vault. |
| **Style Settings** | Keep only if the active theme needs it. |

## Rules
1. Any plugin that needs its own folder or data format must be justified here before install.
2. Templates live in `90-Templates` only. One scheme.
3. If a plugin can be removed and the vault still reads correctly in plain Obsidian, it is allowed.
