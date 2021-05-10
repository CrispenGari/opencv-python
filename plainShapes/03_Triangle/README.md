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
* Calculate teh length of all the triangle sides.
* Sort them in ascending order
* The longest line will be our base
* Based on [this article](https://www.omnicalculator.com/math/triangle-height#:~:text=A%20right%20triangle%20is%20a,c%20%3D%20a%20*%20b%20%2F%20c) find the perpendicular height
* calculate the perimeter and area

### Simple Math
````
                    (x, y)
                        *
                      / | \
                b    /  |   \    c      hc = perpendicular height
                    /   | hc  \         hc = a * b / c 
                   /    |       \       (c) is the base or the longest line
                   --------------
                        a
                Area        =  .5 * base * height
                Perimeter   =   a + b + c
                side        = sqrt((x1, -x2)**2 + (y1, - y2)**2)
````

### ``Code``
```python
import numpy as np
import cv2, math
canvas = np.zeros((400, 512, 3))
board = np.zeros((100, 512, 3))
board[:] = 255
points = []
lines = []
def area(b, h):
    return round(0.5 * b * h, 2)
def perimeter(lines):
    a, b, c = lines
    return round(a + b + c, 2)

def distance(points):
    point1, point2 = points
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1]) ** 2)

def pependicularHeight(lines):
    a, b, c = lines
    return a * b / c

def mouseEvent(event, x, y, params, flags):
    global points, canvas, board, lines
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) == 3:
            # when the points are more than 3 restart the drawing
            canvas = np.zeros((400, 512, 3))
            board = np.zeros((100, 512, 3))
            board[:] = 255
            points = []
            lines = []
        points.append((x, y))
        cv2.circle(canvas, (x, y), 5, (0, 255, 0), -1)

        if len(points) ==2:
            cv2.line(canvas, tuple(points[-2]), tuple(points[-1]), (255, 255, 255), 1)
            lines.append(distance(points[:2]))
        elif len(points) == 3:
            cv2.line(canvas, tuple(points[-2]), tuple(points[-1]), (255, 255, 255), 1)
            cv2.line(canvas, tuple(points[0]), tuple(points[-1]), (255, 255, 255), 1)
            lines.append((distance(points[1:3])))
            lines.append((distance([points[2], points[0]])))

        if len(lines) == 3:
            # our longest line is the base
            lines = sorted(lines)
            perpendicularH = pependicularHeight(lines)
            base = lines[-1]
            board = np.zeros((100, 512, 3))
            board[:] = 255
            cv2.putText(board, f"Area: {area(base, perpendicularH)} units", (10, 30), cv2.FONT_HERSHEY_PLAIN, 1,
                        (0, 0, 0), 1)
            cv2.putText(board, f"Perimeter: {perimeter(lines)} units", (10, 60), cv2.FONT_HERSHEY_PLAIN, 1,
                        (0, 0, 0), 1)
            pass
while True:
    cv2.putText(board, "Area: ", (10, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
    cv2.putText(board, "Perimeter: ", (10, 60), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
    allCanvas = np.row_stack([canvas, board])
    cv2.imshow("TRI-ANGLE", allCanvas)
    cv2.setMouseCallback("TRI-ANGLE", mouseEvent)
    key = cv2.waitKey(1)
    if key & 0xFF == 27:
        break
    if key & 0xFF == ord('c'):
        canvas = np.zeros((400, 512, 3))
        board = np.zeros((100, 512, 3))
        board[:]  = 255
        points = []
        lines = []
```