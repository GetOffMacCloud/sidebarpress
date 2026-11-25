"""The nine Slave Lords tournament characters, 5th level (2014 PHB), per A1 ledger §8.
One data table feeds both the vault notes (notes()) and the FG pregencharsheet records (add_fg(m, srdsp))."""
import re,html
import xml.etree.ElementTree as ET
AB=['strength','dexterity','constitution','intelligence','wisdom','charisma']
SK={'Acrobatics':'dexterity','Animal Handling':'wisdom','Arcana':'intelligence','Athletics':'strength','Deception':'charisma','History':'intelligence','Insight':'wisdom','Intimidation':'charisma','Investigation':'intelligence','Medicine':'wisdom','Nature':'intelligence','Perception':'wisdom','Performance':'charisma','Persuasion':'charisma','Religion':'intelligence','Sleight of Hand':'dexterity','Stealth':'dexterity','Survival':'wisdom'}
mod=lambda x:(x-10)//2
# weapons: (name, attack stat, dice, damage type, magic/style attack bonus, damage bonus, ranged)
P=[
dict(n=1,name='Elwita',sex='F',race='Mountain Dwarf',al='Lawful Good',bg='Soldier',cls=[('Fighter',5,'d10')],sub='Champion',
 sc=[20,11,20,12,8,15],saves=['strength','constitution'],skills=['Athletics','Intimidation','Perception','Survival'],
 ac=22,actext='plate, shield +1, Defense style',speed=25,hp=59,size='Medium',senses='Darkvision 60 ft.',
 lang=['Common','Dwarvish'],prof=['All armor, shields','Simple and martial weapons',"Smith's tools",'Dice set','Vehicles (land)'],
 wpn=[('Warhammer +1','strength','d8','bludgeoning',1,1,0),('Heavy crossbow','dexterity','d10','piercing',0,0,1),('Dagger','strength','d4','piercing',0,0,0)],
 inv=['Plate armor','Shield +1','Warhammer +1','Heavy crossbow','20 crossbow bolts','Dagger','Belt pouch (large)','12 iron spikes','Chisel','Large sack','Wineskin','50 ft. of hempen rope'],
 feat=[('Fighting Style: Defense','+1 AC while wearing armor.'),('Second Wind','Bonus action: regain 1d10 + 5 hit points. Once per short rest.'),('Action Surge','One extra action on your turn. Once per short rest.'),('Improved Critical','Your weapon attacks score a critical hit on a roll of 19 or 20.'),('Extra Attack','Attack twice when you take the Attack action.'),('Dwarven Resilience','Advantage on saves against poison; resistance to poison damage.'),('Stonecunning','Double proficiency on History checks about stonework.'),('Ability Score Improvement','Strength 19 to 20.')],
 spells=None,note='The party\'s wall: AC 22, two hammer blows a round, crits on 19.'),
dict(n=2,name='"Ogre"',sex='M',race='Human',al='Neutral Good',bg='Soldier',cls=[('Fighter',5,'d10')],sub='Battle Master',
 sc=[20,13,19,9,10,7],saves=['strength','constitution'],skills=['Athletics','Intimidation','Perception','Survival'],
 ac=20,actext='splint armor +1, shield',speed=30,hp=54,size='Medium',senses='',
 lang=['Common','Orc'],prof=['All armor, shields','Simple and martial weapons','Dice set','Vehicles (land)'],
 wpn=[('Longsword +1','strength','d8','slashing',1,3,0),('Longbow','dexterity','d8','piercing',0,0,1),('Dagger (throwing knife)','strength','d4','piercing',0,0,0)],
 inv=['Splint armor +1','Shield','Longsword +1','Longbow','Quiver and 20 arrows','Dagger','Backpack','Waterskin','Flask of oil','Blanket','50 ft. of hempen rope'],
 feat=[('Fighting Style: Dueling','+2 damage with a one-handed melee weapon and no other weapon.'),('Second Wind','Bonus action: regain 1d10 + 5 hit points. Once per short rest.'),('Action Surge','One extra action on your turn. Once per short rest.'),('Combat Superiority','4 superiority dice (d8), regained on a short rest. Save DC 16. Maneuvers: Trip Attack, Riposte, Menacing Attack.'),('Student of War',"Proficient with smith's tools."),('Extra Attack','Attack twice when you take the Attack action.'),('Ability Score Improvement','Strength 19 to 20.')],
 spells=None,note='Strongest arm in the party; superiority dice knock foes prone or send them running.'),
dict(n=3,name='Freda',sex='F',race='Human',al='Chaotic Good',bg='Outlander',cls=[('Ranger',5,'d10')],sub='Hunter',
 sc=[16,20,18,14,16,15],saves=['strength','dexterity'],skills=['Athletics','Survival','Perception','Stealth','Nature'],
 ac=19,actext='chain mail +1, shield',speed=30,hp=54,size='Medium',senses='',
 lang=['Common','Elvish','Halfling'],prof=['Light and medium armor, shields','Simple and martial weapons','Flute'],
 wpn=[('Longsword','strength','d8','slashing',0,0,0),('Longbow (Archery)','dexterity','d8','piercing',2,0,1),('Longbow with arrow +1','dexterity','d8','piercing',3,1,1),('Dagger','dexterity','d4','piercing',0,0,0),('Spear','strength','d6','piercing',0,0,0)],
 inv=['Chain mail +1','Shield','Longsword','Longbow','Quiver with 12 arrows','8 arrows +1','Dagger','Spear','Potion of healing','Backpack','Tinderbox','6 torches','50 ft. of hempen rope'],
 feat=[('Favored Enemy','Humanoids (orcs and humans): advantage on Survival checks to track them and Intelligence checks to recall information about them.'),('Natural Explorer','Underdark.'),('Fighting Style: Archery','+2 to attack rolls with ranged weapons.'),('Primeval Awareness','Spend a spell slot to sense aberrations, celestials, dragons, elementals, fey, fiends and undead within 1 mile for 1 minute per slot level.'),('Hunter: Colossus Slayer','Once per turn, +1d8 damage to a creature below its hit point maximum.'),('Extra Attack','Attack twice when you take the Attack action.'),('Ability Score Improvement','Dexterity 18 to 20.')],
 spells=dict(stat='wisdom',slots=[4,2],cantrips=[],known=['hunter\'s mark','cure wounds','goodberry','pass without trace'],type='spontaneous'),
 note='The archer: three ways to hit something far away, and the best tracker in the group.'),
dict(n=4,name='Karraway',sex='M',race='Human',al='Lawful Good',bg='Acolyte',cls=[('Cleric',5,'d8')],sub='Life Domain',
 sc=[10,16,18,13,18,14],saves=['wisdom','charisma'],skills=['Insight','Religion','Medicine','History'],
 ac=20,actext='plate, shield',speed=20,hp=48,size='Medium',senses='',
 lang=['Common','Celestial','Dwarvish'],prof=['All armor, shields','Simple weapons'],
 wpn=[('Mace','strength','d6','bludgeoning',0,0,0),('Warhammer','strength','d8','bludgeoning',0,0,0)],
 inv=['Plate armor','Shield','Mace (footman\'s mace)','Warhammer','Spell scroll (clairvoyance)','Spell scroll (revivify)','Silver holy symbol','Vial of holy water','Hooded lantern','Flask of oil','Backpack','10 iron spikes'],
 feat=[('Disciple of Life','Healing spells of 1st level or higher restore an extra 2 + the spell\'s level in hit points.'),('Channel Divinity (1/rest)','Turn Undead, or Preserve Life: restore 25 hit points divided among creatures within 30 feet (up to half each one\'s maximum).'),('Destroy Undead','Turned undead of CR 1/2 or lower are destroyed.'),('Heavy armor note','Plate needs Strength 15: Karraway\'s speed is 20 feet in it.'),('Ability Score Improvement','Wisdom 17 to 18, Constitution 17 to 18.')],
 spells=dict(stat='wisdom',slots=[4,3,2],cantrips=['light','sacred flame','spare the dying'],known=['bless','cure wounds','lesser restoration','spiritual weapon','beacon of hope','revivify','command','guiding bolt','healing word','hold person','silence','find traps','dispel magic','remove curse','protection from poison'],type='memorization'),
 note='The healer. Life domain spells always prepared: bless, cure wounds, lesser restoration, spiritual weapon, beacon of hope, revivify.'),
dict(n=5,name='Blodgett',sex='M',race='Lightfoot Halfling',al='Neutral Good',bg='Criminal',cls=[('Rogue',5,'d8')],sub='Thief',
 sc=[8,20,18,10,10,7],saves=['dexterity','intelligence'],skills=['Deception','Stealth','Acrobatics','Perception','Sleight of Hand','Investigation'],expert=['Stealth'],
 ac=17,actext='leather, ring of protection',speed=25,hp=48,size='Small',senses='',
 lang=['Common','Halfling',"Thieves' cant"],prof=['Light armor','Simple weapons, hand crossbows, longswords, rapiers, shortswords',"Thieves' tools (expertise)",'Dice set'],
 wpn=[('Shortsword','dexterity','d6','piercing',0,0,0),('Dagger','dexterity','d4','piercing',0,0,0),('Sling','dexterity','d4','bludgeoning',0,0,1)],
 inv=['Leather armor','Shortsword','Dagger','Sling','20 sling bullets','Ring of protection','Boots of elvenkind',"Thieves' tools",'Belt pouch (small)','Tinderbox','2 flasks of oil','20 ft. of hempen rope','4 iron spikes','Waterskin'],
 feat=[('Expertise',"Stealth and thieves' tools (double proficiency; thieves' tools +11)."),('Sneak Attack (3d6)','Once per turn with advantage, or with an ally beside the target.'),('Cunning Action','Bonus action: Dash, Disengage or Hide.'),('Fast Hands','Cunning Action can also make a Sleight of Hand check, use thieves\' tools, or Use an Object.'),('Second-Story Work','Climbing costs no extra movement; running jumps +5 ft.'),('Uncanny Dodge','Reaction: halve the damage of an attack you can see.'),('Lucky','Reroll a natural 1 on an attack roll, ability check or saving throw.'),('Naturally Stealthy','Can hide behind a creature at least one size larger.'),('Ability Score Improvement','Constitution 16 to 18.')],
 spells=None,note="The scout: Stealth +11 (advantage with the boots of elvenkind), thieves' tools +11. The 1e tournament scored a bonus for casting invisibility on him at the start."),
dict(n=6,name='Dread Delgath',sex='M',race='Human',al='Neutral Good',bg='Sage',cls=[('Wizard',5,'d6')],sub='School of Evocation',
 sc=[9,10,17,20,13,16],saves=['intelligence','wisdom'],skills=['Arcana','History','Investigation','Insight'],
 ac=12,actext='bracers of defense; 15 with mage armor',speed=30,hp=37,size='Medium',senses='',
 lang=['Common','Draconic','Elvish','Orc'],prof=['Daggers, darts, slings, quarterstaffs, light crossbows'],
 wpn=[('Quarterstaff','strength','d6','bludgeoning',0,0,0),('Dagger','dexterity','d4','piercing',0,0,0)],
 inv=['Bracers of defense','Wand of fireballs (4 charges)','Quarterstaff','Dagger','Spellbook','Component pouch','Belt pouch (large)','2 flasks of oil','3 tallow candles','2 torches','Tinderbox'],
 feat=[('Arcane Recovery','Once a day after a short rest, recover spell slots totalling up to 3 levels.'),('Evocation Savant','Copying evocation spells costs half.'),('Sculpt Spells','Protect 1 + spell level creatures from your evocation spells: they auto-succeed and take no damage.'),('Wand of fireballs','Up to 3 charges per use: fireball (DC 15), +1d6 per charge after the first.'),('Ability Score Improvement','Intelligence 19 to 20.')],
 spells=dict(stat='intelligence',slots=[4,3,2],cantrips=['fire bolt','light','mage hand','ray of frost'],known=['magic missile','shield','mage armor','detect magic','burning hands','spider climb','levitate','detect thoughts','slow','fireball'],type='memorization'),
 note='The artillery. Sculpt Spells lets him drop a fireball on a melee without roasting the party. The 1e scoring docks points for fireballing the slaves in T12.'),
dict(n=7,name='Phanstern',sex='M',race='Human',al='Chaotic Good',bg='Charlatan',cls=[('Wizard',5,'d6')],sub='School of Illusion',
 sc=[9,19,17,20,13,10],saves=['intelligence','wisdom'],skills=['Deception','Sleight of Hand','Arcana','Investigation'],
 ac=14,actext='Dex; 17 with mage armor',speed=30,hp=37,size='Medium',senses='',
 lang=['Common','Elvish','Gnomish'],prof=['Daggers, darts, slings, quarterstaffs, light crossbows','Disguise kit','Forgery kit'],
 wpn=[('Dagger (silvered)','dexterity','d4','piercing',0,0,0)],
 inv=['Silvered dagger','Potion of greater healing','Spell scroll (blindness/deafness)','Spell scroll (blur)','Spellbook','Component pouch','Bullseye lantern','Flask of oil','Steel mirror','Robe','Wineskin','Belt pouch (small)'],
 feat=[('Arcane Recovery','Once a day after a short rest, recover spell slots totalling up to 3 levels.'),('Illusion Savant','Copying illusion spells costs half.'),('Improved Minor Illusion','Minor illusion makes a sound and an image together.'),('Ability Score Improvement','Intelligence 18 to 20.')],
 spells=dict(stat='intelligence',slots=[4,3,2],cantrips=['minor illusion','light','mage hand','ray of frost'],known=['disguise self','color spray','fog cloud','shield','silent image','mirror image','hold person','invisibility','hypnotic pattern','major image'],type='memorization'),
 note='Control and trickery: hypnotic pattern, hold person, fog cloud. In 1e he was an illusionist; the 5e Illusion school keeps his spell list close.'),
dict(n=8,name='Eljayess',sex='M',race='Half-Elf',al='Chaotic Good',bg='Soldier',cls=[('Cleric',3,'d8'),('Fighter',2,'d10')],sub='War Domain',
 sc=[17,12,17,9,17,15],saves=['wisdom','charisma'],skills=['Athletics','Intimidation','Religion','Medicine','Perception','Persuasion'],
 ac=20,actext='plate, shield',speed=30,hp=45,size='Medium',senses='Darkvision 60 ft.',
 lang=['Common','Elvish','Celestial'],prof=['All armor, shields','Simple and martial weapons','Dice set','Vehicles (land)'],
 wpn=[('Spear +1','strength','d6','piercing',1,3,0),('Longsword','strength','d8','slashing',0,2,0),('Longbow','dexterity','d8','piercing',0,0,1),('Light hammer','strength','d4','bludgeoning',0,2,0)],
 inv=['Plate armor','Shield','Spear +1','Longsword','Longbow','Quiver and 20 arrows','Light hammer','Potion of speed','Wooden holy symbol','Vial of holy water','Small pouch','50 ft. of hempen rope','Waterskin'],
 feat=[('War Priest (3/long rest)','When you take the Attack action, make one weapon attack as a bonus action.'),('Channel Divinity (1/rest)','Turn Undead, or Guided Strike: +10 to one attack roll after seeing the roll.'),('Fighting Style: Dueling','+2 damage with a one-handed melee weapon and no other weapon.'),('Second Wind','Bonus action: regain 1d10 + 2 hit points. Once per short rest.'),('Action Surge','One extra action on your turn. Once per short rest.'),('Fey Ancestry','Advantage on saves against being charmed; magic can\'t put you to sleep.')],
 spells=dict(stat='wisdom',slots=[4,2],cantrips=['guidance','light','sacred flame'],known=['divine favor','shield of faith','magic weapon','spiritual weapon','bless','command','cure wounds','healing word','hold person','silence'],type='memorization'),
 note='Cleric 3 / Fighter 2. War domain spells always prepared: divine favor, shield of faith, magic weapon, spiritual weapon.'),
dict(n=9,name='Kayen Telva',sex='M',race='High Elf',al='Chaotic Good',bg='Sage',cls=[('Fighter',2,'d10'),('Wizard',3,'d6')],sub='School of Abjuration',
 sc=[15,18,15,18,10,9],saves=['strength','constitution'],skills=['Perception','Athletics','Acrobatics','Arcana','History'],
 ac=18,actext='elven chain (mithral chain shirt), shield, Defense style',speed=30,hp=34,size='Medium',senses='Darkvision 60 ft.',
 lang=['Common','Elvish','Draconic','Gnoll'],prof=['All armor, shields','Simple and martial weapons'],
 wpn=[('Longsword','strength','d8','slashing',0,0,0),('Longbow','dexterity','d8','piercing',0,0,1),('Handaxe','strength','d6','slashing',0,0,0),('Javelin of lightning','strength','d6','piercing',0,0,1)],
 inv=['Elven chain (mithral chain shirt)','Shield','Longsword','Longbow','Quiver and 12 arrows','Handaxe','Dagger','2 javelins of lightning','Spell scroll (arcane lock)','Spell scroll (suggestion)','Spellbook','Component pouch','Small sack','Scroll case','Parchment, quill and ink','Brown candle'],
 feat=[('Fighting Style: Defense','+1 AC while wearing armor.'),('Second Wind','Bonus action: regain 1d10 + 2 hit points. Once per short rest.'),('Action Surge','One extra action on your turn. Once per short rest.'),('Arcane Recovery','Once a day after a short rest, recover spell slots totalling up to 2 levels.'),('Arcane Ward','Casting an abjuration spell of 1st level or higher makes a ward of 10 hit points (twice wizard level + Int).'),('Javelin of lightning','Speak its command word as you throw: a 5-ft.-wide, 120-ft. line of lightning, DC 13 Dex save, 4d6 lightning (half on a success); +4d6 to the target. Once per dawn each.'),('Fey Ancestry / Trance','Advantage on saves against being charmed; magic can\'t put you to sleep; 4-hour trance.')],
 spells=dict(stat='intelligence',slots=[4,2],cantrips=['fire bolt','light','mage hand','shocking grasp'],known=['charm person','sleep','shield','magic missile','invisibility','knock','misty step'],type='memorization'),
 note='Fighter 2 / Wizard 3 in elven chain: casts in armor, keeps invisibility and knock from 1e.'),
]
def prof_bonus(p): return 3
def lvl(p): return sum(l for _,l,_ in p['cls'])
def spell_dc(p): st=p['spells']['stat']; return 8+3+mod(p['sc'][AB.index(st)])
def skill_total(p,s): return mod(p['sc'][AB.index(SK[s])])+3*(2 if s in p.get('expert',[]) else 1)
def save_total(p,a): return mod(p['sc'][AB.index(a)])+(3 if a in p['saves'] else 0)
def ordl(l): return {0:'Cantrips',1:'1st',2:'2nd',3:'3rd'}[l]
def title(s): return ' '.join(w if w in ('of','from') else w[:1].upper()+w[1:] for w in s.split())

def notes(srdsp):
    out={}
    for p in P:
        nm=p['name'].strip('"'); cls=' / '.join('%s %d'%(c,l) for c,l,_ in p['cls'])
        L=['---','type: pregen','adventure: "A0–A4 Against the Slave Lords (Convention Mode)"','tags: [pregen, adventure/A1, slave-lords]','level: 5','publish: true','---',
           '# %s'%p['name'],'','> *Tournament character %d.* %s %s, %s (%s). %s background. %s.'%(p['n'],p['race'],cls,p['sub'],p['al'],p['bg'],p['note']),'',
           '| Str | Dex | Con | Int | Wis | Cha |','|---|---|---|---|---|---|','| '+' | '.join('%d (%+d)'%(x,mod(x)) for x in p['sc'])+' |','',
           '- **Armor Class** %d (%s)'%(p['ac'],p['actext']),'- **Hit Points** %d · **Speed** %d ft. · **Proficiency** +3'%(p['hp'],p['speed']),
           '- **Saving Throws** '+', '.join('%s %+d'%(a[:3].title(),save_total(p,a)) for a in p['saves']),
           '- **Skills** '+', '.join('%s %+d'%(s,skill_total(p,s)) for s in p['skills']),
           '- **Senses** '+((p['senses']+', ') if p['senses'] else '')+'passive Perception %d'%(10+(skill_total(p,'Perception') if 'Perception' in p['skills'] else mod(p['sc'][4]))),
           '- **Languages** '+', '.join(p['lang']),'- **Proficiencies** '+'; '.join(p['prof']),'','## Attacks','','| Weapon | To hit | Damage |','|---|---|---|']
        for w,st,d,t,ab,db,rg in p['wpn']:
            sm=mod(p['sc'][AB.index(st)]); L.append('| %s | %+d | %s%+d %s |'%(w,sm+3+ab,'1'+d,sm+db,t))
        L+=['','## Features','']+['- **%s.** %s'%(a,b) for a,b in p['feat']]
        if p['spells']:
            S=p['spells']; L+=['','## Spells','','Save DC %d, spell attack %+d (%s). Slots: %s.'%(spell_dc(p),spell_dc(p)-8,S['stat'].title(),', '.join('%s %d'%(ordl(i+1),n) for i,n in enumerate(S['slots']))),'']
            if S['cantrips']: L.append('- **Cantrips:** '+', '.join('*%s*'%x for x in S['cantrips']))
            by={}
            for x in S['known']: by.setdefault(int(srdsp[x].findtext('level')),[]).append(x)
            for l in sorted(by): L.append('- **%s level:** '%ordl(l)+', '.join('*%s*'%x for x in by[l]))
        L+=['','## Equipment','',', '.join(p['inv'])+'.','','*1e original: A1 p. 48–49 (tournament characters). Built per [[A1 - 5e Conversion Ledger]] §8.*','']
        out[nm]='\n'.join(L)
    return out

def _S(p,tag,typ=None,text=None):
    e=ET.SubElement(p,tag)
    if typ: e.set('type',typ)
    if text is not None: e.text=str(text)
    return e
def _ft(p,tag,txt):
    e=ET.fromstring('<%s type="formattedtext">%s</%s>'%(tag,txt,tag)); p.append(e); return e
ids=lambda n:'id-%05d'%n
def add_fg(root,srdsp):
    """Append <pregencharsheet> to the module db root."""
    import copy
    R=_S(root,'pregencharsheet')
    for i,p in enumerate(P,1):
        c=_S(R,ids(i)); A=_S(c,'abilities')
        for a,x in zip(AB,p['sc']):
            e=_S(A,a); _S(e,'bonus','number',mod(x)); _S(e,'save','number',save_total(p,a)); _S(e,'savemodifier','number',0); _S(e,'saveprof','number',1 if a in p['saves'] else 0); _S(e,'score','number',x)
        _S(c,'background','string',p['bg'])
        C=_S(c,'classes')
        for k,(cn,l,hd) in enumerate(p['cls'],1):
            e=_S(C,ids(k)); _S(e,'hddie','dice',hd); _S(e,'hdused','number',0); _S(e,'level','number',l); _S(e,'name','string',cn)
        co=_S(c,'coins')
        for k,(cn,a) in enumerate((('GP',25),('PP',0),('EP',0),('SP',0),('CP',0)),1):
            e=_S(co,ids(k)); _S(e,'amount','number',a); _S(e,'name','string',cn)
        D=_S(_S(c,'defenses'),'ac'); _S(D,'armor','number',0); _S(D,'dexbonus','string','full'); _S(D,'misc','number',p['ac']-10-mod(p['sc'][1])); _S(D,'prof','number',1); _S(D,'shield','number',0); _S(D,'temporary','number',0); _S(D,'total','number',p['ac'])
        _S(c,'exp','number',6500); _S(c,'expneeded','number',14000)
        F=_S(c,'featurelist')
        for k,(a,b) in enumerate(p['feat'],1):
            e=_S(F,ids(k)); _S(e,'level','number',lvl(p)); _S(e,'name','string',a); _S(e,'source','string',p['cls'][0][0]); _ft(e,'text','<p>%s</p>'%html.escape(b))
        e=_S(F,ids(len(p['feat'])+1)); _S(e,'name','string','Subclass: '+p['sub']); _S(e,'source','string',p['cls'][-1][0] if 'Wizard' in [x[0] for x in p['cls']] and p['sub'].startswith('School') else p['cls'][0][0]); _ft(e,'text','<p>%s</p>'%html.escape(p['note']))
        h=_S(c,'hp'); _S(h,'deathsavefail','number',0); _S(h,'deathsavesuccess','number',0); _S(h,'temporary','number',0); _S(h,'total','number',p['hp']); _S(h,'wounds','number',0)
        ini=_S(c,'initiative'); _S(ini,'misc','number',0); _S(ini,'total','number',mod(p['sc'][1]))
        I=_S(c,'inventorylist')
        for k,x in enumerate(p['inv'],1):
            e=_S(I,ids(k)); _S(e,'carried','number',2); _S(e,'count','number',1); _S(e,'isidentified','number',1); _S(e,'name','string',x)
        La=_S(c,'languagelist')
        for k,x in enumerate(p['lang'],1): _S(_S(La,ids(k)),'name','string',x)
        _S(c,'level','number',lvl(p)); _S(c,'name','string',p['name'])
        pp=10+(skill_total(p,'Perception') if 'Perception' in p['skills'] else mod(p['sc'][4])); _S(c,'perception','number',pp)
        _S(c,'profbonus','number',3)
        Pr=_S(c,'proficiencylist')
        for k,x in enumerate(p['prof'],1): _S(_S(Pr,ids(k)),'name','string',x)
        _S(c,'race','string',p['race']); _S(c,'senses','string',((p['senses']+', ') if p['senses'] else '')+'Passive Perception %d'%pp); _S(c,'size','string',p['size'])
        Sk=_S(c,'skilllist')
        for k,s in enumerate(p['skills'],1):
            e=_S(Sk,ids(k)); _S(e,'misc','number',0); _S(e,'name','string',s); _S(e,'prof','number',2 if s in p.get('expert',[]) else 1); _S(e,'stat','string',SK[s]); _S(e,'total','number',skill_total(p,s))
        sp=_S(c,'speed'); _S(sp,'armor','number',0); _S(sp,'base','number',p['speed']); _S(sp,'misc','number',0); _S(sp,'temporary','number',0); _S(sp,'total','number',p['speed'])
        W=_S(c,'weaponlist')
        for k,(w,st,d,t,ab,db,rg) in enumerate(p['wpn'],1):
            e=_S(W,ids(k)); _S(e,'attackbonus','number',ab); _S(e,'attackstat','string',st); _S(e,'carried','number',2)
            dl=_S(_S(e,'damagelist'),ids(1)); _S(dl,'bonus','number',db); _S(dl,'dice','dice',d); _S(dl,'stat','string',st); _S(dl,'type','string',t)
            _S(e,'name','string',w); _S(e,'prof','number',1); _S(e,'type','number',rg)
        if p['spells']:
            S=p['spells']; g=_S(_S(c,'powergroup'),ids(1)); _S(g,'atkmod','number',spell_dc(p)-8); _S(g,'castertype','string',S['type']); _S(g,'name','string','Spells'); _S(g,'savedc','number',spell_dc(p)); _S(g,'stat','string',S['stat'])
            pm=_S(c,'powermeta')
            for l,n in enumerate(S['slots'],1):
                e=_S(pm,'spellslots%d'%l); _S(e,'max','number',n); _S(e,'used','number',0)
            Pw=_S(c,'powers')
            for k,x in enumerate(S['cantrips']+S['known'],1):
                e=copy.deepcopy(srdsp[x]); e.tag=ids(k); _S(e,'group','string','Spells'); _S(e,'prepared','number',1)
                for t in ('source',):
                    y=e.find(t)
                    if y is not None: e.remove(y)
                Pw.append(e)
    return R
