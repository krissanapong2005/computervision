import cv2

img = cv2.imread("D:\ComputerVision\image\cat.jpg")

imgresize = cv2.resize(img,(700,700))

#วาดข้อความบนภาพ
#  putText(ภาพ, ข้อความ, พิกัดที่จะแสดงข้อความ (x,y),front,ขนาดข้อความ,สี,ความหนา)
cv2.putText(imgresize,"CAT",(570,100),cv2.FONT_HERSHEY_COMPLEX,1.8,(0,0,255),cv2.LINE_4)



cv2.imshow("Output",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()