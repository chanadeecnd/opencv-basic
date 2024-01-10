import cv2
import math
import matplotlib.pyplot as plt

def openPlot(img, title):
    images = [cv2.cvtColor(image, cv2.COLOR_BGR2RGB) for image in img]
    num_img = len(images)
    num_cols = math.ceil(math.sqrt(num_img))
    num_rows = math.ceil(num_img/num_cols)

    for i in range(num_img):
        plt.subplot(num_rows, num_cols, i+1)
        plt.imshow(images[i])
        plt.title(title[i])
        plt.xticks([]), plt.yticks([])

    plt.tight_layout()
    plt.show()
