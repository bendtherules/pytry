import SimpleCV as s
import time
c= s.Camera(0, {'width': 320, 'height': 240})
size=25
count=size-1 # important to make it float
i=[]
for temp in range(size):
    i.append(c.getImage())
    print(temp)
d=s.Display()
while not d.isDone():
    show_img=c.getImage()
    i[int(count)]=show_img
    count+=1
    if count==size:
        count=0
    print(count/(count+1))
    temp_img=s.Image((320,240))
    for temp in i:
        temp_img+=(temp/float(size))
    show_img=(show_img-temp_img)+(temp_img-show_img)
##    print(count)
##    i1.save(d)
##    time.sleep(0.05)
    show_img.binarize(50).erode(4).dilate(4).save(d)