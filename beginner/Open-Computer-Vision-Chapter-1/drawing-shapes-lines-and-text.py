

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

# Drawing shapes on images,


def drawLine():

    # create an image using numpy
    img = np.zeros((512,512, 3), np.uint8)
    # drawing a diagonal line
    img = cv2.line(img,(0,0), (512, 512), (255, 0, 0), 1)
    cv2.imshow("Line", img)
    cv2.waitKey(0)
    return cv2.destroyAllWindows()

def drawRect():
    # create an image using numpy
    img = np.zeros((512, 512, 3), np.uint8)
    # drawing a diagonal line
    img = cv2.rectangle(img, (200, 200), (300, 300), (0, 255, 0), 5)
    #    img = cv2.rectangle(img, (top-left), (bottom-right), (0, 255, 0), 5)
    cv2.imshow("Rectangle", img)
    cv2.waitKey(0)
    return cv2.destroyAllWindows()

def drawCircle():
    # create an image using numpy
    img = np.zeros((512, 512, 3), np.uint8)
    # drawing a diagonal line
    img = cv2.circle(img, (200, 200), 100, (0, 0, 255), -1) # -1 for filling the circle
    # img = cv2.circle(img, (center), radius, (0, 0, 255), 2)
    cv2.imshow("Circle", img)
    cv2.waitKey(0)
    return cv2.destroyAllWindows()

def drawEllipse():
    # create an image using numpy
    img = np.zeros((512, 512, 3), np.uint8)
    # drawing a diagonal line
    img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
    cv2.imshow("ellipse", img)
    cv2.waitKey(0)
    return cv2.destroyAllWindows()

def drawPolly():
    # create an image using numpy
    img = np.zeros((512, 512, 3), np.uint8)
    # drawing a diagonal line
    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    img = cv2.polylines(img, [pts], True, (0, 255, 255))
    cv2.imshow("Pollygon", img)
    cv2.waitKey(0)
    return cv2.destroyAllWindows()

def drawText():
    # create an image using numpy
    img = np.zeros((512, 512, 3), np.uint8)

    font = cv2.FONT_HERSHEY_SIMPLEX
    point = np.array([200, 200])
    text = "Crispen Gari"
    color = np.array([255, 0, 0])
    img = cv2.putText(img, text, (200, 200), font, 1, (255, 0, 0),1, cv2.LINE_4)
    cv2.imshow("Text", img)
    cv2.waitKey(0)
    return cv2.destroyAllWindows()

""""
Challange 1: we want to draw a circle inside a square.
"""
def circleSquare():
    image = np.zeros((512, 512, 3), np.uint8)
    point1 = (50, 50)
    point2 = (450, 450)
    center = (int((point1[0] + point2[0])/2), int((point1[1] + point2[1])/2))
    radius = int((center[0]- point1[0] ))
    image = cv2.rectangle(image, point1, point2,  (0, 255, 0), 2)
    image = cv2.circle(image, center, 2, (0, 0, 255), -1) #cv2.circle(image, center, 100, (0,0, 255), -1)
    image = cv2.circle(image, center, radius, (255, 0, 0), 0)

    cv2.imshow("Circle Inside Rectangle", image)
    cv2.waitKey(0)
    return  cv2.destroyAllWindows()
circleSquare()



""""
Challange 2: Drawing points on a video
"""
def drawPoints():

    while True:
        image = np.zeros((500, 500, 3), np.uint8)

        x = np.random.randint(0, 500, (50))
        y = np.random.randint(0, 500, (50))
        # get the intercept of y
        slope, intercept, r_value, p_value, std_err = linregress(x, y)
        # get the largest value of x and the index of y that corresponds to the value of x
        largest_value_of_x = 0
        index_of_y = largest_value_of_x
        for i in range(len(x)):
            if x[i]> largest_value_of_x:
                largest_value_of_x = x[i]
                index_of_y = i
            else:
                pass
        point_1 = (0, int(intercept))
        point_2 = (largest_value_of_x, y[index_of_y])
        #  Draw a reggression line on the points given point1, point2

        image = cv2.line(image, point_1, point_2, (np.random.randint(0, 255),
                                                   np.random.randint(0, 255), np.random.randint(0, 255)), 1)
        for i in range(len(x)):
            image = cv2.circle(image, (x[i], y[i]), 4,
                               (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)), -1)
        cv2.imshow("points", image)
        key = cv2.waitKey(1000)
        if key & 0xff == ord('q'):
            break
    return cv2.destroyAllWindows()
drawPoints()
