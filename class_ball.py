import pygame
class ball(object):
    #global pygame
    def __init__(self,class_lst,x=320,y=240,speed=3):#pass a shared globals object
        import class_ball
        mouse_down=False
        self.x=x
        self.y=y
        self.speed=speed
        self.dir=None
        self.ball=pygame.image.load("gun.png")
        self.ballrect=self.ball.get_rect()
        #mouse_down=False; # needs to be in a seperate object - make the event stream step-by-step by caching during every step

    def mouse_handler(self):
        if pygame.event.get(pygame.MOUSEBUTTONDOWN) or self.__class__.mouse_down == True:
            self.x=self.mouse_x
            self.y=self.mouse_y
            self.__class__.mouse_down=True
            print 6

        if pygame.event.get(pygame.MOUSEBUTTONUP):
            self.__class__.mouse_down=False

    def step(self):
        self.mouse_x,self.mouse_y=pygame.mouse.get_pos()
        self.diff_x=self.mouse_x-self.x
        self.diff_y=self.mouse_y-self.y
        self.diff_rad=math.atan2(self.diff_y,self.diff_x)
        self.x+=self.speed*math.cos(self.diff_rad)
        self.y+=self.speed*math.sin(self.diff_rad)
        self.ballrect.center=(self.x,self.y)

    def draw(self):
        screen.blit(self.ball, self.ballrect)


    def update(self):
        self.step()
        self.mouse_handler()
        self.draw()

