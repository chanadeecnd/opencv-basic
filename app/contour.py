import cv2
import numpy as np
import utils

paht = '../image/'
filename = 'squares.jpg'

kernel = np.ones((3,3))

def getContours(img):
    global images, titles, imgContours
    img_blur = cv2.GaussianBlur(img, (5,5), 1)
    img_canny = cv2.Canny(img_blur, 50, 200)
    img_dilation = cv2.dilate(img_canny, kernel, iterations=3)
    img_eros = cv2.erode(img_dilation, kernel, iterations=4)
    con, hier = cv2.findContours(img_eros, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    cv2.drawContours(imgContours, con, -1, (255,0,0), 3)
    images = images + [img_eros, imgContours]
    titles = titles + ["Binary", "Contours"]

img = cv2.imread(paht+filename)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgContours = img.copy()

# getContours(img)
img_blur = cv2.GaussianBlur(img_gray, (5,5), 1)
img_canny = cv2.Canny(img_blur, 50, 200)
img_dilation = cv2.dilate(img_canny, kernel, iterations=1)
# img_eros = cv2.erode(img_dilation, kernel, iterations=4)

#contours
con, hier = cv2.findContours(img_dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cnt in con:
    cv2.drawContours(imgContours, cnt, -1,(0,0,255),2)

    #moment
    # cnt = con[0]
    M = cv2.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv2.circle(imgContours,(cx,cy),3,(0,255,0),-1)
    print(cx,cy)

    #area
    area = cv2.contourArea(cnt)
    print(area)

    #arcLenght
    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
    print(len(approx))

images = [img, img_canny, img_dilation,imgContours]
titles = ["Original", "canny", "dialtion", "Contours"]
utils.openPlot(images, titles)

