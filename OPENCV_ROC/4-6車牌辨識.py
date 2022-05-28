import cv2
import numpy as np
import pytesseract as pt

m1=cv2.imread("01.jpg", 1)
m2=m1.copy()
m2[:,:,0]=cv2.adaptiveThreshold(m1[:,:,0],255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,0) # 車牌背景為純色光滑面，使用二值化每張圖片切割成數小塊，給予門檻值操作
m2[:,:,1]=cv2.adaptiveThreshold(m1[:,:,1],255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,0) # 顏色與原色交界處會變成黑色，原色則為白色
m2[:,:,2]=cv2.adaptiveThreshold(m1[:,:,2],255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,0)
m2=cv2.cvtColor(m2,cv2.COLOR_BGR2GRAY) # 轉為灰階
ct, th=cv2.findContours(m2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #輪廓檢測，統計輪廓彼此包覆關係　
parentList=np.zeros((len(ct))) # 車牌自身為輪廓　車牌內文字各自為一個輪廓
for d in th[0]: # 輪廓彼此間包覆關係
	if d[3]!=-1: # 第三為輪廓索引為-1代表沒有 1代表相鄰的下一個輪廓
		parentList[d[3]]+=1


for d in np.where(parentList>9)[0]: # 取共同特徵 當有包覆九個以上輪廓則篩選取出 包含會有 貼紙 中文字 數字 - 和兩個螺絲
	x, y, w, h =cv2.boundingRect(ct[d])
	if w>h*1.2 and w<h*3: #車牌比例
		m2=m1[y:y+h,x:x+w].copy()
		m2=cv2.cvtColor(m2,cv2.COLOR_BGR2GRAY)
		m2=cv2.divide(m2,np.full(m2.shape,51,np.uint8)) # 將顏色淨化處理 除法指令　將顏色值除以51 (0~5)
		m2=cv2.multiply(m2,np.full(m2.shape,51,np.uint8)) # 將顏色淨化處理　乘法指令　將顏色值成以51 (0~255)
		if len(np.where(m2>=204)[0])>m2.shape[0]*m2.shape[1]*0.2: # 將顏色>204篩選出 204/51=4 即唯一只有255大於204 篩選出最亮的車牌
			# cv2.imwrite("output/"+str(x)+".png", m1[y:y+h,x:x+w])
			cv2.rectangle(m1,(x,y),(x+w,y+h),(0,0,255),3)

m1=cv2.resize(m1,(640,360))
cv2.imshow("Image M1", m1)

cv2.waitKey(0)
cv2.destroyAllWindows()