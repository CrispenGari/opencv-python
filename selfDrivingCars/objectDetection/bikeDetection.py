import cv2
import numpy as np
cap = cv2.VideoCapture("./two_wheeler2.mp4")
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 200)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 150)
fps = cap.get(cv2.CAP_PROP_FPS)
pedestrianCascade = cv2.CascadeClassifier('./files/bike.xml')


while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0,0), None, .5, .5)
    HEIGHT, WIDTH = frame.shape[:2]
    imageGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imageBlack = np.zeros_like(frame)
    pd = pedestrianCascade.detectMultiScale(imageGray, 1.3, 2)

    if len(pd) > 0:
        for x, y, w, h in pd:
            person = frame[y:y+h, x: w + x]
            personSeg = np.zeros_like(person)
            personSeg[:] = (0, 255, 255)
            resultImage = cv2.add(person, personSeg)
            frame[y:y + h, x: w + x] = resultImage
            imageBlack[y:y + h, x: w + x] = resultImage

    for x, y, w, h in pd:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 555, 0), 2)

    if ret:
        allImages = np.vstack([frame, imageBlack])
        cv2.imshow("Bikes Detection", allImages)
    else:
        pass
    if cv2.waitKey(int(1000/fps)) & 0xFF == 27:
        cap.release()
        cv2.destroyAllWindows()
        break