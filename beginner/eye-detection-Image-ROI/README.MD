

# EYE DETECTION IMAGE-ROI
This is a simple `opencv` application that detects eyes using a `cascade-classifier` from `open-cv` and create Image ROI for each eye detected and then show the image on a stacked image Frame.


## DEMO
![alt-text](https://github.com/CrispenGari/eye-detection-Image-ROI/blob/main/bandicam%202021-01-24%2016-29-32-657.jpg)

## This app is using
* opencv 
* numpy
* `haarcascade_eye_tree_eyeglasses.xml`

## Installation of `opencv-python` and `numpy`
To install `opencv` and `numpy` run the following:

````shell
$pip install opencv-python
````

```shell
$pip install numpy
```

## Alternatively, you can install it as follows

Copy the following code and paste in the `main.py` file and run it. All opencv and nmpy packages will be installed as

```
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
```

## 1. Declare all global variables

```
# Importing stackImages Function

from stackimages import stackImages

originalImage = cv2.imread("person_1.jpg")
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
imageDrawing = originalImage.copy()
whiteImage = np.zeros((512, 512, 3), np.uint8)
eyeCascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
eyes_detected = []

```

## 2. Loading the cascade classifier for eyes detection

```
eyeCascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
```

## 3. Define a function that detects eyes on images

```
def detectEyes():
    eyes = eyeCascade.detectMultiScale(grayImage)
    if len(eyes):
        for x,y, w, h in eyes:
            imageROI = originalImage[y: y + h,x: x + w]
            eyes_detected.append(imageROI)
            cv2.rectangle(imageDrawing, (x, y), (x+w, y+h), (0,255, 0), 2)
    return
```

## 4. Define a function that shows stacked images 
Note that the stackImages function is coming from `stackimages.py` file so you need to import it.

```
def showStackedImages():
    detectEyes()
    stackedImage = stackImages(.5, [[originalImage,grayImage, imageDrawing], [eyes_detected[0], eyes_detected[1], whiteImage]])
    cv2.imshow("Eye Detection Image ROI",stackedImage)
    cv2.waitKey(0)
    return
showStackedImages()
```

### All Code in one file `main.py`

```


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
```

## What's Next?
* Mathematic operations on Images

[Next]() || [Previous]()
