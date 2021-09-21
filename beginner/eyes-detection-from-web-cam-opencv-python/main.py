
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
def detectEyeGlasses():
    capture = cv2.VideoCapture(0)
    eyesCasecade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
    while capture.isOpened():
        ret, video = capture.read()
        # convert the video to gray_scale
        image_gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
        eyes = eyesCasecade.detectMultiScale(image_gray, 1.1)
        for (x, y, w, h) in  eyes:
            final_image = cv2.rectangle(video, (x, y), (x+w, y+h), (0, 255, 0), 2)
            final_image = cv2.rectangle(final_image, (x-1, y+h+15),(x+30, y+h), (0, 255, 0), -1)
            final_image = cv2.putText(final_image, "Eye", (x, y+h+12), cv2.FONT_HERSHEY_PLAIN, 1,(255, 0, 0), 1)
            cv2.imshow("Eyes Detector", final_image)
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q') or key == 27:
            capture.release()
            return cv2.destroyAllWindows()
    return cv2.destroyAllWindows()
detectEyeGlasses()