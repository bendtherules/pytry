# all imports
import math;
import pygame;
from pygame.locals import *
from class_definition import *
#from class_definition import player_down

# game startup code
c=pygame.time.Clock();

#pygame.display.update()
pygame.display.update(surf.fill((55,55,55)))
steps=0;
# main game loop
while True:
    # event check
    for event in pygame.event.get():
        if event.type == QUIT:
            exit();

    c.tick(30);
    steps+=1;
    if steps==4000:
        b.destroy();
    pygame.display.set_caption(str(c.get_fps()));
    update_inside(player_down.all_instances);
    update_inside(player_above.all_instances);

    # code to clear both player_down and player_above
    if player_down.all_instances:
        temp_instance=(player_down.all_instances.sprites())[0];
        temp_surf=None;
        temp_surf=pygame.Surface((temp_instance.image.get_width(),temp_instance.image.get_height()));
        temp_surf.fill(pygame.Color(255,0,0));
        print(1)
        player_down.all_instances.clear(surf,temp_surf);
        del temp_surf;

    if player_above.all_instances:
        temp_instance=(player_above.all_instances.sprites())[0];
        temp_surf=None;
        temp_surf=pygame.Surface((temp_instance.image.get_width(),temp_instance.image.get_height()));
        temp_surf.fill(pygame.Color(0,255,255));
        print(2)
        player_above.all_instances.clear(surf,temp_surf);
        del temp_surf;
    #"clear code" done
    a=player_down.all_instances.draw(surf)
    b=player_above.all_instances.draw(surf)
    print(a)
    print(b)
    pygame.display.update();
    #pygame.display.update(b);
    #Events here
#--------------------------------------------------------- end---------------------------------------------------#