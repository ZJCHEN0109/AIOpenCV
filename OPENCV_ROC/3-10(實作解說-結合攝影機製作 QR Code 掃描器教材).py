import cv2
import numpy as np
from pyzbar import pyzbar
import os 

p=cv2.VideoCapture(0)
printList=[]
while True:
	ret, m1=p.read() #攝影機是否讀取 ret(True/False)
	if ret==True:
		cv2.imshow("Image 1.png",m1)
		r=pyzbar.decode(m1) #每張影片QRcode掃描辨識
		if len(r)>0: #當有讀取到QRCode資訊
			#os.system("cls")
			for i,d in enumerate(r): #迴圈方式利用enumerate函式來同時輸出影片索引與內容元素
				if d.data not in printList: #判斷每筆雌料是否存在List之中
					printList.append(d.data) #如果不存在則儲存在List之中
					print("第",len(printList),"個條碼，類型：",d.type,"，內容：",end="")
					try:
						print(printList[-1].decode("UTF-8").encode("sjis").decode("UTF-8")) #將編碼轉換成日文編碼再轉換成UTF-8
					except:
						print(printList[-1].decode("UTF-8"))
	cv2.waitKey(50)
cv2.destroyAllWindows()
