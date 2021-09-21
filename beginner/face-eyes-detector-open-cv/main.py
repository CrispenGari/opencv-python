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

# import the imageStack function from stackimages python file
from utils.stackimages import stackImages

# Read all the images in the image folder

img1 = cv2.imread('images/person_1.jpg')
img4 = cv2.imread('images/person_4.jpg')
img2 = cv2.imread('images/person_2.jpg')
img3 = cv2.imread('images/person_3.jpg')
img5 = cv2.imread('images/person_5.jpg')
img6 = cv2.imread('images/avatar.jpg')

# Load images in a python list
images_array =[
    img1, img2, img3, img4, img5, img6
]

# Load the cascade file from the files folder
eyesCascade = cv2.CascadeClassifier('files/haarcascade_eye_tree_eyeglasses.xml')
faceCascade = cv2.CascadeClassifier('files/haarcascade_frontalface_default.xml')


def detectFaceEyes():
    black_image = np.zeros([500, 500, 3], dtype=np.uint8)
    gray_images = []
    final_images_faces = []
    final_images_eyes =[]
    index = 0
    for image in images_array:
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(image_gray)
        eyes = eyesCascade.detectMultiScale(image_gray)
        if len(faces):
            for (x, y, w, h) in faces:
                final_image = cv2.rectangle(images_array[index], (x, y), (x + w, y + h), (0, 255, 0), 3)
                final_images_faces.append(final_image)
            else:
                pass
        if len(eyes):
            for (x,y, w, h) in eyes:
                final_image = cv2.rectangle(images_array[index], (x, y), (x + w, y + h), (0, 255, 255), 3)
                final_images_eyes.append(final_image)
            else:
                pass
        index += 1
        gray_images.append(image_gray)

    imageStacked = stackImages(.3, (
        [gray_images[0], gray_images[1], gray_images[2],black_image],
        [final_images_faces[0], final_images_faces[1], final_images_faces[2], images_array[3]],
        [gray_images[3], gray_images[4], gray_images[5], black_image],
        [final_images_faces[3], final_images_faces[4], final_images_faces[5], gray_images[1]]
    ))
    cv2.imshow("Face Eyes Detector", imageStacked)
    cv2.waitKey(0)
    return
detectFaceEyes()