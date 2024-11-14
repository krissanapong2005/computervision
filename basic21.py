#eye and face detection from video
import cv2

cap = cv2.VideoCapture("image/Mark.mp4")

#read flie for classification
face_cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("Detect/haarcascade_eye_tree_eyeglasses.xml")

while (cap.isOpened()):
    check , frame = cap.read()
    if check == True:
        gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor=1.2,minNeighbors=5)
        eye_detect = eye_cascade.detectMultiScale(gray_img,1.2,5)
        for (x,y,w,h) in face_detect:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=5)
            for (ex,ey,ew,eh) in eye_detect:
                cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(255,0,0),thickness=5)
        cv2.imshow("Output",frame)
        
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()