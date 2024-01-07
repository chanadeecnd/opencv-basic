import cv2
import numpy

while True:
    img = cv2.imread('./image/ball_color.jpg')

    #green
    # upper = numpy.array([96, 255 ,123])
    # lower = numpy.array([4, 105, 7])

    #blue
    upper = numpy.array([253, 231, 136])
    lower = numpy.array([161, 50, 2])

    #purple
    # upper = numpy.array([255, 143, 244])
    # lower = numpy.array([179, 9, 128])
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break