import pygame, sys
from pygame.locals import *
import base as fun
import time as t
from random import *
pygame.init()
surf= pygame.display.set_mode((600, 450))
pygame.display.set_caption('Hello World!')
c1=t.clock()
c=[]
size=500
r=[]
for count in range(size):
    r.append(None)
    r[count]=fun.tiltedRect((randint(0,600),randint(0,450)),(randint(0,600),randint(0,450)),randrange(0,360))
    r[count].rotate_step=random()-random()
    r[count].rotate_time=randrange(500)
    r[count].draw_pos=(randrange(600),randrange(450))

def calc_avg():
    sum=0
    for count in c:
        sum+=count
    avg=sum/len(c)
    return avg

for count in range(100): # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    surf.fill(pygame.Color("black"))
    c2=t.clock()
    c_diff=c2-c1
    c.append(c_diff)
    print(c_diff)
    c1=c2
    surf.lock()
    for count in range(size):
        r[count].rotate_time-=1
        if r[count].rotate_time<=0:
            r[count].rotate_step=random()-random()
            r[count].rotate_time=randrange(500)
        r[count].rotate_ip(r[count].rotate_step)
        r[count].draw(surf,r[count].draw_pos,centered=True)
    surf.unlock()
    pygame.display.flip()

