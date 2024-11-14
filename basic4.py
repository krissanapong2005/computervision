#เปิดVideo by OpenCV
import cv2


cap = cv2.VideoCapture("image/video_test.mp4")
#capresize = cv2.resize(cap,(400,400))

while (cap.isOpened()):
    check, frame = cap.read() #รับภาพจากกล้อง frame to frame
    if check == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #ทำวิดีโอเกรย์สเกล
        cv2.imshow("output",gray)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()