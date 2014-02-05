#-------------------------------------------------------------------------------
# Name:        serial n scan
#
# Purpose:      1.To scan a image n divide into least possible number of lines
#               2.Send required commands in the serial port(maybe, 2 will be better) as tuples
#                 (permitted values are -1,0,1 for both wheels)
#
# Author:      bendtherules
#
# Created:     21-12-2012
#-------------------------------------------------------------------------------

import pygame
from pygame.locals import *
pygame.init();
milli_start=pygame.time.get_ticks()
surf=pygame.display.set_mode((1,1));
img=pygame.image.load("a.png").convert_alpha();
pygame.Surface.lock(img);
arr_3d=pygame.surfarray.pixels3d(img);
arr_2d=pygame.surfarray.pixels_alpha(img);
pygame.Surface.unlock(img);
#loop here
start_x=start_y=None;
all_lists=[];
count_list=0;
counted=[[False]*arr_2d]*arr_2d[0];#used as an array of the same dimensions as arr_2d to know whether it has been scanned
for x in range(len(arr_2d)):
    for y in range(len(arr_2d[0])):
        if arr_2d[x][y]>=128:
            arr_2d[x][y]=255;
            if start_x==None:
                start_x=x;
                start_y=y;
                counted[x][y]=True;
        else:
            arr_2d[x][y]=0;
def scan(start_x=start_x,start_y=start_y,new=True):
    #new should be true when it is a new line or new sub-line
    #start_x and start_y needs to be passed in this recursive function in later recursion calls
    #Default values are passed to make the function friendlier, but they should be overridden in later calls
    global arr_2d;
    global counted;
    global count_list;
    global all_lists;
    if new==True:
        temp_list=[];
    for count_x in (-1,0,1):
        for count_y in (-1,0,1):
            if arr_2d[x+count_x][y+count_y]==255 and counted[x][y]==False:
                #counted[x][y] check eliminated the (start_x,start_y) pixel
                counted[x+count_x][y+count_y]=True;
                all_lists.append((x+count_x,y+count_y))

#the end
milli_end=pygame.time.get_ticks()
print(milli_end-milli_start);
