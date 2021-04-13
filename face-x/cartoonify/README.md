# Cartoonify
* Cool operation on images to create 2 cartoons of a given image path
<p align="center">
<img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
<img src="https://img.shields.io/static/v1?label=package&message=opencv&color=yellow"/>
<img src="https://img.shields.io/static/v1?label=package&message=numpy&color=blueviolet"/>
</p>

## Demo
<img src="https://github.com/CrispenGari/Opencv-Python/blob/main/face-x/cartoonify/bandicam%202021-04-13%2012-50-43-767.jpg" alt="demo" align="center"/>


### How to do it?
* Read the image
* Convert the image to gray scale
* apply a `medianBlur` to an image
* apply a threshold to a blur image
* apply `biletarelFilter` to an image
    *  > A bilateral filter is a non-linear, edge-preserving, and noise-reducing smoothing filter for images
* use `bitwise_and` on the original image and threshold image


### ``Code``

```
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
```