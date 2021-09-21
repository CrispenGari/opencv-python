

try:
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.stats import linregress
except ImportError as e:
    from pip._internal import main as install
    packages = ["numpy", "opencv-python", "matplotlib", "scipy"]
    for package in packages:
        install(["install", package])
finally:
    pass


