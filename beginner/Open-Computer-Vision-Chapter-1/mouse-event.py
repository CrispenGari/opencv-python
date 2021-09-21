

try:
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.stats import linregress
except ImportError as e:
    from pip._internal import main as install
    packages = ["numpy", "opencv-python", "matplotlib", "scipy"]
    for package in packages:
        install(["install", package])
finally:
    pass


# getting all the mouse events

def mouseEvents():
    events = [i for i in dir(cv2) if "EVENT" in i]
    print(events)
    return

""""
Drawing a circle point when, on the point where the mouse is clicked.
"""
image = np.zeros((500, 500, 3), np.uint8)
def drawCicle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN or event == 1 or event == cv2.EVENT_LBUTTONDBLCLK or event == 7:
        cv2.circle(image,(x, y), 3, (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256)), -1)
        cv2.imshow("Mouse Event", image)
    return

def performTask():
    cv2.imshow("Mouse Event", image)
    cv2.setMouseCallback("Mouse Event", drawCicle)
    key = cv2.waitKey(0)
    if key & 0xff == ord('q'):
        cv2.destroyAllWindows()
    else:
        pass

performTask()


