import sys, subprocess, numpy as np
src, dst, t0, t1 = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
W,H=1024,576; X0,X1,Y0,Y1=290,470,215,315
def rgb2hsv(a):
    r,g,b=a[...,0],a[...,1],a[...,2]; mx=a.max(-1); mn=a.min(-1); d=mx-mn+1e-6
    h=np.where(mx==r,((g-b)/d)%6,np.where(mx==g,(b-r)/d+2,(r-g)/d+4))*60
    s=np.where(mx>0,(mx-mn)/(mx+1e-6),0); return h,s,mx
def hsv2rgb(h,s,v):
    c=v*s; x=c*(1-np.abs((h/60)%2-1)); m=v-c; z=np.zeros_like(h); k=(h//60).astype(int)%6
    r=np.select([k==0,k==1,k==2,k==3,k==4,k==5],[c,x,z,z,x,c]); g=np.select([k==0,k==1,k==2,k==3,k==4,k==5],[x,c,c,x,z,z]); b=np.select([k==0,k==1,k==2,k==3,k==4,k==5],[z,z,x,c,c,x])
    return np.stack([r+m,g+m,b+m],-1)
dec=subprocess.Popen(['ffmpeg','-v','error','-i',src,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
enc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r','24','-i','-','-c:v','libx264','-crf','14','-pix_fmt','yuv420p',dst],stdin=subprocess.PIPE)
n=0
# soft box window
yy,xx=np.mgrid[Y0:Y1,X0:X1]; win=np.clip(np.minimum.reduce([xx-X0,X1-xx,yy-Y0,Y1-yy])/15.0,0,1)
while True:
    buf=dec.stdout.read(W*H*3)
    if len(buf)<W*H*3: break
    f=np.frombuffer(buf,np.uint8).reshape(H,W,3).astype(np.float32)/255
    t=n/24
    if t0<=t<t1:
        p=f[Y0:Y1,X0:X1]; h,s,v=rgb2hsv(p)
        m=np.clip((0.57-v)/0.10,0,1)*np.clip((17.5-h)/4,0,1)*(h>=0)*np.clip((s-0.53)/0.06,0,1)*win
        s2=s*(1-0.18*m); h2=h+3*m; v2=np.clip(v*(1+0.16*m),0,1)
        f[Y0:Y1,X0:X1]=hsv2rgb(h2%360,s2,v2)
    enc.stdin.write((np.clip(f,0,1)*255).astype(np.uint8).tobytes()); n+=1
enc.stdin.close(); enc.wait(); print('frames',n)
