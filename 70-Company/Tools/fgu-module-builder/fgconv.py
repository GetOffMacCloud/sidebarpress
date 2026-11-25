"""Obsidian markdown -> Fantasy Grounds formattedtext. Part of the Sidebar Press FGU module builder."""
import re,os,json,html,sys
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
NAMES={}   # vault note name -> name shown in the module (set by module.py)
STRIP=[]   # note-name prefixes to drop when no NAMES entry (e.g. 'SP-GA05 — ')
SEEN=[]    # wikilink targets met since the last page/record was built (for "See also" links)
def resolve(target):
    note,_,head=target.partition('#')
    if not note.strip(): SEEN.append(head.strip()); return head.strip()  # [[#Heading]] within the same note: show the heading as written
    target=note.split('/')[-1].strip()
    SEEN.append(target)
    if target in NAMES: return NAMES[target]
    for pre in STRIP:
        if target.startswith(pre): return target[len(pre):]
    return target
def _wl(m):
    target,alias=m.group(1),m.group(2)
    shown=resolve(target)
    return alias if alias else shown
def inline(s):
    s=html.escape(s,quote=False)
    s=re.sub(r'!\[\[[^\]]*\]\]','',s)
    s=re.sub(r'\[\[([^\]|]*?)(?:\\?\|([^\]]*))?\]\]',_wl,s)
    s=re.sub(r'`([^`]*)`',r'\1',s)
    s=re.sub(r'\*\*([^*]+?)\*([^*]+?)\*\*\*',r'<b>\1<i>\2</i></b>',s)  # **text *italic*** (bold ending in italic)
    s=re.sub(r'\*\*\*(.+?)\*\*\*',r'<b><i>\1</i></b>',s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])',r'<i>\1</i>',s)
    return s.strip()
def plain(s):
    """A metadata field (spell components etc.): wikilinks resolved, no markup."""
    return html.unescape(re.sub(r'<[^>]+>','',inline(s)))
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
                if not re.match(r'^[\s:\-|]+$',r): rows.append([c.strip().replace('\x00','|') for c in re.sub(r'\[\[[^\]]*\]\]',lambda w: w.group(0).replace('\\|','\x00').replace('|','\x00'),r).split('|')])  # a pipe inside [[note|label]] is not a cell break
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
