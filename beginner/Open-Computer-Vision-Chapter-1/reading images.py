

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

def createWindow():
    #  Creates a simple window
    cv2.namedWindow("Window Name ", cv2.WINDOW_NORMAL)
    cv2.waitKey(0)
    return
#  Changing the color of the image
def changeColor():
    img = cv2.imread("person_5.jpg")
    image_color = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)
    cv2.imshow("Color Image", image_color)
    cv2.waitKey(0)
    return

def readImage():
    img = cv2.imread("person_4.jpg", -1) # [0 -gray scale, 1 - color image default, -1 unchaged]
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    return

# Summing it up
""""
We want to create a simple application that 
saves images of different colors.
"""
def saveImageColor():
    image = cv2.imread("pic07.jpg")
    color_image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    cv2.imshow("Image", color_image)
    key = cv2.waitKey(0)
    print(key)
    if key == 27:
        #  esc
        cv2.destroyAllWindows()
    elif key & 0xFF == ord('s') or key == 115 or key == ord('s'):
        # key press s and save the image.
        cv2.imwrite("Color2Image.png", color_image)
        cv2.destroyAllWindows()
    else:
        pass
saveImageColor()

