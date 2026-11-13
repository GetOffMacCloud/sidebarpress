"""SP-PBS-05 The Pilgrims of the Hollow Bell -> Fantasy Grounds module. Run: python3 module.py [--install]
Uses the shared builder in 70-Company/Tools/fgu-module-builder (see the fgu-module-build skill).
Sellable master edition: no Friday-table material (Pip, Elric's squire, the FNFT insert)."""
import os,sys,re,glob,shutil,html
HERE=os.path.dirname(os.path.abspath(__file__)); ADV=os.path.dirname(os.path.dirname(HERE)); VAULT=os.path.dirname(os.path.dirname(ADV))
sys.path.insert(0,os.path.join(VAULT,'70-Company','Tools','fgu-module-builder'))
from fgmod import Mod, conv, body, sections, _S, _FT
FG=os.environ.get('FG_DIR',os.path.expanduser('~/mnt/Fantasy Grounds'))
# ---- edition settings (a renamed edition changes only this block) ----
CODE='SP-PBS-05'; NAME='SP-PBS-05 The Pilgrims of the Hollow Bell'; DISPLAY='SP-PBS-05 — The Pilgrims of the Hollow Bell'
SRC=ADV; ASSETS=os.path.join(VAULT,'99-Assets',CODE); TEXT_MAP={}
EXCLUDE_IMAGES=('portrait-pip-thistlebottom',)                       # Friday-table only
RENAME_IMAGES={'token-zombie-pip':'token-zombie-signaller','portrait-elrics-squire':'portrait-kalbach-letter-writer'}
DROP_SECTIONS=('Friday Night Field Trips Insert','Open Items')       # DM's Notes sections left out of the sold module
FRAME='Greyhawk University'
# -----------------------------------------------------------------------
WORK=os.path.expanduser('~/work/fgu/'+CODE); FLAT=WORK+'-src'; os.makedirs(FLAT,exist_ok=True)
def ikey(f):  # vault asset file name -> module image key
    n=os.path.splitext(f)[0]; n=n[len(CODE)+1:] if n.startswith(CODE+' ') else n
    return RENAME_IMAGES.get(n,n)
for f in glob.glob(os.path.join(ASSETS,'*','*')):
    k=ikey(os.path.basename(f)); dst=os.path.join(FLAT,k+os.path.splitext(f)[1].lower())
    if k not in EXCLUDE_IMAGES and not os.path.exists(dst): shutil.copyfile(f,dst)
m=Mod(NAME,DISPLAY,'Sidebar Press','Sidebar Press',FG,WORK,text_map=TEXT_MAP)
m.images(FLAT)
P=lambda pat: glob.glob(os.path.join(SRC,pat))[0]
NOTE=lambda folder,name: os.path.join(VAULT,folder,name+'.md')
MAIN=P(CODE+'-The-Pilgrims*.md'); DMN=P("*DM's Notes.md"); BEST=P('*Bestiary.md'); PRIMER=P('*Field Warden*.md')
# ---- helpers: images from embeds, art callouts stripped, sections ----
EMB=re.compile(r'!\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]')
def imgs(t): return [k for k in (ikey(x) for x in EMB.findall(t)) if k in m.IMG and k not in EXCLUDE_IMAGES]
def noart(t):
    out=[]; skip=False
    for l in t.split('\n'):
        if l.startswith('> [!art'): skip=True; continue
        if skip and l.startswith('>'): continue
        skip=False; out.append(l)
    return '\n'.join(out)
def C(t): return conv(noart(t))
M=sections(body(MAIN)); D=sections(body(DMN))
pick=lambda S,*n: '\n'.join('## %s\n%s'%(x,S[x]) for x in n if x in S)
def subs(t):  # split a Part section at its ### headings
    out=[]; cur=None
    for l in t.split('\n'):
        mm=re.match(r'^### (.*)',l)
        if mm: cur=[mm.group(1).strip(),[]]; out.append(cur)
        elif cur: cur[1].append(l)
    return [(a,'\n'.join(b)) for a,b in out]
PART={k:subs(v) for k,v in M.items() if k.startswith('Part ')}
def fullnote(p): return re.sub(r'^# .*\n','',body(p),count=1)
# ---- homebrew NPCs, parsed from each note's ## FGU Import block ----
def fgu_block(p):
    return re.search(r'## FGU Import.*?```text\n(.*?)```',open(p).read(),re.S).group(1).strip().split('\n')
def homebrew(key,p,token=None,picture=None):
    L=fgu_block(p); name=L[0]; st=L[1]; sz,rest=st.split(' ',1); typ,align=rest.rsplit(', ',1)
    ac,actext=re.match(r'Armor Class (\d+)\s*(.*)',L[2]).groups(); hp,hd=re.match(r'Hit Points (\d+)\s*(.*)',L[3]).groups()
    speed=L[4][6:]; ab=[int(x) for x in re.findall(r'(\d+) \(',L[6])]
    f={}; i=7
    while not L[i].startswith('Proficiency Bonus'):
        for lab in ('Saving Throws','Skills','Damage Vulnerabilities','Damage Resistances','Damage Immunities','Condition Immunities','Senses','Languages','Challenge'):
            if L[i].startswith(lab+' '): f[lab]=L[i][len(lab)+1:]
        i+=1
    cr,xp=re.match(r'(\S+) \(([\d,]+) XP\)',f['Challenge']).groups(); i+=1
    traits,actions,cur=[],[],None; tgt=traits
    for l in L[i:]:
        if l=='Actions': tgt=actions; continue
        mm=re.match(r"^([A-Z][A-Za-z' -]{1,40})\. (.*)",l)
        if mm and not l.startswith(('Cantrips','1st','2nd','3rd')): cur=[mm.group(1),mm.group(2)]; tgt.append(cur)
        elif l.strip() and cur: cur[1]+='\n'+l
    text=' '.join(x.strip('- ') for x in re.findall(r'^- \*\*(?:Description|Appearance|In this adventure|Animal variant):\*\* .*$',body(p),re.M))
    text=re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]',r'\1',text).replace('**','').replace('*','')
    m.npc(key,name,sz,typ,align,int(ac),actext,int(hp),hd,speed,ab,cr,int(xp.replace(',','')),f.get('Senses',''),f.get('Languages',''),
          traits=[tuple(t) for t in traits],actions=[tuple(a) for a in actions],skills=f.get('Skills',''),saves=f.get('Saving Throws',''),
          immunities=f.get('Damage Immunities',''),text=text,picture=picture or token)
    e=m._cat('npc').find(key)
    for lab,tag in (('Damage Resistances','damageresistances'),('Damage Vulnerabilities','damagevulnerabilities'),('Condition Immunities','conditionimmunities')):
        if lab in f: _S(e,tag,'string',f[lab])
    if token: _S(e,'token','token',m.imgpath(token)); m.TOK[key]=m.imgpath(token)
def srd(src,name,key,token,dress):
    m.npc_srd(src,name,key,dress=dress,picture=token)
    e=m._cat('npc').find(key); old=e.find('token')
    if old is not None: e.remove(old)
    _S(e,'token','token',m.imgpath(token)); m.TOK[key]=m.imgpath(token)
