import torch
from PIL import Image
import numpy as np
import cv2 as cv

def apply_padding(image, padding):
    """Add padding to the image and save it."""
    top, bottom, left, right = padding
    return cv.copyMakeBorder(image, top, bottom, left, right, cv.BORDER_CONSTANT, value=[255, 255, 255])

   