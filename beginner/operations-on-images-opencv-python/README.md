# Basic Operations On Images

### 1. Merging and Splitting Images

Suppose we have an image `avatar.jpg` and we want to split the channels of images `(b,g,r)` we can do it as follows:

```
image = cv2.imread("avatar.jpg")
b,g, r = cv2.split(image) # b,g, r are now images you can show them using cv2.imshow() method
```

To merge splitted channels of images we use the `cv2.merge()` function, the following is an example on how to merge
the image that we have splitted.

```
image = cv2.merge((b,g,r))

# Now you can show the image

cv2.imshow("Image", image)
cv2.waitKey(0)
```

### 2. Adding Borders to Images

`cv2.copyMakeBorder(image, top, bottom, left, right, borderType, value)`

This function is used to add borders to images the above code shows how you can use this function in adding borders to images.

```
# Read the Image
image = cv2.imread("avatar.jpg")
#  Create images with different borders
replicate = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_CONSTANT,value=(255, 0, 0))

# Show all the images and their borders
cv2.imshow("BORDER_CONSTANT", constant)
cv2.imshow("BORDER_WRAP", wrap)
cv2.imshow("BORDER_REFLECT", reflect)
cv2.imshow("BORDER_REFLECT_101", reflect101)
cv2.imshow("BORDER_REPLICATE", replicate)
cv2.waitKey(0)

```

### 3. Arithmetic Operations on Images

In this section we will use these two functions:

- `cv2.add()`
- `cv2.addWeighted()`

#### 3.1 `cv2.add()` function

This function will add two images together and the images must be of the same size. Suppose we have 2 images `avatar.jpg` and `pic07.jpg` and we want to add these two images together
we can use the cv2.add() function to do that. The following is an example of how it can be done:

```
# Read the Image
image = cv2.imread("avatar.jpg")
image2 = cv2.imread("pic07.jpg")

#  Give the two images the same size using the cv2.resize() function
image = cv2.resize(image, (300, 300))
image2 = cv2.resize(image2, (300, 300))

# Add the 2 images together
imageResult = cv2.add(image2, image)
# Display  the image result
cv2.imshow("Added Images", imageResult)
cv2.waitKey(0)
```

The images will be added together as 1 and displayed

#### 3.2 `cv2.addWeighted()` function Image Blending

This is also image addition, but different weights are given to images so that it gives a feeling of blending or transparency. The function
works as follows:

```
cv2.addWeighted(src1, opacity1, src2, opacity2, gamma)
```

`opacity2 + opacity1 = 1` But that's not always the case. In this example we are going to add the two images from the previous add function using addWeighted() function and pass different opacity to each image.

```
# Read the Image
image = cv2.imread("avatar.jpg")
image2 = cv2.imread("pic07.jpg")

#  Give the two images the same size using the cv2.resize() function
image = cv2.resize(image, (300, 300))
image2 = cv2.resize(image2, (300, 300))

# Add the 2 images together
imageResult = cv2.addWeighted(image2, .8 ,image, .2, 0)
# Display  the image result
cv2.imshow("Added Images", imageResult)
cv2.waitKey(0)
```

### 4. Bitwise Operations

This includes bitwise AND, OR, NOT and XOR operations. They will be highly useful while extracting any part of
the image (as we will see in coming chapters), defining and working with non-rectangular ROI etc. Suppose we have
two different images which are image1.png and image2.png and we want to perform the bitwise operations on them. This
can be done as follows:

```
image1 =  cv2.imread("image1.png")
image2 =  cv2.imread("image2.png")

imageResultAnd = cv2.bitwise_and(image1, image2)
imageResultOr = cv2.bitwise_or(image1, image2)
imageResultNot = cv2.bitwise_not( image2)
imageResultXOR = cv2.bitwise_xor(image1, image2)
cv2.imshow("And Operator",imageResultAnd)
cv2.imshow("OR Operator",imageResultOr)
cv2.imshow("Not Operator Image 2",imageResultNot)
cv2.imshow("XOR Operator",imageResultXOR)
cv2.waitKey(0)
```

This works exactly the same way XOR, NOT, AND and OR operations works, But in our case we are applying those operations
on images.

### 5. Changing Colors Spaces

### Object Tracking

This is a simple object tracking program that will track the object based on color.

### Step 1:

Import all the modules that we are going to use, `numpy` and `cv2`:

```
try:
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt

except ImportError as e:
    packages = ["opencv-python", "numpy", "matplotlib"]
    from pip._internal import main as install
    for package in packages:
        install(["install", package])
finally:
    pass
```

### Step 2:

Import the `stackImages` function from the `stackImages.py` file for displaying images on the same window.

```
from stackedImages import stackImages
```

### Step 3:

Create an `empty` function that accept `x` as its argument and pass.

```
def empty(x):
    pass
```

### Step 4:

Create a named window and put 6 trackbars `[HUE_MAX, HUE_MIN, VALUE_MAX, VALUE_MIN, SAT_MAX, SAT_MIN]` that will help us to change the color spaces of an image in real time.

```
cv2.namedWindow("Object Tracking")
cv2.createTrackbar("H_MAX","Object Tracking", 255, 255, empty)
cv2.createTrackbar("H_MIN","Object Tracking", 0, 255, empty)
cv2.createTrackbar("S_MAX","Object Tracking", 255, 255, empty)
cv2.createTrackbar("S_MIN","Object Tracking", 0, 255, empty)
cv2.createTrackbar("V_MAX","Object Tracking", 255, 255, empty)
cv2.createTrackbar("V_MIN","Object Tracking", 0, 255, empty)

```

### Step 5:

- Create a function that when called it will start detecting images on the `webcam` using `VideoCapture()` method.
- Convert the image to `HSV`
- Grab the track bars position using the `getTrackbarPos()` method
- Create two numpy arrays one will store the `maximum` values and the other will store `minimum` values.
- Create a mask image from the image `HSV` using these maximum and minimum values
- use the `bitwise_and()` to get the result and then stack all the frames on one window.
- Create a loop for the frames to show in real time since the frames are coming from the webcam.

```
def objectTracking():
    capture = cv2.VideoCapture(0)
    while True:
        _, image = capture.read()
        imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # define range of blue color in HSV
        l_v = cv2.getTrackbarPos("V_MIN","Object Tracking" )
        u_v = cv2.getTrackbarPos("V_MAX", "Object Tracking")
        l_s = cv2.getTrackbarPos("S_MIN", "Object Tracking")
        u_s = cv2.getTrackbarPos("S_MAX", "Object Tracking")
        l_h = cv2.getTrackbarPos("H_MIN", "Object Tracking")
        u_h = cv2.getTrackbarPos("H_MAX", "Object Tracking")
        print(l_h, l_s, l_v, u_h, u_s, u_v)

        lower = np.array([l_h, l_s, l_v])
        upper = np.array([u_h, u_s, u_v])
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(imageHSV, lower, upper)
        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(image, image, mask=mask)
        finalImage = stackImages(0.5, [[image, imageHSV, mask, res ]])
        cv2.imshow("Object Tracking", finalImage)
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break
    return
objectTracking()
```

### Finding the `HSV` color space of any color.

This is very simple all you need to know is the `BGR` of the color you want it's HVS. For example let's say we want to find the `HSV` color space of the color `Green` We can do it as follows:

```
def bgr2HSV(bgr):
    a, b, c = bgr
    color = np.uint8([[[a, b, c]]])
    hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
    return hsv
print(bgr2HSV((0, 255, 0)))

```

The function that we have created converts the given color to `hsv` from `bgr`. So now we can take [H-10, 100,100] and [H+10, 255, 255] as lower bound and upper bound respectively.

### 6. Image Thresholding

The function used is cv2.threshold. First argument is the source image, which should be a gray scale image. Second argument is the threshold value which is used to classify the pixel values. Third argument is the maxVal which represents the value to be given if pixel value is more than (sometimes less than) the threshold value. OpenCV provides different styles of thresholding and it is decided by the fourth parameter of the function. Different types are:

- cv2.THRESH_BINARY
- cv2.THRESH_BINARY_INV
- cv2.THRESH_TRUNC
- cv2.THRESH_TOZERO
- cv2.THRESH_TOZERO_INV

The following function applies threshold with different threshold types and show the images using the stackImage function.

```
from stackedImages import stackImages

def threshold():
    image = cv2.imread("cup.png")

    ret,thresh_binary = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
    ret,thresh_binary_inv = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
    ret,thresh_trunc = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
    ret,thresh_tozero = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
    ret,thresh_tozero_inv = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)
    thresholdImages = stackImages(.4, [
        [image, thresh_binary, thresh_binary_inv],
         [thresh_trunc, thresh_tozero, thresh_tozero_inv],])
    cv2.imshow("Image", thresholdImages)
    cv2.waitKey(0)

    return cv2.destroyAllWindows()
threshold()
```

### 7. Geometric Transformations of Images

#### Transformations

OpenCV provides two transformation functions, `cv2.warpAffine` and `cv2.warpPerspective`, with which you can have
all kinds of transformations. `cv2.warpAffine` takes a `2x3` transformation matrix while `cv2.warpPerspective` takes a
`3x3` transformation matrix as input.

#### Scaling

Scaling is just resizing of the image. OpenCV comes with a function `cv2.resize()` for this purpose. The size of
the image can be specified manually, or you can specify the scaling factor. Different interpolation methods are
used. Preferable interpolation methods are `cv2.INTER_AREA` for shrinking and `cv2.INTER_CUBIC` (slow) &
`cv2.INTER_LINEAR` for zooming. By default, interpolation method used is `cv2.INTER_LINEAR` for all resizing
purposes.

##### a. Resizing the image and getting the image shape

As we all know that an image is an array of pixels, then to get the shape of the image we use the `npArray.shape` where `npArray` is a `numpy` array. In our case it will be the image. So the npArray will return a turple of values `(width, height, number_of_channels=3)`. Let's try to get the shape of our cup image and print them on the screen.

```
def imageShape(image):
    return image.shape
image = cv2.imread("cup.png")
print("THE Shape OF THE IMAGE IS: ", imageShape(image))
```

##### b. Changing the image dimensions [Image Scale]

Scaling an image means we are changing the pixel width and height of the image. Let's Create a function that takes an image as it's argument and then resize the image for us. We also want to check the size of the resized image and also show the resized image on the window.

```
def changeSizeOfImage(image, dimensions):
    return cv2.resize(image, dimensions)
image = cv2.imread("cup.png")
print(image.shape)
resizedImage = changeSizeOfImage(image, (200, 200))
print(resizedImage.shape)
cv2.imshow("Resized Image", resizedImage)
cv2.imshow("Original Image", image)
cv2.waitKey(0)
```

You can always pass `interpolation` as a keyword argument. For example:

```
cv2.resize(image, (300, 300), interpolation=cv2.INTER_CUBIC)
```

The default interpolation is `cv2.INTER_LINEAR`. The lists of interpolations values includes:

<<<<<<< HEAD

- [x] # cv2.INTER\*LINEAR \*\*\*(Default)\_\*\*
- [x] cv2.INTER\*LINEAR \*\*\*(Default)\_\*\*
  > > > > > > > 7d5605efee0f6a2f125135229caf69e5c03ed5ee
- [ ] cv2.INTER_CUBIC
- [ ] cv2.INTER_AREA

##### Translation

Translation is the shifting of object’s location. You can take make it into a `numpy` array of type np.float32 and pass it into cv2.warpAffine() function. Having knowing the values of `x, y` we can create a matrix that will allow us to shift our images interms of `x & y` values. The matrix is generally created as a **`np.float32()`** array as follows:

```
Matrix = np.float32([
    [1, 0, x],
    [0, 1, y]
])
```

Let's say we want to shift our image with `(100, 10)`:

```
# Read an image as a grayscale image
image = cv2.imread("cup.png", 0)
rows, cols = image.shape
x, y = 100, 10
matrix = np.float32([
    [1, 0, x], [0, 1, y]
])
image = cv2.warpAffine(image, matrix, (rows, cols))
cv2.imshow("Original Image", image)
cv2.waitKey(0)
```

Third argument of the cv2.warpAffine() function is the size of the output image, which should be in
the form of (width, height). Remember width = number of columns, and height = number of rows. We have shifted the image `10` units top and `100` units right

##### Rotation

Rotation of an image for an angle 𝜃 is achieved by the transformation matrix of the form.

```
matrix = [
    [cos𝜃, -sin𝜃],
    [sin𝜃, cos𝜃]
]
```

##### a) cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)

Let's say we want to add an `rotate` an image `90 degrees`:

```
# Read an image as a grayscale image
image = cv2.imread("cup.png", 0)
rows, cols = image.shape
x, y = 100, 10
angle = 90
matrix = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
image = cv2.warpAffine(image,matrix,(cols,rows))
image = cv2.warpAffine(image, matrix, (rows, cols))
cv2.imshow("Original Image", image)

cv2.waitKey(0)
```

##### b) `cv2.getAffineTransform(pts1,pts2)`

In affine transformation, all parallel lines in the original image will still be parallel in the output image.

```
# Read an image as a grayscale image
image = cv2.imread("cup.png", 0)
rows, cols = image.shape
x, y = 100, 10
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
matrix = cv2.getAffineTransform(pts1,pts2)
image = cv2.warpAffine(image,matrix,(cols,rows))
cv2.imshow("Original Image", image)
cv2.waitKey(0)
```

##### c) Perspective Transformation

For perspective transformation, you need a `3x3` transformation matrix. Straight lines will remain straight even after
the transformation. To find this transformation matrix, you need 4 points on the input image and corresponding points
on the output image. Among these 4 points, 3 of them should not be collinear. Then transformation matrix can be
found by the function `cv2.getPerspectiveTransform`. Then apply `cv2.warpPerspective` with this `3x3` transformation
matrix.

Suppose we have an image called `cards.png` and we want to extract one of the card on the image. We can do it as follows.

#### step 1:

Grab the point's of region of interest using the mouse vent in openCV and hardly insert them into two arrays.

```
def mouseEvent(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
while 1:
    image = cv2.imread("cards.png", 0)
    cv2.setMouseCallback('Original Image',mouseEvent)
    cv2.imshow("Original Image", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
## Click the region you want to get the points on the image and copy the values from the console and insert them in array like
# pt1 = np.float32([[284 ,13], [407, 84], [178, 189], [301, 262]])
# pt2 = np.float32([[0, 0], [417, 0], [0, 307], [417, 307]])
```

#### step 2:

Now we have the points we can use the functions to extract the image we want from the `card.png` image.

```
pt1 = np.float32([[284 ,13], [407, 84], [178, 189], [301, 262]])
pt2 = np.float32([[0, 0], [417, 0], [0, 307], [417, 307]])
image = cv2.imread("cards.png", 0)
cv2.imshow("Original", image)
matrix = cv2.getPerspectiveTransform(pt1, pt2)
image = cv2.warpPerspective(image,matrix,image.shape)
cv2.imshow("Wrap Perspective", image)
cv2.waitKey(0)
```

### Image Gradients

- Laplacian
- Sobel

#### 1. Laplacian Gradient

> Code Example:

```
# Read an image in grayscale
img = cv2.imread('avatar.jpg', 0)
# Apply Laplacian gradient
laplacian = cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow("Image Laplacian",laplacian)
cv2.waitKey(0)
```

#### 2. Sobel Gradient

> Example with all the directions xorder and yorder

###### xorder

```
# Read an image in grayscale
img = cv2.imread('avatar.jpg', 0)
# Sobel Gradient
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
cv2.imshow("Image sobelx",sobelx)
cv2.waitKey(0)
```

###### yorder

```
# Read an image in grayscale
img = cv2.imread('avatar.jpg', 0)
# Sobel Gradient
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
cv2.imshow("Image sobely",sobely)
cv2.waitKey(0)
```

### Canny Edge Detection

Canny Edge Detection is a popular edge detection algorithm. It was developed by John F. Canny in 1986.

> Example:

```
img = cv2.imread('avatar.jpg')
imageGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imageCanny = cv2.Canny(imageGray, 100, 200)

images = stackImages(1, [img, imageGray, imageCanny])
cv2.imshow("Image", images)
cv2.waitKey(0)
```

#### Image Pyramids

Normally, we used to work with an image of constant size. But in some occassions, we need to work with images
of different resolution of the same image. For example, while searching for something in an image, like face, we are
not sure at what size the object will be present in the image. In that case, we will need to create a set of images with
different resolution and search for object in all the images. These set of images with different resolution are called
Image Pyramids (because when they are kept in a stack with biggest image at bottom and smallest image at top look
like a pyramid).
There are two kinds of Image Pyramids.

1. Gaussian Pyramid
   - cv2.pyrDown()
   - cv2.pyrUp()
2. Laplacian Pyramids

#### 1. Gaussian pyramid

> Example of cv2.pyrDown() Lower resolution

```
img = cv2.imread('avatar.jpg')
lower_reso = cv2.pyrDown(img)
cv2.imshow("Image", lower_reso)
cv2.waitKey(0)
```

> Example of cv2.pyrUp() Upper resolution

```
img = cv2.imread('avatar.jpg')
upper_reso = cv2.pyrUp(img)
cv2.imshow("Image", upper_reso)
cv2.waitKey(0)
```

#### 2. Laplacian Pyramids

Laplacian Pyramids are formed from the Gaussian Pyramids. There is no exclusive function for that. Laplacian
pyramid images are like edge images only. Most of its elements are zeros. They are used in image compression. A
level in Laplacian Pyramid is formed by the difference between that level in Gaussian Pyramid and expanded version
of its upper level in Gaussian Pyramid. The three levels of a Laplacian level will look like below (contrast is adjusted
to enhance the contents):

> Example of cv2.pyrDown() Lower resolution

```
img = cv2.imread('avatar.jpg', 0)
laplacian = cv2.Laplacian(img, cv2.CV_64F)
lower_reso = cv2.pyrDown(laplacian)
cv2.imshow("Image", lower_reso)
cv2.waitKey(0)
```

> Example of cv2.pyrUp() Upper resolution

```
img = cv2.imread('avatar.jpg', 0)
laplacian = cv2.Laplacian(img, cv2.CV_64F)
upper_reso = cv2.pyrUp(laplacian)
cv2.imshow("Image", upper_reso)
cv2.waitKey(0)
```

#### Image Blending using Pyramids

One application of Pyramids is Image Blending. For example, in image stitching, you will need to stack two images
together, but it may not look good due to discontinuities between images. In that case, image blending with Pyramids
gives you seamless blending without leaving much data in the images.

> Example: Is in the notes on page: 84

## Contours in OpenCV

### What are contours?

Contours can be explained simply as a curve joining all the continuous points (along the boundary), having same color
or intensity. The contours are a useful tool for shape analysis and object detection and recognition.

- For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection.
- findContours function modifies the source image. So if you want source image even after finding contours,
  already store it to some other variables.
- In OpenCV, finding contours is like finding white object from black background. So remember, object to be
  found should be white and background should be black.

> Example: Finding te contours on the image called `shapes.jpg`

```
# 1. Read the image
image = cv2.imread("shapes.jpg")

# 2. Convert the image to grayscale
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. apply the threshhold or Canny to the image
# ret,imageThreshHold = cv2.threshold(imageGray,127,255,cv2.THRESH_BINARY)
imgBlur = cv2.GaussianBlur(imageGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)

# 4. Find and print the contours
contours, hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    print(cnt)

# Draw the contours on the image in yellow

image = cv2.drawContours(image, contours, -1, (255, 255, 0), 5)
plt.imshow(image)
plt.show()
```

### 1. Moments

Image moments help you to calculate some features like center of mass of the object, area of the object etc
The function `cv2.moments()` gives a dictionary of all moment values calculated.

> Example:
> We want to get the moment values of the image `shapes.jpg`

```
# Read the image in gray scale
image = cv2.imread('shapes.jpg', 0)
#  Blur teh image
imgBlur = cv2.GaussianBlur(imageGray, (7,7), 1)
# apply canny edge detection to the image
imgCanny = cv2.Canny(imgBlur, 50, 50)
# Display the image Canny
plt.imshow(imgCanny)
plt.show()
# find the contours from the image
contours, hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Get the moments of all contours and print them
for cnt in contours:
    M = cv2.moments(cnt)
    print(M)
```

### 2. Contour Area

```
area = cv2.contourArea(cnt)
```

> Example we want to find the contour area of each contour detected from our previous example:

```
# Read the image in gray scale
image = cv2.imread('shapes.jpg', 0)
#  Blur teh image
imgBlur = cv2.GaussianBlur(imageGray, (7,7), 1)
# apply canny edge detection to the image
imgCanny = cv2.Canny(imgBlur, 50, 50)
# Display the image Canny
plt.imshow(imgCanny)
plt.show()
# find the contours from the image
contours, hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Get the Area of all contours and print them
for cnt in contours:
    A = cv2.contourArea(cnt)
    print(A)
```

### 3. Contour Perimeter

It is also called arc length. It can be found out using cv2.arcLength() function. Second argument specify whether
shape is a closed contour (if passed True), or just a curve.

```
perimeter = cv2.arcLength(cnt,True)
```

> Example

```
# Read the image in gray scale
image = cv2.imread('shapes.jpg', 0)
#  Blur teh image
imgBlur = cv2.GaussianBlur(imageGray, (7,7), 1)
# apply canny edge detection to the image
imgCanny = cv2.Canny(imgBlur, 50, 50)
# Display the image Canny
plt.imshow(imgCanny)
plt.show()
# find the contours from the image
contours, hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Get the Perimeter of all contours and print them
for cnt in contours:
    P = cv2.arcLength(cnt, True)
    print(P)
```

### 4. Contour Approximation

It approximates a contour shape to another shape with less number of vertices depending upon the precision we specify.
It is an implementation of Douglas-Peucker algorithm. Check the wikipedia page for algorithm and demonstration.
To understand this, suppose you are trying to find a square in an image, but due to some problems in the image, you
didn’t get a perfect square, but a “bad shape” (As shown in first image below). Now you can use this function to
approximate the shape. In this, second argument is called epsilon, which is maximum distance from contour to
approximated contour. It is an accuracy parameter. A wise selection of epsilon is needed to get the correct output.

```
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
```

Third argument specifies whether curve is closed or not.

> Example: Let's say we want to approximate contours from our image from the previous examples for each cnt we can do it as follows:

```
# Read the image in gray scale
image = cv2.imread('shapes.jpg', 0)
#  Blur teh image
imgBlur = cv2.GaussianBlur(imageGray, (7,7), 1)
# apply canny edge detection to the image
imgCanny = cv2.Canny(imgBlur, 50, 50)
# Display the image Canny
plt.imshow(imgCanny)
plt.show()
# find the contours from the image
contours, hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    A = cv2.arcLength(cnt, True)
    epsilon = 0.1 * A
    CA = cv2.approxPolyDP(cnt,epsilon,True)
    print(CA)
```

### 5. Convex Hull

Theory: Convex Hull will look similar to contour approximation, but it is not (Both may provide same results in some cases).
Here, cv2.convexHull() function checks a curve for convexity defects and corrects it. Generally speaking, convex
curves are the curves which are always bulged out, or at-least flat. And if it is bulged inside, it is called convexity
defects. For example, check the below image of hand. Red line shows the convex hull of hand. The double-sided
arrow marks shows the convexity defects, which are the local maximum deviations of hull from contours.

```
....
for cnt in contours:
    hull = cv2.convexHull(cnt)
    print(hull)

```

### 6. Checking Convexity

There is a function to check if a curve is convex or not, cv2.isContourConvex(). It just return whether True or False.
Not a big deal.

> Example

```
for cnt in contours:
    k = cv2.isContourConvex(cnt)
    print(k)
```

### 7. Bounding Rectangle

There are two types of bounding rectangles.

#### a) Straight Bounding Rectangle

We want to get the bounding rectangle for each and every contour detected.

```
x,y,w,h = cv2.boundingRect(cnt)
```

> Example

```
for cnt in contours:
    rect = cv2.boundingRect(cnt)
    print(rect) # returns a turple of (x, y, w, h)
```

#### b) Rotated Rectangle

Here, bounding rectangle is drawn with minimum area, so it considers the rotation also. The function used is
cv2.minAreaRect(). It returns a Box2D structure which contains following detals - ( top-left corner(x,y), (width,
height), angle of rotation ).

```
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
```

> Example

```
for cnt in contours:
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    print(box)

```

#### 8. Minimum Enclosing Circle

Next we find the circumcircle of an object using the function cv2.minEnclosingCircle(). It is a circle which completely covers the object with minimum area

```
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
```

> Example

```
for cnt in contours:
    enclosingCicle= cv2.minEnclosingCircle(cnt)
    print(enclosingCicle)
```

#### 9. Fitting an Ellipse

```
ellipse = cv2.fitEllipse(cnt)
im = cv2.ellipse(im,ellipse,(0,255,0),2)
```

> Example:

```
## points for drawing an ellipse around an object
for cnt in contours:
    ellipse = cv2.fitEllipse(cnt)
    print(ellipse)
```

#### 10. Fitting a Line

Similarly we can fit a line to a set of points. Below image contains a set of white points. We can approximate a straight
line to it.

```
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)

```

> Example

```
for cnt in contours:
    rows,cols = image.shape[:2]
    [vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
    lefty = int((-x*vy/vx) + y)
    righty = int(((cols-x)*vy/vx)+y)
    image = cv2.line(image,(cols-1,righty),(0,lefty),(0,255,0),2)

plt.imshow(image)
plt.show()
```

## Contour Properties

We will learn to extract some frequently used properties of objects like Solidity, Equivalent Diameter, Mask
image, Mean Intensity etc.

> First things first we want to create a black image and draw a green rectangle inside it, then detect some contours on the black image.

#### Image creation and contour detection

##### 1. Image Creation and displaying

```
rect = np.zeros([512, 512, 3], dtype=np.uint8)
rec = cv2.rectangle(rect, (50, 100), (450, 350), (0, 255, 0), 3)

plt.imshow(rect)
cv2.imwrite("rect.png", rect)
plt.show()
print("THE IMAGE WAS SAVED")

# Displaying the created image
rectImg = cv2.imread('rect.png')
plt.imshow(rectImg)
plt.show()
```

##### 2. Convert image to gray scale

```
imgGray = cv2.cvtColor(rectImg, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Imag", imgGray)
cv2.waitKey(0)
```

##### 3. Apply the canny to the image

```
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
plt.imshow(imgCanny)
plt.show()
```

##### 4. Detect the contours on the image

```
contours, hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    print(cnt)
```

## 1. Aspect Ratio

It is the ratio of width to height of bounding rect of the object, found as

```
𝐴𝑠𝑝𝑒𝑐𝑡 𝑅𝑎𝑡𝑖𝑜 = width/height

```

The following example shows how to calculate the aspect ratio of of our rectangle that is on the image.

```
cnt = contours[0]
x, y, w, h = cv2.boundingRect(cnt)
aspectRatio = float(w)/h
aspectRatio
```

## 2. Extent

Extent is the ratio of contour area to bounding rectangle area, found as

```
𝐸𝑥𝑡𝑒𝑛𝑡 = 𝑂𝑏𝑗𝑒𝑐𝑡 𝐴𝑟𝑒𝑎/𝐵𝑜𝑢𝑛𝑑𝑖𝑛𝑔 𝑅𝑒𝑐𝑡𝑎𝑛𝑔𝑙𝑒 𝐴𝑟𝑒
```

> Example:

```
contour_area = cv2.contourArea(cnt)
bounding_area = w*h

extent = float(contour_area)/bounding_area
extent
```

## 3. Solidity

Solidity is the ratio of contour area to its convex hull area found as

```
𝑆𝑜𝑙𝑖𝑑𝑖𝑡𝑦 = 𝐶𝑜𝑛𝑡𝑜𝑢𝑟 𝐴𝑟𝑒𝑎/𝐶𝑜𝑛𝑣𝑒𝑥 𝐻𝑢𝑙𝑙 𝐴𝑟𝑒
```

> Example:

```
contour_area = cv2.contourArea(cnt)
hull_area = cv2.convexHull(cnt)

solidity = float(contour_area)/hull_area
solidity
```

## 4. Equivalent Diameter

Equivalent Diameter is the diameter of the circle whose area is same as the contour area, found

```
𝐸𝑞𝑢𝑖𝑣𝑎𝑙𝑒𝑛𝑡 𝐷𝑖𝑎𝑚𝑒𝑡𝑒 = squareRoot((4*ContourArea)/ pi)
```

> Example

```
contour_area = cv2.contourArea(cnt)

eqi_diameter = np.sqrt(contour_area/np.pi)
eqi_diameter
```

## 5. Orientation

Orientation is the angle at which object is directed. Following method also gives the Major Axis and Minor Axis
lengths.

> Example

```
(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)
```

## 6. Mask and Pixel Points

In some cases, we may need all the points which comprises that object. It can be done as follows:

> Example

```
# mask = np.zeros(imgray.shape,np.uint8)
maskImage = np.zeros_like(imgGray, dtype=np.uint8)
finalMask = cv2.drawContours(maskImage,[cnt],0,255,-1)

# We want to display all the images transforamtions

allTransfomations= np.hstack([imgGray,maskImage,  finalMask])
plt.imshow(allTransfomations)

pixelpoints = np.transpose(np.nonzero(finalMask))
pixelpoints
```

> Here, two methods, one using Numpy functions, next one using OpenCV function (last commented line) are given to do the same. Results are also same, but with a slight difference. Numpy gives coordinates in (row, column) format, while OpenCV gives coordinates in (x,y) format. So basically the answers will be interchanged. Note that, row = x and column = y.

## 7. Maximum Value, Minimum Value and their locations

We can find these parameters using a mask image.

> Example

```
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(imgGray,mask = finalMask)
print(min_val, max_val, min_loc, max_loc)
```

## 8. Mean Color or Mean Intensity

Here, we can find the average color of an object. Or it can be average intensity of the object in grayscale mode. We
again use the same mask to do it.

> Example:

```
mean_val = cv2.mean(imgGray,mask = finalMask)
mean_val
```

## 9. Extreme Points

Extreme Points means topmost, bottommost, rightmost and leftmost points of the object.

> Example

```
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

print(leftmost, rightmost, topmost, bottommost)
```

# More functions

## 1. Convexity Defects

OpenCV comes with a ready-made function to find this, `cv2.convexityDefects()`.

> Example

```
hull = cv2.convexHull(cnt,returnPoints = False)
defects = cv2.convexityDefects(cnt,hull)
defects
```

> It returns an array where each row contains these values - [ start point, end point, farthest point, approximate distance to farthest point ]. We can visualize it using an image. We draw a line joining start point and end point, then draw a circle at the farthest point.

## 2. Point Polygon Test

This function finds the shortest distance between a point in the image and a contour. It returns the distance which is
negative when point is outside the contour, positive when point is inside and zero if point is on the contour.

- In the function, third argument is measureDist. If it is True, it finds the signed distance. If False, it finds
  whether the point is inside or outside or on the contour (it returns +1, -1, 0 respectively).

> Example:

```
dist = cv2.pointPolygonTest(cnt,(50,50),False)
dist # -1.0
```

## 3. Match Shapes

OpenCV comes with a function cv2.matchShapes() which enables us to compare two shapes, or two contours and
returns a metric showing the similarity. The lower the result, the better match it is. It is calculated based on the
hu-moment values. Different measurement methods are explained in the docs.

> Example:

> For the full example open the `main.ipynb` file

- Detect the contours of the shapes you want to match
- Pass the contours to the `cv2.matchShapes()` function
  - if the result is 0 then the shapes matches otherwise they dont

```
ret = cv2.matchShapes(squareCnt,squareCnt,1,0.0)
print(ret)
ret = cv2.matchShapes(star1Cnt, star2Cnt, 1, 0.0)
ret
```

### Contours Hierarchy

> Read the docs
>
> ## FROM NOW ON THE EXAMPLES WILL BE IN THE `main.ipynb`

# Histograms

You can consider histogram as a graph or plot, which gives you an overall idea about the
intensity distribution of an image. It is a plot with pixel values (ranging from 0 to 255, not always) in X-axis and
corresponding number of pixels in the image on Y-axis

## Find Histogram

Before using those functions, we need to understand some terminologies related with
histograms.

- **BINS**
  - The above histogram shows the number of pixels for every pixel value, ie from 0 to 255. ie you need 256 values to show the above histogram. But consider, what if you need not find the number of pixels for all pixel values separately, but number of pixels in a interval of pixel values? say for example, you need to find the number of pixels lying between 0 to 15, then 16 to 31, ..., 240 to 255. You will need only 16 values to represent the histogram. And that is what is shown in example given in OpenCV Tutorials on histograms. So what you do is simply split the whole histogram to 16 sub-parts and value of each sub-part is the sum of all pixel count in it. This each sub-part is called “BIN”. In first case, number of bins where 256 (one for each pixel) while in second case, it is only 16. BINS is represented by the term histSize in OpenCV docs.
- **DIMS**
  - It is the number of parameters for which we collect the data. In this case, we collect data regarding only one thing, intensity value. So here it is 1.
- **RANGE**
  - It is the range of intensity values you want to measure. Normally, it is [0,256], ie all intensity values.
