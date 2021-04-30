import cv2
import numpy as np

catFaceCascade = cv2.CascadeClassifier('haarcascade_frontal_catface.xml')

cap = cv2.VideoCapture('cats/test2.mov')
fps = cap.get(cv2.CAP_PROP_FPS)
while cap.isOpened():
    _, image = cap.read()
    image = cv2.resize(image, (0, 0), None, .8, .8)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cats = catFaceCascade.detectMultiScale(gray)
    for x, y, w, h in cats:
        cv2.rectangle(image, (x, y), (x+w, h+h), (0, 255, 0), 2)
    cv2.imshow('Cat Face', image)
    if cv2.waitKey(int(1000/fps)) & 0xFF == 27:
        cap.release()
        cv2.destroyAllWindows()
        break
