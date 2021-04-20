import cv2
import dlib
import math, time

cap = cv2.VideoCapture("free.mp4")
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 200)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 150)
fps = cap.get(cv2.CAP_PROP_FPS)
carCascade = cv2.CascadeClassifier('myhar.xml')


frameCounter = 0
while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0,0), None, .5, .5)
    imageGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = carCascade.detectMultiScale(imageGray, 2)


    start_time = time.time()
    frameCounter = frameCounter + 1

    carIDtoDelete = []
    if len(cars) > 0:
        print(cars)
    if ret:
        cv2.imshow("Speed Tracking", frame)
    else:
        pass
    if cv2.waitKey(int(1) )== 27:
        cap.release()
        cv2.destroyAllWindows()
        break
