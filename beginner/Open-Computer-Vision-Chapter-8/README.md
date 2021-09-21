# What is the Shape Detector?

This is a simple `opencv-python` Application that detects edges on a `Canny` Image and based on the edges detected the app then `classify` the shape of the image.

### This app is capable of:
* detecting edges on images
* detect conners of images detected
* detemine the shapes on the image
* write the text corresponding to the shape detected

## Demo
![Shapes Detection](https://github.com/CrispenGari/Open-Computer-Vision-Chapter-8/blob/main/bandicam%202021-01-17%2016-30-04-525.jpg)

## Getting started
### First of all install `opencv-python` and `numpy`:
#### You can install `opencv-python` by running:

`python -m pip install opencv-python`

#### You can install `numpy` by running:
`python -m pip install numpy`

### Alternatively, you can install all of them by pasting the following code on your `main.py` and run it.

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

### After installation of all the packages then we are ready to go.

#### step 1:
Define the function that detects contours on the `Canned Imge`

````
def getContors(image, imgOutput):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # print(contours)
    # print(hierarchy)
    for contour in contours:
        area = cv2.contourArea(contour)
        # print(area)
        cv2.drawContours(image, contour, -1, (255, 255, 0), 3)
        perimeter = cv2.arcLength(contour, True)
        # print("PERIMETER: ", perimeter)

        coordinates = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
        # print("COORDINATES OF SHAPE: ", coordinates)
        detectShapes(coordinates, imgOutput)
    return
````

#### step 2:
Create a dictionary of `Shape Names`:
```
shapes = {
    "triagle": "Triagle",
    "rectangle": "Rectangle",
    "square": "Square",
    "circle": "Circle",
    "hexagon": "Hexagon",
    "pentagon": "Pentagon",
    "hectagon": "Hectagon",
    "octagon": "Octagon",
    "decagon": "Decagon",
    "nonagon": "Nonagon",
}
```

Then Create a function that draws bounding boxes as well as putting labels to detected shapes

```
def detectShapes(coordinates, imgOutput):
    sides = len(coordinates)
    boundingBox =cv2.boundingRect(coordinates)
    x, y, w, h = boundingBox
    if sides == 3:
        cv2.rectangle(imgOutput,(x, y), (w+x, h+y), (0, 255, 0), 3 )
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput,shapes["triagle"], (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    elif sides == 4:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 3)
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        if float(x)/float(y) < .05:
            cv2.putText(imgOutput, shapes["square"], (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
        else:
            cv2.putText(imgOutput, shapes["rectangle"], (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    elif sides == 5:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 3)
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput,shapes["pentagon"] , (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    elif sides == 6:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 3)
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput, shapes["hexagon"], (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    elif sides == 7:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 3)
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput,shapes["hectagon"] , (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    elif sides == 8:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 3)
        cv2.rectangle(imgOutput, (x-2, y - 20), (x + w +2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput,shapes["circle"] , (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    elif sides == 9:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 3)
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput,shapes["nonagon"] , (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    elif sides == 10:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 3)
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput, shapes["decagon"], (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
        print()
    else:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 1)
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput, shapes["circle"], (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    return
```

#### step 3:

Create a function that that wraps other function and invoke it to start detecting
shapes

```
def showImages():
    img = cv2.imread("images/shapes5.png")
    img2 = cv2.imread("images/shapes.jpg")

    # for image1
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)
    getContors(imgCanny, img)

    # for image 2
    imgGray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    imgBlur2 = cv2.GaussianBlur(imgGray2, (7, 7), 1)
    imgCanny2 = cv2.Canny(imgBlur2, 50, 50)
    getContors(imgCanny2, img2)
    stackedImage = stackImages(1, ([img2]))
    cv2.imshow("Shape Detection", stackedImage)
    cv2.waitKey(0)

showImages()
```

### All code in one place: `main.py`

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
from functions.stackedImages import stackImages

shapes = {
    "triagle": "Triagle",
    "rectangle": "Rectangle",
    "square": "Square",
    "circle": "Circle",
    "hexagon": "Hexagon",
    "pentagon": "Pentagon",
    "hectagon": "Hectagon",
    "octagon": "Octagon",
    "decagon": "Decagon",
    "nonagon": "Nonagon",
}

def detectShapes(coordinates, imgOutput):
    sides = len(coordinates)
    boundingBox =cv2.boundingRect(coordinates)
    x, y, w, h = boundingBox
    if sides == 3:
        cv2.rectangle(imgOutput,(x, y), (w+x, h+y), (0, 255, 0), 3 )
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput,shapes["triagle"], (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    elif sides == 4:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 3)
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        if float(x)/float(y) < .05:
            cv2.putText(imgOutput, shapes["square"], (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
        else:
            cv2.putText(imgOutput, shapes["rectangle"], (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    elif sides == 5:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 3)
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput,shapes["pentagon"] , (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    elif sides == 6:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 3)
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput, shapes["hexagon"], (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    elif sides == 7:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 3)
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput,shapes["hectagon"] , (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    elif sides == 8:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 3)
        cv2.rectangle(imgOutput, (x-2, y - 20), (x + w +2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput,shapes["circle"] , (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    elif sides == 9:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 3)
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput,shapes["nonagon"] , (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    elif sides == 10:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 3)
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput, shapes["decagon"], (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
        print()
    else:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 1)
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput, shapes["circle"], (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    return

def getContors(image, imgOutput):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # print(contours)
    # print(hierarchy)
    for contour in contours:
        area = cv2.contourArea(contour)
        # print(area)
        cv2.drawContours(image, contour, -1, (255, 255, 0), 3)
        perimeter = cv2.arcLength(contour, True)
        # print("PERIMETER: ", perimeter)

        coordinates = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
        # print("COORDINATES OF SHAPE: ", coordinates)
        detectShapes(coordinates, imgOutput)
    return

def showImages():
    img = cv2.imread("images/shapes5.png")
    img2 = cv2.imread("images/shapes.jpg")

    # for image1
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)
    getContors(imgCanny, img)

    # for image 2
    imgGray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    imgBlur2 = cv2.GaussianBlur(imgGray2, (7, 7), 1)
    imgCanny2 = cv2.Canny(imgBlur2, 50, 50)
    getContors(imgCanny2, img2)
    stackedImage = stackImages(1, ([img2]))
    cv2.imshow("Shape Detection", stackedImage)
    cv2.waitKey(0)

showImages()
```
That's all

#### What is next?

- Visual Painting

[Next](https://github.com/CrispenGari/Open-Computer-Vision-Chapter-9) || [Previous](https://github.com/CrispenGari/Open-Computer-Version-Chapter-7)

