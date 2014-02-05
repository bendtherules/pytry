import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_mode((200,200))
pygame.display.set_caption("wat?")
a=pygame.image.load("a.png");
while True:
    # event check
    for event in pygame.event.get():
        if event.type == QUIT:
            exit();
