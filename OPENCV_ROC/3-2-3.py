import cv2
import numpy as np

m1=cv2.imread("IMG_5349.JPG",1)
#cv2.imshow("Image 1",m1)

p=cv2.getRotationMatrix2D((150,150),45,1)
m1=cv2.warpAffine(m1,p,(500,300))

cv2.imshow("Image 2",m1)
cv2.waitKey(0)
cv2.destroyAllWindows()