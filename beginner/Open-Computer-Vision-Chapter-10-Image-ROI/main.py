
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

img = cv2.imread("avatar.jpg")
top_head, bottom_head = (107, 42),(197 ,127)

# RIO img[y1:y2, x1:x2]
head = img[42:127, 107: 197]

img[10: 95, 15:105 ] = head
# FOR GETTING THE CODINATES OF THE HEAD FOM THE AVATAR
def mouse_event(event, x, y,flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
    return

def showImage():
    cv2.imshow("Image RIO", img)
    cv2.setMouseCallback("Image RIO", mouse_event)
    cv2.waitKey(0)
    return

showImage()