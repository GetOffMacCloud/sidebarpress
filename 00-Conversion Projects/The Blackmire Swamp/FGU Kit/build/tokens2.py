"""Painterly pass for Blackmire creature tokens: anatomy along a curved spine, skin textured
from the book's own location art, emboss lighting, ripples. Imports helpers from tokens.py."""
import math,random,os
from PIL import Image,ImageDraw,ImageFilter,ImageChops,ImageEnhance,ImageOps
import tokens as T
S,R,SRC=T.S,T.R,T.SRC
def tex(src,box,tint):
    im=Image.open(os.path.join(SRC,src)).convert('L').crop(box).resize((S,S),Image.LANCZOS)
    im=ImageOps.autocontrast(im,cutoff=2)
    return Image.merge('RGB',[im.point(lambda v,c=c:int(c*(0.45+v/255*0.9))) for c in tint])
def spine(L,wave,phase,N=200):
    pts=[]
    for i in range(N+1):
        t=i/N; y=R-L/2+L*t; x=R+wave*L*(max(0,t-0.35)**1.6)*math.sin(phase+t*4.2)
        pts.append((x,y,t))
    return pts
def width(t,L,bulk):
    k=[(0,0.012),(0.04,0.03),(0.11,0.036),(0.16,0.058),(0.21,0.052),(0.30,0.09),(0.42,0.10),(0.52,0.088),(0.60,0.06),(0.80,0.03),(1.0,0.004)]
    for (a,wa),(b,wb) in zip(k,k[1:]):
        if a<=t<=b: return L*bulk*(wa+(wb-wa)*(t-a)/(b-a))
    return 2
def croc(scale,skin,eye,seed,bulk=1.0,wave=0.10,thorns=False,glow=None,angle=-30):
    rnd=random.Random(seed); L=S*0.88*scale
    P=spine(L,wave,rnd.uniform(0,3)); m=Image.new('L',(S,S),0); d=ImageDraw.Draw(m)
    left=[];right=[]
    for i,(x,y,t) in enumerate(P):
        x2,y2,_=P[min(i+1,len(P)-1)]; x1,y1,_=P[max(i-1,0)]; dx,dy=x2-x1,y2-y1; n=math.hypot(dx,dy) or 1
        nx,ny=-dy/n,dx/n; w=width(t,L,bulk); left.append((x+nx*w,y+ny*w)); right.append((x-nx*w,y-ny*w))
    d.polygon(left+right[::-1],fill=255)
    def at(t): return P[int(t*(len(P)-1))]
    limbs=[]
    for t,fwd in ((0.27,-1),(0.53,1)):
        x,y,_=at(t)
        for side in (-1,1):
            w=width(t,L,bulk); sx=x+side*w*0.8; ex=x+side*w*1.75; ey=y+fwd*w*0.35; fx=x+side*w*2.05; fy=y-fwd*w*0.25
            th=int(L*0.045*bulk); d.line([(sx,y),(ex,ey)],fill=255,width=th); d.line([(ex,ey),(fx,fy)],fill=255,width=int(th*0.8))
            for ex2,ey2 in ((ex,ey),(fx,fy)): d.ellipse([ex2-th*0.45,ey2-th*0.45,ex2+th*0.45,ey2+th*0.45],fill=255)
            for k in (-2,-1,0,1):
                a=math.atan2(fy-ey,fx-ex)+k*0.32; d.line([(fx,fy),(fx+math.cos(a)*th*1.3,fy+math.sin(a)*th*1.3)],fill=255,width=max(4,th//4))
            limbs.append((sx,y,ex,ey,fx,fy))
    col=ImageEnhance.Brightness(tex(*skin)).enhance(0.72); cd=ImageDraw.Draw(col,'RGBA')
    for i in range(30,len(P)-12,5):  # osteoderm rows following the spine
        x,y,t=P[i]; w=width(t,L,bulk); rows=4 if t<0.55 else 2
        for k in range(rows):
            off=(k-(rows-1)/2)*w*0.32; r=max(6,w*0.09)
            cd.ellipse([x+off-r,y-r*0.8,x+off+r,y+r*0.8],fill=(0,0,0,70),outline=(255,240,190,40),width=3)
    for _ in range(2500):  # fine scale noise
        x=rnd.uniform(0,S); y=rnd.uniform(0,S); r=rnd.uniform(3,7); cd.ellipse([x-r,y-r,x+r,y+r],fill=(0,0,0,rnd.randint(15,45)))
    hx,hy,_=at(0.145)
    for side in (-1,1):
        x,y,t=at(0.145); w=width(0.145,L,bulk)*0.55; ex=x+side*w; r=L*0.0095*bulk
        cd.ellipse([ex-r*1.5,y-r*1.5,ex+r*1.5,y+r*1.5],fill=(0,0,0,120)); cd.ellipse([ex-r,y-r,ex+r,y+r],fill=eye+(255,)); cd.ellipse([ex-r*0.25,y-r*0.9,ex+r*0.25,y+r*0.9],fill=(8,8,4,255))
        nx,ny,_=at(0.02); cd.ellipse([nx+side*L*0.006-r*0.4,ny+L*0.006-r*0.4,nx+side*L*0.006+r*0.4,ny+L*0.006+r*0.4],fill=(0,0,0,200))
    if thorns:
        for i in range(36,len(P)-20,9):
            x,y,t=P[i]; w=width(t,L,bulk)
            for side in (-1,1):
                bx=x+side*w*0.9; tip=(bx+side*w*0.55,y+w*0.15); poly=[(bx,y-w*0.12),tip,(bx,y+w*0.12)]
                d.polygon(poly,fill=255); cd.polygon(poly,fill=(58,44,28,255))
        vine=Image.new('L',(S,S),0); vd=ImageDraw.Draw(vine)
        for k in range(7):
            pts=[]; o=rnd.uniform(-0.6,0.6)
            for i in range(30,len(P)-30,8):
                x,y,t=P[i]; w=width(t,L,bulk); pts.append((x+o*w+rnd.uniform(-w*0.12,w*0.12),y))
            vd.line(pts,fill=150,width=7,joint='curve')
        vine=ImageChops.multiply(vine,m)
        col=Image.composite(Image.new('RGB',(S,S),glow),col,vine.filter(ImageFilter.GaussianBlur(3)))
    col=T.shade(col,m)
    edge=ImageChops.subtract(m,m.filter(ImageFilter.MinFilter(15))); col=Image.composite(Image.new('RGB',(S,S),(10,10,6)),col,edge.point(lambda v:v*0.6))
    return [im.rotate(angle,resample=Image.BICUBIC,center=(R,R)) for im in (m,col)]
def ripples(bg,seed,cx=R,cy=R):
    rnd=random.Random(seed); o=Image.new('L',(S,S),0); d=ImageDraw.Draw(o)
    for i in range(7):
        r=rnd.uniform(500,900); a=rnd.uniform(0,360); d.arc([cx-r,cy-r*0.9,cx+r,cy+r*0.9],a,a+rnd.uniform(40,110),fill=rnd.randint(60,120),width=10)
    return Image.composite(Image.new('RGB',(S,S),(170,190,170)),bg,o.filter(ImageFilter.GaussianBlur(6)).point(lambda v:v*0.5))
def croc_token(name,scale,skin,eye,accent,seed,**k):
    bg=ripples(T.water(seed),seed); m,col=croc(scale,skin,eye,seed,**k)
    sh=ImageChops.offset(m.filter(ImageFilter.GaussianBlur(45)),35,50).point(lambda v:v*0.75)
    bg=Image.composite(Image.new('RGB',(S,S),(0,0,0)),bg,sh)
    if k.get('glow'): bg=Image.composite(Image.new('RGB',(S,S),k['glow']),bg,m.filter(ImageFilter.GaussianBlur(110)).point(lambda v:v*0.45))
    bg.paste(col,(0,0),m); T.finish(T.ring(bg,accent),name)
if __name__=='__main__':
    BARK=('crocodile_throne_pool_labeled.png',(0,0,450,560)); ROOT=('the_rootmaw_labyrinth_labeled.png',(0,200,560,760))
    croc_token('juvenilecrocodile',0.66,BARK+((122,130,84),),(225,205,90),T.GREEN,11,bulk=0.85,wave=0.14)
    croc_token('huntingcrocodile',0.78,BARK+((104,112,72),),(235,190,60),T.TEAL,12,bulk=0.95,wave=0.12)
    croc_token('alphacrocodile',0.88,BARK+((92,94,64),),(240,175,40),T.AMBER,13,bulk=1.05,wave=0.10)
    croc_token('swamptyrant',0.95,BARK+((84,80,60),),(245,140,40),T.RED,14,bulk=1.2,wave=0.08,angle=-18)
    croc_token('thornheart',0.97,ROOT+((80,98,64),),(180,255,150),T.GOLD,15,bulk=1.2,wave=0.09,thorns=True,glow=(150,230,120),angle=-26)
