# What is this?

This is a simple Machine Learning open computer version 
application that detects faces in real time using `haarcascade_frontalface_default.xml` from opencv.

### Demo
[![Watch the video](https://github.com/CrispenGari/face-detection-open-computer-version-python/blob/main/bandicam%202020-12-09%2018-38-25-346.jpg)](https://github.com/CrispenGari/face-detection-open-computer-version-python/blob/main/bandicam%202020-12-09%2018-32-49-471.mp4)
### App capabilities.
This app is cappable of:
* detecting faces in real time
* draw rectangle around each face detected
* put text label `Face` to show that this is a Face

### First of all install `opencv-python` and `numpy`:
#### You can install `opencv-python` by running:

`python -m pip install opencv-python`

#### You can install `numpy` by running:
`python -m pip install numpy`

### Alternatively, you can install all of them by pasting the following code on your `main.py` and run it.

````buildoutcfg
try:
    import cv2
    import numpy as np
except ImportError as e:
    from pip._internal import main as install
    packages = ["numpy", "opencv-python"]
    for package in packages:
        install(["install", package])
finally:
    pass
````

### After installation of all the packages then we are ready to go.

#### step 1:
Create an image name `numpy` array.
````buildoutcfg
images_names = np.array([
    "avatar.jpg", "blog-post-1.jpg","person_1.jpg",
"person_2.jpg","person_3.jpg","person_4.jpg","person_5.jpg"
])
````
#### step 2:
Load the face cascade
````buildoutcfg
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
````
#### step 3:
Create a video from images in a `while` loop
````buildoutcfg
while True:
    # randomise the image index and display in on the screen
    image_index = np.random.randint(0, len(images_names))
    current_image = cv2.imread("images/{}".format(images_names[image_index]))
````
#### step 4:
Convert the image to gray-scale and detects face-points
````buildoutcfg
gray_image = cv2.cvtColor(current_image, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray_image,1.1,4)
````
Now we have all the point to draw the rectangle to our original image.



#### step 5:
Loop through faces array and draw a rectangle around each face that is going to be detected. Draw the text as was as a rectangle that is filled with green color that bounds the text
and show the image.
````buildoutcfg
for face in faces:
    #     face contains [x,y,w,h]
    #    Draw a rectangle around the face and text labeled Face

    final_image = cv2.rectangle(current_image, (face[0], face[1]), (face[0] + face[2],
                                                                    face[1] + face[3]), (0, 255, 0), 2)
    cv2.rectangle(final_image, (face[0] + 50, face[1] - 20), (face[0]-1, face[1]), (0, 255, 0), -1)
    cv2.putText(final_image, "Face", (face[0], face[1]-5), cv2.FONT_HERSHEY_PLAIN,  1, (255, 255, 255),1, cv2.LINE_4 )

    cv2.imshow("Face Detections", final_image)
````
Now everything is ready we are only left with showing images in a loop
#### step 6:
````buildoutcfg
key = cv2.waitKey(2000)
    if key & 0xFF == ord('q'):
        break
````

### All code in one place: `main.py`

````buildoutcfg
try:
    import cv2
    import numpy as np
except ImportError as e:
    from pip._internal import main as install
    packages = ["numpy", "opencv-python"]
    for package in packages:
        install(["install", package])
finally:
    pass

## we want to create a video of images
images_names = np.array([
    "avatar.jpg", "blog-post-1.jpg","person_1.jpg",
"person_2.jpg","person_3.jpg","person_4.jpg","person_5.jpg"
])
def detectFaces():
    # load the model
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    while True:
        # randomise the image index and display in on the screen
        image_index = np.random.randint(0, len(images_names))
        current_image = cv2.imread("images/{}".format(images_names[image_index]))
        # convert the image to gray-scale and detects face-points
        gray_image = cv2.cvtColor(current_image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray_image,1.1,4)
        for face in faces:
            #     face contains [x,y,w,h]
            #    Draw a rectangle around the face and text labeled Face

            final_image = cv2.rectangle(current_image, (face[0], face[1]), (face[0] + face[2],
                                                                            face[1] + face[3]), (0, 255, 0), 2)
            cv2.rectangle(final_image, (face[0] + 50, face[1] - 20), (face[0]-1, face[1]), (0, 255, 0), -1)
            cv2.putText(final_image, "Face", (face[0], face[1]-5), cv2.FONT_HERSHEY_PLAIN,  1, (255, 255, 255),1, cv2.LINE_4 )

            cv2.imshow("Face Detections", final_image)
        key = cv2.waitKey(2000)
        if key & 0xFF == ord('q'):
            break

    return cv2.destroyAllWindows()
detectFaces()
````

### Where to find the face cascade classifier?
You will find it on the opencv github [here](https://github.com/opencv/opencv/tree/master/data/haarcascades)
 
### Why this simple App?
This app was build for practise purposes.
