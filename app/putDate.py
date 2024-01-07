import cv2
import datetime as dt

def getTime():
    return dt.datetime.now().strftime('%H:%M:%S')

def getDate():
    return dt.datetime.now().strftime('%d/%m/%Y')

def add_date_time(image):
    date_time = f'{getDate()} {getTime()}'
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_size = cv2.LINE_4
    color = (51, 255, 51) # green (BGR)
    cv2.putText(image, date_time, (15, 30), font, .8, color, font_size)

def showImg(paht: str, size: tuple, name: str):
    try:
        img = cv2.imread(paht)
        #resize
        size_img = cv2.resize(img, size)
        add_date_time(size_img)
        #show
        cv2.imshow(name, size_img)
        cv2.waitKey(0)

        cv2.destroyAllWindows()
    except cv2.error as e:
        print(f"cv2 error: {e}")

def showVideo(paht: str, size: tuple, name: str):
    cap = cv2.VideoCapture(paht)

    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            #resize
            size_video = cv2.resize(frame, size)
            add_date_time(size_video)
            #show
            cv2.imshow(name, size_video)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    
    cap.release()
    cv2.destroyAllWindows()




# showImg('./image/cat.jpg', (600, 480), 'Output')
showVideo('./video/person_walk.mp4', (600, 480), 'Output')
