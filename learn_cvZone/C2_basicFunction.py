import cv2
import utils
import numpy as np

kernel = np.ones((5,5), np.uint8)

img = cv2.imread('../image/cat.jpg')
img = cv2.resize(img, (600,600))

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlure = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img,100,100)
imgDilation = cv2.dilate(imgCanny,kernel, iterations=1)
imgEros = cv2.erode(imgDilation, kernel, iterations=1)


images = [img, imgGray, imgBlure, imgCanny, imgDilation, imgEros]
titles = ["ORIGINAL", "GRAY", "BLUR", "CANNY", "DILATION", "EROSION"]
utils.openPlot(images, titles)
