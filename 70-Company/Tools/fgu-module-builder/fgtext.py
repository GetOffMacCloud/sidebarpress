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
NAME=re.compile(r"^((?:[A-Z0-9][\w'’\-+/,]*|of|the|and|a|an|in|to|on|with|from|or)(?: (?:[A-Z0-9(][\w'’\-+/,()]*|of|the|and|a|an|in|to|on|with|from|or|\d[\w/\-]*\)?|\([^)]*\)|\+\d+))*)\. (.+)$")
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
    MISSES.extend((d['name'],x) for x in innate(m,e)); phb_links_for_spellcasting(m,e)
    return e

# ---------- spells: clickable NPC spell entries (desc from the SRD Data module) + links to the PHB records
PHB='DD PHB Deluxe'
XGE="DD Xanathar's Guide to Everything Players"
OTHER={'searing smite':('reference.spelldata.searingsmite@'+PHB,'Searing Smite'),'banishing smite':('reference.spelldata.banishingsmite@'+PHB,'Banishing Smite'),
       'destructive wave':('reference.spelldata.destructivewave@'+PHB,'Destructive Wave'),'storm sphere':('spell.stormsphere@'+XGE,'Storm Sphere')}  # non-SRD book spells (verified in FG 2026-11-17)
HOMEBREW=None  # optional callable(name) -> (recordname, label, desc) for homebrew spells built into the module
MISSES=[]  # (npc, spell) innate spells not found in the SRD data
_SRD=None
def _srd(m):
    global _SRD
    if _SRD is None:
        import zipfile,os
        z=zipfile.ZipFile(os.path.join(m.fg,'modules','DD5E SRD Data.mod'))
        r=ET.fromstring(z.read('client.xml')); _SRD={e.findtext('name','').lower():(e.tag,e) for e in next(r.iter('spelldata'))}
    return _SRD
def _desc(e):
    lv=e.findtext('level') or '0'
    head='Level: %s\nCasting Time: %s\nComponents: %s\nDuration: %s\nRange: %s\n'%(lv if lv!='0' else 'Cantrip',e.findtext('castingtime',''),e.findtext('components',''),e.findtext('duration',''),e.findtext('range',''))
    d=e.find('description'); body='\n'.join(' '.join(''.join(p.itertext()).split()) for p in (d if d is not None else []) if ''.join(p.itertext()).strip())
    return head+body+'\n'
def spell_name(x): return re.sub(r'\s*\(.*?\)\s*','',x).strip().rstrip('.').strip()
def innate(m,e):
    """Innate Spellcasting trait -> innatespells entries ('Name (3/day)') and PHB links in the notes. Returns names not found in the SRD."""
    tr=[x for x in (e.find('traits') if e.find('traits') is not None else []) if (x.findtext('name') or '').startswith('Innate Spellcasting')]
    if not tr: return []
    S=_srd(m); L=e.find('innatespells')
    if L is None: L=_S(e,'innatespells')
    links=[]; miss=[]
    for line in tr[0].findtext('desc').split('\n'):
        mm=re.match(r'^\s*(At will|\d+/day)[^:]*:\s*(.*)$',line,re.I)
        if not mm: continue
        tag=mm.group(1).capitalize() if mm.group(1).lower()=='at will' else mm.group(1)
        for sp in re.split(r',\s*(?![^()]*\))',mm.group(2)):
            nm=spell_name(sp)
            if not nm: continue
            hit=S.get(nm.lower())
            it=_S(L,ids(len(L)+1)); _S(it,'desc','string',_desc(hit[1]) if hit else ''); _S(it,'name','string','%s (%s)'%(hit[1].findtext('name') if hit else nm[:1].upper()+nm[1:],tag))
            if hit: links.append(('reference.spelldata.%s@%s'%(hit[0],PHB),hit[1].findtext('name')))
            elif nm.lower() in OTHER: links.append(OTHER[nm.lower()]); it.find('desc').text='See the linked spell.'
            elif HOMEBREW and HOMEBREW(nm):
                rec,lab,ds=HOMEBREW(nm); links.append((rec,lab)); it.find('desc').text=ds; it.find('name').text='%s (%s)'%(lab,tag)
            else: miss.append(nm)
    tx=e.find('text')
    if links and tx is not None:
        p=ET.SubElement(tx,'p'); b=ET.SubElement(p,'b'); b.text='Spells'; b.tail=':'
        ll=ET.SubElement(tx,'linklist')
        for k,n in dict.fromkeys(links):
            a=ET.SubElement(ll,'link',{'class':'power','recordname':k}); a.text='Spell: '+n
    return miss
def phb_links_for_spellcasting(m,e):
    """Spellcasting trait (slot caster): add PHB links for every SRD spell it names."""
    tr=[x for x in (e.find('traits') if e.find('traits') is not None else []) if (x.findtext('name') or '')=='Spellcasting']
    if not tr: return
    S=_srd(m); links=[]
    for line in tr[0].findtext('desc').split('\n'):
        mm=re.match(r'^\s*(?:Cantrips|\d(?:st|nd|rd|th) level)[^:]*:\s*(.*)$',line)
        if not mm: continue
        for sp in re.split(r',\s*(?![^()]*\))',mm.group(1)):
            nm=spell_name(sp).lower(); hit=S.get(nm)
            if hit: links.append(('reference.spelldata.%s@%s'%(hit[0],PHB),hit[1].findtext('name')))
            elif nm in OTHER: links.append(OTHER[nm])
            elif HOMEBREW and HOMEBREW(nm): links.append(HOMEBREW(nm)[:2])
    tx=e.find('text')
    if links and tx is not None:
        p=ET.SubElement(tx,'p'); b=ET.SubElement(p,'b'); b.text='Spells'; b.tail=':'
        ll=ET.SubElement(tx,'linklist')
        for k,n in dict.fromkeys(links):
            a=ET.SubElement(ll,'link',{'class':'power','recordname':k}); a.text='Spell: '+n
