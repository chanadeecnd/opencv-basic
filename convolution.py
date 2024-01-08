import cv2
import numpy as np
import matplotlib.pyplot as plt

kernel3 = np.ones((3,3), np.float32) / 9
kernel5 = np.ones((5,5), np.float32) / 25

img = cv2.imread('./image/noise.jpg', 0)
img = cv2.resize(img, (400, 400))
fil1 = cv2.filter2D(img, -1, kernel3)
fil2 = cv2.filter2D(img, -1, kernel5)

ori = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
res_fil1 = cv2.cvtColor(fil1, cv2.COLOR_BGR2RGB)
res_fil2 = cv2.cvtColor(fil2, cv2.COLOR_BGR2RGB)

titles = ["ORIGINAL", "CONVOLUTION 3x3", "CONVOLUTION 5x5"]
images = [ori, res_fil1, res_fil2]

for i in range(len(images)):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()