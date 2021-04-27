# EYE-BLINKING
* This is a simple program that detects and count how many times `eyes` has been blinked with the help of `haar_cascades` from opencv.

<p align="center">
<img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
<img src="https://img.shields.io/static/v1?label=package&message=opencv&color=yellow"/>
<img src="https://img.shields.io/static/v1?label=package&message=numpy&color=blueviolet"/>
</p>

### Demo

<p align="center">
<img src="https://github.com/CrispenGari/Opencv-Python/blob/main/eye-blink/ey.jpg" alt="demo" align="center"/>
</p>

## Implementaion
* Read the image
* Create a grayscale image from the original image
* detect the face and create an image **R**egion **O**f **I**ntrest (ROI) of the face
* convert the face to gray scale
* detect the eyes from the face
* if the eyes are closed then the person blink count and print to the console.

### `Code` 
```python
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
        cv2.destr
```