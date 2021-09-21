
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

# read an image and a video
image = cv2.imread("avatar.jpg")
capture = cv2.VideoCapture("video1.mp4")

# BASIC BLUR FUNCTION
def blurImage():
    image_blur = cv2.blur(image, (5, 7), 0)
    cv2.imshow("Blur Image", image_blur)
    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()
    return cv2.destroyAllWindows()

blurImage()

# medianBlur FUNCTION
def medianBlurImage():
    image_blur = cv2.medianBlur(image, 5)
    cv2.imshow("MedianBlur Image", image_blur)
    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()
    return cv2.destroyAllWindows()
medianBlurImage()

#  GaussianBlur FUNCTION
def gaussianBlurImage():
    image_blur = cv2.GaussianBlur(image, (7, 7), 0)
    cv2.imshow("GaussianBlur Image", image_blur)
    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()
    return cv2.destroyAllWindows()
gaussianBlurImage()

# CHALLENGE
def blurMedia(media):
    # check if the media type is video or image
    if media["type"] == "video":
        while capture.isOpened():
            ret, video = capture.read()
            image_blur = cv2.GaussianBlur(video,(7, 7), 0) # note that the kanel size should be odd numbers
            cv2.imshow("GaussianBlur Video", image_blur)
            if cv2.waitKey(1) == ord('q'):
                capture.release()
                break
    else:
        image_blur = cv2.GaussianBlur(image, (7, 7), 0)
        cv2.imshow("GaussianBlur Image", image_blur)
        if cv2.waitKey(0) == ord('q'):
            cv2.destroyAllWindows()
    return cv2.destroyAllWindows()

blurMedia({"type": "video"}) # shows a blury video
blurMedia({"type": "image"}) # shows a blury image
