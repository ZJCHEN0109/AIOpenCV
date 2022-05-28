import cv2
import numpy as np

img1=cv2.imread("IMG_5349.JPG",1)

img2=np.full(img1.shape,(100,100,100),np.uint8)

img3=cv2.subtract(img1,img2)

cv2.imshow("Image 1",img1)
cv2.imshow("Image 2",img2)
cv2.imshow("Image 3",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()