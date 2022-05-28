import cv2
import numpy as np

m1=cv2.imread("IMG_01.png",1)
cv2.imshow("Image 1 Resource",m1)

m1=cv2.Canny(m1,100,150)
cv2.imshow("Image 1 Change",m1)

cv2.waitKey(0)
cv2.destroyAllWindows()