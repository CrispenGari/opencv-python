
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
image = cv2.imread("person_4.jpg", 0)
ksize = np.ones((3, 3), np.uint8)

def dilateImage():
    image_dilate= cv2.dilate(image,ksize, iterations=1)
    image_erode = cv2.dilate(image, ksize, iterations=1)
    cv2.imshow("Image Original", image)
    cv2.imshow("Image Dilate", image_dilate)
    cv2.imshow("Image Erode", image_erode)
    dilated_eroded = cv2.dilate(image_dilate, ksize, iterations=1)
    cv2.imshow("Image Dilated Eroded", dilated_eroded)
    cv2.waitKey(0)
    return cv2.destroyAllWindows()
dilateImage()


# capture = cv2.VideoCapture("video1.mp4")
