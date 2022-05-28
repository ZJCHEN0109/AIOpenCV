import cv2
import numpy as np
import pytesseract as pt

m1=cv2.imread("English.png",1)
cv2.imshow("Image 1",m1)

t=pt.image_to_string(m1,"eng")
print(t)


cv2.waitKey(0)
cv2.destroyAllWindows()