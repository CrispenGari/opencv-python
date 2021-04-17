
import cv2
import numpy as np
class ColorFullSketch(object):
    def __init__(self, image=None):
        self.image = image
        pass

    def colorSketch(self):
        image = self.image
        image = cv2.resize(image, (int(image.shape[1] * .5), int(image.shape[0] * .5)))
        originalImage = image.copy()
        image_small = cv2.pyrDown(image)
        n_iterations = 5
        for i in range(n_iterations):
            image_small = cv2.bilateralFilter(image_small, 9, 9, 7)
        finalImage = cv2.pyrUp(image_small)
        imageGray = cv2.cvtColor(finalImage, cv2.COLOR_BGR2GRAY)
        imageBlur = cv2.medianBlur(imageGray, ksize=7)
        imageEdge = cv2.adaptiveThreshold(imageBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 0.2)
        imageEdge = cv2.cvtColor(imageEdge, cv2.COLOR_GRAY2BGR)
        result = cv2.bitwise_or(imageEdge, image)
        allImages = np.hstack([originalImage, result])
        cv2.imshow("ColorFull Sketch", allImages)
        cv2.waitKey(0)

if __name__ == '__main__':
    image = cv2.imread("../images/me.jpg")
    pencil = ColorFullSketch(image = image)
    pencil.colorSketch()
