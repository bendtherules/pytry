# all imports
import pygame
from pygame.locals import *

# init
pygame.init()

# setting display
surf=pygame.display.set_mode((400,400))
pygame.display.set_caption("Wtf is this??")

# loading sprites and backgrounds
spr_cursor=pygame.image.load("sprite0.png").convert_alpha();
back_0=pygame.image.load("result.png").convert();

# set up fonts
font_default=pygame.font.SysFont(None,40);

# set up colour
c_grey=(128,128,128);

# set up text
text=font_default.render("This is a text",True,c_grey);
textRect=text.get_rect();
textRect.center=surf.get_rect().center

# main game loop
while True:
    # event check
    for event in pygame.event.get():
        if event.type == QUIT:
            exit();
    # draw
    surf.blit(back_0,(0,0));
    surf.blit(text,textRect);
    x,y=pygame.mouse.get_pos();
    x-=spr_cursor.get_width()/2;
    y-=spr_cursor.get_height()/2;
    surf.blit(spr_cursor,(x,y));

    pygame.display.update();