# What is this color Detection App?

This is a simple open computer vision `opencv-python` that filters all the color from an image using track bars and left us with a color we want.

### Demo

![image-demo](https://github.com/CrispenGari/Open-Computer-Vision-Chapter-7/blob/main/bandicam%202021-01-07%2018-52-50-383.jpg)

### App capabilities.

This app is cappable of:

- detecting color from images
- stack images together

### First of all install `opencv-python` and `numpy`:

### How to detect color from an image?

#### Step 1:

Install packages that we will be using which are:

- `numpy`
- `opencv-python`

#### You can install `opencv-python` by running:

#### To install `opencv-python` run:
`python -m pip install opencv-python`

#### You can install `numpy` by running:

##### To install `numpy` by run:
`python -m pip install numpy`

Alternatively, you can install all of them by pasting the following code on your `main.py` and run it.

```
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
```

#### Step 2:

Import `imageStacks` function from the utils folder in the `stackimages.py` file for stacking images together as 1.

```
from utils.stackimages import stackImages
```

#### Step 3:

Create a new window which will hold all the track bars as well as an empty function that does nothing. Add 6 track bars on the top of the `namedWindow` as follows

```
def empty(args):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 600, 200)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 131, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

```

#### Step 4:

- Get the position of the track bars in read time using a `while True` loop
- read the image and convert it to `hsv` color using the `cv2.cvtColor()` function
- create a mask images using the values of the track bars `lower` and `upper` arrays of track bars
- create a result image which will be the image result after comparison of the 2 images using the `and` bitwise operation from opencv-python
- stack images together in the way you want

```
# Track Bars
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 600, 200)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 131, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)
while True:
    og_image = cv2.imread("images/car1.jpg")
    hsv_image = cv2.cvtColor(og_image, cv2.COLOR_BGR2HSV)
    # Get the positions of the TrackBars
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    # print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    # mask the image
    mask = cv2.inRange(hsv_image, lower, upper)
    imgResult = cv2.bitwise_and(og_image, og_image, mask=mask)
    image_label = cv2.putText(image_black, "RED COLOR", (200, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), cv2.LINE_4)
    imageStack = stackImages(.5, ([image_label, og_image , hsv_image], [ mask, imgResult, image_black]))
    cv2.imshow("Color Images", imageStack)
    # cv2.resizeWindow("Color Images", 600, 600)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q') or key == 27:
        break
```

#### All the code in one file `main.py`:

The whole code for the application is as follows:

- I've created a function that wraps all the code and when called it runs the application.
- Note that the track bars are on their window and they can be adjusted to find the suitable color

```
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

# Import the image Stack function
from utils.stackimages import stackImages
def empty(args):
    pass

image_black = np.zeros([500, 500, 3], dtype=np.uint8)
def detectColor():
    # Track Bars
    cv2.namedWindow("TrackBars")
    cv2.resizeWindow("TrackBars", 600, 200)
    cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
    cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
    cv2.createTrackbar("Sat Min", "TrackBars", 131, 255, empty)
    cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
    cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
    cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)
    while True:
        og_image = cv2.imread("images/car1.jpg")
        hsv_image = cv2.cvtColor(og_image, cv2.COLOR_BGR2HSV)
        # Get the positions of the TrackBars
        h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
        h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
        s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
        s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
        v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
        v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
        # print(h_min, h_max, s_min, s_max, v_min, v_max)
        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        # mask the image
        mask = cv2.inRange(hsv_image, lower, upper)
        imgResult = cv2.bitwise_and(og_image, og_image, mask=mask)
        image_label = cv2.putText(image_black, "RED COLOR", (200, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), cv2.LINE_4)
        imageStack = stackImages(.5, ([image_label, og_image , hsv_image], [ mask, imgResult, image_black]))
        cv2.imshow("Color Images", imageStack)
        # cv2.resizeWindow("Color Images", 600, 600)
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q') or key == 27:
            break
    return
detectColor()

```

That's all

#### What is next?

- Shape Detection

[Next](https://github.com/CrispenGari/Open-Computer-Vision-Chapter-8) || [Previous](https://github.com/CrispenGari/Open-Computer-Version-Chapter-6)
