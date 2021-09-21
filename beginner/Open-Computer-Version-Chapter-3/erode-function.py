
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
image = cv2.imread("avatar.jpg")

def erodeImage():
    ksize = np.ones((5,5), np.uint8) # if kannel size is an aray of 0's the erode method will not have effect
    image_canny = cv2.erode(image,ksize, iterations=1 )
    cv2.imshow("Image Erode", image_canny)
    cv2.waitKey(0)
    return cv2.destroyAllWindows()
erodeImage()


# capture = cv2.VideoCapture("video1.mp4")
