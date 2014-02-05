import cv2
# read image
im = cv2.imread("Photo0094.jpg")
h,w = im.shape[:2]
print h,w
# save image
cv2.imwrite("result.png",im)