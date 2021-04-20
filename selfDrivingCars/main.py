
import cv2
import numpy as np
cap = cv2.VideoCapture('./lane-detection/solidWhiteRight.mp4')
carCascade = cv2.CascadeClassifier('./objectDetection/files/car.xml')
fps = cap.get(cv2.CAP_PROP_FPS)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 100)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 40)
def drawLanes(image, lanes):
    original = image.copy()
    blackImage = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
    for line in lanes:
        for x1, y1, x2, y2 in line:
            cv2.line(blackImage, (x1, y1), (x2, y2),(0, 255, 0), 5)
    return cv2.bitwise_or(blackImage, original)
def regionOfInterest(image, vertices):
    maskImage = np.zeros_like(image)
    match_mask_color =(255, 0, 0)
    cv2.fillPoly(maskImage, vertices, match_mask_color)
    return cv2.bitwise_and(image, maskImage)

# Car detections
def detectCars(frame):
    HEIGHT, WIDTH = frame.shape[:2]
    imageGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imageBlack = np.zeros_like(frame)
    cars = carCascade.detectMultiScale(imageGray, 2, 1)
    # I want to detect cars that ain't far
    for index, (x, y, w, h) in enumerate(cars):
        if HEIGHT * .5 <= y and index != -1:
            car = frame[y:h + y, x: x + w]
            carSeg = np.zeros_like(car)
            carSeg[:] = (128, 0, 128)
            car = cv2.add(car, carSeg)
            frame[y:h + y, x: x + w] = car
            imageBlack[y:h + y, x: x + w] = car
            # cv2.imshow("", finalCar)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+ w, h +y), (0, 255, 0), 2)
        cv2.rectangle(imageBlack, (x, y), (x + w, h + y), (0, 255, 0), 2)

    return np.hstack([frame, imageBlack])

def detectLines():
    while cap.isOpened():
        ret, image = cap.read()
        image = cv2.resize(image, (int(image.shape[1]*.6), int(image.shape[0]*.6)))

        # REGION OF INTEREST VERTICES
        (height, width) = image.shape[:2]
        roi_vertices = [(0, height), (width/2 , height/2), (width, height)]
        print(roi_vertices)

        # CREATE A GRAY IMAGE
        grayImage = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
        # CREATE IMAGE CANNY (reduce some noise on the image, USE LARGE THRESHOLD VALUES)
        cannyImage = cv2.Canny(grayImage,200, 150)
        # GET THE REGION OF INTEREST FROM THE IMAGE
        croppedImage = regionOfInterest(cannyImage, np.array([roi_vertices], np.int32))

        line1 = cv2.HoughLinesP(croppedImage, rho=6, theta=np.pi / 60, threshold=160, lines=np.array([]), minLineLength=40,
                                maxLineGap=20)
        imageWithLanes = drawLanes(image, line1)
        image = detectCars(frame=imageWithLanes)

        cv2.imshow("Lanes", image)
        if cv2.waitKey(int(1000/fps)) & 0xFF == 27:
            cap.release()
            cv2.destroyAllWindows()
            break

detectLines()