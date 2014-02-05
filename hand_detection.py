import SimpleCV as s
import math as m
import random
c=s.Camera()
d=s.Display()
i1=c.getImage().pixelize()
avgX=0
absX=0
ballPos=[320,240]
ballSpeedX=10+random.randint(0,5)
ballSpeedY=10+random.randint(0,5)
print ballPos
ballRadius=10
while True:
    i2=c.getImage().pixelize()
    i3=(i2-i1)+(i1-i2)
    i1=i2
    i3=i3.binarize(50).erode(3).dilate(3)
    i3=i3.invert().flipHorizontal()
    f=i3.findBlobs(minsize=200,threshval=50)
    if f:
        totalSum=0
        areaSum=0
        for temp in f:
            areaSum+=temp.area()
            totalSum+=temp.area()*temp.x
        if areaSum!=0:
            avgX=totalSum/areaSum
        f.draw(width=3)
    else:
        print("None")
    x_diff=(avgX-absX)
    if m.copysign(x_diff,1)>=40:
        absX+=m.copysign(40,x_diff)
    else:
        absX=avgX
    #i3.drawText(text="Avg. X="+str(avgX),x=avgX,color=s.Color.AQUAMARINE)
    i3.drawRectangle(absX-50,50,100,20)
    print ballPos
    if ballPos[0]-ballRadius<150:
        ballSpeedX=-ballSpeedX
    if ballPos[0]+ballRadius>640-150:
        ballSpeedX=-ballSpeedX
    if ballPos[1]+ballRadius>480:
        ballSpeedY=-ballSpeedY
    if (ballPos[0] in range(int(absX)-50,int(absX)+50)) and ((ballPos[1]-ballRadius) in range(50,70)):
        ballSpeedY=-ballSpeedY
    elif ballPos[1]-ballRadius<0:
        print("Quitting "+str(ballPos))
        quit()
    ballPos[0]+=ballSpeedX
    ballPos[1]+=ballSpeedY
    i3.drawCircle(tuple(ballPos),ballRadius,color=s.Color.AQUAMARINE)
    #print(absX)
    i3.save(d)