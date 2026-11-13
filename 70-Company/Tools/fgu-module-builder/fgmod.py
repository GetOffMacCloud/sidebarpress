"""Sidebar Press FGU module builder: writes a Fantasy Grounds Unity .mod (5E) with a
story-book reference manual, NPCs, encounters, items and images. Format follows FGU 5.1
story-book exports (class story_book_page_advanced). See the fgu-module-build skill."""
import os,re,html,copy,zipfile,glob
import xml.etree.ElementTree as ET
from fgconv import conv, body, sections

def _S(p,tag,typ=None,text=None):
    e=ET.SubElement(p,tag)
    if typ: e.set('type',typ)
    if text is not None: e.text=str(text)
    return e
def _FT(p,tag,x):
    e=ET.fromstring('<%s type="formattedtext">%s</%s>'%(tag,x,tag)); p.append(e); return e
def _WR(p,tag,cls,rec):
    e=_S(p,tag,'windowreference'); _S(e,'class',None,cls); _S(e,'recordname',None,rec); return e
def ids(n): return 'id-%05d'%n
STOP=set('the and a an of to in is it on for with as at by or be if that this their they them from are was but not his her he she you your one two any all can will has have who what when'.split())

class Mod:
    def __init__(s,name,display,category,author,fg_dir,work_dir,srd_module='DD5E SRD Bestiary.mod',text_map=None):
        s.name,s.display,s.category,s.author=name,display,category,author
        s.fg=fg_dir; s.work=work_dir; s.img=os.path.join(work_dir,'images'); os.makedirs(s.img,exist_ok=True)
        s.map=text_map or {}
        z=zipfile.ZipFile(os.path.join(fg_dir,'modules',srd_module)); s.srd=ET.fromstring(z.read('db.xml')).find('reference/npcdata')
        s.root=ET.Element('root',{'version':'5.1','dataversion':'20260124','release':'9|CoreRPG:7'})
        s.cat={}; s.IMG={}; s.imgfiles=[]; s.NPC={}; s.TOK={}; s.XP={}; s.BAT={}; s.BATN={}; s.ITEM={}; s.ITEMN={}; s.pages=[]
    def t(s,x):  # apply the edition's rename map to any text
        for a,b in s.map.items(): x=x.replace(a,b)
        return x
    def _cat(s,tag):
        if tag not in s.cat:
            r=_S(s.root,tag); c=_S(r,'category'); c.set('name',s.name); s.cat[tag]=c
        return s.cat[tag]
    # ---------- images
    def images(s,src_dir,exclude=(),keep_original=()):
        from PIL import Image
        for f in sorted(os.listdir(src_dir)):
            n,ext=os.path.splitext(f)
            if n in exclude or ext.lower() not in ('.png','.jpg','.jpeg','.webp'): continue
            out=os.path.join(s.img,n+'.webp')
            if n in keep_original or ext.lower()=='.webp':
                out=os.path.join(s.img,f)
                if not os.path.exists(out): open(out,'wb').write(open(os.path.join(src_dir,f),'rb').read())
            elif not os.path.exists(out):
                im=Image.open(os.path.join(src_dir,f))
                if im.mode not in ('RGB','RGBA'): im=im.convert('RGB')
                im.save(out,'WEBP',quality=88 if n.startswith('battlemap') else 82,method=4)
                if os.path.getsize(out)>os.path.getsize(os.path.join(src_dir,f)):
                    os.remove(out); out=os.path.join(s.img,f); open(out,'wb').write(open(os.path.join(src_dir,f),'rb').read())
            s.imgfiles.append(os.path.basename(out))
        c=s._cat('image')
        for k,f in enumerate(s.imgfiles,1):
            n=os.path.splitext(f)[0]; s.IMG[n]=(ids(k),f); r=_S(c,ids(k)); s._layers(r,f); _S(r,'name','string',s.pretty(n))
    def _layers(s,p,f):
        im=_S(p,'image','image'); _S(im,'color',None,'#FFFFFFFF'); l=_S(_S(im,'layers'),'layer')
        for k,v in (('name',f),('id',0),('parentid',-1),('type','image'),('bitmap','images/'+f)): _S(l,k,None,v)
    @staticmethod
    def pretty(n):
        for a,b in (('npc-','NPC — '),('scene-','Scene Art — '),('battlemap-','Battlemap — '),('item-','Item — '),('map-','Map — ')):
            if n.startswith(a): return b+n[len(a):].replace('-',' ').title()
        return n.replace('-',' ').title()
    def imgpath(s,n): return 'images/%s@%s'%(s.IMG[n][1],s.name)
    # ---------- NPCs
    def npc_srd(s,src,name,key,dress=None,picture=None):
        e=copy.deepcopy(s.srd.find(src)); assert e is not None,'SRD npc not found: '+src
        e.tag=key; e.find('name').text=name; t=e.find('text')
        if t is None: t=_S(e,'text','formattedtext')
        if dress: p=ET.SubElement(t,'p'); b=ET.SubElement(p,'b'); b.text='Sidebar Press. '; b.tail=s.t(dress)
        p=ET.SubElement(t,'p'); i=ET.SubElement(p,'i'); i.text='Statblock: 5E SRD 5.1 (CC-BY-4.0).'
        if picture:
            if e.find('picture') is not None: e.remove(e.find('picture'))
            _S(e,'picture','token',s.imgpath(picture))
        s._cat('npc').append(e); s._reg(key,e)
    def npc(s,key,name,size,typ,align,ac,actext,hp,hd,speed,abilities,cr,xp,senses,languages,traits=(),actions=(),bonus=(),reactions=(),skills='',saves='',immunities='',text='',token_from=None,picture=None):
        e=_S(s._cat('npc'),key); a=_S(e,'abilities')
        for n,v in zip(['strength','dexterity','constitution','intelligence','wisdom','charisma'],abilities):
            x=_S(a,n); _S(x,'bonus','number',(v-10)//2); _S(x,'score','number',v)
        _S(e,'ac','number',ac); _S(e,'actext','string',actext)
        for tag,items in (('actions',actions),('traits',traits),('bonusactions',bonus),('reactions',reactions)):
            L=_S(e,tag)
            for k,(n,d) in enumerate(items,1): it=_S(L,ids(k)); _S(it,'desc','string',s.t(d)); _S(it,'name','string',s.t(n))
        for k,v in (('alignment',align),('cr',cr),('hd',hd),('languages',s.t(languages)),('name',s.t(name)),('senses',senses),('size',size),('speed',speed),('type',typ)): _S(e,k,'string',v)
        _S(e,'hp','number',hp); _S(e,'xp','number',xp)
        if skills: _S(e,'skills','string',skills)
        if saves: _S(e,'savingthrows','string',saves)
        if immunities: _S(e,'damageimmunities','string',immunities)
        _FT(e,'text','<h>%s</h><p>%s</p><p><i>Sidebar Press homebrew.</i></p>'%(html.escape(s.t(name)),html.escape(s.t(text))))
        tok=s.TOK.get(token_from,'') if token_from else ''
        if tok: _S(e,'token','token',tok)
        if picture: _S(e,'picture','token',s.imgpath(picture))
        s._reg(key,e)
    def _reg(s,key,e):
        s.NPC[key]='npc.'+key; s.TOK[key]=e.findtext('token') or ''; s.XP[key]=int(e.findtext('xp') or 0)
    def npcname(s,key): return s._cat('npc').find(key).findtext('name')
    # ---------- encounters
    def battle(s,code,name,creatures,map_image=None):
        c=s._cat('battle'); k=len(s.BAT)+1; r=_S(c,ids(k))
        _S(r,'exp','number',sum(s.XP[n]*cnt for n,cnt in creatures))
        if map_image: _WR(r,'maplink','imagewindow','image.'+s.IMG[map_image][0])
        _S(r,'name','string','%s %s'%(code,s.t(name))); L=_S(r,'npclist')
        for j,(n,cnt) in enumerate(creatures,1):
            it=_S(L,ids(j)); _S(it,'count','number',cnt); _S(it,'faction','string','foe'); _WR(it,'link','npc',s.NPC[n]); _S(it,'name','string',s.npcname(n))
            if s.TOK.get(n): _S(it,'token','token',s.TOK[n])
        s.BAT[code]='battle.'+ids(k); s.BATN[code]=s.t(name)
    # ---------- items
    def item(s,key,name,typ,desc_xml,subtype='',rarity='',picture=None,**fields):
        r=_S(s._cat('item'),key); _S(r,'name','string',s.t(name)); _S(r,'type','string',typ)
        if subtype: _S(r,'subtype','string',subtype)
        if rarity: _S(r,'rarity','string',rarity)
        for k,v in fields.items(): _S(r,k,'number' if isinstance(v,(int,float)) else 'string',v)
        _S(r,'isidentified','number',1); _FT(r,'description',s.t(desc_xml))
        if picture: _S(r,'picture','token',s.imgpath(picture))
        s.ITEM[key]='item.'+key; s.ITEMN[key]=s.t(name)
    # ---------- link helpers for page sidebars
    def B(s,c): return ('battle',s.BAT[c],'Encounter: %s %s'%(c,s.BATN[c]))
    def N(s,k): return ('npc',s.NPC[k],'NPC: '+s.npcname(k))
    def I(s,k): return ('imagewindow','image.'+s.IMG[k][0],'Image: '+s.pretty(k))
    def IT(s,k): return ('item',s.ITEM[k],'Item: '+s.ITEMN[k])
    # ---------- reference manual
    def page(s,section,name,xml,images=(),links=()):
        s.pages.append((section,s.t(name),[i for i in images if i in s.IMG],links,s.t(xml)))
    def _imgblock(s,bl,o,n):
        b=_S(bl,ids(o)); _S(b,'blocktype','string','image'); _S(b,'caption','string',s.pretty(n))
        s._layers(b,s.IMG[n][1]); _WR(b,'imagelink','imagewindow','image.'+s.IMG[n][0]); _S(b,'order','number',o)
    def build(s,out_path,cover_image=None):
        ref=_S(s.root,'reference'); rd=_S(ref,'refmanualdata'); chs=_S(_S(ref,'refmanualindex'),'chapters')
        ch=_S(chs,ids(1)); _S(ch,'name','string',s.display); _S(ch,'order','number',1); subs=_S(ch,'subchapters'); SUB={}
        for k,(sec,pname,imgs,ll,xml) in enumerate(s.pages,1):
            if sec not in SUB:
                sb=_S(subs,ids(len(SUB)+1)); _S(sb,'name','string',sec); _S(sb,'order','number',len(SUB)+1); SUB[sec]=[_S(sb,'refpages'),0]
            SUB[sec][1]+=1; rp,n=SUB[sec]; pid=ids(k); pg=_S(rd,pid); bl=_S(pg,'blocks'); o=0
            for im in imgs: o+=1; s._imgblock(bl,o,im)
            if ll:
                o+=1; b=_S(bl,ids(o)); _S(b,'blocktype','string','singletext'); _S(b,'frame','string','sidebar')
                _FT(b,'text','<p><b>Records for this page</b></p><linklist>'+''.join('<link class="%s" recordname="%s">%s</link>'%(c,r,html.escape(l)) for c,r,l in ll)+'</linklist>'); _S(b,'order','number',o)
            o+=1; b=_S(bl,ids(o)); _S(b,'blocktype','string','singletext'); _FT(b,'text',xml); _S(b,'order','number',o); _S(pg,'name','string',pname)
            words=sorted({w for w in re.findall(r"[a-z][a-z'-]{2,}",re.sub(r'<[^>]+>',' ',xml).lower()) if w not in STOP})
            e=_S(rp,ids(n)); _S(e,'keywords','string',' '.join(words[:400])); _WR(e,'listlink','story_book_page_advanced','reference.refmanualdata.'+pid); _S(e,'name','string',pname); _S(e,'order','number',n)
        libkey=re.sub(r'[^a-z0-9]','',s.name.lower()); le=_S(_S(s.root,'library'),libkey); le.set('static','true')
        _S(le,'categoryname','string',s.category); _S(le,'name','string',libkey); en=_S(le,'entries')
        x=_S(en,'_story_book'); _WR(x,'librarylink','reference_manual','reference.refmanualindex'); _S(x,'name','string','Book - '+s.display)
        for tag,label in (('battle','Encounters'),('encounter','Story'),('image','Images'),('item','Items'),('npc','NPCs')):
            if tag in s.cat: x=_S(en,tag); _WR(x,'librarylink','reference_list','..'); _S(x,'name','string',label); _S(x,'recordtype','string',tag)
        ET.indent(s.root,'\t'); db=b'<?xml version="1.0" encoding="utf-8"?>\n'+ET.tostring(s.root,encoding='utf-8'); s.check(db)
        d='<?xml version="1.0" encoding="utf-8"?>\n<root version="5.1" dataversion="20260124" release="9|CoreRPG:7">\n\t<name>%s</name>\n\t<displayname>%s</displayname>\n\t<category>%s</category>\n\t<author>%s</author>\n\t<ruleset>5E</ruleset>\n</root>\n'%tuple(html.escape(x) for x in (s.name,s.display,s.category,s.author))
        with zipfile.ZipFile(out_path,'w',zipfile.ZIP_DEFLATED) as z:
            z.writestr('definition.xml',d); z.writestr('db.xml',db)
            if cover_image and cover_image in s.IMG:
                from PIL import Image
                im=Image.open(os.path.join(s.img,s.IMG[cover_image][1])).convert('RGB'); im.thumbnail((256,256)); tp=os.path.join(s.work,'thumbnail.png'); im.save(tp); z.write(tp,'thumbnail.png')
            for f in s.imgfiles: z.write(os.path.join(s.img,f),'images/'+f)
        print('built %s: %d pages, %d npcs, %d encounters, %d items, %d images, %.1f MB'%(os.path.basename(out_path),len(s.pages),len(s.NPC),len(s.BAT),len(s.ITEM),len(s.imgfiles),os.path.getsize(out_path)/1048576))
    def check(s,db):
        r=ET.fromstring(db); paths=set()
        def walk(e,p):
            for c in e:
                if c.tag=='category': walk(c,p); continue
                q=p+'.'+c.tag if p else c.tag; paths.add(q); walk(c,q)
        walk(r,'')
        bad=sorted({x for x in [e.text for e in r.iter('recordname')]+[e.get('recordname') for e in r.iter('link')] if x and x!='..' and '@' not in x and x not in paths})
        assert not bad,'broken links: %s'%bad
