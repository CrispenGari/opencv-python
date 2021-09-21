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

import cv2
import numpy as np

image = cv2.imread('img_1.jpg')
image_shape = image.shape # returns (height, width), 3) on BGR images
def resizeImage():
    final_size = (image_shape[1]//2, image_shape[0]//2)
    image_resize = cv2.resize(image, final_size)
    # image_resize = cv2.resize(src, (width, height))
    cv2.imshow("Resized image", image_resize)
    cv2.waitKey(0)
    return cv2.destroyAllWindows()
resizeImage()


def cropImage():
    phone_top_left_conner = (241,276)
    phone_bottom_left_conner = (241, 744)
    phone_top_right_conner = (241, 482)
    cropped_image = image[phone_top_left_conner[1]:phone_bottom_left_conner[1],
                    phone_top_right_conner[0]:phone_top_right_conner[1]]
    cv2.imshow("Cropped image", cropped_image)
    cv2.waitKey(0)
    return cv2.destroyAllWindows()
cropImage()
points = []
def moseEvent(event, x, y, flag, param):

    if event == cv2.EVENT_LBUTTONDOWN or event == cv2.EVENT_RBUTTONDOWN:
        points.append((x,y))
    else:
        pass
    if len(points) == 3:
        # sort the points
        index_largest_h =0
        index_larges_w = 0
        index_small_w =0
        largest_h = points[0][1]
        largest_w = points[0][0]
        smallest_w = points[0][0]
        for i in range(len(points)):
            if points[i][1] > largest_h:
                index_largest_h = i
            if points[i][0] >largest_w:
                index_larges_w = i
            if points[i][0] < smallest_w:
                index_small_w =i
        _top_left_conner = points[index_small_w]
        _bottom_left_conner = points[index_largest_h]
        _top_right_conner = points[index_larges_w]

        print(_top_left_conner, _bottom_left_conner, _top_left_conner, )

        cropped_image = image[_top_left_conner[1]:_bottom_left_conner[1],
                        _top_right_conner[0]:_top_right_conner[1]]
        cv2.imshow("Cropped image", cropped_image)
        cv2.waitKey(0)
        points.clear()
    else:
        pass
    return

def cropImageBaseOnMouse():
    cv2.imshow("Cropped image based on mouse",image)
    cv2.setMouseCallback("Cropped image based on mouse", moseEvent)
    cv2.waitKey(0)
    return cv2.destroyAllWindows()

cropImageBaseOnMouse()