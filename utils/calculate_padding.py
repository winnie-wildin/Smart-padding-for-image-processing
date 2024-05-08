import torch
from PIL import Image
import numpy as np
import cv2 as cv
def calculate_padding(bounding_rect, image_height, image_width):
    """Calculate and return necessary padding."""
    top = bottom = left = right = 0
    if bounding_rect:
        x1, y1, w, h = bounding_rect
        y3 = y1 + h
        x2 = x1 + w

        th_result = y1 / image_height
        bh_result = (image_height - y3) / image_height
        lw_result = x1 / image_width
        rw_result = (image_width - x2) / image_width

        if th_result < 0.10: top = 200
        if bh_result < 0.10: bottom = 200
        if lw_result < 0.10: left = 200
        if rw_result < 0.10: right = 200

    return top, bottom, left, right