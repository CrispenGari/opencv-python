### Detecting Objects in OpenCV Python

We are going to use `opencv` to count uniform objects on an image. We are going to count how may beans are there on an image.

<p align="center">
<img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
<img src="https://img.shields.io/static/v1?label=package&message=opencv&color=yellow"/>
<img src="https://img.shields.io/static/v1?label=package&message=numpy&color=blueviolet"/>
</p>


### Imports

We are going to use `cv2` and `numpy`
```python
import cv2
import numpy as np
```

### Reading the images

```python
originalImage = cv2.imread('img.png', cv2.IMREAD_UNCHANGED)
originalImage = cv2.resize(originalImage,(0, 0) , None, .4, .4)
image = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
```

### Get The Image Width and Height
```python
H, W = image.shape[:2]
```

### Removing some noise from an image

```python
image_blur = cv2.medianBlur(image, 9)
image_blur = cv2.GaussianBlur(image_blur, (11, 11), 21)
```

### Finding outlines
```python
image_thresh = cv2.adaptiveThreshold(
    image_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 61, 2)
```

### Fill the area with black to find the objects
* The `floodFill` does not have much of an effect in our case
````python
cv2.floodFill(image_thresh, np.zeros((H + 2, W + 2), np.uint8), (0, 0), 0)
image_erosion = cv2.erode(image_thresh, np.ones((5, 5)))
````

### Finding contours or objects count
````python
cnts, _ = cv2.findContours(image_erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
````

### Printing the number of objects found on an image

````python
print("Objects detected: ", len(cnts))
#  Converting from grayscale to BGR
c = 0
````
### Drawing countors and displaying the image
````python
for cnt in cnts:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.circle(originalImage, (x+w//2, y+h//2), max(w, h)//2, (c, 150, 255-c), 3)
    c += 5

cv2.imshow("Original Image", originalImage)
cv2.waitKey(0)
````

### Result

<p align="center">
<img src="https://github.com/CrispenGari/Opencv-Python/blob/main/objects-counter/bandicam%202021-08-25%2020-47-21-981.jpg" alt=""/>
</p>

````shell
Objects detected:  16
````

### The whole code

```python

import cv2
import numpy as np

originalImage = cv2.imread('img.png', cv2.IMREAD_UNCHANGED)
originalImage = cv2.resize(originalImage,(0, 0) , None, .4, .4)
image = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

# Getting image Dimensions
H, W = image.shape[:2]

# Remove some noise
image_blur = cv2.medianBlur(image, 9)
image_blur = cv2.GaussianBlur(image_blur, (11, 11), 21)

# Finding Outlines
image_thresh = cv2.adaptiveThreshold(
    image_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 61, 2)

# Fill the area with black to find objects

cv2.floodFill(image_thresh, np.zeros((H + 2, W + 2), np.uint8), (0, 0), 0)
image_erosion = cv2.erode(image_thresh, np.ones((5, 5)))

#  Finding objects
cnts, _ = cv2.findContours(image_erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print("Objects detected: ", len(cnts))
#  Converting from grayscale to BGR
c = 0
for cnt in cnts:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.circle(originalImage, (x+w//2, y+h//2), max(w, h)//2, (c, 150, 255-c), 3)
    c += 5

cv2.imshow("Original Image", originalImage)
cv2.waitKey(0)

```