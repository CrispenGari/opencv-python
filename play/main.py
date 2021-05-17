import cv2
import numpy as np

image = cv2.imread('ai.jpeg')
image = cv2.resize(image, (0, 0), None, .2, .2)

print(image.shape)
h, w, _ = image.shape
image = image[0:h-200, 0:w]


cv2.putText(image, "Crispen Gari", (270, 90), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 2)
cv2.putText(image, "Welcome to my GitHub, get to explore Data Science and Web Development.", (100, 130), cv2.FONT_HERSHEY_COMPLEX,.4, (255, 255, 255), 1)
cv2.imshow('', image)
cv2.waitKey(0)

cv2.imwrite("cover.jpeg", image)
print("saved")