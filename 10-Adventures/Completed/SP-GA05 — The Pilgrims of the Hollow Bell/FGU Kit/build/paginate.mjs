// Re-paginate a Homebrewery V3 brew by measuring with the real renderer + theme.
// Keeps the cover page and a hard break before every "# " chapter; fills pages greedily,
// never ends a page on a heading, and reports blocks too big for one page.
// usage: LOCAL_IMG=1 node paginate.mjs in.md out.md
import fs from 'fs';
import { createRequire } from 'module';
import pkg from 'marked-hbfm';
const { hbfm } = pkg;
const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const [,, inp, outp] = process.argv;
const raw = fs.readFileSync(inp, 'utf8');
const fm = (raw.match(/^---\n[\s\S]*?\n---\n/) || [''])[0];
let rest = raw.slice(fm.length);
const cm = (rest.match(/^\s*<!--[\s\S]*?-->\n*/) || [''])[0];
let body = rest.slice(cm.length);

const ids = fs.existsSync('ids.txt') ? Object.fromEntries(fs.readFileSync('ids.txt', 'utf8').trim().split('\n').map(l => l.split(' ').reverse())) : {};
const localize = t => process.env.LOCAL_IMG ? t.replace(/https:\/\/lh3\.googleusercontent\.com\/d\/([\w-]+)/g, (m, id) => ids[id] ? `http://localhost:8765/img/${ids[id]}.jpg` : m) : t;

// sections split on existing \page lines
const sections = body.split(/^\\page(?:break)?[^\n]*\n/m).map(s => s.replace(/^\s+|\s+$/g, ''));
const cover = sections.shift();
// group into chapters: a section starting with "# " opens a new chapter
const chapters = [];
for (const s of sections) {
  if (!s) continue;
  if (/^# /.test(s) || !chapters.length) chapters.push([s]); else chapters[chapters.length - 1].push(s);
}
function blocksOf(text) {
  const lines = text.split('\n'); const blocks = []; let cur = []; let depth = 0, fence = false;
  for (const l of lines) {
    if (/^```/.test(l)) fence = !fence;
    if (!fence) {
      const opens = (l.match(/{{(?![^{}]*}})/g) || []).length; const closes = (l.match(/(?<!{{[^{}]*)}}/g) || []).length;
      depth += opens - closes; if (depth < 0) depth = 0;
    }
    if (l.trim() === '' && depth === 0 && !fence) { if (cur.length) { blocks.push(cur.join('\n')); cur = []; } }
    else cur.push(l);
  }
  if (cur.length) blocks.push(cur.join('\n'));
  return blocks;
}
const isHeading = b => /^#{1,4} /.test(b) && !b.includes('\n');

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1000, height: 1200 } });
await page.goto('http://localhost:8765/brew.html', { waitUntil: 'networkidle' });
await page.evaluate(() => {
  const p = document.querySelector('.page'); const t = p.cloneNode(false); t.id = 'probe';
  t.innerHTML = '<div class="columnWrapper"></div>'; document.querySelector('.pages').prepend(t);
});
async function overflows(md) {
  const html = hbfm.render(localize(md) + `\n\n&nbsp;\n\\column\n&nbsp;`, 0);
  return page.evaluate(async (h) => {
    const p = document.getElementById('probe'); const cw = p.firstChild; cw.innerHTML = h;
    await Promise.all([...cw.querySelectorAll('img')].map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; })));
    const r = p.getBoundingClientRect(); const kids = [...cw.children];
    const tail = new Set(kids.slice(-3).filter(k => k.textContent.trim() === '' || k.textContent.trim() === '\u00a0'));
    let bad = false;
    cw.querySelectorAll('*').forEach(e => {
      let top = e; while (top.parentElement !== cw) top = top.parentElement; if (tail.has(top)) return;
      const q = e.getBoundingClientRect(); if (!q.width && !q.height) return;
      if (q.right > r.right + 2 || q.bottom > r.bottom + 2) bad = true;
    });
    return bad;
  }, html);
}

const outPages = []; const warnings = [];
for (const ch of chapters) {
  const blocks = blocksOf(ch.join('\n\n'));
  let cur = [];
  for (const b of blocks) {
    if (!cur.length) { cur = [b]; if (await overflows(b)) warnings.push('Too big for one page: ' + b.slice(0, 70).replace(/\n/g, ' ')); continue; }
    if (!(await overflows([...cur, b].join('\n\n')))) { cur.push(b); continue; }
    // close page; carry trailing headings forward
    const carry = []; while (cur.length > 1 && isHeading(cur[cur.length - 1])) carry.unshift(cur.pop());
    outPages.push(cur.join('\n\n')); cur = [...carry, b];
    if (await overflows(cur.join('\n\n'))) warnings.push('Overflow after carry: ' + b.slice(0, 70).replace(/\n/g, ' '));
  }
  if (cur.length) outPages.push(cur.join('\n\n'));
}
await browser.close();
const out = fm + cm + cover + '\n\n' + outPages.map(p => '\\page\n\n' + p).join('\n\n') + '\n';
fs.writeFileSync(outp, out);
console.log('chapters', chapters.length, 'pages', outPages.length + 1);
warnings.forEach(w => console.log('WARN', w));
