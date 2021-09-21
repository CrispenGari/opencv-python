
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
    "5.jpg",
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