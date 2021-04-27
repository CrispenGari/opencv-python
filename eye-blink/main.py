import cv2
import numpy as np
eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
countBlink = 0
while cap.isOpened():
    _ret, frame = cap.read()
    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blackImage = np.zeros_like(frame)
    faces = faceCascade.detectMultiScale(grayImage, 1.3, 5)
    for x, y, w, h in faces:
        blinking = True
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        face = frame[y:y+h, x:x+w]
        # Detect an eye from a face
        eyes = eyeCascade.detectMultiScale(cv2.cvtColor(face, cv2.COLOR_BGRA2GRAY))
        for ex, ey, ew, eh in eyes:
            blinking = False
            cv2.rectangle(face, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)
        if blinking == True:
            countBlink += 1
            print(f"YOU HAVE BLINKED {countBlink} time(s)")
        else:
            print("You are not blinking")
    cv2.imshow("Eye Blink", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        cap.release()
        cv2.destroyAllWindows()

