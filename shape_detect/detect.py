import SimpleCV as s
from math import *
import time as t
thresh=8 # in percentage
fname=r"D:\Babu\github_files\pytry\shape_detect\pics\rect.jpg"
c=s.Camera()
def run():
    t1=t.clock()
    i=s.Image(fname).scale(.25)
    #i=c.getImage()
    #i.show()
    blobs=i.findBlobs()

    def isClose(a,b):
        if float(abs(a-b))/min(a,b)*100<=thresh:
            return True
        else:
            return False

    def checkSymmetry():
        tmp_img=blob.crop()
        #tmp_img.show()
        tmp_img_upper=tmp_img.crop(0,0,tmp_w,tmp_h/2)
        tmp_img_lower=tmp_img.crop(0,tmp_h/2,tmp_w,tmp_h/2)
        #tmp_img_upper.sideBySide(tmp_img_lower).show()
        tmp_blob_upper=tmp_img_upper.findBlobs()[0]
        tmp_blob_lower=tmp_img_lower.findBlobs()[0]
        return isClose(tmp_blob_upper.area(),tmp_blob_lower.area())

    def checkCircle():
        if isClose(tmp_w,tmp_h) and isClose(pi*(tmp_w/2)**2,tmp_a):
            return "Circle"
        else:
            return False

    def checkRect():
        if isClose(tmp_w*tmp_h,tmp_a):
            return "Rectangle"
        else:
            return False

    def checkTri():
        if isClose(0.5*tmp_w*tmp_h,tmp_a) and not checkSymmetry():
            return "Triangle"
        else:
            return False

    if blobs:
        #blobs.show()
        for blob in blobs:
            tmp_w=blob.width()
            tmp_h=blob.height()
            tmp_a=blob.area()
            #print(tmp_w,tmp_h,tmp_a)
            isCircle=checkCircle()
            #print(isCircle)
            isRect=checkRect()
            #print(isRect)
            isTri=checkTri()
            #print(isTri)
            print isCircle or isRect or isTri

    t2=t.clock()
    print(1/(t2-t1))

run()