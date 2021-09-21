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
from stackimages import stackImages
def horizontalStack(images):
    horizontalImages = np.hstack(images)
    cv2.imshow("Horizontal Images", horizontalImages)
    cv2.waitKey(0)
    return

def verticalStack(images):
    verticalImages = np.vstack(images)
    cv2.imshow("Vertical Images", verticalImages)
    cv2.waitKey(0)
    return
images = np.array([cv2.imread("images/person_4.jpg")
                ,cv2.imread("images/person_2.jpg"),
                ])

verticalStack(images)
horizontalStack(images)
img = cv2.imread("images/person_1.jpg")
imgGray = cv2.imread("images/person_1.jpg", 0)
imageStack = stackImages(0.5, ([img, img, img], [img, imgGray, img]))
cv2.imshow("Stuck Images", imageStack)
cv2.waitKey(0)