import cv2

def draw_squre(frame, contours):
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour)>90:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
    

def draw_contours(frame, thres):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 1)
    thres, res = cv2.threshold(blur, thres, 255, cv2.THRESH_BINARY)
    contours, h = cv2.findContours(res, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # cv2.drawContours(frame, contours, -1, (0,255,0), 2)
    draw_squre(frame, contours)
    return frame


cap = cv2.VideoCapture('./video/person_walk.mp4')
while cap.isOpened():
    chk, frame = cap.read()
    frame = cv2.resize(frame, (600,500))
    if chk:
        con = draw_contours(frame,150)
        cv2.imshow('output', con)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()