import cv2
import numpy as np
p=cv2.VideoCapture(0)
while True:
	ret,m1=p.read()
	if ret==True:
		cv2.imshow("Image 1.png",m1)

	cv2.waitKey(50)
cv2.destroyAllWindows()