
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

def morphologyExImage(morphologies):
    if len(morphologies):
        while True:
            index = np.random.randint(0, len(morphologies))
            image_moph = cv2.morphologyEx(image, morphologies[index], kernel=ksize)
            cv2.imshow("Image Original", image_moph)
            if cv2.waitKey(1000) & 0xff == 'q':
                return cv2.destroyAllWindows()
    return cv2.destroyAllWindows()
# capture = cv2.VideoCapture("video1.mp4")
morphologies = np.array([
cv2.MORPH_OPEN,
cv2.MORPH_CLOSE,
cv2.MORPH_GRADIENT,
cv2.MORPH_TOPHAT,
cv2.MORPH_BLACKHAT
])
morphologyExImage(morphologies)