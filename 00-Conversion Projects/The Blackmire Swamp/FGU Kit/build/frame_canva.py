"""Frame the Canva token art (99-Assets/SP-CV01/token-art) with the Blackmire bronze ring.
Output: 99-Assets/SP-CV01/tokens/<Name> — Token.png (512 px, transparent outside the ring)."""
import os
from PIL import Image,ImageEnhance
import tokens as T
S=T.S
H=os.path.dirname(os.path.abspath(__file__))
ASSETS=next(p for p in [os.path.join(H,'..','..','..','..','99-Assets','SP-CV01'),os.path.expanduser('~/mnt/99-Assets/SP-CV01')] if os.path.isdir(p))
ART=os.path.join(ASSETS,'token-art'); OUT=os.path.join(ASSETS,'tokens'); os.makedirs(OUT,exist_ok=True)
# key: (display name, ring accent, crop inset — portraits already sit in a circle, so trim a little)
TOK={'juvenilecrocodile':('Juvenile Crocodile',T.GREEN,0.0),'huntingcrocodile':('Hunting Crocodile',T.TEAL,0.0),
 'alphacrocodile':('Alpha Crocodile',T.AMBER,0.0),'swamptyrant':('Swamp Tyrant Crocodile',T.RED,0.0),
 'thornheart':('The Thorn-Heart Archdruid Crocodile',T.GOLD,0.0),'drownedsentry':('Drowned Sentry',T.TEAL,0.0),
 'rootboundsentinel':('Rootbound Sentinel',T.GREEN,0.0),'mireechospirit':('Mire-Echo Spirit',(160,230,200),0.0),
 'oldmarrowfinch':('Old Marrow Finch',T.GOLD,0.04),'sistervell':('Sister Vell',T.GOLD,0.04),
 'captainrusk':('Captain Rusk Ironstake',T.GOLD,0.04),'silt':('Silt',T.GOLD,0.04),'astervale':('Aster Vale',T.GOLD,0.04)}
def path(key): return os.path.join(OUT,TOK[key][0]+' — Token.png')
if __name__=='__main__':
    for key,(name,accent,inset) in TOK.items():
        im=Image.open(os.path.join(ART,name+' — Token Art.jpg')).convert('RGB'); w,h=im.size; s=min(w,h); i=int(s*inset)
        im=im.crop(((w-s)//2+i,(h-s)//2+i,(w+s)//2-i,(h+s)//2-i)).resize((S,S),Image.LANCZOS)
        im=ImageEnhance.Brightness(im).enhance(1.12)  # lift the very dark art slightly so it reads at grid size
        T.OUT=OUT; T.finish(T.ring(im,accent),name+' — Token')
    print(sorted(os.listdir(OUT)))
