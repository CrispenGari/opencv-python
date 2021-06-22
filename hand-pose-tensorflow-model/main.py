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
