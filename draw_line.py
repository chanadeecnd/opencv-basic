import cv2

paht = './image'
filename = 'cat'
width = 640
height = 480
size = (width, height)

img = cv2.imread(f'{paht}/{filename}.jpg')

#resize
size_img = cv2.resize(img, size)

#draw line => line( image, start(x, y), end(x, y), color(bgr), weight)
cv2.line(size_img, (40,400), (600,400), (33, 33, 247), 3) # red line
cv2.arrowedLine(size_img, (40,350), (600,350), (255, 51, 51), 5) # blue line with arrow

#show
cv2.imshow('Output', size_img)
cv2.waitKey(0)

cv2.destroyAllWindows()
