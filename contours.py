import cv2

img = cv2.imread('./image/ant.jpg')
img = cv2.resize(img, (500,500))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thres, res = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

contours, hiera = cv2.findContours(res, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

print(len(contours))

cv2.imshow('output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()