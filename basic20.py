#detect eye and face
import cv2

img = cv2.imread("image/girl.jpg")

face_cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("Detect/haarcascade_eye_tree_eyeglasses.xml")

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_detect = face_cascade.detectMultiScale(gray_img,1.1,4)

eye_detect = eye_cascade.detectMultiScale(img,1.1,4)

for (x,y,w,h) in face_detect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=5)
    for (ex,ey,ew,eh) in eye_detect:
        cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(255,0,0),thickness=5)

cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()