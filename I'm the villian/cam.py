from SimpleCV import Camera, Display, Image;
cam=Camera();
disp=Display();
img=cam.getImage();
img.sample_points(disp);