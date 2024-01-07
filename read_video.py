import cv2

paht = './video'
video_name = 'person_road'

cap = cv2.VideoCapture(f'{paht}/{video_name}.mp4')


while cap.isOpened():
    # status(boolean), piture
    chk, frame = cap.read() #read piture frame/frame


    if chk:
        #resize
        resize_video = cv2.resize(frame, (640, 480))

        gray_video = cv2.cvtColor(resize_video, cv2.COLOR_BGR2GRAY)

        cv2.imshow('Output', gray_video)

        if cv2.waitKey(1) & 0xFF == ord('e'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()