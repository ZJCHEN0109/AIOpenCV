import cv2
import numpy as np

m1=cv2.imread("IMG_01.png",1)
cv2.imshow("Image 1 source",m1)

m2=cv2.inRange(m1,(0,0,0),(255,50,50))
m2=cv2.bitwise_not(m2)
m2=cv2.cvtColor(m2,cv2.COLOR_GRAY2BGR)
m2=cv2.add(m1,m2)
cv2.imshow("Image 2",m2)

cv2.waitKey(0)
cv2.destroyAllWindows()