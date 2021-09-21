
try:
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt

except ImportError as e:
    packages = ["opencv-python", "numpy", "matplotlib"]
    from pip._internal import main as install
    for package in packages:
        install(["install", package])
finally:
    pass
from stackedImages import stackImages

img = cv2.imread('stars.gif')

cv2.imshow("Image", img)
cv2.waitKey(1)