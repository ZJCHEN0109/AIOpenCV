import cv2
import numpy as np

m1=np.full((300,500,3),(255,255,255),np.uint8)

from PIL import ImageFont,ImageDraw,Image
p=Image.fromarray(m1)

ImageDraw.Draw(p).text((100,100),"你好",(0,0,255),ImageFont.truetype("kaiu.ttf",30))

m1=np.array(p)

cv2.imshow("Image 1",m1)

cv2.waitKey(0)
cv2.destroyAllWindows()