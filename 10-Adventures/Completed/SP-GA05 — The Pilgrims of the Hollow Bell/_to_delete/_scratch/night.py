import numpy as np, sys
from PIL import Image, ImageFilter
def night(src, dst, lights, preview=None):
    im=Image.open(src).convert('RGB'); W,H=im.size
    a=np.asarray(im).astype(np.float32)/255
    lum=a@np.array([0.299,0.587,0.114],dtype=np.float32)
    grey=np.repeat(lum[...,None],3,axis=2)
    desat=a*0.45+grey*0.55
    dark=desat*np.array([0.42,0.52,0.78],dtype=np.float32)*0.62            # cold moonless blue
    dark=np.clip(dark+0.015,0,1)
    L=np.zeros((H,W),np.float32); yy,xx=np.mgrid[0:H,0:W].astype(np.float32)
    for (fx,fy,fr,strength) in lights:
        cx,cy,r=fx*W,fy*H,fr*W
        d=np.sqrt((xx-cx)**2+(yy-cy)**2)/r
        L=np.maximum(L,np.clip(1-d,0,1)**1.6*strength)
    warm=np.clip(a*np.array([1.18,0.98,0.72],dtype=np.float32)*1.05,0,1)    # firelit colour
    out=dark*(1-L[...,None])+warm*L[...,None]
    Image.fromarray((np.clip(out,0,1)*255).astype(np.uint8)).save(dst)
    if preview:
        p=Image.open(dst); p.thumbnail((1400,1400)); p.save(preview,quality=85)
