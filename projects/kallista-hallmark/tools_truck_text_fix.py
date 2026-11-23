import cv2,numpy as np
im=cv2.imread('fr/001.png').astype(np.float32)
H,W=im.shape[:2]
L=im.mean(2); sat=im.max(2)-im.min(2)
# letter glyph boxes on line 2 (x0,x1); y range generous
box={'I':(340,345),'T':(350,374),'E':(379,398),'R':(405,427),'Y':(432,454)}
slope=(602-617)/(454-214)   # baseline rise per px
def bottom(x): return 617+slope*(x-214)
# background (door green) and letter color
bgL=np.median(L[620:640,330:460]); fgL=np.percentile(L[586:606,379:398],97)
fgC=np.array([np.percentile(im[586:606,379:398,c],97) for c in range(3)])
alpha=np.clip((L-bgL-8)/(fgL-bgL-8),0,1)
# --- clean plate: inpaint all line-2 letters from I to Y
m=np.zeros((H,W),np.uint8)
for x in range(337,458):
    yb=int(round(bottom(x)))+3
    col=(alpha[yb-24:yb,x]>0.08)
    m[yb-24:yb,x]=col*255
m=cv2.dilate(m,np.ones((3,3),np.uint8),1)
for x in range(337,458):
    m[:int(round(bottom(x)))-23,x]=0
clean=cv2.inpaint(im.astype(np.uint8),m,4,cv2.INPAINT_TELEA).astype(np.float32)
# restore door seam (dark vertical line near x~376) from just below the text
seam=[x for x in range(368,386) if L[625,x]<L[625,360]-12]
for x in seam:
    for y in range(560,622):
        if m[y,x]: clean[y,x]=im[626,x]*0.6+clean[y,x]*0.4
# glyph alpha stamps
def stamp(k):
    a,b=box[k]; yb=int(round(bottom((a+b)/2)))
    return alpha[yb-23:yb+3,a-1:b+2].copy(), a-1, yb-23
st={k:stamp(k) for k in 'ETRY'}
# synthesize N with the same stroke weight and blur as E/T
h=st['E'][0].shape[0]; sw=5
Nw=24; up=4
big=np.zeros((h*up,(Nw)*up),np.float32)
top=int(2*up); bot=int((h-3)*up)
cv2.rectangle(big,(1*up,top),(1*up+sw*up,bot),1,-1)
cv2.rectangle(big,((Nw-1-sw)*up,top),((Nw-1)*up,bot),1,-1)
pts=np.array([[1*up,top],[(1+sw+1)*up,top],[(Nw-1)*up,bot],[(Nw-1-sw-1)*up,bot]],np.int32)
cv2.fillConvexPoly(big,pts,1)
Nst=cv2.resize(big,(Nw,h),interpolation=cv2.INTER_AREA)
Nst=cv2.GaussianBlur(Nst,(3,3),0.8)
# match the E stamp's peak/softness
Nst=np.clip(Nst*st['E'][0].max(),0,1)
# layout ENTRY starting at x=340 with ~0.93 width scale
seq=[('E',st['E'][0]),('N',Nst),('T',st['T'][0]),('R',st['R'][0]),('Y',st['Y'][0])]
out=clean.copy(); x=339; gap=3
ov=np.zeros((H,W),np.float32)
for k,s in seq:
    w=max(4,int(round(s.shape[1]*0.93)))
    s2=cv2.resize(s,(w,s.shape[0]),interpolation=cv2.INTER_AREA)
    yb=int(round(bottom(x+w/2))); y0=yb-23
    ov[y0:y0+s2.shape[0],x:x+w]=np.maximum(ov[y0:y0+s2.shape[0],x:x+w],s2)
    x+=w+gap
print('line ends at',x,'(was 454)')
np.save('ov.npy',ov); np.save('fg.npy',fgC)
out=clean*(1-ov[...,None])+fgC*ov[...,None]
cv2.imwrite('fixed0.png',out.astype(np.uint8))
# keep clean-plate delta for other frames: patch = out - frame0 within region
np.save('patch_region.npy',np.array([330,560,480,630]))
d=(out-im); np.save('delta.npy',d[560:630,330:480])
a=im[540:640,180:500].astype(np.uint8);b=out[540:640,180:500].astype(np.uint8)
cv2.imwrite('fix_ab.png',cv2.resize(np.vstack([a,b]),None,fx=3,fy=3,interpolation=cv2.INTER_LANCZOS4))
