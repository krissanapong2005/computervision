#สร้างเส้นเชื่อมโยง

import cv2
import numpy as np
img = np.zeros([400,400,3])

points = []
def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,0,255),4)
        points.append((x,y))
        print(points)
        if len(points) >= 2:
            cv2.line(img,points[-2],points[-1],(0,255,0),5)
        cv2.imshow("Output",img)

#แสดงภาพ
cv2.imshow("Output",img)

#ทำงานกับ Mouse
cv2.setMouseCallback("Output",clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()