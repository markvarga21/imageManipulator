from PIL import ImageEnhance, ImageFilter

from util.cleaner_service import delete_temp_files
from util.temp_file_creator import return_temp_file


def get_retouch_image_file(pillow_img, retouch_type, new_value):
    delete_temp_files('.jpeg')
    if retouch_type == 'brightness':
        enhancer = ImageEnhance.Brightness(pillow_img)
    elif retouch_type == 'contrast':
        enhancer = ImageEnhance.Contrast(pillow_img)
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
    enhancer.enhance(new_value).save(temp_file)
    return temp_file

