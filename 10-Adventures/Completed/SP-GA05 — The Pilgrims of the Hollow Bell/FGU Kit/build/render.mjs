// Render a Homebrewery V3 brew to static HTML using the real hbfm renderer and theme CSS.
// usage: node render.mjs brew.md out.html [theme=5ePHB]
import fs from 'fs';
import pkg from 'marked-hbfm';
const { hbfm } = pkg;
const [,, inp, out, theme='5ePHB'] = process.argv;
let text = fs.readFileSync(inp, 'utf8');
text = text.replace(/^---\n[\s\S]*?\n---\n/, '');          // Obsidian frontmatter (not pasted)
text = text.replace(/^<!--[\s\S]*?-->\n*/, '');            // header comment
if (process.env.LOCAL_IMG) { // measure with local copies of the hosted images
  const ids = Object.fromEntries(fs.readFileSync('ids.txt','utf8').trim().split('\n').map(l => l.split(' ').reverse()));
  text = text.replace(/https:\/\/lh3\.googleusercontent\.com\/d\/([\w-]+)/g, (m, id) => ids[id] ? `/img/${ids[id]}.jpg` : m);
}
// split exactly like brewRenderer.jsx
let style = '';
const sm = text.match(/<!-- HB-STYLE\n([\s\S]*?)\nHB-STYLE -->/);
if (sm) { style = sm[1]; text = text.replace(sm[0], ''); }
const pages = text.split(/^(?=\\page(?:break)?(?: *{[^\n{}]*})?$)/m);
let html = '';
pages.forEach((p, i) => {
  let cls = 'page'; let st = '';
  if (p.startsWith('\\page')) {
    const t = hbfm.marked.lexer(p.split('\n', 1)[0])[0].tokens;
    const inj = t?.find(o => o.injectedTags !== undefined)?.injectedTags;
    if (inj) { cls = [cls, inj.classes].join(' ').trim();
      st = Object.entries(inj.styles || {}).map(([k, v]) => `${k}:${v}`).join(';'); }
    p = p.includes('\n') ? p.substring(p.indexOf('\n') + 1) : '';
  }
  p += `\n\n&nbsp;\n\\column\n&nbsp;`;
  const body = hbfm.render(p, i);
  html += `<div class="${cls}" id="p${i + 1}" style="${st}"><div class="columnWrapper">${body}</div></div>\n`;
});
const doc = `<!DOCTYPE html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="/themes/V3/Blank/style.css">
${theme !== 'Blank' ? `<link rel="stylesheet" href="/themes/V3/${theme}/style.css">` : ''}
<style>body{margin:0;background:#888} .pages{display:flex;flex-direction:column;gap:10px;align-items:center} ${style}</style>
</head><body><div class="brewRenderer"><div class="pages">${html}</div></div></body></html>`;
fs.writeFileSync(out, doc);
console.log('pages', pages.length);
