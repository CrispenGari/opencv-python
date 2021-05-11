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