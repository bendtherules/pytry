import SimpleCV as s
import time
import simulate_keypress as press
#c=s.JpegStreamCamera(r"192.168.173.169:8080/videofeed")
c=s.Camera()
c1=time.clock()
gesture_time=30
detection_sleep=False
blobs=[None]*gesture_time
#d=s.Display()
i1=c.getImage()
img_width_ori=i1.width
img_height=i1.height
i1=i1.crop(img_width_ori/4,0,img_width_ori*3/4,img_height/2).flipHorizontal()
img_width=img_width_ori/2
count=0
while True:
    i2=c.getImage().crop(img_width_ori/4,0,img_width_ori*3/4,img_height/2).flipHorizontal()
    i3=(i2-i1)+(i1-i2)
    i1=i2
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
            min_x_list.append([min(temp[0] for temp in blobs_temp.center()),count_blobs])
            #min_y_list.append([min(temp[1] for temp in blobs_temp.topLeftCorners()),count_blobs])
            max_x_list.append([max(temp[0] for temp in blobs_temp.center()),count_blobs])
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
        if not detection_sleep and detection_width> img_width*0.80:
            print("Detected")
            blobs=[None]*gesture_time
            print(right_step,left_step)
            if right_step>left_step:
                print("Left to right")
                press.press_up()
            else:
                print("Right to left")
                press.press_down()
            print(c1)
            detection_sleep=gesture_time*2
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
    if f:
        f.draw(width=2)
    #i3.show()
    c2=time.clock()
    #print(1/(c1-c2))
    c1=c2
    count+=1
    count=count%gesture_time
##    i2.findSkintoneBlobs().show()