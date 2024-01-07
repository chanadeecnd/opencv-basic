import cv2

img = cv2.imread('./image/cat.jpg')

#resize
size_img = cv2.resize(img, (600, 480))

font = cv2.FONT_HERSHEY_SIMPLEX

#put text=> cv2.putText(image, text, point, font, font size, color, weight)
cv2.putText(size_img, 'Hello World', (15,30), font, 1, (255, 0, 0), cv2.LINE_4)

#show
cv2.imshow('Output', size_img)
cv2.waitKey(0)

cv2.destroyAllWindows()