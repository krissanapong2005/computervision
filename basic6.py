import cv2

img = cv2.imread("D:\ComputerVision\image\cat.jpg")

imgresize = cv2.resize(img,(700,700))


#วาดเส้นตรง
#line (ภาพ, จดเริ่มต้น(x,y), จุดสุดท้าย(x,y) สี(BGR) , ความหนา)

cv2.arrowedLine(imgresize,(0,0),(100,100),(0,255,0),5)
cv2.arrowedLine(imgresize,(300,200),(100,100),(255,0,0),5)



cv2.imshow("Output",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()