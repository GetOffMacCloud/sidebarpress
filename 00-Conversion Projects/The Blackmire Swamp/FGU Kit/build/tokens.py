"""Blackmire token art: round tokens with a bronze ring (matching the book's label frames),
a swamp-water ground sampled from the location art, and a top-down creature figure.
Story NPC tokens are circular crops of their portraits. Output: ../tokens/*.png (512 px)."""
import os,math,random
from PIL import Image,ImageDraw,ImageFilter,ImageChops,ImageEnhance
HERE=os.path.dirname(os.path.abspath(__file__)); SRC=os.path.normpath(os.path.join(HERE,'..','..'))
OUT=os.path.join(HERE,'..','tokens'); os.makedirs(OUT,exist_ok=True)
S=2048; R=S//2  # supersampled canvas
BRONZE=(184,150,86); BRONZE_D=(92,70,36); INK=(18,22,18)
def water(seed,src='crocodile_throne_pool_labeled.png',box=(260,620,860,1120),tint=(1.0,1.0,1.0)):
    im=Image.open(os.path.join(SRC,src)).convert('RGB').crop(box).resize((S,S),Image.LANCZOS)
    im=ImageEnhance.Brightness(im).enhance(0.75); r,g,b=im.split()
    im=Image.merge('RGB',[c.point(lambda v,k=k:min(255,int(v*k))) for c,k in zip((r,g,b),tint)])
    v=Image.new('L',(S,S),0); d=ImageDraw.Draw(v)
    for i in range(60): d.ellipse([i*14,i*14,S-i*14,S-i*14],fill=int(255*min(1,i/45)))
    return Image.composite(im,Image.new('RGB',(S,S),(8,12,10)),v.filter(ImageFilter.GaussianBlur(60)))
def ring(img,accent):
    g=Image.new('RGB',(S,S)); gd=ImageDraw.Draw(g)
    for y in range(S):
        k=0.55+0.45*math.cos((y/S)*math.pi*1.2-0.3)
        gd.line([(0,y),(S,y)],fill=tuple(int(c*k) for c in (176,138,72)))
    m=Image.new('L',(S,S),0); md=ImageDraw.Draw(m); md.ellipse([0,0,S-1,S-1],fill=255); md.ellipse([110,110,S-111,S-111],fill=0)
    img.paste(g,(0,0),m); d=ImageDraw.Draw(img)
    d.ellipse([4,4,S-5,S-5],outline=(40,30,14),width=14); d.ellipse([104,104,S-105,S-105],outline=(30,22,10),width=16)
    d.ellipse([40,40,S-41,S-41],outline=(222,196,130),width=5); d.ellipse([84,84,S-85,S-85],outline=(90,66,30),width=5)
    for a in range(0,360,30):
        x=R+(R-62)*math.cos(math.radians(a)); y=R+(R-62)*math.sin(math.radians(a)); r=15 if a%90==0 else 9
        d.ellipse([x-r,y-r,x+r,y+r],fill=accent if a%90==0 else (60,44,20))
    return img
def finish(img,name):
    m=Image.new('L',(S,S),0); ImageDraw.Draw(m).ellipse([0,0,S-1,S-1],fill=255)
    out=Image.new('RGBA',(S,S),(0,0,0,0)); out.paste(img,(0,0),m)
    out.resize((512,512),Image.LANCZOS).save(os.path.join(OUT,name+'.png'))
def shade(layer,mask,light=(-0.5,-0.7)):
    """emboss-style lighting so flat shapes read as painted forms"""
    e=mask.filter(ImageFilter.GaussianBlur(30)); hi=ImageChops.offset(e,int(light[0]*40),int(light[1]*40))
    hl=ImageChops.subtract(e,hi).point(lambda v:min(255,v*3)); sh=ImageChops.subtract(hi,e).point(lambda v:min(255,v*3))
    layer=Image.composite(Image.new('RGB',(S,S),(200,190,120)),layer,hl.point(lambda v:v*0.35))
    return Image.composite(Image.new('RGB',(S,S),(0,0,0)),layer,sh.point(lambda v:v*0.6))
def croc(scale,body,belly,eye,seed,thorns=False,glow=None,angle=-35):
    rnd=random.Random(seed); m=Image.new('L',(S,S),0); d=ImageDraw.Draw(m); L=S*0.80*scale; W=L*0.17
    pts=[]  # outline along spine: snout (top) -> tail (bottom)
    def width(t):
        if t<0.10: return W*(0.28+t*3.2)
        if t<0.17: return W*0.62
        if t<0.50: return W*(0.85+0.15*math.sin((t-0.17)/0.33*math.pi))
        return W*0.85*(1-(t-0.5)/0.5)**1.25+4
    N=120; ys=[R-L/2+L*i/N for i in range(N+1)]
    left=[(R-width(i/N)*(1+0.03*math.sin(i)),ys[i]) for i in range(N+1)]; right=[(R+width(i/N),ys[i]) for i in range(N+1)]
    d.polygon(left+right[::-1],fill=255)
    for side in (-1,1):  # legs
        for t,dirn in ((0.23,-1),(0.47,1)):
            y=R-L/2+L*t; x=R+side*W*0.8
            d.line([(x,y),(x+side*W*0.9,y+dirn*W*0.5),(x+side*W*1.15,y+dirn*W*0.25)],fill=255,width=int(W*0.32),joint='curve')
            for k in (-1,0,1): d.line([(x+side*W*1.15,y+dirn*W*0.25),(x+side*W*1.4,y+dirn*W*0.25+k*W*0.18)],fill=255,width=int(W*0.08))
    col=Image.new('RGB',(S,S),body); cd=ImageDraw.Draw(col)
    for i in range(14,N-8,3):  # dorsal scutes
        t=i/N; w=width(t)*0.55; y=ys[i]
        for k in (-1,-0.35,0.35,1):
            if t>0.55 and abs(k)>0.5: continue
            cx=R+k*w*0.6; cd.rounded_rectangle([cx-w*0.16,y-L*0.009,cx+w*0.16,y+L*0.009],radius=8,fill=tuple(int(c*0.6) for c in body),outline=belly,width=3)
    cd.line([(R,ys[0]+L*0.02),(R,ys[int(N*0.12)])],fill=tuple(int(c*0.7) for c in body),width=6)
    for side in (-1,1):  # eyes
        ex=R+side*W*0.42; ey=R-L/2+L*0.135; r=W*0.11
        cd.ellipse([ex-r,ey-r,ex+r,ey+r],fill=eye); cd.ellipse([ex-r*0.25,ey-r*0.85,ex+r*0.25,ey+r*0.85],fill=(10,10,5))
    if thorns:
        for i in range(12,N-10,7):
            for side in (-1,1):
                x=R+side*width(i/N); y=ys[i]; cd.polygon([(x,y-12),(x+side*W*0.35,y+W*0.05),(x,y+12)],fill=(70,52,30))
                d.polygon([(x,y-12),(x+side*W*0.35,y+W*0.05),(x,y+12)],fill=255)
        for i in range(6):  # glowing vine lines
            p=[(R+rnd.uniform(-W*0.6,W*0.6),ys[0]+L*0.15)]
            for j in range(9): p.append((p[-1][0]+rnd.uniform(-W*0.25,W*0.25),p[-1][1]+L*0.07))
            cd.line(p,fill=glow,width=10,joint='curve')
    col=shade(col,m)
    sh=m.filter(ImageFilter.GaussianBlur(40)).point(lambda v:v*0.7)
    m,col,sh=[x.rotate(angle,resample=Image.BICUBIC,center=(R,R)) for x in (m,col,sh)]
    return m,col,ImageChops.offset(sh,30,40)
def creature_token(name,scale,body,belly,eye,accent,seed,**k):
    bg=water(seed); m,col,sh=croc(scale,body,belly,eye,seed,**k)
    bg=Image.composite(Image.new('RGB',(S,S),(0,0,0)),bg,sh)
    if k.get('glow'):
        g=m.filter(ImageFilter.GaussianBlur(90)); bg=Image.composite(Image.new('RGB',(S,S),k['glow']),bg,g.point(lambda v:v*0.55))
    bg.paste(col,(0,0),m); finish(ring(bg,accent),name)
def figure_token(name,kind,accent,seed):
    if kind=='sentry':
        bg=water(seed,'the_sunken_war_church_labeled.png',(200,800,800,1300),(0.85,0.95,1.15)); m=Image.new('L',(S,S),0); d=ImageDraw.Draw(m)
        d.ellipse([R-430,R-170,R+430,R+260],fill=255)              # shoulders/pauldrons
        d.ellipse([R-230,R-260,R+230,R+200],fill=255)              # helm
        d.line([(R-700,R+520),(R+700,R-560)],fill=255,width=70)     # spear shaft
        d.polygon([(R+640,R-520),(R+800,R-720),(R+720,R-470)],fill=255)
        col=Image.new('RGB',(S,S),(78,92,96)); cd=ImageDraw.Draw(col)
        cd.ellipse([R-230,R-260,R+230,R+200],fill=(96,108,110)); cd.line([(R,R-260),(R,R+200)],fill=(58,66,64),width=40)
        cd.line([(R-700,R+520),(R+700,R-560)],fill=(92,70,46),width=70); cd.polygon([(R+640,R-520),(R+800,R-720),(R+720,R-470)],fill=(120,96,70))
        rnd=random.Random(seed)
        for i in range(40): x=rnd.uniform(R-420,R+420); y=rnd.uniform(R-150,R+250); cd.ellipse([x-18,y-18,x+18,y+18],fill=(110,84,52))  # rust
        for i in range(10): x=rnd.uniform(R-380,R+380); cd.line([(x,R+150),(x+rnd.uniform(-40,40),R+420)],fill=(52,70,52),width=12)   # weed
        col=shade(col,m); bg.paste(col,(0,0),m)
        g=Image.new('L',(S,S),0); ImageDraw.Draw(g).ellipse([R-120,R-90,R-40,R-30],fill=255); ImageDraw.Draw(g).ellipse([R+40,R-90,R+120,R-30],fill=255)
        bg=Image.composite(Image.new('RGB',(S,S),(150,220,230)),bg,g.filter(ImageFilter.GaussianBlur(10)))
    elif kind=='sentinel':
        bg=water(seed,'the_rootmaw_labyrinth_labeled.png',(250,500,850,1000)); m=Image.new('L',(S,S),0); d=ImageDraw.Draw(m)
        col=Image.new('RGB',(S,S),(74,58,38)); cd=ImageDraw.Draw(col); rnd=random.Random(seed)
        for a in range(0,360,24):  # roots radiating and curling
            p=[(R,R)]; ang=math.radians(a+rnd.uniform(-8,8))
            for j in range(9): ang+=rnd.uniform(-0.25,0.35); rr=(j+1)*85; p.append((R+rr*math.cos(ang),R+rr*math.sin(ang)))
            w=int(rnd.uniform(60,95)); d.line(p,fill=255,width=w,joint='curve'); cd.line(p,fill=(84+rnd.randint(-10,10),64,40),width=w,joint='curve')
            cd.line(p,fill=(52,40,26),width=max(6,w//6),joint='curve')
        d.ellipse([R-330,R-330,R+330,R+330],fill=255); cd.ellipse([R-330,R-330,R+330,R+330],fill=(70,54,34))
        for i in range(5): cd.arc([R-300+i*55,R-300+i*55,R+300-i*55,R+300-i*55],rnd.randint(0,180),rnd.randint(200,360),fill=(44,34,22),width=14)
        for x,y in ((R-110,R-60),(R+110,R-60)): cd.ellipse([x-38,y-26,x+38,y+26],fill=(170,210,90))
        col=shade(col,m); bg.paste(col,(0,0),m)
    else:  # spirit
        bg=water(seed,'the_sunken_druid_grove_labeled.png',(250,600,850,1100),(0.8,1.05,1.0)); rnd=random.Random(seed)
        g=Image.new('L',(S,S),0); d=ImageDraw.Draw(g)
        for i in range(26):
            a=rnd.uniform(0,2*math.pi); r0=rnd.uniform(80,600)
            d.arc([R-r0,R-r0,R+r0,R+r0],math.degrees(a),math.degrees(a)+rnd.uniform(60,160),fill=rnd.randint(90,200),width=rnd.randint(20,60))
        d.ellipse([R-260,R-330,R+260,R+260],fill=170)
        g=g.filter(ImageFilter.GaussianBlur(28))
        bg=Image.composite(Image.new('RGB',(S,S),(170,235,200)),bg,g)
        h=ImageDraw.Draw(bg)
        for x in (R-110,R+110): h.ellipse([x-55,R-120,x+55,R-20],fill=(12,30,24))
        h.ellipse([R-70,R+60,R+70,R+190],fill=(12,30,24))
    finish(ring(bg,accent),name)
def portrait_token(name,src,accent,box):
    im=Image.open(os.path.join(SRC,src)).convert('RGB'); x0,y0,x1,y1=box
    bg=im.crop((x0,y0,x1,y1)).resize((S,S),Image.LANCZOS); finish(ring(bg,accent),name)

GOLD=(214,182,92); GREEN=(110,190,110); TEAL=(80,170,170); AMBER=(220,150,60); RED=(170,60,50)
if __name__=='__main__':
    for key,src in (('oldmarrowfinch','Old_Marrow_Finch.png'),('sistervell','Sister_Vell.png'),('captainrusk','Captain_Rusk_Ironstake.png'),('silt','Silt.png'),('astervale','Aster_Vale.png')):
        portrait_token(key,src,GOLD,(193,120,893,820))
    print(sorted(os.listdir(OUT)))
    