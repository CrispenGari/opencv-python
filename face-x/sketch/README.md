# Sketch
* Cool operation on images to sketch an image.
<p align="center">
<img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
<img src="https://img.shields.io/static/v1?label=package&message=opencv&color=yellow"/>
<img src="https://img.shields.io/static/v1?label=package&message=numpy&color=blueviolet"/>
</p>

## Demo
<img src="https://github.com/CrispenGari/Opencv-Python/blob/main/face-x/sketch/bandicam%202021-04-13%2013-32-56-055.jpg" alt="demo" align="center"/>


### How to do it?
* Read the image
* Convert the image to gray scale
* invert the image using the `bitwise_not`
* smooth the inverted image using the `GassianBlur`
* divide the gray image with smoothed imaged lowered from `255`
* the output is the sketch


### ``Code``

```
import cv2
import numpy as np

class Sketch(object):
    def __init__(self, image_path, scale=200):
        self.image_path = image_path
        self.scale = scale

    def sketch(self):
        image = cv2.imread(self.image_path)
        image = cv2.resize(image, (int(image.shape[1] * .4), int(image.shape[0] * .4)))
        grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Invert the image using bitwise_not
        inventImage = cv2.bitwise_not(grayImage)
        blurImage = cv2.GaussianBlur(inventImage, (21, 21), sigmaX=0, sigmaY=0)
        sketchImage = cv2.divide(grayImage, 255-blurImage, scale=self.scale)
        cv2.imshow("Sketch", sketchImage)
        cv2.waitKey(0)
        return
    def defaultDrawing(self):
        image = cv2.imread(self.image_path)
        image = cv2.resize(image, (int(image.shape[1] * .4), int(image.shape[0] * .4)))
        grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Invert the image using bitwise_not
        inventImage = cv2.bitwise_not(grayImage)
        blurImage = cv2.GaussianBlur(inventImage, (21, 21), sigmaX=0, sigmaY=0)
        sketchImage = cv2.divide(grayImage, 255-blurImage, scale=100)
        cv2.imshow("Drawing", sketchImage)
        cv2.waitKey(0)
        return
    def coolSketch(self):
        image = cv2.imread(self.image_path)
        image = cv2.resize(image, (int(image.shape[1] * .2), int(image.shape[0] * .2)))
        grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Invert the image using bitwise_not
        inventImage = cv2.bitwise_not(grayImage)
        blurImage = cv2.GaussianBlur(inventImage, (21, 21), sigmaX=0, sigmaY=0)

        allImages = []

        for scale in [50, 100, 150, 200, 250]:
            sketchImage = cv2.divide(grayImage, 255-blurImage, scale=scale)
            allImages.append(sketchImage)

        sketchImages = np.hstack(allImages)
        cv2.imshow("Cool Sketch", sketchImages)
        cv2.waitKey(0)
        return
sketch = Sketch(image_path='../images/me.jpg', scale=100)

if __name__ == '__main__':
    sketch.coolSketch()
    sketch.defaultDrawing()
    sketch.sketch()
```