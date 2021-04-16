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
    image = cv2.imread('./images/Crispen Gari.png')
    decoder = DecodeCode(image)
    decoder.decode()