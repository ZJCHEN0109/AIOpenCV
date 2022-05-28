import cv2
import numpy as np

m1=cv2.imread("IMG_01.JPG",1)

m1[100:200,200:500]=255
cv2.imshow("Image 2",m1)

cv2.waitKey(0)
cv2.destroyAllWindows()