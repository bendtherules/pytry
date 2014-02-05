import SimpleCV as s
import math as m
import random
c=s.Camera()
d=s.Display()
i1=c.getImage()

while d.isNotDone:
    i2=c.getImage()
    #i2=i2.pixelize(10)
    i3=i1-i2
    i1=i2
    i3.save(d)