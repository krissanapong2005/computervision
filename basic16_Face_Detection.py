#face Detection
import cv2

#read image
img = cv2.imread("image/boy.jpg")
img_resize = cv2.resize(img,(600,400))

#read flie for classification
face_cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")

gray_img = cv2.cvtColor(img_resize,cv2.COLOR_BGR2GRAY)

#classify face
#scalfactor = defult 1.1
#minNeighber = defult 3
face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors=3)

#show position of face
for (x,y,w,h) in face_detect:
    cv2.rectangle(img_resize,(x,y),(x+w,y+h),(0,255,0),thickness=5)

#show image
#cv2.imshow("Original",img_resize)
cv2.imshow("Result",img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()