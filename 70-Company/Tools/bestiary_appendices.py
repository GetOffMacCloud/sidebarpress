"""Sidebar Press: regenerate the static appendix tables (by Challenge, by Environment) from creature frontmatter.
Usage: python3 bestiary_appendices.py "<vault>/65-Bestiary"
"""
import os, sys, yaml, glob
d = sys.argv[1]
rows = []
for p in glob.glob(os.path.join(d, "*.md")):
    t = open(p, encoding="utf-8").read()
    if not t.startswith("---"): continue
    fm = yaml.safe_load(t.split("---")[1])
    if fm.get("type") != "creature": continue
    fm["_stem"]=os.path.basename(p)[:-3]
    rows.append(fm)
rows.sort(key=lambda r: (r["cr_num"], r["creature"]))
def lk(r): return f'[[{r["_stem"]}]]' if r['_stem']==r['creature'] else f'[[{r["_stem"]}|{r["creature"]}]]'
def sec(r): return "Rogues' Gallery" if r.get("section") == "rogues-gallery" else "Bestiary"
def crs(r): return "—" if r["cr"] == "none" else r["cr"]
def xps(r): return "—" if r["cr"] == "none" else f'{r["xp"]:,}'
out = ['---','type: appendix','adventure: "SP-BST-01"','section: appendix-tables','publish_order: 9000','publish: true','status: drafted','---','',
       '# Creatures by Challenge','',
       '*Generated from each entry\'s frontmatter. Regenerate after changing a CR.*','',
       '| CR | XP | Creature | Type | Origin | Section |','|---|---|---|---|---|---|']
for r in rows:
    out.append(f'| {crs(r)} | {xps(r)} | {lk(r)} | {r["size"]} {r["creature_type"]} | {r["origin"]} | {sec(r)} |')
out += ['', '**Template:** [[Bone Beast Template]] — apply to any *Monster Manual* beast; CR unchanged.', '']
open(os.path.join(d, "90 — Creatures by Challenge.md"), "w", encoding="utf-8").write("\n".join(out))
envs = {}
for r in rows:
    for e in r.get("environment", []):
        envs.setdefault(e, []).append(r)
out = ['---','type: appendix','adventure: "SP-BST-01"','section: appendix-tables','publish_order: 9100','publish: true','status: drafted','---','',
       '# Creatures by Environment','',
       '*Generated from each entry\'s frontmatter. Creatures are listed by CR within each environment.*','',
       '| Environment | Creatures (CR) |','|---|---|']
for e in sorted(envs):
    lst = ", ".join(f'{lk(r)} ({crs(r)})' for r in envs[e])
    out.append(f'| {e.capitalize()} | {lst} |')
out.append('')
open(os.path.join(d, "91 — Creatures by Environment.md"), "w", encoding="utf-8").write("\n".join(out))
print(len(rows), "creatures;", len(envs), "environments")
