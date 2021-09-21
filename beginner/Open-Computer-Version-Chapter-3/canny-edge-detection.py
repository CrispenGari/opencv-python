
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

# read an image and a video
image = cv2.imread("avatar.jpg")

def cannyImage():
    image_canny = cv2.Canny(image, 100, 200)
    cv2.imshow("Image Canny", image_canny)
    cv2.waitKey(0)
    return cv2.destroyAllWindows()
cannyImage()


# capture = cv2.VideoCapture("video1.mp4")
