import os,sys
V=sys.argv[1]; A=os.path.join(V,'10-Adventures','SP-OP01 — What the Dead Fear')
def edit(p,pairs):
    s=open(p).read()
    for a,b in pairs:
        if a not in s: print('MISSING in',os.path.basename(p),':',a[:70]); continue
        s=s.replace(a,b,1)
    open(p,'w').write(s)
WT='''| d6 | Code | Encounter (4 / 5 / 6 PCs, all Hard) |
|---|---|---|
| 1–2 | W1 | **Husk procession:** 4/5/6 ogre zombies and 4/4/6 husks (zombies), all shuffling toward the ossuary. 5,000 / 6,125 / 7,500 XP. |
| 3–4 | W2 | **Crawler nest:** 5/7/8 ossuary crawlers on a cured limb that fell off its hook. 4,500 / 7,875 / 7,200 XP. |
| 5 | W3 | **Butcher's crew:** 2/3/4 ogre zombies hauling a salt barrel, shadowed by 3/4/4 ossuary crawlers. 4,500 / 7,875 / 7,200 XP. |
| 6 | — | No fight. Ossian's voice speaks in every head at once: *"Hurry, friends. They're getting away."* |'''
OLDWT='''| d6 | Code | Encounter |
|---|---|---|
| 1–2 | W1 | 6 husks (zombies) shuffling along a corridor, all facing the same way: toward the ossuary |
| 3–4 | W2 | 1 ogre zombie in burial linen and 4 husks, carrying a salt barrel |
| 5 | W3 | 2 ossuary crawlers, feeding on a cured limb that fell off its hook |
| 6 | — | No fight. Ossian's voice speaks in every head at once: *"Hurry, friends. They're getting away."* |'''
DAY='''**Adventuring day (2014 DMG; 5,000 XP per 7th-level character).** Allow a short rest after the graveyard and another after Scene 2.

| PCs | Day budget | Four set fights | % | + one Wandering Husks fight | % |
|---|---|---|---|---|---|
| 4 | 20,000 | 15,075 | 75% | 19,575–20,075 | 98–100% |
| 5 | 25,000 | 21,165 | 85% | 27,290–29,040 | 109–116% |
| 6 | 30,000 | 23,575 | 79% | 30,775–31,075 | 103–104% |

With 5 PCs, a wandering fight puts the day over budget, so skip the roll or let Ossian's voice (result 6) stand in.'''
edit(os.path.join(A,'Scenes','Scene 01 — The Grateful Mortician.md'),[
 ('## Fight: The Graveyard Rising (Easy–Medium)','## Fight: The Graveyard Rising (Medium)'),
 ('| E1b | 5 | 8 zombies + 2 ogre zombies | 3,250 | Easy |','| E1b | 5 | 10 zombies + 2 ogre zombies | 4,200 | Medium |')])
edit(os.path.join(A,'Scenes','Scene 02 — The Catacombs.md'),[
 ('Fight: The Kitchen (Easy)','Fight: The Kitchen (Medium)'),
 ('> | E3a | 4 | 2 gibbering mouthers + 6 cured hands | 2,400 | Easy |\n> | E3b | 5 | 3 gibbering mouthers + 6 cured hands | 3,525 | Easy |\n> | E3c | 6 | 3 gibbering mouthers + 10 cured hands | 3,625 | Easy |',
  '> | E3a | 4 | 3 gibbering mouthers + 4 cured hands | 3,475 | Medium |\n> | E3b | 5 | 3 gibbering mouthers + 8 cured hands | 4,290 | Medium |\n> | E3c | 6 | 4 gibbering mouthers + 8 cured hands | 4,700 | Medium |'),
 ('These fights are attrition, not set pieces (trivial to Easy).','Every result is a Hard fight, so roll at most once per rest or delay.'),
 (OLDWT,WT)])
M=os.path.join(A,'SP-OP01-What-the-Dead-Fear.md'); s=open(M).read()
i=s.index('**Adventuring day (4 PCs):**'); j=s.index('\n',i)
s=s[:i]+DAY+s[j:]; open(M,'w').write(s)
edit(M,[
 ('| E1a–c | 01 | 4 / 5 / 6 | The Graveyard Rising: 6/8/10 zombies + 2/2/3 ogre zombies | 3,000 / 3,250 / 4,625 | Medium / Easy / Medium |',
  '| E1a–c | 01 | 4 / 5 / 6 | The Graveyard Rising: 6/10/10 zombies + 2/2/3 ogre zombies | 3,000 / 4,200 / 4,625 | Medium |'),
 ('| E3a–c | 02 (C2) | 4 / 5 / 6 | The Kitchen: 2/3/3 gibbering mouthers + 6/6/10 cured hands | 2,400 / 3,525 / 3,625 | Easy |',
  '| E3a–c | 02 (C2) | 4 / 5 / 6 | The Kitchen: 3/3/4 gibbering mouthers + 4/8/8 cured hands | 3,475 / 4,290 / 4,700 | Medium |'),
 ('| W1–3 | any | any | Wandering Husks (Scene 02 table) | 600–1,350 | trivial–Easy |',
  '| W1–3 | any | 4 / 5 / 6 | Wandering Husks (Scene 02 table) | 4,500–5,000 / 6,125–7,875 / 7,200–7,500 | Hard |')])
F=os.path.join(A,'FGU Kit','build','module.py')
edit(F,[
 ("('E1b','01 The Graveyard Rising (5 PCs)',[('husk',8),('ogrehusk',2)])","('E1b','01 The Graveyard Rising (5 PCs)',[('husk',10),('ogrehusk',2)])"),
 ("(('E3a','02 The Kitchen (4 PCs)',[('mouther',2),('curedhand',6)]),('E3b','02 The Kitchen (5 PCs)',[('mouther',3),('curedhand',6)]),('E3c','02 The Kitchen (6 PCs)',[('mouther',3),('curedhand',10)]))",
  "(('E3a','02 The Kitchen (4 PCs)',[('mouther',3),('curedhand',4)]),('E3b','02 The Kitchen (5 PCs)',[('mouther',3),('curedhand',8)]),('E3c','02 The Kitchen (6 PCs)',[('mouther',4),('curedhand',8)]))"),
 ("for c,n,cr in (('W1','Wandering Husks: 6 husks',[('husk',6)]),('W2','Wandering Husks: ogre husk and 4 husks',[('ogrehusk',1),('husk',4)]),('W3','Wandering Husks: 2 ossuary crawlers',[('crawler',2)])): m.battle(c,n,cr)",
  "for c,n,cr in (('W1a','Wandering: Husk procession (4 PCs)',[('ogrehusk',4),('husk',4)]),('W1b','Wandering: Husk procession (5 PCs)',[('ogrehusk',5),('husk',4)]),('W1c','Wandering: Husk procession (6 PCs)',[('ogrehusk',6),('husk',6)]),\n    ('W2a','Wandering: Crawler nest (4 PCs)',[('crawler',5)]),('W2b','Wandering: Crawler nest (5 PCs)',[('crawler',7)]),('W2c','Wandering: Crawler nest (6 PCs)',[('crawler',8)]),\n    ('W3a',\"Wandering: Butcher's crew (4 PCs)\",[('ogrehusk',2),('crawler',3)]),('W3b',\"Wandering: Butcher's crew (5 PCs)\",[('ogrehusk',3),('crawler',4)]),('W3c',\"Wandering: Butcher's crew (6 PCs)\",[('ogrehusk',4),('crawler',4)])): m.battle(c,n,cr)"),
 ("[m.B(w) for w in ('W1','W2','W3')]+[m.N(k) for k in ('ossian'","[m.B(w+x) for w in ('W1','W2','W3') for x in 'abc']+[m.N(k) for k in ('ossian'"),
 ("[m.B(w) for w in ('W1','W2','W3')]+[m.N('larderghoul')","[m.B(w+x) for w in ('W1','W2','W3') for x in 'abc']+[m.N('larderghoul')"),
 ("W1–W3 are the Wandering Husks","W1–W3 are the Wandering Husks (all Hard)")])
print('done')
