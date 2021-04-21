import cv2
import numpy as np
from math import pow, sqrt

points = []
letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
image = np.zeros((512, 512, 3), np.uint8)
def mouseEvent(event, x, y, params, flags):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, (x, y), 5, (0, 0, 255), -1)
        cv2.putText(image, letters[len(points) if len(points) < 26 else 0], (x, y), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        points.append((x, y))
    if len(points) > 1:
        last_two_points = points[-2:]
        d, midpoint = findDistance(last_two_points)
        cv2.putText(image, f'{round(d)} (px)', midpoint, cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
        cv2.line(image, tuple(last_two_points[0]), tuple(last_two_points[1]),(0, 255, 0), 2)
    return

def findDistance(points):
    x1, y1 = points[0]
    x2, y2 = points[1]
    d = sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
    midpoint = tuple(([(x1 + x2)//2, (y1 + y2)//2]))
    return d, midpoint

while True:
    cv2.putText(image, f'TO CLEAR THE POINTS PRESS (c)', (20, 20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
    cv2.imshow("DISTANCE BETWEEN TWO POINTS", image)
    cv2.setMouseCallback("DISTANCE BETWEEN TWO POINTS", mouseEvent, None)
    key = cv2.waitKey(1)
    if key & 0xFF == 27:
        cv2.destroyAllWindows()
        break
    elif key & 0xFF == ord('c'):
        image = np.zeros((512, 512, 3), np.uint8)
        points = []
# cm = pixels / 96 * 2.54
