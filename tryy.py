import sys,pygame,math,class_ball;
#from class_ball import *
pygame.init()
clock = pygame.time.Clock()
size=width,height=640,480
#x=320
#y=240
#speed=3
#dir=None
black=0,0,0
class_list=[]
screen=pygame.display.set_mode(size)
#ball=pygame.image.load("gun.png")
#ballrect=ball.get_rect()
#mouse_down=False
#print pygame

##class ball(object):
##    global mouse_down
##    def __init__(self,x=320,y=240,speed=3):
##        self.x=x
##        self.y=y
##        self.speed=speed
##        self.dir=None
##        self.ball=pygame.image.load("gun.png")
##        self.ballrect=self.ball.get_rect()
##        #global mouse_down
##        #mouse_down=False;
##        if not mouse_down:
##            print 5
##
##    def mouse_handler(self):
##        global mouse_down
##        if pygame.event.get(pygame.MOUSEBUTTONDOWN) or mouse_down == True:
##            self.x=self.mouse_x
##            self.y=self.mouse_y
##            mouse_down=True
##            print 6
##
##        if pygame.event.get(pygame.MOUSEBUTTONUP):
##            mouse_down=False
##
##    def step(self):
##        self.mouse_x,self.mouse_y=pygame.mouse.get_pos()
##        self.diff_x=self.mouse_x-self.x
##        self.diff_y=self.mouse_y-self.y
##        self.diff_rad=math.atan2(self.diff_y,self.diff_x)
##        self.x+=self.speed*math.cos(self.diff_rad)
##        self.y+=self.speed*math.sin(self.diff_rad)
##        self.ballrect.center=(self.x,self.y)
##
##    def draw(self):
##        screen.blit(self.ball, self.ballrect)
##
##
##    def update(self):
##        self.step()
##        self.mouse_handler()
##        self.draw()


#ball_1=ball(class_lst=class_list)
while 1:
        screen.fill(black)

##            if event.type == pygame.MOUSEBUTTONDOWN or mouse_down == True:
##                x=mouse_x
##                y=mouse_y
##                mouse_down=True
##
##            if event.type == pygame.MOUSEBUTTONUP:
##                mouse_down=False
##
##        mouse_x,mouse_y=pygame.mouse.get_pos()
##        diff_x=mouse_x-x
##        diff_y=mouse_y-y
##        diff_rad=math.atan2(diff_y,diff_x)
##        x+=speed*math.cos(diff_rad)
##        y+=speed*math.sin(diff_rad)
##
##        ballrect.center=(x,y)
##        if ballrect.left < 0 or ballrect.right > width:
##            speed[0] = -speed[0]
##        if ballrect.top < 0 or ballrect.bottom > height:
##            speed[1] = -speed[1]


##        screen.blit(ball, ballrect)

        #ball_1.update()
        clock.tick(120)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        pygame.display.flip()