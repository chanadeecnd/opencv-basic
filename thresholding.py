import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./image/threshold.jpg')
img = cv2.resize(img, (500,500))

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thres_bin, result_bin = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
thres_bin_in, result_bin_in = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
thres_trunc, result_trunc = cv2.threshold(gray, 128, 255, cv2.THRESH_TRUNC)
thres_2zero, result_2zero = cv2.threshold(gray, 128, 255, cv2.THRESH_TOZERO)
thres_2zero_in, result_2zero_in = cv2.threshold(gray, 128, 255, cv2.THRESH_TOZERO_INV)

r1 = cv2.cvtColor(result_bin, cv2.COLOR_BGR2RGB)
r2 = cv2.cvtColor(result_bin_in, cv2.COLOR_BGR2RGB)
r3 = cv2.cvtColor(result_trunc, cv2.COLOR_BGR2RGB)
r4 = cv2.cvtColor(result_2zero, cv2.COLOR_BGR2RGB)
r5 = cv2.cvtColor(result_2zero_in, cv2.COLOR_BGR2RGB)
# cv2.imshow('gray', gray)
# cv2.imshow('result', result_bin)
images = [r1, r2, r3, r4, r4, r5]
titles = ["GRAY", "BINARY", "BINARY-INVERT", "TRUNC", "TOZERO", "TOZERO-INVERT"]

for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()