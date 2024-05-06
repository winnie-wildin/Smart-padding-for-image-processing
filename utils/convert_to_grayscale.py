import torch
from PIL import Image
import numpy as np
import cv2 as cv

def convert_to_grayscale(image_pil):
    """Convert an image to grayscale."""
    image_np = np.array(image_pil)
    return cv.cvtColor(image_np, cv.COLOR_BGR2GRAY), image_np