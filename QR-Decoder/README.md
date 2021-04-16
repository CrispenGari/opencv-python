## QR-BAR_CODE Decoder
* This is a simple program that decodes the QR codes and Bar Codes using `pyzbar`

<p align="center">
<img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
<img src="https://img.shields.io/static/v1?label=package&message=opencv&color=yellow"/>
<img src="https://img.shields.io/static/v1?label=package&message=pyzbar&color=pink"/>
<img src="https://img.shields.io/static/v1?label=package&message=numpy&color=blueviolet"/>
<img src="https://img.shields.io/static/v1?label=package&message=pyqrcode&color=black"/>
<img src="https://img.shields.io/static/v1?label=package&message=pyimage&color=orange"/>
</p>

### Demo
<img align="center" src="https://github.com/CrispenGari/Opencv-Python/blob/main/angle-finder/bandicam%202021-04-14%2012-26-30-705.jpg" alt="demo"/>
<img align="center" src="https://github.com/CrispenGari/Opencv-Python/blob/main/angle-finder/bandicam%202021-04-14%2012-26-30-705.jpg" alt="demo"/>

### Required packages:
* opencv
* numpy
* pyzbar

### Installation
* To install the required packages run:
`````shell
pip install opencv-python
pip install numpy
pip install pyzbar
`````
### Code:
* The following code is found in the `main.py` file:
```
import cv2
from pyzbar.pyzbar import decode
import numpy as np

class Images:
    BAR_CODE_IMAGE= './images/3.png'
    QR_IMAGE = './images/2.png'
class DecodeCode(object):
    def __init__(self, image):
        self.image = image
    def decode(self):
        for data in decode(self.image):
            label = data.data.decode('utf8')
            type_ = data.type
            polyPoints = np.array(data.polygon, dtype=np.uint32)
            pts = np.array(polyPoints, np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(self.image, [pts], True, (0, 255, 0), 2)
            rectPoints = np.array(data.rect)
            cv2.putText(self.image, type_, (rectPoints[0], rectPoints[1] - 2), 1, cv2.FONT_HERSHEY_PLAIN, (255, 0, 0), 2)
            cv2.putText(self.image, label, (rectPoints[0] - 40, rectPoints[-1] + 55), 1, cv2.FONT_HERSHEY_PLAIN, (255, 0, 0), 1)
        cv2.imshow("QR - BarCode Decoder", self.image)
        cv2.waitKey(0)

if __name__ == '__main__':
    image = cv2.imread(Images.BAR_CODE_IMAGE)
    decoder = DecodeCode(image)
    decoder.decode()
```
### Generating QrCodes
* To generate our own qrcode images we used the package called `pyqrcode` to install it run the following commsnd:
```shell
pip install pyqrcode
```
> This package reqires pypng to save images on our local file, so it need o be installed:

````shell
pip install pypng
````
#### Code:
* This code generates QR code image and save them in a directory image.
```
from pyqrcode import QRCode
import random
class QRCodeGenerator(object):
    def __init__(self, name=str(random.randint(10, 1000))):
        self.name = name
    def generate(self):
        qr = QRCode(self.name)
        qr.png('./images/'+self.name+'.png', scale=10)
        return
qr = QRCodeGenerator('Crispen Gari')
qr.generate()
```
### Credits
* [OpenCv](https://docs.opencv.org/master/dc/da5/tutorial_py_drawing_functions.html)
* [PyZbar](https://pypi.org/project/pyzbar/)
* [PyQRCode](https://pythonhosted.org/PyQRCode/moddoc.html)