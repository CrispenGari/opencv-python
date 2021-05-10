## Cat Face Detector
This is an opencv simple application that detects the face of a cat from a video using a `haarcascade_fontal_catface.xml` file.

<p align="center">
<img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
<img src="https://img.shields.io/static/v1?label=package&message=opencv&color=yellow"/>
</p>

## Demo
<p align="center">
<img src="https://github.com/CrispenGari/Opencv-Python/blob/main/object-detection/cat-detector/bandicam%202021-04-30%2015-46-21-230.jpg" alt="demo" align="center"/>
</p>

### How to do it?
* Read the image
* Convert the image to gray scale
* load the `haarcascade_` file 
* detects the faces from a video frame
* draw the rectangle around the face of the cat.

### ``Code``

```python
import cv2
catFaceCascade = cv2.CascadeClassifier('haarcascade_frontal_catface.xml')
cap = cv2.VideoCapture('cats/test2.mov')
fps = cap.get(cv2.CAP_PROP_FPS)
while cap.isOpened():
    _, image = cap.read()
    image = cv2.resize(image, (0, 0), None, .8, .8)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cats = catFaceCascade.detectMultiScale(gray)
    for x, y, w, h in cats:
        cv2.rectangle(image, (x, y), (x+w, h+h), (0, 255, 0), 2)
    cv2.imshow('Cat Face', image)
    if cv2.waitKey(int(1000/fps)) & 0xFF == 27:
        cap.release()
        cv2.destroyAllWindows()
        break
```