import numpy as np
import cv2
canvas = np.zeros((400, 512, 3))
board = np.zeros((100, 512, 3))
board[:] = 255
points = []
def area(w, h):
    return w * h
def perimeter(w, h):
    return 2 * w + 2 * h
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
        cv2.circle(canvas, (x, y), 5, (0, 255, 255), -1)
        if len(points) == 2:
            points = sorted(points)
            (x, y), (w, h) = points
            cv2.rectangle(canvas, (x, y), (w, h), (0, 255, 0), 1)
            board = np.zeros((100, 512, 3))
            board[:] = 255
            cv2.putText(board, f"Area: {area(w, h)} units", (10, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
            cv2.putText(board, f"Perimeter: {perimeter(w, h)} units", (10, 60), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
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