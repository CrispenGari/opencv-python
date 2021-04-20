import cv2
import numpy as np
cap = cv2.VideoCapture("./bus1.mp4")
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 200)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 150)
fps = cap.get(cv2.CAP_PROP_FPS)
busCascade = cv2.CascadeClassifier('./files/bus.xml')

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0,0), None, .5, .5)
    HEIGHT, WIDTH = frame.shape[:2]
    imageGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imageBlack = np.zeros_like(frame)
    buses = busCascade.detectMultiScale(imageGray, 1.3, 2)

    if len(buses) > 0:
        for x, y, w, h in buses:
            bus = frame[y:y+h, x: w + x]
            busSeg = np.zeros_like(bus)
            busSeg[:] = [128, 0, 128]
            resultImage = cv2.add(bus, busSeg)
            frame[y:y + h, x: w + x] = resultImage
            imageBlack[y:y + h, x: w + x] = resultImage
    for x, y, w, h in buses:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 555, 0), 2)

    if ret:
        allImages = np.vstack([frame, imageBlack])
        cv2.imshow("Buses Detection", allImages)
    else:
        pass
    if cv2.waitKey(int(1000/fps)) & 0xFF == 27:
        cap.release()
        cv2.destroyAllWindows()
        break