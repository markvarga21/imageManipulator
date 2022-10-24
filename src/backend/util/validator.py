from PIL import Image, ImageDraw

from util.cleaner_service import delete_temp_files
from util.temp_file_creator import return_temp_file
from util.value_mapper import CONTRAST_FRONTEND_MIN, CONTRAST_FRONTEND_MAX, COLOR_FRONTEND_MAX, COLOR_FRONTEND_MIN, \
    BRIGHTNESS_FRONTEND_MIN, BRIGHTNESS_FRONTEND_MAX, SHARPNESS_FRONTEND_MIN, SHARPNESS_FRONTEND_MAX, BLUR_FRONTEND_MIN, \
    BLUR_FRONTEND_MAX


def get_error_image_file(title):
    delete_temp_files('.jpeg')
    error_image = Image.open('resources/error.jpeg')
    resized_image = error_image.resize((200, 200))
    rgb_image = resized_image.convert('RGB')
    image_editable = ImageDraw.Draw(rgb_image)
    image_editable.text((15, 15), title, (237, 230, 211))
    temp_file = return_temp_file('.jpeg')
    rgb_image.save(temp_file)
    return temp_file


def validate_new_value_for_retouch_type(retouch_type, new_value):
    if retouch_type == 'contrast':
        if new_value < CONTRAST_FRONTEND_MIN or new_value > CONTRAST_FRONTEND_MAX:
            return False
    if retouch_type == 'color':
        if new_value < COLOR_FRONTEND_MIN or new_value > COLOR_FRONTEND_MAX:
            return False
    if retouch_type == 'brightness':
        if new_value < BRIGHTNESS_FRONTEND_MIN or new_value > BRIGHTNESS_FRONTEND_MAX:
            return False
    if retouch_type == 'sharpness':
        if new_value < SHARPNESS_FRONTEND_MIN or new_value > SHARPNESS_FRONTEND_MAX:
            return False
    if retouch_type == 'blur':
        if new_value < BLUR_FRONTEND_MIN or new_value > BLUR_FRONTEND_MAX:
            return False
    return True
