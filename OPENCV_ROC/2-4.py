import cv2
import numpy as np


m1=np.full((300,500,3),(255,255,255),np.uint8)

cv2.circle(m1,(200,150),100,(255,0,0),-1)

cv2.imshow("Image1.png",m1)

cv2.waitKey(0)
cv2.destroyAllWindows()