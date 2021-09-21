# What is this?

This is a simple Machine Learning open computer version 
application that detects eyes from a webcam in real time using 
`haarcascade_eye_tree_eyeglasses.xml` from opencv.

### App capabilities.
This app is cappable of:
* detecting eyes in real time from a webcam
* draw rectangle around each eye detected from the webcam
* put text label `Eye` under a rectangle to show that this is an eye

### First of all install `opencv-python` and `numpy`:
#### You can install `opencv-python` by running:

`python -m pip install opencv-python`

#### You can install `numpy` by running:
`python -m pip install numpy`

### Alternatively, you can install all of them by pasting the following code on your `main.py` and run it.

````buildoutcfg
try:
    import cv2
    import numpy as np
except ImportError as e:
    from pip._internal import main as install
    packages = ["numpy", "opencv-python"]
    for package in packages:
        install(["install", package])
finally:
    pass
````

### After installation of all the packages then we are ready to go.

#### step 1:
Capture the webcam from a computer
````buildoutcfg
capture = cv2.VideoCapture(0)
````
#### step 2:
Load the haarcascade_eye_tree_eyeglasses
````buildoutcfg
eyesCasecade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
````
#### step 3:
Get the images from a video using a `while` loop
````buildoutcfg
while capture.isOpened():
    ret, video = capture.read()
````
#### step 4:
Convert each image to gray scale so that detection will be easy and accurate for the haarcascade_eye_tree_eyeglasses
and start detecting eyes
````buildoutcfg
gimage_gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
        eyes = eyesCasecade.detectMultiScale(image_gray, 1.1)
````
Now we have all the point to draw the rectangle of eyes to our original image.

#### step 5:
Loop through eyes array and draw a rectangle around each 
eye that is going to be detected. Draw the text 
as was as a rectangle that is filled with green color
that bounds the text
and show the image.
````buildoutcfg
for (x, y, w, h) in  eyes:
    final_image = cv2.rectangle(video, (x, y), (x+w, y+h), (0, 255, 0), 2)
    final_image = cv2.rectangle(final_image, (x-1, y+h+15),(x+30, y+h), (0, 255, 0), -1)
    final_image = cv2.putText(final_image, "Eye", (x, y+h+12), cv2.FONT_HERSHEY_PLAIN, 1,(255, 0, 0), 1)
    cv2.imshow("Eyes Detector", final_image)
````
Now everything is ready we are only left with showing images in a loop
#### step 6:
````buildoutcfg
key = cv2.waitKey(1)
if key & 0xFF == ord('q') or key == 27:
    capture.release()
    return cv2.destroyAllWindows()
````

### All code in one place: `main.py`

````buildoutcfg

try:
    import cv2
    import numpy as np
except ImportError as e:
    from pip._internal import main as install
    packages = ["numpy", "opencv-python"]
    for package in packages:
        install(["install", package])
finally:
    pass
def detectEyeGlasses():
    capture = cv2.VideoCapture(0)
    eyesCasecade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
    while capture.isOpened():
        ret, video = capture.read()
        # convert the video to gray_scale
        image_gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
        eyes = eyesCasecade.detectMultiScale(image_gray, 1.1)
        for (x, y, w, h) in  eyes:
            final_image = cv2.rectangle(video, (x, y), (x+w, y+h), (0, 255, 0), 2)
            final_image = cv2.rectangle(final_image, (x-1, y+h+15),(x+30, y+h), (0, 255, 0), -1)
            final_image = cv2.putText(final_image, "Eye", (x, y+h+12), cv2.FONT_HERSHEY_PLAIN, 1,(255, 0, 0), 1)
            cv2.imshow("Eyes Detector", final_image)
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q') or key == 27:
            capture.release()
            return cv2.destroyAllWindows()
    return cv2.destroyAllWindows()
detectEyeGlasses()
````

### Where to find the haarcascade_eye_tree_eyeglasses cascade classifier?
You will find it on the opencv github [here](https://github.com/opencv/opencv/edit/master/data/haarcascades/)
 
### Why this simple App?
This app was build for practise purposes.
