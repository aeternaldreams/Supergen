import numpy as np, subprocess, random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
S='/tmp/claude-0/-home-user-Supergen/7f59304c-b564-5bd2-91b1-c7608be0a4bc/scratchpad/'
F=S+'fonts/'; OUT=S+'finale/'
W,H,FPS=1280,720,24
cream=(250,244,232); gold=(226,192,118)
def font(n,s,w=None):
    f=ImageFont.truetype(F+n,s)
    if w:
        try: f.set_variation_by_axes([w])
        except Exception: pass
    return f
def ease(t): t=min(max(t,0),1); return 1-(1-t)**3
def ramp(t,a,b): return min(max((t-a)/(b-a),0),1)
random.seed(5)
flakes=[[random.uniform(0,W),random.uniform(-H,H),random.uniform(1.2,4.2),random.uniform(30,90),random.uniform(0,6.28)] for _ in range(260)]
def snow(img,t):
    d=ImageDraw.Draw(img)
    for x,y,r,v,ph in flakes:
        yy=(y+v*t*1.0)%(H+40)-20; xx=x+12*np.sin(t*0.8+ph)
        a=int(150*min(1,r/3.5)); d.ellipse((xx-r,yy-r,xx+r,yy+r),fill=(255,255,255,a))
def enc(name,frames):
    p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-c:v','libx264','-crf','16','-pix_fmt','yuv420p',OUT+name],stdin=subprocess.PIPE)
    for fr in frames: p.stdin.write(fr.tobytes())
    p.stdin.close(); p.wait()

def title():
    D=4.6; n=int(D*FPS)
    bg=Image.open(S+'finale/bnb_night.jpg').convert('RGB').resize((int(W*1.08),int(H*1.08)))
    a=np.asarray(bg.filter(ImageFilter.GaussianBlur(3)),float)/255; h,w=a.shape[:2]
    yy=np.arange(h)[:,None]/h; xx=np.arange(w)[None,:]/w
    band=np.exp(-((yy-0.45)/0.22)**2)*np.exp(-((xx-0.5)/0.45)**2); a=a*(1-0.62*band[...,None])*0.85
    bg=Image.fromarray((a.clip(0,1)*255).astype('uint8'))
    def layer(draw_fn):
        t=Image.new('RGBA',(W,H),(0,0,0,0)); td=ImageDraw.Draw(t); sh=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(sh)
        draw_fn(td,sd); return Image.alpha_composite(sh.filter(ImageFilter.GaussianBlur(6)),t)
    def ct(td,sd,y,txt,f,fill,sp=0):
        ww=sum(td.textlength(c,font=f)+sp for c in txt)-sp; x=(W-ww)/2
        for c in txt: sd.text((x+2,y+3),c,font=f,fill=(0,0,0,220)); td.text((x,y),c,font=f,fill=fill); x+=td.textlength(c,font=f)+sp
    L1=layer(lambda td,sd: ct(td,sd,160,"Holiday",font('Playball-Regular.ttf',114),gold+(255,)))
    L2=layer(lambda td,sd: ct(td,sd,300,"RESERVATIONS",font('Cinzel[wght].ttf',82,600),cream+(255,),sp=9))
    def l3(td,sd):
        td.line((W/2-115,418,W/2+115,418),fill=gold+(255,),width=2)
        ct(td,sd,436,"Some reservations are meant to be cancelled.",font('PlayfairDisplay-Italic[wght].ttf',34,500),cream+(255,))
    L3=layer(l3)
    a1=np.asarray(L1,float)/255
    frames=[]
    for i in range(n):
        t=i/FPS; s=1.08-0.06*ease(t/D)
        cw,chh=int(W*s),int(H*s); ox=(bg.width-cw)//2; oy=(bg.height-chh)//2
        fr=bg.crop((ox,oy,ox+cw,oy+chh)).resize((W,H)).convert('RGBA')
        sl=Image.new('RGBA',(W,H),(0,0,0,0)); snow(sl,t); fr=Image.alpha_composite(fr,sl)
        for L,a0,b0 in [(L1,0.35,1.1),(L2,0.75,1.5),(L3,1.6,2.4)]:
            k=ease(ramp(t,a0,b0))
            if k>0:
                l=L.copy(); al=np.asarray(l)[...,3].astype(float)*k; l.putalpha(Image.fromarray(al.astype('uint8'))); fr=Image.alpha_composite(fr,l)
        # glint sweep across Holiday
        g=ramp(t,1.3,2.3)
        if 0<g<1:
            cx=W*(0.32+0.38*g); xs=np.arange(W)[None,:]; band=np.exp(-((xs-cx)/28.0)**2)
            gl=(a1[...,3]*band*0.8)[...,None]*np.array([1,0.97,0.85])
            arr=np.asarray(fr,float)/255; arr[...,:3]=np.clip(arr[...,:3]+gl,0,1); fr=Image.fromarray((arr*255).astype('uint8'))
        fade=1-ease(ramp(t,D-0.45,D))
        arr=np.asarray(fr.convert('RGB'),float)*fade
        frames.append(arr.astype('uint8'))
    enc('title_card.mp4',frames)

def tunein():
    D=4.6; n=int(D*FPS)
    random.seed(3); boks=[(random.uniform(0,W),random.uniform(0,H),random.uniform(10,42),random.randint(20,60),random.uniform(-8,8)) for _ in range(60)]
    card=Image.open(OUT+'card_layer.png'); card=card.resize((int(card.width*W/1920),int(card.height*W/1920)),Image.LANCZOS).rotate(-2,expand=True,resample=Image.BICUBIC)
    stamp=Image.open(OUT+'stamp_layer.png'); stamp=stamp.resize((int(stamp.width*W/1920*0.78),int(stamp.height*W/1920*0.78)),Image.LANCZOS)
    cx0,cy0=(W-card.width)//2,(H-card.height)//2
    sx,sy=cx0+card.width-stamp.width-int(30*W/1920),cy0+int(30*W/1920)
    frames=[]; HIT=1.6
    for i in range(n):
        t=i/FPS
        fr=Image.new('RGBA',(W,H),(14,32,28,255)); bl=Image.new('RGBA',(W,H),(0,0,0,0)); bd=ImageDraw.Draw(bl)
        for x,y,r,al,dx in boks:
            xx=x+dx*t; bd.ellipse((xx-r,y-r,xx+r,y+r),fill=(240,200,130,al))
        fr=Image.alpha_composite(fr,bl.filter(ImageFilter.GaussianBlur(7)))
        sl=Image.new('RGBA',(W,H),(0,0,0,0)); snow(sl,t); fr=Image.alpha_composite(fr,sl)
        k=ease(ramp(t,0.0,0.8)); yoff=int((1-k)*260)
        shd=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(shd).rectangle((cx0+14,cy0+20+yoff,cx0+card.width,cy0+card.height+14+yoff),fill=(0,0,0,int(160*k)))
        fr=Image.alpha_composite(fr,shd.filter(ImageFilter.GaussianBlur(18)))
        c=card.copy(); c.putalpha(Image.fromarray((np.asarray(c)[...,3]*k).astype('uint8'))); fr.alpha_composite(c,(cx0,cy0+yoff))
        if t>=HIT-0.12:
            q=ramp(t,HIT-0.12,HIT); sc=1.0+0.7*(1-q)
            st=stamp.resize((int(stamp.width*sc),int(stamp.height*sc)),Image.BICUBIC)
            st.putalpha(Image.fromarray((np.asarray(st)[...,3]*min(1,q*1.3)).astype('uint8')))
            fr.alpha_composite(st,(sx-(st.width-stamp.width)//2,sy-(st.height-stamp.height)//2))
        # shake
        if HIT<=t<HIT+0.18:
            amp=8*(1-(t-HIT)/0.18); ox,oy=int(amp*np.sin(t*90)),int(amp*np.cos(t*77))
            fr=Image.fromarray(np.roll(np.roll(np.asarray(fr),ox,1),oy,0))
        fade=1-ease(ramp(t,D-0.45,D)); fin=ease(ramp(t,0,0.25))
        frames.append((np.asarray(fr.convert('RGB'),float)*fade*fin).astype('uint8'))
    enc('tunein_card.mp4',frames)
tunein(); print('ok')
