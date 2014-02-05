# all imports
import math;
import pygame;
from pygame.locals import *
from class_definition import *

# game startup code
c=pygame.time.Clock();

#pygame.display.update()
pygame.display.update(surf.fill((0,0,0)))

# main game loop
while True:
    # event check
    for event in pygame.event.get():
        if event.type == QUIT:
            exit();

    c.tick();
    pygame.display.set_caption(str(c.get_fps()));
    update_inside(player.all_instances);
    player.all_instances.clear(surf,pygame.Surface((400,400)))
    pygame.display.update(player.all_instances.draw(surf));
    #Events here
#--------------------------------------------------------- end---------------------------------------------------#