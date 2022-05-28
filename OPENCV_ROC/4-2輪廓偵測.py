import cv2
import numpy as np

m1=cv2.imread("Tibame_01.png",0)
t,m1=cv2.threshold(m1,240,255,cv2.THRESH_BINARY)
cv2.imshow("Image 1 source",m1)
p,t=cv2.findContours(m1,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

print("輪廓點資料:")
print(p)

print("階層資料:")
print(t)

cv2.waitKey(0)
cv2.destroyAllWindows()