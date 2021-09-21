# Open Computer Version - Commonly used opencv functions

We are going to go through the commonly used opencv functions which are:
* `cvtColor`
* `GaussianBlur`
*  `blur`
* `medianBlur`
* `Canny`
*  `dilate`
* `erode`
* `morphologyEx`
    * `cv2.MORPH_OPEN`
    * `cv2.MORPH_CLOSE`
    * `cv2.MORPH_GRADIENT`
    * `cv2.MORPH_TOPHAT`
    * `cv2.MORPH_BLACKHAT`
    

### 1. cvtColor
This function is used to change the color of images. Consider the following example that converts the
image to grayscale when called.
````buildoutcfg
image = cv2.imread("avatar.jpg")
def changeColor(color= cv2.COLOR_BGR2BGRA):
    color_image = cv2.cvtColor(image, color)
    cv2.imshow("Color Image", color_image)
    key = cv2.waitKey(0)
    if key & 0xff ==ord('q'):
        return cv2.destroyAllWindows()
    return cv2.destroyAllWindows()

changeColor(cv2.COLOR_BGR2GRAY)
````
Note that this function accepts any color that you want an image to be converted to.
#### Challange: Create a program that changes the color of images after a second

Modify the changeColor function to:
````buildoutcfg
image = cv2.imread("avatar.jpg")
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
````
### 2. GaussianBlur
This function is commonly used for blurring images or videos
#### Basic usage:
````buildoutcfg
def gaussianBlurImage():
    image_blur = cv2.GaussianBlur(image, (7, 7), 0)
    cv2.imshow("GaussianBlur Image", image_blur)
    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()
    return cv2.destroyAllWindows()
gaussianBlurImage()
````

### 3. blur
This function blurs an image just like the GaussianBlur the following code shows the basic usage of this function.
````buildoutcfg
image = cv2.imread("avatar.jpg")

def blurImage():
    image_blur = cv2.blur(image, (5, 7), 0)
    cv2.imshow("Blur Image", image_blur)
    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()
    return cv2.destroyAllWindows()

blurImage()
````
### 4. medianBlur
Here, the function `cv2.medianBlur()` computes the median of all the pixels under the kernel window and the central
pixel is replaced with this median value. This is highly effective in removing salt-and-pepper noise.
The following function shows the basic usage of the `medianBlur` function:

````buildoutcfg
image = cv2.imread("avatar.jpg")
def medianBlurImage():
    image_blur = cv2.medianBlur(image, 5)
    cv2.imshow("MedianBlur Image", image_blur)
    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()
    return cv2.destroyAllWindows()
medianBlurImage()
````
#### Challange: We want to write a simple function that blurs an images or a video when it is called this can be done as follows:
````buildoutcfg
# read an image and a video
image = cv2.imread("avatar.jpg")
capture = cv2.VideoCapture("video1.mp4")

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
````
When you run the code above we should see two windows poping up the one with the blury image 
and the other with the blury video. Not that you can change from `cv2.GaussianBlur` to one of the blur functions that you like in the above function

### 5. Canny
This function is used for edge detection in an image. 
First argument is our input
image. Second and third arguments are our minVal and maxVal respectively.
#### Basic Usage:
````buildoutcfg
image = cv2.imread("avatar.jpg")
def cannyImage():
    image_canny = cv2.Canny(image, 100, 200)
    cv2.imshow("Image Canny", image_canny)
    cv2.waitKey(0)
    return cv2.destroyAllWindows()
cannyImage()
````

### 6. erode
The basic idea of erosion is just like soil erosion only, it erodes away the boundaries of foreground object (Always
try to keep foreground in white). So what does it do? The kernel slides through the image (as in 2D convolution). A
pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it
is eroded (made to zero).
##### Basic usage 
````buildoutcfg
image = cv2.imread("avatar.jpg")

def erodeImage():
    ksize = np.ones((5,5), np.uint8) # if kannel size is an aray of 0's the erode method will not have effect
    image_erode = cv2.erode(image,ksize, iterations=1 )
    cv2.imshow("Image Erode", image_erode)
    cv2.waitKey(0)
    return cv2.destroyAllWindows()
erodeImage()
````
You can play around the kernel size to get the results you want.

### 7. dilate
It is just opposite of erosion. Here, a pixel element is ‘1’ if atleast one pixel under the kernel is ‘1’. So it increases
the white region in the image or size of foreground object increases.
#### Basic usage:

````buildoutcfg
image = cv2.imread("avatar.jpg")

def dilateImage():
    ksize = np.ones((5,5), np.uint8) # if kannel size is an aray of 0's the erode method will not have effect
    image_dilate = cv2.dilate(image,ksize, iterations=1 )
    cv2.imshow("Image Dilate", image_dilate)
    cv2.waitKey(0)
    return cv2.destroyAllWindows()
dilateImage()
````

Note that if you erode the image and dilate it with the same kernel or vise versa the image will go back to its original state.

### 8. morphologyEx
It is useful in removing noise from an image.

#### Basic usage of morphologyEx with the constants 
* `cv2.MORPH_OPEN`
* `cv2.MORPH_CLOSE`
* `cv2.MORPH_GRADIENT`
* `cv2.MORPH_TOPHAT`
* `cv2.MORPH_BLACKHAT`

In one function.

````buildoutcfg
image = cv2.imread("person_4.jpg", 0)
ksize = np.ones((3, 3), np.uint8)

def morphologyExImage(morphologies):
    if len(morphologies):
        while True:
            index = np.random.randint(0, len(morphologies))
            image_moph = cv2.morphologyEx(image, morphologies[index], kernel=ksize)
            cv2.imshow("Image Original", image_moph)
            if cv2.waitKey(1000) & 0xff == 'q':
                return cv2.destroyAllWindows()
    return cv2.destroyAllWindows()
# capture = cv2.VideoCapture("video1.mp4")
morphologies = np.array([
cv2.MORPH_OPEN,
cv2.MORPH_CLOSE,
cv2.MORPH_GRADIENT,
cv2.MORPH_TOPHAT,
cv2.MORPH_BLACKHAT
])
morphologyExImage(morphologies)
````

### What is Next?
In the following chapter we will resize and crop images

[Next](https://github.com/CrispenGari/Open-Computer-Version-Chapter4) || [Previous]()
