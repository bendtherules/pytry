import SimpleCV as s
import time
c=s.JpegStreamCamera(r"192.168.173.169:8080/videofeed")
c1=time.clock()
gesture_time=60
detection_sleep=False
blobs=[None]*gesture_time
#d=s.Display()
i1=c.getImage()
img_width=i1.width
img_height=i1.height
i1=i1.crop(0,0,img_width,img_height/2).flipHorizontal()
count=0
while True:
    i2=c.getImage().crop(0,0,img_width,img_height/2).flipHorizontal()
    i3=(i2-i1)+(i1-i2)
    i1=i2
##    i3=i3.erode(7).dilate(7).binarize()
##    i3=i3.invert()
##    f=i3.findBlobs(minsize=35)
##    if f:
##        totalSum=0
##        areaSum=0
##        for temp in f:
##            areaSum+=temp.area()
##            totalSum+=temp.area()*temp.x
##        if areaSum!=0:
##            avgX=totalSum/areaSum
##        i3.drawText(text="Avg. X="+str(avgX),x=avgX,color=s.Color.AQUAMARINE)
##        f.draw(width=3)
##    else:
##        print("None")
    i3=i3.stretch(10,255).erode(2).dilate(2)
    f=i3.findBlobs(minsize=100)
    blobs[count]=f
    min_x_list=[]
    #min_y_list=[]
    max_x_list=[]
    #max_y_list=[]
    blobs_empty=True
    count_blobs=0
    for blobs_temp in blobs:
        count_blobs+=1
        if blobs_temp:
            min_x_list.append([min(temp[0] for temp in blobs_temp.topLeftCorners()),count_blobs])
            #min_y_list.append([min(temp[1] for temp in blobs_temp.topLeftCorners()),count_blobs])
            max_x_list.append([max(temp[0] for temp in blobs_temp.bottomRightCorners()),count_blobs])
            #max_y_list.append([min(temp[1] for temp in blobs_temp.bottomRightCorners()),count_blobs])
            blobs_empty=False
    if not blobs_empty:
        min_x=min([temp[0] for temp in min_x_list])
        left_step=min_x_list[[temp[0] for temp in min_x_list].index(min_x)][1]
        #min_y=min([temp[0] for temp in min_y_list])
        max_x=max([temp[0] for temp in max_x_list])
        right_step=max_x_list[[temp[0] for temp in max_x_list].index(max_x)][1]
        #max_y=max([temp[0] for temp in max_y_list])
        detection_width=abs(max_x-min_x)
        if not detection_sleep and detection_width> img_width*0.70:
            print("Detected")
            print(right_step,left_step)
            if right_step>left_step:
                print("Left to right")
            else:
                print("Right to left")
            print(c1)
            detection_sleep=gesture_time+1
        else:
            pass
            #print("Not detected")
    else:
        min_x=None
        min_y=None
        max_x=None
        max_y=None
    if detection_sleep:
        detection_sleep-=1
##    max_x=min([max([temp[0] for temp in blobs_temp.topLeftCorners()]) for blobs_temp in blobs if blobs_temp ].append(0))
##    min_x=min([min([temp[0] for temp in blobs_temp.topLeftCorners()]) for blobs_temp in blobs])
##    max_y=max([max([temp[1] for temp in blobs_temp.bottomRightCorners()]) for blobs_temp in blobs])
##    min_y=min([min([temp[1] for temp in blobs_temp.bottomRightCorners()]) for blobs_temp in blobs])
    if f:
        f.draw(width=2)
    i3.show()
    c2=time.clock()
    #print(1/(c1-c2))
    c1=c2
    count+=1
    count=count%gesture_time
##    i2.findSkintoneBlobs().show()