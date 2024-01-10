import cv2
import numpy as np
import utils


def getContours(img):
    contours, hier = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        cv2.drawContours(imgContours, cnt, -1, (255,0,0), 3)
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
        
        objCor = len(approx)
        x, y, w, h = cv2.boundingRect(approx)
        if objCor == 3:
            objectType = "Tri"
        elif objCor == 4:
            aspRation = w/float(h)
            if aspRation > 0.95 and aspRation < 1.05:
                objectType = "Square"
            else:
                objectType = "Reatangle"
        elif objCor > 4:
            objectType = "Circle"
        else:
            objectType = "None"
        cv2.rectangle(imgContours, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(imgContours,objectType,(x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)

paht = "../image/"
filename = "shape.jpg"

kernel = np.ones((2,2), np.uint8)

img = cv2.imread(paht+filename)
img = cv2.resize(img, (500,500))

#result image
imgContours = img.copy()

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7,7), 1)
img_canny = cv2.Canny(img_blur, 50, 50)
img_dilation = cv2.dilate(img_canny, kernel, iterations=2)
img_closing = cv2.morphologyEx(img_dilation, cv2.MORPH_CLOSE, kernel, iterations=5)
getContours(img_closing)

# Display image
images = [img, img_gray, img_blur, img_canny, img_dilation, img_closing, imgContours]
titles = ["original", "gray", "blur", "canny", "dilate", "Close","contours"]
utils.openPlot(images, titles)

cv2.waitKey(0)
