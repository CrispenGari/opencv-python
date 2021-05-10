## Triagle - Plain Shapes
This is a simple opencv application that listens to the mouse clicks on the canvas and calculate the area and perimeter of a triangle.

<p align="center">
<img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
<img src="https://img.shields.io/static/v1?label=package&message=opencv&color=yellow"/>
<img src="https://img.shields.io/static/v1?label=package&message=numpy&color=blue"/>
<img src="https://img.shields.io/static/v1?label=package&message=math&color=red"/>
</p>

## Demo
<p align="center">
<img src="https://github.com/CrispenGari/Opencv-Python/blob/main/plainShapes/02_Circle/bandicam%202021-05-10%2020-06-51-982.jpg" alt="demo" align="center"/>
</p>

### How to do it?
* Create a black image
* Listen to the mouse click event and keep on tracking the points
* Calculate the  radius, which is the line between 2 points
* The user just have to click on two points for the area to be calculated

### Simple Math
````
            
                . (x1, y1)
                |
                |
                | (x2, y2)
                
                Area        = pi * radius**2
                Perimeter   = 2 * pi * radius
                radius      = sqrt((x1, -x2)**2 + (y1, - y2)**2)
````

### ``Code``

```python
import numpy as np
import cv2, math
canvas = np.zeros((400, 512, 3))
board = np.zeros((100, 512, 3))
board[:] = 255
points = []
def area(radius):
    return round(math.pi * radius ** 2, 2)
def perimeter(radius):
    return round(2 * math.pi * radius, 2)
def radius(x, y, w, h):
    return int(math.sqrt((x - w)**2 + (y - h) ** 2))
def mouseEvent(event, x, y, params, flags):
    global points, canvas, board
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) == 2:
            # when the points are more than 2 restart the drawing
            canvas = np.zeros((400, 512, 3))
            board = np.zeros((100, 512, 3))
            board[:] = 255
            points = []
        points.append((x, y))
        if len(points) == 1:
            cv2.putText(canvas, f"  ({points[0][0]}, {points[0][1]})    ",
                        (points[0][0], points[0][1]), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
            cv2.circle(canvas, (x, y), 5, (0, 255, 0), -1)
        if len(points) == 2:
            points = points
            (x, y), (w, h) = points
            cv2.circle(canvas, (x, y), radius(x, y, w, h), (0, 255, 255), 1)
            cv2.line(canvas, (x, y), (w, h), (255, 255, 255), 1)
            board = np.zeros((100, 512, 3))
            board[:] = 255
            cv2.putText(board, f"Area: {area(radius(x, y, w, h))} units", (10, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
            cv2.putText(board, f"Perimeter: {perimeter(radius(x, y, w, h))} units", (10, 60), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
    pass
while True:
    cv2.putText(board, "Area: ", (10, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
    cv2.putText(board, "Perimeter: ", (10, 60), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
    allCanvas = np.row_stack([canvas, board])
    cv2.imshow("RECTANGLE", allCanvas)
    cv2.setMouseCallback("RECTANGLE", mouseEvent)
    key = cv2.waitKey(1)
    if key & 0xFF == 27:
        break
    if key & 0xFF == ord('c'):
        canvas = np.zeros((400, 512, 3))
        board = np.zeros((100, 512, 3))
        board[:]  = 255
        points = []
```