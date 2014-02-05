import SimpleCV as s
import time
#cam=s.Camera()
cam=s.JpegStreamCamera(r"192.168.173.227:8080/videofeed")
c1=time.clock()
while True:
    img=cam.getImage().show()
    c2=time.clock()
    print(1/(c1-c2))
    c1=c2