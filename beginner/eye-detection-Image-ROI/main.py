

try:
    import cv2
    import numpy as np
except ImportError as e:
    packages = ["opencv-python", "numpy"]
    from pip._internal import main as install
    for package in packages:
        install(["install", package])
finally:
    pass

from stackimages import stackImages

originalImage = cv2.imread("person_1.jpg")
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
imageDrawing = originalImage.copy()
whiteImage = np.zeros((512, 512, 3), np.uint8)
eyeCascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
eyes_detected = []
def detectEyes():
    eyes = eyeCascade.detectMultiScale(grayImage)
    if len(eyes):
        for x,y, w, h in eyes:
            imageROI = originalImage[y: y + h,x: x + w]
            eyes_detected.append(imageROI)
            cv2.rectangle(imageDrawing, (x, y), (x+w, y+h), (0,255, 0), 2)
    return
def showStackedImages():
    detectEyes()
    stackedImage = stackImages(.5, [[originalImage,grayImage, imageDrawing], [eyes_detected[0], eyes_detected[1], whiteImage]])
    cv2.imshow("Eye Detection Image ROI",stackedImage)
    cv2.waitKey(0)
    return
showStackedImages()