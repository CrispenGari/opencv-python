# Image Transformations - cv2.warpPerspective()

#### Basic usage
We have an image named `cards.jpg`  which contains some cards on it and we want to crop and get the image of the King of spades from the cards. We must use the warpPerspective function to perform such task.

The following code does the job of taking the King of spades from the cards on the picture `cards.jpg`
````buildoutcfg

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

def warpPerspectiveImage():
    image = cv2.imread("cards.jpg")
    width, height = 250,350
    pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    image_wrap = cv2.warpPerspective(image, matrix, (width, height))
    cv2.imshow("Phones", image_wrap)
    cv2.waitKey(0)
    return  cv2.destroyAllWindows()
warpPerspectiveImage()
````
That's all 

#### What's next?
##### stacking images
* `vstack`
* `hstack`

[Next](https://github.com/CrispenGari/Open-Computer-Version-Chapter-6) || [Previous](https://github.com/CrispenGari/Open-Computer-Version-Chapter-4)