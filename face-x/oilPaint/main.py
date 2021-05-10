import cv2

class OilPaint:
    image = cv2.imread('me.jpg', cv2.IMREAD_UNCHANGED)
    image = cv2.resize(image, (0, 0), None, .5, .5)
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    imageSmall = cv2.pyrDown(imageRGB)

    for i in range(55):
        imageSmall = cv2.bilateralFilter(imageSmall, 10, 5, 7)

    imageRGB = cv2.pyrUp(imageSmall)
    imageGray = cv2.cvtColor(imageRGB, cv2.COLOR_RGB2GRAY)
    imageBlur = cv2.medianBlur(imageGray, 13)
    imageEdge = cv2.cvtColor(imageBlur, cv2.COLOR_GRAY2RGB)
    finalImage = cv2.bitwise_and(imageEdge, image)
    cv2.imshow("Oil Paint", finalImage)
    cv2.waitKey(0)
OilPaint()