import torch
from PIL import Image
import numpy as np
import cv2 as cv
def find_contours(thresh):
    """Detect contours in the thresholded image and then find the largest among them"""
    contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    if not contours:  # Add check if no contours found
        return None 
    max_height = 0
    bounding_rect = None
    for cnt in contours:
        x, y, w, h = cv.boundingRect(cnt)
        if h > max_height:
            max_height = h
            bounding_rect = (x, y, w, h)
    return bounding_rect
