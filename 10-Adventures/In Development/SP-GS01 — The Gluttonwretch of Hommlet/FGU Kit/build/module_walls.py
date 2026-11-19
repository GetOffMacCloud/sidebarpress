# ---- SP-GS01 walls and line of sight on the player battlemaps (exec'd by module.py) ----
# Polylines in pixels from the map's top-left. FGU stores them from the centre with y UP.
def box(cx,cy,h): return [(cx-h,cy-h),(cx+h,cy-h),(cx+h,cy+h),(cx-h,cy+h)]
T4=lambda pts: [(round(x/0.3807),round(y/0.3807)) for x,y in pts]  # T1 Map 4 walls were traced on a 0.3807 preview
WALLS={
 'map-m2a-smokehouse-ground-floor':[([(350,600),(350,175),(1630,175),(1630,1105),(1110,1105)],0),([(870,1105),(350,1105),(350,660)],0),
                                     ([(350,385),(900,385)],0),([(1110,385),(1630,385)],0)],
 'map-m2b-smokehouse-cellar':[([(1233,1111),(667,1111),(667,667)],0),([(667,589),(667,138),(1900,138),(1900,1111),(1322,1111)],0),
                              ([(667,200),(200,200),(200,884),(667,884)],0)],
 'map-m1-feast-green':[([(433,0),(433,217),(1400,217)],0),([(1567,217),(2567,217),(2567,0)],0)],
 'map-m3-jaroos-grove':[(box(x*2.667,y*2.667,48),1) for x,y in ((283,240),(615,225),(180,355),(717,355),(195,500),(712,500),(283,610),(612,618),(450,670),(450,205))]
                      +[(box(440*2.667,140*2.667,90),1)],
 'map-m4-emridy-meadows':[(box(1733,1283,80),1)],
 'map-t1-traders-establishment':[(T4([(20,25),(255,25),(255,495),(20,495)]),1),(T4([(175,495),(175,640)]),0),
                                 (T4([(130,640),(130,890),(255,890)]),0),(T4([(285,890),(600,890),(600,495),(470,495),(470,640),(375,640)]),0),
                                 (T4([(345,640),(265,640)]),0),(T4([(240,640),(130,640)]),0)],
}
for k,walls in WALLS.items():
    rec=m._cat('image').find(m.IMG[k][0]); im=rec.find('image'); W,H=_size(k)
    for tag in ('uselos',): e=ET.Element(tag); e.text='on'; im.insert(0,e)
    L=im.find('layers'); base=L[0]; base.find('parentid').text='-2'
    wl=_S(L,'layer'); _S(wl,'name',None,'Walls'); _S(wl,'id',None,1); _S(wl,'parentid',None,-1); _S(wl,'type',None,'image'); _S(wl,'bitmap'); oc=_S(wl,'occluders')
    for j,(pts,closed) in enumerate(walls):
        o=_S(oc,'occluder'); _S(o,'id',None,j)
        _S(o,'points',None,','.join('%g,%g'%(round(x-W/2,1),round(H/2-y,1)) for x,y in pts))
        if closed: _S(o,'closed')
