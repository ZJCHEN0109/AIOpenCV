import cv2
import numpy as np

m1=cv2.imread("1.png",1)

m2=cv2.cvtColor(m1,cv2.COLOR_BGR2HSV)

cv2.imshow("Image M1",m1)
cv2.imshow("Image M2",m2)
cv2.waitKey(0)
cv2.destroyAllWindows()