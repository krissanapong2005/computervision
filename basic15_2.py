import cv2
import numpy as np

while True:
    img = cv2.imread("image/ball2d.jpg")
    
    if img is None:
        print("Error: Could not read image.")
        break
    
    # Resize the image to 400x400 pixels
    img = cv2.resize(img, (400, 400))
    
    # Define the BGR color range for masking
    # Uncomment the desired color range

    # Green
    upper = np.array([96, 255, 123])
    lower = np.array([4, 105, 7])

    # Blue
    # upper = np.array([253, 231, 136])
    # lower = np.array([161, 50, 2])

    # Purple
    # upper = np.array([255, 143, 244])
    # lower = np.array([179, 9, 128])

    # Create a mask based on the color range
    mask = cv2.inRange(img, lower, upper)
    
    # Apply the mask to get the result
    result = cv2.bitwise_and(img, img, mask=mask)
    
    # Display the images
    cv2.imshow("Original", img)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)
    
    # Wait for the key press and break the loop if 'e' is pressed
    if cv2.waitKey(0) & 0xFF == ord("e"):
        break

cv2.destroyAllWindows()
