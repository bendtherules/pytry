# all imports
import math;
import pygame;
from pygame.locals import *

# init
pygame.init()

# setting display
surf=pygame.display.set_mode((400,400))
pygame.display.set_caption("Wtf is this??")

#custom image-loading function
def load_image(self,sprite_filename=None,alpha=None):
    '''Load correct image with convert calls'''
    if sprite_filename!=None:
        self.spr=pygame.image.load(sprite_filename);
        if alpha==None:
            self.spr=self.spr.convert();
        elif alpha==1:
            self.spr=self.spr.convert();
            self.spr.set_colorkey(self.spr.get_at((self.spr.get_width()-1,self.spr.get_height()-1)));
        elif alpha==2:
            self.spr=self.spr.convert_alpha();

        self.image=self.spr;#spr and image point to the same surface, to be checked
    else:
        self.image=self.spr=None;

class obj(pygame.sprite.Sprite):
    '''Can be inherited as a base class'''
    #all_obj_derived=pygame.sprite.Group();
    def __init__(self,x,y,sprite_filename=None,alpha=None):
        ''' alpha may have values None(no alpha set),1(set_colorkey as the bottom-right corner),2(per-pixel alpha)'''
        super(obj,self).__init__();
        self.x=x;
        self.y=y;
        self.xprevious=x;
        self.yprevious=y; #ToDO : Make way for acceleration ("force" model) and setting speed
        self.hspeed=0;
        self.vspeed=0;
        global load_image;
        load_image(self,sprite_filename,alpha);
        # as it is a derived class of Sprite, it can be directly added to gr group
        #obj.all_obj_derived.add(self);


    #obj.list.append(self);

    def draw_self(self):
        surf.blit(self.sprite,(self.x-self.sprite.get_width()/2,self.y-self.sprite.get_height()/2));

    def update(self):
        ''' Should be called after draw_self (or as the last method) to update xprevious.
            If not called, get_speed(),get_hspeed(),get_vspeed() won't work'''
        self.xprevious=self.x;
        self.yprevious=self.y;
        self.x+=self.hspeed;
        self.y+=self.vspeed;
        self.speed=int(math.sqrt(self.hspeed**2+self.vspeed**2));
        self.rect=self.image.get_rect(center=(self.x,self.y));

#custom-made functions
def update_inside(group_name):
    '''e.g. group_name=a.all_instances.
    Calls group_name.update only when sprite.image is within screen, else delete it.'''
    temp=None;
    for temp in group_name.sprites():
        if (temp.x-temp.image.get_width()/2<surf.get_width()):
            temp.update();
        else:
            group_name.remove(temp);

# creating new classes
class player(obj):
    all_instances=pygame.sprite.RenderUpdates();
    def __init__(self,x,y,sprite_filename,alpha=None):
        super().__init__(x,y,sprite_filename,alpha)
        player.all_instances.add(self);


a1=player(surf.get_width()/2,surf.get_height()/2,"a.png",alpha=1)
a1.vspeed=.1;
a2=player(100,100,"a.png",alpha=1)