<%*
/*
  Sidebar Press — Board Auto-Mover (Templater startup script)
  ------------------------------------------------------------
  Keeps every adventure folder in the right place:
    10-Adventures/Completed/       every checkbox on its "— Board" ticked
    10-Adventures/In Development/  anything else, or no board at all
  10-Adventures/Pocket Modules/ is never touched.

  Runs once 3 seconds after Obsidian opens (a full sweep, which also sorts
  any new adventure folder created directly under 10-Adventures), then
  re-checks a board 1.5 seconds after you edit it. Folders move through
  Obsidian, so wikilinks update automatically (Settings → Files & Links →
  "Automatically update internal links" must stay on).

  Registered in Templater → Settings → Startup templates. Do not insert
  this template into a note.
*/
const Notice = tp.obsidian.Notice;
if (window.__spBoardMover) {
  new Notice("Board Auto-Mover already running.", 3000);
} else {
  window.__spBoardMover = true;
  new Notice("Board Auto-Mover loaded; sorting adventures…", 4000);

  const ROOT = "10-Adventures";
  const DEV  = ROOT + "/In Development";
  const DONE = ROOT + "/Completed";
  const SKIP = [ROOT + "/Pocket Modules", DEV, DONE];
  const busy = new Set();

  const get = (p) => app.vault.getAbstractFileByPath(p);
  const isFolder = (f) => f && Array.isArray(f.children);
  const isBoard = (f) => f && f.extension === "md" && /— Board$/.test(f.basename);
  const ensureFolder = async (p) => { if (!get(p)) await app.vault.createFolder(p); };

  // A board counts as complete when it has at least one task and no open ones.
  // The Kanban settings block at the bottom is ignored.
  const boardComplete = async (file) => {
    const body = (await app.vault.read(file)).split("%% kanban:settings")[0];
    const open = (body.match(/^\s*[-*+] \[ \]/gm) || []).length;
    const done = (body.match(/^\s*[-*+] \[[xX]\]/gm) || []).length;
    return open === 0 && done > 0;
  };

  const boardOf = (folder) => folder.children.find(isBoard);

  const place = async (folder, complete) => {
    const target = complete ? DONE : DEV;
    if (folder.parent.path === target || busy.has(folder.path)) return;
    const dest = target + "/" + folder.name;
    if (get(dest)) { new Notice(`Board Auto-Mover: "${dest}" already exists; left "${folder.name}" where it is.`, 8000); return; }
    busy.add(folder.path);
    try {
      await ensureFolder(target);
      await app.fileManager.renameFile(folder, dest);
      new Notice(`${folder.name} → ${complete ? "Completed ✅" : "In Development"}`, 6000);
    } catch (e) {
      console.error("Board Auto-Mover", e);
      new Notice(`Board Auto-Mover could not move "${folder.name}": ${e.message}`, 10000);
    } finally { busy.delete(folder.path); }
  };

  // The adventure folder is the board's own folder, sitting directly in ROOT, DEV or DONE.
  const checkBoard = async (file) => {
    const folder = file.parent;
    if (!folder || !folder.parent || SKIP.includes(folder.path)) return;
    if (![ROOT, DEV, DONE].includes(folder.parent.path)) return;
    await place(folder, await boardComplete(file));
  };

  const sweep = async () => {
    if (!get(ROOT)) return;
    await ensureFolder(DEV); await ensureFolder(DONE);
    for (const parentPath of [ROOT, DEV, DONE]) {
      for (const f of [...(get(parentPath)?.children || [])]) {
        if (!isFolder(f) || SKIP.includes(f.path)) continue;
        const board = boardOf(f);
        await place(f, board ? await boardComplete(board) : false);
      }
    }
  };

  const timers = new Map();
  app.metadataCache.on("changed", (file) => {
    if (!isBoard(file)) return;
    clearTimeout(timers.get(file.path));
    timers.set(file.path, setTimeout(() => checkBoard(file), 1500));
  });
  const runSweep = () => sweep()
    .then(() => new Notice("Board Auto-Mover: sweep finished.", 4000))
    .catch(e => { console.error("Board Auto-Mover", e); new Notice("Board Auto-Mover sweep failed: " + e.message, 10000); });
  app.workspace.onLayoutReady(() => setTimeout(runSweep, 3000));
}
%>
