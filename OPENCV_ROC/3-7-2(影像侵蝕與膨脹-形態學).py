import cv2
import numpy as np

m1=cv2.imread("IMG_01.png",1)
cv2.imshow("Image 1 Resource",m1)

#m1=cv2.morphologyEx(m1,cv2.MORPH_OPEN,np.ones((5,5)))
#m1=cv2.morphologyEx(m1,cv2.MORPH_CLOSE,np.ones((5,5)))
m1=cv2.morphologyEx(m1,cv2.MORPH_GRADIENT,np.ones((5,5)))

cv2.imshow("Image 1 Change",m1)

cv2.waitKey(0)
cv2.destroyAllWindows()