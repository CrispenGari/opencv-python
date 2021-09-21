

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
from functions.stackedImages import stackImages

shapes = {
    "triagle": "Triagle",
    "rectangle": "Rectangle",
    "square": "Square",
    "circle": "Circle",
    "hexagon": "Hexagon",
    "pentagon": "Pentagon",
    "hectagon": "Hectagon",
    "octagon": "Octagon",
    "decagon": "Decagon",
    "nonagon": "Nonagon",
}

def detectShapes(coordinates, imgOutput):
    sides = len(coordinates)
    boundingBox =cv2.boundingRect(coordinates)
    x, y, w, h = boundingBox
    if sides == 3:
        cv2.rectangle(imgOutput,(x, y), (w+x, h+y), (0, 255, 0), 3 )
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput,shapes["triagle"], (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    elif sides == 4:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 3)
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        if float(x)/float(y) < .05:
            cv2.putText(imgOutput, shapes["square"], (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
        else:
            cv2.putText(imgOutput, shapes["rectangle"], (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    elif sides == 5:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 3)
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput,shapes["pentagon"] , (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    elif sides == 6:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 3)
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput, shapes["hexagon"], (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    elif sides == 7:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 3)
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput,shapes["hectagon"] , (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    elif sides == 8:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 3)
        cv2.rectangle(imgOutput, (x-2, y - 20), (x + w +2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput,shapes["circle"] , (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    elif sides == 9:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 3)
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput,shapes["nonagon"] , (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    elif sides == 10:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 3)
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput, shapes["decagon"], (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
        print()
    else:
        cv2.rectangle(imgOutput, (x, y), (w + x, h + y), (0, 255, 0), 1)
        cv2.rectangle(imgOutput, (x - 2, y - 20), (x + w + 2, y), (0, 255, 0), -1)
        cv2.putText(imgOutput, shapes["circle"], (x + 5, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
    return

def getContors(image, imgOutput):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # print(contours)
    # print(hierarchy)
    for contour in contours:
        area = cv2.contourArea(contour)
        # print(area)
        cv2.drawContours(image, contour, -1, (255, 255, 0), 3)
        perimeter = cv2.arcLength(contour, True)
        # print("PERIMETER: ", perimeter)

        coordinates = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
        # print("COORDINATES OF SHAPE: ", coordinates)
        detectShapes(coordinates, imgOutput)
    return

def showImages():
    img = cv2.imread("images/shapes5.png")
    img2 = cv2.imread("images/shapes.jpg")

    # for image1
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)
    getContors(imgCanny, img)

    # for image 2
    imgGray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    imgBlur2 = cv2.GaussianBlur(imgGray2, (7, 7), 1)
    imgCanny2 = cv2.Canny(imgBlur2, 50, 50)
    getContors(imgCanny2, img2)
    stackedImage = stackImages(1, ([img2]))
    cv2.imshow("Shape Detection", stackedImage)
    cv2.waitKey(0)

showImages()

