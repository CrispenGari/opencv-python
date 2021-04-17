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