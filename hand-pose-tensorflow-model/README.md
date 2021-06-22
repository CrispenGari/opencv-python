## Hand Pose.
We will predict hand `poses` using a model that I have trained in this [notebook](https://github.com/CrispenGari/Computer-Vision-In-TensorFlow/tree/main/01_Classification/04_Hand_Gasture) using tensorflow 2.0.

<p align="center">
<img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
<img src="https://img.shields.io/static/v1?label=package&message=opencv&color=yellow"/>
<img src="https://img.shields.io/static/v1?label=package&message=numpy&color=blue"/>
<img src="https://img.shields.io/static/v1?label=package&message=tensorflow&color=yellow"/>
</p>

The following code will make predictions on the images that are located in the `testing` folder.

````python
import tensorflow as tf
from tensorflow import keras
import cv2
import numpy as np, os
model = keras.models.load_model('model/hand-gestures.h5')
def predictClass(frame, path):
    resized_image = cv2.resize(frame, (96, 96))
    resized_image = np.reshape(resized_image, (-1, 96, 96, 1)).astype('float32') / 255.
    classes = {'Blank': 0, 'Fist': 1, 'Five': 2, 'ThumbsUp': 3, 'Two': 4, 'Yo': 5}
    classes_reversed = dict([(v, k) for (k, v) in classes.items()])
    predictions = tf.squeeze(tf.argmax(model(resized_image), axis=1)).numpy()
    print(f"IMAGE PATH: \t{path}\nPREDICTED CLASS: \t{predictions}\nLABEL CLASS: \t{classes_reversed[predictions]}")

base_dir = 'testing'
image_paths = [i for i in os.listdir(base_dir)]
for path in image_paths:
    image = cv2.imread(os.path.join(base_dir, path), cv2.IMREAD_UNCHANGED)
    predictClass(image, path)
    print('-----------------------------------')
````