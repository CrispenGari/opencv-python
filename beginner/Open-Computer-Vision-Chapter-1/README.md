# Open Computer Version
These are just notes on the basics of `opencv-python`

## Installation of packages
Installation of packages can be done in many ways

### First way
Installation using pip:
```
python -m pip install opencv-python 
python -m pip install numpy
```
### Second ways
Installation using the text editor during program execution
```buildoutcfg
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

### Importing the required packages
if you used the second way of installing packages you don't need to import packages otherwise importing packages can be done as follows:
````buildoutcfg
import cv2
import numpy as np
````

### Creating a simple window in opencv-python.
This can be done as follows:
````buildoutcfg
def createWindow():
    #  Creates a simple window
    cv2.namedWindow("Window Name ", cv2.WINDOW_NORMAL)
    cv2.waitKey(0)
    return
createWindow()
````
### Reading Images
Reading images from the local filesystem can be done as follows:
````buildoutcfg
def readImage():
    img = cv2.imread("person_4.jpg", -1) # [0 -gray scale, 1 - color image default, -1 unchaged]
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    return
readImage()
````
### Saving Images
Saving images is simple all the function that will be used is ``imwrite()``
````buildoutcfg
""""
We want to create a simple application that 
saves images of different colors.
"""
def saveImageColor():
    image = cv2.imread("pic07.jpg")
    color_image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    cv2.imshow("Image", color_image)
    key = cv2.waitKey(0)
    print(key)
    if key == 27:
        #  esc
        cv2.destroyAllWindows()
    elif key & 0xFF == ord('s') or key == 115 or key == ord('s'):
        # key press s and save the image.
        cv2.imwrite("Color2Image.png", color_image)
        cv2.destroyAllWindows()
    else:
        pass
saveImageColor()
````

### Changing image Color
Changing color of an image can be done using the following functions:

````buildoutcfg
#  Changing the color of the image
def changeColor():
    img = cv2.imread("person_5.jpg")
    image_color = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)
    cv2.imshow("Color Image", image_color)
    cv2.waitKey(0)
    return
changeColor()
````

### Reading Web Camera

Reading a video stream from a web camera can be done as follows:

````buildoutcfg
# Reading a video from a web camera

def readWebCamera():
    capture = cv2.VideoCapture(0) # takes the Id of the camera
    # print(capture.isOpened())
    # print(capture.read())
    # you can set or get the video properties
    print(capture.get(4)) # hieght
    print(capture.get(3))
    capture.set(3, 1000)
    capture.set(4, 900)
    while True:
        ret, video = capture.read()
        gray_image = cv2.cvtColor(video, cv2.COLOR_BGR2LUV)
        cv2.imshow("Video", gray_image)
        if cv2.waitKey(1) == ord('q') or cv2.waitKey(1) & 0xFF == ord('q') :
            break
    return capture.release() and cv2.destroyAllWindows()
readWebCamera()
````
### Saving Videos
Saving videos can be done as follows:
````buildoutcfg
def recordingVideo():
    capture = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    while capture.isOpened():
        ret, video = capture.read()
        cv2.imshow("Preview",video)
        if ret:
            video = cv2.flip(video, 0)
            out.write(video)
        else:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    out.release()
    capture.release()
    return cv2.destroyAllWindows()
recordingVideo()
````
### Reading Local Videos

Reading videos locally is simmilar to reading videos from a web camera but the difference is instead of passing the camera id we pass the video's path and can be done as follows:
````buildoutcfg
# reading a video locally
def readLocalVideo():

    capture = cv2.VideoCapture("output.avi")

    while capture.isOpened():
        ret, video = capture.read()
        img_gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)

        cv2.imshow("Local Video", img_gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return capture.release() and cv2.destroyAllWindows()
````
#### Playing local videos with normal speed
playing videos with a normal speed can be done as follows:

````buildoutcfg
def playVidNormal():
    capture = cv2.VideoCapture("video1.mp4")
    # get the versions of cv2 and convert them to a python list [major_version, minor_version, subminor_version]
    versions = str(cv2.__version__).split('.')
    # check if the major version integer value is less or greater than 3
    if int(versions[0]) < 3:
        # if less fps will be equal to
        fps = capture.get(cv2.cv.CV_CAP_PROP_FPS)
    else:
        # if greater fps will be
        fps = capture.get(cv2.CAP_PROP_FPS)
    while capture.isOpened():
        ret, video = capture.read()
        img_gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)

        cv2.imshow("Local Video", img_gray)
        if cv2.waitKey(int(1000/fps)) & 0xFF == ord('q'):
            break
    return capture.release() and cv2.destroyAllWindows()
playVidNormal()
````

## Drawing Shapes, Text and Lines
### Drawing a line
Drawing a line can be done as follows:
```
cv2.line(img,starting_coord, ending_coord, color, line_thickness)
```
````buildoutcfg
def drawLine():

    # create an image using numpy
    img = np.zeros((512,512, 3), np.uint8)
    img = cv2.line(img,(0,0), (512, 512), (255, 0, 0), 1)
    cv2.imshow("Line", img)
    cv2.waitKey(0)
    return cv2.destroyAllWindows()
drawLine()
````
### Drawing a rectangle
Drawing a rectangle can be done as follows:
````
cv2.rectangle(img, top_left_conner, bottom_right_conner, color, line_thickness)
````
````buildoutcfg
def drawRect():
    # create an image using numpy
    img = np.zeros((512, 512, 3), np.uint8)
    img = cv2.rectangle(img, (200, 200), (300, 300), (0, 255, 0), 5)
    #    img = cv2.rectangle(img, (top-left), (bottom-right), (0, 255, 0), 5)
    cv2.imshow("Rectangle", img)
    cv2.waitKey(0)
    return cv2.destroyAllWindows()
drawRect()
````
### Drawing a circle
Drawing a circle can be done as follows:
```
cv2.circle(img, center, radius, color, filling);
[-1 to fill the circle]
```
````buildoutcfg
def drawCircle():
    # create an image using numpy
    img = np.zeros((512, 512, 3), np.uint8)
    img = cv2.circle(img, (200, 200), 100, (0, 0, 255), -1) # -1 for filling the circle
    # img = cv2.circle(img, (center), radius, (0, 0, 255), 2)
    cv2.imshow("Circle", img)
    cv2.waitKey(0)
    return cv2.destroyAllWindows()
drawCircle()
````
### Drawing an Ellipse
Drawing an Ellipse can be done as follows:
````buildoutcfg
def drawEllipse():
    # create an image using numpy
    img = np.zeros((512, 512, 3), np.uint8)
    img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
    cv2.imshow("ellipse", img)
    cv2.waitKey(0)
    return cv2.destroyAllWindows()
drawEllipse()

````
### Drawing a polygon

Drawing a polygon can be done as follows:
````buildoutcfg
def drawPolly():
    # create an image using numpy
    img = np.zeros((512, 512, 3), np.uint8)
    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    img = cv2.polylines(img, [pts], True, (0, 255, 255))
    cv2.imshow("Pollygon", img)
    cv2.waitKey(0)
    return cv2.destroyAllWindows()
drawPolly()
````

### Drawing Text:

Drawing text using can be done as follows:

````buildoutcfg
def drawText():
    # create an image using numpy
    img = np.zeros((512, 512, 3), np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    point = np.array([200, 200])
    text = "Crispen Gari"
    color = np.array([255, 0, 0])
    img = cv2.putText(img, text, (200, 200), font, 1, (255, 0, 0),1, cv2.LINE_4)
    cv2.imshow("Text", img)
    cv2.waitKey(0)
    return cv2.destroyAllWindows()
drawText()
````
### Challanges on shapes

##### Challange 1: we want to draw a circle inside a square.
````buildoutcfg
""""
Challange 1: we want to draw a circle inside a square.
"""
def circleSquare():
    image = np.zeros((512, 512, 3), np.uint8)
    point1 = (50, 50)
    point2 = (450, 450)
    center = (int((point1[0] + point2[0])/2), int((point1[1] + point2[1])/2))
    radius = int((center[0]- point1[0] ))
    image = cv2.rectangle(image, point1, point2,  (0, 255, 0), 2)
    image = cv2.circle(image, center, 2, (0, 0, 255), -1) #cv2.circle(image, center, 100, (0,0, 255), -1)
    image = cv2.circle(image, center, radius, (255, 0, 0), 0)

    cv2.imshow("Circle Inside Rectangle", image)
    cv2.waitKey(0)
    return  cv2.destroyAllWindows()
circleSquare()
````
#### Challange  2: Drawing points on an image every second
The following code draws images on an image in real time after every single second as well as the estimated line of best fit.
````buildoutcfg
""""
Drawing points on a video
"""
def drawPoints():

    while True:
        image = np.zeros((500, 500, 3), np.uint8)

        x = np.random.randint(0, 500, (50))
        y = np.random.randint(0, 500, (50))
        # get the intercept of y
        slope, intercept, r_value, p_value, std_err = linregress(x, y)
        # get the largest value of x and the index of y that corresponds to the value of x
        largest_value_of_x = 0
        index_of_y = largest_value_of_x
        for i in range(len(x)):
            if x[i]> largest_value_of_x:
                largest_value_of_x = x[i]
                index_of_y = i
            else:
                pass
        point_1 = (0, int(intercept))
        point_2 = (largest_value_of_x, y[index_of_y])
        #  Draw a reggression line on the points given point1, point2

        image = cv2.line(image, point_1, point_2, (np.random.randint(0, 255),
                                                   np.random.randint(0, 255), np.random.randint(0, 255)), 1)
        for i in range(len(x)):
            image = cv2.circle(image, (x[i], y[i]), 4,
                               (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)), -1)
        cv2.imshow("points", image)
        key = cv2.waitKey(1000)
        if key & 0xff == ord('q'):
            break
    return cv2.destroyAllWindows()
drawPoints()
````
## Mouse events in opencv-python

###  Getting all the mouse events
To get all the mouse events can be done as follows.
````buildoutcfg
def mouseEvents():
    events = [i for i in dir(cv2) if "EVENT" in i]
    print(events)
    return
mouseEvents()
````

#### Challenge on mouse events
This is a simple GUI that grabs the position of the mouse when single-right-clicked or double clicked and draw a point on that position.

````buildoutcfg
""""
Drawing a circle point when, on the point where the mouse is clicked.
"""
image = np.zeros((500, 500, 3), np.uint8)
def drawCicle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN or event == 1 or event == cv2.EVENT_LBUTTONDBLCLK or event == 7:
        cv2.circle(image,(x, y), 3, (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256)), -1)
        cv2.imshow("Mouse Event", image)
    return

def performTask():
    cv2.imshow("Mouse Event", image)
    cv2.setMouseCallback("Mouse Event", drawCicle)
    key = cv2.waitKey(0)
    if key & 0xff == ord('q'):
        cv2.destroyAllWindows()
    else:
        pass

performTask()
````

## What's Next?
We have covered a lot of things for now except the tool bar and color palatte. Now we should move to the next chapter which is ``Core Operations
``
### Core Operations will cover:
* Basic Operations on Images
* Arithmetic Operations on Images
* Performance Measurement and Improvement Techniques
* Mathematical Tools in OpenCV

## [NEXT](https://github.com/CrispenGari/Open-Computer-Version-Chapter-2) ===== Core Operations
