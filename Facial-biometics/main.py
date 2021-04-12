import dlib
import cv2
import numpy as np
import time
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('files/shape_predictor_68_face_landmarks.dat')
image = cv2.imread('images/2.jpg')
image = cv2.resize(image, (int(image.shape[1] * .5), int(image.shape[0] * .5) ))

imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = detector(imageGray)
index =0
name = "ADMIN" #input("WHAT IS YOUR NAME?: ")

while True:
    blackImage = np.zeros_like(image)
    for face in faces:
        x1,y1,x2,y2 = face.left(), face.top(), face.right(), face.bottom()
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.rectangle(blackImage, (x1-20, y1-40), (x2+20, y2+50), (170, 178, 32), 2)
        # Get the list of landmarks on each face
        landmarks = predictor(imageGray, face)
        # Drawing the landmarks
        for landmark in landmarks.parts():
            cv2.circle(image, (landmark.x, landmark.y), 1, (0, 255, 255), -1)
            cv2.circle(blackImage, (landmark.x, landmark.y), 1, (0, 255,0), -1)

        index += 1
        if index % 10 == 0:
            for i in range(10):
                cv2.line(blackImage, (x1 - 15, y2 ), (x2 + 15, y2), (247,155, 1), 5)
                cv2.line(blackImage, (x1 - 15, y2 -10), (x2 + 15, y2 - 10), (247, 155, 1), 5)
                cv2.line(blackImage, (x1 - 15, y2- 20), (x2 + 15, y2 - 20), (247, 155, 1), 5)
                cv2.line(blackImage, (x1 - 15, y2- 30), (x2 + 15, y2 - 30), (247, 155, 1), 5)
                cv2.line(blackImage, (x1 - 15, y2-40), (x2 + 15, y2 - 40), (247, 155, 1), 5)
                cv2.line(blackImage, (x1 - 15, y2 - 50), (x2 + 15, y2 - 50), (247, 155, 1), 5)
                cv2.line(blackImage, (x1 - 15, y2 - 60), (x2 + 15, y2 - 60), (247, 155, 1), 5)
                cv2.line(blackImage, (x1 - 15, y2 - 70), (x2 + 15, y2 - 70), (247, 155, 1), 5)
                cv2.line(blackImage, (x1 - 15, y2 - 80), (x2 + 15, y2 - 80), (247, 155, 1), 5)
                cv2.line(blackImage, (x1 - 15, y2 - 90), (x2 + 15, y2 - 90), (247, 155, 1), 5)
                cv2.line(blackImage, (x1 - 15, y2 - 100), (x2 + 15, y2 - 100), (247, 155, 1), 5)
    if index < 1000:
        cv2.putText(blackImage, "Verifying...",( x1 + 30, y2 + 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    else:
        cv2.putText(blackImage, f"Verified {name}",( x1 + 20, y2 + 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    allImages = np.hstack([image, blackImage])
    cv2.imshow("Face Verification", allImages)
    if cv2.waitKey(1) & 0xFF == 27:
        break


