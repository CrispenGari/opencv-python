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

# Import the image Stack function
from utils.stackimages import stackImages
def empty(args):
    pass

image_black = np.zeros([500, 500, 3], dtype=np.uint8)
def detectColor():
    # Track Bars
    cv2.namedWindow("TrackBars")
    cv2.resizeWindow("TrackBars", 600, 200)
    cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
    cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
    cv2.createTrackbar("Sat Min", "TrackBars", 131, 255, empty)
    cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
    cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
    cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)
    while True:
        og_image = cv2.imread("images/car1.jpg")
        hsv_image = cv2.cvtColor(og_image, cv2.COLOR_BGR2HSV)
        # Get the positions of the TrackBars
        h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
        h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
        s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
        s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
        v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
        v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
        # print(h_min, h_max, s_min, s_max, v_min, v_max)
        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        # mask the image
        mask = cv2.inRange(hsv_image, lower, upper)
        imgResult = cv2.bitwise_and(og_image, og_image, mask=mask)
        image_label = cv2.putText(image_black, "RED COLOR", (200, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), cv2.LINE_4)
        imageStack = stackImages(.5, ([image_label, og_image , hsv_image], [ mask, imgResult, image_black]))
        cv2.imshow("Color Images", imageStack)
        # cv2.resizeWindow("Color Images", 600, 600)
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q') or key == 27:
            break
    return
detectColor()

