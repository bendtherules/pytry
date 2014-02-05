# all imports
import math;
import pygame;
from pygame.locals import *

# init
pygame.init()

# setting display
surf=pygame.display.set_mode((400,400))
pygame.display.set_caption("Bendtherules rocks!!")

class obj():
    '''Can be inherited as a base class'''
    list=[];
    def __init__(self,x,y,sprite_filename):
        self.x=x;
        self.y=y;
        self.xprevious=x;
        self.yprevious=y; #ToDO : Make way for acceleration ("force" model) and setting speed
        self.sprite=pygame.image.load(sprite_filename).convert_alpha();
        obj.list.append(self);

    def get_speed(self):
        return int(math.sqrt(self.get_hspeed()**2+self.get_vspeed*()*2));

    def get_hspeed(self):
        return (self.x-self.xprevious);

    def get_vspeed(self):
        return (self.y-self.yprevious);

    def draw_self(self):
        surf.blit(self.sprite,(self.x-self.sprite.get_width()/2,self.y-self.sprite.get_height()/2));

    def update(self):
        ''' Should be called after draw_self (or as the last method) to update xprevious.
            If not called, get_speed(),get_hspeed(),get_vspeed() won't work'''
        self.xprevious=self.x;
        self.x+=1

# game startup code
c=pygame.time.Clock();
a=obj(100,100,"a.png");
surf.fill((250,50,50))
# main game loop
while True:
    # event check
    for event in pygame.event.get():
        if event.type == QUIT:
            exit();
    surf.fill((250,50,50))
    a.update()
    a.draw_self();
    c.tick();
    pygame.display.set_caption(str(c.get_fps()));
    pygame.display.update();

    #Events here
#--------------------------------------------------------- end---------------------------------------------------#