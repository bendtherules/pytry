# all imports
import math;
import pygame;
from pygame.locals import *

# init
pygame.init()

# setting display
surf=pygame.display.set_mode((400,400))
pygame.display.set_caption("Wtf is this??")

'''class obj(pygame.sprite.Sprite):
    Can be inherited as a base class
    #all_obj_derived=pygame.sprite.Group();
    def __init__(self,x,y,sprite_filename,alpha=None):
         alpha may have values None(no alpha set),1(set_colorkey as the bottom-right corner),2(per-pixel alpha)
        super(obj,self).__init__();
        self.x=x;
        self.y=y;
        self.xprevious=x;
        self.yprevious=y; #ToDO : Make way for acceleration ("force" model) and setting speed
        # set correct spr attribute
        self.spr=pygame.image.load(sprite_filename).convert();

        if alpha==None:
            self.spr=self.spr.convert();
        elif alpha==1:
            self.spr=self.spr.convert();
            self.spr.set_colorkey(self.spr.get_at((self.spr.get_width(),self.spr.get_height())));
        elif alpha==2:
            self.spr=self.spr.convert_alpha();

        self.image=self.spr;#spr and image point to the same surface, to be checked

        # as it is a derived class of Sprite, it can be directly added to gr group
        #obj.all_obj_derived.add(self);


    #obj.list.append(self);

    def get_speed(self):
        return int(math.sqrt(self.get_hspeed()**2+self.get_vspeed*()*2));

    def get_hspeed(self):
        return (self.x-self.xprevious);

    def get_vspeed(self):
        return (self.y-self.yprevious);

    def draw_self(self):
        surf.blit(self.sprite,(self.x-self.sprite.get_width()/2,self.y-self.sprite.get_height()/2));

    def update(self):
         Should be called after draw_self (or as the last method) to update xprevious.
            If not called, get_speed(),get_hspeed(),get_vspeed() won't work
        self.x+=1;
        #self.y+=1;
        self.xprevious=self.x;
        self.yprevious=self.y;
        self.rect=self.image.get_rect(center=(self.x,self.y));'''

# creating new classes
'''class a(obj):
    all_instances=pygame.sprite.RenderUpdates();
    def __init__(self,x,y,sprite_filename,alpha=None):
        super().__init__(x,y,sprite_filename,alpha=None)
        a.all_instances.add(self);'''
#    wow=True;

#class b(obj):
    #wow=False;

#a1=a(surf.get_width()/2,surf.get_height()/2,"ball.bmp")
#a2=a(100,100,"ball.bmp")
# game startup code
c=pygame.time.Clock();
#surf.fill((255,0,255))
# main game loop
while True:
    # event check
    for event in pygame.event.get():
        if event.type == QUIT:
            exit();

    c.tick();
#    pygame.display.set_caption(str(c.get_fps()));
    #

'''    for b in a.all_instances.sprites():
        if b.x+b.image.get_width()<surf.get_width():
            b.update()
        else:
            a.all_instances.remove(b);
            print(12)'''

    #pygame.display.update(a.all_instances.draw(surf));
    #Events here
#--------------------------------------------------------- end---------------------------------------------------#