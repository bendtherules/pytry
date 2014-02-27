import SimpleCV as s
#c=s.JpegStreamCamera(r"http://192.168.173.144:8080/videofeed")
c=s.Camera()
##i=c.getImage().scale(.5)
##f=i.findHaarFeatures("face.xml")
count=1
while count<5:
    count+=1
    i=c.getImage()
    f=i.findHaarFeatures("face.xml")
    if f:
        f.draw(width=2)
    i.show()

i.flipHorizontal().save(r"D:\Babu\github_files\pytry\robocon\face_detect.jpg")
##f.show()
##import time
##cl=time.clock()
##if time.clock()-cl<2:
##    pass
##fs1=[]
##bbox=f[0].boundingBox()
##
##while True:
##    img1 = c.getImage()
##    fs1 = img1.track("camshift",fs1,i,tuple(bbox),num_frames=5)
##    fs1.drawBB()
##    fs1.draw()
##    img1.show()
##    del img1
    #fs1.drawPredict(color=Color.RED)