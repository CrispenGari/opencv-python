# Scaling - image cropping and resizing
* `resize`
* `image cropping image[height1: height2, width1: width2]` 

### 1. resize
This function resizes the image to a given size
#### Basic usage:
##### Getting the image shape
To get the image shape we use the `shape` property this can be done as follows:

````buildoutcfg
image = cv2.imread('img_1.jpg')
print(image.shape) # returns the height and the width of the image in the order (height, width, 3) if the image is color
image = cv2.imread('img_1.jpg', 0)
print(image.shape) # returns the height and the width of the image in the order (height, width) respectively

````

Note that the shape of the image in `opencv` is given by `(height, width)` not `(width, height)` as usual.

#### resizing an image Example:
Suppose we want to resize the image to half of its original `width` and `height` we can firstly get the `shape` of the image then resize
it by dividing the `width` and `height` by 2. But this is a litle bit tricky because in `opencv` the image `height` comes first when we use the 
`shape` property but when resizing we must pass the `width` first then `height`
The following code shows how can we resize the image to it's half size

````buildoutcfg
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
````
That is it for resizing an image

### 2. cropping an image
On the image that we are working on right now of name `img_1.jpg`
there is a person holding a cell phone. we want to crop the whole image and leave the 
phone. First we need to grab the points, and find the width and the height of the image.

````buildoutcfg
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
````
#### How to grab the coodinates on an image?
* use `paint`, `adobe photoshop` etc.
* use of the `mouse event in opencv`


#### What is Next?
######  `warpPerspective` Function


[Next](https://github.com/CrispenGari/Open-Computer-Version-Chapter-5) || [Previous](https://github.com/CrispenGari/Open-Computer-Version-Chapter-3)
