import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./image/noise.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


kernel = np.ones((5,5), np.float32) / 25

ori = cv2.cvtColor(gray, cv2.COLOR_BGR2RGB)

#filter2D
filter2D = cv2.filter2D(gray, -1, kernel)
filter2D = cv2.cvtColor(filter2D, cv2.COLOR_BGR2RGB)

#blur
blur = cv2.blur(gray, (5,5))
blur = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)

#median
median = cv2.medianBlur(gray, 5)
median = cv2.cvtColor(median, cv2.COLOR_BGR2RGB)

#gaussian blur
gauss = cv2.GaussianBlur(gray,(5,5),5)
gauss = cv2.cvtColor(gauss, cv2.COLOR_BGR2RGB)

images = [ori, filter2D, blur, median, gauss]
titles = ["ORIGINAL", "FILTER 2D", "MEAN", "MEDIAN", "GAUSSIAN"]

for i in range(len(images)):
    plt.subplot(2,3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
