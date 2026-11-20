"""Round, transparent tokens for Fantasy Grounds (Sidebar Press, 2026-11-20).
Print art keeps its white background; the module gets a 512 px RGBA PNG per token,
cut just outside the token's own ring, or (no ring) cropped to a circle and given
the house double ring (thick outer, thin inner, as on the GA5 lamb token)."""
import math
from PIL import Image, ImageDraw
SIZE=512; SS=4

def _ring_circle(g):
    """Find a drawn ring: outermost dark pixel along 72 rays from the centre."""
    w,h=g.size; cx,cy=w/2,h/2; px=g.load(); R=min(w,h)/2-1; pts=[]
    for k in range(72):
        a=2*math.pi*k/72; dx,dy=math.cos(a),math.sin(a)
        for r in range(int(R),int(R*0.6),-1):
            x,y=int(cx+dx*r),int(cy+dy*r)
            if px[x,y]<110: pts.append((x,y)); break
    if len(pts)<60: return None
    xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
    ccx=(min(xs)+max(xs))/2; ccy=(min(ys)+max(ys))/2
    rr=sorted(math.hypot(x-ccx,y-ccy) for x,y in pts); r=rr[len(rr)//2]
    if rr[int(len(rr)*0.9)]-rr[int(len(rr)*0.1)]>0.04*r: return None   # not a clean circle
    return ccx,ccy,r

def make(src,dst,ringed=None):
    im=Image.open(src).convert('RGB'); g=im.convert('L')
    found=_ring_circle(g) if ringed is not False else None
    if found:
        cx,cy,r=found; r+=3
        im=im.crop((int(cx-r),int(cy-r),int(cx+r),int(cy+r)))
        art=im.resize((SIZE*SS,SIZE*SS),Image.LANCZOS).convert('RGBA')
    else:
        s=min(im.size); l=(im.width-s)//2; t=(im.height-s)//2
        art=im.crop((l,t,l+s,t+s)).resize((SIZE*SS,SIZE*SS),Image.LANCZOS).convert('RGBA')
        d=ImageDraw.Draw(art); C=SIZE*SS/2; R=C-2*SS
        # white band between the rings, then the house double ring
        r2=R-21*SS
        band=Image.new('L',art.size,0); bd=ImageDraw.Draw(band)
        bd.ellipse((C-R-4*SS,C-R-4*SS,C+R+4*SS,C+R+4*SS),fill=255); bd.ellipse((C-r2,C-r2,C+r2,C+r2),fill=0)
        art.paste((255,255,255,255),(0,0),band)
        d.ellipse((C-R,C-R,C+R,C+R),outline=(0,0,0,255),width=int(7*SS))
        d.ellipse((C-r2,C-r2,C+r2,C+r2),outline=(0,0,0,255),width=int(2.5*SS))
    mask=Image.new('L',art.size,0); C=art.width/2
    ImageDraw.Draw(mask).ellipse((1,1,art.width-2,art.height-2),fill=255)
    art.putalpha(mask)
    art.resize((SIZE,SIZE),Image.LANCZOS).save(dst,'PNG')
    return bool(found)
