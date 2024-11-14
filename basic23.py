#แสดงผลภาพด้วย matplotlib
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image/girl.jpg")
cv2.imshow("Output",img)

plt.imshow(img)
plt.show()