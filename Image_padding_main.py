from .utils.tensor_to_image import tensor_to_image
from .utils.convert_to_grayscale import convert_to_grayscale
from .utils.apply_threshold import apply_threshold
from .utils.find_contours import find_contours
from .utils.calculate_padding import calculate_padding
from .utils.apply_padding import apply_padding
from .utils.image_to_tensor import image_to_tensor



class ImagePadding:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }
    CATEGORY = "SmartPaddingxp/image"
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "image_padding"


    def image_padding(self, image):
        image_pil = tensor_to_image(image)
        gray_image, image_np = convert_to_grayscale(image_pil)
        thresh = apply_threshold(gray_image)
        bounding_rect = find_contours(thresh)
        padding = calculate_padding(bounding_rect, gray_image.shape[0], gray_image.shape[1])
        padded_image = apply_padding(image_np, padding)
        image = image_to_tensor(padded_image)
        return (image,)
