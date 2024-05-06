import torch
from PIL import Image
import numpy as np


def tensor_to_image(tensor: torch.Tensor) -> Image:
    # Remove batch dimension and correct color channel ordering
    image = tensor.squeeze(0).permute(1, 2, 0)
    # Rescale to [0, 255] and convert to uint8
    image = (image.numpy() * 255).clip(0, 255).astype(np.uint8)
    if image.shape[2] == 1:  # Grayscale
        image = image.squeeze()  # Remove channel
    return Image.fromarray(image, 'RGBA' if image.shape[-1] == 4 else 'RGB')