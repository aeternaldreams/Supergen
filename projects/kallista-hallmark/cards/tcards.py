import random
from PIL import Image,ImageDraw,ImageFont,ImageFilter
S='/tmp/claude-0/-home-user-Supergen/7f59304c-b564-5bd2-91b1-c7608be0a4bc/scratchpad/';F=S+'fonts/'
W,H=1280,720;cream=(250,244,232);gold=(226,192,118);K=1.3
def font(n,s,w=None):
    f=ImageFont.truetype(F+n,int(s*K))
    if w:
        try:f.set_variation_by_axes([w])
        except Exception:pass
    return f
def bg(seed):
    random.seed(seed);fr=Image.new('RGBA',(W,H),(14,32,28,255));bl=Image.new('RGBA',(W,H),(0,0,0,0));d=ImageDraw.Draw(bl)
    for _ in range(55):
        x,y,r,a=random.uniform(0,W),random.uniform(0,H),random.uniform(10,42),random.randint(18,55);d.ellipse((x-r,y-r,x+r,y+r),fill=(240,200,130,a))
    fr=Image.alpha_composite(fr,bl.filter(ImageFilter.GaussianBlur(7)))
    sn=Image.new('RGBA',(W,H),(0,0,0,0));d=ImageDraw.Draw(sn)
    for _ in range(200):
        x,y,r=random.uniform(0,W),random.uniform(0,H),random.uniform(1.2,4);d.ellipse((x-r,y-r,x+r,y+r),fill=(255,255,255,int(150*min(1,r/3.5))))
    fr=Image.alpha_composite(fr,sn)
    v=Image.new('RGBA',(W,H),(0,0,0,0));ImageDraw.Draw(v).ellipse((W*0.08,H*0.22,W*0.92,H*0.78),fill=(6,16,14,130))
    return Image.alpha_composite(fr,v.filter(ImageFilter.GaussianBlur(60)))
it=lambda s:font('PlayfairDisplay-Italic[wght].ttf',s,400)
pb=lambda s:font('Playball-Regular.ttf',s)
def card(lines,seed,name):
    im=bg(seed);d=ImageDraw.Draw(im);LH=int(78*K);n=len(lines)
    base0=H//2+int(20*K)-(n-1)*LH//2;maxw=0
    for li,parts in enumerate(lines):
        ws=[d.textlength(t,font=f) for t,f,c,dy in parts];x=(W-sum(ws))/2;maxw=max(maxw,sum(ws))
        for (t,f,c,dy),w in zip(parts,ws):
            d.text((x,base0+li*LH+dy),t,font=f,fill=c,anchor='ls');x+=w
    yr=base0+(n-1)*LH+int(42*K);d.line((W//2-70,yr,W//2+70,yr),fill=gold+(200,),width=2)
    print(name,'max line width %.0f%%'%(maxw/W*100));im.convert('RGB').save(name);return im
c=[card([[('This winter…',it(58),cream,0)]],1,'c1.png'),
   card([[('…',it(58),cream,0),('love',pb(80),gold,4),('  was in the',it(58),cream,0)],[("last place she'd look.",it(58),cream,0)]],2,'c2.png'),
   card([[('She came for a',it(58),cream,0)],[('quiet getaway…',it(58),cream,0)]],3,'c3.png'),
   card([[('…but she had her',it(58),cream,0)],[('reservations.',pb(84),gold,6)]],4,'c4.png')]
sheet=Image.new('RGB',(W*2+12,H*2+12),(0,0,0))
for i,im in enumerate(c): sheet.paste(im.convert('RGB'),((i%2)*(W+12),(i//2)*(H+12)))
sheet.resize((sheet.width//2,sheet.height//2),Image.LANCZOS).save('text_cards_concept_v2.png')
