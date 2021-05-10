## Plane Shapes
* Computer vision task on plane shapes in real time.
* A plane shape is a flat or two-dimensional shape that is closed. The straight lines that make up the shape are the sides, where the parts where two sides come together are the corners.

<p align="center">
<img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
<img src="https://img.shields.io/static/v1?label=package&message=opencv&color=yellow"/>
<img src="https://img.shields.io/static/v1?label=package&message=numpy&color=blue"/>
<img src="https://img.shields.io/static/v1?label=package&message=math&color=red"/>
</p>

<p align="center">
<img src="https://github.com/CrispenGari/Opencv-Python/blob/main/plainShapes/cover.jpeg" alt="demo" align="center"/>
</p>

### Calculating
* Area 
* Perimeter

### Basic shapes
* Rectangle/Square
````
(x1, y1)
     _________________________
    |                         |
    |                         | (h)     Area        = w * h
    |                         |         Perimeter   = 2*w + 2*h
    |_________________________|
                (w)             (x2, y2)|| (w, h)
````

  
* Circle
### Simple Math
````
            
                . (x1, y1)
                |
                |
                | (x2, y2)
                
                Area        = pi * radius**2
                Perimeter   = 2 * pi * radius
                radius      = sqrt((x1, -x2)**2 + (y1, - y2)**2)
````

* Triangle

### Simple Math
````
                    (x, y)
                        *
                      / | \
                b    /  |   \    c      hc = perpendicular height
                    /   | hc \         hc  = a * b / c 
                   /    |     \       (c) is the base or the longest line
                   ------------
                        a
                Area        =  .5 * base * height
                Perimeter   =   a + b + c
                side        = sqrt((x1, -x2)**2 + (y1, - y2)**2)
````
