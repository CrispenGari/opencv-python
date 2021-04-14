import cv2, math
import numpy as np

class FindAngle(object):
    def __init__(self, image_path):
        self.image_path = image_path
        self.image_ = cv2.imread(self.image_path)
        self.image = cv2.resize(self.image_, (int(self.image_.shape[1]*.7), int(self.image_.shape[0]*.7)))
        self.blackImage = np.zeros_like(self.image)
        self.pointsList = []

    def mouseEvent(self, event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.pointsList.append((x, y))
            size = len(self.pointsList)
            print(size)
            if size != 0 and size % 3 == 0:
                anglePoint = self.pointsList[-3]
                for point in self.pointsList[-3:]:
                    cv2.line(self.image, anglePoint, point, (0, 255, 0), 2)
            cv2.circle(self.image, (x, y), 5, (0, 255, 0), -1)
        return
    def gradients(self, points):
        m1 = (points[0][1] - points[1][1])/(points[0][0] - points[1][0])
        m2 = (points[0][1] - points[2][1])/(points[0][0] - points[2][0])
        return m1, m2
    def findAngle(self, points):
        if len(points) % 3 == 0 and len(points) !=0:
            m1, m2 = self.gradients(points[-3:])
            angleRadians = math.atan((m1-m2)/(1 + m1 * m2))
            angleDegrees = math.degrees(angleRadians)
            return abs(round(angleDegrees, 1))
    def displayAngle(self):
        while True:
            allImages = np.hstack([self.image, self.blackImage])
            cv2.imshow("Angles", allImages)
            cv2.setMouseCallback("Angles", self.mouseEvent)
            key = cv2.waitKey(1)
            # click c to empty the points, esc to close the window
            if key & 0xFF == ord('c'):
                self.pointsList.clear()
                self.image_ = cv2.imread(self.image_path)
            elif key & 0xFF == 27:
                cv2.destroyAllWindows()
                break
            if len(self.pointsList) % 3 == 0 and len(self.pointsList) != 0:
                self.blackImage = np.zeros_like(self.image)
                cv2.putText(self.blackImage, "{} deg".format(self.findAngle(self.pointsList)),
                            (self.image.shape[0] // 2 - 100, self.image.shape[1] // 2), cv2.FONT_HERSHEY_SIMPLEX, 1.5,
                            (255, 255, 255), 2)


angle = FindAngle("1.jpg")
if __name__ == '__main__':
    angle.displayAngle()

def findAngleFunction():
    image = cv2.imread('1.jpg')
    image = cv2.resize(image, (int(image.shape[1]*.7), int(image.shape[0]*.7)))
    blackImage = np.zeros_like(image)
    pointsList = []

    # Mouse Event Function
    def mouseEvent(event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            pointsList.append((x, y))
            size = len(pointsList)
            print(size)
            if size != 0 and size % 3 == 0:
                anglePoint = pointsList[-3]
                for point in pointsList[-3:]:
                    cv2.line(image, anglePoint, point, (0, 255, 0), 2)
            cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
        return

    def gradients(points):
        m1 = (points[0][1] - points[1][1])/(points[0][0] - points[1][0])
        m2 = (points[0][1] - points[2][1])/(points[0][0] - points[2][0])
        return m1, m2
    def findAngle(points):
        if len(points) % 3 == 0 and len(points) !=0:
            m1, m2 = gradients(points[-3:])
            angleRadians = math.atan((m1-m2)/(1 + m1 * m2))
            angleDegrees = math.degrees(angleRadians)
            return abs(round(angleDegrees, 1))

    # Listen to mouse events on the picture
    while True:
        allImages = np.hstack([image, blackImage])
        cv2.imshow("Angles", allImages)
        cv2.setMouseCallback("Angles", mouseEvent)
        key = cv2.waitKey(1)
        # click c to empty the points, esc to close the window
        if key & 0xFF == ord('c'):
            pointsList.clear()
            image = cv2.imread("1.jpg")
        elif key & 0xFF == 27:
            cv2.destroyAllWindows()
            break
        if len(pointsList) % 3 == 0 and len(pointsList) != 0:
            blackImage = np.zeros(image.shape[:2])
            cv2.putText(blackImage, "{} deg".format(findAngle(pointsList)), (image.shape[0]//2 - 100, image.shape[1]//2),cv2.FONT_HERSHEY_SIMPLEX, 1.5,(255,255,255),2)
