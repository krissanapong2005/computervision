import cv2

img = cv2.imread("D:\ComputerVision\image\cat.jpg")

imgresize = cv2.resize(img,(700,700))

#circle(ภาพ , ตำแหน่งจุดศูนย์กลางวงกลม(x,y) , รัศมี , สี ,ความหนา)
cv2.circle(imgresize,(200,200),70,(0,0,255),7)




cv2.imshow("Output",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()