import SimpleCV as s
import math as m
import random
col=s.Color.RED
c=s.Camera()
d=s.Display()
i1=c.getImage()
i1a=i1.colorDistance(col).binarize(50).erode().dilate()
while True:
    i2=c.getImage()
    i2a=i2.hueDistance(col).binarize(10).show()
##    i3=(i2a-i1a)
##    i3=i3.dilate().erode().morphClose().flipHorizontal()
##    i3.show()
##    i1a=i2a
##
##    f=i3.findBlobs(minsize=200)
##    if f:
##            f=f[-5:]
##            totalSumX=0
##            totalSumY=0
##            areaSum=0
##            for temp in f:
##                areaSum+=temp.area()
##                totalSumX+=temp.area()*temp.x
##                totalSumY+=temp.area()*temp.y
##            if areaSum!=0:
##                avgX=totalSumX/areaSum
##                avgY=totalSumY/areaSum
##            f.draw(width=3)
##            i3.drawText(text="("+str(avgX)+","+str(avgY)+")",x=avgX,y=avgY,color=s.Color.AQUAMARINE)
####    f=i1.findBlobs(minsize=300)
####    if f:
####        f.draw(width=3)
##    i3.save(d)