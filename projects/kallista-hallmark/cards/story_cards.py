# Animated story-card pairs, 1024x576 to match the footage. Same world as the tune-in card.
import random,subprocess,numpy as np
from PIL import Image,ImageDraw,ImageFont,ImageFilter
S='/tmp/claude-0/-home-user-Supergen/7f59304c-b564-5bd2-91b1-c7608be0a4bc/scratchpad/';F=S+'fonts/'
W,H,FPS=1024,576,24; k=W/1280; K=1.3*k
cream=(250,244,232); gold=(226,192,118)
def font(n,s,w=None):
    f=ImageFont.truetype(F+n,int(s*K))
    if w:
        try:f.set_variation_by_axes([w])
        except Exception:pass
    return f
it=lambda s:font('PlayfairDisplay-Italic[wght].ttf',s,400); pb=lambda s:font('Playball-Regular.ttf',s)
def ease(t): t=min(max(t,0),1); return 1-(1-t)**3
def ramp(t,a,b): return min(max((t-a)/(b-a),0),1)
def background(seed):
    random.seed(seed); fr=Image.new('RGBA',(W,H),(14,32,28,255)); bl=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(bl)
    for _ in range(55):
        x,y,r,a=random.uniform(0,W),random.uniform(0,H),random.uniform(8,34),random.randint(18,55); d.ellipse((x-r,y-r,x+r,y+r),fill=(240,200,130,a))
    fr=Image.alpha_composite(fr,bl.filter(ImageFilter.GaussianBlur(6)))
    v=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(v).ellipse((W*0.08,H*0.22,W*0.92,H*0.78),fill=(6,16,14,130))
    return Image.alpha_composite(fr,v.filter(ImageFilter.GaussianBlur(48)))
random.seed(9); flakes=[[random.uniform(0,W),random.uniform(-H,H),random.uniform(1,3.4),random.uniform(25,70),random.uniform(0,6.28)] for _ in range(200)]
def snow(img,t):
    d=ImageDraw.Draw(img)
    for x,y,r,v,ph in flakes:
        yy=(y+v*t)%(H+40)-20; xx=x+10*np.sin(t*0.8+ph); d.ellipse((xx-r,yy-r,xx+r,yy+r),fill=(255,255,255,int(150*min(1,r/3))))
def text_layer(lines,gold_alpha):
    """lines: list of lists of (text,font,is_gold,dy). Returns cream layer and gold layer."""
    c=Image.new('RGBA',(W,H),(0,0,0,0)); g=Image.new('RGBA',(W,H),(0,0,0,0)); dc,dg=ImageDraw.Draw(c),ImageDraw.Draw(g)
    LH=int(78*K); n=len(lines); base0=H//2+int(20*K)-(n-1)*LH//2
    for li,parts in enumerate(lines):
        ws=[dc.textlength(t,font=f) for t,f,isg,dy in parts]; x=(W-sum(ws))/2
        for (t,f,isg,dy),w in zip(parts,ws):
            (dg if isg else dc).text((x,base0+li*LH+dy),t,font=f,fill=(gold if isg else cream)+(255,),anchor='ls'); x+=w
    yr=base0+(n-1)*LH+int(42*K); dc.line((W//2-int(70*k),yr,W//2+int(70*k),yr),fill=gold+(200,),width=2)
    return c,g
def alpha(img,a):
    im=img.copy(); im.putalpha(Image.fromarray((np.asarray(img)[...,3]*a).astype('uint8'))); return im
def pair(name,cardA,cardB,seed,D=4.6,split=2.25):
    bg=background(seed); A=text_layer(cardA,1); B=text_layer(cardB,1); frames=[]
    for i in range(int(D*FPS)):
        t=i/FPS; fr=bg.copy(); sl=Image.new('RGBA',(W,H),(0,0,0,0)); snow(sl,t); fr=Image.alpha_composite(fr,sl)
        for (c,g),t0,t1 in ((A,0,split),(B,split,D)):
            if not (t0<=t<t1): continue
            lt=t-t0; dur=t1-t0
            a=ease(ramp(lt,0.05,0.45))*(1-ease(ramp(lt,dur-0.35,dur-0.02)))
            ag=ease(ramp(lt,0.35,0.8))*(1-ease(ramp(lt,dur-0.35,dur-0.02)))
            dx=int(3*lt)  # 3 px/s drift, like the name cards
            for L,aa in ((c,a),(g,ag)):
                if aa>0: fr.alpha_composite(alpha(L,aa).transform((W,H),Image.AFFINE,(1,0,-dx,0,1,0)))
        fade=ease(ramp(t,0,0.2))*(1-ease(ramp(t,D-0.2,D)))
        frames.append((np.asarray(fr.convert('RGB'),float)*fade).astype('uint8'))
    p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-shortest','-c:v','libx264','-crf','14','-pix_fmt','yuv420p','-profile:v','high','-c:a','aac',S+'tcards/out/'+name],stdin=subprocess.PIPE)
    for f in frames: p.stdin.write(f.tobytes())
    p.stdin.close(); p.wait()
pair('card_pair1_this_winter.mp4',
     [[('This winter…',it(58),False,0)]],
     [[('…',it(58),False,0),('love',pb(80),True,4),('  was in the',it(58),False,0)],[("last place she'd look.",it(58),False,0)]],1)
pair('card_pair2_reservations.mp4',
     [[('She came for a',it(58),False,0)],[('quiet getaway…',it(58),False,0)]],
     [[('…but she had her',it(58),False,0)],[('reservations.',pb(84),True,6)]],3)
print('ok')
