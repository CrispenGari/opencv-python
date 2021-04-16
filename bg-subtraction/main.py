import numpy as np
import cv2


fgbg = cv2.createBackgroundSubtractorMOG2()


fgmask = fgbg.apply(cv2.imread('1.jpg'))
cv2.imshow('frame',fgmask)
cv2.waitKey(0)
