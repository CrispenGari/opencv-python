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