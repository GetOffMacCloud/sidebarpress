import os,re,sys,glob,yaml
SRC,DST=sys.argv[1],sys.argv[2]
os.makedirs(DST,exist_ok=True)
ORDER=["Appearance","Personality & Mannerisms","Goals & Secrets","Role & Context","Conversation Guide","Services","Quest Hooks","Relationships","Inventory","Stat Block","Appearances","Player Log","Canon Notes","Continuity"]
MAP={"appearance":"Appearance","appearance & manner":"Appearance","the man":"Appearance",
 "personality & mannerisms":"Personality & Mannerisms","personality":"Personality & Mannerisms","mannerisms":"Personality & Mannerisms","voice":"Personality & Mannerisms",
 "goals & secrets":"Goals & Secrets","key motivation":"Goals & Secrets","secrets & hidden motivations":"Goals & Secrets","the real story":"Goals & Secrets","what they know (but won't say)":"Goals & Secrets","what they fear":"Goals & Secrets","how to reveal it":"Goals & Secrets","what he fears":"Goals & Secrets","wants and fears":"Goals & Secrets","knows":"Goals & Secrets",
 "town role & function":"Role & Context","role in sidebar press adventures":"Role & Context","role in the campaign":"Role & Context","roles (ritterstadt gazetteer)":"Role & Context","who he is":"Role & Context","general":"Role & Context","role & context":"Role & Context","campaign connection":"Role & Context",
 "conversation guide":"Conversation Guide","trust-gated information":"Conversation Guide",
 "services":"Services","known services / interactions":"Services",
 "quest hooks":"Quest Hooks","relationship web":"Relationships","relationships":"Relationships",
 "inventory":"Inventory","stat block":"Stat Block","statblock":"Stat Block","stat pointer":"Stat Block",
 "appearances":"Appearances","player log":"Player Log","canon notes":"Canon Notes","source":"Canon Notes","continuity":"Continuity",
 "connections":"_drop","character descriptor":"_oneliner","public profile":"_container"}
PRIMARY={"appearance","appearance & manner","mannerisms","personality","personality & mannerisms","town role & function","who he is","role in the campaign","role in sidebar press adventures","conversation guide","services","quest hooks","relationship web","relationships","statblock","stat block","source","canon notes","continuity","appearances","goals & secrets","general","inventory"}
BOILER=["Is the person linked to any groups or quests?","The following items belong to","List important relationships here.","This is the persons description.","Make notes of what you need to track in the town here.","*No items currently equipped.*"]
def norm(h):
    h=re.sub(r"\*\(.*?\)\*","",h)                       # *(Sidebar Press)*
    h=re.sub(r"[^\w\s&'()/,\-.]","",h)                  # emoji
    return re.sub(r"\s+"," ",h).strip().lower()
NEWKEYS=[("type","npc"),("status","alive"),("canon",False),("faction",""),("location",""),("aliases",[]),("species",""),("heritage",""),("gender",""),("age",""),("alignment",""),("occupation",""),("class",""),("subclass",""),("prestige_class",""),("level",""),("adventure_role",""),("disposition",""),("party_trust",""),("items",[]),("connected_quests",[]),("connected_groups",[]),("parents",[]),("partner",[]),("children",[]),("siblings",[]),("allies",[]),("enemies",[]),("deceased_date",""),("tags",[])]
RENAME={"char_alignment":"alignment","char_status":"status","char_gender":"gender","char_age":"age","char_items":"items","Connected_Quests":"connected_quests","Connected_Groups":"connected_groups"}
HER={"oeridian":"Human — Oeridian","oerdian":"Human — Oeridian","suel":"Human — Suel","suloise":"Human — Suel","baklunish":"Human — Baklunish","flan":"Human — Flan","rhennee":"Human — Rhennee",
 "hill dwarf":"Dwarf — Hill","mountain dwarf":"Dwarf — Mountain","high elf":"Elf — High","sylvan":"Elf — Sylvan","grey elf":"Elf — Grey (Faerie)","valley elf":"Elf — Valley","grugach":"Elf — Wild (Grugach)","wild elf":"Elf — Wild (Grugach)",
 "rock gnome":"Gnome — Rock","svirfneblin":"Gnome — Svirfneblin","deep gnome":"Gnome — Svirfneblin","lightfoot":"Halfling — Lightfoot","stout":"Halfling — Stout","tallfellow":"Halfling — Tallfellow"}
def race(raw):
    r=str(raw or "").strip(); l=r.lower()
    if not r: return "",""
    for k in ["half-elf","half-orc"]:
        if k in l: return k.title().replace("-E","-E").replace("Half-elf","Half-Elf").replace("Half-orc","Half-Orc"),""
    her=next((v for k,v in HER.items() if k in l),"")
    for b in ["Human","Dwarf","Elf","Gnome","Halfling","Goliath"]:
        if b.lower() in l or (her and her.startswith(b)): return b,her
    if her: return her.split(" — ")[0],her
    return r,""
STATUS={"alive":"alive","dead":"dead","mia":"missing","missing":"missing","unknown":"unknown","permanent":"alive"}
QE='''> [!abstract]- Quick edit (Meta Bind)
> Status `INPUT[template-status][:status]` · Disposition `INPUT[template-npc-disposition][:disposition]` · Party trust `INPUT[template-npc-trust][:party_trust]` · Role `INPUT[template-npc-role][:adventure_role]`
> Race `INPUT[template-person-race][:species]` · Heritage `INPUT[template-person-heritage][:heritage]` · Gender `INPUT[template-person-gender][:gender]` · Age `INPUT[template-person-age-range][:age]` · Alignment `INPUT[template-npc-alignment][:alignment]`
> Class `INPUT[template-person-class][:class]` · Subclass `INPUT[template-person-subclass][:subclass]` · Prestige class `INPUT[template-prestige-class][:prestige_class]` · Level `INPUT[number:level]`
> Occupation `INPUT[text:occupation]` · Lives at `INPUT[suggester(optionQuery("40-Locations")):location]`
> Quests `INPUT[inlineListSuggester(optionQuery("60-Continuity/Quests")):connected_quests]` · Groups `INPUT[inlineListSuggester(optionQuery("20-World/Factions"), optionQuery("20-World/Homebrew")):connected_groups]` · Items `INPUT[inlineListSuggester(optionQuery("50-Items")):items]`'''
SKEL={"Conversation Guide":"| Topic | Freely discussed? | Notes / sample line |\n|---|:---:|---|\n| | | |",
 "Services":"| Service | Cost / notes |\n|---|---|\n| | |","Quest Hooks":"| Hook | Leads to | Trigger |\n|---|---|---|\n| | | |",
 "Player Log":"| Date (CY) | Party | What happened |\n|---|---|---|\n| | | |"}
REL_DV='''```dataview
TABLE WITHOUT ID parents AS "Parents", partner AS "Partner", children AS "Children", siblings AS "Siblings", allies AS "Allies", enemies AS "Enemies"
WHERE file.path = this.file.path
```'''
INV_DV='''```dataview
LIST FROM "50-Items" WHERE contains(this.items, file.link)
```'''
def clean(txt):
    txt=re.sub(r"```dataviewjs.*?```","",txt,flags=re.S)
    txt=re.sub(r"<%\*.*?%>","",txt,flags=re.S)
    out=[]
    for ln in txt.split("\n"):
        s=ln.strip()
        if re.search(r"INPUT\[|BUTTON\[|VIEW\[|= this\.file\.name",s): continue
        if re.match(r"^%%.*%%$",s) and ("MODIFY" in s or "DISPLAYS" in s or "CODE" in s or "MERMAID" in s or "Nodes will" in s): continue
        if s=="%%": continue
        if any(s.startswith(b) for b in BOILER): continue
        out.append(ln)
    txt="\n".join(out)
    txt=re.sub(r"(?m)^> \[!NOTE\]- Relationship Config.*?(?=\n[^>]|\Z)","",txt,flags=re.S)
    txt=re.sub(r"\n{3,}","\n\n",txt).strip()
    if re.fullmatch(r"(-{3,}\s*)*",txt): txt=""
    txt=re.sub(r"^(?:---\s*\n)+|(?:\n\s*---\s*)+$","",txt).strip()
    return txt
report=[]
for path in sorted(glob.glob(os.path.join(SRC,"*.md"))):
    name=os.path.basename(path)[:-3]; t=open(path,encoding="utf-8").read()
    m=re.match(r"---\n(.*?)\n---\n?",t,re.S)
    fm=yaml.safe_load(m.group(1)) if m else {}
    fm=fm or {}
    body=t[m.end():] if m else t
    tourist="char_race" in fm or "MyContainer" in fm
    if tourist:   # drop the Meta Bind layout block before the first heading
        i=re.search(r"(?m)^# ",body); body=body[i.start():] if i else body
    # ---- frontmatter
    new={}
    for k,v in list(fm.items()):
        if k in RENAME:
            if v not in (None,"",[]) : new[RENAME[k]]=v
            continue
        if k in ("char_race","ancestry"):
            sp,he=race(v); 
            if sp: new["species"]=sp
            if he: new["heritage"]=he
            continue
        if k=="MyContainer":
            if v and not fm.get("location"): new["location"]=v[0] if isinstance(v,list) and len(v)==1 else v
            new["MyContainer"]=v; continue
        if k=="town_role" and v and not fm.get("adventure_role"): new["town_role"]=v; continue
        new[k]=v
    if "status" in new and isinstance(new["status"],str): new["status"]=STATUS.get(new["status"].strip().lower(),new["status"])
    if "items" in new and new["items"] is None: new["items"]=[]
    if str(new.get("type","")).lower()=="npc": new["type"]="npc"
    out={}
    for k,d in NEWKEYS: out[k]=new.pop(k) if k in new and new[k] is not None else (d if k not in new else d)
    for k in list(new.keys()):
        if k in out: new.pop(k)
    out.update(new)
    # ---- body sections
    lines=body.split("\n"); title=None; pre=[]; chunks=[]; cur=None
    for ln in lines:
        h=re.match(r"^(#{1,3}) (.+?)\s*$",ln)
        if h:
            lvl=len(h.group(1)); key=norm(h.group(2)); tgt=MAP.get(key)
            if lvl==1 and title is None and tgt is None and not tourist:
                title=h.group(2); continue
            if tgt or lvl<=2:
                cur={"head":h.group(2),"lvl":lvl,"tgt":tgt or "_extra","lines":[]}; chunks.append(cur); continue
        (cur["lines"] if cur else pre).append(ln)
    if title is None or norm(title) in MAP: title=name
    title=re.sub(r"^👤\s*","",title)
    sec={k:[] for k in ORDER}; extras=[]; fgu=None; oneliner=None
    prec=clean("\n".join(pre))
    q=re.search(r"(?m)^> (?!\[!)(.+)$",prec)
    if q: oneliner=q.group(1).strip(); prec=clean(prec.replace(q.group(0),"",1))
    if prec: sec["Role & Context"].append(prec)
    for c in chunks:
        txt=clean("\n".join(c["lines"]))
        if c["tgt"]=="_drop" : 
            if txt: extras.append((c["head"],txt))
            continue
        if c["tgt"]=="_container":
            if txt: sec["Role & Context"].append(txt)
            continue
        if c["tgt"]=="_oneliner":
            if not oneliner and txt:
                first,_,rest=txt.partition("\n")
                oneliner=re.sub(r"^[*_]|[*_]$","",first).strip()
                if rest.strip(): sec["Role & Context"].append(rest.strip())
            elif txt: sec["Personality & Mannerisms"].append(txt)
            continue
        if c["tgt"]=="_extra":
            if norm(c["head"])=="fgu import": fgu="## FGU Import\n"+"\n".join(c["lines"]).strip()
            elif txt: extras.append((c["head"],txt))
            continue
        if not txt: continue
        h=c["head"]; label=re.sub(r"\*\(.*?\)\*","",h).strip()
        if norm(h) in PRIMARY: sec[c["tgt"]].append(txt); continue
        if norm(h) not in ("general",) and (c["lvl"]==3 or norm(h)!=norm(c["tgt"])): txt=f"### {label}\n{txt}" if c["lvl"]==3 or c["tgt"] in ("Goals & Secrets","Role & Context","Conversation Guide","Services") else txt
        sec[c["tgt"]].append(txt)
    # ---- assemble
    parts=[f"# {title}",""]
    parts.append(f"> {oneliner}" if oneliner else "> ")
    parts+=["",QE,""]
    for s in ORDER:
        parts.append(f"## {s}")
        body_s="\n\n".join(sec[s]).strip()
        if s=="Relationships": parts.append(REL_DV)
        if s=="Inventory": parts.append(INV_DV)
        if body_s: parts.append(body_s)
        elif s in SKEL: parts.append(SKEL[s])
        parts.append("")
    for h,txt in extras:
        parts+= [f"## {h}",txt,""]
    if fgu: parts+=[fgu,""]
    y=yaml.safe_dump(out,sort_keys=False,allow_unicode=True,width=10000,default_flow_style=None)
    res="---\n"+y+"---\n\n"+"\n".join(parts).rstrip()+"\n"
    open(os.path.join(DST,name+".md"),"w",encoding="utf-8").write(res)
    report.append((name,"tourist" if tourist else "sp",len(extras),sum(1 for s in ORDER if sec[s])))
for r in report: print(*r,sep="\t")
