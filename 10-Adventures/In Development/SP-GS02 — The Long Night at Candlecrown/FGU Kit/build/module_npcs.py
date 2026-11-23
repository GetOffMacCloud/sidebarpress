# ---- SP-GS02 NPCs, encounters and items (exec'd by module.py) ----
HEAD={'Actions':'actions','Bonus Actions':'bonusactions','Reactions':'reactions','Legendary Actions':'legendaryactions','Lair Actions':'lairactions'}
ITEMRX=re.compile(r"^([A-Z][^.]{1,60}?)\. (.+)$")
def fgu_blocks(p):
    """Every FGU import block in a note: plain ```text fences and ones inside > callouts."""
    t=open(p).read(); out=[]
    for mm in re.finditer(r'(?ms)^(> )?```text\n(.*?)^(?:> )?```',t):
        out.append([re.sub(r'^> ?','',l) for l in mm.group(2).strip().split('\n')])
    return out
def addlist(e,tag,items):
    L=e.find(tag)
    if L is None: L=_S(e,tag)
    n=len(L)
    for nm,d in items: n+=1; it=_S(L,ids(n)); _S(it,'desc','string',d); _S(it,'name','string',nm)
def homebrew(key,L,picture=None,name=None):
    nm=L[0]; sz,rest=L[1].split(' ',1); typ,align=rest.rsplit(', ',1)
    ac,actext=re.match(r'Armor Class (\d+)\s*\(?([^)]*)\)?',L[2]).groups(); hp,hd=re.match(r'Hit Points (\d+)\s*(.*)',L[3]).groups()
    speed=L[4][6:]; ab=[int(x) for x in re.findall(r'(\d+) \(',L[6])]
    f={}; i=7
    while not L[i].startswith('Challenge'):
        for lab in ('Saving Throws','Skills','Damage Vulnerabilities','Damage Resistances','Damage Immunities','Condition Immunities','Senses','Languages'):
            if L[i].startswith(lab+' '): f[lab]=L[i][len(lab)+1:]
        i+=1
    cr,xp=re.match(r'Challenge (\S+) \(([\d,]+) XP\)',L[i]).groups(); i+=1
    sec={'traits':[]}; cur=None; tgt=sec['traits']
    for l in L[i:]:
        if l.strip() in HEAD: tgt=sec.setdefault(HEAD[l.strip()],[]); cur=None; continue
        mm=ITEMRX.match(l)
        if mm and not l.startswith('On initiative'): cur=[mm.group(1),mm.group(2)]; tgt.append(cur)
        elif l.strip() and cur: cur[1]+='\n'+l
    lang=f.get('Languages','');lang='' if lang.strip() in ('-','—') else lang
    m.npc(key,name or nm,sz,typ,align,int(ac),'('+actext+')' if actext else '',int(hp),hd.strip(),speed,ab,cr,int(xp.replace(',','')),f.get('Senses',''),lang,
          traits=[tuple(t) for t in sec['traits']],actions=[tuple(a) for a in sec.get('actions',[])],bonus=[tuple(a) for a in sec.get('bonusactions',[])],
          reactions=[tuple(a) for a in sec.get('reactions',[])],skills=f.get('Skills',''),saves=f.get('Saving Throws',''),immunities=f.get('Damage Immunities',''),text='',picture=picture)
    e=m._cat('npc').find(key)
    for lab,tag in (('Damage Resistances','damageresistances'),('Damage Vulnerabilities','damagevulnerabilities'),('Condition Immunities','conditionimmunities')):
        if lab in f: _S(e,tag,'string',f[lab])
    for tag in ('legendaryactions','lairactions'):
        if sec.get(tag): addlist(e,tag,[tuple(a) for a in sec[tag]])
    if picture: _S(e,'token','token',m.imgpath(picture)); m.TOK[key]=m.imgpath(picture)
    return e
def notes(key,xml):
    e=m._cat('npc').find(key); t=e.find('text')
    if t is not None: e.remove(t)
    _FT(e,'text',xml)
def srd(src,name,key,dress,picture=None,**kw):
    m.npc_srd(src,name,key,dress=dress,picture=picture,keep_srd_text=False,**kw)
    e=m._cat('npc').find(key); old=e.find('token')
    if old is not None: e.remove(old)
    if picture: _S(e,'token','token',m.imgpath(picture)); m.TOK[key]=m.imgpath(picture)
    else: m.TOK[key]=''
    return e
def retext(key,subs):
    for x in m._cat('npc').find(key).iter():
        if x.tag in ('name','desc') and x.text:
            for a,b in subs: x.text=x.text.replace(a,b)
BT=sections(body(BEST))
def riders(sec):  # the bestiary's "In SP-GS02 only" / "Riders" bullets as Notes-tab XML
    return C(BT[sec])
# --- homebrew from the GS02 bestiary notes ---
IM=fgu_blocks(NOTEP('Immoth'))[0]
homebrew('hrimvald',IM,picture='scene-seventh-verse',name='Hrimvald the Gatherer (immoth)')
notes('hrimvald','<h>Hrimvald the Gatherer</h><p><i>An immoth: a giant of written ice that gathers the scattered words of a Suel binding-curse. Courtly, patient, and a fair judge of a bargain.</i></p>'+riders('Hrimvald the Gatherer')+'<p><i>Immoth adapted from the 3e Monster Manual II; Sidebar Press conversion.</i></p>')
TY=fgu_blocks(NOTEP('Tyrg'))
homebrew('tyrg',TY[0],picture='scene-candle-stair'); homebrew('tyrgalpha',TY[1],picture='scene-candle-stair',name='Tyrg Alpha ("the Grey Bitch")')
notes('tyrg','<h>Tyrg</h><p>Hrimvald\'s hunting dogs: pony-sized white wolves of the Tors.</p>'+riders('Tyrgs and the alpha')+'<p><i>Sidebar Press conversion (2e MC5).</i></p>')
notes('tyrgalpha','<h>Tyrg Alpha</h><p>The pack\'s grey matriarch. She leads wave 3 at the gate and fights at Hrimvald\'s side if she lives.</p><p><i>Sidebar Press conversion.</i></p>')
homebrew('guardian',fgu_blocks(NOTEP('Ice-Rune Guardian'))[0],name='Ice-Rune Guardian')
notes('guardian','<h>Ice-Rune Guardian</h>'+riders('Ice-rune guardians')+'<p><b>Fire kills it in one splash:</b> a flask of burning oil, or 20 fire damage from one source, melts its Rune Heart.</p><p><i>Sidebar Press homebrew.</i></p>')
# --- minions (APL 6 builds, from the scene callouts) ---
homebrew('tyrgminion',fgu_blocks(SC(1))[0])
homebrew('rimeshard',fgu_blocks(SC(5))[0])
for k in ('tyrgminion','rimeshard'):
    notes(k,'<h>%s</h><p>Built at APL 6 (575 XP). Every four minions count as one creature for the encounter multiplier. Other APLs: see the Minion Pack table in the scene.</p><p><i>Sidebar Press minion template.</i></p>'%html.escape(m.npcname(k)))
# --- SRD copies ---
srd('vampirespawn','Aurel Vasch','aurel','A vampire spawn whose master died in the Passage of Slerotin. Polite, cold, and honest about deals. He can\'t cross the gate, a threshold or the workshop door without a villager\'s invitation; a PC\'s doesn\'t count.',
    picture='npc-aurel',overrides={'alignment':'neutral evil','languages':'Common, Keolandish, Suloise (reads a little)'})
notes('aurel','<h>Aurel Vasch</h>'+riders('Aurel Vasch')+'<p><i>Statblock: vampire spawn, SRD 5.1 (CC-BY-4.0).</i></p>')
srd('priest','Old Mother Sedge','sedge','Shrine-keeper of Telchur. Swap spirit guardians for protection from energy, and guiding bolt for bless. Her shrine is the safety valve.',picture='npc-sedge',overrides={'alignment':'true neutral'})
srd('guard','Dob Kettle (gate-warden)','dob','The gate-warden: spear and lantern. Armed by the party in Scene 09, the gate-watch becomes the militia.',picture='npc-dob-tansy')
srd('guard','Gate-Watch Guard','gateguard','One of the six on the gate-watch. Spears and lanterns.')
srd('commoner','Candlecrown Villager','villager','Lantern-makers, toymakers, singers. Brannoc, Wenna, Corin, Pell and Ash use this block; Tansy is a child (2 hit points) and won\'t fight.')
# ---- encounters: one per party size (4 / 5 / 6 PCs at level 6) ----
def band(code,name,rows,mp):
    for suf,ix,lab in (('a',0,'4 PCs'),('b',1,'5 PCs'),('c',2,'6 PCs')):
        cs=[(k,c[ix]) for k,c in rows if c[ix]]
        m.battle(code+suf,'%s (%s)'%(name,lab),cs,mp)
band('E01','01 The Candle Stair',[('tyrg',(3,4,6))],'map-m1-candle-stair')
m.battle('E04','04 The Coal-Store Scout',[('tyrg',1)],'map-m2-hall-workshop')
band('E05','05 The Rune-Pillar (M7)',[('guardian',(1,1,2))],'map-m3-old-workings')
band('E05x','05/08 Aurel, if fought',[('aurel',(1,1,1)),('guardian',(0,0,1))],'map-m3-old-workings')
band('E06','06 Dusk on the Stair',[('tyrg',(4,5,7))],'map-m1-candle-stair')
band('E10a','10 Wave 1: the Stair',[('tyrg',(3,4,6))],'map-m1-candle-stair')
band('E10b','10 Wave 2: the Mine',[('tyrg',(2,3,4)),('guardian',(1,1,1))],'map-m2-hall-workshop')
band('E10c','10 Wave 3: the Gate',[('tyrgalpha',(1,1,1)),('tyrg',(2,3,4))],'map-m2-candlecrown')
m.battle('E11','11 The Seventh Verse',[('hrimvald',1)],'map-m2-candlecrown')
m.battle('E11x','11 The Seventh Verse, with the alpha alive',[('hrimvald',1),('tyrgalpha',1)],'map-m2-candlecrown')
band('E13','13 The Ice Library',[('hrimvald',(1,1,1)),('guardian',(1,1,2))],'map-m4-ice-library')
m.battle('M1','Minion pack: tyrgs (add four at a time)',[('tyrgminion',4)],'map-m1-candle-stair')
m.battle('M2','Minion pack: rime shards (add four at a time)',[('rimeshard',4)],'map-m3-old-workings')
# ---- items ----
def itemtext(p):
    t=fullnote(p); t=re.split(r'\n## (?:Found In|Continuity|Appearances)',t)[0]
    return C(t)
for key,name in (('lantern','The Long Night Lantern'),('heartrune','Heart-Rune of Hrimvald')):
    p=NOTEP(name); rar=(re.search(r'^rarity: *"?([^"\n]*)',open(p).read(),re.M) or [None,''])[1].title()
    m.item(key,name,'Wondrous Item','<h>%s</h>'%html.escape(name)+itemtext(p),rarity=rar)
for key,name,typ,xml in (
  ('tailtip','Immoth Tail-Tip','Treasure','<p>A long, curved shard of blue ice as thick as a man\'s arm, gnawed by tyrgs, as cold as ice that never melts (M3). A sage pays 100 gp.</p>'),
  ('signet','Halvard Signet Ring','Treasure','<p>A Keoish signet of the house of Halvard, from the hunter\'s purse (M3). 25 gp, and a sequel hook: the family still offers a reward for the bones of Sir Edric Halvard.</p>'),
  ('pendant','Silver Hammer Pendant of Fortubo','Treasure','<p>From the hollow under the chapel altar (M5). 50 gp; a holy symbol of Fortubo.</p>'),
  ('wennapaper',"Wenna's Paper (the written verse)",'Adventuring Gear','<p>A lantern-paper with the seventh verse\'s sounds spelled out in Common letters. Hrimvald can\'t resist a written verse: see the lure in Scene 11. <b>The verse itself is never printed in this module.</b></p>'),
  ('rubbing','Rubbing of the Counter-Verse','Adventuring Gear','<p>A charcoal rubbing of the Suel half of the carving in the chapel (M5). A day\'s work or a DC 15 Intelligence (History) check gives its sounds, enough to sing it; its meaning needs a reader of Suloise.</p>'),
  ('ringwarmth','Ring of Warmth','Ring','<p>From the Keoish envoy\'s satchel in the Ice Library (I6). Standard magic item (requires attunement).</p>'),
  ('wandweb','Wand of Web (7 charges)','Wand','<p>A dwarf\'s carved bone wand from the Ice Library hoard (I6). Standard magic item (requires attunement by a spellcaster).</p>')):
    m.item(key,name,typ,xml)
