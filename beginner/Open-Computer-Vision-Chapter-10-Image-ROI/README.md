
# IMAGE ROI 
Known as `Region of Intrest` from an image. Sometimes we want to get certain parts of an image. We can use `numpy` indexing to get the image that we are intrested in
from this example we are going to grab the face of the images `avatar.jpg` and put the face on the left top conner of the original image and display the original image.


## DEMO
![alt-text](https://github.com/CrispenGari/Open-Computer-Vision-Chapter-10-Image-ROI/blob/main/bandicam%202021-01-24%2014-40-01-910.jpg)

## First we need to install `opencv-python`

Run in the file `main.py`
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
OR for `opencv`:
```shell
$pip install opencv-python
```

For `numpy` run:
```shell
$pip install numpy
```

### Then 
We need to grab our region of interest, by listening to the mouse click event on the original image. We 
will manually write the points down of the region of interest as well as where we want to put the image. In our case
the face of the avatar.
```
def mouse_event(event, x, y,flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
    return
```
These are the points of the image ROI as well as placing the Image ROI on the 
top left conner of the original image:

```
# RIO img[y1:y2, x1:x2]
head = img[42:127, 107: 197]
img[10: 95, 15:105 ] = head
```
Then now we should display the image. The following function does the part of displaying the image on the screen with the image ROI attached to the original image:

```
def showImage():
    cv2.imshow("Image RIO", img)
    cv2.setMouseCallback("Image RIO", mouse_event)
    cv2.waitKey(0)
    return

showImage()
```
### All the code in one file `main.py`
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

img = cv2.imread("avatar.jpg")
top_head, bottom_head = (107, 42),(197 ,127)

# RIO img[y1:y2, x1:x2]
head = img[42:127, 107: 197]

img[10: 95, 15:105 ] = head
# FOR GETTING THE CODINATES OF THE HEAD FOM THE AVATAR
def mouse_event(event, x, y,flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
    return

def showImage():
    cv2.imshow("Image RIO", img)
    cv2.setMouseCallback("Image RIO", mouse_event)
    cv2.waitKey(0)
    return

showImage()

```

## What's Next?
* Color Palate

[Next]() || [Previous]()
