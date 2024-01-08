import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread('./image/ball_color.jpg')
img = cv2.resize(img, (400, 400))

# while True:

# color range (b,g,r)
lower = numpy.array([7, 104, 0])
upper = numpy.array([119, 253, 110])

# mask => binary
mask = cv2.inRange(img, lower, upper)

result = cv2.bitwise_and(img, img, mask=mask)

img_plt = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
mask_plt = cv2.cvtColor(mask,cv2.COLOR_BGR2RGB)
result_plt = cv2.cvtColor(result,cv2.COLOR_BGR2RGB)

cv2.imshow('Original', img)
cv2.imshow('Mask', mask)
cv2.imshow('Result', result)
plt.imshow(img_plt)
plt.show()
cv2.waitKey(0)

cv2.destroyAllWindows()