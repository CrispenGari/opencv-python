import cv2
import numpy as np

# READ AN IMAGE
image = cv2.imread('lanes.jpg')
def drawLanes(image, lanes):
    original = image.copy()
    blackImage = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
    for line in lanes:
        for x1, y1, x2, y2 in line:
            cv2.line(blackImage, (x1, y1), (x2, y2),(0, 255, 0), 5)

    return cv2.bitwise_or(blackImage, original)
def regionOfInterest(image, vertices):
    maskImage = np.zeros_like(image)
    match_mask_color =(255, 0, 0)
    cv2.fillPoly(maskImage, vertices, match_mask_color)
    return cv2.bitwise_and(image, maskImage)


# REGION OF INTEREST VERTICES
(height, width) = image.shape[:2]
roi_vertices = [(0, height), (width/2, height/2), (width, height)]
print(roi_vertices)

# CREATE A GRAY IMAGE
grayImage = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
# CREATE IMAGE CANNY (reduce some noise on the image, USE LARGE THRESHOLD VALUES)
cannyImage = cv2.Canny(grayImage, 200, 150)


# GET THE REGION OF INTEREST FROM THE IMAGE
croppedImage = regionOfInterest(cannyImage, np.array([roi_vertices], np.int32))

line1 = cv2.HoughLinesP(croppedImage, rho=6, theta=np.pi/60,threshold=160, lines=np.array([]), minLineLength=40, maxLineGap=20 )
# DISPLAY THE IMAGE

imageWithLanes = drawLanes(image, line1)
cv2.imshow("Lanes", imageWithLanes)
cv2.waitKey(0)