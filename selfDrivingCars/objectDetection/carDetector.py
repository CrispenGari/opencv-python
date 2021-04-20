import cv2
import numpy as np
cap = cv2.VideoCapture("../speedDetection/free.mp4")
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 200)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 150)
fps = cap.get(cv2.CAP_PROP_FPS)
carCascade = cv2.CascadeClassifier('./files/car.xml')


while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0,0), None, .4, .4)
    HEIGHT, WIDTH = frame.shape[:2]
    imageGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imageBlack = np.zeros_like(frame)
    cars = carCascade.detectMultiScale(imageGray, 2, 1)
    # I want to detect cars that ain't far
    for x, y, w, h in cars:
        if HEIGHT * .4 <= y:
            car = frame[y:h+y, x: x+w]
            finalCar = car.copy()
            finalCar2 = car.copy()

            carSeg1 = np.zeros_like(car)
            carSeg2 = np.zeros_like(car)
            carSeg1[:] = (0, 0, 255)
            carSeg2[:] = (0, 255, 0)
            finalCar = cv2.addWeighted(finalCar, 0.4, carSeg1, .6, 1, 1)
            finalCar2 = cv2.addWeighted(finalCar2, 0.4, carSeg2, .6, 1, 1)
            frame[y:h + y, x: x + w] = finalCar
            imageBlack[y:h + y, x: x + w] = finalCar2
            # cv2.imshow("", finalCar)
    if ret:
        allImages = np.vstack([frame, imageBlack])
        cv2.imshow("Car Detection", allImages)
    else:
        pass
    if cv2.waitKey(int(1)) & 0xFF == 27:
        cap.release()
        cv2.destroyAllWindows()
        break
