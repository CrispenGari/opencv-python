# Facial Biometric
This repository detects a human face using Dlib's 68 points model. As the human face is way too complex for a computer to learn, so we have used the 68 points model to ease the process of facial recognition. Facial Biometric uses a two step biometric process for facial recognition. These steps are:

<img src="https://github.com/CrispenGari/Opencv-Python/blob/main/Facial-biometics/images/localisation1.jpg" align="center"/>
* Facial localization to locate a human face and return 4(x,y)-coordinates that forms a rectangle bounding the face.
Detecting facial structures using Dlib's 68 points model.
* The below image is an example of Dlib's 68 points model. This pre-trained facial landmark detector inside the Dlib's library is used to estimate the location of 68(x,y)-coordinates that maps to the different facial structures.

## Demo
<img src="https://github.com/CrispenGari/Opencv-Python/blob/main/Facial-biometics/images/bandicam%202021-04-10%2020-44-04-067.jpg" align="center"/>
<img src="https://github.com/CrispenGari/Opencv-Python/blob/main/Facial-biometics/images/bandicam%202021-04-10%2020-44-03-597.jpg" align="center"/>
## Installations
* We need to install these three packages:
    1. opencv
    2. dlib
    3. cmake
    4. numpy
    
````shell
pip install opencv
pip install cmake
pip install dlib
pip install numpy
````
> Why `cmake`? 
    * dlib is a library written in c++ that used applications like cmake,boost, so installation may require us to install `cmake` first.

## Imports
* We are going to import all the required packages as follows:

```python
import numpy as np
import cv2
import dlib
```
### Detecting a face using `dlib`
* To detect the position of the face in using `dlib` is just simple as follows:

```python
import dlib
import cv2

detector = dlib.get_frontal_face_detector()
image = cv2.imread('images/2.jpg')
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = detector(imageGray)
print(faces)
for face in faces:
    x1,y1,x2,y2 = face.left(), face.top(), face.right(), face.bottom()
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
cv2.imshow("Image", image)
cv2.waitKey(0)
```
### Getting face landmarks
```python
predictor = dlib.shape_predictor('files/shape_predictor_68_face_landmarks.dat')
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = detector(imageGray)

for face in faces:
    x1,y1,x2,y2 = face.left(), face.top(), face.right(), face.bottom()
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
    landmarks = predictor(imageGray, face)
    print(landmarks.parts(), len(landmarks.parts())) # 68 landmarks
    
    for landmark in landmarks.parts():
    cv2.circle(image, (landmark.x, landmark.y), 2, (0, 255, 255), -1)
```

### Downloading Files
* [shape_predictor_68_face_landmarks.dat](https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat)