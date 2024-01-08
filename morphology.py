import cv2
import numpy as np

img = cv2.imread('./image/coin_noise.jpg')
img = cv2.resize(img, (300,300))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thres, res = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

#dilation => การขนาดพื้นที่
#สร้าง array ประกอบไปด้วย 1 ขนาด 2x2
kernel = np.ones((2,2), np.uint8)
dilation = cv2.dilate(res,kernel,iterations=3)

#erosion
erosion = cv2.erode(res,kernel,iterations=3)

#opening
opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel, iterations=5)


cv2.imshow('ORIGINAL', gray)
cv2.imshow('THRES', res)
cv2.imshow('DILATION', dilation)
cv2.imshow('EROSION', erosion)
cv2.imshow('OPENING', opening)


cv2.waitKey(0)
cv2.destroyAllWindows()
