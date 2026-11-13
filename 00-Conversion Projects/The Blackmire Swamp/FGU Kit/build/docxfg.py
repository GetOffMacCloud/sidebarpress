"""Word (.docx) -> Fantasy Grounds formattedtext for The Blackmire Swamp conversion.
Reads the book's styles: ChapterKicker/Heading1/2/3, ListBullet, StatText, SmallText, and
shaded tables (20372F data table, E8EFE8 read-aloud/handout, F6F1E5/E7EEF0 sidebar,
355847 statblock title, E7D7AB ability scores)."""
import zipfile,re,html
import xml.etree.ElementTree as ET
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def _on(rp,tag):
    e=rp.find(W+tag) if rp is not None else None
    return e is not None and e.get(W+'val') not in ('0','false')
def pxml(p):
    out=[]
    for r in p.iter(W+'r'):
        t=''
        for x in r:
            if x.tag==W+'t': t+=x.text or ''
            elif x.tag==W+'tab': t+=' '
            elif x.tag==W+'br': t+=' '
        if not t: continue
        rp=r.find(W+'rPr'); s=html.escape(t,quote=False)
        if _on(rp,'i'): s='<i>%s</i>'%s
        if _on(rp,'b'): s='<b>%s</b>'%s
        out.append(s)
    x=''.join(out)
    for a in ('b','i'): x=x.replace('</%s><%s>'%(a,a),'')
    return re.sub(r'\s+',' ',x).strip()
def plain(x): return html.unescape(re.sub(r'<[^>]+>','',x)).strip()
def style(p):
    s=p.find(W+'pPr/'+W+'pStyle'); return s.get(W+'val') if s is not None else ''

def blocks(path):
    """Ordered list of ('p',style,xml) and ('tbl',fill,rows) where rows=[[ [cellpara xml,...] ,...],...]."""
    root=ET.fromstring(zipfile.ZipFile(path).read('word/document.xml')); out=[]
    for el in root.find(W+'body'):
        if el.tag==W+'p':
            x=pxml(el)
            if x: out.append(('p',style(el),x))
        elif el.tag==W+'tbl':
            f=el.find('.//'+W+'shd'); fill=(f.get(W+'fill') if f is not None else '-').upper()
            rows=[[[pxml(p) for p in tc.iter(W+'p') if pxml(p)] for tc in tr.findall(W+'tc')] for tr in el.findall(W+'tr')]
            out.append(('tbl',fill,rows))
    return out

def table_xml(rows):
    t='<table>'
    for k,r in enumerate(rows):
        t+='<tr>'+''.join('<td>%s</td>'%(('<b>%s</b>' if k==0 else '%s')%' '.join(c)) for c in r)+'</tr>'
    return t+'</table>'
def cell_text(rows): return [p for r in rows for c in r for p in c]

SEC={'TRAITS':'Traits','ACTIONS':'Actions','BONUS ACTIONS':'Bonus Actions','REACTIONS':'Reactions','LEGENDARY ACTIONS':'Legendary Actions','LAIR ACTIONS':'Lair Actions'}
SMALL={'of','the','and','in','to','a','an','for','on'}
def tcase(s):
    w=s.lower().split(' ')
    return ' '.join(x if (k and x in SMALL) else '-'.join(y[:1].upper()+y[1:] for y in x.split('-')) for k,x in enumerate(w))

def book(path,split_h3=(),skip_h2=()):
    """Returns (front, chapters, stat) where chapters=[(kicker,title,tagline,[(page,xml)])]
    and stat={title:{'lines':[plain StatText],'abil':[6 ints],'tactics':str}}."""
    B=blocks(path); front=[]; chs=[]; stat={}; cur=None; kick=''; parent=''; lst=[]; skipping=False; sb=None
    def _put(x):
        if cur is None: return
        if not cur: cur.append([chs[-1][1],[]])
        cur[-1][1].append(x)
    def flush():
        if lst: _put('<list>'+''.join('<li>%s</li>'%x for x in lst)+'</list>')
        lst.clear()
    def newpage(n):
        flush(); cur.append([n,[]])
    def add(x):
        flush(); _put(x)
    for b in B:
        if b[0]=='p':
            _,st,x=b
            if st=='ChapterKicker': flush(); kick=plain(x); continue
            if st=='Heading1':
                flush(); cur=[]; skipping=False; sb=None; chs.append([kick,plain(x),'',cur]); continue
            if cur is None: front.append(plain(x)); continue
            if st=='Heading2':
                parent=plain(x); skipping=parent in skip_h2; sb=None
                if not skipping: newpage(parent)
                continue
            if skipping: continue
            if st=='Heading3':
                if parent in split_h3: newpage(plain(x))
                else: add('<h>%s</h>'%x)
                continue
            if not cur and not chs[-1][2]:  # tagline under Heading1
                chs[-1][2]=plain(x); continue
            if st=='ListBullet': lst.append(x); continue
            if st=='SmallText': add('<p><i>%s</i></p>'%plain(x)); continue
            if st=='StatText':
                p=plain(x)
                if sb is not None: stat[sb]['lines'].append(p)
                if p in SEC: add('<p><b>%s</b></p>'%SEC[p]); continue
                m=re.match(r'^([^.]{2,80}?\.)\s(.*)$',p)
                add('<p><b>%s</b> %s</p>'%(html.escape(m.group(1)),html.escape(m.group(2))) if m and '<b>' not in x else '<p>%s</p>'%x); continue
            add('<p>%s</p>'%x)
        else:
            _,fill,rows=b
            if cur is None or skipping: continue
            ps=cell_text(rows)
            if fill=='355847':
                sb=tcase(plain(ps[0])); stat[sb]={'lines':[],'abil':[],'tactics':''}; newpage(sb); continue
            if fill=='E7D7AB':
                if sb: stat[sb]['abil']=[int(re.match(r'\d+',plain(c[0])).group()) for c in rows[1]]
                add(table_xml(rows)); continue
            if fill=='E8EFE8':
                lab=plain(ps[0])
                if lab!='READ ALOUD': add('<p><b>%s</b></p>'%html.escape(tcase(lab)))
                for p in ps[1:]: add('<frame>%s</frame>'%p)
                continue
            if fill in ('F6F1E5','E7EEF0'):
                lab=plain(ps[0]); body=' '.join(ps[1:])
                if lab=='TACTICS' and sb: stat[sb]['tactics']=plain(body)
                add('<p><b>%s.</b> <i>%s</i></p>'%(html.escape(tcase(lab)),body)); continue
            add(table_xml(rows))
    flush()
    chs=[(k,t,tg,[(n,''.join(x)) for n,x in pg if x]) for k,t,tg,pg in chs]
    return front,chs,stat

def find_table(path,header):
    for b in blocks(path):
        if b[0]=='tbl' and b[2] and plain(' '.join(b[2][0][0]))==header: return [[plain(' '.join(c)) for c in r] for r in b[2]]
