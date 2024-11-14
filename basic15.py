import cv2
import numpy as np


while True:
    img = cv2.imread("image/ball2d.jpg")
    img = cv2.resize(img,(400,400))


    #ช่วงของสี BGR
    #green
    upper = np.array([96,255,123])
    lower = np.array([4,105,7])

    #blue
    #upper = np.array([253,231,136])
    #lower = np.array([161,50,2])

    #purple
    #upper = np.array([255,143,244])
    #lower = np.array([179,9,128])

    mask = cv2.inRange(img,lower,upper)
    result = cv2.bitwise_and(img,img,mask=mask) 



    if cv2.waitKey(0) & 0xFF == ord("e"):
        break
    
    cv2.imshow("Original",img)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",result)



cv2.destroyAllWindows()
