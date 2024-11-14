#Morphological
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image/CoinNoise.png",0)
thres , result = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)

titles = ["Original","Thresh"]
images = [img,result]

for i in range(len(images)):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],cmap="gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()