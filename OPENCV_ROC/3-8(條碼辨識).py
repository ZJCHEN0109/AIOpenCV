import cv2
import numpy as np

m1=cv2.imread("QRCode2.png",1)
cv2.imshow("Image 1 Resource",m1)

from pyzbar import pyzbar

r=pyzbar.decode(m1)

for i,d in enumerate(r):
	print("第",i+1,"個條碼,類型:",d.type,",內容:",d.data.decode("UTF-8"))

cv2.imshow("Image 1 Change",m1)

cv2.waitKey(0)
cv2.destroyAllWindows()