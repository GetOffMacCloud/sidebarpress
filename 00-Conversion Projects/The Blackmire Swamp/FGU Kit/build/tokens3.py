"""Painterly pass for the non-crocodile Blackmire creatures (sentry, sentinel, spirit)."""
import math,random,os
from PIL import Image,ImageDraw,ImageFilter,ImageChops,ImageEnhance
import tokens as T, tokens2 as T2
S,R=T.S,T.R
def taper(d,pts,w0,w1,fill=255):
    n=len(pts)-1
    for i in range(n):
        (x0,y0),(x1,y1)=pts[i],pts[i+1]
        K=max(12,int(math.hypot(x1-x0,y1-y0)/6))
        for k in range(K):
            f=(i+k/K)/n; x=x0+(x1-x0)*k/K; y=y0+(y1-y0)*k/K; w=(w0+(w1-w0)*f)/2
            d.ellipse([x-w,y-w,x+w,y+w],fill=fill)
def paint(bg,m,col,glow=None):
    sh=ImageChops.offset(m.filter(ImageFilter.GaussianBlur(45)),35,50).point(lambda v:v*0.7)
    bg=Image.composite(Image.new('RGB',(S,S),(0,0,0)),bg,sh)
    if glow: bg=Image.composite(Image.new('RGB',(S,S),glow),bg,m.filter(ImageFilter.GaussianBlur(100)).point(lambda v:v*0.4))
    col=T.shade(col,m); edge=ImageChops.subtract(m,m.filter(ImageFilter.MinFilter(13)))
    col=Image.composite(Image.new('RGB',(S,S),(8,8,6)),col,edge.point(lambda v:v*0.6)); bg.paste(col,(0,0),m); return bg
def sentinel(seed=21):
    rnd=random.Random(seed); bg=T2.ripples(T.water(seed,'the_rootmaw_labyrinth_labeled.png',(250,500,850,1000)),seed)
    m=Image.new('L',(S,S),0); d=ImageDraw.Draw(m)
    for a in range(0,360,30):
        ang=math.radians(a+rnd.uniform(-10,10)); p=[(R,R)]; L=rnd.uniform(620,860)
        for j in range(1,10):
            ang+=rnd.uniform(-0.28,0.28); rr=L*j/9; p.append((R+rr*math.cos(ang),R+rr*math.sin(ang)))
        taper(d,p,rnd.uniform(150,200),14)
        if rnd.random()<0.7:  # side rootlet
            k=rnd.randint(3,6); b=p[k]; a2=ang+rnd.choice((-1,1))*0.9; q=[b]+[(b[0]+t*45*math.cos(a2+t*0.1),b[1]+t*45*math.sin(a2+t*0.1)) for t in range(1,7)]
            taper(d,q,60,8)
    d.ellipse([R-300,R-300,R+300,R+300],fill=255)
    col=ImageEnhance.Brightness(T2.tex('the_rooted_archive_labeled.png',(0,600,500,1100),(120,92,58))).enhance(0.8); cd=ImageDraw.Draw(col,'RGBA')
    for i in range(6): r=280-i*45; cd.arc([R-r,R-r,R+r,R+r],rnd.randint(0,360),rnd.randint(0,360),fill=(30,22,12,170),width=16)
    for x,y in ((R-95,R-40),(R+95,R-40)):
        cd.ellipse([x-30,y-14,x+30,y+14],fill=(190,220,90,255))
    return paint(bg,m,col)
def sentry(seed=22):
    rnd=random.Random(seed); bg=T2.ripples(T.water(seed,'the_sunken_war_church_labeled.png',(150,650,750,1150),(0.8,0.9,1.1)),seed)
    m=Image.new('L',(S,S),0); d=ImageDraw.Draw(m)
    d.ellipse([R-470,R-180,R+470,R+300],fill=255)            # shoulders
    for s in (-1,1): d.ellipse([R+s*300-230,R-200,R+s*300+230,R+180],fill=255)  # pauldrons
    taper(d,[(R-720,R+560),(R+640,R-600)],70,56)             # spear
    d.polygon([(R+600,R-560),(R+840,R-800),(R+690,R-500)],fill=255)
    d.ellipse([R-220,R-250,R+220,R+190],fill=255)           # helm
    col=ImageEnhance.Brightness(T2.tex('fort_drowned_spear_labeled.png',(500,250,1000,750),(96,112,120))).enhance(0.55); cd=ImageDraw.Draw(col,'RGBA')
    for s in (-1,1):
        for k in range(4): r=210-k*40; cd.arc([R+s*300-r,R-10-r*0.85,R+s*300+r,R-10+r*0.85],200 if s<0 else -20,340 if s<0 else 160,fill=(20,24,24,180),width=12)
    shaft=Image.new('L',(S,S),0); taper(ImageDraw.Draw(shaft),[(R-720,R+560),(R+640,R-600)],70,56)
    col=Image.composite(Image.new('RGB',(S,S),(78,56,34)),col,shaft)
    cd=ImageDraw.Draw(col,'RGBA')
    cd.polygon([(R+600,R-560),(R+840,R-800),(R+690,R-500)],fill=(96,86,74,255))
    cd.ellipse([R-220,R-250,R+220,R+190],outline=(30,34,34,255),width=14); cd.line([(R,R-250),(R,R+190)],fill=(40,46,46,230),width=34)
    for i in range(160): x=rnd.uniform(R-460,R+460); y=rnd.uniform(R-220,R+300); r=rnd.uniform(8,28); cd.ellipse([x-r,y-r,x+r,y+r],fill=(120,74,34,rnd.randint(40,100)))
    for i in range(14):
        x=rnd.uniform(R-420,R+420); y=rnd.uniform(R+60,R+240); cd.line([(x,y),(x+rnd.uniform(-60,60),y+rnd.uniform(160,320))],fill=(50,74,46,220),width=rnd.randint(8,16))
    out=paint(bg,m,col)
    g=Image.new('L',(S,S),0); gd=ImageDraw.Draw(g)
    for x in (R-95,R+95): gd.ellipse([x-45,R-95,x+45,R-55],fill=255)
    return Image.composite(Image.new('RGB',(S,S),(160,230,235)),out,g.filter(ImageFilter.GaussianBlur(14)))
def spirit(seed=23):
    rnd=random.Random(seed); bg=T.water(seed,'the_sunken_druid_grove_labeled.png',(250,600,850,1100),(0.8,1.0,0.95))
    g=Image.new('L',(S,S),0); d=ImageDraw.Draw(g)
    d.ellipse([R-170,R-520,R+170,R-160],fill=200)                       # head
    d.polygon([(R-430,R-120),(R+430,R-120),(R+260,R+420),(R-260,R+420)],fill=150)  # shoulders/robe
    d.ellipse([R-430,R-260,R+430,R+20],fill=170)
    for i in range(14):  # trailing wisps
        x=R+rnd.uniform(-260,260); p=[(x,R+300)]
        for j in range(6): p.append((p[-1][0]+rnd.uniform(-90,90),p[-1][1]+rnd.uniform(70,120)))
        taper(d,p,rnd.uniform(70,130),6,fill=rnd.randint(90,150))
    for i in range(10):
        r=rnd.uniform(350,800); a=rnd.uniform(0,360); d.arc([R-r,R-r,R+r,R+r],a,a+rnd.uniform(40,120),fill=rnd.randint(40,90),width=rnd.randint(14,40))
    g=g.filter(ImageFilter.GaussianBlur(30))
    out=Image.composite(Image.new('RGB',(S,S),(175,240,210)),bg,g.point(lambda v:int(v*0.8)))
    h=Image.new('L',(S,S),0); hd=ImageDraw.Draw(h)
    for x in (R-70,R+70): hd.ellipse([x-38,R-360,x+38,R-320],fill=150)
    return Image.composite(Image.new('RGB',(S,S),(14,40,32)),out,h.filter(ImageFilter.GaussianBlur(10)))
if __name__=='__main__':
    T.finish(T.ring(sentinel(),T.GREEN),'rootboundsentinel')
    T.finish(T.ring(sentry(),T.TEAL),'drownedsentry')
    T.finish(T.ring(spirit(),(160,230,200)),'mireechospirit')
