import cv2
import numpy as np

m1=cv2.imread("Tibame_01.png",1)

m2=cv2.cvtColor(m1,cv2.COLOR_BGR2GRAY)
t,m2=cv2.threshold(m2,240,255,cv2.THRESH_BINARY)
cv2.imshow("Image 2 Gray threshold",m2)
p,t=cv2.findContours(m2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

cv2.drawContours(m1,p,12,(0,0,255),2)
cv2.imshow("Image 1 BGR",m1)



cv2.waitKey(0)
cv2.destroyAllWindows()