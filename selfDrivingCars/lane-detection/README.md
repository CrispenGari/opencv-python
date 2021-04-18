## Lane Detection - Self Driving Cars
* Computer Vision application that detects lanes in real time from an image and from a video

<p align="center">
<img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
<img src="https://img.shields.io/static/v1?label=package&message=opencv&color=yellow"/>
<img src="https://img.shields.io/static/v1?label=package&message=numpy&color=blueviolet"/>
</p>

### Demo:

<img src="https://github.com/CrispenGari/Opencv-Python/blob/main/selfDrivingCars/lane-detection/bandicam%202021-04-18%2022-41-01-429.jpg" alt="demo"/>

### What are vertices?
* These are points that forms a tri-angle from an image
* In our case we created vertices points for lane detection, so the camera only focus on a certain area
* Implementation is as follows:

```
roi_vertices = [(0, height), (width/2, height/2), (width, height)]
colors = [(0, 255, 0), (255, 0, 0), (0, 0, 255)]
for (x, y), color in zip(roi_vertices, colors):
    cv2.circle(image, (int(x), int(y)), 15, (int(color[0]), int(color[1]), int(color[-1])), -1)
```
> The code above will help us to visually see the region of interest, we don't want to detect lanes for the whole camera, we just want to detect half the area


```
                (w/2, h/2)
                    0
                  /    \
                /        \
               0   car     0   
            (0, h)        (w,h)
```
### 
* Create a mask image
* Fill the vertices with a certain color
```
maskImage = np.zeros_like(image)
match_mask_color = 255
cv2.fillPoly(maskImage, np.array([roi_vertices], np.int32), match_mask_color)
```

### Main Functions
The `regionOfInterest()` function
```
def regionOfInterest(image, vertices):
    maskImage = np.zeros_like(image)
    match_mask_color =(255, 0, 0)
    cv2.fillPoly(maskImage, vertices, match_mask_color)
    return cv2.bitwise_and(image, maskImage)
```
* This function takes an image and vertices of the region of interest and returns a mask image
* We created a black image with the same shape as the imageCanny
* This function returns the bitwise_and between the maskImage and the imageCanny

The `drawLanes()` function
```
def drawLanes(image, lanes):
    original = image.copy()
    blackImage = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
    for line in lanes:
        for x1, y1, x2, y2 in line:
            cv2.line(blackImage, (x1, y1), (x2, y2),(0, 255, 0), 5)

    return cv2.bitwise_or(blackImage, original)
```
* This function takes the image and the lanes
* draws the lanes on an image and return that image:

### All code:
```
import cv2
import numpy as np

# READ AN IMAGE
image = cv2.imread('lanes.jpg')
def drawLanes(image, lanes):
    original = image.copy()
    blackImage = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
    for line in lanes:
        for x1, y1, x2, y2 in line:
            cv2.line(blackImage, (x1, y1), (x2, y2),(0, 255, 0), 5)

    return cv2.bitwise_or(blackImage, original)
def regionOfInterest(image, vertices):
    maskImage = np.zeros_like(image)
    match_mask_color =(255, 0, 0)
    cv2.fillPoly(maskImage, vertices, match_mask_color)
    return cv2.bitwise_and(image, maskImage)


# REGION OF INTEREST VERTICES
(height, width) = image.shape[:2]
roi_vertices = [(0, height), (width/2, height/2), (width, height)]
print(roi_vertices)

# CREATE A GRAY IMAGE
grayImage = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
# CREATE IMAGE CANNY (reduce some noise on the image, USE LARGE THRESHOLD VALUES)
cannyImage = cv2.Canny(grayImage, 200, 150)


# GET THE REGION OF INTEREST FROM THE IMAGE
croppedImage = regionOfInterest(cannyImage, np.array([roi_vertices], np.int32))

line1 = cv2.HoughLinesP(croppedImage, rho=6, theta=np.pi/60,threshold=160, lines=np.array([]), minLineLength=40, maxLineGap=20 )
# DISPLAY THE IMAGE

imageWithLanes = drawLanes(image, line1)
cv2.imshow("Lanes", imageWithLanes)

cv2.waitKey(0)
```

## Detections of lane from a video
```
import cv2
import numpy as np

cap = cv2.VideoCapture('solidWhiteRight.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 100)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 40)
def drawLanes(image, lanes):
    original = image.copy()
    blackImage = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
    for line in lanes:
        for x1, y1, x2, y2 in line:
            cv2.line(blackImage, (x1, y1), (x2, y2),(0, 255, 0), 5)
    return cv2.bitwise_or(blackImage, original)
def regionOfInterest(image, vertices):
    maskImage = np.zeros_like(image)
    match_mask_color =(255, 0, 0)
    cv2.fillPoly(maskImage, vertices, match_mask_color)
    return cv2.bitwise_and(image, maskImage)


while cap.isOpened():
    ret, image = cap.read()

    # REGION OF INTEREST VERTICES
    (height, width) = image.shape[:2]
    roi_vertices = [(0, height), (width/2 , height/2), (width, height)]
    print(roi_vertices)

    # CREATE A GRAY IMAGE
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
    # CREATE IMAGE CANNY (reduce some noise on the image, USE LARGE THRESHOLD VALUES)
    cannyImage = cv2.Canny(grayImage, 200, 150)
    # GET THE REGION OF INTEREST FROM THE IMAGE
    croppedImage = regionOfInterest(cannyImage, np.array([roi_vertices], np.int32))

    line1 = cv2.HoughLinesP(croppedImage, rho=6, theta=np.pi / 60, threshold=160, lines=np.array([]), minLineLength=40,
                            maxLineGap=20)
    imageWithLanes = drawLanes(image, line1)
    cv2.imshow("Lanes", imageWithLanes)
    if cv2.waitKey(int(1000/fps)) & 0xFF == 27:
        cap.release()
        cv2.destroyAllWindows()
        break
```