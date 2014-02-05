import SimpleCV as s
import time
import time
img = s.Image("C:\Users\Abhas_2\Pictures\world_of_tanks_2-851x315.jpg")
iset=s.ImageSet()
total_time=50 # in steps
w=40
h=40
c=time.clock()
class Pixel(object):
    def __init__(self,(ori_x,ori_y),(start_x,start_y),arr):
        self.ori_x=ori_x+img.width/2
        self.ori_y=ori_y+img.height/2
        self.x=float(start_x)
        self.y=float(start_y)
        self.angle=s.math.atan2(-(self.ori_y-self.y),(self.ori_x-self.x))
        self.dist=distance((self.ori_x,self.ori_y),(self.x,self.y)) #float
        self.accln=2*self.dist/float((total_time**2))
        #print(self.dist*2/(self.accln*(total_time**2)))
        self.vel=self.accln*total_time
        self.arr=arr
    def step(self):
        if distance((self.x,self.y),(self.ori_x,self.ori_y))>self.vel:
            self.x+=self.vel*s.math.cos(self.angle)
            self.y-=self.vel*s.math.sin(self.angle)
        else:
            self.x=self.ori_x
            self.y=self.ori_y

##            if round(self.x)<w/2:
##                self.x=w/2
##            if round(self.y)<h/2:
##                self.y=h/2
##            if round(self.x)>img.width-w/2:
##                self.x=img.width-w/2
##            if round(self.y)>img.height-h/2:
##                self.y=img.height-h/2
        self.vel-=self.accln


def distance((x1,y1),(x2,y2)):
    import math
    return(math.sqrt((x2-x1)**2+(y2-y1)**2))

n1=img.getNumpy()
p_list=[]
from random import randint
for c1 in range(img.width/w):
    for c2 in range(img.height/h):
        p_list.append( Pixel( ((c1+0.5)*w,(c2+0.5)*h),(randint(w+1,img.width*2-w-1),randint(h+1,img.height*2-h-1)),n1[c1*w:(c1+1)*w,c2*h:(c2+1)*h] ) )
print("Done "+str(time.clock()-c))
c=time.clock()
        #print((c1+0.5)*w,(c2+0.5)*h)
print(len(p_list))
n1=img.scale(2).getNumpy()
for count in range(total_time+5):
    #del n1
    print(count)
    #i1=s.Image((img.width*2,img.height*2))
    n1[:,:]=[0,0,0]
    #del i1
    for p in p_list:
        p.step()
        #temp=n[round(p.x)-w/2:round(p.x)+w/2,round(p.y)-h/2:round(p.y)+h/2]
        n1[round(p.x)-w/2:round(p.x)+w/2,round(p.y)-h/2:round(p.y)+h/2]=p.arr
    img=s.Image(n1)
    #img=img.scale(0.5)
##    if count<70:
##        img=img.blur((70-count)/10+1)
    iset.append(img)
    #img.scale(2).show()
print(time.clock()-c)
iset.save(r"C:\Users\Abhas_2\Desktop\ani.gif",3.5/100)