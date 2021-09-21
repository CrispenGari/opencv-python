

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

# Reading a video from a web camera

def readWebCamera():
    capture = cv2.VideoCapture(0) # takes the Id of the camera
    # print(capture.isOpened())
    # print(capture.read())
    # you can set or get the video properties
    print(capture.get(4)) # hieght
    print(capture.get(3))

    capture.set(3, 1000)
    capture.set(4, 900)
    while True:
        ret, video = capture.read()
        gray_image = cv2.cvtColor(video, cv2.COLOR_BGR2LUV)
        cv2.imshow("Video", gray_image)
        if cv2.waitKey(1) == ord('q') or cv2.waitKey(1) & 0xFF == ord('q') :
            break
    return capture.release() and cv2.destroyAllWindows()

# reading a video locally
def readLocalVideo():

    capture = cv2.VideoCapture("output.avi")
    while capture.isOpened():
        ret, video = capture.read()
        img_gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)

        cv2.imshow("Local Video", img_gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return capture.release() and cv2.destroyAllWindows()
def recordingVideo():
    capture = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    while capture.isOpened():
        ret, video = capture.read()
        cv2.imshow("Preview",video)
        if ret:
            video = cv2.flip(video, 0)
            out.write(video)
        else:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    out.release()
    capture.release()
    return cv2.destroyAllWindows()
recordingVideo()