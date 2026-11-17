"""Writes '65-Bestiary/FGU Kit/Sidebar Press Bestiary — Image Prompts.md': a plate prompt (B&W ink) and a colour
portrait prompt (FGU portrait + token source) for every creature in the Sidebar Press Bestiary module."""
import os,re,glob,zlib
from prompt_subjects import S
V=os.path.abspath(os.path.join(os.path.dirname(__file__),'../../..'))
PLATE=('{s}, full figure centered with the head and shoulders in the upper middle of the frame and clear space on every side, classic 1970s fantasy role-playing game rulebook illustration, black ink pen-and-ink drawing on pure white paper, bold hand-inked contour lines, crosshatching and stippling for shadow, textures rendered as hand-drawn patterns, small solid black cast shadow on the ground beneath it, no background, high contrast black and white line art, slightly naive hand-drawn charm --ar 3:4 --v 8.1 --style raw --stylize 75 --seed {seed} --no color, grey wash, gradient shading, painting, watercolor, 3d render, photograph, text, letters, signature, watermark')
PORT=('{s}, {c}, head and shoulders portrait in three-quarter view, the head in the upper middle of the frame with clear space around it, stylized fantasy tabletop RPG creature portrait, crisp painted digital game art, clean confident linework with painterly cel-like shading, vivid but controlled color, soft rim light, strong readable silhouette, on a soft light dusty blue-grey background with a gentle vignette --ar 3:4 --v 8.1 --stylize 150 --seed {seed} --no text, letters, signature, watermark, frame, border, dark background, black background')
C12=[l.split(' | ')[0] for l in []]
def block(name,s,c,where):
    seed=zlib.crc32(name.encode())%90000+10000
    return ('### %s\n*Save as* `%s/%s — Portrait.png` *and* `99-Assets/Bestiary/Print/%s.png`\n\n**Plate (print, black and white)**\n```\n%s\n```\n**Colour portrait (FGU portrait and token source)**\n```\n%s\n```\n'%(name,where,name,name,PLATE.format(s=s,seed=seed),PORT.format(s=s,c=c,seed=seed)))
c12=open(V+'/00-Conversion Projects/C12 - The Forgotten Library of Raanet/FGU Kit/C12 - FG NPC Import.txt').read()
c12n=[re.sub(r'\s*\(.*$','',h).strip() if not h.strip().startswith(('Hydra','Pyrohydra','Dwarf','Elf','Gnome','Halfling')) else h.strip() for h in re.findall(r'^#### \d+ (.*?) ####',c12,re.M)]
c12n=[n if n in S else re.sub(r'\s*\((Area|Areas)[^)]*\)$','',n) for n in c12n]
out=['---','type: reference','tags: [bestiary, art-prompts, fgu]','---','','# Sidebar Press Bestiary — Image Prompts','',
 'One **plate** (black-and-white ink, for print) and one **colour portrait** (FGU portrait and the source for the token) per creature. All prompts use `--v 8.1`. '
 'Minion templates have no prompt: they reskin the creature they are applied to.','',
 '- [ ] = portrait not yet generated. Tick it when the portrait is saved, then we make the token.','']
out+=['## C12 The Forgotten Library of Raanet (new)','']
for n in c12n:
    s,c=S[n]; out.append('- [ ] '+n)
out.append('')
for n in c12n: s,c=S[n]; out.append(block(n,s,c,'99-Assets/Bestiary/FGU/Portraits'))
out+=['## Vault creatures without a prompt yet (new)','']
for n in ['Barrow Dead','Ghoul Rider','Penny-Risen','Cured Hand','Ossuary Crawler','Brother Ossian','Brother-Reaper Ansgar Vell','Cathal Red-Torc','Grukka One-Tusk','Sister Halse']:
    s,c=S[n]; out.append(block(n,s,c,'99-Assets/Bestiary/FGU/Portraits'))
out+=['## Vault creatures with prompts already in their notes','','These are copied from each note\'s **Art Prompt** section (the note stays the master copy).','']
for f in sorted(glob.glob(V+'/65-Bestiary/*.md')+glob.glob(V+'/65-Bestiary/*/*.md')):
    t=open(f).read()
    if '## Art Prompt' not in t or '```text' not in t: continue
    sec=t.split('## Art Prompt',1)[1].split('\n## ',1)[0]
    code=re.findall(r'```\n(.*?)```',sec,re.S)
    n=os.path.basename(f)[:-3]
    out.append('### %s\n[[%s]]\n'%(n,n)+''.join('\n**%s**\n```\n%s```\n'%(lab,c) for lab,c in zip(['Plate (print, black and white)','Colour portrait (FGU portrait and token source)'],code)))
p=V+'/65-Bestiary/FGU Kit/Sidebar Press Bestiary — Image Prompts.md'
open(p,'w').write('\n'.join(out)); print(p, len(c12n), sum(1 for l in out if l.startswith('### ')))
