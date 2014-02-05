import SimpleCV as s
import time
import time
img = s.Image("C:\Users\Abhas_2\Pictures\world_of_tanks_2-851x315.jpg")
iset=s.ImageSet()
total_time=100 # in steps
w=40
h=40
c=time.clock()
class Pixel(object):
    def __init__(self,(ori_x,ori_y),(start_x,start_y),arr):
        self.ori_x=ori_x
        self.ori_y=ori_y
        self.x=float(start_x)
        self.y=float(start_y)
        self.angle=s.math.atan2(-(ori_y-start_y),(ori_x-start_x))
        self.dist=distance((ori_x,ori_y),(start_x,start_y)) #float
        self.accln=2*self.dist/float((total_time**2))
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
        p_list.append( Pixel( ((c1+0.5)*w,(c2+0.5)*h),(randint(w/2,img.width-w/2),randint(h/2,img.height-h/2)),n1[c1*w:(c1+1)*w,c2*h:(c2+1)*h] ) )
print("Done "+str(time.clock()-c))
c=time.clock()
        #print((c1+0.5)*w,(c2+0.5)*h)
print(len(p_list))
for count in range(total_time+5):
    #del n
    i1=s.Image((img.width,img.height))
    n=i1.getNumpy()
    for p in p_list:
        p.step()
        #temp=n[round(p.x)-w/2:round(p.x)+w/2,round(p.y)-h/2:round(p.y)+h/2]
        n[round(p.x)-w/2:round(p.x)+w/2,round(p.y)-h/2:round(p.y)+h/2]=p.arr
    img=s.Image(n)
    iset.append(img)
    print(count)
    #img.scale(2).show()
print(time.clock()-c)
iset.save(r"C:\Users\Abhas_2\Desktop\ani.gif",3.5/100)