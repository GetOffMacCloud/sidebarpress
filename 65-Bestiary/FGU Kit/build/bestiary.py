"""Sidebar Press Bestiary: every homebrew/converted creature in the vault as one FGU 5E module.
Sources: 65-Bestiary (FGU Import blocks), 30-NPCs, the Minion templates, and conversion kits.
Run:  FG_DIR="$HOME/mnt/Fantasy Grounds" FG_WORK="$HOME/fgwork/bestiary" python3 bestiary.py [--test|--install]"""
import os,sys,re,glob,html,shutil
V=os.path.abspath(os.path.join(os.path.dirname(__file__),'../../..'))
sys.path.insert(0,os.path.join(V,'70-Company/Tools/fgu-module-builder'))
import fgmod,fgconv,fgtext
import xml.etree.ElementTree as ET
NAME='Sidebar Press Bestiary'; FG=os.environ['FG_DIR']; WORK=os.environ['FG_WORK']
CONV=[  # conversion kits: (category, import-text file, {block index range: subcategory})
 ('C12 Raanet',V+'/00-Conversion Projects/C12 - The Forgotten Library of Raanet/FGU Kit/C12 - FG NPC Import.txt')]
KEEP=('Lore','Ecology','Tactics','Lair Actions','Lair / Regional Effects','Regional Effects','Variants','Named Example','Adventure Hooks','Spoils')
def fm(t):
    d={}
    if t.startswith('---'):
        for l in t.split('\n---',1)[0].split('\n')[1:]:
            m=re.match(r'^(\w+):\s*"?([^"#]*?)"?\s*(#.*)?$',l)
            if m: d[m.group(1)]=m.group(2)
    return d
def slug(x): return re.sub(r'[^a-z0-9]+','-',x.lower()).strip('-')
m=fgmod.Mod(NAME,NAME,'Sidebar Press',"Sidebar Press",FG,WORK)
os.makedirs(WORK,exist_ok=True)
# ---------- collect
ENTRIES=[]  # (group, statblock dict, notes xml, portrait src)
for f in sorted(glob.glob(V+'/65-Bestiary/**/*.md',recursive=True))+sorted(glob.glob(V+'/30-NPCs/*.md')):
    if '/FGU Kit/' in f: continue
    t=open(f).read(); meta=fm(t); bl=fgtext.blocks_md(t)
    if not bl: continue
    sec=meta.get('section',''); sub=os.path.relpath(os.path.dirname(f),V+'/65-Bestiary')
    if '/30-NPCs/' in f: grp='Named NPCs'
    elif sec in ('minions',) or meta.get('type')=='fgu-templates': grp='Minion Templates'
    elif sec=='rogues-gallery': grp="Rogues' Gallery"
    elif sub not in ('.','Minions'): grp=sub
    else: grp='Creatures'
    b=fgconv.body(f); S=fgconv.sections(b)
    ra=re.search(r'^# .*\n+\*([^*\n].*?)\*\s*$',b,re.M)
    notes=('<frame>%s</frame>'%fgconv.inline(ra.group(1)) if ra and grp!='Minion Templates' else '')
    for k in KEEP:
        if k in S and S[k].strip(): notes+='<h>%s</h>'%k+fgconv.conv(S[k])
    if grp=='Named NPCs':
        pre=b.split('\n## ',1)[0]; pre=re.sub(r'^# .*$','',pre,flags=re.M); notes=fgconv.conv(pre)
    fgconv.SEEN.clear()
    por=None
    for d in [fgtext.parse(x) for x in bl]:
        p=os.path.join(V,'99-Assets/SP-OM01/portraits',d['name']+' — Portrait.png')
        por=p if os.path.exists(p) else None
        ENTRIES.append((grp,d,notes,por,os.path.basename(f)[:-3]))
for cat,path in CONV:
    t=open(path).read(); parts=re.split(r'^(#{8} .* #{8}|#### .*####)\s*$',t,flags=re.M); sub=cat
    for x in parts:
        if x.startswith('########'): sub=cat+(' — Summonable Creatures' if 'PART 2' in x.upper() else ' — Module Creatures'); continue
        if x.startswith('####'): continue
        if re.search(r'^Armor Class',x,re.M) and re.search(r'^Challenge',x,re.M):
            ENTRIES.append((sub,fgtext.parse(x.strip()),'',None,'C12'))
# ---------- portraits
src=os.path.join(WORK,'src'); shutil.rmtree(src,ignore_errors=True); os.makedirs(src)
for g,d,n,p,f in ENTRIES:
    if p: shutil.copy(p,os.path.join(src,'npc-'+slug(d['name'])+'.png'))
m.images(src)
# ---------- npcs, one FG category per group
root=ET.SubElement(m.root,'npc'); CATS={}
def cat(g):
    if g not in CATS: CATS[g]=ET.SubElement(root,'category',{'name':g})
    return CATS[g]
m.cat['npc']=None; used=set(); ROWS=[]; NN={}; m.npcname=lambda k: NN[k]
for g,d,notes,p,f in ENTRIES:
    key=slug(d['name']).replace('-','')[:40] or 'npc'
    if key in used:
        k2=key+slug(g).replace('-','')[:10]; key=k2 if k2 not in used else key+str(len(used))
    used.add(key); m.cat['npc']=cat(g)
    tx='<h>%s</h>%s<p><i>Sidebar Press %s. Source: %s.</i></p>'%(html.escape(d['name']),notes,'conversion' if g.startswith('C12') else 'homebrew',html.escape(f))
    pic='npc-'+slug(d['name']) if p and ('npc-'+slug(d['name'])) in m.IMG else None
    fgtext.add(m,key,d,tx,pic); ROWS.append((g,d,key)); NN[key]=d['name']
# ---------- reference pages
def crv(c):
    try: return eval(c)
    except Exception: return 0
intro=('<p>Every Sidebar Press creature, villain, minion template and conversion statblock in one module. '
 'Load it alongside any campaign and drag creatures straight into encounters or the combat tracker.</p>'
 '<p><b>Groups.</b> '+', '.join('%s (%d)'%(g,sum(1 for r in ROWS if r[0]==g)) for g in CATS)+'.</p>'
 '<p>Statblocks are generated from each vault note\'s FGU Import block. Re-run <i>65-Bestiary/FGU Kit/build/bestiary.py</i> after any statblock change.</p>')
m.page('Introduction','About This Bestiary',intro)
for g in CATS:
    rows=sorted([r for r in ROWS if r[0]==g],key=lambda r:(crv(r[1]['cr']),r[1]['name']))
    tb='<table><tr><td><b>Creature</b></td><td><b>CR</b></td><td><b>Type</b></td></tr>'+''.join('<tr><td>%s</td><td>%s</td><td>%s</td></tr>'%(html.escape(d['name']),d['cr'],html.escape(d['size']+' '+d['type'])) for _,d,k in rows)+'</table>'
    m.page('Groups',g,tb,links=[m.N(k) for _,_,k in rows])
allr=sorted(ROWS,key=lambda r:(crv(r[1]['cr']),r[1]['name']))
for lo,hi,lab in ((0,1,'CR 0–1'),(2,4,'CR 2–4'),(5,10,'CR 5–10'),(11,30,'CR 11+')):
    rr=[r for r in allr if lo<=crv(r[1]['cr'])<=hi or (lo==0 and crv(r[1]['cr'])<1)]
    if lo==2: rr=[r for r in allr if 1<crv(r[1]['cr'])<=4]
    tb='<table><tr><td><b>Creature</b></td><td><b>CR</b></td><td><b>Group</b></td></tr>'+''.join('<tr><td>%s</td><td>%s</td><td>%s</td></tr>'%(html.escape(d['name']),d['cr'],html.escape(g)) for g,d,k in rr)+'</table>'
    m.page('By Challenge',lab,tb,links=[m.N(k) for _,_,k in rr])
out=os.path.join(V,'65-Bestiary/FGU Kit',NAME+('.test' if '--test' in sys.argv else '')+'.mod')
m.build(out)
if '--install' in sys.argv: shutil.copy(out,os.path.join(FG,'modules',NAME+'.mod')); print('installed')
