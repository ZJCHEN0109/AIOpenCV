import cv2
import numpy as np

m1=cv2.imread("IMG_01.png",1)
cv2.imshow("Image 1 Resource",m1)

t,m2=cv2.threshold(m1[:,:,0],120,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
print(t)
t,m2=cv2.threshold(m1[:,:,1],120,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
print(t)
t,m2=cv2.threshold(m1[:,:,2],120,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
print(t)


cv2.imshow("Image 2",m2)

cv2.waitKey(0)
cv2.destroyAllWindows()