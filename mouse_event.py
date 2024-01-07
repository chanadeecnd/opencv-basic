import cv2

img = cv2.imread("./image/natural.jpg")
name = "output"
cv2.namedWindow(name)
# mouse event
size = (600, 480)
size_img = cv2.resize(img, size)
def clickPosition(event, x, y, flags, param):
    text = '' # put text onclick
    color = () # color text
    #left click
    if event == cv2.EVENT_LBUTTONDOWN:
        text = f'{x},{y}'
        color = (0, 0, 255)
    # right click
    elif event == cv2.EVENT_RBUTTONDOWN:
        blue = int(size_img[y,x,0])
        green = int(size_img[y,x,1])
        red = int(size_img[y,x,2])
        text = f'{blue},{green},{red}'
        color = (blue ,green, red)
    
    #posiotion text (x, y)
    if x > 460:
        x -= 100
    if y < 30:
        y += 20

    text_location = (x,y)
    cv2.putText(size_img, text, text_location, cv2.FONT_HERSHEY_SIMPLEX, .8, color, cv2.LINE_4)
    cv2.imshow(name, size_img)

cv2.setMouseCallback(name, clickPosition)

cv2.imshow(name, size_img)
cv2.waitKey(0)
cv2.destroyAllWindows()