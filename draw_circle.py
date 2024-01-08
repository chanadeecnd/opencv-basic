import cv2

img = cv2.imread('./image/cat.jpg')

#resize
size_img = cv2.resize(img, (600, 480))

#draw circle => cv2.circle(image, center, radius, color, weight)
cv2.circle(size_img, (300, 240), 100, (0,0,255), 5)

cv2.imshow('Output', size_img)
cv2.waitKey(0)

cv2.destroyAllWindows()
