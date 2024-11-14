import cv2
gray_img = cv2.imread("image/gradient.png")
#parametor = image ,threshold value(medien),max value,รูปแบบการแบ่งประเภท
threshold, th1 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY)
threshold, th2 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY_INV)
threshold, th3 = cv2.threshold(gray_img,128,255,cv2.THRESH_TRUNC)
threshold, th4 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO)
threshold, th5 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO_INV)

#result = ผลลัพะ์จากการแปลง

cv2.imshow("Orignal",gray_img)
cv2.imshow("Binary",th1)
cv2.imshow("Binary_inv",th2)
cv2.imshow("TRUNC",th3)
cv2.imshow("TOZERO",th4)
cv2.imshow("TOZERO_INV",th5)
cv2.waitKey(0)
cv2.destroyAllWindows()