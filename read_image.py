# read -> rgb to gray -> export image

import cv2

paht = './image'
filename = 'cat'

img = cv2.imread(f'{paht}/{filename}.jpg') # array 3 dimention

#resize
resize_img = cv2.resize(img, (400, 400))

#gray scale
gray_img = cv2.cvtColor(resize_img, cv2.COLOR_RGB2GRAY)


#show image
cv2.imshow('Output', gray_img)
cv2.waitKey(0)

#export image imwrite(paht, image)
cv2.imwrite(f'{paht}/{filename}_cv.jpg', gray_img)

cv2.destroyAllWindows()