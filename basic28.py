import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image/map.jpg",0)

thresh,th1 = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,1)

cv2.imshow("thresh",th1)
cv2.imshow("mean",th2)

cv2.waitKey(0)
cv2.destroyAllWindows()