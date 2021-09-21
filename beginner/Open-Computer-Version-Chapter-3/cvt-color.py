
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

image = cv2.imread("avatar.jpg")
def changeColor(color= cv2.COLOR_BGR2BGRA):
    color_image = cv2.cvtColor(image, color)
    cv2.imshow("Color Image", color_image)
    key = cv2.waitKey(0)
    if key & 0xff ==ord('q'):
        return cv2.destroyAllWindows()
    return cv2.destroyAllWindows()

changeColor(cv2.COLOR_BGR2GRAY)

def changeColor(colors):
    if len(colors):
        while True:
            color_index = np.random.randint(0, len(colors))
            color_image = cv2.cvtColor(image, colors[color_index])
            cv2.imshow("Color Image", color_image)
            key = cv2.waitKey(1000) # 1 second interaval
            if key & 0xff ==ord('q'):
                return cv2.destroyAllWindows()
    return cv2.destroyAllWindows()
colors = np.array([
    cv2.COLOR_BGR2GRAY,
    cv2.COLOR_BGR2BGRA,
    cv2.COLOR_BGR2LUV,
    cv2.COLOR_BGR2HLS,
    cv2.COLOR_BGR2LAB,
    cv2.COLOR_BGR2YUV,
    cv2.COLOR_BGR2XYZ
])
changeColor(colors)