import cv2
import numpy as np
import pytesseract as pt

m1=cv2.imread("Tibame_01.png",1)
m2=cv2.erode(m1,np.ones((7,7))) #將色彩值低的地方浸蝕調色彩值低的地方 而白色為色彩值高-依照圖片客製化
m2=cv2.cvtColor(m2,cv2.COLOR_BGR2GRAY) #將所有黏在一起的字色彩灰階化簡化
t,m2=cv2.threshold(m2,240,255,cv2.THRESH_BINARY) #在做二值化處理只剩黑色及白色
m2=cv2.bitwise_not(m2)
p,t=cv2.findContours(m2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) #尋找輪廓
for d in p:
	x,y,w,h =cv2.boundingRect(d)
	if w > h:
		m2=m1[y:y+h,x:x+w].copy()
		m1[:,:]=255 #清空m1變數
		m1[y:y+h,x:x+w]=m2

cv2.imshow("Image 1",m2)
t=pt.image_to_string(m1,"eng")
# print(p)
# print(t)

cv2.waitKey(0)
cv2.destroyAllWindows()