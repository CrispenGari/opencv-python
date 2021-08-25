
import cv2
import numpy as np

originalImage = cv2.imread('img.png', cv2.IMREAD_UNCHANGED)
originalImage = cv2.resize(originalImage,(0, 0) , None, .4, .4)
image = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

# Getting image Dimensions
H, W = image.shape[:2]

# Remove some noise
image_blur = cv2.medianBlur(image, 9)
image_blur = cv2.GaussianBlur(image_blur, (11, 11), 21)

# Finding Outlines
image_thresh = cv2.adaptiveThreshold(
    image_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 61, 2)

# Fill the area with black to find objects

# cv2.floodFill(image_thresh, np.zeros((H + 2, W + 2), np.uint8), (0, 0), 0)
image_erosion = cv2.erode(image_thresh, np.ones((5, 5)))

#  Finding objects
cnts, _ = cv2.findContours(image_erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print("Objects detected: ", len(cnts))
#  Converting from grayscale to BGR
c = 0
for cnt in cnts:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.circle(originalImage, (x+w//2, y+h//2), max(w, h)//2, (c, 150, 255-c), 3)
    c += 5

cv2.imshow("Original Image", originalImage)
cv2.waitKey(0)

