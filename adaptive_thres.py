'''
cv2.adaptiveThreshold(1,2,3,4,5,6)
1. ภาพ grayscale
2. maxValue
3. adaptive method
4. threshold type
5. box size # ยิ่งเยอะความคมชัดของภาพยิ่งมากขึ้น
6. C
'''

import cv2

img = cv2.imread('./image/earth.jpg')
img = cv2.resize(img, (400,400))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#normal threshold
thres_bin, result_bin = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

# adaptive mean
result_mean = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 1)

# adaptive gaussian
result_gauss = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 1)

cv2.imshow('output',gray)
cv2.imshow('THRES-NORMAL',result_bin)
cv2.imshow('ADAP_MEAN', result_mean)
cv2.imshow('ADAP_GAUSS', result_gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()