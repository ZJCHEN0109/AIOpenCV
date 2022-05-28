import cv2
import numpy as np

m1=cv2.imread("IMG_5349.JPG",1)

cv2.imshow("Image 2",m1[100:200,200:500])

cv2.waitKey(0)
cv2.destroyAllWindows()