
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

def empty(params):
    pass

image = np.zeros((200, 512, 3), np.uint8)

cv2.namedWindow("Colors")
cv2.createTrackbar("ONN: 1\n OFF: 0", "Colors", 0, 1, empty)
cv2.createTrackbar("B", "Colors", 0, 255, empty)
cv2.createTrackbar("G", "Colors", 0, 255, empty)
cv2.createTrackbar("R", "Colors", 0, 255, empty)

def showImage():
    while True:
        cv2.imshow("Colors", image)
        blue = cv2.getTrackbarPos("B", "Colors")
        green = cv2.getTrackbarPos("G", "Colors")
        red = cv2.getTrackbarPos("R", "Colors")
        switch = cv2.getTrackbarPos("ONN: 1\n OFF: 0", "Colors")
        # print(blue, green, red, switch)

        if switch == 1:
            image[:] = (blue, green, red)
        else:
            image[:] = (0,0,0)
        cv2.waitKey(1)
showImage()

