from PIL import Image
import numpy as np
import cv2


def convert_string_to_pillow_image(image_str: str) -> Image:
    file_bytes = np.fromstring(image_str, np.uint8)
    decoded_image = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)
    converted_image = cv2.cvtColor(decoded_image, cv2.COLOR_BGR2RGB)
    pillow_image = Image.fromarray(converted_image)
    return pillow_image


def convert_string_to_cv2_image(image_str: str):
    file_bytes = np.fromstring(image_str, np.uint8)
    decoded_image = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)
    converted_image = cv2.cvtColor(decoded_image, cv2.COLOR_BGR2RGB)
    return converted_image
