import cv2
import numpy as np

class BlurBackground(object):
    def __init__(self, image_path):
        self.image_path = image_path
        self.facesArray = []

    def blurBackground(self):
        # READ THE IMAGE
        image = cv2.imread(self.image_path)
        image = cv2.resize(image, (int(image.shape[1] * .5), int(image.shape[0] * .5)))
        finalImage = image.copy()
        blackImage = np.zeros_like(image)
        # CONVERT THE IMAGE TO GRAYSCALE AND DETECT THE FACES
        imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faceClassifier = cv2.CascadeClassifier('../files/haarcascade_frontalface_default.xml')

        faces = faceClassifier.detectMultiScale(imageGray, 1.3, 5)
        print(faces)
        # GET ALL THE FACES
        for x,y,w, h in faces:
            _face = image[y - 50: y + h + 50,x - 50:x + 50 + w]
            self.facesArray.append([_face, (x, y, w, h)])

        image = cv2.blur(image, ksize=(20, 20))
        # MAKE THE BACKGROUND DIMMER
        image = cv2.addWeighted(image, .4, blackImage, .6, 1)
        for face, _turple in self.facesArray:
            x, y, w, h = _turple
            image[y - 50: y + h + 50, x - 50:x + 50 + w] = face

        image = np.hstack([finalImage, image])
        cv2.imshow("Blur Background", image)
        cv2.waitKey(0)

blur = BlurBackground('../images/me.jpg')
if __name__ == '__main__':
    blur.blurBackground()