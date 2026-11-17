"""Sidebar Press Bestiary: every homebrew/converted creature in the vault as one FGU 5E module,
laid out like the FGU D&D Monster Manual (Legacy): Introduction, Monsters A-Z, Rogues' Gallery,
appendices (minion templates, named NPCs, C12 conversions); NPCs By CR / Letter / Type lists.
Run:  FG_DIR="$HOME/mnt/Fantasy Grounds" FG_WORK="$HOME/fgwork/bestiary" python3 bestiary.py [--test|--install]"""
import os,sys,re,glob,html,shutil
V=os.path.abspath(os.path.join(os.path.dirname(__file__),'../../..'))
sys.path.insert(0,os.path.join(V,'70-Company/Tools/fgu-module-builder')); sys.path.insert(0,os.path.dirname(__file__))
import fgconv,fgtext
from bmod import BMod
from prompt_subjects import S as LOOK
NAME='Sidebar Press Bestiary'; FG=os.environ['FG_DIR']; WORK=os.environ['FG_WORK']; os.makedirs(WORK,exist_ok=True)
C12=V+'/00-Conversion Projects/C12 - The Forgotten Library of Raanet'
LORE=('Lore',); BODY=('Ecology','Tactics','Adventure Hooks','Spoils'); BOX=('Lair Actions','Lair / Regional Effects','Regional Effects','Variants','Named Example')
def fm(t):
    d={}
    if t.startswith('---'):
        for l in t.split('\n---',1)[0].split('\n')[1:]:
            m=re.match(r'^(\w+):\s*"?([^"#]*?)"?\s*(#.*)?$',l)
            if m: d[m.group(1)]=m.group(2)
    return d
slug=lambda x: re.sub(r'[^a-z0-9]+','-',x.lower()).strip('-')
m=BMod(NAME,NAME,'Sidebar Press','Sidebar Press',FG,WORK)
# ---------- collect notes -> pages
PAGES=[]   # dict(chapter, sub, name, blocks: statblock dicts, lore, body, boxes, portrait)
def letter(n): n=re.sub(r'^(The) ','',n); return n[0].upper()
for f in sorted(glob.glob(V+'/65-Bestiary/**/*.md',recursive=True))+[V+'/30-NPCs/%s.md'%n for n in ('Brother Ossian','Brother-Reaper Ansgar Vell','Cathal Red-Torc','Grukka One-Tusk','Sister Halse')]:
    if '/FGU Kit/' in f: continue
    t=open(f).read(); meta=fm(t); bl=fgtext.blocks_md(t)
    if not bl: continue
    name=os.path.basename(f)[:-3]; sec=meta.get('section','')
    b=fgconv.body(f); Sx=fgconv.sections(b); c=lambda k: fgconv.conv(Sx[k]) if k in Sx and Sx[k].strip() else ''
    ra=re.search(r'^# .*\n+\*([^*\n].*?)\*\s*$',b,re.M)
    if '/30-NPCs/' in f:
        pre=re.sub(r'^# .*$','',b.split('\n## ',1)[0],flags=re.M); ch,sub='Appendix B: Named NPCs','Named NPCs'
        lore=fgconv.conv(pre); body=''; boxes=[]
    elif meta.get('type')=='fgu-templates':
        role=name.split(' — ')[0]; rn=V+'/65-Bestiary/%s.md'%role
        rb=fgconv.body(rn) if os.path.exists(rn) else ''; rs=fgconv.sections(rb)
        keep=[k for k in rs if not re.search(r'FGU|Art Prompt|Design Notes|Appears In',k)]
        ch,sub,name='Appendix A: Minion Templates','Minion Templates',role
        lore=fgconv.conv(re.sub(r'^# .*$','',rb.split('\n## ',1)[0],flags=re.M))+''.join('<h>%s</h>%s'%(html.escape(k),fgconv.conv(rs[k])) for k in keep)
        body=''; boxes=[]
    else:
        if sec=='rogues-gallery': ch,sub="Rogues' Gallery",letter(name)
        else: ch,sub='Monsters',letter(name)
        lore=('<p><i>%s</i></p>'%fgconv.inline(ra.group(1)) if ra else '')+c('Lore')
        body=''.join('<h>%s</h>%s'%(k,c(k)) for k in BODY if c(k))
        boxes=['<h>%s</h>%s'%(k,c(k)) for k in BOX if c(k)]
    fgconv.SEEN.clear()
    stats=[fgtext.parse(x) for x in bl]
    por=os.path.join(V,'99-Assets/Bestiary/FGU/Portraits',name+' — Portrait.png')
    PAGES.append(dict(ch=ch,sub=sub,name=name,stats=stats,lore=lore,body=body,boxes=boxes,por=por if os.path.exists(por) else None,cat=ch if ch!='Monsters' else 'Monsters'))
# ---------- C12 conversions (Appendix C)
sb=open(C12+'/C12 - Summoning Bestiary (5e).md').read()
ONEE={m_.group(1).strip():(m_.group(2),m_.group(3)) for m_ in re.finditer(r'^> \[!example\][-+]? (.+?) [·—-] CR[^\n]*?(?:· \*([^*]*)\*)?\n> \*1e(?: \([^)]*\))?: ([^\n]*)\*',sb,re.M)}
t=open(C12+'/FGU Kit/C12 - FG NPC Import.txt').read(); part=''
for hdr,x in re.findall(r'^(#### .*?####)\s*$\n(.*?)(?=^####|\Z)',t,re.M|re.S):
    x=re.split(r'^########',x,flags=re.M)[0]
    if not re.search(r'^Armor Class',x,re.M): continue
    st=fgtext.parse(x.strip()); n=st['name']; num=int(re.match(r'#### (\d+)',hdr).group(1))
    where=re.search(r'\(([^)]*Area[^)]*)\)',hdr)
    sub='Module Creatures' if num<=16 else 'Summonable Creatures'
    look=LOOK.get(n) or LOOK.get(n+' (summoned)') or next((v for k,v in LOOK.items() if k.startswith(n.split(',')[0])),None)
    lore='<p><i>%s.</i></p>'%html.escape(look[0][0].upper()+look[0][1:]) if look else ''
    if where: lore+='<p><b><i>In C12. </i></b>Found in %s of the Temple Incandescent.</p>'%html.escape(where.group(1).replace('Area','Area').replace('wandering','and as a wandering monster'))
    k1=next((k for k in ONEE if k.startswith(n.split(',')[0])),None)
    if k1:
        tab,one=ONEE[k1]; lore+='<p><b><i>Summoning. </i></b>Appears on the <i>Monster Summoning</i> tables%s.</p><p><b><i>1e source. </i></b>%s</p>'%((' ('+html.escape(tab)+')') if tab else '',html.escape(one))
    PAGES.append(dict(ch='Appendix C: C12 Conversions',sub=sub,name=n,stats=[st],lore=lore,body='',boxes=[],por=None,cat='C12 Raanet — '+sub))
# ---------- portraits
src=os.path.join(WORK,'src'); shutil.rmtree(src,ignore_errors=True); os.makedirs(src)
for p in PAGES:
    if p['por']: shutil.copy(p['por'],os.path.join(src,'npc-'+slug(p['name'])+'.png'))
for p in glob.glob(V+'/99-Assets/Bestiary/FGU/Portraits/*— Portrait.png'):
    n=os.path.basename(p).split(' — ')[0]
    for q in PAGES:
        if q['name']==n and q['ch'].startswith('Appendix C'): q['por']=p; shutil.copy(p,os.path.join(src,'npc-'+slug(n)+'.png'))
m.images(src)
# ---------- NPC records (MM style: title, image link, lore, sidebars)
import xml.etree.ElementTree as ET
root=ET.SubElement(m.root,'npc'); CATS={}; NN={}; used=set()
def cat(g):
    if g not in CATS: CATS[g]=ET.SubElement(root,'category',{'name':g})
    return CATS[g]
m.npcname=lambda k: NN[k]
for p in PAGES:
    img='npc-'+slug(p['name']) if p['por'] and 'npc-'+slug(p['name']) in m.IMG else None; p['img']=img; p['keys']=[]
    for d in p['stats']:
        key=re.sub(r'[^a-z0-9]','',d['name'].lower())[:40] or 'npc'
        while key in used: key+='x'
        used.add(key); m.cat['npc']=cat(p['cat'])
        tx='<h>%s</h>'%html.escape(d['name'])
        if img: tx+='<linklist><link class="imagewindow" recordname="image.%s"><b>Image: </b>%s</link></linklist>'%(m.IMG[img][0],html.escape(p['name']))
        tx+=p['lore']+p['body']+''.join(p['boxes'])
        tx+='<p><i>Sidebar Press %s.</i></p>'%('conversion' if p['ch'].startswith('Appendix C') else 'homebrew')
        tk=os.path.join(V,'99-Assets/Bestiary/FGU/Tokens',p['name']+' — Token.png'); tok=None
        if os.path.exists(tk):
            arc='tokens/%s.png'%slug(p['name']); tok=arc+'@'+NAME
            if (tk,arc) not in m.extra: m.extra.append((tk,arc))
        fgtext.add(m,key,d,tx,img,tok); NN[key]=d['name']; p['keys'].append(key)
# ---------- book
def nlinks(p): return '<linklist>'+''.join('<link class="npc" recordname="npc.%s">NPC: %s</link>'%(k,html.escape(NN[k])) for k in p['keys'])+'</linklist>'
def note(f):
    b=fgconv.body(f); b=re.sub(r'^# .*$','',b,count=1,flags=re.M); x=fgconv.conv(b); fgconv.SEEN.clear(); return x
B=V+'/65-Bestiary/'
groups={}
for p in PAGES: groups.setdefault(p['ch'],[]).append(p)
intro=('<p>Every Sidebar Press creature, villain, minion template and conversion statblock in one module, laid out like the <i>Monster Manual</i>: '
 'monsters A to Z, the Rogues\' Gallery of named villains, and appendices for minion templates, named NPCs and the C12 conversions. '
 'Use <b>NPCs - By CR</b>, <b>By Letter</b> or <b>By Type</b> in the library to find a statblock fast, and drag it into an encounter or the combat tracker.</p>'
 '<p>%d statblocks on %d pages. Statblocks come from each vault note\'s FGU Import block; rebuild with <i>65-Bestiary/FGU Kit/build/bestiary.py</i> after any change.</p>')%(sum(len(p['keys']) for p in PAGES),len(PAGES))
m.bpage(NAME,'Front Matter','Sidebar Press Bestiary',[('text',intro)])
for f,n in (('01 — Introduction','Introduction'),('02 — Reading an Entry','Reading an Entry'),('04 — Minions','Minions')):
    if os.path.exists(B+f+'.md'): m.bpage('Introduction','Introduction',n,[('text',note(B+f+'.md'))])
order=['Monsters',"Rogues' Gallery",'Appendix A: Minion Templates','Appendix B: Named NPCs','Appendix C: C12 Conversions']
for ch in order:
    ps=sorted(groups.get(ch,[]),key=lambda p:(p['sub'],re.sub(r'^The ','',p['name']))) if ch!='Appendix C: C12 Conversions' else groups.get(ch,[])
    if ch=="Rogues' Gallery" and os.path.exists(B+"03 — Rogues' Gallery.md"): m.bpage(ch,'About',"The Rogues' Gallery",[('text',note(B+"03 — Rogues' Gallery.md"))])
    for p in ps:
        first=p['lore'] or '<p></p>'
        blocks=[('image',p['img'],'<h>%s</h>'%html.escape(p['name'])+first)] if p['img'] else [('text','<h>%s</h>'%html.escape(p['name'])+first)]
        blocks.append(('text',p['body']+nlinks(p)))
        blocks+= [('box',x) for x in p['boxes']]
        m.bpage(ch,p['sub'],p['name'],blocks)
out=os.path.join(V,'65-Bestiary/FGU Kit',NAME+('.test' if '--test' in sys.argv else '')+'.mod')
m.build(out)
if '--install' in sys.argv: shutil.copy(out,os.path.join(FG,'modules',NAME+'.mod')); print('installed')
