import cv2
import numpy as np

m1=cv2.imread("IMG_01.png",1)
cv2.imshow("Image 1 Resource",m1)

m1[:,:,0]=cv2.equalizeHist(m1[:,:,0])
m1[:,:,1]=cv2.equalizeHist(m1[:,:,1])
m1[:,:,2]=cv2.equalizeHist(m1[:,:,2])
cv2.imshow("Image 1 Change",m1)

cv2.waitKey(0)
cv2.destroyAllWindows()