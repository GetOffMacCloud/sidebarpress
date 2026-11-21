"""SP-GA05 manuscript compile: assembles the shipping notes in manifest order into 'SP-GA05 — Compiled.md'.
Longform can't compile this adventure (its scenes live in the main note and Encounters/), so this script stands in. Run: python3 compile.py"""
import os,re,glob
HERE=os.path.dirname(os.path.abspath(__file__)); ADV=os.path.dirname(os.path.dirname(HERE)); V=ADV
while not os.path.isdir(os.path.join(V,'70-Company')): V=os.path.dirname(V)
def body(p):
    t=open(p,encoding='utf-8').read()
    return re.sub(r'\A---\n.*?\n---\n','',t,count=1,flags=re.S).strip()
def drop(t,*heads):
    for h in heads:
        t=re.sub(r'^## %s\n.*?(?=^## |\Z)'%re.escape(h),'',t,flags=re.S|re.M)
    return t.strip()
def demote(t,n=1): return re.sub(r'^(#+) ',lambda m:'#'*(len(m.group(1))+n)+' ',t,flags=re.M)
A=lambda *x: os.path.join(ADV,*x)
out=[]
main=drop(body(A('SP-GA05-The-Pilgrims-of-the-Hollow-Bell.md')),'Adventure Code','Supporting Files')
out.append(main)
out.append('# Running the Adventure\n\n'+demote(re.sub(r'^# .*\n','',drop(body(A("SP-GA05 — DM's Notes.md")),'Friday Night Field Trips Insert','Open Items'),count=1),0))
out.append('# Encounters')
for f in sorted(glob.glob(A('Encounters','*.md'))): out.append(demote(body(f)))
out.append('# Appendix A: Bestiary\n\n'+demote(re.sub(r'^# .*\n','',body(A('SP-GA05 — Bestiary.md')),count=1),0))
out.append('# Appendix B: New Spells and Items')
for s in ('Ash Tally',"Reaper's Tithe",'Hollowing Toll'): out.append(demote(body(A('Spells',s+'.md'))))
for s in ("Reaper's Penny",'The Bone Clapper','The Sun-Bell of Carn Aedh','The Yati Lambskin','Red Torc of Cathal'): out.append(demote(drop(body(os.path.join(V,'50-Items',s+'.md')),'Found In')))
out.append('# Appendix C: Dramatis Personae')
for s in ('Brother-Reaper Ansgar Vell','Sister Halse','Grukka One-Tusk','Cathal Red-Torc','Udo Pfaff','Brenna','Wendel Krafft'):
    t=drop(body(os.path.join(V,'30-NPCs',s+'.md')),'Statblock','FGU Import','Stat Block','Canon Notes','Appearances')
    t=re.sub(r'> \[!warning\].*?\n\n','',t,flags=re.S)
    out.append(demote(t))
out.append('# Appendix D: Handouts')
for f in sorted(glob.glob(A('*Handout*.md')),key=lambda p:int(re.search(r'publish_order: (\d+)',open(p,encoding='utf-8').read()).group(1))): out.append(demote(re.sub(r'> \[!warning\].*?(\n\n|\Z)','',body(f),flags=re.S)))
out.append("# Appendix E: The Field Warden's Primer\n\n"+demote(re.sub(r'^# .*\n','',body(A("SP-GA05 — Player Gazetteer — The Field Warden's Primer.md")),count=1),1))
out.append('# Appendix F: Continuing the Adventure')
for f in sorted(glob.glob(A('Side Quests','*.md'))): out.append(demote(drop(body(f),'Theme')))
txt='---\ntype: compiled\nadventure: "SP-GA05"\nsection: internal\npublish_order: 0\npublish: false\n---\n\n'+'\n\n'.join(out)+'\n'
open(A('SP-GA05 — Compiled.md'),'w',encoding='utf-8').write(txt); print('compiled',len(txt.split()),'words')
