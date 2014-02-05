# all imports
import math;
import pygame;
from pygame.locals import *

# init
pygame.init()

# setting display
surf=pygame.display.set_mode((400,400))
pygame.display.set_caption("Wtf is this??")

class part():
    list=[];
    def __init__(self,x,y,sprite_filename,life):
        self.x=x;
        self.y=y;
        self.xprevious=x;
        self.yprevious=y;
        self.life=life;
        self.sprite=pygame.image.load(sprite_filename).convert();
        part.list.append(self);

    def draw_self(self):
        surf.blit(self.sprite,(self.x-self.sprite.get_width()/2,self.y-self.sprite.get_height()/2));


# game startup code
#a=part(200,200,"a.png");
c=pygame.time.Clock();

# main game loop
while True:
    # event check
    for event in pygame.event.get():
        if event.type == QUIT:
            exit();

    c.tick();
    pygame.display.set_caption(str(c.get_fps()));

    surf.fill((255,255,255));
    x,y=pygame.mouse.get_pos();
    for count in range(1):
        part(x,y,"a.png",600);
    for count in part.list:
        count.life-=1;
        count.draw_self();
        if count.life<=0:
            part.list.remove(count);
            del count;
            #print("Haha")
    #a.draw_self();
    pygame.display.update();