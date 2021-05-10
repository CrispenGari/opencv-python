import cv2
import numpy as np

image = cv2.imread('water_coins.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# cv2.THRESH_OTSU will change the coins to black and the background to white
# we add thresh binary inverse to make coins white and background black
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN, kernel , iterations = 2)
# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)

dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
ret, markers = cv2.connectedComponents(sure_fg)

markers = markers+1
markers[unknown==255] = 0
markers = cv2.watershed(image,markers)
image[markers == -1] = [255,0,0]
cv2.imshow("Image Binary",image)
cv2.waitKey(0)
