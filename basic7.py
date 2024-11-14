import cv2

img = cv2.imread("D:\ComputerVision\image\cat.jpg")

imgresize = cv2.resize(img,(700,700))

#rectangle(ภาพ , มุมที่ 1 (บนซ้าย) , มุมที่ 2 (ล่างขวา) , สี ,ความหนา)

cv2.rectangle(imgresize,(100,100),(500,500),(0,0,255),5)



cv2.imshow("Output",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()