import math;
import pygame;
from pygame.locals import *
pygame.init()
surf=pygame.display.set_mode((400,400))
pygame.display.set_caption("Wtf is this??")
#c=pygame.time.Clock();
while True:
    # event check
    for event in pygame.event.get():
        if event.type == QUIT:
            exit();

    #c.tick();