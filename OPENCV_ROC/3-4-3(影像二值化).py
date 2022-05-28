import cv2
import numpy as np

m1=cv2.imread("IMG_01.png",1)
cv2.imshow("Image 1 Resource",m1)

m1[:,:,0]=cv2.adaptiveThreshold(m1[:,:,0],255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,0)
m1[:,:,1]=cv2.adaptiveThreshold(m1[:,:,1],255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,0)
m1[:,:,2]=cv2.adaptiveThreshold(m1[:,:,2],255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,0)
cv2.imshow("Image 1 Change",m1)

cv2.waitKey(0)
cv2.destroyAllWindows()