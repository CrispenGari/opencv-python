# Face Bluring -- Facex
* This program detects human face(s) using haarcascade_fontalface classifier from opencv and blur the faces detected leaving the whole body.

<p align="center">
<img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
<img src="https://img.shields.io/static/v1?label=package&message=opencv&color=yellow"/>
<img src="https://img.shields.io/static/v1?label=package&message=numpy&color=blueviolet"/>
</p>

## Demo
<p align="center">
<img src="https://github.com/CrispenGari/Opencv-Python/blob/main/eye-blink/ey.jpg" alt="demo" align="center"/>
</p>

## Implementaion
* Read the image
* Create a grayscale image from the original image
* detect the face and create an image **R**egion **O**f **I**ntrest (ROI) of the face
* blur take the face, blur it and put it back to it's position using numpy indexing

### `Code` 
```python
import cv2

class Paths:
    MY_FACE='../images/me.jpg'
    CASSCADE_CASSIF_PATH = '../files/haarcascade_frontalface_default.xml'
class BlurFace(object):
    def __init__(self, image_path):
        self.image_path = image_path
        pass
    def bluFace(self):
        image = cv2.imread(self.image_path)
        image = cv2.resize(image, (int(image.shape[1] * .4), int(image.shape[0] * .4)))
        imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faceClassifier = cv2.CascadeClassifier(Paths.CASSCADE_CASSIF_PATH)
        faces = faceClassifier.detectMultiScale(imageGray, 1.3, 1)
        for (x, y, w, h) in faces:
            face = image[y: y + h, x: x + w]
            face = cv2.blur(face, ksize=(19, 19))
            image[y: y + h, x: x + w] = face
        cv2.imshow("Face Bluring", image)
        cv2.waitKey(0)
if __name__ == '__main__':
    blurFace = BlurFace(Paths.MY_FACE)
    blurFace.bluFace()
```