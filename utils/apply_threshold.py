import torch
from PIL import Image
import numpy as np
import cv2 as cv

def apply_threshold(gray_image):
    """Apply binary thresholding to the grayscale image."""
    _, thresh = cv.threshold(gray_image, 240, 255, cv.THRESH_BINARY_INV)
    thresh = thresh.astype(np.uint8)
    return thresh