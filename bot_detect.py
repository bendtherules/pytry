import SimpleCV as s
import time
import webcolors as w
import serial_setup
from math import sqrt,atan2,degrees,sin, cos,radians

#Uncomment below line only while using serial
#serial_setup.setup(port=8)

def mean(list_a):
    sum=0
    for elements in list_a:
        sum+=elements
    return float(sum)/len(list_a)

clock1=time.clock()
cam=s.JpegStreamCamera(r"http://192.168.173.109:8080/videofeed")
def loop():
    #img=s.Image(r"C:\Users\Abhas_2\Desktop\untitled.png").scale(.25)
    img=cam.getImage()
    #clock1=time.clock()
    #print("0: "+str(1/(time.clock()-clock1)))
    img2=img.toGray()
    #print("1: "+str(1/(time.clock()-clock1)))
    img_black=img2.stretch(50,50)
    #img_black=img2.threshold(10)
    #print("2: "+str(1/(time.clock()-clock1)))
    bot_blobs=img_black.invert().findBlobs()
    if bot_blobs:
        bot=bot_blobs[-1:][0]
        #print("3: "+str(1/(time.clock()-clock1)))
        bot_hole=(img2.crop(bot)-bot.hullMask().invert()).morphOpen()
        #print("4: "+str(1/(time.clock()-clock1)))
        hole_blobs=bot_hole.findBlobs()
        if hole_blobs:
            hole=hole_blobs[-1:][0]
        hole_center=[bot.topLeftCorner()[0]+hole.x, bot.topLeftCorner()[1]+hole.y]
        #print("5: "+str(1/(time.clock()-clock1)))
        bot_center=bot.centroid()
        bot_radius=bot.radius()
        bot_angle=ball_angle=degrees(atan2(-(hole_center[1]-bot_center[1]),hole_center[0]-bot_center[0]))
        img3=(img2-img)+(img-img2)
        #img3.show()

        #f[0].show()
        #print("6: "+str(1/(time.clock()-clock1)))
        img_=img-img3.threshold(5).invert()
        #print("7: "+str(1/(time.clock()-clock1)))
        f=img_.findBlobs()
        #print("8: "+str(1/(time.clock()-clock1)))
        if f:
            f=f[-1:]
            c_match=f[0].meanColor()
            ball_centre=[f[0].x,f[0].y]
            ball_angle=degrees(atan2(-(ball_centre[1]-bot_center[1]),ball_centre[0]-bot_center[0]))
            #print(ball_angle)
            img.drawLine(ball_centre,bot_center,s.Color.YELLOW,5)
            #img_.drawLine(bot_center,[bot_center[0]+cos(radians( bot_angle))*bot_radius,bot_center[1]-sin(radians(bot_angle))*bot_radius],s.Color.BLUE,5)
            #img_.show()
            #c=f[0].centroid()
            #out=img_.crop(c[0],c[1],f[0].width(),f[0].height(),True)

            #img_in=out.crop(out.width/2,out.height/2,out.width/sqrt(2),out.height/sqrt(2),True)
            #c_match=img_in.toRGB().meanColor()
            #print(c_match)
            c_match=s.Color.getHueFromRGB(c_match)
            #print(c_match)
            least=255*3
            color=None
            list_check=s.Color.colorlist
            #list_check=[s.Color.getHueFromRGB(s.Color.YELLOW),s.Color.getHueFromRGB(s.Color.RED),s.Color.getHueFromRGB(s.Color.BLUE),s.Color.getHueFromRGB(s.Color.GREEN),s.Color.getHueFromRGB(s.Color.HOTPINK)]
            for c in list_check:
                c_=s.Color.getHueFromRGB(c)
                diff=abs(c_match-c_)
                if diff<least:
                    #print(diff)
                    #print(c_)
                    color=c_
                    least=diff
            #print(color)
            color=s.Color.hueToRGB(color)
            #print(color)

            color_name=w.rgb_to_name(color)
            #print(color_name)
        #print("9: "+str(1/(time.clock()-clock1)))
        img.drawLine([bot.x,bot.y],hole_center,s.Color.AQUAMARINE,thickness=5)

        #minimum angle between ball_angle and bot_angle
        # returns positive angle for anti-clockwise rotation and else negative angle
        diff_angle = ball_angle-bot_angle
        diff_angle = (diff_angle + 180) % 360 - 180
        print(diff_angle)

        #send_signal(diff_angle)
        #print("10: "+str(1/(time.clock()-clock1)))
        img.show()

def send_signal(diff_angle):
    basic=120
    total=255
    mod_angle=abs(diff_angle)
    sign=diff_angle/mod_angle
    val=str(sign*(float(mod_angle)/360*(total-basic)+basic))
    print("Sending: "+val)
    serial_setup.ser.write(val)

# Actual code
while True:
    loop()
