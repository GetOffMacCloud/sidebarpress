import re,os,json,html,sys
D=os.path.expanduser('~/mnt/Sidebar Press Vault/10-Adventures/SP-PBS-01 — The False Arrow/')
def body(p):
    t=open(p).read()
    if t.startswith('---'): t=t.split('\n---',1)[1].split('\n',1)[1]
    return t
def sections(t):
    out={}; cur=None
    for l in t.split('\n'):
        m=re.match(r'^## (.*)',l)
        if m: cur=m.group(1).strip(); out[cur]=[]
        elif cur: out[cur].append(l)
    return {k:'\n'.join(v) for k,v in out.items()}
def inline(s):
    s=html.escape(s,quote=False)
    s=re.sub(r'!\[\[[^\]]*\]\]','',s)
    s=re.sub(r'\[\[[^\]|]*\|([^\]]*)\]\]',r'\1',s)
    s=re.sub(r'\[\[(?:[^\]]*/)?([^\]#]*)(#[^\]]*)?\]\]',r'\1',s)
    s=re.sub(r'`([^`]*)`',r'\1',s)
    s=re.sub(r'\*\*\*(.+?)\*\*\*',r'<b><i>\1</i></b>',s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])',r'<i>\1</i>',s)
    return s.strip()
def conv(t):
    o=[]; lines=t.split('\n'); i=0; lst=None
    def close():
        nonlocal lst
        if lst: o.append('<list>'+''.join('<li>%s</li>'%x for x in lst)+'</list>'); lst=None
    while i<len(lines):
        l=lines[i].rstrip()
        if re.match(r'^\s*$',l) or l.strip() in ('---','>'): close(); i+=1; continue
        if 'Scene Index]]' in l and ('←' in l or 'Next →' in l): i+=1; continue
        if l.startswith('**Budget:**'): i+=1; continue
        if l.startswith('```'):
            close(); j=i+1; buf=[]
            while j<len(lines) and not lines[j].startswith('```'): buf.append(lines[j]); j+=1
            o.append('<frame>'+'\n'.join(html.escape(x) for x in buf)+'</frame>'); i=j+1; continue
        m=re.match(r'^(#{1,6}) (.*)',l)
        if m:
            close(); h=inline(m.group(2))
            o.append('<h>%s</h>'%h if len(m.group(1))<=2 else '<p><b>%s</b></p>'%h); i+=1; continue
        if l.startswith('> [!'):
            close(); j=i+1; buf=[]
            title=re.sub(r'^> \[![^\]]*\][-+]?\s*','',l)
            while j<len(lines) and lines[j].startswith('>'): buf.append(lines[j][1:].strip()); j+=1
            if 'FGU Import' not in title and '[!example]' not in l:
                o.append('<p><b>%s</b></p>'%inline(title)); o.append(conv('\n'.join(buf)))
            i=j; continue
        if l.startswith('>'):
            close(); j=i; buf=[]
            while j<len(lines) and lines[j].startswith('>'): buf.append(lines[j][1:].strip()); j+=1
            txt=' '.join(x for x in buf if x)
            if re.match(r'^\*\*[^*]+:\*\*',txt): o.append('<p>%s</p>'%inline(txt))
            else: o.append('<frame>%s</frame>'%inline(txt))
            i=j; continue
        if l.startswith('|'):
            close(); rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                r=lines[i].strip().strip('|')
                if not re.match(r'^[\s:\-|]+$',r): rows.append([c.strip() for c in r.split('|')])
                i+=1
            tb='<table>'
            for k,r in enumerate(rows): tb+='<tr>'+''.join('<td>%s</td>'%(('<b>%s</b>' if k==0 else '%s')%inline(c)) for c in r)+'</tr>'
            o.append(tb+'</table>'); continue
        m=re.match(r'^\s*(?:[-*]|\d+\.)\s+(.*)',l)
        if m:
            item=re.sub(r'^\[[ x]\]\s*','',m.group(1))
            if lst is None: lst=[]
            if l.startswith('   ') or l.startswith('\t'):
                lst[-1]+=' — '+inline(item) if lst else None
            else: lst.append(inline(item))
            i+=1; continue
        close(); o.append('<p>%s</p>'%inline(l)); i+=1
    close(); return ''.join(o)
if __name__=='__main__':
    M=sections(body(D+'SP-PBS-01-The-False-Arrow.md'))
    def pick(*names): return '\n'.join('## %s\n%s'%(n,M[n]) for n in names if n in M)
    cover='**APL 3 (level 3) · 4–6 characters · one 3½-hour session** · Part 1 of *The Plains of Blood and Steel* · Sidebar Press\n\n'
    entries=[('01 — Credits & How to Run', cover+pick('Date','Campaign Frame','Design Frame','Hook','PC Objectives','Subplots (keyed to PCs; assign at the table)','Act Structure')),
     ('02 — The False Arrow: Overview', pick('Chakyik Color','What the Locals Know',"What's Really Happening",'Climax at a Glance','Key NPCs','Key Locations','Encounters')),
     ('03 — The Favor Tracker', body(D+'SP-PBS-01 — The Favor Tracker.md').split('## At a Virtual Table')[0].replace('Back to [[SP-PBS-01-The-False-Arrow]]',''))]
    import glob
    for k,p in enumerate(sorted(glob.glob(D+'Scenes/Scene 0*.md'))):
        entries.append(('%02d — %s'%(4+k,os.path.basename(p)[:-3]),body(p).split('\n',3)[-1] if False else re.sub(r'^# .*\n','',body(p),count=1)))
    entries.append(('12 — Rewards & Continuity', pick('Treasure & Rewards','Continuity')))
    res=[{'name':n,'xml':conv(t)} for n,t in entries]
    json.dump(res,open(os.path.expanduser('~/work/story.json'),'w'),ensure_ascii=False)
    for r in res: print(len(r['xml'].encode()), r['name'])
    