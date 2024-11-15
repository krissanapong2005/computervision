#แสดงภาพสีจากจุด Pixel

import cv2
import numpy as np

img = cv2.imread("image/cat.jpg")

def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        img_color = np.zeros([300,300,3],np.uint8)
        img_color[:] = [blue,green,red]
        cv2.imshow("Result",img_color)

#แสดงภาพ
cv2.imshow("Output",img)

#ทำงานกับ Mouse
cv2.setMouseCallback("Output",clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()


