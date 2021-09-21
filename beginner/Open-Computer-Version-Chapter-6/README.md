# Stacking Images Open-cv

Sometimes we want to show images in a grid form, but `open-cv` only provide us with a function `imshow` that 
shows only one images. Fortunately we have numpy functions `vstack` and `hstack` which can help us to show images vertically and horizontally respectively. 

### The `hstack` function.
The following function stacks images horizontally. Firstly, you have to read the images and put them in a list or a tuple or even in a `numpy` array.
Then display images in a row using the `hstack` numpy function. 

```
images = np.array([cv2.imread("images/person_4.jpg")
                ,cv2.imread("images/person_2.jpg"),
                ])
                
def horizontalStack(images):
    horizontalImages = np.hstack(images)
    cv2.imshow("Horizontal Images", horizontalImages)
    cv2.waitKey(0)
    return
# Call the function 
horizontalStack(images)
```

### The `vstack` function.
The following function stacks images vertically. Firstly, you have to read the images and put them in a list or a tuple or even in a `numpy` array.
Then display images in a column using the `vstack` numpy function. 

```
def verticalStack(images):
    verticalImages = np.vstack(images)
    cv2.imshow("Vertical Images", verticalImages)
    cv2.waitKey(0)
    return
images = np.array([cv2.imread("images/person_4.jpg")
                ,cv2.imread("images/person_2.jpg"),
                ])

# Call the verticalStack function.
verticalStack(images)
```
## Limitations of the `vstack` and the `hstack`
* Images must have the same dimensions that we can not display a gray image and a colored image in the same stacks.

## Displaying * images in a grid system.

There's a function in the `python file` named `stackimages.py`, This function accepts two arguments `image scale` and `image array` when called
and display the images in grid system based on the dimensions/shape of the `array of images`. This function is as follows:

```

import numpy as np
import cv2

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
```

### Usage of the stackImages function.
The following code represents the basic usage of the stackImages function

```
# import the function from the file `stackimages.py`
from stackimages import stackImages

img = cv2.imread("images/person_1.jpg")
imgGray = cv2.imread("images/person_1.jpg", 0)
imageStack = stackImages(0.5, ([img, img, img], [img, imgGray, img]))
cv2.imshow("Stuck Images", imageStack)
cv2.waitKey(0)
```

That's all 

#### What is next?
* Color Detection from images

[Next](https://github.com/CrispenGari/Open-Computer-Vision-Chapter-7) || [Previous](https://github.com/CrispenGari/Open-Computer-Version-Chapter-5)
