import cv2
#อ่านภาพ
img = cv2.imread("image/cat.jpg",-1)
imgresize = cv2.resize(img,(400,400))
#แสดงภาพ ดีเลย์ คืนพื้นที่
cv2.imshow("Output",imgresize)
cv2.waitKey(delay=5000)
cv2.destroyAllWindows()
