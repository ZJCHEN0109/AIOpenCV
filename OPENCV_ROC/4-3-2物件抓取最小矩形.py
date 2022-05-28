import cv2
import numpy as np

m1=cv2.imread("Tibame_01.png",1)

m2=cv2.cvtColor(m1,cv2.COLOR_BGR2GRAY)
t,m2=cv2.threshold(m2,240,255,cv2.THRESH_BINARY)
cv2.imshow("Image 2 Gray threshold",m2)
p,t=cv2.findContours(m2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

x,y,w,h=cv2.boundingRect(p[12])
cv2.rectangle(m1,(x,y),(x*w,y*h),(0,0,255),2)
m1=m1[y:y*h,x:x*w]
cv2.imshow("Image 1 BGR",m1)



cv2.waitKey(0)
cv2.destroyAllWindows()