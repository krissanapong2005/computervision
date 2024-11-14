import cv2
#อ่านภาพ
img = cv2.imread("image/cat.jpg",0)
imgresize = cv2.resize(img,(400,400))
cv2.imshow("My Cat",imgresize)

cv2.imwrite("Output.jpg",imgresize)

cv2.waitKey(0)
cv2.destroyAllWindows()