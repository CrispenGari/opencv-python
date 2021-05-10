## Oil paint - FaceX
* Using different opencv functions to come up  with an oilpainted image.

<p align="center">
<img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
<img src="https://img.shields.io/static/v1?label=package&message=opencv&color=yellow"/>
</p>

## Demo
<img  src="https://github.com/CrispenGari/Opencv-Python/blob/main/face-x/images/bandicam%202021-04-17%2021-57-14-173.jpg" alt="demo" align="center"/>

## Implementaion
* Read the image
* Convert the image to rgb
* apply ``pyrDown`` to the image
* iterate a cuple of time on the small image and apply a ``bilateralFilter``  on an image
* restore the image to it's original size using ``pyrUp``
* converting the image from bgr to gray
* apply a ``medianBlur`` to the image with a certain `` ksize``
* convert the image back to rgb
* apply the bitwise and to the image to get the final image. 

### `Code` 

````python
import cv2

class OilPaint:
    image = cv2.imread('me.jpg', cv2.IMREAD_UNCHANGED)
    image = cv2.resize(image, (0, 0), None, .5, .5)
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    imageSmall = cv2.pyrDown(imageRGB)

    for i in range(55):
        imageSmall = cv2.bilateralFilter(imageSmall, 10, 5, 7)

    imageRGB = cv2.pyrUp(imageSmall)
    imageGray = cv2.cvtColor(imageRGB, cv2.COLOR_RGB2GRAY)
    imageBlur = cv2.medianBlur(imageGray, 13)
    imageEdge = cv2.cvtColor(imageBlur, cv2.COLOR_GRAY2RGB)
    finalImage = cv2.bitwise_and(imageEdge, image)
    cv2.imshow("Oil Paint", finalImage)
    cv2.waitKey(0)
OilPaint()
````