import cv2
import numpy as np
class Cartoonfy(object):
    def __init__(self, image_path):
        self.image_path = image_path

    def cartoonfy(self):
        image = cv2.imread(self.image_path)
        image = cv2.resize(image, (int(image.shape[1] *.4), int(image.shape[0] * .4)))
        imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        imageBlur = cv2.medianBlur(imageGray, ksize=5)
        imageThreshHold = cv2.adaptiveThreshold(imageBlur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        imageThreshHold2 = cv2.adaptiveThreshold(imageBlur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 9, 9)
        imageCanny = cv2.Canny(imageBlur, 31, 39)
        # A bilateral filter is a non-linear, edge-preserving, and noise-reducing smoothing filter for images.
        filteredImage = cv2.bilateralFilter(image, 9, 100, 100)
        cattonImage = cv2.bitwise_and(filteredImage,filteredImage,mask=imageThreshHold)
        cattonImage2 = cv2.bitwise_and(filteredImage, filteredImage, mask=imageThreshHold2)
        cattonImage3 = cv2.bitwise_and(filteredImage, filteredImage, mask=imageCanny)
        #
        allCartoons = np.hstack([cattonImage, cattonImage2, cattonImage3])
        cv2.imshow("CARTOONIFY", allCartoons)
        cv2.waitKey(0)
cartoonify = Cartoonfy('../images/me.jpg')

if __name__ == '__main__':
    cartoonify.cartoonfy()