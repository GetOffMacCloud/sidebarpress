"""Monster-Manual-style book for fgmod.Mod: several chapters, lettered subchapters, pages made of
an imageright block (art + opening lore), a noframe text block ending in NPC links, and green sidebars.
Matches the FGU 'D&D Monster Manual (Legacy)' layout. Also adds the NPCs By CR / Letter / Type lists."""
import re,html,os,zipfile
import xml.etree.ElementTree as ET
import fgmod
from fgmod import _S,_FT,_WR,ids,STOP
class BMod(fgmod.Mod):
    def __init__(s,*a,**k):
        super().__init__(*a,**k); s.book=[]   # (chapter, subchapter, name, blocks)
    def bpage(s,chapter,sub,name,blocks):
        """blocks: ('image', imgkey, xml) | ('text', xml) | ('box', xml)"""
        s.book.append((chapter,sub,name,blocks)); return 'reference.refmanualdata.'+ids(len(s.book))
    def _book(s):
        ref=_S(s.root,'reference'); rd=_S(ref,'refmanualdata'); chs=_S(_S(ref,'refmanualindex'),'chapters'); CH={}
        for k,(ch,sub,name,blocks) in enumerate(s.book,1):
            if ch not in CH:
                c=_S(chs,ids(len(CH)+1)); _S(c,'name','string',ch); _S(c,'order','number',len(CH)+1); CH[ch]=[_S(c,'subchapters'),{}]
            subs,SB=CH[ch]
            if sub not in SB:
                sb=_S(subs,ids(len(SB)+1)); _S(sb,'name','string',sub); _S(sb,'order','number',len(SB)+1); SB[sub]=[_S(sb,'refpages'),0]
            SB[sub][1]+=1; rp,n=SB[sub]; pid=ids(k); pg=_S(rd,pid); bl=_S(pg,'blocks'); alltxt=''
            for o,b in enumerate(blocks,1):
                e=_S(bl,ids(o))
                if b[0]=='image':
                    _S(e,'align','string','left,right'); _S(e,'blocktype','string','imageright'); _S(e,'caption','string',name)
                    s._layers(e,s.IMG[b[1]][1]); _WR(e,'imagelink','imagewindow','image.'+s.IMG[b[1]][0]); _S(e,'scale','number',80); xml=b[2]
                else:
                    _S(e,'align','string','center'); _S(e,'blocktype','string','singletext'); _S(e,'frame','string','green' if b[0]=='box' else 'noframe'); xml=b[1]
                _S(e,'order','number',o); _FT(e,'text',xml); alltxt+=xml
            _S(pg,'name','string',name)
            words=sorted({w for w in re.findall(r"[a-z][a-z'-]{2,}",re.sub(r'<[^>]+>',' ',alltxt).lower()) if w not in STOP})
            e=_S(rp,ids(n)); _S(e,'keywords','string',' '.join(words[:400])); _WR(e,'listlink','reference_manualtextwide','reference.refmanualdata.'+pid); _S(e,'name','string',name); _S(e,'order','number',n)
    def build(s,out_path,cover_image=None):
        s._book()
        L=_S(_S(s.root,'list'),'npc')
        for v in ('bycr','byletter','bytype'): x=_S(L,v); _S(x,'listview','string',v); _S(x,'recordtype','string','npc')
        libkey=re.sub(r'[^a-z0-9]','',s.name.lower()); le=_S(_S(s.root,'library'),libkey); le.set('static','true')
        _S(le,'categoryname','string',s.category); _S(le,'name','string',libkey); en=_S(le,'entries')
        x=_S(en,'story_book'); _WR(x,'librarylink','reference_manual','reference.refmanualindex'); _S(x,'name','string','Book - '+s.display)
        x=_S(en,'image'); _WR(x,'librarylink','reference_list','..'); _S(x,'name','string','Images'); _S(x,'recordtype','string','image')
        x=_S(en,'npc'); _WR(x,'librarylink','reference_list','..'); _S(x,'name','string','NPCs'); _S(x,'recordtype','string','npc')
        for v,lab in (('bycr','NPCs - By CR'),('byletter','NPCs - By Letter'),('bytype','NPCs - By Type')):
            x=_S(en,'npc_'+v); _WR(x,'librarylink','reference_groupedlist','list.npc.'+v); _S(x,'name','string',lab)
        ET.indent(s.root,'\t'); db=b'<?xml version="1.0" encoding="utf-8"?>\n'+ET.tostring(s.root,encoding='utf-8'); s.check(db); s.lint(db)
        d='<?xml version="1.0" encoding="utf-8"?>\n<root version="5.1" dataversion="20260124" release="9|CoreRPG:7">\n\t<name>%s</name>\n\t<displayname>%s</displayname>\n\t<category>%s</category>\n\t<author>%s</author>\n\t<ruleset>5E</ruleset>\n</root>\n'%tuple(html.escape(x) for x in (s.name,s.display,s.category,s.author))
        with zipfile.ZipFile(out_path,'w',zipfile.ZIP_DEFLATED) as z:
            z.writestr('definition.xml',d); z.writestr('db.xml',db)
            for f in s.imgfiles: z.write(os.path.join(s.img,f),'images/'+f)
        print('built %s: %d pages, %d npcs, %d images, %.1f MB'%(os.path.basename(out_path),len(s.book),len(s.NPC),len(s.imgfiles),os.path.getsize(out_path)/1048576))
