"""Pre-place encounter tokens on the GA5 maps (Sidebar Press, 2026-11-21).
Positions are percentages of each map image (0,0 top-left), converted to FGU image
coordinates (pixels from the image centre, y down). Edit SPOTS to move tokens."""
import zipfile, shutil, os, xml.etree.ElementTree as ET
SIZE={'map-kalbach':(3000,1700),'map-hollen-ford-relay':(3840,2160),'map-hollen-ford-tower':(4500,2550),
      'map-orc-camp':(3840,2160),'map-bell-tor':(4500,2550)}
K=[(76,15),(81,16),(78,22),(74,21),(83,22),(80,26)]                       # K4, the wide new mound
SPOTS={  # encounter prefix -> npc name -> (map, [positions])
 'E1':{'Penny-Risen':('map-kalbach',[(76,15),(81,16),(78,22)]),
       'Penny-Risen (Lamb)':('map-kalbach',[(74,21),(80,26)]),'Penny-Risen (Dog)':('map-kalbach',[(83,22)])},
 'E2':{'Ghoul Rider':('map-hollen-ford-relay',[(85,61),(91,63)]),                       # R4 stable loft
       'Penny-Risen (Relay Signaller)':('map-hollen-ford-tower',[(50,23)]),             # R2 foot of the roof ladder
       'Penny-Risen':('map-hollen-ford-tower',[(44,55),(56,55)]),                       # R2 facing the door
       'Penny-Risen (Fox)':('map-hollen-ford-tower',[(50,66)])},
 'E3':{'Grukka One-Tusk':('map-orc-camp',[(50,22)]),                                    # O3 his tent
       'Orc Deserter':('map-orc-camp',[(47,72),(53,74),(44,49),(56,48),(50,58)])},      # O1 picket first, then O2 fire
 'R3':{'Orc Deserter':('map-orc-camp',[(47,6),(53,8)])},                                # foragers coming down the Tor path
 'E4':{'Brother-Reaper Ansgar Vell':('map-bell-tor',[(52,47)]),                          # T2 at the bell's lip
       'Sister Halse':('map-bell-tor',[(62,50)]),                                        # foot of the stair
       'Grey Sickle Acolyte':('map-bell-tor',[(60,41),(60,56),(65,44),(65,54)]),         # ringing the stair
       'Barrow Dead':('map-bell-tor',[(46,24),(54,24),(42,27),(58,27)])},                # reached the ring at the north gap
 'W4':{'Barrow Dead':('map-bell-tor',[(38,8)])},                                         # T6 barrow field
 'X4':{'Cathal Red-Torc':('map-bell-tor',[(50,31)])},                                     # the earth splits inside the ring
}
def _num(parent,tag,v):
    e=ET.SubElement(parent,tag,{'type':'number'}); e.text=str(int(round(v)))
MODNAME='SP-GA05 The Pilgrims of the Hollow Bell'
def apply(modpath):
    z=zipfile.ZipFile(modpath); items={n:z.read(n) for n in z.namelist()}; z.close()
    root=ET.fromstring(items['db.xml'])
    imgid={}
    for cat in root.find('image'):
        for rec in cat:
            lay=rec.find('.//bitmap')
            if lay is not None: imgid[os.path.splitext(os.path.basename(lay.text))[0]]='image.'+rec.tag
    placed=0
    for cat in root.find('battle'):
        for b in cat:
            spots=SPOTS.get((b.findtext('name') or '')[:2])
            if not spots: continue
            for n in b.find('npclist'):
                s=spots.get(n.findtext('name'))
                if not s: continue
                key,pos=s; W,H=SIZE[key]; cnt=int(n.findtext('count') or 1)
                old=n.find('maplink')
                if old is not None: n.remove(old)
                ml=ET.SubElement(n,'maplink')
                for i in range(cnt):
                    px,py=pos[i % len(pos)]
                    e=ET.SubElement(ml,'id-%05d'%(i+1))
                    r=ET.SubElement(e,'imageref',{'type':'windowreference'})
                    ET.SubElement(r,'class').text='imagewindow'; ET.SubElement(r,'recordname').text=imgid[key]+'.image@'+MODNAME   # the image control node, as FGU stores it
                    _num(e,'imagex',(px-50)/100*W); _num(e,'imagey',(py-50)/100*H); placed+=1
    items['db.xml']=ET.tostring(root,encoding='utf-8',xml_declaration=True)
    tmp=modpath+'.tmp'
    with zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED) as out:
        for k,v in items.items(): out.writestr(k,v)
    shutil.move(tmp,modpath); return placed
if __name__=='__main__':
    import sys; print('placed',apply(sys.argv[1]),'tokens')
