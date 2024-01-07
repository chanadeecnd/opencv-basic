import cv2
import numpy 

img = numpy.zeros([700,700,3])
# img = cv2.imread('./image/night.jpg')
# img_size = cv2.resize(img, (700, 700))

points = []
def click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x, y), 1, (0, 0, 255), -1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img, points[0], points[1], (255, 0, 0), 5)
            points.clear()
            points.append((x,y))
            
        cv2.imshow('output', img)


cv2.imshow('output', img)
cv2.setMouseCallback('output', click)
cv2.waitKey(0)

cv2.destroyAllWindows()