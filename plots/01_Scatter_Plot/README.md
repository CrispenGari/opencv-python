## Scatter Plot - Plots

This is a simple opencv application that draws a scatter plot on a white canvas for the randomly generated points

<p align="center">
<img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
<img src="https://img.shields.io/static/v1?label=package&message=opencv&color=yellow"/>
<img src="https://img.shields.io/static/v1?label=package&message=numpy&color=blue"/>
<img src="https://img.shields.io/static/v1?label=package&message=random&color=red"/>
</p>

## Demo
<p align="center">
<img src="https://github.com/CrispenGari/Opencv-Python/blob/main/plots/01_Scatter_Plot/bandicam%202021-05-11%2019-13-56-460.jpg" alt="demo" align="center"/>
</p>

### How to do it?
* Create a white image
* Generate the points
* Draw a small circle for each point generated

### ``Code``
```python
import numpy as np
import cv2
from random import randrange

x = np.array([randrange(1, 100) for i in range(50)])
y = np.array([randrange(1, 100) for i in range(50)])

points = np.column_stack([x, y])
canvas = np.ones((400, 400, 3))

def scalePoint(width, height, point, maxX, maxY):
    return int(width * point[0] / maxX), int(height * point[1] / maxY)

def scatterPlot(points):
    x, y = points[:, 0], points[:, 1]
    maxX = np.max(x)
    maxY = np.max(y)
    for point in points:
        cv2.circle(canvas, scalePoint(400-50, 400, point, maxX=maxX, maxY=maxY), 4, (0, 0, 0), -1)
    cv2.imshow("Scatter Plot", canvas)
    cv2.waitKey(0)
scatterPlot(points)
```