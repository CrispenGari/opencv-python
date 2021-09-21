

# Color-Palette
This is a simple application that uses trackbars to and change the color of the numpy black image to the relative BGR values from trackbars

## Demo
![alt-text](https://github.com/CrispenGari/Open-Computer-Vision-Chapter-11-Color-Pallate-TrackBars/blob/main/bandicam%202021-01-24%2023-42-53-148.jpg)

## This application is using
* opencv-python
* numpy

## 1. Create a Named window and Create track bars on that named window

* Create a named window using a function `cv2.namedWindow`
* create a numpy black image

```

image = np.zeros((200, 512, 3), np.uint8)

cv2.namedWindow("Colors")
cv2.createTrackbar("ONN: 1\n OFF: 0", "Colors", 0, 1, empty)
cv2.createTrackbar("B", "Colors", 0, 255, empty)
cv2.createTrackbar("G", "Colors", 0, 255, empty)
cv2.createTrackbar("R", "Colors", 0, 255, empty)
```

## 2. Show images in a loop
* Display the image on the same window with trackbars
* get the trackbar position values
* if the switch is 1 change the image BGR value
```

def showImage():
    while True:
        cv2.imshow("Colors", image)
        blue = cv2.getTrackbarPos("B", "Colors")
        green = cv2.getTrackbarPos("G", "Colors")
        red = cv2.getTrackbarPos("R", "Colors")
        switch = cv2.getTrackbarPos("ONN: 1\n OFF: 0", "Colors")
        # print(blue, green, red, switch)

        if switch == 1:
            image[:] = (blue, green, red)
        else:
            image[:] = (0,0,0)
        cv2.waitKey(1)
showImage()
```

Thats all

## What's Next?
* Arithmetic operation on images

[Next]() || [Previous]()
