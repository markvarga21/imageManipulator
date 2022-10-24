from PIL import ImageEnhance, ImageFilter

from util.cleaner_service import delete_temp_files
from util.temp_file_creator import return_temp_file
from util.validator import get_error_image_file, validate_new_value_for_retouch_type
from util.value_mapper import map_contrast_value_to_pillow_value


def get_retouch_image_file(pillow_img, retouch_type, new_value):
    delete_temp_files('.jpeg')
    mapped_value = -999
    if retouch_type == 'brightness':
        enhancer = ImageEnhance.Brightness(pillow_img)
    elif retouch_type == 'contrast':
        if not validate_new_value_for_retouch_type(retouch_type=retouch_type, new_value=new_value):
            error_message = f'Invalid {retouch_type} value: {new_value}\nValid range: [-10.0, 10.0]'
            return get_error_image_file(error_message)
        enhancer = ImageEnhance.Contrast(pillow_img)
        mapped_value = map_contrast_value_to_pillow_value(new_value)
    elif retouch_type == 'color':
        enhancer = ImageEnhance.Color(pillow_img)
    elif retouch_type == 'sharpness':
        enhancer = ImageEnhance.Sharpness(pillow_img)
    elif retouch_type == 'blur':
        blured_image = pillow_img.filter(ImageFilter.GaussianBlur(new_value))
        temp_file = return_temp_file('.jpeg')
        blured_image.save(temp_file)
        return temp_file
    else:
        return f'Type {retouch_type} not recognised!'
    temp_file = return_temp_file('.jpeg')
    enhancer.enhance(mapped_value).save(temp_file)
    return temp_file


def retouch_image_all_in_one(pillow_image, values):
    brightness_value = values['brightness']
    contrast_value = values['contrast']
    color_value = values['color']
    sharpness_value = values['sharpness']
    blur_value = values['blur']



