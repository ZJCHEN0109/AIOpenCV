import cv2
import numpy as np

m1=cv2.imread("1.png",1)

cv2.imwrite("1.png",m1,[cv2.IMWRITE_JPEG_QUALITY,0])

m2=cv2.imread("1.jpg",1)

cv2.imshow("Image 1.png",m1)
cv2.imshow("Image 1.jpg",m2)

cv2.waitKey(0)
cv2.destroyAllWindows()