
from .Image_padding_main import image_padding


NODE_CLASS_MAPPINGS = {
    "ImagePadding": image_padding,
}
__all__ = ["NODE_CLASS_MAPPINGS"]