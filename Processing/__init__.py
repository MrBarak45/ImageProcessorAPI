import cv2
import numpy as np

from matplotlib import pyplot as plt
#todo remove matplotlib from venv

import Utilities
import os
from Processing import Filter


def applyGaussianToImage(url, imageName, format):
    e = Utilities.getImageFromUrl(url, imageName, format)
    img = cv2.imread(e)
    blur = cv2.blur(img, (5, 5))
    path = '..\\ProcessedPictures\\' + imageName + '_gaussBlur' + '.' + format
    cv2.imwrite(path, blur)
    return os.getcwd() + '\\' + imageName + '.' + format

def applyGrayscaleToImage(url, imageName, format):
    e = Utilities.getImageFromUrl(url, imageName, format)
    img = cv2.imread(e)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    path = '..\\ProcessedPictures\\' + imageName + '_grayScale' + '.' + format
    cv2.imwrite(path, gray)
    return os.getcwd() + '\\' + imageName + '.' + format

def applyMotionBlurToImage(url, imageName, format, orientation):
    e = Utilities.getImageFromUrl(url, imageName, format)
    img = cv2.imread(e)

    # Specify the kernel size.
    # The greater the size, the more the motion.
    kernel_size = 30

    # Create the vertical kernel.
    kernel_v = np.zeros((kernel_size, kernel_size))

    # Create a copy of the same for creating the horizontal kernel.
    kernel_h = np.copy(kernel_v)

    # Fill the middle row with ones.
    kernel_v[:, int((kernel_size - 1) / 2)] = np.ones(kernel_size)
    kernel_h[int((kernel_size - 1) / 2), :] = np.ones(kernel_size)

    # Normalize.
    kernel_v /= kernel_size
    kernel_h /= kernel_size

    # Apply the vertical kernel.
    vertical_mb = cv2.filter2D(img, -1, kernel_v)

    # Apply the horizontal kernel.
    horizonal_mb = cv2.filter2D(img, -1, kernel_h)

    # Save the outputs.
    cv2.imwrite('car_vertical.jpg', vertical_mb)
    cv2.imwrite('car_horizontal.jpg', horizonal_mb)

