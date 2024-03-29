import cv2
import numpy as np
import utils

faceCascade = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')
paht = "../image/"
filename = "lena.png"

img = cv2.imread(paht+filename)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1, 4)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)


images = [img, imgGray]
titles = ["original", "gray"]
utils.openPlot(images, titles)
