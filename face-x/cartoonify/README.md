# Cartoonify
* Cool operation on images to create 2 cartoons of a given image path
<p align="center">
<img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
<img src="https://img.shields.io/static/v1?label=liked-most&message=opencv&color=yellow"/>
<img src="https://img.shields.io/static/v1?label=liked-most&message=numpy&color=blueviolet"/>
</p>
## Demo
<img src="https://github.com/CrispenGari/Opencv-Python/blob/main/face-x/cartoonify/bandicam%2021-04-13%12-50-43-767.jpg" alt="demo" align="center"/>
### How to do it?
* Read the image
* Convert the image to gray scale
* apply a `medianBlur` to an image
* apply a threshold to a blur image
* apply `biletarelFilter` to an image
    *  > A bilateral filter is a non-linear, edge-preserving, and noise-reducing smoothing filter for images
* use `bitwise_and` on the original image and threshold image


### ``Code``

```

```