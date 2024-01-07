import cv2

img = cv2.imread('./image/cat.jpg')

#resize
size_img = cv2.resize(img, (600, 480))

#draw rectangle => cv2.rectangle(image, start, end, color, weight)
cv2.rectangle(size_img, (300, 100), (500, 200), (204, 0, 102), 5) # purple
cv2.rectangle(size_img, (330, 130), (470, 170), (127, 0, 255), -1) # pink


cv2.imshow('Output', size_img)
cv2.waitKey(0)

cv2.destroyAllWindows()