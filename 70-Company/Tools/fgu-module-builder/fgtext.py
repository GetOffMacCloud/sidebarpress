"""Parse FGU 'Import Text' statblocks (2014 / MotM layout, as written by fgu_import.py and the
conversion kits) into 5E NPC records for fgmod.Mod. One parser for the vault bestiary, 30-NPCs,
minion templates and conversion projects."""
import re,html
import xml.etree.ElementTree as ET
from fgmod import _S,_FT,ids
AB=['strength','dexterity','constitution','intelligence','wisdom','charisma']
FIELDS=[('Saving Throws','savingthrows'),('Skills','skills'),('Damage Vulnerabilities','damagevulnerabilities'),
        ('Damage Resistances','damageresistances'),('Damage Immunities','damageimmunities'),
        ('Condition Immunities','conditionimmunities'),('Senses','senses'),('Languages','languages')]
SECT={'Actions':'actions','Bonus Actions':'bonusactions','Reactions':'reactions','Legendary Actions':'legendaryactions','Mythic Actions':'legendaryactions','Lair Actions':'lairactions'}
NAME=re.compile(r"^((?:[A-Z0-9][\w'’\-+/,]*|of|the|and|a|an|in|to|on|with|from|or)(?: (?:[A-Z0-9(][\w'’\-+/,()]*|of|the|and|a|an|in|to|on|with|from|or|\d[\w/\-]*\)?|\([^)]*\)))*)\. (.+)$")
def _norm(x): return x.replace('−','-').replace('–','-').replace('—','-').strip()
def blocks_md(txt):
    """```text fenced blocks that look like statblocks."""
    return [b for b in re.findall(r'```text\n(.*?)```',txt,re.S) if re.search(r'^Armor Class ',b,re.M) and re.search(r'^Challenge ',b,re.M)]
def parse(block):
    L=[_norm(l) for l in block.strip().split('\n') if l.strip()]
    d={'name':L[0]}; i=1
    m=re.match(r'^(Tiny|Small|Medium|Large|Huge|Gargantuan)(?: or \w+)? (.+?), (.+)$',L[1])
    if m: d['size'],d['type'],d['alignment']=m.groups(); i=2
    else: d['size'],d['type'],d['alignment']='Medium','humanoid','any'
    while i<len(L):
        l=L[i]
        if l.startswith('Armor Class '):
            m=re.match(r'Armor Class (\d+)\s*(.*)',l); d['ac']=int(m.group(1)); d['actext']=m.group(2)
        elif l.startswith('Hit Points '):
            m=re.match(r'Hit Points (\d+)\s*(.*)',l); d['hp']=int(m.group(1)); d['hd']=m.group(2)
        elif l.startswith('Speed '): d['speed']=l[6:]
        elif re.match(r'^STR\s+DEX',l):
            i+=1; sc=[int(x) for x in re.findall(r'(\d+)\s*\(',L[i])]; d['abilities']=sc
        elif l.startswith('Challenge '):
            m=re.match(r'Challenge ([\d/]+)(?: \(([\d,]+) XP\))?',l); d['cr']=m.group(1); d['xp']=int((m.group(2) or '0').replace(',',''))
            i+=1; break
        else:
            for lab,tag in FIELDS:
                if l.startswith(lab+' '): d[tag]=l[len(lab)+1:]; break
        i+=1
    cur='traits'; d['lists']={'traits':[]}
    for l in L[i:]:
        if l in SECT: cur=SECT[l]; d['lists'].setdefault(cur,[]); continue
        if l.startswith('Proficiency Bonus'): continue
        m=NAME.match(l)
        if m and len(m.group(1))<=70: d['lists'][cur].append([m.group(1),m.group(2)])
        elif d['lists'][cur]: d['lists'][cur][-1][1]+='\n'+l
        else: d['lists'][cur].append(['',l])  # intro text (e.g. legendary action preamble)
    LBL={'legendaryactions':'Legendary Actions','lairactions':'Lair Actions','reactions':'Reactions','actions':'Actions','bonusactions':'Bonus Actions','traits':'Note'}
    for k,v in d['lists'].items():
        if v and v[0][0]=='': v[0][0]=LBL.get(k,'Note')
    need=['ac','hp','speed','abilities','cr']
    miss=[k for k in need if k not in d]
    if miss: raise ValueError('%s: missing %s'%(d['name'],miss))
    return d
def add(m,key,d,text_xml='',picture=None,token=None):
    """Write a parsed statblock into the Mod as npc.<key>."""
    e=_S(m._cat('npc'),key); a=_S(e,'abilities')
    for n,v in zip(AB,d['abilities']):
        x=_S(a,n); _S(x,'bonus','number',(v-10)//2); _S(x,'score','number',v)
    _S(e,'ac','number',d['ac']); _S(e,'actext','string',d.get('actext',''))
    for tag,items in d['lists'].items():
        if not items: continue
        Lx=_S(e,tag)
        for k,(n,ds) in enumerate(items,1): it=_S(Lx,ids(k)); _S(it,'desc','string',m.t(ds)); _S(it,'name','string',m.t(n))
    for k in ('alignment','cr','hd','size','speed','type'): _S(e,k,'string',d.get(k,''))
    _S(e,'name','string',m.t(d['name']))
    for lab,tag in FIELDS:
        if tag in d: _S(e,tag,'string',m.t(d[tag]))
    _S(e,'hp','number',d['hp']); _S(e,'xp','number',d.get('xp',0))
    _FT(e,'text',text_xml or '<h>%s</h><p><i>Sidebar Press homebrew.</i></p>'%html.escape(d['name']))
    if picture: _S(e,'picture','token',m.imgpath(picture))
    if token: _S(e,'token','token',token)
    m._reg(key,e); m._slots(e)
    return e
